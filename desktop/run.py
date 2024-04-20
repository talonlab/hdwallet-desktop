from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PySide6.QtCore import QFile
from ui.ui_hdwallet import Ui_MainWindow
from widget.SvgButton import SvgButton


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

    def toggle_expand(self):
        if self.toggle_expand_terminal.isChecked():
            self.layout().removeWidget(self.ui.outputQFrame)
            self.detached_window = QWidget()
            self.detached_window.setWindowTitle("Detached Red Frame")
            self.detached_window.resize(self.ui.outputQFrame.width(), self.ui.outputQFrame.height())
            layout = QVBoxLayout()
            layout.addWidget(self.ui.outputQFrame)
            self.detached_window.setLayout(layout)
            self.detached_window.show()
            self.detached_window.setStyleSheet(self.styleSheet())
        else:
            self.detached_window.close()
            self.ui.centralwidget.layout().addWidget(self.ui.outputQFrame)

    def load_stylesheet(self, path):
        style_file = QFile(path)
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stylesheet = str(style_file.readAll(), encoding='utf-8')
            self.setStyleSheet(stylesheet)


if __name__ == "__main__":
    app = QApplication([])

    main_window = MyMainWindow()
    main_window.show()

    app.exec()
