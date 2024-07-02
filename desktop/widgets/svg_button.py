#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import Optional

from PySide6.QtCore import (
    Signal, QSize, Qt
)
from PySide6.QtWidgets import (
    QWidget, QStackedLayout
)
from PySide6.QtGui import QMouseEvent
from PySide6.QtSvgWidgets import QSvgWidget

class SvgButton(QWidget):
    """
    A custom button widget that uses SVG icons and supports checkable states.
    """

    clicked: Signal = Signal()
    toggled: Signal = Signal()

    checked: bool = False
    checkable: bool = False

    def __init__(self, parent_widget: QWidget, icon_path: str, icon_width: int, icon_height: int, alt_icon_path: Optional[str] = None) -> None:
        """
        Initialize a SvgButton instance.

        :param parent_widget: The parent widget.
        :type parent_widget: QWidget
        :param icon_path: The path to the main icon.
        :type icon_path: str
        :param icon_width: The width of the icon.
        :type icon_width: int
        :param icon_height: The height of the icon.
        :type icon_height: int
        :param alt_icon_path: The path to the alternate icon, default to ``None``.
        :type alt_icon_path: str, optional
        """
        super().__init__(parent_widget)
        QStackedLayout(self)
        self.icon: QSvgWidget = QSvgWidget(icon_path)
        self.icon_alt: Optional[QSvgWidget] = QSvgWidget(alt_icon_path) if alt_icon_path is not None else None

        self.icon_width: int = icon_width
        self.icon_height: int = icon_height

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
        self.parent: QWidget = parent_widget

    def setText(self, text: str) -> None:
        """
        Set the text for the button. (Currently not implemented)

        :param text: The text to set.
        :type text: str
        """
        pass

    def setCheckable(self, value: bool) -> None:
        """
        Set whether the button is checkable.

        :param value: A boolean indicating if the button should be checkable.
        :type value: bool
        """
        self.checkable = value

    def setChecked(self, value: bool) -> None:
        """
        Set the checked state of the button.

        :param value: A boolean indicating the checked state.
        :type value: bool
        """
        self.checked = value

        if self.icon_alt is not None:
            self.layout().setCurrentIndex(int(self.checked))

    def isChecked(self) -> bool:
        """
        Check if the button is currently checked.

        :returns: The checked state of the button.
        :rtype: bool
        """
        return self.checked

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Handle the mouse press event.

        :param event: The mouse press event.
        :type event: QMouseEvent
        """
        if event.button() == Qt.LeftButton:
            self.click()
            self.parent.setProperty("pressed", "true")
            self.parent.style().unpolish(self.parent)
            self.parent.style().polish(self.parent)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """
        Handle the mouse release event.

        :param event: The mouse release event.
        :type event: QMouseEvent
        """
        self.parent.setProperty("pressed", "")
        self.parent.style().unpolish(self.parent)
        self.parent.style().polish(self.parent)

    def click(self) -> None:
        """
        Emit the clicked signal and toggle the checked state if the button is checkable.
        """
        self.clicked.emit()
        if self.checkable:
            self.setChecked(not self.isChecked())
            self.toggled.emit()
