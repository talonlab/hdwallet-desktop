# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addressesHiLIuy.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_addressModalQWidget(object):
    def setupUi(self, addressModalQWidget):
        if not addressModalQWidget.objectName():
            addressModalQWidget.setObjectName(u"addressModalQWidget")
        addressModalQWidget.resize(545, 370)
        self.addressModalQWidgetVLayout = QVBoxLayout(addressModalQWidget)
        self.addressModalQWidgetVLayout.setSpacing(15)
        self.addressModalQWidgetVLayout.setObjectName(u"addressModalQWidgetVLayout")
        self.addressModalQWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.addressNavbarQFrame = QFrame(addressModalQWidget)
        self.addressNavbarQFrame.setObjectName(u"addressNavbarQFrame")
        self.addressNavbarQFrameHLayout = QHBoxLayout(self.addressNavbarQFrame)
        self.addressNavbarQFrameHLayout.setSpacing(10)
        self.addressNavbarQFrameHLayout.setObjectName(u"addressNavbarQFrameHLayout")
        self.addressNavbarQFrameHLayout.setContentsMargins(10, 0, 0, 0)
        self.addressQLabel = QLabel(self.addressNavbarQFrame)
        self.addressQLabel.setObjectName(u"addressQLabel")

        self.addressNavbarQFrameHLayout.addWidget(self.addressQLabel)

        self.addressNavbarQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.addressNavbarQFrameHLayout.addItem(self.addressNavbarQFrameHSpacer)

        self.closeAddressQPushButton = QPushButton(self.addressNavbarQFrame)
        self.closeAddressQPushButton.setObjectName(u"closeAddressQPushButton")
        self.closeAddressQPushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.addressNavbarQFrameHLayout.addWidget(self.closeAddressQPushButton, 0, Qt.AlignRight)


        self.addressModalQWidgetVLayout.addWidget(self.addressNavbarQFrame)

        self.addressBodyQFrame = QFrame(addressModalQWidget)
        self.addressBodyQFrame.setObjectName(u"addressBodyQFrame")
        self.addressBodyQFrameVLayout = QVBoxLayout(self.addressBodyQFrame)
        self.addressBodyQFrameVLayout.setSpacing(15)
        self.addressBodyQFrameVLayout.setObjectName(u"addressBodyQFrameVLayout")
        self.addressBodyQFrameVLayout.setContentsMargins(10, 0, 10, 0)
        self.addressCryptocurrencyAndPublicKeyContainerQFrame = QFrame(self.addressBodyQFrame)
        self.addressCryptocurrencyAndPublicKeyContainerQFrame.setObjectName(u"addressCryptocurrencyAndPublicKeyContainerQFrame")
        self.addressCryptocurrencyAndPublicKeyContainerQFrameHLayout = QHBoxLayout(self.addressCryptocurrencyAndPublicKeyContainerQFrame)
        self.addressCryptocurrencyAndPublicKeyContainerQFrameHLayout.setSpacing(15)
        self.addressCryptocurrencyAndPublicKeyContainerQFrameHLayout.setObjectName(u"addressCryptocurrencyAndPublicKeyContainerQFrameHLayout")
        self.addressCryptocurrencyAndPublicKeyContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.addressCryptocurrencyContainerQFrame = QFrame(self.addressCryptocurrencyAndPublicKeyContainerQFrame)
        self.addressCryptocurrencyContainerQFrame.setObjectName(u"addressCryptocurrencyContainerQFrame")
        self.addressCryptocurrencyContainerQFrame.setMinimumSize(QSize(150, 0))
        self.addressCryptocurrencyContainerQFrameVLayout = QVBoxLayout(self.addressCryptocurrencyContainerQFrame)
        self.addressCryptocurrencyContainerQFrameVLayout.setSpacing(15)
        self.addressCryptocurrencyContainerQFrameVLayout.setObjectName(u"addressCryptocurrencyContainerQFrameVLayout")
        self.addressCryptocurrencyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCryptocurrencyQLabel = QLabel(self.addressCryptocurrencyContainerQFrame)
        self.donationsCryptocurrencyQLabel.setObjectName(u"donationsCryptocurrencyQLabel")

        self.addressCryptocurrencyContainerQFrameVLayout.addWidget(self.donationsCryptocurrencyQLabel, 0, Qt.AlignHCenter)

        self.donationsCryptocurrencyQComboBox = QComboBox(self.addressCryptocurrencyContainerQFrame)
        self.donationsCryptocurrencyQComboBox.setObjectName(u"donationsCryptocurrencyQComboBox")

        self.addressCryptocurrencyContainerQFrameVLayout.addWidget(self.donationsCryptocurrencyQComboBox)


        self.addressCryptocurrencyAndPublicKeyContainerQFrameHLayout.addWidget(self.addressCryptocurrencyContainerQFrame)

        self.addressPublicKeyContainerQFrame = QFrame(self.addressCryptocurrencyAndPublicKeyContainerQFrame)
        self.addressPublicKeyContainerQFrame.setObjectName(u"addressPublicKeyContainerQFrame")
        self.addressPublicKeyContainerQFrameVLayout = QVBoxLayout(self.addressPublicKeyContainerQFrame)
        self.addressPublicKeyContainerQFrameVLayout.setSpacing(15)
        self.addressPublicKeyContainerQFrameVLayout.setObjectName(u"addressPublicKeyContainerQFrameVLayout")
        self.addressPublicKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.addressPublicKeyQLabel = QLabel(self.addressPublicKeyContainerQFrame)
        self.addressPublicKeyQLabel.setObjectName(u"addressPublicKeyQLabel")

        self.addressPublicKeyContainerQFrameVLayout.addWidget(self.addressPublicKeyQLabel)

        self.addressPublicKeyQLineEdit = QLineEdit(self.addressPublicKeyContainerQFrame)
        self.addressPublicKeyQLineEdit.setObjectName(u"addressPublicKeyQLineEdit")
        self.addressPublicKeyQLineEdit.setMinimumSize(QSize(250, 0))

        self.addressPublicKeyContainerQFrameVLayout.addWidget(self.addressPublicKeyQLineEdit)


        self.addressCryptocurrencyAndPublicKeyContainerQFrameHLayout.addWidget(self.addressPublicKeyContainerQFrame)

        self.addressGenerateButtonContainerQFrame = QFrame(self.addressCryptocurrencyAndPublicKeyContainerQFrame)
        self.addressGenerateButtonContainerQFrame.setObjectName(u"addressGenerateButtonContainerQFrame")
        self.addressGenerateButtonContainerQFrameVLayout = QVBoxLayout(self.addressGenerateButtonContainerQFrame)
        self.addressGenerateButtonContainerQFrameVLayout.setSpacing(0)
        self.addressGenerateButtonContainerQFrameVLayout.setObjectName(u"addressGenerateButtonContainerQFrameVLayout")
        self.addressGenerateButtonContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.addressGenerateButtonContainerQFrameVLayout.addItem(self.verticalSpacer)

        self.addressGenerateQPushButton = QPushButton(self.addressGenerateButtonContainerQFrame)
        self.addressGenerateQPushButton.setObjectName(u"addressGenerateQPushButton")

        self.addressGenerateButtonContainerQFrameVLayout.addWidget(self.addressGenerateQPushButton)


        self.addressCryptocurrencyAndPublicKeyContainerQFrameHLayout.addWidget(self.addressGenerateButtonContainerQFrame)


        self.addressBodyQFrameVLayout.addWidget(self.addressCryptocurrencyAndPublicKeyContainerQFrame)

        self.generatedAddressQRContainerQFrame = QFrame(self.addressBodyQFrame)
        self.generatedAddressQRContainerQFrame.setObjectName(u"generatedAddressQRContainerQFrame")
        self.generatedAddressQRContainerQFrameHLayout = QHBoxLayout(self.generatedAddressQRContainerQFrame)
        self.generatedAddressQRContainerQFrameHLayout.setSpacing(0)
        self.generatedAddressQRContainerQFrameHLayout.setObjectName(u"generatedAddressQRContainerQFrameHLayout")
        self.generatedAddressQRContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generatedAddressQRContainerQFrameHLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generatedAddressQRContainerQFrameHLayout.addItem(self.generatedAddressQRContainerQFrameHLSpacer)

        self.generatedAddressQRCodeQFrame = QFrame(self.generatedAddressQRContainerQFrame)
        self.generatedAddressQRCodeQFrame.setObjectName(u"generatedAddressQRCodeQFrame")
        self.generatedAddressQRCodeQFrameVLayout = QVBoxLayout(self.generatedAddressQRCodeQFrame)
        self.generatedAddressQRCodeQFrameVLayout.setSpacing(0)
        self.generatedAddressQRCodeQFrameVLayout.setObjectName(u"generatedAddressQRCodeQFrameVLayout")
        self.generatedAddressQRCodeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generatedAddressQRCodeQLabel = QLabel(self.generatedAddressQRCodeQFrame)
        self.generatedAddressQRCodeQLabel.setObjectName(u"generatedAddressQRCodeQLabel")
        self.generatedAddressQRCodeQLabel.setMinimumSize(QSize(200, 200))
        self.generatedAddressQRCodeQLabel.setMaximumSize(QSize(200, 200))

        self.generatedAddressQRCodeQFrameVLayout.addWidget(self.generatedAddressQRCodeQLabel)


        self.generatedAddressQRContainerQFrameHLayout.addWidget(self.generatedAddressQRCodeQFrame)

        self.generatedAddressQRContainerQFrameHRSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generatedAddressQRContainerQFrameHLayout.addItem(self.generatedAddressQRContainerQFrameHRSpacer)


        self.addressBodyQFrameVLayout.addWidget(self.generatedAddressQRContainerQFrame)

        self.generatedAddressContainerQFrame = QFrame(self.addressBodyQFrame)
        self.generatedAddressContainerQFrame.setObjectName(u"generatedAddressContainerQFrame")
        self.generatedAddressContainerQFrameHLayout = QHBoxLayout(self.generatedAddressContainerQFrame)
        self.generatedAddressContainerQFrameHLayout.setSpacing(0)
        self.generatedAddressContainerQFrameHLayout.setObjectName(u"generatedAddressContainerQFrameHLayout")
        self.generatedAddressContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generatedAddressContainerQFrameHLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generatedAddressContainerQFrameHLayout.addItem(self.generatedAddressContainerQFrameHLSpacer)

        self.generatedAddressQFrame = QFrame(self.generatedAddressContainerQFrame)
        self.generatedAddressQFrame.setObjectName(u"generatedAddressQFrame")
        self.generatedAddressQFrameHLayout = QHBoxLayout(self.generatedAddressQFrame)
        self.generatedAddressQFrameHLayout.setSpacing(15)
        self.generatedAddressQFrameHLayout.setObjectName(u"generatedAddressQFrameHLayout")
        self.generatedAddressQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generatedAddressQLabel = QLabel(self.generatedAddressQFrame)
        self.generatedAddressQLabel.setObjectName(u"generatedAddressQLabel")

        self.generatedAddressQFrameHLayout.addWidget(self.generatedAddressQLabel)

        self.generatedAddressCopyQPushButton = QPushButton(self.generatedAddressQFrame)
        self.generatedAddressCopyQPushButton.setObjectName(u"generatedAddressCopyQPushButton")

        self.generatedAddressQFrameHLayout.addWidget(self.generatedAddressCopyQPushButton)


        self.generatedAddressContainerQFrameHLayout.addWidget(self.generatedAddressQFrame)

        self.generatedAddressContainerQFrameHRSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generatedAddressContainerQFrameHLayout.addItem(self.generatedAddressContainerQFrameHRSpacer)


        self.addressBodyQFrameVLayout.addWidget(self.generatedAddressContainerQFrame)

        self.addressBodyQFrameVSpacer = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.addressBodyQFrameVLayout.addItem(self.addressBodyQFrameVSpacer)


        self.addressModalQWidgetVLayout.addWidget(self.addressBodyQFrame)


        self.retranslateUi(addressModalQWidget)

        QMetaObject.connectSlotsByName(addressModalQWidget)
    # setupUi

    def retranslateUi(self, addressModalQWidget):
        addressModalQWidget.setWindowTitle(QCoreApplication.translate("addressModalQWidget", u"Form", None))
        self.addressQLabel.setText(QCoreApplication.translate("addressModalQWidget", u"Addresses", None))
        self.closeAddressQPushButton.setText(QCoreApplication.translate("addressModalQWidget", u"X", None))
        self.donationsCryptocurrencyQLabel.setText(QCoreApplication.translate("addressModalQWidget", u"Cryptocurrency", None))
        self.donationsCryptocurrencyQComboBox.setPlaceholderText(QCoreApplication.translate("addressModalQWidget", u"Select Cryptocurrency", None))
        self.addressPublicKeyQLabel.setText(QCoreApplication.translate("addressModalQWidget", u"Public Key", None))
        self.addressGenerateQPushButton.setText(QCoreApplication.translate("addressModalQWidget", u"Generate", None))
        self.generatedAddressQRCodeQLabel.setText(QCoreApplication.translate("addressModalQWidget", u"QR Code", None))
        self.generatedAddressQLabel.setText(QCoreApplication.translate("addressModalQWidget", u"Address", None))
        self.generatedAddressCopyQPushButton.setText(QCoreApplication.translate("addressModalQWidget", u"Copy", None))
    # retranslateUi

