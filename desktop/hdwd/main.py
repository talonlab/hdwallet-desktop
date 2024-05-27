import os
import functools
import subprocess

from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QSizePolicy, QWidget, QPushButton

from hdwd.core import *
from hdwd.svg_button import SvgButton
from hdwd.worker import Worker
from hdwd.highlighter import LogHighlighter
from hdwd.donation import Donation
from hdwd.validator import Validator
from hdwd.generate import Generate
from hdwd.dumps import Dumps

class MainApplication():
    def __init__(self):
        super().__init__()

        self.app = Application.instance()
        self.ui = self.app.ui

        self.__init_ui()

    def __init_ui(self):
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

        LogHighlighter(self.ui.outputTerminalQPlainTextEdit.document())

        self.ui.generateEntropyClientContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.generateSeedMnemonicContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.generateLengthContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        vali= [
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
        Validator.validate_input(vali)

        self.generate = Generate(self.app)
        self.dumps = Dumps(self.app)

    def process_command(self):
        cmd = self.ui.outputTerminalQLineEdit.text()
        def process():
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
        widget = self.ui.generateAndDumpTabContainerQFrame
        self.app.widget_changed("hdwalletQStackedWidget", page_name, qPushButton, widget)
