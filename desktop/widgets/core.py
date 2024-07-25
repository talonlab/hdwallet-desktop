#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import os
import json
from typing import (
    Optional, Union
)

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QLayout
)
from PySide6.QtCore import (
    Qt, QEvent, QThreadPool, QSize,
    QRect, QFileSystemWatcher, QObject
)
from PySide6.QtGui import (
    QFontDatabase, QIcon
)

from desktop.utils import (
    put_svg, update_style, resolve_path
)
from desktop.ui.ui_hdwallet import Ui_MainWindow
from desktop.widgets.detached_window import DetachedTerminalWindow

class Application(QMainWindow):
    _instance: Optional['Application'] = None
    ui: Ui_MainWindow = None
    detached_window: DetachedTerminalWindow = None
    fs_watcher: QFileSystemWatcher = None

    def __new__(cls, *args, **kwargs) -> 'Application':
        """
        Create a new instance if not already created, implementing the Singleton pattern.
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """
        Initialize the Application instance if not already initialized.
        """
        if not hasattr(self, 'initialized'):
            super().__init__()
            self.initialize()
            self.initialized = True

    @classmethod
    def instance(cls) -> 'Application':
        """
        Get the singleton instance of the Application.

        :return: The singleton instance of Application.
        """
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def initialize(self) -> None:
        """
        Perform initialization tasks for the application, such as setting up the UI and loading resources.
        """
        QThreadPool.globalInstance().setMaxThreadCount(64)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.detached_window = None

        self.setWindowTitle("Hierarchical Deterministic Wallet")
        self.hdwallet_icon = QIcon(resolve_path("desktop/ui/images/icon/icon.ico"))
        self.setWindowIcon(self.hdwallet_icon)
        css_path = resolve_path("desktop/ui/css/theme.css")
        self.fs_watcher = QFileSystemWatcher([css_path])
        self.fs_watcher.fileChanged.connect(lambda: self.load_stylesheet(css_path))
        self.load_stylesheet(css_path)
        put_svg(
            self.ui.hdwalletLogoHLayout,
            resolve_path("desktop/ui/images/svg/hdwalletLogoFullSize.svg"),
            132.04,
            45
        )
        QFontDatabase.addApplicationFont(resolve_path("desktop/ui/font/HD Wallet-Regular.ttf"))

        self.resize_evt = ResizeEventFilter()
        self.resize_evt.resize_event_callback = self.update_terminal_ui
        self.ui.outputQFrame.installEventFilter(self.resize_evt)
        self.ui.outputTerminalQPlainTextEdit.verticalScrollBar().rangeChanged.connect(self.update_terminal_ui)

    def load_stylesheet(self, path: str) -> None:
        """
        Load and apply a stylesheet from the specified path.

        :param path: The path to the stylesheet file.
        """
        try:
            with open(path, 'r', encoding='utf-8') as style_file:
                stylesheet = style_file.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Failed to load stylesheet: {e}")

    def tab_changed(self, stacked_name: str, page_name: str, button: QWidget, qWidget: QWidget) -> None:
        """
        Handle custom tab changes, updating the active button and changing the displayed page.

        :param stacked_name: The name of the QStackedWidget.
        :param page_name: The name of the page to display.
        :param button: The button widget that was clicked.
        :param qWidget: The parent widget containing the buttons.
        """
        for btn in qWidget.findChildren(QWidget):
            btn.setProperty("Active", "")
            update_style(btn)

        button.setProperty("Active", "true")
        update_style(button)
        self.change_page(stacked_name, page_name)

    def change_page(self, stacked_name: str, widget_name: str) -> None:
        """
        Change the currently displayed page in a QStackedWidget.

        :param stacked_name: The name of the QStackedWidget.
        :param widget_name: The name of the widget to display.
        """
        qStackedWidget: Optional[QStackedWidget] = self.findChild(QStackedWidget, stacked_name)

        if qStackedWidget is None:
            print(f"QStackWidget not found: {stacked_name}")
            return

        qWidget: Optional[QWidget] = qStackedWidget.findChild(QWidget, widget_name)

        if qStackedWidget and qWidget:
            qStackedWidget.setCurrentWidget(qWidget)
        else:
            print(f"ERROR changing page: '{stacked_name}' '{widget_name}'")

    def println(self, s: Union[dict, str, None]) -> None:
        """
        Print a message to the terminal UI.

        :param s: The message to print. Can be a dictionary, string, or None.
        """
        if isinstance(s, dict):
            newtext = json.dumps(s, indent=4, ensure_ascii=False)
        elif s is None:
            return
        else:
            newtext = str(s)
        self.ui.outputTerminalQPlainTextEdit.appendPlainText(f"{newtext}")

    def toggle_expand(self, detach: bool) -> None:
        """
        Toggle the expansion of the terminal window, either detaching it or reattaching it to the main window.

        :param detach: Whether to detach the terminal window.
        """
        if detach:
            self.setMaximumSize(
                self.ui.hdWalletContainerQFrame.width(), self.ui.hdwalletMainQFrame.height()
            )
            self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
            self.showNormal()

            self.layout().removeWidget(self.ui.outputQFrame)
            self.detached_window = DetachedTerminalWindow(self)
            self.detached_window.setWindowTitle("Terminal")
            self.detached_window.setWindowIcon(self.hdwallet_icon)
            self.detached_window.resize(self.ui.outputQFrame.width(), self.ui.outputQFrame.height())
            self.detached_window.setMinimumHeight(self.minimumHeight())

            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self.ui.outputQFrame)

            self.detached_window.setLayout(layout)
            self.detached_window.show()
            self.detached_window.setStyleSheet(self.styleSheet())
            self.setMinimumWidth(0)
            self.detached_window.center_window()

            if not self.isMaximized():
                self.resize(self.width() - self.ui.outputQFrame.width(), self.height())

        else:
            if self.detached_window:
                self.detached_window.close()
                self.detached_window = None

            self.ui.centralwidget.layout().addWidget(self.ui.outputQFrame)


            self.setMaximumSize(16777215, 16777215)
            self.ui.outputQFrame.setGeometry(QRect(
                0, 0, 600, self.ui.outputQFrame.height()
            ))
            self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
            self.show()

    def closeEvent(self, event: QEvent) -> None:
        """
        Handle the close event, ensuring any detached windows are closed.

        :param event: The close event.
        """
        if self.detached_window:
            self.detached_window.close()
        super().closeEvent(event)

    def update_terminal_ui(self) -> None:
        """
        Update the layout of the terminal UI elements.
        """
        self.ui.outputWidgetTopContainerQWidget.setGeometry(QRect(
            (
                self.ui.noLayoutQWidget.width() - (
                    self.ui.outputWidgetTopContainerQFrame.width() + (
                        20 if self.ui.outputTerminalQPlainTextEdit.verticalScrollBar().maximum() > 0 else 10
                    )
                )
            ), 0,
            self.ui.outputWidgetTopContainerQFrame.width(), self.ui.outputWidgetTopContainerQWidget.height()
        ))
        self.ui.outputTerminalQWidget.setGeometry(QRect(
            0, 0, self.ui.noLayoutQWidget.width(), self.ui.noLayoutQWidget.height()
        ))
        self.ui.outputWidgetTopContainerQWidget.raise_()

    def show(self) -> None:
        """
        Override the show method to update the terminal UI when the window is shown.
        """
        super(Application, self).show()
        self.update_terminal_ui()


class ResizeEventFilter(QObject):
    resize_event_callback = None
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Resize:
            if self.resize_event_callback != None:
                self.resize_event_callback()
        return super().eventFilter(obj, event)
