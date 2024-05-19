# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'donationslOPrdS.ui'
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
        Form.resize(389, 268)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(Form)
        self.frame_8.setObjectName(u"frame_8")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.closeDonationsQPushButton = QPushButton(self.frame_8)
        self.closeDonationsQPushButton.setObjectName(u"closeDonationsQPushButton")

        self.horizontalLayout_7.addWidget(self.closeDonationsQPushButton, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.donationsCoreTeamQPushButton = QPushButton(self.frame)
        self.donationsCoreTeamQPushButton.setObjectName(u"donationsCoreTeamQPushButton")

        self.horizontalLayout_10.addWidget(self.donationsCoreTeamQPushButton)

        self.donationsCharityQPushButton = QPushButton(self.frame)
        self.donationsCharityQPushButton.setObjectName(u"donationsCharityQPushButton")

        self.horizontalLayout_10.addWidget(self.donationsCharityQPushButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.donationsCoreTeamQWidget = QWidget()
        self.donationsCoreTeamQWidget.setObjectName(u"donationsCoreTeamQWidget")
        self.verticalLayout = QVBoxLayout(self.donationsCoreTeamQWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.donationsCoreTeamQWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.donationsQRCodeQHBoxLayout = QHBoxLayout()
        self.donationsQRCodeQHBoxLayout.setObjectName(u"donationsQRCodeQHBoxLayout")

        self.horizontalLayout_3.addLayout(self.donationsQRCodeQHBoxLayout)

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
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.donationsAddressQLabel = QLabel(self.frame_6)
        self.donationsAddressQLabel.setObjectName(u"donationsAddressQLabel")

        self.horizontalLayout_4.addWidget(self.donationsAddressQLabel)


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
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.donationsCryptocurrencyQComboBox = QComboBox(self.frame_7)
        self.donationsCryptocurrencyQComboBox.setObjectName(u"donationsCryptocurrencyQComboBox")

        self.verticalLayout_3.addWidget(self.donationsCryptocurrencyQComboBox)


        self.horizontalLayout_6.addWidget(self.frame_7, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_4)

        self.donationsDetailsQLabel = QLabel(self.donationsCoreTeamQWidget)
        self.donationsDetailsQLabel.setObjectName(u"donationsDetailsQLabel")

        self.verticalLayout.addWidget(self.donationsDetailsQLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.donationsCoreTeamQWidget)
        self.donationsCharityQWidget = QWidget()
        self.donationsCharityQWidget.setObjectName(u"donationsCharityQWidget")
        self.verticalLayout_7 = QVBoxLayout(self.donationsCharityQWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_10 = QFrame(self.donationsCharityQWidget)
        self.frame_10.setObjectName(u"frame_10")
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.donationsCharityQRCodeQHBoxLayout = QHBoxLayout()
        self.donationsCharityQRCodeQHBoxLayout.setObjectName(u"donationsCharityQRCodeQHBoxLayout")

        self.horizontalLayout_12.addLayout(self.donationsCharityQRCodeQHBoxLayout)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)


        self.horizontalLayout_11.addWidget(self.frame_11)


        self.verticalLayout_7.addWidget(self.frame_10)

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
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.donationsCharityAddressQLabel = QLabel(self.frame_13)
        self.donationsCharityAddressQLabel.setObjectName(u"donationsCharityAddressQLabel")

        self.horizontalLayout_14.addWidget(self.donationsCharityAddressQLabel)


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
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.donationsCharityCryptocurrencyQComboBox = QComboBox(self.frame_16)
        self.donationsCharityCryptocurrencyQComboBox.setObjectName(u"donationsCharityCryptocurrencyQComboBox")

        self.verticalLayout_6.addWidget(self.donationsCharityCryptocurrencyQComboBox)


        self.horizontalLayout_15.addWidget(self.frame_16, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.donationsCharityDetailsQLabel = QLabel(self.donationsCharityQWidget)
        self.donationsCharityDetailsQLabel.setObjectName(u"donationsCharityDetailsQLabel")

        self.verticalLayout_7.addWidget(self.donationsCharityDetailsQLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 11, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.donationsCharityQWidget)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Donations", None))
        self.closeDonationsQPushButton.setText(QCoreApplication.translate("Form", u"X", None))
        self.donationsCoreTeamQPushButton.setText(QCoreApplication.translate("Form", u"Core Team", None))
        self.donationsCharityQPushButton.setText(QCoreApplication.translate("Form", u"Charity", None))
        self.donationsAddressQLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Cryptocurrency", None))
        self.donationsDetailsQLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.donationsCharityAddressQLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Cryptocurrency", None))
        self.donationsCharityDetailsQLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

