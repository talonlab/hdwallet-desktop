# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'donationslATPzU.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(512, 408)
        self.FormVLayout = QVBoxLayout(Form)
        self.FormVLayout.setSpacing(0)
        self.FormVLayout.setObjectName(u"FormVLayout")
        self.FormVLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsNavbarQFrame = QFrame(Form)
        self.donationsNavbarQFrame.setObjectName(u"donationsNavbarQFrame")
        self.donationsNavbarQFrameHLayout = QHBoxLayout(self.donationsNavbarQFrame)
        self.donationsNavbarQFrameHLayout.setSpacing(10)
        self.donationsNavbarQFrameHLayout.setObjectName(u"donationsNavbarQFrameHLayout")
        self.donationsNavbarQFrameHLayout.setContentsMargins(10, 0, 0, 0)
        self.donationsQLabel = QLabel(self.donationsNavbarQFrame)
        self.donationsQLabel.setObjectName(u"donationsQLabel")

        self.donationsNavbarQFrameHLayout.addWidget(self.donationsQLabel)

        self.donationsNavbarQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsNavbarQFrameHLayout.addItem(self.donationsNavbarQFrameHSpacer)

        self.donationsQPushButtonContainerQFrame = QFrame(self.donationsNavbarQFrame)
        self.donationsQPushButtonContainerQFrame.setObjectName(u"donationsQPushButtonContainerQFrame")
        self.donationsQPushButtonContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.donationsQPushButtonContainerQFrame.setFrameShadow(QFrame.Raised)
        self.donationsQPushButtonContainerQFrameHLayout = QHBoxLayout(self.donationsQPushButtonContainerQFrame)
        self.donationsQPushButtonContainerQFrameHLayout.setSpacing(0)
        self.donationsQPushButtonContainerQFrameHLayout.setObjectName(u"donationsQPushButtonContainerQFrameHLayout")
        self.donationsQPushButtonContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCoreTeamQPushButton = QPushButton(self.donationsQPushButtonContainerQFrame)
        self.donationsCoreTeamQPushButton.setObjectName(u"donationsCoreTeamQPushButton")

        self.donationsQPushButtonContainerQFrameHLayout.addWidget(self.donationsCoreTeamQPushButton)

        self.donationsCharityQPushButton = QPushButton(self.donationsQPushButtonContainerQFrame)
        self.donationsCharityQPushButton.setObjectName(u"donationsCharityQPushButton")

        self.donationsQPushButtonContainerQFrameHLayout.addWidget(self.donationsCharityQPushButton)


        self.donationsNavbarQFrameHLayout.addWidget(self.donationsQPushButtonContainerQFrame)

        self.closeModalButtonQFrame = QFrame(self.donationsNavbarQFrame)
        self.closeModalButtonQFrame.setObjectName(u"closeModalButtonQFrame")
        self.closeModalButtonQFrame.setMinimumSize(QSize(35, 25))
        self.closeModalButtonQFrame.setMaximumSize(QSize(35, 25))
        self.closeModalButtonQFrame.setFrameShape(QFrame.StyledPanel)
        self.closeModalButtonQFrame.setFrameShadow(QFrame.Raised)
        self.closeModalButtonQFrameVLayout = QVBoxLayout(self.closeModalButtonQFrame)
        self.closeModalButtonQFrameVLayout.setSpacing(0)
        self.closeModalButtonQFrameVLayout.setObjectName(u"closeModalButtonQFrameVLayout")
        self.closeModalButtonQFrameVLayout.setContentsMargins(0, 0, 0, 0)

        self.donationsNavbarQFrameHLayout.addWidget(self.closeModalButtonQFrame)


        self.FormVLayout.addWidget(self.donationsNavbarQFrame)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.donationsCoreTeamQWidget = QWidget()
        self.donationsCoreTeamQWidget.setObjectName(u"donationsCoreTeamQWidget")
        self.donationsCoreTeamQWidgetVLayout = QVBoxLayout(self.donationsCoreTeamQWidget)
        self.donationsCoreTeamQWidgetVLayout.setSpacing(15)
        self.donationsCoreTeamQWidgetVLayout.setObjectName(u"donationsCoreTeamQWidgetVLayout")
        self.donationsCoreTeamQWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCoreTeamQWidgetVTSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.donationsCoreTeamQWidgetVLayout.addItem(self.donationsCoreTeamQWidgetVTSpacer)

        self.donationsCoreTeamQRQFrame = QFrame(self.donationsCoreTeamQWidget)
        self.donationsCoreTeamQRQFrame.setObjectName(u"donationsCoreTeamQRQFrame")
        self.donationsCoreTeamQRQFrameHLayout = QHBoxLayout(self.donationsCoreTeamQRQFrame)
        self.donationsCoreTeamQRQFrameHLayout.setSpacing(0)
        self.donationsCoreTeamQRQFrameHLayout.setObjectName(u"donationsCoreTeamQRQFrameHLayout")
        self.donationsCoreTeamQRQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCoreTeamQRCodeQFrame = QFrame(self.donationsCoreTeamQRQFrame)
        self.donationsCoreTeamQRCodeQFrame.setObjectName(u"donationsCoreTeamQRCodeQFrame")
        self.donationsCoreTeamQRCodeQFrameHLayout = QHBoxLayout(self.donationsCoreTeamQRCodeQFrame)
        self.donationsCoreTeamQRCodeQFrameHLayout.setSpacing(0)
        self.donationsCoreTeamQRCodeQFrameHLayout.setObjectName(u"donationsCoreTeamQRCodeQFrameHLayout")
        self.donationsCoreTeamQRCodeQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCoreTeamQRCodeQFrameVLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCoreTeamQRCodeQFrameHLayout.addItem(self.donationsCoreTeamQRCodeQFrameVLSpacer)

        self.donationQRCodeContainerQFrame = QFrame(self.donationsCoreTeamQRCodeQFrame)
        self.donationQRCodeContainerQFrame.setObjectName(u"donationQRCodeContainerQFrame")
        self.donationQRCodeContainerQFrameVLayout = QVBoxLayout(self.donationQRCodeContainerQFrame)
        self.donationQRCodeContainerQFrameVLayout.setSpacing(0)
        self.donationQRCodeContainerQFrameVLayout.setObjectName(u"donationQRCodeContainerQFrameVLayout")
        self.donationQRCodeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsQRCodeQLabel = QLabel(self.donationQRCodeContainerQFrame)
        self.donationsQRCodeQLabel.setObjectName(u"donationsQRCodeQLabel")
        self.donationsQRCodeQLabel.setMinimumSize(QSize(200, 200))
        self.donationsQRCodeQLabel.setMaximumSize(QSize(200, 200))

        self.donationQRCodeContainerQFrameVLayout.addWidget(self.donationsQRCodeQLabel)


        self.donationsCoreTeamQRCodeQFrameHLayout.addWidget(self.donationQRCodeContainerQFrame)

        self.donationsCoreTeamQRCodeQFrameVRSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCoreTeamQRCodeQFrameHLayout.addItem(self.donationsCoreTeamQRCodeQFrameVRSpacer)


        self.donationsCoreTeamQRQFrameHLayout.addWidget(self.donationsCoreTeamQRCodeQFrame)


        self.donationsCoreTeamQWidgetVLayout.addWidget(self.donationsCoreTeamQRQFrame)

        self.donationsCoreTeamAddressContainerQFrame = QFrame(self.donationsCoreTeamQWidget)
        self.donationsCoreTeamAddressContainerQFrame.setObjectName(u"donationsCoreTeamAddressContainerQFrame")
        self.donationsCoreTeamAddressContainerQFrameHLayout = QHBoxLayout(self.donationsCoreTeamAddressContainerQFrame)
        self.donationsCoreTeamAddressContainerQFrameHLayout.setSpacing(0)
        self.donationsCoreTeamAddressContainerQFrameHLayout.setObjectName(u"donationsCoreTeamAddressContainerQFrameHLayout")
        self.donationsCoreTeamAddressContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCoreTeamAddressContainerQFrameHLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCoreTeamAddressContainerQFrameHLayout.addItem(self.donationsCoreTeamAddressContainerQFrameHLSpacer)

        self.donationsCoreTeamAddressQFrame = QFrame(self.donationsCoreTeamAddressContainerQFrame)
        self.donationsCoreTeamAddressQFrame.setObjectName(u"donationsCoreTeamAddressQFrame")
        self.donationsCoreTeamAddressQFrameHLayout = QHBoxLayout(self.donationsCoreTeamAddressQFrame)
        self.donationsCoreTeamAddressQFrameHLayout.setSpacing(15)
        self.donationsCoreTeamAddressQFrameHLayout.setObjectName(u"donationsCoreTeamAddressQFrameHLayout")
        self.donationsCoreTeamAddressQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsAddressQLabel = QLabel(self.donationsCoreTeamAddressQFrame)
        self.donationsAddressQLabel.setObjectName(u"donationsAddressQLabel")

        self.donationsCoreTeamAddressQFrameHLayout.addWidget(self.donationsAddressQLabel)

        self.donationsAddressCopyQPushButton = QPushButton(self.donationsCoreTeamAddressQFrame)
        self.donationsAddressCopyQPushButton.setObjectName(u"donationsAddressCopyQPushButton")

        self.donationsCoreTeamAddressQFrameHLayout.addWidget(self.donationsAddressCopyQPushButton)


        self.donationsCoreTeamAddressContainerQFrameHLayout.addWidget(self.donationsCoreTeamAddressQFrame)

        self.donationsCoreTeamAddressContainerQFrameHRSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCoreTeamAddressContainerQFrameHLayout.addItem(self.donationsCoreTeamAddressContainerQFrameHRSpacer)


        self.donationsCoreTeamQWidgetVLayout.addWidget(self.donationsCoreTeamAddressContainerQFrame)

        self.donationsCoreTeamCryptocurrencyContainerQFrame = QFrame(self.donationsCoreTeamQWidget)
        self.donationsCoreTeamCryptocurrencyContainerQFrame.setObjectName(u"donationsCoreTeamCryptocurrencyContainerQFrame")
        self.donationsCoreTeamCryptocurrencyContainerQFrameHLayout = QHBoxLayout(self.donationsCoreTeamCryptocurrencyContainerQFrame)
        self.donationsCoreTeamCryptocurrencyContainerQFrameHLayout.setSpacing(15)
        self.donationsCoreTeamCryptocurrencyContainerQFrameHLayout.setObjectName(u"donationsCoreTeamCryptocurrencyContainerQFrameHLayout")
        self.donationsCoreTeamCryptocurrencyContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCoreTeamCryptocurrencyContainerQFrameHLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCoreTeamCryptocurrencyContainerQFrameHLayout.addItem(self.donationsCoreTeamCryptocurrencyContainerQFrameHLSpacer)

        self.donationsCoreTeamCryptocurrencyQFrame = QFrame(self.donationsCoreTeamCryptocurrencyContainerQFrame)
        self.donationsCoreTeamCryptocurrencyQFrame.setObjectName(u"donationsCoreTeamCryptocurrencyQFrame")
        self.donationsCoreTeamCryptocurrencyQFrame.setMinimumSize(QSize(150, 0))
        self.donationsCoreTeamCryptocurrencyQFrameVLayout = QVBoxLayout(self.donationsCoreTeamCryptocurrencyQFrame)
        self.donationsCoreTeamCryptocurrencyQFrameVLayout.setSpacing(15)
        self.donationsCoreTeamCryptocurrencyQFrameVLayout.setObjectName(u"donationsCoreTeamCryptocurrencyQFrameVLayout")
        self.donationsCoreTeamCryptocurrencyQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCryptocurrencyQLabel = QLabel(self.donationsCoreTeamCryptocurrencyQFrame)
        self.donationsCryptocurrencyQLabel.setObjectName(u"donationsCryptocurrencyQLabel")

        self.donationsCoreTeamCryptocurrencyQFrameVLayout.addWidget(self.donationsCryptocurrencyQLabel, 0, Qt.AlignHCenter)

        self.donationsCryptocurrencyQComboBox = QComboBox(self.donationsCoreTeamCryptocurrencyQFrame)
        self.donationsCryptocurrencyQComboBox.setObjectName(u"donationsCryptocurrencyQComboBox")

        self.donationsCoreTeamCryptocurrencyQFrameVLayout.addWidget(self.donationsCryptocurrencyQComboBox)


        self.donationsCoreTeamCryptocurrencyContainerQFrameHLayout.addWidget(self.donationsCoreTeamCryptocurrencyQFrame)

        self.donationsCoreTeamCryptocurrencyContainerQFrameHRSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCoreTeamCryptocurrencyContainerQFrameHLayout.addItem(self.donationsCoreTeamCryptocurrencyContainerQFrameHRSpacer)


        self.donationsCoreTeamQWidgetVLayout.addWidget(self.donationsCoreTeamCryptocurrencyContainerQFrame)

        self.donationsCoreTeamCaptionContainerQFrame = QFrame(self.donationsCoreTeamQWidget)
        self.donationsCoreTeamCaptionContainerQFrame.setObjectName(u"donationsCoreTeamCaptionContainerQFrame")
        self.donationsCoreTeamCaptionContainerQFrameHLayout = QHBoxLayout(self.donationsCoreTeamCaptionContainerQFrame)
        self.donationsCoreTeamCaptionContainerQFrameHLayout.setSpacing(0)
        self.donationsCoreTeamCaptionContainerQFrameHLayout.setObjectName(u"donationsCoreTeamCaptionContainerQFrameHLayout")
        self.donationsCoreTeamCaptionContainerQFrameHLayout.setContentsMargins(50, 0, 50, 0)
        self.donationsCaptionQLabel = QLabel(self.donationsCoreTeamCaptionContainerQFrame)
        self.donationsCaptionQLabel.setObjectName(u"donationsCaptionQLabel")

        self.donationsCoreTeamCaptionContainerQFrameHLayout.addWidget(self.donationsCaptionQLabel)


        self.donationsCoreTeamQWidgetVLayout.addWidget(self.donationsCoreTeamCaptionContainerQFrame)

        self.donationsCoreTeamQWidgetVMSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.donationsCoreTeamQWidgetVLayout.addItem(self.donationsCoreTeamQWidgetVMSpacer)

        self.donationsCoreTeamQWidgetVBSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.donationsCoreTeamQWidgetVLayout.addItem(self.donationsCoreTeamQWidgetVBSpacer)

        self.stackedWidget.addWidget(self.donationsCoreTeamQWidget)
        self.donationsCharityQWidget = QWidget()
        self.donationsCharityQWidget.setObjectName(u"donationsCharityQWidget")
        self.donationsCharityQWidgetVLayout = QVBoxLayout(self.donationsCharityQWidget)
        self.donationsCharityQWidgetVLayout.setSpacing(15)
        self.donationsCharityQWidgetVLayout.setObjectName(u"donationsCharityQWidgetVLayout")
        self.donationsCharityQWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCharityQWidgetVTSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.donationsCharityQWidgetVLayout.addItem(self.donationsCharityQWidgetVTSpacer)

        self.donationsCharityQRCodeQFrame = QFrame(self.donationsCharityQWidget)
        self.donationsCharityQRCodeQFrame.setObjectName(u"donationsCharityQRCodeQFrame")
        self.donationsCharityQRCodeQFrameHLayout = QHBoxLayout(self.donationsCharityQRCodeQFrame)
        self.donationsCharityQRCodeQFrameHLayout.setSpacing(0)
        self.donationsCharityQRCodeQFrameHLayout.setObjectName(u"donationsCharityQRCodeQFrameHLayout")
        self.donationsCharityQRCodeQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCharityQRCodeQFrameHLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCharityQRCodeQFrameHLayout.addItem(self.donationsCharityQRCodeQFrameHLSpacer)

        self.donationCharityQRCodeContainerQFrame = QFrame(self.donationsCharityQRCodeQFrame)
        self.donationCharityQRCodeContainerQFrame.setObjectName(u"donationCharityQRCodeContainerQFrame")
        self.donationCharityQRCodeContainerQFrameVLayout = QVBoxLayout(self.donationCharityQRCodeContainerQFrame)
        self.donationCharityQRCodeContainerQFrameVLayout.setSpacing(0)
        self.donationCharityQRCodeContainerQFrameVLayout.setObjectName(u"donationCharityQRCodeContainerQFrameVLayout")
        self.donationCharityQRCodeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCharityQRCodeQLabel = QLabel(self.donationCharityQRCodeContainerQFrame)
        self.donationsCharityQRCodeQLabel.setObjectName(u"donationsCharityQRCodeQLabel")
        self.donationsCharityQRCodeQLabel.setMinimumSize(QSize(200, 200))
        self.donationsCharityQRCodeQLabel.setMaximumSize(QSize(200, 200))

        self.donationCharityQRCodeContainerQFrameVLayout.addWidget(self.donationsCharityQRCodeQLabel)


        self.donationsCharityQRCodeQFrameHLayout.addWidget(self.donationCharityQRCodeContainerQFrame)

        self.donationsCharityQRCodeQFrameHRSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCharityQRCodeQFrameHLayout.addItem(self.donationsCharityQRCodeQFrameHRSpacer)


        self.donationsCharityQWidgetVLayout.addWidget(self.donationsCharityQRCodeQFrame)

        self.donationsCharityAddressContainerQFrame = QFrame(self.donationsCharityQWidget)
        self.donationsCharityAddressContainerQFrame.setObjectName(u"donationsCharityAddressContainerQFrame")
        self.donationsCharityAddressContainerQFrameHLayout = QHBoxLayout(self.donationsCharityAddressContainerQFrame)
        self.donationsCharityAddressContainerQFrameHLayout.setSpacing(0)
        self.donationsCharityAddressContainerQFrameHLayout.setObjectName(u"donationsCharityAddressContainerQFrameHLayout")
        self.donationsCharityAddressContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCharityAddressContainerQFrameHLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCharityAddressContainerQFrameHLayout.addItem(self.donationsCharityAddressContainerQFrameHLSpacer)

        self.donationsCharityAddressQFrame = QFrame(self.donationsCharityAddressContainerQFrame)
        self.donationsCharityAddressQFrame.setObjectName(u"donationsCharityAddressQFrame")
        self.donationsCharityAddressQFrameHLayout = QHBoxLayout(self.donationsCharityAddressQFrame)
        self.donationsCharityAddressQFrameHLayout.setSpacing(15)
        self.donationsCharityAddressQFrameHLayout.setObjectName(u"donationsCharityAddressQFrameHLayout")
        self.donationsCharityAddressQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCharityAddressQLabel = QLabel(self.donationsCharityAddressQFrame)
        self.donationsCharityAddressQLabel.setObjectName(u"donationsCharityAddressQLabel")

        self.donationsCharityAddressQFrameHLayout.addWidget(self.donationsCharityAddressQLabel)

        self.donationsCharityAddressCopyQPushButton = QPushButton(self.donationsCharityAddressQFrame)
        self.donationsCharityAddressCopyQPushButton.setObjectName(u"donationsCharityAddressCopyQPushButton")

        self.donationsCharityAddressQFrameHLayout.addWidget(self.donationsCharityAddressCopyQPushButton)


        self.donationsCharityAddressContainerQFrameHLayout.addWidget(self.donationsCharityAddressQFrame)

        self.donationsCharityAddressContainerQFrameHRSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCharityAddressContainerQFrameHLayout.addItem(self.donationsCharityAddressContainerQFrameHRSpacer)


        self.donationsCharityQWidgetVLayout.addWidget(self.donationsCharityAddressContainerQFrame)

        self.donationsCharityCryptocurrencyContainerQFrame = QFrame(self.donationsCharityQWidget)
        self.donationsCharityCryptocurrencyContainerQFrame.setObjectName(u"donationsCharityCryptocurrencyContainerQFrame")
        self.donationsCharityCryptocurrencyContainerQFrameHLayout = QHBoxLayout(self.donationsCharityCryptocurrencyContainerQFrame)
        self.donationsCharityCryptocurrencyContainerQFrameHLayout.setSpacing(15)
        self.donationsCharityCryptocurrencyContainerQFrameHLayout.setObjectName(u"donationsCharityCryptocurrencyContainerQFrameHLayout")
        self.donationsCharityCryptocurrencyContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCharityCryptocurrencyContainerQFrameHLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCharityCryptocurrencyContainerQFrameHLayout.addItem(self.donationsCharityCryptocurrencyContainerQFrameHLSpacer)

        self.donationsCharityCryptocurrencyQFrame = QFrame(self.donationsCharityCryptocurrencyContainerQFrame)
        self.donationsCharityCryptocurrencyQFrame.setObjectName(u"donationsCharityCryptocurrencyQFrame")
        self.donationsCharityCryptocurrencyQFrame.setMinimumSize(QSize(150, 0))
        self.donationsCharityCryptocurrencyQFrameVLayout = QVBoxLayout(self.donationsCharityCryptocurrencyQFrame)
        self.donationsCharityCryptocurrencyQFrameVLayout.setSpacing(15)
        self.donationsCharityCryptocurrencyQFrameVLayout.setObjectName(u"donationsCharityCryptocurrencyQFrameVLayout")
        self.donationsCharityCryptocurrencyQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.donationsCharityCryptocurrencyQLabel = QLabel(self.donationsCharityCryptocurrencyQFrame)
        self.donationsCharityCryptocurrencyQLabel.setObjectName(u"donationsCharityCryptocurrencyQLabel")

        self.donationsCharityCryptocurrencyQFrameVLayout.addWidget(self.donationsCharityCryptocurrencyQLabel, 0, Qt.AlignHCenter)

        self.donationsCharityCryptocurrencyQComboBox = QComboBox(self.donationsCharityCryptocurrencyQFrame)
        self.donationsCharityCryptocurrencyQComboBox.setObjectName(u"donationsCharityCryptocurrencyQComboBox")

        self.donationsCharityCryptocurrencyQFrameVLayout.addWidget(self.donationsCharityCryptocurrencyQComboBox)


        self.donationsCharityCryptocurrencyContainerQFrameHLayout.addWidget(self.donationsCharityCryptocurrencyQFrame)

        self.donationsCharityCryptocurrencyContainerQFrameHRSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.donationsCharityCryptocurrencyContainerQFrameHLayout.addItem(self.donationsCharityCryptocurrencyContainerQFrameHRSpacer)


        self.donationsCharityQWidgetVLayout.addWidget(self.donationsCharityCryptocurrencyContainerQFrame)

        self.donationsCharityCaptionContainerQFrame = QFrame(self.donationsCharityQWidget)
        self.donationsCharityCaptionContainerQFrame.setObjectName(u"donationsCharityCaptionContainerQFrame")
        self.donationsCharityCaptionContainerQFrameHLayout = QHBoxLayout(self.donationsCharityCaptionContainerQFrame)
        self.donationsCharityCaptionContainerQFrameHLayout.setObjectName(u"donationsCharityCaptionContainerQFrameHLayout")
        self.donationsCharityCaptionContainerQFrameHLayout.setContentsMargins(50, 0, 50, 0)
        self.donationsCharityCaptionQLabel = QLabel(self.donationsCharityCaptionContainerQFrame)
        self.donationsCharityCaptionQLabel.setObjectName(u"donationsCharityCaptionQLabel")

        self.donationsCharityCaptionContainerQFrameHLayout.addWidget(self.donationsCharityCaptionQLabel)


        self.donationsCharityQWidgetVLayout.addWidget(self.donationsCharityCaptionContainerQFrame)

        self.donationsCharityQWidgetVMSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.donationsCharityQWidgetVLayout.addItem(self.donationsCharityQWidgetVMSpacer)

        self.donationsCharityQWidgetVBSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.donationsCharityQWidgetVLayout.addItem(self.donationsCharityQWidgetVBSpacer)

        self.stackedWidget.addWidget(self.donationsCharityQWidget)

        self.FormVLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.donationsQLabel.setText(QCoreApplication.translate("Form", u"Donations", None))
        self.donationsCoreTeamQPushButton.setText(QCoreApplication.translate("Form", u"Team", None))
        self.donationsCharityQPushButton.setText(QCoreApplication.translate("Form", u"Charity", None))
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

