from PySide6.QtCore import (
    QTimer, QAbstractAnimation, QPropertyAnimation, QPoint, QRect
)

from PySide6.QtWidgets import (
    QMainWindow, QHBoxLayout, QGraphicsOpacityEffect, QLabel, QFrame
)

from desktop.widgets.core import Application


class Toast(QFrame):
    def __init__(self, *args, **kwargs):
        super(Toast, self).__init__(*args, **kwargs)
        QHBoxLayout(self)

        self.margin = 0

        self.timer = QTimer(singleShot=True, timeout=self.dispose)

        self.effect = QGraphicsOpacityEffect(opacity=0)
        self.setGraphicsEffect(self.effect)
        self.animation = QPropertyAnimation(self.effect, b'opacity')

        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setDuration(200)

    def dispose(self):
        self.animation.finished.connect(self.close)
        self.animation.setDirection(QAbstractAnimation.Direction.Backward)
        self.animation.setDuration(300)
        self.animation.start()

    def adjust_position(self, rect=None):
        geo = self.geometry()
        parent_rect = self.parent().rect() if not rect else rect
        x_pos = (parent_rect.bottomRight().x() / 2) - (self.width() / 2)  # parent windows center
        geo.moveBottomLeft(parent_rect.bottomLeft() + QPoint(x_pos, -self.margin))
        self.setGeometry(geo)

    def closeEvent(self, event):
        self.deleteLater()

    @staticmethod
    def show_toast(message: str, parent_rect: QRect = None, timeout: int = 1000) -> None:
        toast = Toast(Application.instance().window())

        toast.setObjectName("toastQFrame")
        toast.message_label = QLabel(message)
        toast.layout().addWidget(toast.message_label)

        toast.adjustSize()
        toast.adjust_position(parent_rect)

        toast.timer.setInterval(timeout)
        toast.timer.start()
        toast.show()
        toast.animation.start()
