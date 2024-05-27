from PySide6.QtCore import Signal, QSize, Qt
from PySide6.QtWidgets import QWidget, QStackedLayout, QSizePolicy
from PySide6.QtSvgWidgets import QSvgWidget


class SvgButton(QWidget):
    clicked = Signal()
    toggled = Signal()

    checked = False
    checkable = False

    def __init__(self, parent_widget, icon_path, icon_width, icon_height, alt_icon_path=None):
        super(SvgButton, self).__init__()
        QStackedLayout(self)
        self.icon = QSvgWidget(icon_path)
        self.icon_alt = QSvgWidget(alt_icon_path) if alt_icon_path is not None else None

        self.icon_width = icon_width
        self.icon_height = icon_height

        self.setFixedWidth(parent_widget.width())
        self.setFixedHeight(parent_widget.height())

        self.icon.setMinimumSize(QSize(self.icon_width, self.icon_height))
        self.icon.setMaximumSize(QSize(self.icon_width, self.icon_height))

        self.layout().addWidget(self.icon)

        if self.icon_alt is not None:
            self.icon_alt.setMinimumSize(QSize(self.icon_width, self.icon_height))
            self.icon_alt.setMaximumSize(QSize(self.icon_width, self.icon_height))
            self.layout().addWidget(self.icon_alt)

        parent_widget.layout().addWidget(self)
        self.parent = parent_widget

    def setText(self, text):
        pass

    def setCheckable(self, value):
        self.checkable = value

    def setChecked(self, value):
        self.checked = value

        if self.icon_alt is not None:
            self.layout().setCurrentIndex(int(self.checked))

    def isChecked(self):
        return self.checked

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.click()
            self.parent.setProperty("pressed", "true")
            self.parent.style().unpolish(self.parent)
            self.parent.style().polish(self.parent)

    def mouseReleaseEvent(self, event):
        self.parent.setProperty("pressed", "")
        self.parent.style().unpolish(self.parent)
        self.parent.style().polish(self.parent)

    def click(self):
        self.clicked.emit()
        if self.checkable:
            self.setChecked(self.isChecked() ^ True)
            self.toggled.emit()
