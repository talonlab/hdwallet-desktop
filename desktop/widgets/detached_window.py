#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from PySide6.QtWidgets import (
    QWidget, QFrame, QPlainTextEdit
)
from PySide6.QtCore import (
    QEvent, QRect, Qt
)

class DetachedTerminalWindow(QWidget):
    """
    A custom widget representing a detached window.
    """

    def __init__(self, p: QWidget) -> None:
        """
        Initialize the DetachedWindow instance.

        :param p: The parent widget.
        :type p: QWidget
        """
        super().__init__()
        self.main_window = p

    def closeEvent(self, event) -> None:
        """
        Handle the close event of the detached window.

        :param event: The close event.
        """
        self.main_window.ui.toggle_expand_terminal.setChecked(False)
        self.main_window.toggle_expand(False)
        self.update_terminal_ui()

    def changeEvent(self, event: QEvent) -> None:
        """
        Handle the change event of the detached window.

        :param event: The change event.
        """
        super().changeEvent(event)
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self.update_terminal_ui()
            elif self.windowState() == Qt.WindowNoState:
                self.update_terminal_ui()

    def update_terminal_ui(self) -> None:
        try:
            noLayoutQWidget: QWidget = self.layout().itemAt(0).widget().findChild(QWidget, "noLayoutQWidget")
            outputWidgetTopContainerQWidget: QWidget = self.layout().itemAt(0).widget().findChild(QWidget,
                                                                                                  "outputWidgetTopContainerQWidget")
            outputTerminalQWidget: QWidget = self.layout().itemAt(0).widget().findChild(QWidget, "outputTerminalQWidget")
            outputWidgetTopContainerQFrame: QFrame = self.layout().itemAt(0).widget().findChild(QFrame,
                                                                                                "outputWidgetTopContainerQFrame")
            outputTerminalQPlainTextEdit: QPlainTextEdit = self.layout().itemAt(0).widget().findChild(QPlainTextEdit,
                                                                                                "outputTerminalQPlainTextEdit")
            outputWidgetTopContainerQWidget.setGeometry(QRect(
                (
                    noLayoutQWidget.width() - (
                        outputWidgetTopContainerQFrame.width() + (
                            20 if outputTerminalQPlainTextEdit.verticalScrollBar().maximum() > 0 else 10
                        )
                    )
                ), 0,
                outputWidgetTopContainerQFrame.width(), outputWidgetTopContainerQWidget.height()
            ))
            outputTerminalQWidget.setGeometry(QRect(
                0, 0, noLayoutQWidget.width(), noLayoutQWidget.height()
            ))
            outputWidgetTopContainerQWidget.raise_()
            outputTerminalQWidget.lower()
        except AttributeError:
            pass

    def resizeEvent(self, event: QEvent) -> None:
        """
        Handle the resize event of the detached window.

        :param event: The resize event.
        """
        self.update_terminal_ui()

    def show(self) -> None:
        super(DetachedTerminalWindow, self).show()
        self.update_terminal_ui()

    def center_window(self) -> None:
        """
        Center the detached window on the screen.
        """
        screen = self.screen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
        self.update_terminal_ui()
