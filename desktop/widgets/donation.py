#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit
import os

import qrcode
from PIL.ImageQt import ImageQt, Image

from PySide6.QtWidgets import (
    QWidget, QFrame, QVBoxLayout, QLabel
)
from PySide6.QtCore import QEvent, Qt, Signal
from PySide6.QtGui import QPixmap

from desktop.widgets.svg_button import SvgButton
from desktop.ui.ui_donations import Ui_Form
from desktop.utils.clipboard import copy_to_clipboard
from desktop.addresses import crypto_addresses


class ClickableFrame(QFrame):
    """
    A custom QFrame that emits a clicked signal when pressed.
    """
    clicked = Signal()

    def mousePressEvent(self, event: QEvent) -> None:
        """
        Override the mousePressEvent to emit a clicked signal.

        :param event: The mouse press event.
        """
        if event.button() == Qt.LeftButton:
            self.clicked.emit()


class Donation(QFrame):
    """
    A custom QFrame to handle donations, including UI setup and QR code generation.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the Donation frame.
        """
        super(Donation, self).__init__(*args, **kwargs)
        QVBoxLayout(self)

        self.ui: Optional[Ui_Form] = None
        self.margin: int = 15
        self.width: int = 465
        self.height: int = 565

        self.overlay_frame: ClickableFrame = ClickableFrame(self.parent())
        self.overlay_frame.setStyleSheet("background-color: rgba(0, 0, 0, 128);")
        self.overlay_frame.clicked.connect(self.close)

        self.modal_parent_frame = self.parent().findChild(QFrame, "hdWalletContainerQFrame")
        self.modal_parent_frame.installEventFilter(self)

        self.setObjectName("modalQFrame")

    def re_adjust(self) -> None:
        """
        Re-adjust the frame and overlay positions.
        """
        parent_rect = self.parent().rect()
        geo = self.modal_parent_frame.geometry()
        geo.setHeight(geo.height())

        x_pos = geo.width() / 2 - self.width / 2
        y_pos = geo.height() / 2 - self.height / 2
        self.setGeometry(x_pos, y_pos, self.width, self.height)

        self.overlay_frame.setGeometry(0, 0, geo.width(), geo.height())

    def eventFilter(self, obj: QFrame, event: QEvent) -> bool:
        """
        Override the event filter to handle resize events.

        :param obj: The object being filtered.
        :param event: The event being filtered.
        :return: True if the event should be filtered out, False otherwise.
        """
        if event.type() == QEvent.Resize:
            self.re_adjust()
        return super().eventFilter(obj, event)

    def show(self) -> None:
        """
        Override the show method to display the overlay frame and re-adjust the layout.
        """
        self.overlay_frame.show()
        self.raise_()
        super().show()

    def closeEvent(self, event: QEvent) -> None:
        """
        Handle the close event, deleting the overlay frame.

        :param event: The close event.
        """
        self.overlay_frame.deleteLater()
        self.deleteLater()

    def update_receive_qr(self, qr_label: QLabel, text: str) -> None:
        """
        Generate and update a QR code for receiving cryptocurrency.

        :param qr_label: The QLabel to display the QR code.
        :param text: The text data to encode in the QR code.
        """
        qr_label.setText(None)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="white",
            back_color="#191e24"
        )

        qimage = ImageQt(img)

        pixmap = QPixmap.fromImage(qimage)

        qr_label.setPixmap(pixmap)
        qr_label.setAlignment(Qt.AlignCenter)
        qr_label.setScaledContents(True)

    def __update_btns(self) -> None:
        """
        Update the stylesheets of the donation buttons.
        """
        self.ui.donationsCharityQPushButton.setStyleSheet(
            self.ui.donationsCharityQPushButton.styleSheet()
        )
        self.ui.donationsCoreTeamQPushButton.setStyleSheet(
            self.ui.donationsCoreTeamQPushButton.styleSheet()
        )

    def show_charity(self) -> None:
        """
        Show the charity donation page.
        """
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.donationsCharityQPushButton.setProperty("Active", "true")
        self.ui.donationsCoreTeamQPushButton.setProperty("Active", "")
        self.__update_btns()

    def show_core(self) -> None:
        """
        Show the core team donation page.
        """
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.donationsCharityQPushButton.setProperty("Active", "")
        self.ui.donationsCoreTeamQPushButton.setProperty("Active", "true")
        self.__update_btns()

    def core_crypto_changed(self) -> None:
        """
        Update the core team donation address and QR code when the selected cryptocurrency changes.
        """
        crypto = self.ui.donationsCryptocurrencyQComboBox.currentText()
        addr = crypto_addresses[crypto]
        self.core_addr = addr
        self.ui.donationsAddressQLabel.setText(f"{addr[:15]}...{addr[-10:]}")
        self.update_receive_qr(self.ui.donationsQRCodeQLabel, addr)

    def charity_crypto_changed(self) -> None:
        """
        Update the charity donation address and QR code when the selected cryptocurrency changes.
        """
        crypto = self.ui.donationsCharityCryptocurrencyQComboBox.currentText()
        addr = crypto_addresses[crypto]
        self.charity_addr = addr
        self.ui.donationsCharityAddressQLabel.setText(f"{addr[:15]}...{addr[-10:]}")
        self.update_receive_qr(self.ui.donationsCharityQRCodeQLabel, addr)

    @staticmethod
    def show_donation(main_window: QWidget) -> None:
        """
        Display the donation frame within the given main window.

        :param main_window: The main application window.
        """
        frame: Donation = Donation(main_window)

        main_widget = QWidget()
        main_widget.setContentsMargins(0, 0, 0, 0)
        donation_ui = Ui_Form()
        donation_ui.setupUi(main_widget)
        frame.ui = donation_ui

        donation_ui.closeDonationsQPushButton.clicked.connect(frame.close)

        donation_ui.donationsCoreTeamQPushButton.clicked.connect(frame.show_core)
        donation_ui.donationsCharityQPushButton.clicked.connect(frame.show_charity)

        donation_ui.donationsCryptocurrencyQComboBox.addItems(sorted(crypto_addresses.keys()))
        donation_ui.donationsCryptocurrencyQComboBox.currentIndexChanged.connect(frame.core_crypto_changed)
        donation_ui.donationsCryptocurrencyQComboBox.setCurrentText("Ethereum")

        donation_ui.donationsCharityCryptocurrencyQComboBox.addItems(["Bitcoin", "Ethereum"])
        donation_ui.donationsCharityCryptocurrencyQComboBox.currentIndexChanged.connect(frame.charity_crypto_changed)
        donation_ui.donationsCharityCryptocurrencyQComboBox.setCurrentText("Ethereum")

        donation_ui.donationsCoreTeamQPushButton.click()
        donation_ui.donationsCharityCaptionQLabel.setText(
            "This donation is for the charity team, because without them,\
             we'd have no idea where our good intentions should go. \
            Cheers to our chaos coordinators!"
        )
        donation_ui.donationsCaptionQLabel.setText(
            "This donation is for the core team, because without them,\
            we'd be googling 'how to turn on a computer.' Cheers to our tech wizards!"
        )
        donation_ui.donationsCaptionQLabel.setWordWrap(True)
        donation_ui.donationsCharityCaptionQLabel.setWordWrap(True)

        donation_ui.donationsAddressCopyQPushButton.clicked.connect(
            lambda: copy_to_clipboard(frame.core_addr)
        )
        donation_ui.donationsCharityAddressCopyQPushButton.clicked.connect(
            lambda: copy_to_clipboard(frame.charity_addr)
        )

        frame.layout().addWidget(main_widget)
        frame.re_adjust()
        frame.show()
