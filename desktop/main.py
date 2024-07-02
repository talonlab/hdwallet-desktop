#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit
import os
import re
import functools
import subprocess

from PySide6.QtCore import (
    QThreadPool, QRegularExpression, Slot
)
from PySide6.QtWidgets import (
    QSizePolicy, QWidget, QPushButton, QLineEdit
)
from PySide6.QtGui import QRegularExpressionValidator

from desktop.widgets.core import *
from desktop.widgets.svg_button import SvgButton
from desktop.widgets.donation import Donation
from desktop.utils.worker import Worker
from desktop.utils.highlighter import Highlighter
from desktop.generate import Generate
from desktop.dumps import Dumps

class MainApplication:
    """
    Main application class for managing the UI and core functionalities.
    """
    def __init__(self) -> None:
        """
        Initialize the MainApplication class.
        """
        super().__init__()

        self.app = Application.instance()
        self.ui = self.app.ui

        self.__init_ui()

    def __init_ui(self) -> None:
        """
        Initialize the UI components and their connections.
        """
        self.ui.toggle_expand_terminal = SvgButton(
            parent_widget=self.ui.expandAndCollapseTerminalQFrame,
            icon_path=os.path.join(os.path.dirname(__file__), "ui/images/all_Icons/expand-white-thin.svg"),
            alt_icon_path=os.path.join(os.path.dirname(__file__), "ui/images/all_Icons/collapse-white-thin.svg"),
            icon_width=20,
            icon_height=20
        )
        self.ui.toggle_expand_terminal.setCheckable(True)
        self.ui.toggle_expand_terminal.toggled.connect(
            lambda: self.app.toggle_expand(
                self.ui.toggle_expand_terminal.isChecked()
            )
        )
        self.ui.outputTerminalQLineEdit.returnPressed.connect(self.process_command)
        self.ui.outputTerminalQPushButton.clicked.connect(self.process_command)
        self.ui.outputTerminalQPlainTextEdit.textChanged.connect(self.app.update_terminal_ui)
        self.ui.clearTerminalQPushButton.clicked.connect(self.ui.outputTerminalQPlainTextEdit.clear)

        self.ui.generateQPushButton.clicked.connect(
            functools.partial(self.generate_dump_tab_changed, "generatePageQStackedWidget", self.ui.generateQPushButton)
        )

        self.ui.dumpQPushButton.clicked.connect(
            functools.partial(self.generate_dump_tab_changed, "dumpsPageQStackedWidget", self.ui.dumpQPushButton)
        )
        self.ui.dumpQPushButton.click()

        self.ui.donationHDWalletQPushButton.clicked.connect(lambda: Donation.show_donation(self.app.window()))

        Highlighter(self.ui.outputTerminalQPlainTextEdit.document())

        self.ui.generateEntropyClientContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.generateSeedMnemonicContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.generateLengthContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        inputs = [
            self.ui.bip44AccountQLineEdit,
            self.ui.bip44AddressQLineEdit,
            self.ui.bip49AccountQLineEdit,
            self.ui.bip49AddressQLineEdit,
            self.ui.bip84AccountQLineEdit,
            self.ui.bip84AddressQLineEdit,
            self.ui.bip86AccountQLineEdit,
            self.ui.bip86AddressQLineEdit,
            self.ui.cip1852AccountQLineEdit,
            self.ui.cip1852AddressQLineEdit,
            self.ui.electrumChangeQLineEdit,
            self.ui.electrumAddressQLineEdit,
            self.ui.moneroMinorQLineEdit,
            self.ui.moneroMajorQLineEdit
        ]
        self.__validate_inputs(inputs)

        self.generate = Generate(self.app)
        self.dumps = Dumps(self.app)

    def __validate_inputs(self, line_edits: list) -> None:
        """
        Validate and filter input fields for line edits.

        :param line_edits: A list of QLineEdit widgets to validate.
        """
        def validate_and_filter(input_string: str) -> Optional[str]:
            pattern = r'^\d-\d(?!-)$'
            return input_string if re.match(pattern, input_string) else None

        @Slot()
        def text_changed_callback(line_edit: QLineEdit) -> None:
            def callback() -> None:
                input_text = line_edit.text()
                filtered_text = validate_and_filter(input_text)
                if filtered_text is None:
                    line_edit.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+-[0-9]+(?!-)")))
                else:
                    line_edit.setValidator(None)

            callback()

        for line_edit in line_edits:
            line_edit.textChanged.connect(text_changed_callback(line_edit))

    def process_command(self) -> None:
        """
        Process the command entered in the terminal input.
        """
        cmd = self.ui.outputTerminalQLineEdit.text()

        def process() -> str:
            f_cmd = cmd if cmd.startswith('hdwallet ') else f"hdwallet {cmd}"

            self.ui.outputTerminalQLineEdit.setText(None)
            result = subprocess.run(
                f_cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            output = result.stderr if result.stderr else result.stdout
            return output.decode()

        if cmd.lower() == 'clear':
            self.ui.outputTerminalQPlainTextEdit.setPlainText(None)
            self.ui.outputTerminalQLineEdit.setText(None)
        else:
            job = Worker(process)
            job.signals.interval_finished.connect(self.app.println)
            QThreadPool.globalInstance().start(job)

    def generate_dump_tab_changed(self, page_name: str, qPushButton: QPushButton) -> None:
        """
        Handle the tab change between generate and dump pages.

        :param page_name: The name of the page to switch to.
        :param qPushButton: The QPushButton that was clicked.
        """
        widget = self.ui.generateAndDumpTabContainerQFrame
        self.app.tab_changed("hdwalletQStackedWidget", page_name, qPushButton, widget)
