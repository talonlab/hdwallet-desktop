#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit
import os

from PySide6.QtWidgets import (
    QWidget, QFrame, QVBoxLayout, QLabel
)
from PySide6.QtCore import Qt

from desktop.widgets.modal import Modal
from desktop.widgets.svg_button import SvgButton
from desktop.ui.ui_donations import Ui_Form
from desktop.addresses import crypto_addresses
from desktop.utils import put_qr_code
from desktop.utils.clipboard import copy_to_clipboard


class Donation(Modal):
    """
    A custom QFrame to handle donations, including UI setup and QR code generation.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the Donation frame.
        """
        super(Donation, self).__init__(*args, **kwargs)
        self.ui: Optional[Ui_Form] = None


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
        put_qr_code(self.ui.donationsQRCodeQLabel, addr)

    def charity_crypto_changed(self) -> None:
        """
        Update the charity donation address and QR code when the selected cryptocurrency changes.
        """
        crypto = self.ui.donationsCharityCryptocurrencyQComboBox.currentText()
        addr = crypto_addresses[crypto]
        self.charity_addr = addr
        self.ui.donationsCharityAddressQLabel.setText(f"{addr[:15]}...{addr[-10:]}")
        put_qr_code(self.ui.donationsCharityQRCodeQLabel, addr)

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
        donation_ui.donationsCharityCaptionQLabel.setTextFormat(Qt.RichText)
        donation_ui.donationsCharityCaptionQLabel.setText(
            """This donation is for the charity team, because without them,
        we'd have no idea where our good intentions should go.<br>
        Cheers to our chaos coordinators!"""
        )

        donation_ui.donationsCaptionQLabel.setTextFormat(Qt.RichText)
        donation_ui.donationsCaptionQLabel.setText(
            """This donation is for the core team, because without them,
        we'd be googling 'how to turn on a computer.'<br>
        Cheers to our tech wizards!"""
        )

        donation_ui.donationsCaptionQLabel.setWordWrap(True)
        donation_ui.donationsCharityCaptionQLabel.setWordWrap(True)

        donation_ui.donationsAddressCopyQPushButton.clicked.connect(
            lambda: copy_to_clipboard(text=frame.core_addr, show_toast=True, frame=frame)
        )
        donation_ui.donationsCharityAddressCopyQPushButton.clicked.connect(
            lambda: copy_to_clipboard(frame.charity_addr, show_toast=True, frame=frame)
        )

        frame.layout().addWidget(main_widget)
        frame.re_adjust()
        frame.show()
