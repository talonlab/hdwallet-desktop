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
    Qt, QEvent, QThreadPool, QSize, QRect
)
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QFontDatabase

from desktop.ui.ui_hdwallet import Ui_MainWindow
from desktop.widgets.detached_window import DetachedTerminalWindow

class Application(QMainWindow):
    _instance: Optional['Application'] = None

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
        self.load_stylesheet(os.path.join(os.path.dirname(__file__), "../ui/css/dark-style.css"))
        put_svg(self.ui.hdwalletLogoHLayout, os.path.join(os.path.dirname(__file__), "../ui/images/11.svg"), 132.04, 45)
        QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), "../ui/font/HD Wallet-Regular.ttf"))

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
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
            self.setMaximumSize(
                self.ui.hdWalletContainerQFrame.width(), self.ui.hdwalletMainQFrame.height()
            )
            self.showNormal()

            self.layout().removeWidget(self.ui.outputQFrame)
            self.detached_window = DetachedTerminalWindow(self)
            self.detached_window.setWindowTitle("Terminal")
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

            self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
            self.setMaximumSize(16777215, 16777215)
            self.ui.outputQFrame.setGeometry(QRect(
                0, 0, 600, self.ui.outputQFrame.height()
            ))
            self.show()

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
        self.ui.outputTerminalQWidget.lower()

    def closeEvent(self, event: QEvent) -> None:
        """
        Handle the close event, ensuring any detached windows are closed.

        :param event: The close event.
        """
        if self.detached_window:
            self.detached_window.close()
        super().closeEvent(event)

    def resizeEvent(self, event: QEvent) -> None:
        """
        Handle the resize event, updating the terminal UI.

        :param event: The resize event.
        """
        self.update_terminal_ui()

    def changeEvent(self, event: QEvent) -> None:
        """
        Handle the change event, updating the terminal UI if the window state changes.

        :param event: The change event.
        """
        super().changeEvent(event)
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self.update_terminal_ui()
            elif self.windowState() == Qt.WindowNoState:
                self.update_terminal_ui()

    def show(self) -> None:
        """
        Override the show method to update the terminal UI when the window is shown.
        """
        super(Application, self).show()
        self.update_terminal_ui()
        self.update_terminal_ui()


def clear_layout(layout: QLayout, delete: bool = True) -> None:
    """
    Clear all widgets from a layout.

    :param layout: The layout to clear.
    :param delete: Whether to delete the widgets after removing them from the layout.
    """
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None and delete:
                widget.deleteLater()
            else:
                clear_layout(item.layout())


def put_svg(layout: QLayout, path: str, width: int, height: int) -> QSvgWidget:
    """
    Add an SVG widget to a layout.

    :param layout: The layout to add the SVG widget to.
    :param path: The path to the SVG file.
    :param width: The width of the SVG widget.
    :param height: The height of the SVG widget.
    :return: The SVG widget.
    """
    clear_layout(layout)
    svg = QSvgWidget(path)
    svg.setMinimumSize(QSize(width, height))
    svg.setMaximumSize(QSize(width, height))
    svg.setStyleSheet("background: transparent")
    layout.addWidget(svg)
    return svg


def update_style(widget: QWidget) -> None:
    """
    Update the style of a widget.

    :param widget: The widget to update the style for.
    """
    widget.setStyleSheet(widget.styleSheet())
