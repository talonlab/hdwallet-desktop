import os
import json

from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QLayout
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import Qt, QEvent, QThreadPool, QSize, QRect
from PySide6.QtGui import QFontDatabase

from hdwd.ui.ui_hdwallet import Ui_MainWindow
from hdwd.detached_window import DetachedWindow

class Application(QMainWindow):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            super().__init__()
            self.initialize()
            self.initialized = True

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def initialize(self):
        QThreadPool.globalInstance().setMaxThreadCount(64)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.detached_window = None

        self.setWindowTitle("Hierarchical Deterministic Wallet")
        self.load_stylesheet(os.path.join(os.path.dirname(__file__), "ui/css/dark-style.css"))
        put_svg(self.ui.hdwalletLogoHLayout, os.path.join(os.path.dirname(__file__), "ui/images/11.svg"), 132.04, 45)
        QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), "ui/font/HD Wallet-Regular.ttf"))

    def load_stylesheet(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as style_file:
                stylesheet = style_file.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Failed to load stylesheet: {e}")

    def widget_changed(self, stacked_name: str, page_name: str, button: QWidget, qWidget: QWidget) -> None:
        for btn in qWidget.findChildren(QWidget):
            btn.setProperty("Active", "")
            update_style(btn)

        button.setProperty("Active", "true")
        update_style(button)
        self.change_page(stacked_name, page_name)

    def change_page(self, stacked_name: str, widget_name: str) -> None:
        qStackedWidget: Optional[QStackedWidget] = self.findChild(QStackedWidget, stacked_name)

        if qStackedWidget is None:
            print(f"QStackWidget not found: {stacked_name}")
            return None

        qWidget: Optional[QWidget] = qStackedWidget.findChild(QWidget, widget_name)

        if qStackedWidget and qWidget:
            qStackedWidget.setCurrentWidget(qWidget)
        else:
            print(f"ERROR changing page: '{stacked_name}' '{widget_name}'")

    def println(self, s):
        if isinstance(s, dict):
            newtext = json.dumps(s, indent=4, ensure_ascii=False)
        elif s == None:
            return None
        else:
            newtext = str(s)
        self.ui.outputTerminalQPlainTextEdit.appendPlainText(f"{newtext}")

    def toggle_expand(self, detach: bool):
        if detach:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
            self.setMaximumSize(
                self.ui.hdWalletContainerQFrame.width(), self.ui.hdwalletMainQFrame.height()
                # Set maximum size of main window
            )
            self.showNormal()

            self.layout().removeWidget(self.ui.outputQFrame)
            self.detached_window = DetachedWindow(self)
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
            self.setMaximumSize(
                16777215, 16777215  # Removes maximum size of main window
            )
            self.ui.outputQFrame.setGeometry(QRect(
                0, 0, 600, self.ui.outputQFrame.height()  # Fix from detached into attached
            ))
            self.show()

    def update_terminal_ui(self):
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

    def closeEvent(self, event):
        if self.detached_window:
            self.detached_window.close()
        super().closeEvent(event)

    def resizeEvent(self, event) -> None:
        self.update_terminal_ui()

    def changeEvent(self, event):
        super().changeEvent(event)
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self.update_terminal_ui()
            elif self.windowState() == Qt.WindowNoState:
                self.update_terminal_ui()

    def show(self):
        super(Application, self).show()
        self.update_terminal_ui()
        self.update_terminal_ui()


def clear_layout(layout: QLayout, delete: bool = True) -> None:
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None and delete:
                widget.deleteLater()
            else:
                clear_layout(item.layout())

def put_svg(layout: QLayout, path: str, width: int, height: int) -> QSvgWidget:
    clear_layout(layout)
    svg = QSvgWidget(path)
    svg.setMinimumSize(QSize(width, height))
    svg.setMaximumSize(QSize(width, height))
    svg.setStyleSheet("background: transparent")
    layout.addWidget(svg)
    return svg

def update_style(widget: QWidget):
    widget.setStyleSheet(widget.styleSheet())