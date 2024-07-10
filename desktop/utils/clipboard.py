#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from PySide6.QtGui import (
    QGuiApplication, QClipboard
)

from desktop.widgets.toast import Toast


def copy_to_clipboard(text: str, show_toast=True, frame_rect=None) -> None:
    """
    Copy text to the system clipboard.

    :param text: The text to be copied to the clipboard.
    :type text: str
    """
    clipboard: QClipboard = QGuiApplication.clipboard()
    clipboard.setText(text)
    if show_toast:
        Toast.show_toast(message="Copied!", parent_rect=frame_rect)

def get_clipboard_text() -> str:
    """
    Retrieve text from the system clipboard.

    :returns: The text currently stored in the clipboard.
    :rtype: str
    """
    clipboard: QClipboard = QGuiApplication.clipboard()
    return clipboard.text()

def clear_clipboard() -> None:
    """
    Clear the contents of the system clipboard.
    """
    clipboard: QClipboard = QGuiApplication.clipboard()
    clipboard.clear()
