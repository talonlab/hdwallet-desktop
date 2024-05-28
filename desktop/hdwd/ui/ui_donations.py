# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'donationsUrSTHY.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(512, 408)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.donationsNavbarQFrame = QFrame(Form)
        self.donationsNavbarQFrame.setObjectName(u"donationsNavbarQFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.donationsNavbarQFrame)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.donationsQLabel = QLabel(self.donationsNavbarQFrame)
        self.donationsQLabel.setObjectName(u"donationsQLabel")

        self.horizontalLayout_7.addWidget(self.donationsQLabel)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.frame_9 = QFrame(self.donationsNavbarQFrame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.donationsCoreTeamQPushButton = QPushButton(self.frame_9)
        self.donationsCoreTeamQPushButton.setObjectName(u"donationsCoreTeamQPushButton")

        self.horizontalLayout_16.addWidget(self.donationsCoreTeamQPushButton)

        self.donationsCharityQPushButton = QPushButton(self.frame_9)
        self.donationsCharityQPushButton.setObjectName(u"donationsCharityQPushButton")

        self.horizontalLayout_16.addWidget(self.donationsCharityQPushButton)


        self.horizontalLayout_7.addWidget(self.frame_9)

        self.closeDonationsQPushButton = QPushButton(self.donationsNavbarQFrame)
        self.closeDonationsQPushButton.setObjectName(u"closeDonationsQPushButton")

        self.horizontalLayout_7.addWidget(self.closeDonationsQPushButton, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.donationsNavbarQFrame)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.donationsCoreTeamQWidget = QWidget()
        self.donationsCoreTeamQWidget.setObjectName(u"donationsCoreTeamQWidget")
        self.verticalLayout = QVBoxLayout(self.donationsCoreTeamQWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.frame_2 = QFrame(self.donationsCoreTeamQWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.donationQRCodeContainerQFrame = QFrame(self.frame_5)
        self.donationQRCodeContainerQFrame.setObjectName(u"donationQRCodeContainerQFrame")
        self.verticalLayout_5 = QVBoxLayout(self.donationQRCodeContainerQFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.donationsQRCodeQLabel = QLabel(self.donationQRCodeContainerQFrame)
        self.donationsQRCodeQLabel.setObjectName(u"donationsQRCodeQLabel")
        self.donationsQRCodeQLabel.setMinimumSize(QSize(200, 200))
        self.donationsQRCodeQLabel.setMaximumSize(QSize(200, 200))

        self.verticalLayout_5.addWidget(self.donationsQRCodeQLabel)


        self.horizontalLayout_3.addWidget(self.donationQRCodeContainerQFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.donationsCoreTeamQWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.donationsAddressQLabel = QLabel(self.frame_6)
        self.donationsAddressQLabel.setObjectName(u"donationsAddressQLabel")

        self.horizontalLayout_4.addWidget(self.donationsAddressQLabel)

        self.donationsAddressCopyQPushButton = QPushButton(self.frame_6)
        self.donationsAddressCopyQPushButton.setObjectName(u"donationsAddressCopyQPushButton")

        self.horizontalLayout_4.addWidget(self.donationsAddressCopyQPushButton)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.donationsCoreTeamQWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_15)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(150, 0))
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.donationsCryptocurrencyQLabel = QLabel(self.frame_7)
        self.donationsCryptocurrencyQLabel.setObjectName(u"donationsCryptocurrencyQLabel")

        self.verticalLayout_3.addWidget(self.donationsCryptocurrencyQLabel, 0, Qt.AlignHCenter)

        self.donationsCryptocurrencyQComboBox = QComboBox(self.frame_7)
        self.donationsCryptocurrencyQComboBox.setObjectName(u"donationsCryptocurrencyQComboBox")

        self.verticalLayout_3.addWidget(self.donationsCryptocurrencyQComboBox)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_16)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.donationsCoreTeamQWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.horizontalLayout_17 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(50, 0, 50, 0)
        self.donationsCaptionQLabel = QLabel(self.frame_8)
        self.donationsCaptionQLabel.setObjectName(u"donationsCaptionQLabel")

        self.horizontalLayout_17.addWidget(self.donationsCaptionQLabel)


        self.verticalLayout.addWidget(self.frame_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.donationsCoreTeamQWidget)
        self.donationsCharityQWidget = QWidget()
        self.donationsCharityQWidget.setObjectName(u"donationsCharityQWidget")
        self.verticalLayout_7 = QVBoxLayout(self.donationsCharityQWidget)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.frame_11 = QFrame(self.donationsCharityQWidget)
        self.frame_11.setObjectName(u"frame_11")
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.donationCharityQRCodeContainerQFrame = QFrame(self.frame_11)
        self.donationCharityQRCodeContainerQFrame.setObjectName(u"donationCharityQRCodeContainerQFrame")
        self.verticalLayout_4 = QVBoxLayout(self.donationCharityQRCodeContainerQFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.donationsCharityQRCodeQLabel = QLabel(self.donationCharityQRCodeContainerQFrame)
        self.donationsCharityQRCodeQLabel.setObjectName(u"donationsCharityQRCodeQLabel")
        self.donationsCharityQRCodeQLabel.setMinimumSize(QSize(200, 200))
        self.donationsCharityQRCodeQLabel.setMaximumSize(QSize(200, 200))

        self.verticalLayout_4.addWidget(self.donationsCharityQRCodeQLabel)


        self.horizontalLayout_12.addWidget(self.donationCharityQRCodeContainerQFrame)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)


        self.verticalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.donationsCharityQWidget)
        self.frame_12.setObjectName(u"frame_12")
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.donationsCharityAddressQLabel = QLabel(self.frame_13)
        self.donationsCharityAddressQLabel.setObjectName(u"donationsCharityAddressQLabel")

        self.horizontalLayout_14.addWidget(self.donationsCharityAddressQLabel)

        self.donationsCharityAddressCopyQPushButton = QPushButton(self.frame_13)
        self.donationsCharityAddressCopyQPushButton.setObjectName(u"donationsCharityAddressCopyQPushButton")

        self.horizontalLayout_14.addWidget(self.donationsCharityAddressCopyQPushButton)


        self.horizontalLayout_13.addWidget(self.frame_13)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.donationsCharityQWidget)
        self.frame_14.setObjectName(u"frame_14")
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setSpacing(15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_13)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(150, 0))
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.donationsCharityCryptocurrencyQLabel = QLabel(self.frame_16)
        self.donationsCharityCryptocurrencyQLabel.setObjectName(u"donationsCharityCryptocurrencyQLabel")

        self.verticalLayout_6.addWidget(self.donationsCharityCryptocurrencyQLabel, 0, Qt.AlignHCenter)

        self.donationsCharityCryptocurrencyQComboBox = QComboBox(self.frame_16)
        self.donationsCharityCryptocurrencyQComboBox.setObjectName(u"donationsCharityCryptocurrencyQComboBox")

        self.verticalLayout_6.addWidget(self.donationsCharityCryptocurrencyQComboBox)


        self.horizontalLayout_15.addWidget(self.frame_16)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.donationsCharityQWidget)
        self.frame_15.setObjectName(u"frame_15")
        self.horizontalLayout_18 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(50, 0, 50, 0)
        self.donationsCharityCaptionQLabel = QLabel(self.frame_15)
        self.donationsCharityCaptionQLabel.setObjectName(u"donationsCharityCaptionQLabel")

        self.horizontalLayout_18.addWidget(self.donationsCharityCaptionQLabel)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.donationsCharityQWidget)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.donationsQLabel.setText(QCoreApplication.translate("Form", u"Donations", None))
        self.donationsCoreTeamQPushButton.setText(QCoreApplication.translate("Form", u"Core Team", None))
        self.donationsCharityQPushButton.setText(QCoreApplication.translate("Form", u"Charity", None))
        self.closeDonationsQPushButton.setText(QCoreApplication.translate("Form", u"X", None))
        self.donationsQRCodeQLabel.setText(QCoreApplication.translate("Form", u"QR Code", None))
        self.donationsAddressQLabel.setText(QCoreApplication.translate("Form", u"Address", None))
        self.donationsAddressCopyQPushButton.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.donationsCryptocurrencyQLabel.setText(QCoreApplication.translate("Form", u"Cryptocurrency", None))
        self.donationsCryptocurrencyQComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"Select Cryptocurrency", None))
        self.donationsCaptionQLabel.setText(QCoreApplication.translate("Form", u"Caption", None))
        self.donationsCharityQRCodeQLabel.setText(QCoreApplication.translate("Form", u"QR Code", None))
        self.donationsCharityAddressQLabel.setText(QCoreApplication.translate("Form", u"Address", None))
        self.donationsCharityAddressCopyQPushButton.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.donationsCharityCryptocurrencyQLabel.setText(QCoreApplication.translate("Form", u"Cryptocurrency", None))
        self.donationsCharityCryptocurrencyQComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"Select Cryptocurrency", None))
        self.donationsCharityCaptionQLabel.setText(QCoreApplication.translate("Form", u"Caption", None))
    # retranslateUi

