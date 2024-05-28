from PySide6.QtWidgets import QWidget, QFrame, QPlainTextEdit
from PySide6.QtCore import QEvent, QRect

class DetachedWindow(QWidget):
    def __init__(self, p):
        super().__init__()
        self.main_window = p

    def closeEvent(self, event):
        self.main_window.ui.toggle_expand_terminal.setChecked(False)
        self.main_window.toggle_expand(False)
        self.update_terminal_ui()

    def changeEvent(self, event):
        super().changeEvent(event)
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self.update_terminal_ui()
            elif self.windowState() == Qt.WindowNoState:
                self.update_terminal_ui()

    def update_terminal_ui(self):
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

    def resizeEvent(self, event) -> None:
        self.update_terminal_ui()

    def show(self):
        super(DetachedWindow, self).show()
        self.update_terminal_ui()

    def center_window(self):
        # Get the screen resolution from the application
        screen = self.screen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
        self.update_terminal_ui()