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

        self.margin = 60

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

    def adjust_position(self, frame=None):
        geo = self.geometry()
        parent = self.parent() if not frame else frame
        x_pos = parent.geometry().x() + (parent.rect().bottomRight().x() / 2) - (self.width() / 2)  # parent windows center
        y_pos = parent.geometry().y() + parent.geometry().height() - self.margin
        geo.moveTo(QPoint(x_pos, y_pos))
        self.setGeometry(geo)

    def closeEvent(self, event):
        self.deleteLater()

    @staticmethod
    def show_toast(message: str, parent_frame: QRect = None, timeout: int = 1000) -> None:
        toast = Toast(Application.instance().window())

        toast.setObjectName("toastQFrame")
        toast.message_label = QLabel(message)
        toast.layout().addWidget(toast.message_label)

        toast.adjustSize()
        toast.adjust_position(parent_frame)

        toast.timer.setInterval(timeout)
        toast.timer.start()
        toast.show()
        toast.animation.start()
