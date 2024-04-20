from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui.ui_hdwallet import Ui_MainWindow
from widget.SvgButton import SvgButton


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hierarchical Deterministic Wallet")

        self.load_stylesheet("ui/css/dark-style.css")

        self.toggle_expand_terminal = SvgButton(
            parent_widget=self.expandTerminalQFrame,
            icon_path="ui/images/icon_maximize.svg",
            alt_icon_path="ui/images/icon_minimize.svg",
            icon_width=17,
            icon_height=17
        )
        self.toggle_expand_terminal.setCheckable(True)

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
