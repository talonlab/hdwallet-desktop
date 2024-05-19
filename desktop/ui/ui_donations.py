# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'donationsLUMeWO.ui'
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
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.verticalLayout = QVBoxLayout(self.stackedWidgetPage1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.stackedWidgetPage1)
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

        self.frame_3 = QFrame(self.stackedWidgetPage1)
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

        self.frame_4 = QFrame(self.stackedWidgetPage1)
        self.frame_4.setObjectName(u"frame_4")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.donationsECCPublicKeyQComboBox = QComboBox(self.frame_9)
        self.donationsECCPublicKeyQComboBox.setObjectName(u"donationsECCPublicKeyQComboBox")

        self.verticalLayout_4.addWidget(self.donationsECCPublicKeyQComboBox)


        self.horizontalLayout_6.addWidget(self.frame_9)

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


        self.horizontalLayout_6.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_4)

        self.donationsDetailsQLabel = QLabel(self.stackedWidgetPage1)
        self.donationsDetailsQLabel.setObjectName(u"donationsDetailsQLabel")

        self.verticalLayout.addWidget(self.donationsDetailsQLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.stackedWidget.addWidget(self.stackedWidgetPage2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.closeDonationsQPushButton.setText(QCoreApplication.translate("Form", u"X", None))
        self.donationsCoreTeamQPushButton.setText(QCoreApplication.translate("Form", u"Core Team", None))
        self.donationsCharityQPushButton.setText(QCoreApplication.translate("Form", u"Charity", None))
        self.donationsAddressQLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ECC Public Key", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Cryptocurrency", None))
        self.donationsDetailsQLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

