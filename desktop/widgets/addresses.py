#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit
import os

import qrcode
from PIL.ImageQt import ImageQt, Image
from PySide6.QtSvg import QSvgRenderer

from PySide6.QtWidgets import (
    QWidget, QFrame, QVBoxLayout, QLabel
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter

from desktop.widgets.modal import Modal
from desktop.ui.ui_addresses import Ui_addressModalQWidget
from desktop.utils import put_svg, resolve_path, render_svg_on_label, put_qr_code


class Addresses(Modal):
    """
    Address modal implementation
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the address frame.
        """
        super(Addresses, self).__init__(*args, **kwargs)
        self.width: int = 650
        self.height: int = 500
        self.ui: Optional[Ui_Form] = None

    def generate_qr_code(self) -> None:
        addr = self.ui.addressPublicKeyQLineEdit.text()
        put_qr_code(self.ui.generatedAddressQRCodeQLabel, addr)

    @staticmethod
    def show_address_modal(main_window: QWidget, parent_frame: QWidget) -> None:
        """
        Display the address frame within the given main window.

        :param main_window: The main application window.
        :param parent_frame: Modal parent frame
        """
        frame: Addresses = Addresses(parent=main_window, parent_frame=parent_frame)

        main_widget = QWidget()
        main_widget.setContentsMargins(0, 0, 0, 0)
        addresses_ui = Ui_addressModalQWidget()
        addresses_ui.setupUi(main_widget)
        frame.ui = addresses_ui

        addresses_ui.closeModalQPushButton.clicked.connect(frame.close)
        # addresses_ui.generatedAddressCopyQPushButton.clicked.connect(
        #     lambda: copy_to_clipboard(, show_toast=True, frame=frame)
        # )
        render_svg_on_label(
            label=addresses_ui.generatedAddressQRCodeQLabel,
            svg_path=resolve_path("desktop/ui/images/svg/qr-empty.svg")
        )
        addresses_ui.addressGenerateQPushButton.clicked.connect(frame.generate_qr_code)

        frame.layout().addWidget(main_widget)
        frame.re_adjust()
        frame.show()
