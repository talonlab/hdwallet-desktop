import subprocess

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PySide6.QtCore import QFile, Qt

from ui.ui_hdwallet import Ui_MainWindow
from widget.SvgButton import SvgButton

class DetachedWindow(QWidget):
    def __init__(self, p):
        super().__init__()
        self.main_window = p

    def closeEvent(self, event):
        self.main_window.toggle_expand_terminal.setChecked(False)
        self.main_window.toggle_expand()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Hierarchical Deterministic Wallet")

        self.load_stylesheet("ui/css/dark-style.css")

        self.toggle_expand_terminal = SvgButton(
            parent_widget=self.ui.expandTerminalQFrame,
            icon_path="ui/images/icon_maximize.svg",
            alt_icon_path="ui/images/icon_minimize.svg",
            icon_width=17,
            icon_height=17
        )
        self.toggle_expand_terminal.setCheckable(True)
        self.toggle_expand_terminal.toggled.connect(self.toggle_expand)
        self.ui.outputTerminalQLineEdit.returnPressed.connect(self.process_command)
        self.detached_window = None

    def process_command(self):
        result = subprocess.run(
                    f'hdwallet {self.ui.outputTerminalQLineEdit.text()}',
                    shell=True, 
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )

        output = result.stderr if result.stderr else result.stdout

        self.ui.outputTerminalQLineEdit.setText(None)
        self.ui.outputTerminalQTextEdit.setText(output.decode())

    def toggle_expand(self):
        if self.toggle_expand_terminal.isChecked():
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)     
            self.showNormal()

            self.layout().removeWidget(self.ui.outputQFrame)
            self.detached_window = DetachedWindow(self)
            self.detached_window.setWindowTitle("Hierarchical Deterministic Wallet - Output")
            self.detached_window.resize(self.ui.outputQFrame.width(), self.ui.outputQFrame.height())

            layout = QVBoxLayout()
            layout.addWidget(self.ui.outputQFrame)

            self.detached_window.setLayout(layout)
            self.detached_window.show()
            self.detached_window.setStyleSheet(self.styleSheet())
            self.setMinimumWidth(0)

            if not self.isMaximized():
                self.resize(self.width() - self.ui.outputQFrame.width(), self.height())

        else:
            if self.detached_window:
                self.detached_window.close()
                self.detached_window = None

            self.ui.centralwidget.layout().addWidget(self.ui.outputQFrame)

            self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
            self.show()

    def load_stylesheet(self, path):
        style_file = QFile(path)
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stylesheet = str(style_file.readAll(), encoding='utf-8')
            self.setStyleSheet(stylesheet)

    def closeEvent(self, event):
        if self.detached_window:
            self.detached_window.close()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication([])

    main_window = MyMainWindow()
    main_window.show()

    app.exec()
