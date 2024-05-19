from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout
from PySide6.QtCore import QEvent

from ui.ui_donations import Ui_Form

class Donation(QFrame):
    def __init__(self, *args, **kwargs):
        super(Donation, self).__init__(*args, **kwargs)
        QVBoxLayout(self)

        self.margin = 15
        self.width = 465
        self.height = 565

        self.overlay_frame = QFrame(self.parent())
        self.overlay_frame.setStyleSheet("background-color: rgba(0, 0, 0, 128);")

        self.modal_parent_frame = self.parent().findChild(QFrame, "hdWalletContainerQFrame")
        self.modal_parent_frame.installEventFilter(self)

        self.setObjectName("modalQFrame")

    def re_adjust(self):
        parent_rect = self.parent().rect()
        geo = self.modal_parent_frame.geometry()
        geo.setHeight(geo.height())

        x_pos = geo.width() / 2 - self.width / 2
        y_pos = geo.height() / 2 - self.height / 2
        self.setGeometry(x_pos, y_pos, self.width, self.height)

        self.overlay_frame.setGeometry(0, 0, geo.width(), geo.height())

    def eventFilter(self, obj, event):
        if (event.type() == QEvent.Resize):
            self.re_adjust()
        return super().eventFilter(obj, event)

    def show(self):
        self.overlay_frame.show()
        self.raise_()
        super().show()

    def closeEvent(self, event):
        self.overlay_frame.deleteLater()
        self.deleteLater()

    @staticmethod
    def show_donation(main_window):
        frame = Donation(main_window)
    
        main_widget = QWidget()
        donation_ui = Ui_Form()
        donation_ui.setupUi(main_widget)

        donation_ui.closeDonationsQPushButton.clicked.connect(frame.close)

        frame.layout().addWidget(main_widget)
        frame.re_adjust()
        frame.show()
        return frame