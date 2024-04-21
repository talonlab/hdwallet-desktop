# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hdwalletQXYKgh.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 501)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.hdWalletContainerQFrame = QFrame(self.centralwidget)
        self.hdWalletContainerQFrame.setObjectName(u"hdWalletContainerQFrame")
        self.hdWalletContainerQFrame.setMinimumSize(QSize(600, 0))
        self.hdWalletContainerQFrame.setMaximumSize(QSize(600, 16777215))
        self.hdWalletContainerQFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.hdWalletContainerQFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.hdWalletContainerQFrame)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(525, 47))
        self.frame_22.setMaximumSize(QSize(16777215, 47))
        self.horizontalLayout_6 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 15, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.verticalLayout_20 = QVBoxLayout(self.frame_23)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.frame_23)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.pushButton_4 = QPushButton(self.frame_22)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_22)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.frame_22)

        self.frame = QFrame(self.hdWalletContainerQFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(525, 0))
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_10)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.hdQComboBox = QComboBox(self.frame_9)
        self.hdQComboBox.addItem("")
        self.hdQComboBox.addItem("")
        self.hdQComboBox.addItem("")
        self.hdQComboBox.addItem("")
        self.hdQComboBox.addItem("")
        self.hdQComboBox.addItem("")
        self.hdQComboBox.addItem("")
        self.hdQComboBox.addItem("")
        self.hdQComboBox.addItem("")
        self.hdQComboBox.addItem("")
        self.hdQComboBox.setObjectName(u"hdQComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hdQComboBox.sizePolicy().hasHeightForWidth())
        self.hdQComboBox.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.hdQComboBox)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.fromContainerQFrame = QFrame(self.frame_3)
        self.fromContainerQFrame.setObjectName(u"fromContainerQFrame")
        self.verticalLayout_6 = QVBoxLayout(self.fromContainerQFrame)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.fromContainerQFrame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.fromQComboBox = QComboBox(self.fromContainerQFrame)
        self.fromQComboBox.addItem("")
        self.fromQComboBox.addItem("")
        self.fromQComboBox.addItem("")
        self.fromQComboBox.addItem("")
        self.fromQComboBox.addItem("")
        self.fromQComboBox.addItem("")
        self.fromQComboBox.addItem("")
        self.fromQComboBox.addItem("")
        self.fromQComboBox.setObjectName(u"fromQComboBox")
        sizePolicy.setHeightForWidth(self.fromQComboBox.sizePolicy().hasHeightForWidth())
        self.fromQComboBox.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.fromQComboBox)


        self.horizontalLayout_2.addWidget(self.fromContainerQFrame)

        self.CryptocurrencyQFrame = QFrame(self.frame_3)
        self.CryptocurrencyQFrame.setObjectName(u"CryptocurrencyQFrame")
        self.CryptocurrencyVLayout = QVBoxLayout(self.CryptocurrencyQFrame)
        self.CryptocurrencyVLayout.setSpacing(5)
        self.CryptocurrencyVLayout.setObjectName(u"CryptocurrencyVLayout")
        self.CryptocurrencyVLayout.setContentsMargins(0, 0, 0, 0)
        self.CryptocurrencyLabelQFrame = QFrame(self.CryptocurrencyQFrame)
        self.CryptocurrencyLabelQFrame.setObjectName(u"CryptocurrencyLabelQFrame")
        self.CryptocurrencyLabelHLayout = QHBoxLayout(self.CryptocurrencyLabelQFrame)
        self.CryptocurrencyLabelHLayout.setSpacing(15)
        self.CryptocurrencyLabelHLayout.setObjectName(u"CryptocurrencyLabelHLayout")
        self.CryptocurrencyLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.CryptocurrencyLabelQLabel = QLabel(self.CryptocurrencyLabelQFrame)
        self.CryptocurrencyLabelQLabel.setObjectName(u"CryptocurrencyLabelQLabel")

        self.CryptocurrencyLabelHLayout.addWidget(self.CryptocurrencyLabelQLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.CryptocurrencyLabelHLayout.addItem(self.horizontalSpacer_3)


        self.CryptocurrencyVLayout.addWidget(self.CryptocurrencyLabelQFrame)

        self.CryptocurrencyQComboBox = QComboBox(self.CryptocurrencyQFrame)
        self.CryptocurrencyQComboBox.addItem("")
        self.CryptocurrencyQComboBox.addItem("")
        self.CryptocurrencyQComboBox.addItem("")
        self.CryptocurrencyQComboBox.addItem("")
        self.CryptocurrencyQComboBox.setObjectName(u"CryptocurrencyQComboBox")

        self.CryptocurrencyVLayout.addWidget(self.CryptocurrencyQComboBox)


        self.horizontalLayout_2.addWidget(self.CryptocurrencyQFrame)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.BIPS = QWidget()
        self.BIPS.setObjectName(u"BIPS")
        self.verticalLayout_21 = QVBoxLayout(self.BIPS)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.fromQStackedWidget_2 = QStackedWidget(self.BIPS)
        self.fromQStackedWidget_2.setObjectName(u"fromQStackedWidget_2")
        self.fromEntropyQStackedWidget_2 = QWidget()
        self.fromEntropyQStackedWidget_2.setObjectName(u"fromEntropyQStackedWidget_2")
        self.verticalLayout_22 = QVBoxLayout(self.fromEntropyQStackedWidget_2)
        self.verticalLayout_22.setSpacing(15)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.fromEntropyQStackedWidget_2)
        self.frame_25.setObjectName(u"frame_25")
        self.verticalLayout_23 = QVBoxLayout(self.frame_25)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.EntropyQFrame_2 = QFrame(self.frame_25)
        self.EntropyQFrame_2.setObjectName(u"EntropyQFrame_2")
        self.EntropyQFrame_2.setMinimumSize(QSize(400, 0))
        self.EntropyVLayout_3 = QVBoxLayout(self.EntropyQFrame_2)
        self.EntropyVLayout_3.setSpacing(15)
        self.EntropyVLayout_3.setObjectName(u"EntropyVLayout_3")
        self.EntropyVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.EntropyLabelQFrame_3 = QFrame(self.EntropyQFrame_2)
        self.EntropyLabelQFrame_3.setObjectName(u"EntropyLabelQFrame_3")
        self.EntropyLabelHLayout_3 = QHBoxLayout(self.EntropyLabelQFrame_3)
        self.EntropyLabelHLayout_3.setSpacing(15)
        self.EntropyLabelHLayout_3.setObjectName(u"EntropyLabelHLayout_3")
        self.EntropyLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLabel_3 = QLabel(self.EntropyLabelQFrame_3)
        self.EntropyQLabel_3.setObjectName(u"EntropyQLabel_3")

        self.EntropyLabelHLayout_3.addWidget(self.EntropyQLabel_3)

        self.EntropyLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_3.addItem(self.EntropyLabelHSpacer_3)


        self.EntropyVLayout_3.addWidget(self.EntropyLabelQFrame_3)


        self.verticalLayout_23.addWidget(self.EntropyQFrame_2)

        self.EGenerateQFrame_2 = QFrame(self.frame_25)
        self.EGenerateQFrame_2.setObjectName(u"EGenerateQFrame_2")
        self.horizontalLayout_23 = QHBoxLayout(self.EGenerateQFrame_2)
        self.horizontalLayout_23.setSpacing(15)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLineEdit_3 = QLineEdit(self.EGenerateQFrame_2)
        self.EntropyQLineEdit_3.setObjectName(u"EntropyQLineEdit_3")

        self.horizontalLayout_23.addWidget(self.EntropyQLineEdit_3)

        self.EGenerateQPushButton_3 = QPushButton(self.EGenerateQFrame_2)
        self.EGenerateQPushButton_3.setObjectName(u"EGenerateQPushButton_3")

        self.horizontalLayout_23.addWidget(self.EGenerateQPushButton_3)


        self.verticalLayout_23.addWidget(self.EGenerateQFrame_2)


        self.verticalLayout_22.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.fromEntropyQStackedWidget_2)
        self.frame_26.setObjectName(u"frame_26")
        self.horizontalLayout_24 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_24.setSpacing(15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_4 = QFrame(self.frame_26)
        self.ClientQFrame_4.setObjectName(u"ClientQFrame_4")
        self.ClientQFrame_4.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_4 = QVBoxLayout(self.ClientQFrame_4)
        self.ClientVLayout_4.setSpacing(5)
        self.ClientVLayout_4.setObjectName(u"ClientVLayout_4")
        self.ClientVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_4 = QFrame(self.ClientQFrame_4)
        self.ClientLabelQFrame_4.setObjectName(u"ClientLabelQFrame_4")
        self.MStrengthLabelHLayout_6 = QHBoxLayout(self.ClientLabelQFrame_4)
        self.MStrengthLabelHLayout_6.setSpacing(15)
        self.MStrengthLabelHLayout_6.setObjectName(u"MStrengthLabelHLayout_6")
        self.MStrengthLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_4 = QLabel(self.ClientLabelQFrame_4)
        self.ClientQLabel_4.setObjectName(u"ClientQLabel_4")

        self.MStrengthLabelHLayout_6.addWidget(self.ClientQLabel_4)

        self.ClientLabelHSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_6.addItem(self.ClientLabelHSpacer_4)


        self.ClientVLayout_4.addWidget(self.ClientLabelQFrame_4)

        self.ClientQComboBox_4 = QComboBox(self.ClientQFrame_4)
        self.ClientQComboBox_4.addItem("")
        self.ClientQComboBox_4.addItem("")
        self.ClientQComboBox_4.addItem("")
        self.ClientQComboBox_4.addItem("")
        self.ClientQComboBox_4.addItem("")
        self.ClientQComboBox_4.addItem("")
        self.ClientQComboBox_4.setObjectName(u"ClientQComboBox_4")

        self.ClientVLayout_4.addWidget(self.ClientQComboBox_4)


        self.horizontalLayout_24.addWidget(self.ClientQFrame_4)

        self.EPassphraseQFrame_2 = QFrame(self.frame_26)
        self.EPassphraseQFrame_2.setObjectName(u"EPassphraseQFrame_2")
        self.EPassphraseVLayout_3 = QVBoxLayout(self.EPassphraseQFrame_2)
        self.EPassphraseVLayout_3.setSpacing(5)
        self.EPassphraseVLayout_3.setObjectName(u"EPassphraseVLayout_3")
        self.EPassphraseVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseLabelQFrame_2 = QFrame(self.EPassphraseQFrame_2)
        self.EPassphraseLabelQFrame_2.setObjectName(u"EPassphraseLabelQFrame_2")
        self.EPassphraseLabelHLayout_3 = QHBoxLayout(self.EPassphraseLabelQFrame_2)
        self.EPassphraseLabelHLayout_3.setSpacing(15)
        self.EPassphraseLabelHLayout_3.setObjectName(u"EPassphraseLabelHLayout_3")
        self.EPassphraseLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLabel_2 = QLabel(self.EPassphraseLabelQFrame_2)
        self.EPassphraseQLabel_2.setObjectName(u"EPassphraseQLabel_2")

        self.EPassphraseLabelHLayout_3.addWidget(self.EPassphraseQLabel_2)

        self.EPassphraseLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_3.addItem(self.EPassphraseLabelHSpacer_2)


        self.EPassphraseVLayout_3.addWidget(self.EPassphraseLabelQFrame_2)

        self.frame_27 = QFrame(self.EPassphraseQFrame_2)
        self.frame_27.setObjectName(u"frame_27")
        self.horizontalLayout_25 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_25.setSpacing(15)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLineEdit_2 = QLineEdit(self.frame_27)
        self.EPassphraseQLineEdit_2.setObjectName(u"EPassphraseQLineEdit_2")

        self.horizontalLayout_25.addWidget(self.EPassphraseQLineEdit_2)

        self.pushButton_6 = QPushButton(self.frame_27)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_25.addWidget(self.pushButton_6)


        self.EPassphraseVLayout_3.addWidget(self.frame_27)


        self.horizontalLayout_24.addWidget(self.EPassphraseQFrame_2)


        self.verticalLayout_22.addWidget(self.frame_26)

        self.frame_28 = QFrame(self.fromEntropyQStackedWidget_2)
        self.frame_28.setObjectName(u"frame_28")
        self.horizontalLayout_26 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQFrame_2 = QFrame(self.frame_28)
        self.ELanguageQFrame_2.setObjectName(u"ELanguageQFrame_2")
        self.ELanguageVLayout_2 = QVBoxLayout(self.ELanguageQFrame_2)
        self.ELanguageVLayout_2.setSpacing(5)
        self.ELanguageVLayout_2.setObjectName(u"ELanguageVLayout_2")
        self.ELanguageVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ELanguageLabelQFrame_2 = QFrame(self.ELanguageQFrame_2)
        self.ELanguageLabelQFrame_2.setObjectName(u"ELanguageLabelQFrame_2")
        self.ELanguageLabelHLayout_2 = QHBoxLayout(self.ELanguageLabelQFrame_2)
        self.ELanguageLabelHLayout_2.setSpacing(15)
        self.ELanguageLabelHLayout_2.setObjectName(u"ELanguageLabelHLayout_2")
        self.ELanguageLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQLabel_2 = QLabel(self.ELanguageLabelQFrame_2)
        self.ELanguageQLabel_2.setObjectName(u"ELanguageQLabel_2")

        self.ELanguageLabelHLayout_2.addWidget(self.ELanguageQLabel_2)

        self.ELanguageLabelHSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout_2.addItem(self.ELanguageLabelHSpacer_2)


        self.ELanguageVLayout_2.addWidget(self.ELanguageLabelQFrame_2)

        self.ELanguageQComboBox_2 = QComboBox(self.ELanguageQFrame_2)
        self.ELanguageQComboBox_2.addItem("")
        self.ELanguageQComboBox_2.addItem("")
        self.ELanguageQComboBox_2.addItem("")
        self.ELanguageQComboBox_2.addItem("")
        self.ELanguageQComboBox_2.addItem("")
        self.ELanguageQComboBox_2.addItem("")
        self.ELanguageQComboBox_2.addItem("")
        self.ELanguageQComboBox_2.addItem("")
        self.ELanguageQComboBox_2.setObjectName(u"ELanguageQComboBox_2")

        self.ELanguageVLayout_2.addWidget(self.ELanguageQComboBox_2)


        self.horizontalLayout_26.addWidget(self.ELanguageQFrame_2)

        self.EWordsQFrame_2 = QFrame(self.frame_28)
        self.EWordsQFrame_2.setObjectName(u"EWordsQFrame_2")
        self.EStrengthVLayout_2 = QVBoxLayout(self.EWordsQFrame_2)
        self.EStrengthVLayout_2.setSpacing(5)
        self.EStrengthVLayout_2.setObjectName(u"EStrengthVLayout_2")
        self.EStrengthVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.EWordsLabelQFrame_2 = QFrame(self.EWordsQFrame_2)
        self.EWordsLabelQFrame_2.setObjectName(u"EWordsLabelQFrame_2")
        self.EStrengthLabelHLayout_2 = QHBoxLayout(self.EWordsLabelQFrame_2)
        self.EStrengthLabelHLayout_2.setSpacing(15)
        self.EStrengthLabelHLayout_2.setObjectName(u"EStrengthLabelHLayout_2")
        self.EStrengthLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.EWordsQLabel_2 = QLabel(self.EWordsLabelQFrame_2)
        self.EWordsQLabel_2.setObjectName(u"EWordsQLabel_2")

        self.EStrengthLabelHLayout_2.addWidget(self.EWordsQLabel_2)

        self.EWordsLabelHSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout_2.addItem(self.EWordsLabelHSpacer_2)


        self.EStrengthVLayout_2.addWidget(self.EWordsLabelQFrame_2)

        self.EWordsQComboBox_2 = QComboBox(self.EWordsQFrame_2)
        self.EWordsQComboBox_2.addItem("")
        self.EWordsQComboBox_2.addItem("")
        self.EWordsQComboBox_2.addItem("")
        self.EWordsQComboBox_2.addItem("")
        self.EWordsQComboBox_2.addItem("")
        self.EWordsQComboBox_2.setObjectName(u"EWordsQComboBox_2")

        self.EStrengthVLayout_2.addWidget(self.EWordsQComboBox_2)


        self.horizontalLayout_26.addWidget(self.EWordsQFrame_2)


        self.verticalLayout_22.addWidget(self.frame_28)

        self.fromQStackedWidget_2.addWidget(self.fromEntropyQStackedWidget_2)
        self.fromMnemonicQStackedWidget_2 = QWidget()
        self.fromMnemonicQStackedWidget_2.setObjectName(u"fromMnemonicQStackedWidget_2")
        self.verticalLayout_24 = QVBoxLayout(self.fromMnemonicQStackedWidget_2)
        self.verticalLayout_24.setSpacing(15)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQFrame_2 = QFrame(self.fromMnemonicQStackedWidget_2)
        self.MnemonicQFrame_2.setObjectName(u"MnemonicQFrame_2")
        self.MnemonicVLayout_2 = QVBoxLayout(self.MnemonicQFrame_2)
        self.MnemonicVLayout_2.setSpacing(5)
        self.MnemonicVLayout_2.setObjectName(u"MnemonicVLayout_2")
        self.MnemonicVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MnemonicLabelQFrame_2 = QFrame(self.MnemonicQFrame_2)
        self.MnemonicLabelQFrame_2.setObjectName(u"MnemonicLabelQFrame_2")
        self.MnemonicLabelHLayout_2 = QHBoxLayout(self.MnemonicLabelQFrame_2)
        self.MnemonicLabelHLayout_2.setSpacing(15)
        self.MnemonicLabelHLayout_2.setObjectName(u"MnemonicLabelHLayout_2")
        self.MnemonicLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLabel_2 = QLabel(self.MnemonicLabelQFrame_2)
        self.MnemonicQLabel_2.setObjectName(u"MnemonicQLabel_2")

        self.MnemonicLabelHLayout_2.addWidget(self.MnemonicQLabel_2)

        self.MnemonicLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout_2.addItem(self.MnemonicLabelHSpacer_2)


        self.MnemonicVLayout_2.addWidget(self.MnemonicLabelQFrame_2)

        self.frame_29 = QFrame(self.MnemonicQFrame_2)
        self.frame_29.setObjectName(u"frame_29")
        self.horizontalLayout_27 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_27.setSpacing(15)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLineEdit_2 = QLineEdit(self.frame_29)
        self.MnemonicQLineEdit_2.setObjectName(u"MnemonicQLineEdit_2")

        self.horizontalLayout_27.addWidget(self.MnemonicQLineEdit_2)

        self.MGenerateQFrame_2 = QFrame(self.frame_29)
        self.MGenerateQFrame_2.setObjectName(u"MGenerateQFrame_2")
        self.GenerateMnemonicVLayout_2 = QVBoxLayout(self.MGenerateQFrame_2)
        self.GenerateMnemonicVLayout_2.setSpacing(15)
        self.GenerateMnemonicVLayout_2.setObjectName(u"GenerateMnemonicVLayout_2")
        self.GenerateMnemonicVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MGenerateQPushButton_2 = QPushButton(self.MGenerateQFrame_2)
        self.MGenerateQPushButton_2.setObjectName(u"MGenerateQPushButton_2")

        self.GenerateMnemonicVLayout_2.addWidget(self.MGenerateQPushButton_2)


        self.horizontalLayout_27.addWidget(self.MGenerateQFrame_2)


        self.MnemonicVLayout_2.addWidget(self.frame_29)


        self.verticalLayout_24.addWidget(self.MnemonicQFrame_2)

        self.frame_30 = QFrame(self.fromMnemonicQStackedWidget_2)
        self.frame_30.setObjectName(u"frame_30")
        self.horizontalLayout_28 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_28.setSpacing(15)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_5 = QFrame(self.frame_30)
        self.ClientQFrame_5.setObjectName(u"ClientQFrame_5")
        self.ClientQFrame_5.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_5 = QVBoxLayout(self.ClientQFrame_5)
        self.ClientVLayout_5.setSpacing(5)
        self.ClientVLayout_5.setObjectName(u"ClientVLayout_5")
        self.ClientVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_5 = QFrame(self.ClientQFrame_5)
        self.ClientLabelQFrame_5.setObjectName(u"ClientLabelQFrame_5")
        self.MStrengthLabelHLayout_7 = QHBoxLayout(self.ClientLabelQFrame_5)
        self.MStrengthLabelHLayout_7.setSpacing(15)
        self.MStrengthLabelHLayout_7.setObjectName(u"MStrengthLabelHLayout_7")
        self.MStrengthLabelHLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_5 = QLabel(self.ClientLabelQFrame_5)
        self.ClientQLabel_5.setObjectName(u"ClientQLabel_5")

        self.MStrengthLabelHLayout_7.addWidget(self.ClientQLabel_5)

        self.ClientLabelHSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_7.addItem(self.ClientLabelHSpacer_5)


        self.ClientVLayout_5.addWidget(self.ClientLabelQFrame_5)

        self.ClientQComboBox_5 = QComboBox(self.ClientQFrame_5)
        self.ClientQComboBox_5.addItem("")
        self.ClientQComboBox_5.addItem("")
        self.ClientQComboBox_5.addItem("")
        self.ClientQComboBox_5.addItem("")
        self.ClientQComboBox_5.addItem("")
        self.ClientQComboBox_5.addItem("")
        self.ClientQComboBox_5.setObjectName(u"ClientQComboBox_5")

        self.ClientVLayout_5.addWidget(self.ClientQComboBox_5)


        self.horizontalLayout_28.addWidget(self.ClientQFrame_5)

        self.MPassphraseQFrame_2 = QFrame(self.frame_30)
        self.MPassphraseQFrame_2.setObjectName(u"MPassphraseQFrame_2")
        self.EPassphraseVLayout_4 = QVBoxLayout(self.MPassphraseQFrame_2)
        self.EPassphraseVLayout_4.setSpacing(5)
        self.EPassphraseVLayout_4.setObjectName(u"EPassphraseVLayout_4")
        self.EPassphraseVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseLabelQFrame_2 = QFrame(self.MPassphraseQFrame_2)
        self.MPassphraseLabelQFrame_2.setObjectName(u"MPassphraseLabelQFrame_2")
        self.MPassphraseLabelHLayout_2 = QHBoxLayout(self.MPassphraseLabelQFrame_2)
        self.MPassphraseLabelHLayout_2.setSpacing(15)
        self.MPassphraseLabelHLayout_2.setObjectName(u"MPassphraseLabelHLayout_2")
        self.MPassphraseLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLabel_2 = QLabel(self.MPassphraseLabelQFrame_2)
        self.MPassphraseQLabel_2.setObjectName(u"MPassphraseQLabel_2")

        self.MPassphraseLabelHLayout_2.addWidget(self.MPassphraseQLabel_2)

        self.MPassphraseLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout_2.addItem(self.MPassphraseLabelHSpacer_2)


        self.EPassphraseVLayout_4.addWidget(self.MPassphraseLabelQFrame_2)

        self.frame_31 = QFrame(self.MPassphraseQFrame_2)
        self.frame_31.setObjectName(u"frame_31")
        self.horizontalLayout_29 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_29.setSpacing(15)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLineEdit_2 = QLineEdit(self.frame_31)
        self.MPassphraseQLineEdit_2.setObjectName(u"MPassphraseQLineEdit_2")

        self.horizontalLayout_29.addWidget(self.MPassphraseQLineEdit_2)

        self.pushButton_7 = QPushButton(self.frame_31)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_29.addWidget(self.pushButton_7)


        self.EPassphraseVLayout_4.addWidget(self.frame_31)


        self.horizontalLayout_28.addWidget(self.MPassphraseQFrame_2)


        self.verticalLayout_24.addWidget(self.frame_30)

        self.frame_32 = QFrame(self.fromMnemonicQStackedWidget_2)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_30.setSpacing(15)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQFrame_2 = QFrame(self.frame_32)
        self.MLanguageQFrame_2.setObjectName(u"MLanguageQFrame_2")
        self.MLanguageVLayout_2 = QVBoxLayout(self.MLanguageQFrame_2)
        self.MLanguageVLayout_2.setSpacing(5)
        self.MLanguageVLayout_2.setObjectName(u"MLanguageVLayout_2")
        self.MLanguageVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MLanguageLabelQWidget_2 = QWidget(self.MLanguageQFrame_2)
        self.MLanguageLabelQWidget_2.setObjectName(u"MLanguageLabelQWidget_2")
        self.MLanguageLabelHLayout_2 = QHBoxLayout(self.MLanguageLabelQWidget_2)
        self.MLanguageLabelHLayout_2.setSpacing(15)
        self.MLanguageLabelHLayout_2.setObjectName(u"MLanguageLabelHLayout_2")
        self.MLanguageLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQLabel_2 = QLabel(self.MLanguageLabelQWidget_2)
        self.MLanguageQLabel_2.setObjectName(u"MLanguageQLabel_2")

        self.MLanguageLabelHLayout_2.addWidget(self.MLanguageQLabel_2)

        self.MLanguageLabelHSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MLanguageLabelHLayout_2.addItem(self.MLanguageLabelHSpacer_2)


        self.MLanguageVLayout_2.addWidget(self.MLanguageLabelQWidget_2)

        self.MLanguageQComboBox_2 = QComboBox(self.MLanguageQFrame_2)
        self.MLanguageQComboBox_2.addItem("")
        self.MLanguageQComboBox_2.addItem("")
        self.MLanguageQComboBox_2.addItem("")
        self.MLanguageQComboBox_2.addItem("")
        self.MLanguageQComboBox_2.addItem("")
        self.MLanguageQComboBox_2.addItem("")
        self.MLanguageQComboBox_2.addItem("")
        self.MLanguageQComboBox_2.addItem("")
        self.MLanguageQComboBox_2.setObjectName(u"MLanguageQComboBox_2")

        self.MLanguageVLayout_2.addWidget(self.MLanguageQComboBox_2)


        self.horizontalLayout_30.addWidget(self.MLanguageQFrame_2)

        self.MWordsQFrame_2 = QFrame(self.frame_32)
        self.MWordsQFrame_2.setObjectName(u"MWordsQFrame_2")
        self.MStrengthVLayout_2 = QVBoxLayout(self.MWordsQFrame_2)
        self.MStrengthVLayout_2.setSpacing(5)
        self.MStrengthVLayout_2.setObjectName(u"MStrengthVLayout_2")
        self.MStrengthVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MWordsLabelQFrame_2 = QFrame(self.MWordsQFrame_2)
        self.MWordsLabelQFrame_2.setObjectName(u"MWordsLabelQFrame_2")
        self.MStrengthLabelHLayout_2 = QHBoxLayout(self.MWordsLabelQFrame_2)
        self.MStrengthLabelHLayout_2.setSpacing(15)
        self.MStrengthLabelHLayout_2.setObjectName(u"MStrengthLabelHLayout_2")
        self.MStrengthLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MWordsQLabel_2 = QLabel(self.MWordsLabelQFrame_2)
        self.MWordsQLabel_2.setObjectName(u"MWordsQLabel_2")

        self.MStrengthLabelHLayout_2.addWidget(self.MWordsQLabel_2)

        self.MWordsLabelHSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_2.addItem(self.MWordsLabelHSpacer_2)


        self.MStrengthVLayout_2.addWidget(self.MWordsLabelQFrame_2)

        self.MWordsQComboBox_2 = QComboBox(self.MWordsQFrame_2)
        self.MWordsQComboBox_2.addItem("")
        self.MWordsQComboBox_2.setObjectName(u"MWordsQComboBox_2")

        self.MStrengthVLayout_2.addWidget(self.MWordsQComboBox_2)


        self.horizontalLayout_30.addWidget(self.MWordsQFrame_2)


        self.verticalLayout_24.addWidget(self.frame_32)

        self.fromQStackedWidget_2.addWidget(self.fromMnemonicQStackedWidget_2)
        self.fromSeedQStackedWidget_2 = QWidget()
        self.fromSeedQStackedWidget_2.setObjectName(u"fromSeedQStackedWidget_2")
        self.verticalLayout_25 = QVBoxLayout(self.fromSeedQStackedWidget_2)
        self.verticalLayout_25.setSpacing(15)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.SeedQFrame_2 = QFrame(self.fromSeedQStackedWidget_2)
        self.SeedQFrame_2.setObjectName(u"SeedQFrame_2")
        self.SeedQFrame_2.setMinimumSize(QSize(400, 0))
        self.SeedVLayout_2 = QVBoxLayout(self.SeedQFrame_2)
        self.SeedVLayout_2.setSpacing(5)
        self.SeedVLayout_2.setObjectName(u"SeedVLayout_2")
        self.SeedVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.SeedQFrame_2)
        self.frame_33.setObjectName(u"frame_33")
        self.horizontalLayout_31 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_31.setSpacing(15)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_6 = QFrame(self.frame_33)
        self.ClientQFrame_6.setObjectName(u"ClientQFrame_6")
        self.ClientQFrame_6.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_6 = QVBoxLayout(self.ClientQFrame_6)
        self.ClientVLayout_6.setSpacing(5)
        self.ClientVLayout_6.setObjectName(u"ClientVLayout_6")
        self.ClientVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_6 = QFrame(self.ClientQFrame_6)
        self.ClientLabelQFrame_6.setObjectName(u"ClientLabelQFrame_6")
        self.MStrengthLabelHLayout_8 = QHBoxLayout(self.ClientLabelQFrame_6)
        self.MStrengthLabelHLayout_8.setSpacing(15)
        self.MStrengthLabelHLayout_8.setObjectName(u"MStrengthLabelHLayout_8")
        self.MStrengthLabelHLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_6 = QLabel(self.ClientLabelQFrame_6)
        self.ClientQLabel_6.setObjectName(u"ClientQLabel_6")

        self.MStrengthLabelHLayout_8.addWidget(self.ClientQLabel_6)

        self.ClientLabelHSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_8.addItem(self.ClientLabelHSpacer_6)


        self.ClientVLayout_6.addWidget(self.ClientLabelQFrame_6)

        self.ClientQComboBox_6 = QComboBox(self.ClientQFrame_6)
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.setObjectName(u"ClientQComboBox_6")

        self.ClientVLayout_6.addWidget(self.ClientQComboBox_6)


        self.horizontalLayout_31.addWidget(self.ClientQFrame_6)

        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_34)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.SeedLabelQFrame_2 = QFrame(self.frame_34)
        self.SeedLabelQFrame_2.setObjectName(u"SeedLabelQFrame_2")
        self.SeedLabelHLayout_2 = QHBoxLayout(self.SeedLabelQFrame_2)
        self.SeedLabelHLayout_2.setSpacing(15)
        self.SeedLabelHLayout_2.setObjectName(u"SeedLabelHLayout_2")
        self.SeedLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SeedQLabel_2 = QLabel(self.SeedLabelQFrame_2)
        self.SeedQLabel_2.setObjectName(u"SeedQLabel_2")

        self.SeedLabelHLayout_2.addWidget(self.SeedQLabel_2)

        self.SeedLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout_2.addItem(self.SeedLabelHSpacer_2)


        self.verticalLayout_26.addWidget(self.SeedLabelQFrame_2)

        self.SeedQLineEdit_2 = QLineEdit(self.frame_34)
        self.SeedQLineEdit_2.setObjectName(u"SeedQLineEdit_2")

        self.verticalLayout_26.addWidget(self.SeedQLineEdit_2)


        self.horizontalLayout_31.addWidget(self.frame_34)


        self.SeedVLayout_2.addWidget(self.frame_33)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout_2.addItem(self.verticalSpacer_9)


        self.verticalLayout_25.addWidget(self.SeedQFrame_2)

        self.fromQStackedWidget_2.addWidget(self.fromSeedQStackedWidget_2)
        self.fromXPrivateKeyQStackedWidget_2 = QWidget()
        self.fromXPrivateKeyQStackedWidget_2.setObjectName(u"fromXPrivateKeyQStackedWidget_2")
        self.verticalLayout_27 = QVBoxLayout(self.fromXPrivateKeyQStackedWidget_2)
        self.verticalLayout_27.setSpacing(15)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQFrame_2 = QFrame(self.fromXPrivateKeyQStackedWidget_2)
        self.XPrivateKeyQFrame_2.setObjectName(u"XPrivateKeyQFrame_2")
        self.XPrivateKeyVLayout_2 = QVBoxLayout(self.XPrivateKeyQFrame_2)
        self.XPrivateKeyVLayout_2.setSpacing(5)
        self.XPrivateKeyVLayout_2.setObjectName(u"XPrivateKeyVLayout_2")
        self.XPrivateKeyVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyLabelQFrame_2 = QFrame(self.XPrivateKeyQFrame_2)
        self.XPrivateKeyLabelQFrame_2.setObjectName(u"XPrivateKeyLabelQFrame_2")
        self.XPrivateKeyLabelHLayout_2 = QHBoxLayout(self.XPrivateKeyLabelQFrame_2)
        self.XPrivateKeyLabelHLayout_2.setSpacing(15)
        self.XPrivateKeyLabelHLayout_2.setObjectName(u"XPrivateKeyLabelHLayout_2")
        self.XPrivateKeyLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQLabel_2 = QLabel(self.XPrivateKeyLabelQFrame_2)
        self.XPrivateKeyQLabel_2.setObjectName(u"XPrivateKeyQLabel_2")

        self.XPrivateKeyLabelHLayout_2.addWidget(self.XPrivateKeyQLabel_2)

        self.XPrivateKeyLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPrivateKeyLabelHLayout_2.addItem(self.XPrivateKeyLabelHSpacer_2)


        self.XPrivateKeyVLayout_2.addWidget(self.XPrivateKeyLabelQFrame_2)

        self.XPrivateKeyQLineEdit_2 = QLineEdit(self.XPrivateKeyQFrame_2)
        self.XPrivateKeyQLineEdit_2.setObjectName(u"XPrivateKeyQLineEdit_2")

        self.XPrivateKeyVLayout_2.addWidget(self.XPrivateKeyQLineEdit_2)


        self.verticalLayout_27.addWidget(self.XPrivateKeyQFrame_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_10)

        self.fromQStackedWidget_2.addWidget(self.fromXPrivateKeyQStackedWidget_2)
        self.fromXPublicKeyQStackedWidget_2 = QWidget()
        self.fromXPublicKeyQStackedWidget_2.setObjectName(u"fromXPublicKeyQStackedWidget_2")
        self.verticalLayout_28 = QVBoxLayout(self.fromXPublicKeyQStackedWidget_2)
        self.verticalLayout_28.setSpacing(15)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQFrame_2 = QFrame(self.fromXPublicKeyQStackedWidget_2)
        self.XPublicKeyQFrame_2.setObjectName(u"XPublicKeyQFrame_2")
        self.XPublicKeyVLayout_2 = QVBoxLayout(self.XPublicKeyQFrame_2)
        self.XPublicKeyVLayout_2.setSpacing(5)
        self.XPublicKeyVLayout_2.setObjectName(u"XPublicKeyVLayout_2")
        self.XPublicKeyVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyLabelQFrame_2 = QFrame(self.XPublicKeyQFrame_2)
        self.XPublicKeyLabelQFrame_2.setObjectName(u"XPublicKeyLabelQFrame_2")
        self.XPublicKeyLabelHLayout_2 = QHBoxLayout(self.XPublicKeyLabelQFrame_2)
        self.XPublicKeyLabelHLayout_2.setSpacing(15)
        self.XPublicKeyLabelHLayout_2.setObjectName(u"XPublicKeyLabelHLayout_2")
        self.XPublicKeyLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQLabel_2 = QLabel(self.XPublicKeyLabelQFrame_2)
        self.XPublicKeyQLabel_2.setObjectName(u"XPublicKeyQLabel_2")

        self.XPublicKeyLabelHLayout_2.addWidget(self.XPublicKeyQLabel_2)

        self.XPublicKeyLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPublicKeyLabelHLayout_2.addItem(self.XPublicKeyLabelHSpacer_2)


        self.XPublicKeyVLayout_2.addWidget(self.XPublicKeyLabelQFrame_2)

        self.XPublicKeyQLineEdit_2 = QLineEdit(self.XPublicKeyQFrame_2)
        self.XPublicKeyQLineEdit_2.setObjectName(u"XPublicKeyQLineEdit_2")

        self.XPublicKeyVLayout_2.addWidget(self.XPublicKeyQLineEdit_2)


        self.verticalLayout_28.addWidget(self.XPublicKeyQFrame_2)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_11)

        self.fromQStackedWidget_2.addWidget(self.fromXPublicKeyQStackedWidget_2)
        self.fromWIFQStackedWidget_2 = QWidget()
        self.fromWIFQStackedWidget_2.setObjectName(u"fromWIFQStackedWidget_2")
        self.verticalLayout_29 = QVBoxLayout(self.fromWIFQStackedWidget_2)
        self.verticalLayout_29.setSpacing(15)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.WIFQFrame_2 = QFrame(self.fromWIFQStackedWidget_2)
        self.WIFQFrame_2.setObjectName(u"WIFQFrame_2")
        self.WIFQFrame_2.setMinimumSize(QSize(400, 0))
        self.WIFVLayout_2 = QVBoxLayout(self.WIFQFrame_2)
        self.WIFVLayout_2.setSpacing(5)
        self.WIFVLayout_2.setObjectName(u"WIFVLayout_2")
        self.WIFVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.WIFLabelQFrame_2 = QFrame(self.WIFQFrame_2)
        self.WIFLabelQFrame_2.setObjectName(u"WIFLabelQFrame_2")
        self.WIFLabelHLayout_2 = QHBoxLayout(self.WIFLabelQFrame_2)
        self.WIFLabelHLayout_2.setSpacing(15)
        self.WIFLabelHLayout_2.setObjectName(u"WIFLabelHLayout_2")
        self.WIFLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.WIFQLabel_2 = QLabel(self.WIFLabelQFrame_2)
        self.WIFQLabel_2.setObjectName(u"WIFQLabel_2")

        self.WIFLabelHLayout_2.addWidget(self.WIFQLabel_2)

        self.WIFLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WIFLabelHLayout_2.addItem(self.WIFLabelHSpacer_2)


        self.WIFVLayout_2.addWidget(self.WIFLabelQFrame_2)

        self.WIFQLineEdit_2 = QLineEdit(self.WIFQFrame_2)
        self.WIFQLineEdit_2.setObjectName(u"WIFQLineEdit_2")

        self.WIFVLayout_2.addWidget(self.WIFQLineEdit_2)


        self.verticalLayout_29.addWidget(self.WIFQFrame_2)

        self.frame_35 = QFrame(self.fromWIFQStackedWidget_2)
        self.frame_35.setObjectName(u"frame_35")
        self.verticalLayout_30 = QVBoxLayout(self.frame_35)
        self.verticalLayout_30.setSpacing(5)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFPassphraseLabelQFrame_2 = QFrame(self.frame_35)
        self.BIP38EncryptedWIFPassphraseLabelQFrame_2.setObjectName(u"BIP38EncryptedWIFPassphraseLabelQFrame_2")
        self.EPassphraseLabelHLayout_4 = QHBoxLayout(self.BIP38EncryptedWIFPassphraseLabelQFrame_2)
        self.EPassphraseLabelHLayout_4.setSpacing(15)
        self.EPassphraseLabelHLayout_4.setObjectName(u"EPassphraseLabelHLayout_4")
        self.EPassphraseLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFQCheckBox_2 = QCheckBox(self.BIP38EncryptedWIFPassphraseLabelQFrame_2)
        self.BIP38EncryptedWIFQCheckBox_2.setObjectName(u"BIP38EncryptedWIFQCheckBox_2")

        self.EPassphraseLabelHLayout_4.addWidget(self.BIP38EncryptedWIFQCheckBox_2)

        self.BIP38EncryptedWIFPassphraseLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_4.addItem(self.BIP38EncryptedWIFPassphraseLabelHSpacer_2)


        self.verticalLayout_30.addWidget(self.BIP38EncryptedWIFPassphraseLabelQFrame_2)

        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.horizontalLayout_32 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_32.setSpacing(15)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.BIP38PassphraseQLineEdit_2 = QLineEdit(self.frame_36)
        self.BIP38PassphraseQLineEdit_2.setObjectName(u"BIP38PassphraseQLineEdit_2")

        self.horizontalLayout_32.addWidget(self.BIP38PassphraseQLineEdit_2)

        self.pushButton_8 = QPushButton(self.frame_36)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)

        self.horizontalLayout_32.addWidget(self.pushButton_8)


        self.verticalLayout_30.addWidget(self.frame_36)


        self.verticalLayout_29.addWidget(self.frame_35)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_12)

        self.fromQStackedWidget_2.addWidget(self.fromWIFQStackedWidget_2)
        self.fromPrivateKeyQStackedWidget_2 = QWidget()
        self.fromPrivateKeyQStackedWidget_2.setObjectName(u"fromPrivateKeyQStackedWidget_2")
        self.verticalLayout_31 = QVBoxLayout(self.fromPrivateKeyQStackedWidget_2)
        self.verticalLayout_31.setSpacing(15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQFrame_2 = QFrame(self.fromPrivateKeyQStackedWidget_2)
        self.PrivateKeyQFrame_2.setObjectName(u"PrivateKeyQFrame_2")
        self.PrivateKeyQFrame_2.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_2 = QVBoxLayout(self.PrivateKeyQFrame_2)
        self.PrivateKeyVLayout_2.setSpacing(5)
        self.PrivateKeyVLayout_2.setObjectName(u"PrivateKeyVLayout_2")
        self.PrivateKeyVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyLabelQFrame_2 = QFrame(self.PrivateKeyQFrame_2)
        self.PrivateKeyLabelQFrame_2.setObjectName(u"PrivateKeyLabelQFrame_2")
        self.PrivateKeyLabelHLayout_2 = QHBoxLayout(self.PrivateKeyLabelQFrame_2)
        self.PrivateKeyLabelHLayout_2.setSpacing(15)
        self.PrivateKeyLabelHLayout_2.setObjectName(u"PrivateKeyLabelHLayout_2")
        self.PrivateKeyLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQLabel_2 = QLabel(self.PrivateKeyLabelQFrame_2)
        self.PrivateKeyQLabel_2.setObjectName(u"PrivateKeyQLabel_2")

        self.PrivateKeyLabelHLayout_2.addWidget(self.PrivateKeyQLabel_2)

        self.PrivateKeyLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_2.addItem(self.PrivateKeyLabelHSpacer_2)


        self.PrivateKeyVLayout_2.addWidget(self.PrivateKeyLabelQFrame_2)

        self.PrivateKeyQLineEdit_2 = QLineEdit(self.PrivateKeyQFrame_2)
        self.PrivateKeyQLineEdit_2.setObjectName(u"PrivateKeyQLineEdit_2")

        self.PrivateKeyVLayout_2.addWidget(self.PrivateKeyQLineEdit_2)


        self.verticalLayout_31.addWidget(self.PrivateKeyQFrame_2)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_13)

        self.fromQStackedWidget_2.addWidget(self.fromPrivateKeyQStackedWidget_2)
        self.fromPublicKeyQStackedWidget_2 = QWidget()
        self.fromPublicKeyQStackedWidget_2.setObjectName(u"fromPublicKeyQStackedWidget_2")
        self.verticalLayout_32 = QVBoxLayout(self.fromPublicKeyQStackedWidget_2)
        self.verticalLayout_32.setSpacing(15)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQFrame_2 = QFrame(self.fromPublicKeyQStackedWidget_2)
        self.PublicKeyQFrame_2.setObjectName(u"PublicKeyQFrame_2")
        self.PublicKeyVLayout_2 = QVBoxLayout(self.PublicKeyQFrame_2)
        self.PublicKeyVLayout_2.setSpacing(5)
        self.PublicKeyVLayout_2.setObjectName(u"PublicKeyVLayout_2")
        self.PublicKeyVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyLabelQFrame_2 = QFrame(self.PublicKeyQFrame_2)
        self.PublicKeyLabelQFrame_2.setObjectName(u"PublicKeyLabelQFrame_2")
        self.PublicKeyLabelHLayout_2 = QHBoxLayout(self.PublicKeyLabelQFrame_2)
        self.PublicKeyLabelHLayout_2.setSpacing(15)
        self.PublicKeyLabelHLayout_2.setObjectName(u"PublicKeyLabelHLayout_2")
        self.PublicKeyLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQLabel_2 = QLabel(self.PublicKeyLabelQFrame_2)
        self.PublicKeyQLabel_2.setObjectName(u"PublicKeyQLabel_2")

        self.PublicKeyLabelHLayout_2.addWidget(self.PublicKeyQLabel_2)

        self.PublicKeyLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PublicKeyLabelHLayout_2.addItem(self.PublicKeyLabelHSpacer_2)


        self.PublicKeyVLayout_2.addWidget(self.PublicKeyLabelQFrame_2)

        self.PublicKeyQLineEdit_2 = QLineEdit(self.PublicKeyQFrame_2)
        self.PublicKeyQLineEdit_2.setObjectName(u"PublicKeyQLineEdit_2")

        self.PublicKeyVLayout_2.addWidget(self.PublicKeyQLineEdit_2)


        self.verticalLayout_32.addWidget(self.PublicKeyQFrame_2)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_14)

        self.fromQStackedWidget_2.addWidget(self.fromPublicKeyQStackedWidget_2)

        self.verticalLayout_21.addWidget(self.fromQStackedWidget_2)

        self.stackedWidget.addWidget(self.BIPS)
        self.Cardano = QWidget()
        self.Cardano.setObjectName(u"Cardano")
        self.verticalLayout_33 = QVBoxLayout(self.Cardano)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.fromQStackedWidget_3 = QStackedWidget(self.Cardano)
        self.fromQStackedWidget_3.setObjectName(u"fromQStackedWidget_3")
        self.fromEntropyQStackedWidget_3 = QWidget()
        self.fromEntropyQStackedWidget_3.setObjectName(u"fromEntropyQStackedWidget_3")
        self.verticalLayout_34 = QVBoxLayout(self.fromEntropyQStackedWidget_3)
        self.verticalLayout_34.setSpacing(15)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.fromEntropyQStackedWidget_3)
        self.frame_37.setObjectName(u"frame_37")
        self.verticalLayout_35 = QVBoxLayout(self.frame_37)
        self.verticalLayout_35.setSpacing(5)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.EntropyQFrame_3 = QFrame(self.frame_37)
        self.EntropyQFrame_3.setObjectName(u"EntropyQFrame_3")
        self.EntropyQFrame_3.setMinimumSize(QSize(400, 0))
        self.EntropyVLayout_4 = QVBoxLayout(self.EntropyQFrame_3)
        self.EntropyVLayout_4.setSpacing(15)
        self.EntropyVLayout_4.setObjectName(u"EntropyVLayout_4")
        self.EntropyVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.EntropyLabelQFrame_4 = QFrame(self.EntropyQFrame_3)
        self.EntropyLabelQFrame_4.setObjectName(u"EntropyLabelQFrame_4")
        self.EntropyLabelHLayout_4 = QHBoxLayout(self.EntropyLabelQFrame_4)
        self.EntropyLabelHLayout_4.setSpacing(15)
        self.EntropyLabelHLayout_4.setObjectName(u"EntropyLabelHLayout_4")
        self.EntropyLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLabel_4 = QLabel(self.EntropyLabelQFrame_4)
        self.EntropyQLabel_4.setObjectName(u"EntropyQLabel_4")

        self.EntropyLabelHLayout_4.addWidget(self.EntropyQLabel_4)

        self.EntropyLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_4.addItem(self.EntropyLabelHSpacer_4)


        self.EntropyVLayout_4.addWidget(self.EntropyLabelQFrame_4)


        self.verticalLayout_35.addWidget(self.EntropyQFrame_3)

        self.EGenerateQFrame_3 = QFrame(self.frame_37)
        self.EGenerateQFrame_3.setObjectName(u"EGenerateQFrame_3")
        self.horizontalLayout_33 = QHBoxLayout(self.EGenerateQFrame_3)
        self.horizontalLayout_33.setSpacing(15)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLineEdit_4 = QLineEdit(self.EGenerateQFrame_3)
        self.EntropyQLineEdit_4.setObjectName(u"EntropyQLineEdit_4")

        self.horizontalLayout_33.addWidget(self.EntropyQLineEdit_4)

        self.EGenerateQPushButton_4 = QPushButton(self.EGenerateQFrame_3)
        self.EGenerateQPushButton_4.setObjectName(u"EGenerateQPushButton_4")

        self.horizontalLayout_33.addWidget(self.EGenerateQPushButton_4)


        self.verticalLayout_35.addWidget(self.EGenerateQFrame_3)


        self.verticalLayout_34.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.fromEntropyQStackedWidget_3)
        self.frame_38.setObjectName(u"frame_38")
        self.horizontalLayout_34 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_34.setSpacing(15)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_7 = QFrame(self.frame_38)
        self.ClientQFrame_7.setObjectName(u"ClientQFrame_7")
        self.ClientQFrame_7.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_7 = QVBoxLayout(self.ClientQFrame_7)
        self.ClientVLayout_7.setSpacing(5)
        self.ClientVLayout_7.setObjectName(u"ClientVLayout_7")
        self.ClientVLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_7 = QFrame(self.ClientQFrame_7)
        self.ClientLabelQFrame_7.setObjectName(u"ClientLabelQFrame_7")
        self.MStrengthLabelHLayout_9 = QHBoxLayout(self.ClientLabelQFrame_7)
        self.MStrengthLabelHLayout_9.setSpacing(15)
        self.MStrengthLabelHLayout_9.setObjectName(u"MStrengthLabelHLayout_9")
        self.MStrengthLabelHLayout_9.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_7 = QLabel(self.ClientLabelQFrame_7)
        self.ClientQLabel_7.setObjectName(u"ClientQLabel_7")

        self.MStrengthLabelHLayout_9.addWidget(self.ClientQLabel_7)

        self.ClientLabelHSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_9.addItem(self.ClientLabelHSpacer_7)


        self.ClientVLayout_7.addWidget(self.ClientLabelQFrame_7)

        self.ClientQComboBox_7 = QComboBox(self.ClientQFrame_7)
        self.ClientQComboBox_7.addItem("")
        self.ClientQComboBox_7.addItem("")
        self.ClientQComboBox_7.addItem("")
        self.ClientQComboBox_7.addItem("")
        self.ClientQComboBox_7.addItem("")
        self.ClientQComboBox_7.addItem("")
        self.ClientQComboBox_7.setObjectName(u"ClientQComboBox_7")

        self.ClientVLayout_7.addWidget(self.ClientQComboBox_7)


        self.horizontalLayout_34.addWidget(self.ClientQFrame_7)

        self.EPassphraseQFrame_3 = QFrame(self.frame_38)
        self.EPassphraseQFrame_3.setObjectName(u"EPassphraseQFrame_3")
        self.EPassphraseVLayout_5 = QVBoxLayout(self.EPassphraseQFrame_3)
        self.EPassphraseVLayout_5.setSpacing(5)
        self.EPassphraseVLayout_5.setObjectName(u"EPassphraseVLayout_5")
        self.EPassphraseVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseLabelQFrame_3 = QFrame(self.EPassphraseQFrame_3)
        self.EPassphraseLabelQFrame_3.setObjectName(u"EPassphraseLabelQFrame_3")
        self.EPassphraseLabelHLayout_5 = QHBoxLayout(self.EPassphraseLabelQFrame_3)
        self.EPassphraseLabelHLayout_5.setSpacing(15)
        self.EPassphraseLabelHLayout_5.setObjectName(u"EPassphraseLabelHLayout_5")
        self.EPassphraseLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLabel_3 = QLabel(self.EPassphraseLabelQFrame_3)
        self.EPassphraseQLabel_3.setObjectName(u"EPassphraseQLabel_3")

        self.EPassphraseLabelHLayout_5.addWidget(self.EPassphraseQLabel_3)

        self.EPassphraseLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_5.addItem(self.EPassphraseLabelHSpacer_3)


        self.EPassphraseVLayout_5.addWidget(self.EPassphraseLabelQFrame_3)

        self.frame_39 = QFrame(self.EPassphraseQFrame_3)
        self.frame_39.setObjectName(u"frame_39")
        self.horizontalLayout_35 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_35.setSpacing(15)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLineEdit_3 = QLineEdit(self.frame_39)
        self.EPassphraseQLineEdit_3.setObjectName(u"EPassphraseQLineEdit_3")

        self.horizontalLayout_35.addWidget(self.EPassphraseQLineEdit_3)

        self.pushButton_9 = QPushButton(self.frame_39)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_35.addWidget(self.pushButton_9)


        self.EPassphraseVLayout_5.addWidget(self.frame_39)


        self.horizontalLayout_34.addWidget(self.EPassphraseQFrame_3)


        self.verticalLayout_34.addWidget(self.frame_38)

        self.frame_40 = QFrame(self.fromEntropyQStackedWidget_3)
        self.frame_40.setObjectName(u"frame_40")
        self.horizontalLayout_36 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_36.setSpacing(15)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQFrame_3 = QFrame(self.frame_40)
        self.ELanguageQFrame_3.setObjectName(u"ELanguageQFrame_3")
        self.ELanguageVLayout_3 = QVBoxLayout(self.ELanguageQFrame_3)
        self.ELanguageVLayout_3.setSpacing(5)
        self.ELanguageVLayout_3.setObjectName(u"ELanguageVLayout_3")
        self.ELanguageVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ELanguageLabelQFrame_3 = QFrame(self.ELanguageQFrame_3)
        self.ELanguageLabelQFrame_3.setObjectName(u"ELanguageLabelQFrame_3")
        self.ELanguageLabelHLayout_3 = QHBoxLayout(self.ELanguageLabelQFrame_3)
        self.ELanguageLabelHLayout_3.setSpacing(15)
        self.ELanguageLabelHLayout_3.setObjectName(u"ELanguageLabelHLayout_3")
        self.ELanguageLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQLabel_3 = QLabel(self.ELanguageLabelQFrame_3)
        self.ELanguageQLabel_3.setObjectName(u"ELanguageQLabel_3")

        self.ELanguageLabelHLayout_3.addWidget(self.ELanguageQLabel_3)

        self.ELanguageLabelHSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout_3.addItem(self.ELanguageLabelHSpacer_3)


        self.ELanguageVLayout_3.addWidget(self.ELanguageLabelQFrame_3)

        self.ELanguageQComboBox_3 = QComboBox(self.ELanguageQFrame_3)
        self.ELanguageQComboBox_3.addItem("")
        self.ELanguageQComboBox_3.addItem("")
        self.ELanguageQComboBox_3.addItem("")
        self.ELanguageQComboBox_3.addItem("")
        self.ELanguageQComboBox_3.addItem("")
        self.ELanguageQComboBox_3.addItem("")
        self.ELanguageQComboBox_3.addItem("")
        self.ELanguageQComboBox_3.addItem("")
        self.ELanguageQComboBox_3.setObjectName(u"ELanguageQComboBox_3")

        self.ELanguageVLayout_3.addWidget(self.ELanguageQComboBox_3)


        self.horizontalLayout_36.addWidget(self.ELanguageQFrame_3)

        self.EWordsQFrame_3 = QFrame(self.frame_40)
        self.EWordsQFrame_3.setObjectName(u"EWordsQFrame_3")
        self.EStrengthVLayout_3 = QVBoxLayout(self.EWordsQFrame_3)
        self.EStrengthVLayout_3.setSpacing(5)
        self.EStrengthVLayout_3.setObjectName(u"EStrengthVLayout_3")
        self.EStrengthVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.EWordsLabelQFrame_3 = QFrame(self.EWordsQFrame_3)
        self.EWordsLabelQFrame_3.setObjectName(u"EWordsLabelQFrame_3")
        self.EStrengthLabelHLayout_3 = QHBoxLayout(self.EWordsLabelQFrame_3)
        self.EStrengthLabelHLayout_3.setSpacing(15)
        self.EStrengthLabelHLayout_3.setObjectName(u"EStrengthLabelHLayout_3")
        self.EStrengthLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.EWordsQLabel_3 = QLabel(self.EWordsLabelQFrame_3)
        self.EWordsQLabel_3.setObjectName(u"EWordsQLabel_3")

        self.EStrengthLabelHLayout_3.addWidget(self.EWordsQLabel_3)

        self.EWordsLabelHSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout_3.addItem(self.EWordsLabelHSpacer_3)


        self.EStrengthVLayout_3.addWidget(self.EWordsLabelQFrame_3)

        self.EWordsQComboBox_3 = QComboBox(self.EWordsQFrame_3)
        self.EWordsQComboBox_3.addItem("")
        self.EWordsQComboBox_3.addItem("")
        self.EWordsQComboBox_3.addItem("")
        self.EWordsQComboBox_3.addItem("")
        self.EWordsQComboBox_3.addItem("")
        self.EWordsQComboBox_3.setObjectName(u"EWordsQComboBox_3")

        self.EStrengthVLayout_3.addWidget(self.EWordsQComboBox_3)


        self.horizontalLayout_36.addWidget(self.EWordsQFrame_3)


        self.verticalLayout_34.addWidget(self.frame_40)

        self.fromQStackedWidget_3.addWidget(self.fromEntropyQStackedWidget_3)
        self.fromMnemonicQStackedWidget_3 = QWidget()
        self.fromMnemonicQStackedWidget_3.setObjectName(u"fromMnemonicQStackedWidget_3")
        self.verticalLayout_36 = QVBoxLayout(self.fromMnemonicQStackedWidget_3)
        self.verticalLayout_36.setSpacing(15)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQFrame_3 = QFrame(self.fromMnemonicQStackedWidget_3)
        self.MnemonicQFrame_3.setObjectName(u"MnemonicQFrame_3")
        self.MnemonicVLayout_3 = QVBoxLayout(self.MnemonicQFrame_3)
        self.MnemonicVLayout_3.setSpacing(5)
        self.MnemonicVLayout_3.setObjectName(u"MnemonicVLayout_3")
        self.MnemonicVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MnemonicLabelQFrame_3 = QFrame(self.MnemonicQFrame_3)
        self.MnemonicLabelQFrame_3.setObjectName(u"MnemonicLabelQFrame_3")
        self.MnemonicLabelHLayout_3 = QHBoxLayout(self.MnemonicLabelQFrame_3)
        self.MnemonicLabelHLayout_3.setSpacing(15)
        self.MnemonicLabelHLayout_3.setObjectName(u"MnemonicLabelHLayout_3")
        self.MnemonicLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLabel_3 = QLabel(self.MnemonicLabelQFrame_3)
        self.MnemonicQLabel_3.setObjectName(u"MnemonicQLabel_3")

        self.MnemonicLabelHLayout_3.addWidget(self.MnemonicQLabel_3)

        self.MnemonicLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout_3.addItem(self.MnemonicLabelHSpacer_3)


        self.MnemonicVLayout_3.addWidget(self.MnemonicLabelQFrame_3)

        self.frame_41 = QFrame(self.MnemonicQFrame_3)
        self.frame_41.setObjectName(u"frame_41")
        self.horizontalLayout_37 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_37.setSpacing(15)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLineEdit_3 = QLineEdit(self.frame_41)
        self.MnemonicQLineEdit_3.setObjectName(u"MnemonicQLineEdit_3")

        self.horizontalLayout_37.addWidget(self.MnemonicQLineEdit_3)

        self.MGenerateQFrame_3 = QFrame(self.frame_41)
        self.MGenerateQFrame_3.setObjectName(u"MGenerateQFrame_3")
        self.GenerateMnemonicVLayout_3 = QVBoxLayout(self.MGenerateQFrame_3)
        self.GenerateMnemonicVLayout_3.setSpacing(15)
        self.GenerateMnemonicVLayout_3.setObjectName(u"GenerateMnemonicVLayout_3")
        self.GenerateMnemonicVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MGenerateQPushButton_3 = QPushButton(self.MGenerateQFrame_3)
        self.MGenerateQPushButton_3.setObjectName(u"MGenerateQPushButton_3")

        self.GenerateMnemonicVLayout_3.addWidget(self.MGenerateQPushButton_3)


        self.horizontalLayout_37.addWidget(self.MGenerateQFrame_3)


        self.MnemonicVLayout_3.addWidget(self.frame_41)


        self.verticalLayout_36.addWidget(self.MnemonicQFrame_3)

        self.frame_42 = QFrame(self.fromMnemonicQStackedWidget_3)
        self.frame_42.setObjectName(u"frame_42")
        self.horizontalLayout_38 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_38.setSpacing(15)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_8 = QFrame(self.frame_42)
        self.ClientQFrame_8.setObjectName(u"ClientQFrame_8")
        self.ClientQFrame_8.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_8 = QVBoxLayout(self.ClientQFrame_8)
        self.ClientVLayout_8.setSpacing(5)
        self.ClientVLayout_8.setObjectName(u"ClientVLayout_8")
        self.ClientVLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_8 = QFrame(self.ClientQFrame_8)
        self.ClientLabelQFrame_8.setObjectName(u"ClientLabelQFrame_8")
        self.MStrengthLabelHLayout_10 = QHBoxLayout(self.ClientLabelQFrame_8)
        self.MStrengthLabelHLayout_10.setSpacing(15)
        self.MStrengthLabelHLayout_10.setObjectName(u"MStrengthLabelHLayout_10")
        self.MStrengthLabelHLayout_10.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_8 = QLabel(self.ClientLabelQFrame_8)
        self.ClientQLabel_8.setObjectName(u"ClientQLabel_8")

        self.MStrengthLabelHLayout_10.addWidget(self.ClientQLabel_8)

        self.ClientLabelHSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_10.addItem(self.ClientLabelHSpacer_8)


        self.ClientVLayout_8.addWidget(self.ClientLabelQFrame_8)

        self.ClientQComboBox_8 = QComboBox(self.ClientQFrame_8)
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.setObjectName(u"ClientQComboBox_8")

        self.ClientVLayout_8.addWidget(self.ClientQComboBox_8)


        self.horizontalLayout_38.addWidget(self.ClientQFrame_8)

        self.MPassphraseQFrame_3 = QFrame(self.frame_42)
        self.MPassphraseQFrame_3.setObjectName(u"MPassphraseQFrame_3")
        self.EPassphraseVLayout_6 = QVBoxLayout(self.MPassphraseQFrame_3)
        self.EPassphraseVLayout_6.setSpacing(5)
        self.EPassphraseVLayout_6.setObjectName(u"EPassphraseVLayout_6")
        self.EPassphraseVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseLabelQFrame_3 = QFrame(self.MPassphraseQFrame_3)
        self.MPassphraseLabelQFrame_3.setObjectName(u"MPassphraseLabelQFrame_3")
        self.MPassphraseLabelHLayout_3 = QHBoxLayout(self.MPassphraseLabelQFrame_3)
        self.MPassphraseLabelHLayout_3.setSpacing(15)
        self.MPassphraseLabelHLayout_3.setObjectName(u"MPassphraseLabelHLayout_3")
        self.MPassphraseLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLabel_3 = QLabel(self.MPassphraseLabelQFrame_3)
        self.MPassphraseQLabel_3.setObjectName(u"MPassphraseQLabel_3")

        self.MPassphraseLabelHLayout_3.addWidget(self.MPassphraseQLabel_3)

        self.MPassphraseLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout_3.addItem(self.MPassphraseLabelHSpacer_3)


        self.EPassphraseVLayout_6.addWidget(self.MPassphraseLabelQFrame_3)

        self.frame_43 = QFrame(self.MPassphraseQFrame_3)
        self.frame_43.setObjectName(u"frame_43")
        self.horizontalLayout_39 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_39.setSpacing(15)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLineEdit_3 = QLineEdit(self.frame_43)
        self.MPassphraseQLineEdit_3.setObjectName(u"MPassphraseQLineEdit_3")

        self.horizontalLayout_39.addWidget(self.MPassphraseQLineEdit_3)

        self.pushButton_10 = QPushButton(self.frame_43)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_39.addWidget(self.pushButton_10)


        self.EPassphraseVLayout_6.addWidget(self.frame_43)


        self.horizontalLayout_38.addWidget(self.MPassphraseQFrame_3)


        self.verticalLayout_36.addWidget(self.frame_42)

        self.frame_44 = QFrame(self.fromMnemonicQStackedWidget_3)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_40.setSpacing(15)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQFrame_3 = QFrame(self.frame_44)
        self.MLanguageQFrame_3.setObjectName(u"MLanguageQFrame_3")
        self.MLanguageVLayout_3 = QVBoxLayout(self.MLanguageQFrame_3)
        self.MLanguageVLayout_3.setSpacing(5)
        self.MLanguageVLayout_3.setObjectName(u"MLanguageVLayout_3")
        self.MLanguageVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MLanguageLabelQWidget_3 = QWidget(self.MLanguageQFrame_3)
        self.MLanguageLabelQWidget_3.setObjectName(u"MLanguageLabelQWidget_3")
        self.MLanguageLabelHLayout_3 = QHBoxLayout(self.MLanguageLabelQWidget_3)
        self.MLanguageLabelHLayout_3.setSpacing(15)
        self.MLanguageLabelHLayout_3.setObjectName(u"MLanguageLabelHLayout_3")
        self.MLanguageLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQLabel_3 = QLabel(self.MLanguageLabelQWidget_3)
        self.MLanguageQLabel_3.setObjectName(u"MLanguageQLabel_3")

        self.MLanguageLabelHLayout_3.addWidget(self.MLanguageQLabel_3)

        self.MLanguageLabelHSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MLanguageLabelHLayout_3.addItem(self.MLanguageLabelHSpacer_3)


        self.MLanguageVLayout_3.addWidget(self.MLanguageLabelQWidget_3)

        self.MLanguageQComboBox_3 = QComboBox(self.MLanguageQFrame_3)
        self.MLanguageQComboBox_3.addItem("")
        self.MLanguageQComboBox_3.addItem("")
        self.MLanguageQComboBox_3.addItem("")
        self.MLanguageQComboBox_3.addItem("")
        self.MLanguageQComboBox_3.addItem("")
        self.MLanguageQComboBox_3.addItem("")
        self.MLanguageQComboBox_3.addItem("")
        self.MLanguageQComboBox_3.addItem("")
        self.MLanguageQComboBox_3.setObjectName(u"MLanguageQComboBox_3")

        self.MLanguageVLayout_3.addWidget(self.MLanguageQComboBox_3)


        self.horizontalLayout_40.addWidget(self.MLanguageQFrame_3)

        self.MWordsQFrame_3 = QFrame(self.frame_44)
        self.MWordsQFrame_3.setObjectName(u"MWordsQFrame_3")
        self.MStrengthVLayout_3 = QVBoxLayout(self.MWordsQFrame_3)
        self.MStrengthVLayout_3.setSpacing(5)
        self.MStrengthVLayout_3.setObjectName(u"MStrengthVLayout_3")
        self.MStrengthVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MWordsLabelQFrame_3 = QFrame(self.MWordsQFrame_3)
        self.MWordsLabelQFrame_3.setObjectName(u"MWordsLabelQFrame_3")
        self.MStrengthLabelHLayout_11 = QHBoxLayout(self.MWordsLabelQFrame_3)
        self.MStrengthLabelHLayout_11.setSpacing(15)
        self.MStrengthLabelHLayout_11.setObjectName(u"MStrengthLabelHLayout_11")
        self.MStrengthLabelHLayout_11.setContentsMargins(0, 0, 0, 0)
        self.MWordsQLabel_3 = QLabel(self.MWordsLabelQFrame_3)
        self.MWordsQLabel_3.setObjectName(u"MWordsQLabel_3")

        self.MStrengthLabelHLayout_11.addWidget(self.MWordsQLabel_3)

        self.MWordsLabelHSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_11.addItem(self.MWordsLabelHSpacer_3)


        self.MStrengthVLayout_3.addWidget(self.MWordsLabelQFrame_3)

        self.MWordsQComboBox_3 = QComboBox(self.MWordsQFrame_3)
        self.MWordsQComboBox_3.addItem("")
        self.MWordsQComboBox_3.setObjectName(u"MWordsQComboBox_3")

        self.MStrengthVLayout_3.addWidget(self.MWordsQComboBox_3)


        self.horizontalLayout_40.addWidget(self.MWordsQFrame_3)


        self.verticalLayout_36.addWidget(self.frame_44)

        self.fromQStackedWidget_3.addWidget(self.fromMnemonicQStackedWidget_3)
        self.fromSeedQStackedWidget_3 = QWidget()
        self.fromSeedQStackedWidget_3.setObjectName(u"fromSeedQStackedWidget_3")
        self.verticalLayout_37 = QVBoxLayout(self.fromSeedQStackedWidget_3)
        self.verticalLayout_37.setSpacing(15)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.SeedQFrame_3 = QFrame(self.fromSeedQStackedWidget_3)
        self.SeedQFrame_3.setObjectName(u"SeedQFrame_3")
        self.SeedQFrame_3.setMinimumSize(QSize(400, 0))
        self.SeedVLayout_3 = QVBoxLayout(self.SeedQFrame_3)
        self.SeedVLayout_3.setSpacing(5)
        self.SeedVLayout_3.setObjectName(u"SeedVLayout_3")
        self.SeedVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.SeedQFrame_3)
        self.frame_45.setObjectName(u"frame_45")
        self.horizontalLayout_41 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_41.setSpacing(15)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_9 = QFrame(self.frame_45)
        self.ClientQFrame_9.setObjectName(u"ClientQFrame_9")
        self.ClientQFrame_9.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_9 = QVBoxLayout(self.ClientQFrame_9)
        self.ClientVLayout_9.setSpacing(5)
        self.ClientVLayout_9.setObjectName(u"ClientVLayout_9")
        self.ClientVLayout_9.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_9 = QFrame(self.ClientQFrame_9)
        self.ClientLabelQFrame_9.setObjectName(u"ClientLabelQFrame_9")
        self.MStrengthLabelHLayout_12 = QHBoxLayout(self.ClientLabelQFrame_9)
        self.MStrengthLabelHLayout_12.setSpacing(15)
        self.MStrengthLabelHLayout_12.setObjectName(u"MStrengthLabelHLayout_12")
        self.MStrengthLabelHLayout_12.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_9 = QLabel(self.ClientLabelQFrame_9)
        self.ClientQLabel_9.setObjectName(u"ClientQLabel_9")

        self.MStrengthLabelHLayout_12.addWidget(self.ClientQLabel_9)

        self.ClientLabelHSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_12.addItem(self.ClientLabelHSpacer_9)


        self.ClientVLayout_9.addWidget(self.ClientLabelQFrame_9)

        self.ClientQComboBox_9 = QComboBox(self.ClientQFrame_9)
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.setObjectName(u"ClientQComboBox_9")

        self.ClientVLayout_9.addWidget(self.ClientQComboBox_9)


        self.horizontalLayout_41.addWidget(self.ClientQFrame_9)

        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_46)
        self.verticalLayout_38.setSpacing(5)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.SeedLabelQFrame_3 = QFrame(self.frame_46)
        self.SeedLabelQFrame_3.setObjectName(u"SeedLabelQFrame_3")
        self.SeedLabelHLayout_3 = QHBoxLayout(self.SeedLabelQFrame_3)
        self.SeedLabelHLayout_3.setSpacing(15)
        self.SeedLabelHLayout_3.setObjectName(u"SeedLabelHLayout_3")
        self.SeedLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.SeedQLabel_3 = QLabel(self.SeedLabelQFrame_3)
        self.SeedQLabel_3.setObjectName(u"SeedQLabel_3")

        self.SeedLabelHLayout_3.addWidget(self.SeedQLabel_3)

        self.SeedLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout_3.addItem(self.SeedLabelHSpacer_3)


        self.verticalLayout_38.addWidget(self.SeedLabelQFrame_3)

        self.SeedQLineEdit_3 = QLineEdit(self.frame_46)
        self.SeedQLineEdit_3.setObjectName(u"SeedQLineEdit_3")

        self.verticalLayout_38.addWidget(self.SeedQLineEdit_3)


        self.horizontalLayout_41.addWidget(self.frame_46)


        self.SeedVLayout_3.addWidget(self.frame_45)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout_3.addItem(self.verticalSpacer_15)


        self.verticalLayout_37.addWidget(self.SeedQFrame_3)

        self.fromQStackedWidget_3.addWidget(self.fromSeedQStackedWidget_3)
        self.fromXPrivateKeyQStackedWidget_3 = QWidget()
        self.fromXPrivateKeyQStackedWidget_3.setObjectName(u"fromXPrivateKeyQStackedWidget_3")
        self.verticalLayout_39 = QVBoxLayout(self.fromXPrivateKeyQStackedWidget_3)
        self.verticalLayout_39.setSpacing(15)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQFrame_3 = QFrame(self.fromXPrivateKeyQStackedWidget_3)
        self.XPrivateKeyQFrame_3.setObjectName(u"XPrivateKeyQFrame_3")
        self.XPrivateKeyVLayout_3 = QVBoxLayout(self.XPrivateKeyQFrame_3)
        self.XPrivateKeyVLayout_3.setSpacing(5)
        self.XPrivateKeyVLayout_3.setObjectName(u"XPrivateKeyVLayout_3")
        self.XPrivateKeyVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyLabelQFrame_3 = QFrame(self.XPrivateKeyQFrame_3)
        self.XPrivateKeyLabelQFrame_3.setObjectName(u"XPrivateKeyLabelQFrame_3")
        self.XPrivateKeyLabelHLayout_3 = QHBoxLayout(self.XPrivateKeyLabelQFrame_3)
        self.XPrivateKeyLabelHLayout_3.setSpacing(15)
        self.XPrivateKeyLabelHLayout_3.setObjectName(u"XPrivateKeyLabelHLayout_3")
        self.XPrivateKeyLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQLabel_3 = QLabel(self.XPrivateKeyLabelQFrame_3)
        self.XPrivateKeyQLabel_3.setObjectName(u"XPrivateKeyQLabel_3")

        self.XPrivateKeyLabelHLayout_3.addWidget(self.XPrivateKeyQLabel_3)

        self.XPrivateKeyLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPrivateKeyLabelHLayout_3.addItem(self.XPrivateKeyLabelHSpacer_3)


        self.XPrivateKeyVLayout_3.addWidget(self.XPrivateKeyLabelQFrame_3)

        self.XPrivateKeyQLineEdit_3 = QLineEdit(self.XPrivateKeyQFrame_3)
        self.XPrivateKeyQLineEdit_3.setObjectName(u"XPrivateKeyQLineEdit_3")

        self.XPrivateKeyVLayout_3.addWidget(self.XPrivateKeyQLineEdit_3)


        self.verticalLayout_39.addWidget(self.XPrivateKeyQFrame_3)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_16)

        self.fromQStackedWidget_3.addWidget(self.fromXPrivateKeyQStackedWidget_3)
        self.fromXPublicKeyQStackedWidget_3 = QWidget()
        self.fromXPublicKeyQStackedWidget_3.setObjectName(u"fromXPublicKeyQStackedWidget_3")
        self.verticalLayout_40 = QVBoxLayout(self.fromXPublicKeyQStackedWidget_3)
        self.verticalLayout_40.setSpacing(15)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQFrame_3 = QFrame(self.fromXPublicKeyQStackedWidget_3)
        self.XPublicKeyQFrame_3.setObjectName(u"XPublicKeyQFrame_3")
        self.XPublicKeyVLayout_3 = QVBoxLayout(self.XPublicKeyQFrame_3)
        self.XPublicKeyVLayout_3.setSpacing(5)
        self.XPublicKeyVLayout_3.setObjectName(u"XPublicKeyVLayout_3")
        self.XPublicKeyVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyLabelQFrame_3 = QFrame(self.XPublicKeyQFrame_3)
        self.XPublicKeyLabelQFrame_3.setObjectName(u"XPublicKeyLabelQFrame_3")
        self.XPublicKeyLabelHLayout_3 = QHBoxLayout(self.XPublicKeyLabelQFrame_3)
        self.XPublicKeyLabelHLayout_3.setSpacing(15)
        self.XPublicKeyLabelHLayout_3.setObjectName(u"XPublicKeyLabelHLayout_3")
        self.XPublicKeyLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQLabel_3 = QLabel(self.XPublicKeyLabelQFrame_3)
        self.XPublicKeyQLabel_3.setObjectName(u"XPublicKeyQLabel_3")

        self.XPublicKeyLabelHLayout_3.addWidget(self.XPublicKeyQLabel_3)

        self.XPublicKeyLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPublicKeyLabelHLayout_3.addItem(self.XPublicKeyLabelHSpacer_3)


        self.XPublicKeyVLayout_3.addWidget(self.XPublicKeyLabelQFrame_3)

        self.XPublicKeyQLineEdit_3 = QLineEdit(self.XPublicKeyQFrame_3)
        self.XPublicKeyQLineEdit_3.setObjectName(u"XPublicKeyQLineEdit_3")

        self.XPublicKeyVLayout_3.addWidget(self.XPublicKeyQLineEdit_3)


        self.verticalLayout_40.addWidget(self.XPublicKeyQFrame_3)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_17)

        self.fromQStackedWidget_3.addWidget(self.fromXPublicKeyQStackedWidget_3)
        self.fromWIFQStackedWidget_3 = QWidget()
        self.fromWIFQStackedWidget_3.setObjectName(u"fromWIFQStackedWidget_3")
        self.verticalLayout_41 = QVBoxLayout(self.fromWIFQStackedWidget_3)
        self.verticalLayout_41.setSpacing(15)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.WIFQFrame_3 = QFrame(self.fromWIFQStackedWidget_3)
        self.WIFQFrame_3.setObjectName(u"WIFQFrame_3")
        self.WIFQFrame_3.setMinimumSize(QSize(400, 0))
        self.WIFVLayout_3 = QVBoxLayout(self.WIFQFrame_3)
        self.WIFVLayout_3.setSpacing(5)
        self.WIFVLayout_3.setObjectName(u"WIFVLayout_3")
        self.WIFVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.WIFLabelQFrame_3 = QFrame(self.WIFQFrame_3)
        self.WIFLabelQFrame_3.setObjectName(u"WIFLabelQFrame_3")
        self.WIFLabelHLayout_3 = QHBoxLayout(self.WIFLabelQFrame_3)
        self.WIFLabelHLayout_3.setSpacing(15)
        self.WIFLabelHLayout_3.setObjectName(u"WIFLabelHLayout_3")
        self.WIFLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.WIFQLabel_3 = QLabel(self.WIFLabelQFrame_3)
        self.WIFQLabel_3.setObjectName(u"WIFQLabel_3")

        self.WIFLabelHLayout_3.addWidget(self.WIFQLabel_3)

        self.WIFLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WIFLabelHLayout_3.addItem(self.WIFLabelHSpacer_3)


        self.WIFVLayout_3.addWidget(self.WIFLabelQFrame_3)

        self.WIFQLineEdit_3 = QLineEdit(self.WIFQFrame_3)
        self.WIFQLineEdit_3.setObjectName(u"WIFQLineEdit_3")

        self.WIFVLayout_3.addWidget(self.WIFQLineEdit_3)


        self.verticalLayout_41.addWidget(self.WIFQFrame_3)

        self.frame_47 = QFrame(self.fromWIFQStackedWidget_3)
        self.frame_47.setObjectName(u"frame_47")
        self.verticalLayout_42 = QVBoxLayout(self.frame_47)
        self.verticalLayout_42.setSpacing(5)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFPassphraseLabelQFrame_3 = QFrame(self.frame_47)
        self.BIP38EncryptedWIFPassphraseLabelQFrame_3.setObjectName(u"BIP38EncryptedWIFPassphraseLabelQFrame_3")
        self.EPassphraseLabelHLayout_6 = QHBoxLayout(self.BIP38EncryptedWIFPassphraseLabelQFrame_3)
        self.EPassphraseLabelHLayout_6.setSpacing(15)
        self.EPassphraseLabelHLayout_6.setObjectName(u"EPassphraseLabelHLayout_6")
        self.EPassphraseLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFQCheckBox_3 = QCheckBox(self.BIP38EncryptedWIFPassphraseLabelQFrame_3)
        self.BIP38EncryptedWIFQCheckBox_3.setObjectName(u"BIP38EncryptedWIFQCheckBox_3")

        self.EPassphraseLabelHLayout_6.addWidget(self.BIP38EncryptedWIFQCheckBox_3)

        self.BIP38EncryptedWIFPassphraseLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_6.addItem(self.BIP38EncryptedWIFPassphraseLabelHSpacer_3)


        self.verticalLayout_42.addWidget(self.BIP38EncryptedWIFPassphraseLabelQFrame_3)

        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.horizontalLayout_42 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_42.setSpacing(15)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.BIP38PassphraseQLineEdit_3 = QLineEdit(self.frame_48)
        self.BIP38PassphraseQLineEdit_3.setObjectName(u"BIP38PassphraseQLineEdit_3")

        self.horizontalLayout_42.addWidget(self.BIP38PassphraseQLineEdit_3)

        self.pushButton_11 = QPushButton(self.frame_48)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)

        self.horizontalLayout_42.addWidget(self.pushButton_11)


        self.verticalLayout_42.addWidget(self.frame_48)


        self.verticalLayout_41.addWidget(self.frame_47)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_18)

        self.fromQStackedWidget_3.addWidget(self.fromWIFQStackedWidget_3)
        self.fromPrivateKeyQStackedWidget_3 = QWidget()
        self.fromPrivateKeyQStackedWidget_3.setObjectName(u"fromPrivateKeyQStackedWidget_3")
        self.verticalLayout_43 = QVBoxLayout(self.fromPrivateKeyQStackedWidget_3)
        self.verticalLayout_43.setSpacing(15)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQFrame_3 = QFrame(self.fromPrivateKeyQStackedWidget_3)
        self.PrivateKeyQFrame_3.setObjectName(u"PrivateKeyQFrame_3")
        self.PrivateKeyQFrame_3.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_3 = QVBoxLayout(self.PrivateKeyQFrame_3)
        self.PrivateKeyVLayout_3.setSpacing(5)
        self.PrivateKeyVLayout_3.setObjectName(u"PrivateKeyVLayout_3")
        self.PrivateKeyVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyLabelQFrame_3 = QFrame(self.PrivateKeyQFrame_3)
        self.PrivateKeyLabelQFrame_3.setObjectName(u"PrivateKeyLabelQFrame_3")
        self.PrivateKeyLabelHLayout_3 = QHBoxLayout(self.PrivateKeyLabelQFrame_3)
        self.PrivateKeyLabelHLayout_3.setSpacing(15)
        self.PrivateKeyLabelHLayout_3.setObjectName(u"PrivateKeyLabelHLayout_3")
        self.PrivateKeyLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQLabel_3 = QLabel(self.PrivateKeyLabelQFrame_3)
        self.PrivateKeyQLabel_3.setObjectName(u"PrivateKeyQLabel_3")

        self.PrivateKeyLabelHLayout_3.addWidget(self.PrivateKeyQLabel_3)

        self.PrivateKeyLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_3.addItem(self.PrivateKeyLabelHSpacer_3)


        self.PrivateKeyVLayout_3.addWidget(self.PrivateKeyLabelQFrame_3)

        self.PrivateKeyQLineEdit_3 = QLineEdit(self.PrivateKeyQFrame_3)
        self.PrivateKeyQLineEdit_3.setObjectName(u"PrivateKeyQLineEdit_3")

        self.PrivateKeyVLayout_3.addWidget(self.PrivateKeyQLineEdit_3)


        self.verticalLayout_43.addWidget(self.PrivateKeyQFrame_3)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_19)

        self.fromQStackedWidget_3.addWidget(self.fromPrivateKeyQStackedWidget_3)
        self.fromPublicKeyQStackedWidget_3 = QWidget()
        self.fromPublicKeyQStackedWidget_3.setObjectName(u"fromPublicKeyQStackedWidget_3")
        self.verticalLayout_44 = QVBoxLayout(self.fromPublicKeyQStackedWidget_3)
        self.verticalLayout_44.setSpacing(15)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQFrame_3 = QFrame(self.fromPublicKeyQStackedWidget_3)
        self.PublicKeyQFrame_3.setObjectName(u"PublicKeyQFrame_3")
        self.PublicKeyVLayout_3 = QVBoxLayout(self.PublicKeyQFrame_3)
        self.PublicKeyVLayout_3.setSpacing(5)
        self.PublicKeyVLayout_3.setObjectName(u"PublicKeyVLayout_3")
        self.PublicKeyVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyLabelQFrame_3 = QFrame(self.PublicKeyQFrame_3)
        self.PublicKeyLabelQFrame_3.setObjectName(u"PublicKeyLabelQFrame_3")
        self.PublicKeyLabelHLayout_3 = QHBoxLayout(self.PublicKeyLabelQFrame_3)
        self.PublicKeyLabelHLayout_3.setSpacing(15)
        self.PublicKeyLabelHLayout_3.setObjectName(u"PublicKeyLabelHLayout_3")
        self.PublicKeyLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQLabel_3 = QLabel(self.PublicKeyLabelQFrame_3)
        self.PublicKeyQLabel_3.setObjectName(u"PublicKeyQLabel_3")

        self.PublicKeyLabelHLayout_3.addWidget(self.PublicKeyQLabel_3)

        self.PublicKeyLabelHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PublicKeyLabelHLayout_3.addItem(self.PublicKeyLabelHSpacer_3)


        self.PublicKeyVLayout_3.addWidget(self.PublicKeyLabelQFrame_3)

        self.PublicKeyQLineEdit_3 = QLineEdit(self.PublicKeyQFrame_3)
        self.PublicKeyQLineEdit_3.setObjectName(u"PublicKeyQLineEdit_3")

        self.PublicKeyVLayout_3.addWidget(self.PublicKeyQLineEdit_3)


        self.verticalLayout_44.addWidget(self.PublicKeyQFrame_3)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_20)

        self.fromQStackedWidget_3.addWidget(self.fromPublicKeyQStackedWidget_3)

        self.verticalLayout_33.addWidget(self.fromQStackedWidget_3)

        self.stackedWidget.addWidget(self.Cardano)
        self.ElectrumV1 = QWidget()
        self.ElectrumV1.setObjectName(u"ElectrumV1")
        self.verticalLayout_45 = QVBoxLayout(self.ElectrumV1)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.fromQStackedWidget_4 = QStackedWidget(self.ElectrumV1)
        self.fromQStackedWidget_4.setObjectName(u"fromQStackedWidget_4")
        self.fromEntropyQStackedWidget_4 = QWidget()
        self.fromEntropyQStackedWidget_4.setObjectName(u"fromEntropyQStackedWidget_4")
        self.verticalLayout_46 = QVBoxLayout(self.fromEntropyQStackedWidget_4)
        self.verticalLayout_46.setSpacing(15)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.fromEntropyQStackedWidget_4)
        self.frame_49.setObjectName(u"frame_49")
        self.verticalLayout_47 = QVBoxLayout(self.frame_49)
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.EntropyQFrame_4 = QFrame(self.frame_49)
        self.EntropyQFrame_4.setObjectName(u"EntropyQFrame_4")
        self.EntropyQFrame_4.setMinimumSize(QSize(400, 0))
        self.EntropyVLayout_5 = QVBoxLayout(self.EntropyQFrame_4)
        self.EntropyVLayout_5.setSpacing(15)
        self.EntropyVLayout_5.setObjectName(u"EntropyVLayout_5")
        self.EntropyVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.EntropyLabelQFrame_5 = QFrame(self.EntropyQFrame_4)
        self.EntropyLabelQFrame_5.setObjectName(u"EntropyLabelQFrame_5")
        self.EntropyLabelHLayout_5 = QHBoxLayout(self.EntropyLabelQFrame_5)
        self.EntropyLabelHLayout_5.setSpacing(15)
        self.EntropyLabelHLayout_5.setObjectName(u"EntropyLabelHLayout_5")
        self.EntropyLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLabel_5 = QLabel(self.EntropyLabelQFrame_5)
        self.EntropyQLabel_5.setObjectName(u"EntropyQLabel_5")

        self.EntropyLabelHLayout_5.addWidget(self.EntropyQLabel_5)

        self.EntropyLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_5.addItem(self.EntropyLabelHSpacer_5)


        self.EntropyVLayout_5.addWidget(self.EntropyLabelQFrame_5)


        self.verticalLayout_47.addWidget(self.EntropyQFrame_4)

        self.EGenerateQFrame_4 = QFrame(self.frame_49)
        self.EGenerateQFrame_4.setObjectName(u"EGenerateQFrame_4")
        self.horizontalLayout_43 = QHBoxLayout(self.EGenerateQFrame_4)
        self.horizontalLayout_43.setSpacing(15)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLineEdit_5 = QLineEdit(self.EGenerateQFrame_4)
        self.EntropyQLineEdit_5.setObjectName(u"EntropyQLineEdit_5")

        self.horizontalLayout_43.addWidget(self.EntropyQLineEdit_5)

        self.EGenerateQPushButton_5 = QPushButton(self.EGenerateQFrame_4)
        self.EGenerateQPushButton_5.setObjectName(u"EGenerateQPushButton_5")

        self.horizontalLayout_43.addWidget(self.EGenerateQPushButton_5)


        self.verticalLayout_47.addWidget(self.EGenerateQFrame_4)


        self.verticalLayout_46.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.fromEntropyQStackedWidget_4)
        self.frame_50.setObjectName(u"frame_50")
        self.horizontalLayout_44 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_44.setSpacing(15)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_10 = QFrame(self.frame_50)
        self.ClientQFrame_10.setObjectName(u"ClientQFrame_10")
        self.ClientQFrame_10.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_10 = QVBoxLayout(self.ClientQFrame_10)
        self.ClientVLayout_10.setSpacing(5)
        self.ClientVLayout_10.setObjectName(u"ClientVLayout_10")
        self.ClientVLayout_10.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_10 = QFrame(self.ClientQFrame_10)
        self.ClientLabelQFrame_10.setObjectName(u"ClientLabelQFrame_10")
        self.MStrengthLabelHLayout_13 = QHBoxLayout(self.ClientLabelQFrame_10)
        self.MStrengthLabelHLayout_13.setSpacing(15)
        self.MStrengthLabelHLayout_13.setObjectName(u"MStrengthLabelHLayout_13")
        self.MStrengthLabelHLayout_13.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_10 = QLabel(self.ClientLabelQFrame_10)
        self.ClientQLabel_10.setObjectName(u"ClientQLabel_10")

        self.MStrengthLabelHLayout_13.addWidget(self.ClientQLabel_10)

        self.ClientLabelHSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_13.addItem(self.ClientLabelHSpacer_10)


        self.ClientVLayout_10.addWidget(self.ClientLabelQFrame_10)

        self.ClientQComboBox_10 = QComboBox(self.ClientQFrame_10)
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.setObjectName(u"ClientQComboBox_10")

        self.ClientVLayout_10.addWidget(self.ClientQComboBox_10)


        self.horizontalLayout_44.addWidget(self.ClientQFrame_10)

        self.EPassphraseQFrame_4 = QFrame(self.frame_50)
        self.EPassphraseQFrame_4.setObjectName(u"EPassphraseQFrame_4")
        self.EPassphraseVLayout_7 = QVBoxLayout(self.EPassphraseQFrame_4)
        self.EPassphraseVLayout_7.setSpacing(5)
        self.EPassphraseVLayout_7.setObjectName(u"EPassphraseVLayout_7")
        self.EPassphraseVLayout_7.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseLabelQFrame_4 = QFrame(self.EPassphraseQFrame_4)
        self.EPassphraseLabelQFrame_4.setObjectName(u"EPassphraseLabelQFrame_4")
        self.EPassphraseLabelHLayout_7 = QHBoxLayout(self.EPassphraseLabelQFrame_4)
        self.EPassphraseLabelHLayout_7.setSpacing(15)
        self.EPassphraseLabelHLayout_7.setObjectName(u"EPassphraseLabelHLayout_7")
        self.EPassphraseLabelHLayout_7.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLabel_4 = QLabel(self.EPassphraseLabelQFrame_4)
        self.EPassphraseQLabel_4.setObjectName(u"EPassphraseQLabel_4")

        self.EPassphraseLabelHLayout_7.addWidget(self.EPassphraseQLabel_4)

        self.EPassphraseLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_7.addItem(self.EPassphraseLabelHSpacer_4)


        self.EPassphraseVLayout_7.addWidget(self.EPassphraseLabelQFrame_4)

        self.frame_51 = QFrame(self.EPassphraseQFrame_4)
        self.frame_51.setObjectName(u"frame_51")
        self.horizontalLayout_45 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_45.setSpacing(15)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLineEdit_4 = QLineEdit(self.frame_51)
        self.EPassphraseQLineEdit_4.setObjectName(u"EPassphraseQLineEdit_4")

        self.horizontalLayout_45.addWidget(self.EPassphraseQLineEdit_4)

        self.pushButton_12 = QPushButton(self.frame_51)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_45.addWidget(self.pushButton_12)


        self.EPassphraseVLayout_7.addWidget(self.frame_51)


        self.horizontalLayout_44.addWidget(self.EPassphraseQFrame_4)


        self.verticalLayout_46.addWidget(self.frame_50)

        self.frame_52 = QFrame(self.fromEntropyQStackedWidget_4)
        self.frame_52.setObjectName(u"frame_52")
        self.horizontalLayout_46 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_46.setSpacing(15)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQFrame_4 = QFrame(self.frame_52)
        self.ELanguageQFrame_4.setObjectName(u"ELanguageQFrame_4")
        self.ELanguageVLayout_4 = QVBoxLayout(self.ELanguageQFrame_4)
        self.ELanguageVLayout_4.setSpacing(5)
        self.ELanguageVLayout_4.setObjectName(u"ELanguageVLayout_4")
        self.ELanguageVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ELanguageLabelQFrame_4 = QFrame(self.ELanguageQFrame_4)
        self.ELanguageLabelQFrame_4.setObjectName(u"ELanguageLabelQFrame_4")
        self.ELanguageLabelHLayout_4 = QHBoxLayout(self.ELanguageLabelQFrame_4)
        self.ELanguageLabelHLayout_4.setSpacing(15)
        self.ELanguageLabelHLayout_4.setObjectName(u"ELanguageLabelHLayout_4")
        self.ELanguageLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQLabel_4 = QLabel(self.ELanguageLabelQFrame_4)
        self.ELanguageQLabel_4.setObjectName(u"ELanguageQLabel_4")

        self.ELanguageLabelHLayout_4.addWidget(self.ELanguageQLabel_4)

        self.ELanguageLabelHSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout_4.addItem(self.ELanguageLabelHSpacer_4)


        self.ELanguageVLayout_4.addWidget(self.ELanguageLabelQFrame_4)

        self.ELanguageQComboBox_4 = QComboBox(self.ELanguageQFrame_4)
        self.ELanguageQComboBox_4.addItem("")
        self.ELanguageQComboBox_4.addItem("")
        self.ELanguageQComboBox_4.addItem("")
        self.ELanguageQComboBox_4.addItem("")
        self.ELanguageQComboBox_4.addItem("")
        self.ELanguageQComboBox_4.addItem("")
        self.ELanguageQComboBox_4.addItem("")
        self.ELanguageQComboBox_4.addItem("")
        self.ELanguageQComboBox_4.setObjectName(u"ELanguageQComboBox_4")

        self.ELanguageVLayout_4.addWidget(self.ELanguageQComboBox_4)


        self.horizontalLayout_46.addWidget(self.ELanguageQFrame_4)

        self.EWordsQFrame_4 = QFrame(self.frame_52)
        self.EWordsQFrame_4.setObjectName(u"EWordsQFrame_4")
        self.EStrengthVLayout_4 = QVBoxLayout(self.EWordsQFrame_4)
        self.EStrengthVLayout_4.setSpacing(5)
        self.EStrengthVLayout_4.setObjectName(u"EStrengthVLayout_4")
        self.EStrengthVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.EWordsLabelQFrame_4 = QFrame(self.EWordsQFrame_4)
        self.EWordsLabelQFrame_4.setObjectName(u"EWordsLabelQFrame_4")
        self.EStrengthLabelHLayout_4 = QHBoxLayout(self.EWordsLabelQFrame_4)
        self.EStrengthLabelHLayout_4.setSpacing(15)
        self.EStrengthLabelHLayout_4.setObjectName(u"EStrengthLabelHLayout_4")
        self.EStrengthLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.EWordsQLabel_4 = QLabel(self.EWordsLabelQFrame_4)
        self.EWordsQLabel_4.setObjectName(u"EWordsQLabel_4")

        self.EStrengthLabelHLayout_4.addWidget(self.EWordsQLabel_4)

        self.EWordsLabelHSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout_4.addItem(self.EWordsLabelHSpacer_4)


        self.EStrengthVLayout_4.addWidget(self.EWordsLabelQFrame_4)

        self.EWordsQComboBox_4 = QComboBox(self.EWordsQFrame_4)
        self.EWordsQComboBox_4.addItem("")
        self.EWordsQComboBox_4.addItem("")
        self.EWordsQComboBox_4.addItem("")
        self.EWordsQComboBox_4.addItem("")
        self.EWordsQComboBox_4.addItem("")
        self.EWordsQComboBox_4.setObjectName(u"EWordsQComboBox_4")

        self.EStrengthVLayout_4.addWidget(self.EWordsQComboBox_4)


        self.horizontalLayout_46.addWidget(self.EWordsQFrame_4)


        self.verticalLayout_46.addWidget(self.frame_52)

        self.fromQStackedWidget_4.addWidget(self.fromEntropyQStackedWidget_4)
        self.fromMnemonicQStackedWidget_4 = QWidget()
        self.fromMnemonicQStackedWidget_4.setObjectName(u"fromMnemonicQStackedWidget_4")
        self.verticalLayout_48 = QVBoxLayout(self.fromMnemonicQStackedWidget_4)
        self.verticalLayout_48.setSpacing(15)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQFrame_4 = QFrame(self.fromMnemonicQStackedWidget_4)
        self.MnemonicQFrame_4.setObjectName(u"MnemonicQFrame_4")
        self.MnemonicVLayout_4 = QVBoxLayout(self.MnemonicQFrame_4)
        self.MnemonicVLayout_4.setSpacing(5)
        self.MnemonicVLayout_4.setObjectName(u"MnemonicVLayout_4")
        self.MnemonicVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MnemonicLabelQFrame_4 = QFrame(self.MnemonicQFrame_4)
        self.MnemonicLabelQFrame_4.setObjectName(u"MnemonicLabelQFrame_4")
        self.MnemonicLabelHLayout_4 = QHBoxLayout(self.MnemonicLabelQFrame_4)
        self.MnemonicLabelHLayout_4.setSpacing(15)
        self.MnemonicLabelHLayout_4.setObjectName(u"MnemonicLabelHLayout_4")
        self.MnemonicLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLabel_4 = QLabel(self.MnemonicLabelQFrame_4)
        self.MnemonicQLabel_4.setObjectName(u"MnemonicQLabel_4")

        self.MnemonicLabelHLayout_4.addWidget(self.MnemonicQLabel_4)

        self.MnemonicLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout_4.addItem(self.MnemonicLabelHSpacer_4)


        self.MnemonicVLayout_4.addWidget(self.MnemonicLabelQFrame_4)

        self.frame_53 = QFrame(self.MnemonicQFrame_4)
        self.frame_53.setObjectName(u"frame_53")
        self.horizontalLayout_47 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_47.setSpacing(15)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLineEdit_4 = QLineEdit(self.frame_53)
        self.MnemonicQLineEdit_4.setObjectName(u"MnemonicQLineEdit_4")

        self.horizontalLayout_47.addWidget(self.MnemonicQLineEdit_4)

        self.MGenerateQFrame_4 = QFrame(self.frame_53)
        self.MGenerateQFrame_4.setObjectName(u"MGenerateQFrame_4")
        self.GenerateMnemonicVLayout_4 = QVBoxLayout(self.MGenerateQFrame_4)
        self.GenerateMnemonicVLayout_4.setSpacing(15)
        self.GenerateMnemonicVLayout_4.setObjectName(u"GenerateMnemonicVLayout_4")
        self.GenerateMnemonicVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MGenerateQPushButton_4 = QPushButton(self.MGenerateQFrame_4)
        self.MGenerateQPushButton_4.setObjectName(u"MGenerateQPushButton_4")

        self.GenerateMnemonicVLayout_4.addWidget(self.MGenerateQPushButton_4)


        self.horizontalLayout_47.addWidget(self.MGenerateQFrame_4)


        self.MnemonicVLayout_4.addWidget(self.frame_53)


        self.verticalLayout_48.addWidget(self.MnemonicQFrame_4)

        self.frame_54 = QFrame(self.fromMnemonicQStackedWidget_4)
        self.frame_54.setObjectName(u"frame_54")
        self.horizontalLayout_48 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_48.setSpacing(15)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_11 = QFrame(self.frame_54)
        self.ClientQFrame_11.setObjectName(u"ClientQFrame_11")
        self.ClientQFrame_11.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_11 = QVBoxLayout(self.ClientQFrame_11)
        self.ClientVLayout_11.setSpacing(5)
        self.ClientVLayout_11.setObjectName(u"ClientVLayout_11")
        self.ClientVLayout_11.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_11 = QFrame(self.ClientQFrame_11)
        self.ClientLabelQFrame_11.setObjectName(u"ClientLabelQFrame_11")
        self.MStrengthLabelHLayout_14 = QHBoxLayout(self.ClientLabelQFrame_11)
        self.MStrengthLabelHLayout_14.setSpacing(15)
        self.MStrengthLabelHLayout_14.setObjectName(u"MStrengthLabelHLayout_14")
        self.MStrengthLabelHLayout_14.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_11 = QLabel(self.ClientLabelQFrame_11)
        self.ClientQLabel_11.setObjectName(u"ClientQLabel_11")

        self.MStrengthLabelHLayout_14.addWidget(self.ClientQLabel_11)

        self.ClientLabelHSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_14.addItem(self.ClientLabelHSpacer_11)


        self.ClientVLayout_11.addWidget(self.ClientLabelQFrame_11)

        self.ClientQComboBox_11 = QComboBox(self.ClientQFrame_11)
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.setObjectName(u"ClientQComboBox_11")

        self.ClientVLayout_11.addWidget(self.ClientQComboBox_11)


        self.horizontalLayout_48.addWidget(self.ClientQFrame_11)

        self.MPassphraseQFrame_4 = QFrame(self.frame_54)
        self.MPassphraseQFrame_4.setObjectName(u"MPassphraseQFrame_4")
        self.EPassphraseVLayout_8 = QVBoxLayout(self.MPassphraseQFrame_4)
        self.EPassphraseVLayout_8.setSpacing(5)
        self.EPassphraseVLayout_8.setObjectName(u"EPassphraseVLayout_8")
        self.EPassphraseVLayout_8.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseLabelQFrame_4 = QFrame(self.MPassphraseQFrame_4)
        self.MPassphraseLabelQFrame_4.setObjectName(u"MPassphraseLabelQFrame_4")
        self.MPassphraseLabelHLayout_4 = QHBoxLayout(self.MPassphraseLabelQFrame_4)
        self.MPassphraseLabelHLayout_4.setSpacing(15)
        self.MPassphraseLabelHLayout_4.setObjectName(u"MPassphraseLabelHLayout_4")
        self.MPassphraseLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLabel_4 = QLabel(self.MPassphraseLabelQFrame_4)
        self.MPassphraseQLabel_4.setObjectName(u"MPassphraseQLabel_4")

        self.MPassphraseLabelHLayout_4.addWidget(self.MPassphraseQLabel_4)

        self.MPassphraseLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout_4.addItem(self.MPassphraseLabelHSpacer_4)


        self.EPassphraseVLayout_8.addWidget(self.MPassphraseLabelQFrame_4)

        self.frame_55 = QFrame(self.MPassphraseQFrame_4)
        self.frame_55.setObjectName(u"frame_55")
        self.horizontalLayout_49 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_49.setSpacing(15)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLineEdit_4 = QLineEdit(self.frame_55)
        self.MPassphraseQLineEdit_4.setObjectName(u"MPassphraseQLineEdit_4")

        self.horizontalLayout_49.addWidget(self.MPassphraseQLineEdit_4)

        self.pushButton_13 = QPushButton(self.frame_55)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_49.addWidget(self.pushButton_13)


        self.EPassphraseVLayout_8.addWidget(self.frame_55)


        self.horizontalLayout_48.addWidget(self.MPassphraseQFrame_4)


        self.verticalLayout_48.addWidget(self.frame_54)

        self.frame_56 = QFrame(self.fromMnemonicQStackedWidget_4)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_50.setSpacing(15)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQFrame_4 = QFrame(self.frame_56)
        self.MLanguageQFrame_4.setObjectName(u"MLanguageQFrame_4")
        self.MLanguageVLayout_4 = QVBoxLayout(self.MLanguageQFrame_4)
        self.MLanguageVLayout_4.setSpacing(5)
        self.MLanguageVLayout_4.setObjectName(u"MLanguageVLayout_4")
        self.MLanguageVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MLanguageLabelQWidget_4 = QWidget(self.MLanguageQFrame_4)
        self.MLanguageLabelQWidget_4.setObjectName(u"MLanguageLabelQWidget_4")
        self.MLanguageLabelHLayout_4 = QHBoxLayout(self.MLanguageLabelQWidget_4)
        self.MLanguageLabelHLayout_4.setSpacing(15)
        self.MLanguageLabelHLayout_4.setObjectName(u"MLanguageLabelHLayout_4")
        self.MLanguageLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQLabel_4 = QLabel(self.MLanguageLabelQWidget_4)
        self.MLanguageQLabel_4.setObjectName(u"MLanguageQLabel_4")

        self.MLanguageLabelHLayout_4.addWidget(self.MLanguageQLabel_4)

        self.MLanguageLabelHSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MLanguageLabelHLayout_4.addItem(self.MLanguageLabelHSpacer_4)


        self.MLanguageVLayout_4.addWidget(self.MLanguageLabelQWidget_4)

        self.MLanguageQComboBox_4 = QComboBox(self.MLanguageQFrame_4)
        self.MLanguageQComboBox_4.addItem("")
        self.MLanguageQComboBox_4.addItem("")
        self.MLanguageQComboBox_4.addItem("")
        self.MLanguageQComboBox_4.addItem("")
        self.MLanguageQComboBox_4.addItem("")
        self.MLanguageQComboBox_4.addItem("")
        self.MLanguageQComboBox_4.addItem("")
        self.MLanguageQComboBox_4.addItem("")
        self.MLanguageQComboBox_4.setObjectName(u"MLanguageQComboBox_4")

        self.MLanguageVLayout_4.addWidget(self.MLanguageQComboBox_4)


        self.horizontalLayout_50.addWidget(self.MLanguageQFrame_4)

        self.MWordsQFrame_4 = QFrame(self.frame_56)
        self.MWordsQFrame_4.setObjectName(u"MWordsQFrame_4")
        self.MStrengthVLayout_4 = QVBoxLayout(self.MWordsQFrame_4)
        self.MStrengthVLayout_4.setSpacing(5)
        self.MStrengthVLayout_4.setObjectName(u"MStrengthVLayout_4")
        self.MStrengthVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MWordsLabelQFrame_4 = QFrame(self.MWordsQFrame_4)
        self.MWordsLabelQFrame_4.setObjectName(u"MWordsLabelQFrame_4")
        self.MStrengthLabelHLayout_15 = QHBoxLayout(self.MWordsLabelQFrame_4)
        self.MStrengthLabelHLayout_15.setSpacing(15)
        self.MStrengthLabelHLayout_15.setObjectName(u"MStrengthLabelHLayout_15")
        self.MStrengthLabelHLayout_15.setContentsMargins(0, 0, 0, 0)
        self.MWordsQLabel_4 = QLabel(self.MWordsLabelQFrame_4)
        self.MWordsQLabel_4.setObjectName(u"MWordsQLabel_4")

        self.MStrengthLabelHLayout_15.addWidget(self.MWordsQLabel_4)

        self.MWordsLabelHSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_15.addItem(self.MWordsLabelHSpacer_4)


        self.MStrengthVLayout_4.addWidget(self.MWordsLabelQFrame_4)

        self.MWordsQComboBox_4 = QComboBox(self.MWordsQFrame_4)
        self.MWordsQComboBox_4.addItem("")
        self.MWordsQComboBox_4.setObjectName(u"MWordsQComboBox_4")

        self.MStrengthVLayout_4.addWidget(self.MWordsQComboBox_4)


        self.horizontalLayout_50.addWidget(self.MWordsQFrame_4)


        self.verticalLayout_48.addWidget(self.frame_56)

        self.fromQStackedWidget_4.addWidget(self.fromMnemonicQStackedWidget_4)
        self.fromSeedQStackedWidget_4 = QWidget()
        self.fromSeedQStackedWidget_4.setObjectName(u"fromSeedQStackedWidget_4")
        self.verticalLayout_49 = QVBoxLayout(self.fromSeedQStackedWidget_4)
        self.verticalLayout_49.setSpacing(15)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.SeedQFrame_4 = QFrame(self.fromSeedQStackedWidget_4)
        self.SeedQFrame_4.setObjectName(u"SeedQFrame_4")
        self.SeedQFrame_4.setMinimumSize(QSize(400, 0))
        self.SeedVLayout_4 = QVBoxLayout(self.SeedQFrame_4)
        self.SeedVLayout_4.setSpacing(5)
        self.SeedVLayout_4.setObjectName(u"SeedVLayout_4")
        self.SeedVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.SeedQFrame_4)
        self.frame_57.setObjectName(u"frame_57")
        self.horizontalLayout_51 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_51.setSpacing(15)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_12 = QFrame(self.frame_57)
        self.ClientQFrame_12.setObjectName(u"ClientQFrame_12")
        self.ClientQFrame_12.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_12 = QVBoxLayout(self.ClientQFrame_12)
        self.ClientVLayout_12.setSpacing(5)
        self.ClientVLayout_12.setObjectName(u"ClientVLayout_12")
        self.ClientVLayout_12.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_12 = QFrame(self.ClientQFrame_12)
        self.ClientLabelQFrame_12.setObjectName(u"ClientLabelQFrame_12")
        self.MStrengthLabelHLayout_16 = QHBoxLayout(self.ClientLabelQFrame_12)
        self.MStrengthLabelHLayout_16.setSpacing(15)
        self.MStrengthLabelHLayout_16.setObjectName(u"MStrengthLabelHLayout_16")
        self.MStrengthLabelHLayout_16.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_12 = QLabel(self.ClientLabelQFrame_12)
        self.ClientQLabel_12.setObjectName(u"ClientQLabel_12")

        self.MStrengthLabelHLayout_16.addWidget(self.ClientQLabel_12)

        self.ClientLabelHSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_16.addItem(self.ClientLabelHSpacer_12)


        self.ClientVLayout_12.addWidget(self.ClientLabelQFrame_12)

        self.ClientQComboBox_12 = QComboBox(self.ClientQFrame_12)
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.setObjectName(u"ClientQComboBox_12")

        self.ClientVLayout_12.addWidget(self.ClientQComboBox_12)


        self.horizontalLayout_51.addWidget(self.ClientQFrame_12)

        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_58)
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.SeedLabelQFrame_4 = QFrame(self.frame_58)
        self.SeedLabelQFrame_4.setObjectName(u"SeedLabelQFrame_4")
        self.SeedLabelHLayout_4 = QHBoxLayout(self.SeedLabelQFrame_4)
        self.SeedLabelHLayout_4.setSpacing(15)
        self.SeedLabelHLayout_4.setObjectName(u"SeedLabelHLayout_4")
        self.SeedLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.SeedQLabel_4 = QLabel(self.SeedLabelQFrame_4)
        self.SeedQLabel_4.setObjectName(u"SeedQLabel_4")

        self.SeedLabelHLayout_4.addWidget(self.SeedQLabel_4)

        self.SeedLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout_4.addItem(self.SeedLabelHSpacer_4)


        self.verticalLayout_50.addWidget(self.SeedLabelQFrame_4)

        self.SeedQLineEdit_4 = QLineEdit(self.frame_58)
        self.SeedQLineEdit_4.setObjectName(u"SeedQLineEdit_4")

        self.verticalLayout_50.addWidget(self.SeedQLineEdit_4)


        self.horizontalLayout_51.addWidget(self.frame_58)


        self.SeedVLayout_4.addWidget(self.frame_57)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout_4.addItem(self.verticalSpacer_21)


        self.verticalLayout_49.addWidget(self.SeedQFrame_4)

        self.fromQStackedWidget_4.addWidget(self.fromSeedQStackedWidget_4)
        self.fromXPrivateKeyQStackedWidget_4 = QWidget()
        self.fromXPrivateKeyQStackedWidget_4.setObjectName(u"fromXPrivateKeyQStackedWidget_4")
        self.verticalLayout_51 = QVBoxLayout(self.fromXPrivateKeyQStackedWidget_4)
        self.verticalLayout_51.setSpacing(15)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQFrame_4 = QFrame(self.fromXPrivateKeyQStackedWidget_4)
        self.XPrivateKeyQFrame_4.setObjectName(u"XPrivateKeyQFrame_4")
        self.XPrivateKeyVLayout_4 = QVBoxLayout(self.XPrivateKeyQFrame_4)
        self.XPrivateKeyVLayout_4.setSpacing(5)
        self.XPrivateKeyVLayout_4.setObjectName(u"XPrivateKeyVLayout_4")
        self.XPrivateKeyVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyLabelQFrame_4 = QFrame(self.XPrivateKeyQFrame_4)
        self.XPrivateKeyLabelQFrame_4.setObjectName(u"XPrivateKeyLabelQFrame_4")
        self.XPrivateKeyLabelHLayout_4 = QHBoxLayout(self.XPrivateKeyLabelQFrame_4)
        self.XPrivateKeyLabelHLayout_4.setSpacing(15)
        self.XPrivateKeyLabelHLayout_4.setObjectName(u"XPrivateKeyLabelHLayout_4")
        self.XPrivateKeyLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQLabel_4 = QLabel(self.XPrivateKeyLabelQFrame_4)
        self.XPrivateKeyQLabel_4.setObjectName(u"XPrivateKeyQLabel_4")

        self.XPrivateKeyLabelHLayout_4.addWidget(self.XPrivateKeyQLabel_4)

        self.XPrivateKeyLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPrivateKeyLabelHLayout_4.addItem(self.XPrivateKeyLabelHSpacer_4)


        self.XPrivateKeyVLayout_4.addWidget(self.XPrivateKeyLabelQFrame_4)

        self.XPrivateKeyQLineEdit_4 = QLineEdit(self.XPrivateKeyQFrame_4)
        self.XPrivateKeyQLineEdit_4.setObjectName(u"XPrivateKeyQLineEdit_4")

        self.XPrivateKeyVLayout_4.addWidget(self.XPrivateKeyQLineEdit_4)


        self.verticalLayout_51.addWidget(self.XPrivateKeyQFrame_4)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_51.addItem(self.verticalSpacer_22)

        self.fromQStackedWidget_4.addWidget(self.fromXPrivateKeyQStackedWidget_4)
        self.fromXPublicKeyQStackedWidget_4 = QWidget()
        self.fromXPublicKeyQStackedWidget_4.setObjectName(u"fromXPublicKeyQStackedWidget_4")
        self.verticalLayout_52 = QVBoxLayout(self.fromXPublicKeyQStackedWidget_4)
        self.verticalLayout_52.setSpacing(15)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQFrame_4 = QFrame(self.fromXPublicKeyQStackedWidget_4)
        self.XPublicKeyQFrame_4.setObjectName(u"XPublicKeyQFrame_4")
        self.XPublicKeyVLayout_4 = QVBoxLayout(self.XPublicKeyQFrame_4)
        self.XPublicKeyVLayout_4.setSpacing(5)
        self.XPublicKeyVLayout_4.setObjectName(u"XPublicKeyVLayout_4")
        self.XPublicKeyVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyLabelQFrame_4 = QFrame(self.XPublicKeyQFrame_4)
        self.XPublicKeyLabelQFrame_4.setObjectName(u"XPublicKeyLabelQFrame_4")
        self.XPublicKeyLabelHLayout_4 = QHBoxLayout(self.XPublicKeyLabelQFrame_4)
        self.XPublicKeyLabelHLayout_4.setSpacing(15)
        self.XPublicKeyLabelHLayout_4.setObjectName(u"XPublicKeyLabelHLayout_4")
        self.XPublicKeyLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQLabel_4 = QLabel(self.XPublicKeyLabelQFrame_4)
        self.XPublicKeyQLabel_4.setObjectName(u"XPublicKeyQLabel_4")

        self.XPublicKeyLabelHLayout_4.addWidget(self.XPublicKeyQLabel_4)

        self.XPublicKeyLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPublicKeyLabelHLayout_4.addItem(self.XPublicKeyLabelHSpacer_4)


        self.XPublicKeyVLayout_4.addWidget(self.XPublicKeyLabelQFrame_4)

        self.XPublicKeyQLineEdit_4 = QLineEdit(self.XPublicKeyQFrame_4)
        self.XPublicKeyQLineEdit_4.setObjectName(u"XPublicKeyQLineEdit_4")

        self.XPublicKeyVLayout_4.addWidget(self.XPublicKeyQLineEdit_4)


        self.verticalLayout_52.addWidget(self.XPublicKeyQFrame_4)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_23)

        self.fromQStackedWidget_4.addWidget(self.fromXPublicKeyQStackedWidget_4)
        self.fromWIFQStackedWidget_4 = QWidget()
        self.fromWIFQStackedWidget_4.setObjectName(u"fromWIFQStackedWidget_4")
        self.verticalLayout_53 = QVBoxLayout(self.fromWIFQStackedWidget_4)
        self.verticalLayout_53.setSpacing(15)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.WIFQFrame_4 = QFrame(self.fromWIFQStackedWidget_4)
        self.WIFQFrame_4.setObjectName(u"WIFQFrame_4")
        self.WIFQFrame_4.setMinimumSize(QSize(400, 0))
        self.WIFVLayout_4 = QVBoxLayout(self.WIFQFrame_4)
        self.WIFVLayout_4.setSpacing(5)
        self.WIFVLayout_4.setObjectName(u"WIFVLayout_4")
        self.WIFVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.WIFLabelQFrame_4 = QFrame(self.WIFQFrame_4)
        self.WIFLabelQFrame_4.setObjectName(u"WIFLabelQFrame_4")
        self.WIFLabelHLayout_4 = QHBoxLayout(self.WIFLabelQFrame_4)
        self.WIFLabelHLayout_4.setSpacing(15)
        self.WIFLabelHLayout_4.setObjectName(u"WIFLabelHLayout_4")
        self.WIFLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.WIFQLabel_4 = QLabel(self.WIFLabelQFrame_4)
        self.WIFQLabel_4.setObjectName(u"WIFQLabel_4")

        self.WIFLabelHLayout_4.addWidget(self.WIFQLabel_4)

        self.WIFLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WIFLabelHLayout_4.addItem(self.WIFLabelHSpacer_4)


        self.WIFVLayout_4.addWidget(self.WIFLabelQFrame_4)

        self.WIFQLineEdit_4 = QLineEdit(self.WIFQFrame_4)
        self.WIFQLineEdit_4.setObjectName(u"WIFQLineEdit_4")

        self.WIFVLayout_4.addWidget(self.WIFQLineEdit_4)


        self.verticalLayout_53.addWidget(self.WIFQFrame_4)

        self.frame_59 = QFrame(self.fromWIFQStackedWidget_4)
        self.frame_59.setObjectName(u"frame_59")
        self.verticalLayout_54 = QVBoxLayout(self.frame_59)
        self.verticalLayout_54.setSpacing(5)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFPassphraseLabelQFrame_4 = QFrame(self.frame_59)
        self.BIP38EncryptedWIFPassphraseLabelQFrame_4.setObjectName(u"BIP38EncryptedWIFPassphraseLabelQFrame_4")
        self.EPassphraseLabelHLayout_8 = QHBoxLayout(self.BIP38EncryptedWIFPassphraseLabelQFrame_4)
        self.EPassphraseLabelHLayout_8.setSpacing(15)
        self.EPassphraseLabelHLayout_8.setObjectName(u"EPassphraseLabelHLayout_8")
        self.EPassphraseLabelHLayout_8.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFQCheckBox_4 = QCheckBox(self.BIP38EncryptedWIFPassphraseLabelQFrame_4)
        self.BIP38EncryptedWIFQCheckBox_4.setObjectName(u"BIP38EncryptedWIFQCheckBox_4")

        self.EPassphraseLabelHLayout_8.addWidget(self.BIP38EncryptedWIFQCheckBox_4)

        self.BIP38EncryptedWIFPassphraseLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_8.addItem(self.BIP38EncryptedWIFPassphraseLabelHSpacer_4)


        self.verticalLayout_54.addWidget(self.BIP38EncryptedWIFPassphraseLabelQFrame_4)

        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.horizontalLayout_52 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_52.setSpacing(15)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.BIP38PassphraseQLineEdit_4 = QLineEdit(self.frame_60)
        self.BIP38PassphraseQLineEdit_4.setObjectName(u"BIP38PassphraseQLineEdit_4")

        self.horizontalLayout_52.addWidget(self.BIP38PassphraseQLineEdit_4)

        self.pushButton_14 = QPushButton(self.frame_60)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy1.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy1)

        self.horizontalLayout_52.addWidget(self.pushButton_14)


        self.verticalLayout_54.addWidget(self.frame_60)


        self.verticalLayout_53.addWidget(self.frame_59)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_24)

        self.fromQStackedWidget_4.addWidget(self.fromWIFQStackedWidget_4)
        self.fromPrivateKeyQStackedWidget_4 = QWidget()
        self.fromPrivateKeyQStackedWidget_4.setObjectName(u"fromPrivateKeyQStackedWidget_4")
        self.verticalLayout_55 = QVBoxLayout(self.fromPrivateKeyQStackedWidget_4)
        self.verticalLayout_55.setSpacing(15)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQFrame_4 = QFrame(self.fromPrivateKeyQStackedWidget_4)
        self.PrivateKeyQFrame_4.setObjectName(u"PrivateKeyQFrame_4")
        self.PrivateKeyQFrame_4.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_4 = QVBoxLayout(self.PrivateKeyQFrame_4)
        self.PrivateKeyVLayout_4.setSpacing(5)
        self.PrivateKeyVLayout_4.setObjectName(u"PrivateKeyVLayout_4")
        self.PrivateKeyVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyLabelQFrame_4 = QFrame(self.PrivateKeyQFrame_4)
        self.PrivateKeyLabelQFrame_4.setObjectName(u"PrivateKeyLabelQFrame_4")
        self.PrivateKeyLabelHLayout_4 = QHBoxLayout(self.PrivateKeyLabelQFrame_4)
        self.PrivateKeyLabelHLayout_4.setSpacing(15)
        self.PrivateKeyLabelHLayout_4.setObjectName(u"PrivateKeyLabelHLayout_4")
        self.PrivateKeyLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQLabel_4 = QLabel(self.PrivateKeyLabelQFrame_4)
        self.PrivateKeyQLabel_4.setObjectName(u"PrivateKeyQLabel_4")

        self.PrivateKeyLabelHLayout_4.addWidget(self.PrivateKeyQLabel_4)

        self.PrivateKeyLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_4.addItem(self.PrivateKeyLabelHSpacer_4)


        self.PrivateKeyVLayout_4.addWidget(self.PrivateKeyLabelQFrame_4)

        self.PrivateKeyQLineEdit_4 = QLineEdit(self.PrivateKeyQFrame_4)
        self.PrivateKeyQLineEdit_4.setObjectName(u"PrivateKeyQLineEdit_4")

        self.PrivateKeyVLayout_4.addWidget(self.PrivateKeyQLineEdit_4)


        self.verticalLayout_55.addWidget(self.PrivateKeyQFrame_4)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_25)

        self.fromQStackedWidget_4.addWidget(self.fromPrivateKeyQStackedWidget_4)
        self.fromPublicKeyQStackedWidget_4 = QWidget()
        self.fromPublicKeyQStackedWidget_4.setObjectName(u"fromPublicKeyQStackedWidget_4")
        self.verticalLayout_56 = QVBoxLayout(self.fromPublicKeyQStackedWidget_4)
        self.verticalLayout_56.setSpacing(15)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQFrame_4 = QFrame(self.fromPublicKeyQStackedWidget_4)
        self.PublicKeyQFrame_4.setObjectName(u"PublicKeyQFrame_4")
        self.PublicKeyVLayout_4 = QVBoxLayout(self.PublicKeyQFrame_4)
        self.PublicKeyVLayout_4.setSpacing(5)
        self.PublicKeyVLayout_4.setObjectName(u"PublicKeyVLayout_4")
        self.PublicKeyVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyLabelQFrame_4 = QFrame(self.PublicKeyQFrame_4)
        self.PublicKeyLabelQFrame_4.setObjectName(u"PublicKeyLabelQFrame_4")
        self.PublicKeyLabelHLayout_4 = QHBoxLayout(self.PublicKeyLabelQFrame_4)
        self.PublicKeyLabelHLayout_4.setSpacing(15)
        self.PublicKeyLabelHLayout_4.setObjectName(u"PublicKeyLabelHLayout_4")
        self.PublicKeyLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQLabel_4 = QLabel(self.PublicKeyLabelQFrame_4)
        self.PublicKeyQLabel_4.setObjectName(u"PublicKeyQLabel_4")

        self.PublicKeyLabelHLayout_4.addWidget(self.PublicKeyQLabel_4)

        self.PublicKeyLabelHSpacer_4 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PublicKeyLabelHLayout_4.addItem(self.PublicKeyLabelHSpacer_4)


        self.PublicKeyVLayout_4.addWidget(self.PublicKeyLabelQFrame_4)

        self.PublicKeyQLineEdit_4 = QLineEdit(self.PublicKeyQFrame_4)
        self.PublicKeyQLineEdit_4.setObjectName(u"PublicKeyQLineEdit_4")

        self.PublicKeyVLayout_4.addWidget(self.PublicKeyQLineEdit_4)


        self.verticalLayout_56.addWidget(self.PublicKeyQFrame_4)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_26)

        self.fromQStackedWidget_4.addWidget(self.fromPublicKeyQStackedWidget_4)

        self.verticalLayout_45.addWidget(self.fromQStackedWidget_4)

        self.stackedWidget.addWidget(self.ElectrumV1)
        self.ElectrumV2 = QWidget()
        self.ElectrumV2.setObjectName(u"ElectrumV2")
        self.verticalLayout_57 = QVBoxLayout(self.ElectrumV2)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.fromQStackedWidget_5 = QStackedWidget(self.ElectrumV2)
        self.fromQStackedWidget_5.setObjectName(u"fromQStackedWidget_5")
        self.fromEntropyQStackedWidget_5 = QWidget()
        self.fromEntropyQStackedWidget_5.setObjectName(u"fromEntropyQStackedWidget_5")
        self.verticalLayout_58 = QVBoxLayout(self.fromEntropyQStackedWidget_5)
        self.verticalLayout_58.setSpacing(15)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_61 = QFrame(self.fromEntropyQStackedWidget_5)
        self.frame_61.setObjectName(u"frame_61")
        self.verticalLayout_59 = QVBoxLayout(self.frame_61)
        self.verticalLayout_59.setSpacing(5)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.EntropyQFrame_5 = QFrame(self.frame_61)
        self.EntropyQFrame_5.setObjectName(u"EntropyQFrame_5")
        self.EntropyQFrame_5.setMinimumSize(QSize(400, 0))
        self.EntropyVLayout_6 = QVBoxLayout(self.EntropyQFrame_5)
        self.EntropyVLayout_6.setSpacing(15)
        self.EntropyVLayout_6.setObjectName(u"EntropyVLayout_6")
        self.EntropyVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.EntropyLabelQFrame_6 = QFrame(self.EntropyQFrame_5)
        self.EntropyLabelQFrame_6.setObjectName(u"EntropyLabelQFrame_6")
        self.EntropyLabelHLayout_6 = QHBoxLayout(self.EntropyLabelQFrame_6)
        self.EntropyLabelHLayout_6.setSpacing(15)
        self.EntropyLabelHLayout_6.setObjectName(u"EntropyLabelHLayout_6")
        self.EntropyLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLabel_6 = QLabel(self.EntropyLabelQFrame_6)
        self.EntropyQLabel_6.setObjectName(u"EntropyQLabel_6")

        self.EntropyLabelHLayout_6.addWidget(self.EntropyQLabel_6)

        self.EntropyLabelHSpacer_6 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_6.addItem(self.EntropyLabelHSpacer_6)


        self.EntropyVLayout_6.addWidget(self.EntropyLabelQFrame_6)


        self.verticalLayout_59.addWidget(self.EntropyQFrame_5)

        self.EGenerateQFrame_5 = QFrame(self.frame_61)
        self.EGenerateQFrame_5.setObjectName(u"EGenerateQFrame_5")
        self.horizontalLayout_53 = QHBoxLayout(self.EGenerateQFrame_5)
        self.horizontalLayout_53.setSpacing(15)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLineEdit_6 = QLineEdit(self.EGenerateQFrame_5)
        self.EntropyQLineEdit_6.setObjectName(u"EntropyQLineEdit_6")

        self.horizontalLayout_53.addWidget(self.EntropyQLineEdit_6)

        self.EGenerateQPushButton_6 = QPushButton(self.EGenerateQFrame_5)
        self.EGenerateQPushButton_6.setObjectName(u"EGenerateQPushButton_6")

        self.horizontalLayout_53.addWidget(self.EGenerateQPushButton_6)


        self.verticalLayout_59.addWidget(self.EGenerateQFrame_5)


        self.verticalLayout_58.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.fromEntropyQStackedWidget_5)
        self.frame_62.setObjectName(u"frame_62")
        self.horizontalLayout_54 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_54.setSpacing(15)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_13 = QFrame(self.frame_62)
        self.ClientQFrame_13.setObjectName(u"ClientQFrame_13")
        self.ClientQFrame_13.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_13 = QVBoxLayout(self.ClientQFrame_13)
        self.ClientVLayout_13.setSpacing(5)
        self.ClientVLayout_13.setObjectName(u"ClientVLayout_13")
        self.ClientVLayout_13.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_13 = QFrame(self.ClientQFrame_13)
        self.ClientLabelQFrame_13.setObjectName(u"ClientLabelQFrame_13")
        self.MStrengthLabelHLayout_17 = QHBoxLayout(self.ClientLabelQFrame_13)
        self.MStrengthLabelHLayout_17.setSpacing(15)
        self.MStrengthLabelHLayout_17.setObjectName(u"MStrengthLabelHLayout_17")
        self.MStrengthLabelHLayout_17.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_13 = QLabel(self.ClientLabelQFrame_13)
        self.ClientQLabel_13.setObjectName(u"ClientQLabel_13")

        self.MStrengthLabelHLayout_17.addWidget(self.ClientQLabel_13)

        self.ClientLabelHSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_17.addItem(self.ClientLabelHSpacer_13)


        self.ClientVLayout_13.addWidget(self.ClientLabelQFrame_13)

        self.ClientQComboBox_13 = QComboBox(self.ClientQFrame_13)
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.setObjectName(u"ClientQComboBox_13")

        self.ClientVLayout_13.addWidget(self.ClientQComboBox_13)


        self.horizontalLayout_54.addWidget(self.ClientQFrame_13)

        self.EPassphraseQFrame_5 = QFrame(self.frame_62)
        self.EPassphraseQFrame_5.setObjectName(u"EPassphraseQFrame_5")
        self.EPassphraseVLayout_9 = QVBoxLayout(self.EPassphraseQFrame_5)
        self.EPassphraseVLayout_9.setSpacing(5)
        self.EPassphraseVLayout_9.setObjectName(u"EPassphraseVLayout_9")
        self.EPassphraseVLayout_9.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseLabelQFrame_5 = QFrame(self.EPassphraseQFrame_5)
        self.EPassphraseLabelQFrame_5.setObjectName(u"EPassphraseLabelQFrame_5")
        self.EPassphraseLabelHLayout_9 = QHBoxLayout(self.EPassphraseLabelQFrame_5)
        self.EPassphraseLabelHLayout_9.setSpacing(15)
        self.EPassphraseLabelHLayout_9.setObjectName(u"EPassphraseLabelHLayout_9")
        self.EPassphraseLabelHLayout_9.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLabel_5 = QLabel(self.EPassphraseLabelQFrame_5)
        self.EPassphraseQLabel_5.setObjectName(u"EPassphraseQLabel_5")

        self.EPassphraseLabelHLayout_9.addWidget(self.EPassphraseQLabel_5)

        self.EPassphraseLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_9.addItem(self.EPassphraseLabelHSpacer_5)


        self.EPassphraseVLayout_9.addWidget(self.EPassphraseLabelQFrame_5)

        self.frame_63 = QFrame(self.EPassphraseQFrame_5)
        self.frame_63.setObjectName(u"frame_63")
        self.horizontalLayout_55 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_55.setSpacing(15)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLineEdit_5 = QLineEdit(self.frame_63)
        self.EPassphraseQLineEdit_5.setObjectName(u"EPassphraseQLineEdit_5")

        self.horizontalLayout_55.addWidget(self.EPassphraseQLineEdit_5)

        self.pushButton_15 = QPushButton(self.frame_63)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_55.addWidget(self.pushButton_15)


        self.EPassphraseVLayout_9.addWidget(self.frame_63)


        self.horizontalLayout_54.addWidget(self.EPassphraseQFrame_5)


        self.verticalLayout_58.addWidget(self.frame_62)

        self.frame_64 = QFrame(self.fromEntropyQStackedWidget_5)
        self.frame_64.setObjectName(u"frame_64")
        self.horizontalLayout_56 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_56.setSpacing(15)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQFrame_5 = QFrame(self.frame_64)
        self.ELanguageQFrame_5.setObjectName(u"ELanguageQFrame_5")
        self.ELanguageVLayout_5 = QVBoxLayout(self.ELanguageQFrame_5)
        self.ELanguageVLayout_5.setSpacing(5)
        self.ELanguageVLayout_5.setObjectName(u"ELanguageVLayout_5")
        self.ELanguageVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ELanguageLabelQFrame_5 = QFrame(self.ELanguageQFrame_5)
        self.ELanguageLabelQFrame_5.setObjectName(u"ELanguageLabelQFrame_5")
        self.ELanguageLabelHLayout_5 = QHBoxLayout(self.ELanguageLabelQFrame_5)
        self.ELanguageLabelHLayout_5.setSpacing(15)
        self.ELanguageLabelHLayout_5.setObjectName(u"ELanguageLabelHLayout_5")
        self.ELanguageLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQLabel_5 = QLabel(self.ELanguageLabelQFrame_5)
        self.ELanguageQLabel_5.setObjectName(u"ELanguageQLabel_5")

        self.ELanguageLabelHLayout_5.addWidget(self.ELanguageQLabel_5)

        self.ELanguageLabelHSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout_5.addItem(self.ELanguageLabelHSpacer_5)


        self.ELanguageVLayout_5.addWidget(self.ELanguageLabelQFrame_5)

        self.ELanguageQComboBox_5 = QComboBox(self.ELanguageQFrame_5)
        self.ELanguageQComboBox_5.addItem("")
        self.ELanguageQComboBox_5.addItem("")
        self.ELanguageQComboBox_5.addItem("")
        self.ELanguageQComboBox_5.addItem("")
        self.ELanguageQComboBox_5.addItem("")
        self.ELanguageQComboBox_5.addItem("")
        self.ELanguageQComboBox_5.addItem("")
        self.ELanguageQComboBox_5.addItem("")
        self.ELanguageQComboBox_5.setObjectName(u"ELanguageQComboBox_5")

        self.ELanguageVLayout_5.addWidget(self.ELanguageQComboBox_5)


        self.horizontalLayout_56.addWidget(self.ELanguageQFrame_5)

        self.EWordsQFrame_5 = QFrame(self.frame_64)
        self.EWordsQFrame_5.setObjectName(u"EWordsQFrame_5")
        self.EStrengthVLayout_5 = QVBoxLayout(self.EWordsQFrame_5)
        self.EStrengthVLayout_5.setSpacing(5)
        self.EStrengthVLayout_5.setObjectName(u"EStrengthVLayout_5")
        self.EStrengthVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.EWordsLabelQFrame_5 = QFrame(self.EWordsQFrame_5)
        self.EWordsLabelQFrame_5.setObjectName(u"EWordsLabelQFrame_5")
        self.EStrengthLabelHLayout_5 = QHBoxLayout(self.EWordsLabelQFrame_5)
        self.EStrengthLabelHLayout_5.setSpacing(15)
        self.EStrengthLabelHLayout_5.setObjectName(u"EStrengthLabelHLayout_5")
        self.EStrengthLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.EWordsQLabel_5 = QLabel(self.EWordsLabelQFrame_5)
        self.EWordsQLabel_5.setObjectName(u"EWordsQLabel_5")

        self.EStrengthLabelHLayout_5.addWidget(self.EWordsQLabel_5)

        self.EWordsLabelHSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout_5.addItem(self.EWordsLabelHSpacer_5)


        self.EStrengthVLayout_5.addWidget(self.EWordsLabelQFrame_5)

        self.EWordsQComboBox_5 = QComboBox(self.EWordsQFrame_5)
        self.EWordsQComboBox_5.addItem("")
        self.EWordsQComboBox_5.addItem("")
        self.EWordsQComboBox_5.addItem("")
        self.EWordsQComboBox_5.addItem("")
        self.EWordsQComboBox_5.addItem("")
        self.EWordsQComboBox_5.setObjectName(u"EWordsQComboBox_5")

        self.EStrengthVLayout_5.addWidget(self.EWordsQComboBox_5)


        self.horizontalLayout_56.addWidget(self.EWordsQFrame_5)


        self.verticalLayout_58.addWidget(self.frame_64)

        self.fromQStackedWidget_5.addWidget(self.fromEntropyQStackedWidget_5)
        self.fromMnemonicQStackedWidget_5 = QWidget()
        self.fromMnemonicQStackedWidget_5.setObjectName(u"fromMnemonicQStackedWidget_5")
        self.verticalLayout_60 = QVBoxLayout(self.fromMnemonicQStackedWidget_5)
        self.verticalLayout_60.setSpacing(15)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQFrame_5 = QFrame(self.fromMnemonicQStackedWidget_5)
        self.MnemonicQFrame_5.setObjectName(u"MnemonicQFrame_5")
        self.MnemonicVLayout_5 = QVBoxLayout(self.MnemonicQFrame_5)
        self.MnemonicVLayout_5.setSpacing(5)
        self.MnemonicVLayout_5.setObjectName(u"MnemonicVLayout_5")
        self.MnemonicVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MnemonicLabelQFrame_5 = QFrame(self.MnemonicQFrame_5)
        self.MnemonicLabelQFrame_5.setObjectName(u"MnemonicLabelQFrame_5")
        self.MnemonicLabelHLayout_5 = QHBoxLayout(self.MnemonicLabelQFrame_5)
        self.MnemonicLabelHLayout_5.setSpacing(15)
        self.MnemonicLabelHLayout_5.setObjectName(u"MnemonicLabelHLayout_5")
        self.MnemonicLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLabel_5 = QLabel(self.MnemonicLabelQFrame_5)
        self.MnemonicQLabel_5.setObjectName(u"MnemonicQLabel_5")

        self.MnemonicLabelHLayout_5.addWidget(self.MnemonicQLabel_5)

        self.MnemonicLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout_5.addItem(self.MnemonicLabelHSpacer_5)


        self.MnemonicVLayout_5.addWidget(self.MnemonicLabelQFrame_5)

        self.frame_65 = QFrame(self.MnemonicQFrame_5)
        self.frame_65.setObjectName(u"frame_65")
        self.horizontalLayout_57 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_57.setSpacing(15)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLineEdit_5 = QLineEdit(self.frame_65)
        self.MnemonicQLineEdit_5.setObjectName(u"MnemonicQLineEdit_5")

        self.horizontalLayout_57.addWidget(self.MnemonicQLineEdit_5)

        self.MGenerateQFrame_5 = QFrame(self.frame_65)
        self.MGenerateQFrame_5.setObjectName(u"MGenerateQFrame_5")
        self.GenerateMnemonicVLayout_5 = QVBoxLayout(self.MGenerateQFrame_5)
        self.GenerateMnemonicVLayout_5.setSpacing(15)
        self.GenerateMnemonicVLayout_5.setObjectName(u"GenerateMnemonicVLayout_5")
        self.GenerateMnemonicVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MGenerateQPushButton_5 = QPushButton(self.MGenerateQFrame_5)
        self.MGenerateQPushButton_5.setObjectName(u"MGenerateQPushButton_5")

        self.GenerateMnemonicVLayout_5.addWidget(self.MGenerateQPushButton_5)


        self.horizontalLayout_57.addWidget(self.MGenerateQFrame_5)


        self.MnemonicVLayout_5.addWidget(self.frame_65)


        self.verticalLayout_60.addWidget(self.MnemonicQFrame_5)

        self.frame_66 = QFrame(self.fromMnemonicQStackedWidget_5)
        self.frame_66.setObjectName(u"frame_66")
        self.horizontalLayout_58 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_58.setSpacing(15)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_14 = QFrame(self.frame_66)
        self.ClientQFrame_14.setObjectName(u"ClientQFrame_14")
        self.ClientQFrame_14.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_14 = QVBoxLayout(self.ClientQFrame_14)
        self.ClientVLayout_14.setSpacing(5)
        self.ClientVLayout_14.setObjectName(u"ClientVLayout_14")
        self.ClientVLayout_14.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_14 = QFrame(self.ClientQFrame_14)
        self.ClientLabelQFrame_14.setObjectName(u"ClientLabelQFrame_14")
        self.MStrengthLabelHLayout_18 = QHBoxLayout(self.ClientLabelQFrame_14)
        self.MStrengthLabelHLayout_18.setSpacing(15)
        self.MStrengthLabelHLayout_18.setObjectName(u"MStrengthLabelHLayout_18")
        self.MStrengthLabelHLayout_18.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_14 = QLabel(self.ClientLabelQFrame_14)
        self.ClientQLabel_14.setObjectName(u"ClientQLabel_14")

        self.MStrengthLabelHLayout_18.addWidget(self.ClientQLabel_14)

        self.ClientLabelHSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_18.addItem(self.ClientLabelHSpacer_14)


        self.ClientVLayout_14.addWidget(self.ClientLabelQFrame_14)

        self.ClientQComboBox_14 = QComboBox(self.ClientQFrame_14)
        self.ClientQComboBox_14.addItem("")
        self.ClientQComboBox_14.addItem("")
        self.ClientQComboBox_14.addItem("")
        self.ClientQComboBox_14.addItem("")
        self.ClientQComboBox_14.addItem("")
        self.ClientQComboBox_14.addItem("")
        self.ClientQComboBox_14.setObjectName(u"ClientQComboBox_14")

        self.ClientVLayout_14.addWidget(self.ClientQComboBox_14)


        self.horizontalLayout_58.addWidget(self.ClientQFrame_14)

        self.MPassphraseQFrame_5 = QFrame(self.frame_66)
        self.MPassphraseQFrame_5.setObjectName(u"MPassphraseQFrame_5")
        self.EPassphraseVLayout_10 = QVBoxLayout(self.MPassphraseQFrame_5)
        self.EPassphraseVLayout_10.setSpacing(5)
        self.EPassphraseVLayout_10.setObjectName(u"EPassphraseVLayout_10")
        self.EPassphraseVLayout_10.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseLabelQFrame_5 = QFrame(self.MPassphraseQFrame_5)
        self.MPassphraseLabelQFrame_5.setObjectName(u"MPassphraseLabelQFrame_5")
        self.MPassphraseLabelHLayout_5 = QHBoxLayout(self.MPassphraseLabelQFrame_5)
        self.MPassphraseLabelHLayout_5.setSpacing(15)
        self.MPassphraseLabelHLayout_5.setObjectName(u"MPassphraseLabelHLayout_5")
        self.MPassphraseLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLabel_5 = QLabel(self.MPassphraseLabelQFrame_5)
        self.MPassphraseQLabel_5.setObjectName(u"MPassphraseQLabel_5")

        self.MPassphraseLabelHLayout_5.addWidget(self.MPassphraseQLabel_5)

        self.MPassphraseLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout_5.addItem(self.MPassphraseLabelHSpacer_5)


        self.EPassphraseVLayout_10.addWidget(self.MPassphraseLabelQFrame_5)

        self.frame_67 = QFrame(self.MPassphraseQFrame_5)
        self.frame_67.setObjectName(u"frame_67")
        self.horizontalLayout_59 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_59.setSpacing(15)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLineEdit_5 = QLineEdit(self.frame_67)
        self.MPassphraseQLineEdit_5.setObjectName(u"MPassphraseQLineEdit_5")

        self.horizontalLayout_59.addWidget(self.MPassphraseQLineEdit_5)

        self.pushButton_16 = QPushButton(self.frame_67)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_59.addWidget(self.pushButton_16)


        self.EPassphraseVLayout_10.addWidget(self.frame_67)


        self.horizontalLayout_58.addWidget(self.MPassphraseQFrame_5)


        self.verticalLayout_60.addWidget(self.frame_66)

        self.frame_68 = QFrame(self.fromMnemonicQStackedWidget_5)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_60.setSpacing(15)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQFrame_5 = QFrame(self.frame_68)
        self.MLanguageQFrame_5.setObjectName(u"MLanguageQFrame_5")
        self.MLanguageVLayout_5 = QVBoxLayout(self.MLanguageQFrame_5)
        self.MLanguageVLayout_5.setSpacing(5)
        self.MLanguageVLayout_5.setObjectName(u"MLanguageVLayout_5")
        self.MLanguageVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MLanguageLabelQWidget_5 = QWidget(self.MLanguageQFrame_5)
        self.MLanguageLabelQWidget_5.setObjectName(u"MLanguageLabelQWidget_5")
        self.MLanguageLabelHLayout_5 = QHBoxLayout(self.MLanguageLabelQWidget_5)
        self.MLanguageLabelHLayout_5.setSpacing(15)
        self.MLanguageLabelHLayout_5.setObjectName(u"MLanguageLabelHLayout_5")
        self.MLanguageLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQLabel_5 = QLabel(self.MLanguageLabelQWidget_5)
        self.MLanguageQLabel_5.setObjectName(u"MLanguageQLabel_5")

        self.MLanguageLabelHLayout_5.addWidget(self.MLanguageQLabel_5)

        self.MLanguageLabelHSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MLanguageLabelHLayout_5.addItem(self.MLanguageLabelHSpacer_5)


        self.MLanguageVLayout_5.addWidget(self.MLanguageLabelQWidget_5)

        self.MLanguageQComboBox_5 = QComboBox(self.MLanguageQFrame_5)
        self.MLanguageQComboBox_5.addItem("")
        self.MLanguageQComboBox_5.addItem("")
        self.MLanguageQComboBox_5.addItem("")
        self.MLanguageQComboBox_5.addItem("")
        self.MLanguageQComboBox_5.addItem("")
        self.MLanguageQComboBox_5.addItem("")
        self.MLanguageQComboBox_5.addItem("")
        self.MLanguageQComboBox_5.addItem("")
        self.MLanguageQComboBox_5.setObjectName(u"MLanguageQComboBox_5")

        self.MLanguageVLayout_5.addWidget(self.MLanguageQComboBox_5)


        self.horizontalLayout_60.addWidget(self.MLanguageQFrame_5)

        self.MWordsQFrame_5 = QFrame(self.frame_68)
        self.MWordsQFrame_5.setObjectName(u"MWordsQFrame_5")
        self.MStrengthVLayout_5 = QVBoxLayout(self.MWordsQFrame_5)
        self.MStrengthVLayout_5.setSpacing(5)
        self.MStrengthVLayout_5.setObjectName(u"MStrengthVLayout_5")
        self.MStrengthVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MWordsLabelQFrame_5 = QFrame(self.MWordsQFrame_5)
        self.MWordsLabelQFrame_5.setObjectName(u"MWordsLabelQFrame_5")
        self.MStrengthLabelHLayout_19 = QHBoxLayout(self.MWordsLabelQFrame_5)
        self.MStrengthLabelHLayout_19.setSpacing(15)
        self.MStrengthLabelHLayout_19.setObjectName(u"MStrengthLabelHLayout_19")
        self.MStrengthLabelHLayout_19.setContentsMargins(0, 0, 0, 0)
        self.MWordsQLabel_5 = QLabel(self.MWordsLabelQFrame_5)
        self.MWordsQLabel_5.setObjectName(u"MWordsQLabel_5")

        self.MStrengthLabelHLayout_19.addWidget(self.MWordsQLabel_5)

        self.MWordsLabelHSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_19.addItem(self.MWordsLabelHSpacer_5)


        self.MStrengthVLayout_5.addWidget(self.MWordsLabelQFrame_5)

        self.MWordsQComboBox_5 = QComboBox(self.MWordsQFrame_5)
        self.MWordsQComboBox_5.addItem("")
        self.MWordsQComboBox_5.setObjectName(u"MWordsQComboBox_5")

        self.MStrengthVLayout_5.addWidget(self.MWordsQComboBox_5)


        self.horizontalLayout_60.addWidget(self.MWordsQFrame_5)


        self.verticalLayout_60.addWidget(self.frame_68)

        self.fromQStackedWidget_5.addWidget(self.fromMnemonicQStackedWidget_5)
        self.fromSeedQStackedWidget_5 = QWidget()
        self.fromSeedQStackedWidget_5.setObjectName(u"fromSeedQStackedWidget_5")
        self.verticalLayout_61 = QVBoxLayout(self.fromSeedQStackedWidget_5)
        self.verticalLayout_61.setSpacing(15)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.SeedQFrame_5 = QFrame(self.fromSeedQStackedWidget_5)
        self.SeedQFrame_5.setObjectName(u"SeedQFrame_5")
        self.SeedQFrame_5.setMinimumSize(QSize(400, 0))
        self.SeedVLayout_5 = QVBoxLayout(self.SeedQFrame_5)
        self.SeedVLayout_5.setSpacing(5)
        self.SeedVLayout_5.setObjectName(u"SeedVLayout_5")
        self.SeedVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.SeedQFrame_5)
        self.frame_69.setObjectName(u"frame_69")
        self.horizontalLayout_61 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_61.setSpacing(15)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_15 = QFrame(self.frame_69)
        self.ClientQFrame_15.setObjectName(u"ClientQFrame_15")
        self.ClientQFrame_15.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_15 = QVBoxLayout(self.ClientQFrame_15)
        self.ClientVLayout_15.setSpacing(5)
        self.ClientVLayout_15.setObjectName(u"ClientVLayout_15")
        self.ClientVLayout_15.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_15 = QFrame(self.ClientQFrame_15)
        self.ClientLabelQFrame_15.setObjectName(u"ClientLabelQFrame_15")
        self.MStrengthLabelHLayout_20 = QHBoxLayout(self.ClientLabelQFrame_15)
        self.MStrengthLabelHLayout_20.setSpacing(15)
        self.MStrengthLabelHLayout_20.setObjectName(u"MStrengthLabelHLayout_20")
        self.MStrengthLabelHLayout_20.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_15 = QLabel(self.ClientLabelQFrame_15)
        self.ClientQLabel_15.setObjectName(u"ClientQLabel_15")

        self.MStrengthLabelHLayout_20.addWidget(self.ClientQLabel_15)

        self.ClientLabelHSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_20.addItem(self.ClientLabelHSpacer_15)


        self.ClientVLayout_15.addWidget(self.ClientLabelQFrame_15)

        self.ClientQComboBox_15 = QComboBox(self.ClientQFrame_15)
        self.ClientQComboBox_15.addItem("")
        self.ClientQComboBox_15.addItem("")
        self.ClientQComboBox_15.addItem("")
        self.ClientQComboBox_15.addItem("")
        self.ClientQComboBox_15.addItem("")
        self.ClientQComboBox_15.addItem("")
        self.ClientQComboBox_15.setObjectName(u"ClientQComboBox_15")

        self.ClientVLayout_15.addWidget(self.ClientQComboBox_15)


        self.horizontalLayout_61.addWidget(self.ClientQFrame_15)

        self.frame_70 = QFrame(self.frame_69)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_70)
        self.verticalLayout_62.setSpacing(5)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.SeedLabelQFrame_5 = QFrame(self.frame_70)
        self.SeedLabelQFrame_5.setObjectName(u"SeedLabelQFrame_5")
        self.SeedLabelHLayout_5 = QHBoxLayout(self.SeedLabelQFrame_5)
        self.SeedLabelHLayout_5.setSpacing(15)
        self.SeedLabelHLayout_5.setObjectName(u"SeedLabelHLayout_5")
        self.SeedLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.SeedQLabel_5 = QLabel(self.SeedLabelQFrame_5)
        self.SeedQLabel_5.setObjectName(u"SeedQLabel_5")

        self.SeedLabelHLayout_5.addWidget(self.SeedQLabel_5)

        self.SeedLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout_5.addItem(self.SeedLabelHSpacer_5)


        self.verticalLayout_62.addWidget(self.SeedLabelQFrame_5)

        self.SeedQLineEdit_5 = QLineEdit(self.frame_70)
        self.SeedQLineEdit_5.setObjectName(u"SeedQLineEdit_5")

        self.verticalLayout_62.addWidget(self.SeedQLineEdit_5)


        self.horizontalLayout_61.addWidget(self.frame_70)


        self.SeedVLayout_5.addWidget(self.frame_69)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout_5.addItem(self.verticalSpacer_27)


        self.verticalLayout_61.addWidget(self.SeedQFrame_5)

        self.fromQStackedWidget_5.addWidget(self.fromSeedQStackedWidget_5)
        self.fromXPrivateKeyQStackedWidget_5 = QWidget()
        self.fromXPrivateKeyQStackedWidget_5.setObjectName(u"fromXPrivateKeyQStackedWidget_5")
        self.verticalLayout_63 = QVBoxLayout(self.fromXPrivateKeyQStackedWidget_5)
        self.verticalLayout_63.setSpacing(15)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQFrame_5 = QFrame(self.fromXPrivateKeyQStackedWidget_5)
        self.XPrivateKeyQFrame_5.setObjectName(u"XPrivateKeyQFrame_5")
        self.XPrivateKeyVLayout_5 = QVBoxLayout(self.XPrivateKeyQFrame_5)
        self.XPrivateKeyVLayout_5.setSpacing(5)
        self.XPrivateKeyVLayout_5.setObjectName(u"XPrivateKeyVLayout_5")
        self.XPrivateKeyVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyLabelQFrame_5 = QFrame(self.XPrivateKeyQFrame_5)
        self.XPrivateKeyLabelQFrame_5.setObjectName(u"XPrivateKeyLabelQFrame_5")
        self.XPrivateKeyLabelHLayout_5 = QHBoxLayout(self.XPrivateKeyLabelQFrame_5)
        self.XPrivateKeyLabelHLayout_5.setSpacing(15)
        self.XPrivateKeyLabelHLayout_5.setObjectName(u"XPrivateKeyLabelHLayout_5")
        self.XPrivateKeyLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQLabel_5 = QLabel(self.XPrivateKeyLabelQFrame_5)
        self.XPrivateKeyQLabel_5.setObjectName(u"XPrivateKeyQLabel_5")

        self.XPrivateKeyLabelHLayout_5.addWidget(self.XPrivateKeyQLabel_5)

        self.XPrivateKeyLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPrivateKeyLabelHLayout_5.addItem(self.XPrivateKeyLabelHSpacer_5)


        self.XPrivateKeyVLayout_5.addWidget(self.XPrivateKeyLabelQFrame_5)

        self.XPrivateKeyQLineEdit_5 = QLineEdit(self.XPrivateKeyQFrame_5)
        self.XPrivateKeyQLineEdit_5.setObjectName(u"XPrivateKeyQLineEdit_5")

        self.XPrivateKeyVLayout_5.addWidget(self.XPrivateKeyQLineEdit_5)


        self.verticalLayout_63.addWidget(self.XPrivateKeyQFrame_5)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_28)

        self.fromQStackedWidget_5.addWidget(self.fromXPrivateKeyQStackedWidget_5)
        self.fromXPublicKeyQStackedWidget_5 = QWidget()
        self.fromXPublicKeyQStackedWidget_5.setObjectName(u"fromXPublicKeyQStackedWidget_5")
        self.verticalLayout_64 = QVBoxLayout(self.fromXPublicKeyQStackedWidget_5)
        self.verticalLayout_64.setSpacing(15)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQFrame_5 = QFrame(self.fromXPublicKeyQStackedWidget_5)
        self.XPublicKeyQFrame_5.setObjectName(u"XPublicKeyQFrame_5")
        self.XPublicKeyVLayout_5 = QVBoxLayout(self.XPublicKeyQFrame_5)
        self.XPublicKeyVLayout_5.setSpacing(5)
        self.XPublicKeyVLayout_5.setObjectName(u"XPublicKeyVLayout_5")
        self.XPublicKeyVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyLabelQFrame_5 = QFrame(self.XPublicKeyQFrame_5)
        self.XPublicKeyLabelQFrame_5.setObjectName(u"XPublicKeyLabelQFrame_5")
        self.XPublicKeyLabelHLayout_5 = QHBoxLayout(self.XPublicKeyLabelQFrame_5)
        self.XPublicKeyLabelHLayout_5.setSpacing(15)
        self.XPublicKeyLabelHLayout_5.setObjectName(u"XPublicKeyLabelHLayout_5")
        self.XPublicKeyLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQLabel_5 = QLabel(self.XPublicKeyLabelQFrame_5)
        self.XPublicKeyQLabel_5.setObjectName(u"XPublicKeyQLabel_5")

        self.XPublicKeyLabelHLayout_5.addWidget(self.XPublicKeyQLabel_5)

        self.XPublicKeyLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPublicKeyLabelHLayout_5.addItem(self.XPublicKeyLabelHSpacer_5)


        self.XPublicKeyVLayout_5.addWidget(self.XPublicKeyLabelQFrame_5)

        self.XPublicKeyQLineEdit_5 = QLineEdit(self.XPublicKeyQFrame_5)
        self.XPublicKeyQLineEdit_5.setObjectName(u"XPublicKeyQLineEdit_5")

        self.XPublicKeyVLayout_5.addWidget(self.XPublicKeyQLineEdit_5)


        self.verticalLayout_64.addWidget(self.XPublicKeyQFrame_5)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_64.addItem(self.verticalSpacer_29)

        self.fromQStackedWidget_5.addWidget(self.fromXPublicKeyQStackedWidget_5)
        self.fromWIFQStackedWidget_5 = QWidget()
        self.fromWIFQStackedWidget_5.setObjectName(u"fromWIFQStackedWidget_5")
        self.verticalLayout_65 = QVBoxLayout(self.fromWIFQStackedWidget_5)
        self.verticalLayout_65.setSpacing(15)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.WIFQFrame_5 = QFrame(self.fromWIFQStackedWidget_5)
        self.WIFQFrame_5.setObjectName(u"WIFQFrame_5")
        self.WIFQFrame_5.setMinimumSize(QSize(400, 0))
        self.WIFVLayout_5 = QVBoxLayout(self.WIFQFrame_5)
        self.WIFVLayout_5.setSpacing(5)
        self.WIFVLayout_5.setObjectName(u"WIFVLayout_5")
        self.WIFVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.WIFLabelQFrame_5 = QFrame(self.WIFQFrame_5)
        self.WIFLabelQFrame_5.setObjectName(u"WIFLabelQFrame_5")
        self.WIFLabelHLayout_5 = QHBoxLayout(self.WIFLabelQFrame_5)
        self.WIFLabelHLayout_5.setSpacing(15)
        self.WIFLabelHLayout_5.setObjectName(u"WIFLabelHLayout_5")
        self.WIFLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.WIFQLabel_5 = QLabel(self.WIFLabelQFrame_5)
        self.WIFQLabel_5.setObjectName(u"WIFQLabel_5")

        self.WIFLabelHLayout_5.addWidget(self.WIFQLabel_5)

        self.WIFLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WIFLabelHLayout_5.addItem(self.WIFLabelHSpacer_5)


        self.WIFVLayout_5.addWidget(self.WIFLabelQFrame_5)

        self.WIFQLineEdit_5 = QLineEdit(self.WIFQFrame_5)
        self.WIFQLineEdit_5.setObjectName(u"WIFQLineEdit_5")

        self.WIFVLayout_5.addWidget(self.WIFQLineEdit_5)


        self.verticalLayout_65.addWidget(self.WIFQFrame_5)

        self.frame_71 = QFrame(self.fromWIFQStackedWidget_5)
        self.frame_71.setObjectName(u"frame_71")
        self.verticalLayout_66 = QVBoxLayout(self.frame_71)
        self.verticalLayout_66.setSpacing(5)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFPassphraseLabelQFrame_5 = QFrame(self.frame_71)
        self.BIP38EncryptedWIFPassphraseLabelQFrame_5.setObjectName(u"BIP38EncryptedWIFPassphraseLabelQFrame_5")
        self.EPassphraseLabelHLayout_10 = QHBoxLayout(self.BIP38EncryptedWIFPassphraseLabelQFrame_5)
        self.EPassphraseLabelHLayout_10.setSpacing(15)
        self.EPassphraseLabelHLayout_10.setObjectName(u"EPassphraseLabelHLayout_10")
        self.EPassphraseLabelHLayout_10.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFQCheckBox_5 = QCheckBox(self.BIP38EncryptedWIFPassphraseLabelQFrame_5)
        self.BIP38EncryptedWIFQCheckBox_5.setObjectName(u"BIP38EncryptedWIFQCheckBox_5")

        self.EPassphraseLabelHLayout_10.addWidget(self.BIP38EncryptedWIFQCheckBox_5)

        self.BIP38EncryptedWIFPassphraseLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_10.addItem(self.BIP38EncryptedWIFPassphraseLabelHSpacer_5)


        self.verticalLayout_66.addWidget(self.BIP38EncryptedWIFPassphraseLabelQFrame_5)

        self.frame_72 = QFrame(self.frame_71)
        self.frame_72.setObjectName(u"frame_72")
        self.horizontalLayout_62 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_62.setSpacing(15)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.BIP38PassphraseQLineEdit_5 = QLineEdit(self.frame_72)
        self.BIP38PassphraseQLineEdit_5.setObjectName(u"BIP38PassphraseQLineEdit_5")

        self.horizontalLayout_62.addWidget(self.BIP38PassphraseQLineEdit_5)

        self.pushButton_17 = QPushButton(self.frame_72)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy1.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy1)

        self.horizontalLayout_62.addWidget(self.pushButton_17)


        self.verticalLayout_66.addWidget(self.frame_72)


        self.verticalLayout_65.addWidget(self.frame_71)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_30)

        self.fromQStackedWidget_5.addWidget(self.fromWIFQStackedWidget_5)
        self.fromPrivateKeyQStackedWidget_5 = QWidget()
        self.fromPrivateKeyQStackedWidget_5.setObjectName(u"fromPrivateKeyQStackedWidget_5")
        self.verticalLayout_67 = QVBoxLayout(self.fromPrivateKeyQStackedWidget_5)
        self.verticalLayout_67.setSpacing(15)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQFrame_5 = QFrame(self.fromPrivateKeyQStackedWidget_5)
        self.PrivateKeyQFrame_5.setObjectName(u"PrivateKeyQFrame_5")
        self.PrivateKeyQFrame_5.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_5 = QVBoxLayout(self.PrivateKeyQFrame_5)
        self.PrivateKeyVLayout_5.setSpacing(5)
        self.PrivateKeyVLayout_5.setObjectName(u"PrivateKeyVLayout_5")
        self.PrivateKeyVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyLabelQFrame_5 = QFrame(self.PrivateKeyQFrame_5)
        self.PrivateKeyLabelQFrame_5.setObjectName(u"PrivateKeyLabelQFrame_5")
        self.PrivateKeyLabelHLayout_5 = QHBoxLayout(self.PrivateKeyLabelQFrame_5)
        self.PrivateKeyLabelHLayout_5.setSpacing(15)
        self.PrivateKeyLabelHLayout_5.setObjectName(u"PrivateKeyLabelHLayout_5")
        self.PrivateKeyLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQLabel_5 = QLabel(self.PrivateKeyLabelQFrame_5)
        self.PrivateKeyQLabel_5.setObjectName(u"PrivateKeyQLabel_5")

        self.PrivateKeyLabelHLayout_5.addWidget(self.PrivateKeyQLabel_5)

        self.PrivateKeyLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_5.addItem(self.PrivateKeyLabelHSpacer_5)


        self.PrivateKeyVLayout_5.addWidget(self.PrivateKeyLabelQFrame_5)

        self.PrivateKeyQLineEdit_5 = QLineEdit(self.PrivateKeyQFrame_5)
        self.PrivateKeyQLineEdit_5.setObjectName(u"PrivateKeyQLineEdit_5")

        self.PrivateKeyVLayout_5.addWidget(self.PrivateKeyQLineEdit_5)


        self.verticalLayout_67.addWidget(self.PrivateKeyQFrame_5)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_67.addItem(self.verticalSpacer_31)

        self.fromQStackedWidget_5.addWidget(self.fromPrivateKeyQStackedWidget_5)
        self.fromPublicKeyQStackedWidget_5 = QWidget()
        self.fromPublicKeyQStackedWidget_5.setObjectName(u"fromPublicKeyQStackedWidget_5")
        self.verticalLayout_68 = QVBoxLayout(self.fromPublicKeyQStackedWidget_5)
        self.verticalLayout_68.setSpacing(15)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQFrame_5 = QFrame(self.fromPublicKeyQStackedWidget_5)
        self.PublicKeyQFrame_5.setObjectName(u"PublicKeyQFrame_5")
        self.PublicKeyVLayout_5 = QVBoxLayout(self.PublicKeyQFrame_5)
        self.PublicKeyVLayout_5.setSpacing(5)
        self.PublicKeyVLayout_5.setObjectName(u"PublicKeyVLayout_5")
        self.PublicKeyVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyLabelQFrame_5 = QFrame(self.PublicKeyQFrame_5)
        self.PublicKeyLabelQFrame_5.setObjectName(u"PublicKeyLabelQFrame_5")
        self.PublicKeyLabelHLayout_5 = QHBoxLayout(self.PublicKeyLabelQFrame_5)
        self.PublicKeyLabelHLayout_5.setSpacing(15)
        self.PublicKeyLabelHLayout_5.setObjectName(u"PublicKeyLabelHLayout_5")
        self.PublicKeyLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQLabel_5 = QLabel(self.PublicKeyLabelQFrame_5)
        self.PublicKeyQLabel_5.setObjectName(u"PublicKeyQLabel_5")

        self.PublicKeyLabelHLayout_5.addWidget(self.PublicKeyQLabel_5)

        self.PublicKeyLabelHSpacer_5 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PublicKeyLabelHLayout_5.addItem(self.PublicKeyLabelHSpacer_5)


        self.PublicKeyVLayout_5.addWidget(self.PublicKeyLabelQFrame_5)

        self.PublicKeyQLineEdit_5 = QLineEdit(self.PublicKeyQFrame_5)
        self.PublicKeyQLineEdit_5.setObjectName(u"PublicKeyQLineEdit_5")

        self.PublicKeyVLayout_5.addWidget(self.PublicKeyQLineEdit_5)


        self.verticalLayout_68.addWidget(self.PublicKeyQFrame_5)

        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_68.addItem(self.verticalSpacer_32)

        self.fromQStackedWidget_5.addWidget(self.fromPublicKeyQStackedWidget_5)

        self.verticalLayout_57.addWidget(self.fromQStackedWidget_5)

        self.stackedWidget.addWidget(self.ElectrumV2)
        self.Monero = QWidget()
        self.Monero.setObjectName(u"Monero")
        self.verticalLayout_69 = QVBoxLayout(self.Monero)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.fromQStackedWidget = QStackedWidget(self.Monero)
        self.fromQStackedWidget.setObjectName(u"fromQStackedWidget")
        self.fromEntropyQStackedWidget = QWidget()
        self.fromEntropyQStackedWidget.setObjectName(u"fromEntropyQStackedWidget")
        self.verticalLayout_4 = QVBoxLayout(self.fromEntropyQStackedWidget)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.fromEntropyQStackedWidget)
        self.frame_16.setObjectName(u"frame_16")
        self.verticalLayout_8 = QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.EntropyQFrame = QFrame(self.frame_16)
        self.EntropyQFrame.setObjectName(u"EntropyQFrame")
        self.EntropyQFrame.setMinimumSize(QSize(400, 0))
        self.EntropyVLayout_2 = QVBoxLayout(self.EntropyQFrame)
        self.EntropyVLayout_2.setSpacing(15)
        self.EntropyVLayout_2.setObjectName(u"EntropyVLayout_2")
        self.EntropyVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.EntropyLabelQFrame_2 = QFrame(self.EntropyQFrame)
        self.EntropyLabelQFrame_2.setObjectName(u"EntropyLabelQFrame_2")
        self.EntropyLabelHLayout_2 = QHBoxLayout(self.EntropyLabelQFrame_2)
        self.EntropyLabelHLayout_2.setSpacing(15)
        self.EntropyLabelHLayout_2.setObjectName(u"EntropyLabelHLayout_2")
        self.EntropyLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLabel_2 = QLabel(self.EntropyLabelQFrame_2)
        self.EntropyQLabel_2.setObjectName(u"EntropyQLabel_2")

        self.EntropyLabelHLayout_2.addWidget(self.EntropyQLabel_2)

        self.EntropyLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_2.addItem(self.EntropyLabelHSpacer_2)


        self.EntropyVLayout_2.addWidget(self.EntropyLabelQFrame_2)


        self.verticalLayout_8.addWidget(self.EntropyQFrame)

        self.EGenerateQFrame = QFrame(self.frame_16)
        self.EGenerateQFrame.setObjectName(u"EGenerateQFrame")
        self.horizontalLayout_13 = QHBoxLayout(self.EGenerateQFrame)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLineEdit_2 = QLineEdit(self.EGenerateQFrame)
        self.EntropyQLineEdit_2.setObjectName(u"EntropyQLineEdit_2")

        self.horizontalLayout_13.addWidget(self.EntropyQLineEdit_2)

        self.EGenerateQPushButton_2 = QPushButton(self.EGenerateQFrame)
        self.EGenerateQPushButton_2.setObjectName(u"EGenerateQPushButton_2")

        self.horizontalLayout_13.addWidget(self.EGenerateQPushButton_2)


        self.verticalLayout_8.addWidget(self.EGenerateQFrame)


        self.verticalLayout_4.addWidget(self.frame_16)

        self.frame_7 = QFrame(self.fromEntropyQStackedWidget)
        self.frame_7.setObjectName(u"frame_7")
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame = QFrame(self.frame_7)
        self.ClientQFrame.setObjectName(u"ClientQFrame")
        self.ClientQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout = QVBoxLayout(self.ClientQFrame)
        self.ClientVLayout.setSpacing(5)
        self.ClientVLayout.setObjectName(u"ClientVLayout")
        self.ClientVLayout.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame = QFrame(self.ClientQFrame)
        self.ClientLabelQFrame.setObjectName(u"ClientLabelQFrame")
        self.MStrengthLabelHLayout_3 = QHBoxLayout(self.ClientLabelQFrame)
        self.MStrengthLabelHLayout_3.setSpacing(15)
        self.MStrengthLabelHLayout_3.setObjectName(u"MStrengthLabelHLayout_3")
        self.MStrengthLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel = QLabel(self.ClientLabelQFrame)
        self.ClientQLabel.setObjectName(u"ClientQLabel")

        self.MStrengthLabelHLayout_3.addWidget(self.ClientQLabel)

        self.ClientLabelHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_3.addItem(self.ClientLabelHSpacer)


        self.ClientVLayout.addWidget(self.ClientLabelQFrame)

        self.ClientQComboBox = QComboBox(self.ClientQFrame)
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.setObjectName(u"ClientQComboBox")

        self.ClientVLayout.addWidget(self.ClientQComboBox)


        self.horizontalLayout_9.addWidget(self.ClientQFrame)

        self.EPassphraseQFrame = QFrame(self.frame_7)
        self.EPassphraseQFrame.setObjectName(u"EPassphraseQFrame")
        self.EPassphraseVLayout = QVBoxLayout(self.EPassphraseQFrame)
        self.EPassphraseVLayout.setSpacing(5)
        self.EPassphraseVLayout.setObjectName(u"EPassphraseVLayout")
        self.EPassphraseVLayout.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseLabelQFrame = QFrame(self.EPassphraseQFrame)
        self.EPassphraseLabelQFrame.setObjectName(u"EPassphraseLabelQFrame")
        self.EPassphraseLabelHLayout = QHBoxLayout(self.EPassphraseLabelQFrame)
        self.EPassphraseLabelHLayout.setSpacing(15)
        self.EPassphraseLabelHLayout.setObjectName(u"EPassphraseLabelHLayout")
        self.EPassphraseLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLabel = QLabel(self.EPassphraseLabelQFrame)
        self.EPassphraseQLabel.setObjectName(u"EPassphraseQLabel")

        self.EPassphraseLabelHLayout.addWidget(self.EPassphraseQLabel)

        self.EPassphraseLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout.addItem(self.EPassphraseLabelHSpacer)


        self.EPassphraseVLayout.addWidget(self.EPassphraseLabelQFrame)

        self.frame_12 = QFrame(self.EPassphraseQFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setSpacing(15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLineEdit = QLineEdit(self.frame_12)
        self.EPassphraseQLineEdit.setObjectName(u"EPassphraseQLineEdit")

        self.horizontalLayout_15.addWidget(self.EPassphraseQLineEdit)

        self.pushButton = QPushButton(self.frame_12)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_15.addWidget(self.pushButton)


        self.EPassphraseVLayout.addWidget(self.frame_12)


        self.horizontalLayout_9.addWidget(self.EPassphraseQFrame)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.fromEntropyQStackedWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQFrame = QFrame(self.frame_8)
        self.ELanguageQFrame.setObjectName(u"ELanguageQFrame")
        self.ELanguageVLayout = QVBoxLayout(self.ELanguageQFrame)
        self.ELanguageVLayout.setSpacing(5)
        self.ELanguageVLayout.setObjectName(u"ELanguageVLayout")
        self.ELanguageVLayout.setContentsMargins(0, 0, 0, 0)
        self.ELanguageLabelQFrame = QFrame(self.ELanguageQFrame)
        self.ELanguageLabelQFrame.setObjectName(u"ELanguageLabelQFrame")
        self.ELanguageLabelHLayout = QHBoxLayout(self.ELanguageLabelQFrame)
        self.ELanguageLabelHLayout.setSpacing(15)
        self.ELanguageLabelHLayout.setObjectName(u"ELanguageLabelHLayout")
        self.ELanguageLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQLabel = QLabel(self.ELanguageLabelQFrame)
        self.ELanguageQLabel.setObjectName(u"ELanguageQLabel")

        self.ELanguageLabelHLayout.addWidget(self.ELanguageQLabel)

        self.ELanguageLabelHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout.addItem(self.ELanguageLabelHSpacer)


        self.ELanguageVLayout.addWidget(self.ELanguageLabelQFrame)

        self.ELanguageQComboBox = QComboBox(self.ELanguageQFrame)
        self.ELanguageQComboBox.addItem("")
        self.ELanguageQComboBox.addItem("")
        self.ELanguageQComboBox.addItem("")
        self.ELanguageQComboBox.addItem("")
        self.ELanguageQComboBox.addItem("")
        self.ELanguageQComboBox.addItem("")
        self.ELanguageQComboBox.addItem("")
        self.ELanguageQComboBox.addItem("")
        self.ELanguageQComboBox.setObjectName(u"ELanguageQComboBox")

        self.ELanguageVLayout.addWidget(self.ELanguageQComboBox)


        self.horizontalLayout_7.addWidget(self.ELanguageQFrame)

        self.EWordsQFrame = QFrame(self.frame_8)
        self.EWordsQFrame.setObjectName(u"EWordsQFrame")
        self.EStrengthVLayout = QVBoxLayout(self.EWordsQFrame)
        self.EStrengthVLayout.setSpacing(5)
        self.EStrengthVLayout.setObjectName(u"EStrengthVLayout")
        self.EStrengthVLayout.setContentsMargins(0, 0, 0, 0)
        self.EWordsLabelQFrame = QFrame(self.EWordsQFrame)
        self.EWordsLabelQFrame.setObjectName(u"EWordsLabelQFrame")
        self.EStrengthLabelHLayout = QHBoxLayout(self.EWordsLabelQFrame)
        self.EStrengthLabelHLayout.setSpacing(15)
        self.EStrengthLabelHLayout.setObjectName(u"EStrengthLabelHLayout")
        self.EStrengthLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.EWordsQLabel = QLabel(self.EWordsLabelQFrame)
        self.EWordsQLabel.setObjectName(u"EWordsQLabel")

        self.EStrengthLabelHLayout.addWidget(self.EWordsQLabel)

        self.EWordsLabelHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout.addItem(self.EWordsLabelHSpacer)


        self.EStrengthVLayout.addWidget(self.EWordsLabelQFrame)

        self.EWordsQComboBox = QComboBox(self.EWordsQFrame)
        self.EWordsQComboBox.addItem("")
        self.EWordsQComboBox.addItem("")
        self.EWordsQComboBox.addItem("")
        self.EWordsQComboBox.addItem("")
        self.EWordsQComboBox.addItem("")
        self.EWordsQComboBox.setObjectName(u"EWordsQComboBox")

        self.EStrengthVLayout.addWidget(self.EWordsQComboBox)


        self.horizontalLayout_7.addWidget(self.EWordsQFrame)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.fromQStackedWidget.addWidget(self.fromEntropyQStackedWidget)
        self.fromMnemonicQStackedWidget = QWidget()
        self.fromMnemonicQStackedWidget.setObjectName(u"fromMnemonicQStackedWidget")
        self.verticalLayout_7 = QVBoxLayout(self.fromMnemonicQStackedWidget)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQFrame = QFrame(self.fromMnemonicQStackedWidget)
        self.MnemonicQFrame.setObjectName(u"MnemonicQFrame")
        self.MnemonicVLayout = QVBoxLayout(self.MnemonicQFrame)
        self.MnemonicVLayout.setSpacing(5)
        self.MnemonicVLayout.setObjectName(u"MnemonicVLayout")
        self.MnemonicVLayout.setContentsMargins(0, 0, 0, 0)
        self.MnemonicLabelQFrame = QFrame(self.MnemonicQFrame)
        self.MnemonicLabelQFrame.setObjectName(u"MnemonicLabelQFrame")
        self.MnemonicLabelHLayout = QHBoxLayout(self.MnemonicLabelQFrame)
        self.MnemonicLabelHLayout.setSpacing(15)
        self.MnemonicLabelHLayout.setObjectName(u"MnemonicLabelHLayout")
        self.MnemonicLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLabel = QLabel(self.MnemonicLabelQFrame)
        self.MnemonicQLabel.setObjectName(u"MnemonicQLabel")

        self.MnemonicLabelHLayout.addWidget(self.MnemonicQLabel)

        self.MnemonicLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout.addItem(self.MnemonicLabelHSpacer)


        self.MnemonicVLayout.addWidget(self.MnemonicLabelQFrame)

        self.frame_13 = QFrame(self.MnemonicQFrame)
        self.frame_13.setObjectName(u"frame_13")
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLineEdit = QLineEdit(self.frame_13)
        self.MnemonicQLineEdit.setObjectName(u"MnemonicQLineEdit")

        self.horizontalLayout_10.addWidget(self.MnemonicQLineEdit)

        self.MGenerateQFrame = QFrame(self.frame_13)
        self.MGenerateQFrame.setObjectName(u"MGenerateQFrame")
        self.GenerateMnemonicVLayout = QVBoxLayout(self.MGenerateQFrame)
        self.GenerateMnemonicVLayout.setSpacing(15)
        self.GenerateMnemonicVLayout.setObjectName(u"GenerateMnemonicVLayout")
        self.GenerateMnemonicVLayout.setContentsMargins(0, 0, 0, 0)
        self.MGenerateQPushButton = QPushButton(self.MGenerateQFrame)
        self.MGenerateQPushButton.setObjectName(u"MGenerateQPushButton")

        self.GenerateMnemonicVLayout.addWidget(self.MGenerateQPushButton)


        self.horizontalLayout_10.addWidget(self.MGenerateQFrame)


        self.MnemonicVLayout.addWidget(self.frame_13)


        self.verticalLayout_7.addWidget(self.MnemonicQFrame)

        self.frame_15 = QFrame(self.fromMnemonicQStackedWidget)
        self.frame_15.setObjectName(u"frame_15")
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_2 = QFrame(self.frame_15)
        self.ClientQFrame_2.setObjectName(u"ClientQFrame_2")
        self.ClientQFrame_2.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_2 = QVBoxLayout(self.ClientQFrame_2)
        self.ClientVLayout_2.setSpacing(5)
        self.ClientVLayout_2.setObjectName(u"ClientVLayout_2")
        self.ClientVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_2 = QFrame(self.ClientQFrame_2)
        self.ClientLabelQFrame_2.setObjectName(u"ClientLabelQFrame_2")
        self.MStrengthLabelHLayout_4 = QHBoxLayout(self.ClientLabelQFrame_2)
        self.MStrengthLabelHLayout_4.setSpacing(15)
        self.MStrengthLabelHLayout_4.setObjectName(u"MStrengthLabelHLayout_4")
        self.MStrengthLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_2 = QLabel(self.ClientLabelQFrame_2)
        self.ClientQLabel_2.setObjectName(u"ClientQLabel_2")

        self.MStrengthLabelHLayout_4.addWidget(self.ClientQLabel_2)

        self.ClientLabelHSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_4.addItem(self.ClientLabelHSpacer_2)


        self.ClientVLayout_2.addWidget(self.ClientLabelQFrame_2)

        self.ClientQComboBox_2 = QComboBox(self.ClientQFrame_2)
        self.ClientQComboBox_2.addItem("")
        self.ClientQComboBox_2.addItem("")
        self.ClientQComboBox_2.addItem("")
        self.ClientQComboBox_2.addItem("")
        self.ClientQComboBox_2.addItem("")
        self.ClientQComboBox_2.addItem("")
        self.ClientQComboBox_2.setObjectName(u"ClientQComboBox_2")

        self.ClientVLayout_2.addWidget(self.ClientQComboBox_2)


        self.horizontalLayout_12.addWidget(self.ClientQFrame_2)

        self.MPassphraseQFrame = QFrame(self.frame_15)
        self.MPassphraseQFrame.setObjectName(u"MPassphraseQFrame")
        self.EPassphraseVLayout_2 = QVBoxLayout(self.MPassphraseQFrame)
        self.EPassphraseVLayout_2.setSpacing(5)
        self.EPassphraseVLayout_2.setObjectName(u"EPassphraseVLayout_2")
        self.EPassphraseVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseLabelQFrame = QFrame(self.MPassphraseQFrame)
        self.MPassphraseLabelQFrame.setObjectName(u"MPassphraseLabelQFrame")
        self.MPassphraseLabelHLayout = QHBoxLayout(self.MPassphraseLabelQFrame)
        self.MPassphraseLabelHLayout.setSpacing(15)
        self.MPassphraseLabelHLayout.setObjectName(u"MPassphraseLabelHLayout")
        self.MPassphraseLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLabel = QLabel(self.MPassphraseLabelQFrame)
        self.MPassphraseQLabel.setObjectName(u"MPassphraseQLabel")

        self.MPassphraseLabelHLayout.addWidget(self.MPassphraseQLabel)

        self.MPassphraseLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout.addItem(self.MPassphraseLabelHSpacer)


        self.EPassphraseVLayout_2.addWidget(self.MPassphraseLabelQFrame)

        self.frame_19 = QFrame(self.MPassphraseQFrame)
        self.frame_19.setObjectName(u"frame_19")
        self.horizontalLayout_16 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLineEdit = QLineEdit(self.frame_19)
        self.MPassphraseQLineEdit.setObjectName(u"MPassphraseQLineEdit")

        self.horizontalLayout_16.addWidget(self.MPassphraseQLineEdit)

        self.pushButton_2 = QPushButton(self.frame_19)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_16.addWidget(self.pushButton_2)


        self.EPassphraseVLayout_2.addWidget(self.frame_19)


        self.horizontalLayout_12.addWidget(self.MPassphraseQFrame)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.frame_14 = QFrame(self.fromMnemonicQStackedWidget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQFrame = QFrame(self.frame_14)
        self.MLanguageQFrame.setObjectName(u"MLanguageQFrame")
        self.MLanguageVLayout = QVBoxLayout(self.MLanguageQFrame)
        self.MLanguageVLayout.setSpacing(5)
        self.MLanguageVLayout.setObjectName(u"MLanguageVLayout")
        self.MLanguageVLayout.setContentsMargins(0, 0, 0, 0)
        self.MLanguageLabelQWidget = QWidget(self.MLanguageQFrame)
        self.MLanguageLabelQWidget.setObjectName(u"MLanguageLabelQWidget")
        self.MLanguageLabelHLayout = QHBoxLayout(self.MLanguageLabelQWidget)
        self.MLanguageLabelHLayout.setSpacing(15)
        self.MLanguageLabelHLayout.setObjectName(u"MLanguageLabelHLayout")
        self.MLanguageLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQLabel = QLabel(self.MLanguageLabelQWidget)
        self.MLanguageQLabel.setObjectName(u"MLanguageQLabel")

        self.MLanguageLabelHLayout.addWidget(self.MLanguageQLabel)

        self.MLanguageLabelHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MLanguageLabelHLayout.addItem(self.MLanguageLabelHSpacer)


        self.MLanguageVLayout.addWidget(self.MLanguageLabelQWidget)

        self.MLanguageQComboBox = QComboBox(self.MLanguageQFrame)
        self.MLanguageQComboBox.addItem("")
        self.MLanguageQComboBox.addItem("")
        self.MLanguageQComboBox.addItem("")
        self.MLanguageQComboBox.addItem("")
        self.MLanguageQComboBox.addItem("")
        self.MLanguageQComboBox.addItem("")
        self.MLanguageQComboBox.addItem("")
        self.MLanguageQComboBox.addItem("")
        self.MLanguageQComboBox.setObjectName(u"MLanguageQComboBox")

        self.MLanguageVLayout.addWidget(self.MLanguageQComboBox)


        self.horizontalLayout_11.addWidget(self.MLanguageQFrame)

        self.MWordsQFrame = QFrame(self.frame_14)
        self.MWordsQFrame.setObjectName(u"MWordsQFrame")
        self.MStrengthVLayout = QVBoxLayout(self.MWordsQFrame)
        self.MStrengthVLayout.setSpacing(5)
        self.MStrengthVLayout.setObjectName(u"MStrengthVLayout")
        self.MStrengthVLayout.setContentsMargins(0, 0, 0, 0)
        self.MWordsLabelQFrame = QFrame(self.MWordsQFrame)
        self.MWordsLabelQFrame.setObjectName(u"MWordsLabelQFrame")
        self.MStrengthLabelHLayout = QHBoxLayout(self.MWordsLabelQFrame)
        self.MStrengthLabelHLayout.setSpacing(15)
        self.MStrengthLabelHLayout.setObjectName(u"MStrengthLabelHLayout")
        self.MStrengthLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.MWordsQLabel = QLabel(self.MWordsLabelQFrame)
        self.MWordsQLabel.setObjectName(u"MWordsQLabel")

        self.MStrengthLabelHLayout.addWidget(self.MWordsQLabel)

        self.MWordsLabelHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout.addItem(self.MWordsLabelHSpacer)


        self.MStrengthVLayout.addWidget(self.MWordsLabelQFrame)

        self.MWordsQComboBox = QComboBox(self.MWordsQFrame)
        self.MWordsQComboBox.addItem("")
        self.MWordsQComboBox.setObjectName(u"MWordsQComboBox")

        self.MStrengthVLayout.addWidget(self.MWordsQComboBox)


        self.horizontalLayout_11.addWidget(self.MWordsQFrame)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.fromQStackedWidget.addWidget(self.fromMnemonicQStackedWidget)
        self.fromSeedQStackedWidget = QWidget()
        self.fromSeedQStackedWidget.setObjectName(u"fromSeedQStackedWidget")
        self.verticalLayout_9 = QVBoxLayout(self.fromSeedQStackedWidget)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.SeedQFrame = QFrame(self.fromSeedQStackedWidget)
        self.SeedQFrame.setObjectName(u"SeedQFrame")
        self.SeedQFrame.setMinimumSize(QSize(400, 0))
        self.SeedVLayout = QVBoxLayout(self.SeedQFrame)
        self.SeedVLayout.setSpacing(5)
        self.SeedVLayout.setObjectName(u"SeedVLayout")
        self.SeedVLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.SeedQFrame)
        self.frame_20.setObjectName(u"frame_20")
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setSpacing(15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.ClientQFrame_3 = QFrame(self.frame_20)
        self.ClientQFrame_3.setObjectName(u"ClientQFrame_3")
        self.ClientQFrame_3.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_3 = QVBoxLayout(self.ClientQFrame_3)
        self.ClientVLayout_3.setSpacing(5)
        self.ClientVLayout_3.setObjectName(u"ClientVLayout_3")
        self.ClientVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_3 = QFrame(self.ClientQFrame_3)
        self.ClientLabelQFrame_3.setObjectName(u"ClientLabelQFrame_3")
        self.MStrengthLabelHLayout_5 = QHBoxLayout(self.ClientLabelQFrame_3)
        self.MStrengthLabelHLayout_5.setSpacing(15)
        self.MStrengthLabelHLayout_5.setObjectName(u"MStrengthLabelHLayout_5")
        self.MStrengthLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_3 = QLabel(self.ClientLabelQFrame_3)
        self.ClientQLabel_3.setObjectName(u"ClientQLabel_3")

        self.MStrengthLabelHLayout_5.addWidget(self.ClientQLabel_3)

        self.ClientLabelHSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_5.addItem(self.ClientLabelHSpacer_3)


        self.ClientVLayout_3.addWidget(self.ClientLabelQFrame_3)

        self.ClientQComboBox_3 = QComboBox(self.ClientQFrame_3)
        self.ClientQComboBox_3.addItem("")
        self.ClientQComboBox_3.addItem("")
        self.ClientQComboBox_3.addItem("")
        self.ClientQComboBox_3.addItem("")
        self.ClientQComboBox_3.addItem("")
        self.ClientQComboBox_3.addItem("")
        self.ClientQComboBox_3.setObjectName(u"ClientQComboBox_3")

        self.ClientVLayout_3.addWidget(self.ClientQComboBox_3)


        self.horizontalLayout_17.addWidget(self.ClientQFrame_3)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_21)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.SeedLabelQFrame = QFrame(self.frame_21)
        self.SeedLabelQFrame.setObjectName(u"SeedLabelQFrame")
        self.SeedLabelHLayout = QHBoxLayout(self.SeedLabelQFrame)
        self.SeedLabelHLayout.setSpacing(15)
        self.SeedLabelHLayout.setObjectName(u"SeedLabelHLayout")
        self.SeedLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.SeedQLabel = QLabel(self.SeedLabelQFrame)
        self.SeedQLabel.setObjectName(u"SeedQLabel")

        self.SeedLabelHLayout.addWidget(self.SeedQLabel)

        self.SeedLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout.addItem(self.SeedLabelHSpacer)


        self.verticalLayout_16.addWidget(self.SeedLabelQFrame)

        self.SeedQLineEdit = QLineEdit(self.frame_21)
        self.SeedQLineEdit.setObjectName(u"SeedQLineEdit")

        self.verticalLayout_16.addWidget(self.SeedQLineEdit)


        self.horizontalLayout_17.addWidget(self.frame_21)


        self.SeedVLayout.addWidget(self.frame_20)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout.addItem(self.verticalSpacer)


        self.verticalLayout_9.addWidget(self.SeedQFrame)

        self.fromQStackedWidget.addWidget(self.fromSeedQStackedWidget)
        self.fromXPrivateKeyQStackedWidget = QWidget()
        self.fromXPrivateKeyQStackedWidget.setObjectName(u"fromXPrivateKeyQStackedWidget")
        self.verticalLayout_10 = QVBoxLayout(self.fromXPrivateKeyQStackedWidget)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQFrame = QFrame(self.fromXPrivateKeyQStackedWidget)
        self.XPrivateKeyQFrame.setObjectName(u"XPrivateKeyQFrame")
        self.XPrivateKeyVLayout = QVBoxLayout(self.XPrivateKeyQFrame)
        self.XPrivateKeyVLayout.setSpacing(5)
        self.XPrivateKeyVLayout.setObjectName(u"XPrivateKeyVLayout")
        self.XPrivateKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyLabelQFrame = QFrame(self.XPrivateKeyQFrame)
        self.XPrivateKeyLabelQFrame.setObjectName(u"XPrivateKeyLabelQFrame")
        self.XPrivateKeyLabelHLayout = QHBoxLayout(self.XPrivateKeyLabelQFrame)
        self.XPrivateKeyLabelHLayout.setSpacing(15)
        self.XPrivateKeyLabelHLayout.setObjectName(u"XPrivateKeyLabelHLayout")
        self.XPrivateKeyLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQLabel = QLabel(self.XPrivateKeyLabelQFrame)
        self.XPrivateKeyQLabel.setObjectName(u"XPrivateKeyQLabel")

        self.XPrivateKeyLabelHLayout.addWidget(self.XPrivateKeyQLabel)

        self.XPrivateKeyLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPrivateKeyLabelHLayout.addItem(self.XPrivateKeyLabelHSpacer)


        self.XPrivateKeyVLayout.addWidget(self.XPrivateKeyLabelQFrame)

        self.XPrivateKeyQLineEdit = QLineEdit(self.XPrivateKeyQFrame)
        self.XPrivateKeyQLineEdit.setObjectName(u"XPrivateKeyQLineEdit")

        self.XPrivateKeyVLayout.addWidget(self.XPrivateKeyQLineEdit)


        self.verticalLayout_10.addWidget(self.XPrivateKeyQFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.fromQStackedWidget.addWidget(self.fromXPrivateKeyQStackedWidget)
        self.fromXPublicKeyQStackedWidget = QWidget()
        self.fromXPublicKeyQStackedWidget.setObjectName(u"fromXPublicKeyQStackedWidget")
        self.verticalLayout_11 = QVBoxLayout(self.fromXPublicKeyQStackedWidget)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQFrame = QFrame(self.fromXPublicKeyQStackedWidget)
        self.XPublicKeyQFrame.setObjectName(u"XPublicKeyQFrame")
        self.XPublicKeyVLayout = QVBoxLayout(self.XPublicKeyQFrame)
        self.XPublicKeyVLayout.setSpacing(5)
        self.XPublicKeyVLayout.setObjectName(u"XPublicKeyVLayout")
        self.XPublicKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyLabelQFrame = QFrame(self.XPublicKeyQFrame)
        self.XPublicKeyLabelQFrame.setObjectName(u"XPublicKeyLabelQFrame")
        self.XPublicKeyLabelHLayout = QHBoxLayout(self.XPublicKeyLabelQFrame)
        self.XPublicKeyLabelHLayout.setSpacing(15)
        self.XPublicKeyLabelHLayout.setObjectName(u"XPublicKeyLabelHLayout")
        self.XPublicKeyLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQLabel = QLabel(self.XPublicKeyLabelQFrame)
        self.XPublicKeyQLabel.setObjectName(u"XPublicKeyQLabel")

        self.XPublicKeyLabelHLayout.addWidget(self.XPublicKeyQLabel)

        self.XPublicKeyLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPublicKeyLabelHLayout.addItem(self.XPublicKeyLabelHSpacer)


        self.XPublicKeyVLayout.addWidget(self.XPublicKeyLabelQFrame)

        self.XPublicKeyQLineEdit = QLineEdit(self.XPublicKeyQFrame)
        self.XPublicKeyQLineEdit.setObjectName(u"XPublicKeyQLineEdit")

        self.XPublicKeyVLayout.addWidget(self.XPublicKeyQLineEdit)


        self.verticalLayout_11.addWidget(self.XPublicKeyQFrame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.fromQStackedWidget.addWidget(self.fromXPublicKeyQStackedWidget)
        self.fromWIFQStackedWidget = QWidget()
        self.fromWIFQStackedWidget.setObjectName(u"fromWIFQStackedWidget")
        self.verticalLayout_12 = QVBoxLayout(self.fromWIFQStackedWidget)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.WIFQFrame = QFrame(self.fromWIFQStackedWidget)
        self.WIFQFrame.setObjectName(u"WIFQFrame")
        self.WIFQFrame.setMinimumSize(QSize(400, 0))
        self.WIFVLayout = QVBoxLayout(self.WIFQFrame)
        self.WIFVLayout.setSpacing(5)
        self.WIFVLayout.setObjectName(u"WIFVLayout")
        self.WIFVLayout.setContentsMargins(0, 0, 0, 0)
        self.WIFLabelQFrame = QFrame(self.WIFQFrame)
        self.WIFLabelQFrame.setObjectName(u"WIFLabelQFrame")
        self.WIFLabelHLayout = QHBoxLayout(self.WIFLabelQFrame)
        self.WIFLabelHLayout.setSpacing(15)
        self.WIFLabelHLayout.setObjectName(u"WIFLabelHLayout")
        self.WIFLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.WIFQLabel = QLabel(self.WIFLabelQFrame)
        self.WIFQLabel.setObjectName(u"WIFQLabel")

        self.WIFLabelHLayout.addWidget(self.WIFQLabel)

        self.WIFLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WIFLabelHLayout.addItem(self.WIFLabelHSpacer)


        self.WIFVLayout.addWidget(self.WIFLabelQFrame)

        self.WIFQLineEdit = QLineEdit(self.WIFQFrame)
        self.WIFQLineEdit.setObjectName(u"WIFQLineEdit")

        self.WIFVLayout.addWidget(self.WIFQLineEdit)


        self.verticalLayout_12.addWidget(self.WIFQFrame)

        self.frame_17 = QFrame(self.fromWIFQStackedWidget)
        self.frame_17.setObjectName(u"frame_17")
        self.verticalLayout_15 = QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFPassphraseLabelQFrame = QFrame(self.frame_17)
        self.BIP38EncryptedWIFPassphraseLabelQFrame.setObjectName(u"BIP38EncryptedWIFPassphraseLabelQFrame")
        self.EPassphraseLabelHLayout_2 = QHBoxLayout(self.BIP38EncryptedWIFPassphraseLabelQFrame)
        self.EPassphraseLabelHLayout_2.setSpacing(15)
        self.EPassphraseLabelHLayout_2.setObjectName(u"EPassphraseLabelHLayout_2")
        self.EPassphraseLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFQCheckBox = QCheckBox(self.BIP38EncryptedWIFPassphraseLabelQFrame)
        self.BIP38EncryptedWIFQCheckBox.setObjectName(u"BIP38EncryptedWIFQCheckBox")

        self.EPassphraseLabelHLayout_2.addWidget(self.BIP38EncryptedWIFQCheckBox)

        self.BIP38EncryptedWIFPassphraseLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_2.addItem(self.BIP38EncryptedWIFPassphraseLabelHSpacer)


        self.verticalLayout_15.addWidget(self.BIP38EncryptedWIFPassphraseLabelQFrame)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.BIP38PassphraseQLineEdit = QLineEdit(self.frame_18)
        self.BIP38PassphraseQLineEdit.setObjectName(u"BIP38PassphraseQLineEdit")

        self.horizontalLayout_14.addWidget(self.BIP38PassphraseQLineEdit)

        self.pushButton_3 = QPushButton(self.frame_18)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_14.addWidget(self.pushButton_3)


        self.verticalLayout_15.addWidget(self.frame_18)


        self.verticalLayout_12.addWidget(self.frame_17)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.fromQStackedWidget.addWidget(self.fromWIFQStackedWidget)
        self.fromPrivateKeyQStackedWidget = QWidget()
        self.fromPrivateKeyQStackedWidget.setObjectName(u"fromPrivateKeyQStackedWidget")
        self.verticalLayout_13 = QVBoxLayout(self.fromPrivateKeyQStackedWidget)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQFrame = QFrame(self.fromPrivateKeyQStackedWidget)
        self.PrivateKeyQFrame.setObjectName(u"PrivateKeyQFrame")
        self.PrivateKeyQFrame.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout = QVBoxLayout(self.PrivateKeyQFrame)
        self.PrivateKeyVLayout.setSpacing(5)
        self.PrivateKeyVLayout.setObjectName(u"PrivateKeyVLayout")
        self.PrivateKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyLabelQFrame = QFrame(self.PrivateKeyQFrame)
        self.PrivateKeyLabelQFrame.setObjectName(u"PrivateKeyLabelQFrame")
        self.PrivateKeyLabelHLayout = QHBoxLayout(self.PrivateKeyLabelQFrame)
        self.PrivateKeyLabelHLayout.setSpacing(15)
        self.PrivateKeyLabelHLayout.setObjectName(u"PrivateKeyLabelHLayout")
        self.PrivateKeyLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQLabel = QLabel(self.PrivateKeyLabelQFrame)
        self.PrivateKeyQLabel.setObjectName(u"PrivateKeyQLabel")

        self.PrivateKeyLabelHLayout.addWidget(self.PrivateKeyQLabel)

        self.PrivateKeyLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout.addItem(self.PrivateKeyLabelHSpacer)


        self.PrivateKeyVLayout.addWidget(self.PrivateKeyLabelQFrame)

        self.PrivateKeyQLineEdit = QLineEdit(self.PrivateKeyQFrame)
        self.PrivateKeyQLineEdit.setObjectName(u"PrivateKeyQLineEdit")

        self.PrivateKeyVLayout.addWidget(self.PrivateKeyQLineEdit)


        self.verticalLayout_13.addWidget(self.PrivateKeyQFrame)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.fromQStackedWidget.addWidget(self.fromPrivateKeyQStackedWidget)
        self.fromPublicKeyQStackedWidget = QWidget()
        self.fromPublicKeyQStackedWidget.setObjectName(u"fromPublicKeyQStackedWidget")
        self.verticalLayout_14 = QVBoxLayout(self.fromPublicKeyQStackedWidget)
        self.verticalLayout_14.setSpacing(15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQFrame = QFrame(self.fromPublicKeyQStackedWidget)
        self.PublicKeyQFrame.setObjectName(u"PublicKeyQFrame")
        self.PublicKeyVLayout = QVBoxLayout(self.PublicKeyQFrame)
        self.PublicKeyVLayout.setSpacing(5)
        self.PublicKeyVLayout.setObjectName(u"PublicKeyVLayout")
        self.PublicKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyLabelQFrame = QFrame(self.PublicKeyQFrame)
        self.PublicKeyLabelQFrame.setObjectName(u"PublicKeyLabelQFrame")
        self.PublicKeyLabelHLayout = QHBoxLayout(self.PublicKeyLabelQFrame)
        self.PublicKeyLabelHLayout.setSpacing(15)
        self.PublicKeyLabelHLayout.setObjectName(u"PublicKeyLabelHLayout")
        self.PublicKeyLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQLabel = QLabel(self.PublicKeyLabelQFrame)
        self.PublicKeyQLabel.setObjectName(u"PublicKeyQLabel")

        self.PublicKeyLabelHLayout.addWidget(self.PublicKeyQLabel)

        self.PublicKeyLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PublicKeyLabelHLayout.addItem(self.PublicKeyLabelHSpacer)


        self.PublicKeyVLayout.addWidget(self.PublicKeyLabelQFrame)

        self.PublicKeyQLineEdit = QLineEdit(self.PublicKeyQFrame)
        self.PublicKeyQLineEdit.setObjectName(u"PublicKeyQLineEdit")

        self.PublicKeyVLayout.addWidget(self.PublicKeyQLineEdit)


        self.verticalLayout_14.addWidget(self.PublicKeyQFrame)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.fromQStackedWidget.addWidget(self.fromPublicKeyQStackedWidget)

        self.verticalLayout_69.addWidget(self.fromQStackedWidget)

        self.stackedWidget.addWidget(self.Monero)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setSpacing(15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.DerivationQFrame = QFrame(self.frame_5)
        self.DerivationQFrame.setObjectName(u"DerivationQFrame")
        self.DerivationVLayout = QVBoxLayout(self.DerivationQFrame)
        self.DerivationVLayout.setSpacing(5)
        self.DerivationVLayout.setObjectName(u"DerivationVLayout")
        self.DerivationVLayout.setContentsMargins(0, 0, 0, 0)
        self.DerivationLabelQFrame = QFrame(self.DerivationQFrame)
        self.DerivationLabelQFrame.setObjectName(u"DerivationLabelQFrame")
        self.DerivationLabelHLayout = QHBoxLayout(self.DerivationLabelQFrame)
        self.DerivationLabelHLayout.setSpacing(15)
        self.DerivationLabelHLayout.setObjectName(u"DerivationLabelHLayout")
        self.DerivationLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.DerivationQLabel = QLabel(self.DerivationLabelQFrame)
        self.DerivationQLabel.setObjectName(u"DerivationQLabel")

        self.DerivationLabelHLayout.addWidget(self.DerivationQLabel)

        self.DerivationLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.DerivationLabelHLayout.addItem(self.DerivationLabelHSpacer)


        self.DerivationVLayout.addWidget(self.DerivationLabelQFrame)

        self.DerivationsQTabWidget = QTabWidget(self.DerivationQFrame)
        self.DerivationsQTabWidget.setObjectName(u"DerivationsQTabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DerivationsQTabWidget.sizePolicy().hasHeightForWidth())
        self.DerivationsQTabWidget.setSizePolicy(sizePolicy2)
        self.CustomQWidget = QWidget()
        self.CustomQWidget.setObjectName(u"CustomQWidget")
        self.BIP32HLayout = QHBoxLayout(self.CustomQWidget)
        self.BIP32HLayout.setSpacing(15)
        self.BIP32HLayout.setObjectName(u"BIP32HLayout")
        self.BIP32HLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomPathQFrame = QFrame(self.CustomQWidget)
        self.CustomPathQFrame.setObjectName(u"CustomPathQFrame")
        self.BIP32DerivationPathVLayout = QVBoxLayout(self.CustomPathQFrame)
        self.BIP32DerivationPathVLayout.setSpacing(5)
        self.BIP32DerivationPathVLayout.setObjectName(u"BIP32DerivationPathVLayout")
        self.BIP32DerivationPathVLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomPathLabelQFrame = QFrame(self.CustomPathQFrame)
        self.CustomPathLabelQFrame.setObjectName(u"CustomPathLabelQFrame")
        self.BIP32DerivationPathLabelHLayout = QHBoxLayout(self.CustomPathLabelQFrame)
        self.BIP32DerivationPathLabelHLayout.setSpacing(15)
        self.BIP32DerivationPathLabelHLayout.setObjectName(u"BIP32DerivationPathLabelHLayout")
        self.BIP32DerivationPathLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomPathQLabel = QLabel(self.CustomPathLabelQFrame)
        self.CustomPathQLabel.setObjectName(u"CustomPathQLabel")

        self.BIP32DerivationPathLabelHLayout.addWidget(self.CustomPathQLabel)

        self.CustomPathLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP32DerivationPathLabelHLayout.addItem(self.CustomPathLabelHSpacer)


        self.BIP32DerivationPathVLayout.addWidget(self.CustomPathLabelQFrame)

        self.CustomPathQLineEdit = QLineEdit(self.CustomPathQFrame)
        self.CustomPathQLineEdit.setObjectName(u"CustomPathQLineEdit")

        self.BIP32DerivationPathVLayout.addWidget(self.CustomPathQLineEdit)


        self.BIP32HLayout.addWidget(self.CustomPathQFrame)

        self.CustomClientQFrame = QFrame(self.CustomQWidget)
        self.CustomClientQFrame.setObjectName(u"CustomClientQFrame")
        self.CustomClientQFrame.setMinimumSize(QSize(175, 0))
        self.CustomClientQFrame.setMaximumSize(QSize(300, 16777215))
        self.BIP32ClientVLayout = QVBoxLayout(self.CustomClientQFrame)
        self.BIP32ClientVLayout.setSpacing(5)
        self.BIP32ClientVLayout.setObjectName(u"BIP32ClientVLayout")
        self.BIP32ClientVLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomClientLabelQFrame = QFrame(self.CustomClientQFrame)
        self.CustomClientLabelQFrame.setObjectName(u"CustomClientLabelQFrame")
        self.BIP32ClientLabelHLayout = QHBoxLayout(self.CustomClientLabelQFrame)
        self.BIP32ClientLabelHLayout.setSpacing(15)
        self.BIP32ClientLabelHLayout.setObjectName(u"BIP32ClientLabelHLayout")
        self.BIP32ClientLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomClientQLabel = QLabel(self.CustomClientLabelQFrame)
        self.CustomClientQLabel.setObjectName(u"CustomClientQLabel")

        self.BIP32ClientLabelHLayout.addWidget(self.CustomClientQLabel)

        self.CustomClientLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP32ClientLabelHLayout.addItem(self.CustomClientLabelHSpacer)


        self.BIP32ClientVLayout.addWidget(self.CustomClientLabelQFrame)

        self.CustomClientQComboBox = QComboBox(self.CustomClientQFrame)
        self.CustomClientQComboBox.addItem("")
        self.CustomClientQComboBox.addItem("")
        self.CustomClientQComboBox.addItem("")
        self.CustomClientQComboBox.addItem("")
        self.CustomClientQComboBox.addItem("")
        self.CustomClientQComboBox.setObjectName(u"CustomClientQComboBox")

        self.BIP32ClientVLayout.addWidget(self.CustomClientQComboBox)


        self.BIP32HLayout.addWidget(self.CustomClientQFrame)

        self.DerivationsQTabWidget.addTab(self.CustomQWidget, "")
        self.BIP44QWidget = QWidget()
        self.BIP44QWidget.setObjectName(u"BIP44QWidget")
        self.BIP44HLayout = QHBoxLayout(self.BIP44QWidget)
        self.BIP44HLayout.setSpacing(15)
        self.BIP44HLayout.setObjectName(u"BIP44HLayout")
        self.BIP44HLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44PurposeQFrame = QFrame(self.BIP44QWidget)
        self.BIP44PurposeQFrame.setObjectName(u"BIP44PurposeQFrame")
        self.BIP44PurposeVLayout = QVBoxLayout(self.BIP44PurposeQFrame)
        self.BIP44PurposeVLayout.setSpacing(5)
        self.BIP44PurposeVLayout.setObjectName(u"BIP44PurposeVLayout")
        self.BIP44PurposeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44PurposeLabelQFrame = QFrame(self.BIP44PurposeQFrame)
        self.BIP44PurposeLabelQFrame.setObjectName(u"BIP44PurposeLabelQFrame")
        self.BIP44PurposeLabelHLayout = QHBoxLayout(self.BIP44PurposeLabelQFrame)
        self.BIP44PurposeLabelHLayout.setSpacing(5)
        self.BIP44PurposeLabelHLayout.setObjectName(u"BIP44PurposeLabelHLayout")
        self.BIP44PurposeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44PurposeQLabel = QLabel(self.BIP44PurposeLabelQFrame)
        self.BIP44PurposeQLabel.setObjectName(u"BIP44PurposeQLabel")

        self.BIP44PurposeLabelHLayout.addWidget(self.BIP44PurposeQLabel)

        self.BIP44PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44PurposeLabelHLayout.addItem(self.BIP44PurposeLabelHSpacer)


        self.BIP44PurposeVLayout.addWidget(self.BIP44PurposeLabelQFrame)

        self.BIP44PurposeQLineEdit = QLineEdit(self.BIP44PurposeQFrame)
        self.BIP44PurposeQLineEdit.setObjectName(u"BIP44PurposeQLineEdit")
        self.BIP44PurposeQLineEdit.setEnabled(False)

        self.BIP44PurposeVLayout.addWidget(self.BIP44PurposeQLineEdit)


        self.BIP44HLayout.addWidget(self.BIP44PurposeQFrame)

        self.BIP44CoinTypeQFrame = QFrame(self.BIP44QWidget)
        self.BIP44CoinTypeQFrame.setObjectName(u"BIP44CoinTypeQFrame")
        self.BIP44CoinTypeVLayout = QVBoxLayout(self.BIP44CoinTypeQFrame)
        self.BIP44CoinTypeVLayout.setSpacing(5)
        self.BIP44CoinTypeVLayout.setObjectName(u"BIP44CoinTypeVLayout")
        self.BIP44CoinTypeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44CoinTypeLabelQFrame = QFrame(self.BIP44CoinTypeQFrame)
        self.BIP44CoinTypeLabelQFrame.setObjectName(u"BIP44CoinTypeLabelQFrame")
        self.BIP44CoinTypeLabelHLayout = QHBoxLayout(self.BIP44CoinTypeLabelQFrame)
        self.BIP44CoinTypeLabelHLayout.setSpacing(5)
        self.BIP44CoinTypeLabelHLayout.setObjectName(u"BIP44CoinTypeLabelHLayout")
        self.BIP44CoinTypeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44CoinTypeQLabel = QLabel(self.BIP44CoinTypeLabelQFrame)
        self.BIP44CoinTypeQLabel.setObjectName(u"BIP44CoinTypeQLabel")

        self.BIP44CoinTypeLabelHLayout.addWidget(self.BIP44CoinTypeQLabel)

        self.BIP44CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44CoinTypeLabelHLayout.addItem(self.BIP44CoinTypeLabelHSpacer)


        self.BIP44CoinTypeVLayout.addWidget(self.BIP44CoinTypeLabelQFrame)

        self.BIP44CoinTypeQLineEdit = QLineEdit(self.BIP44CoinTypeQFrame)
        self.BIP44CoinTypeQLineEdit.setObjectName(u"BIP44CoinTypeQLineEdit")
        self.BIP44CoinTypeQLineEdit.setEnabled(False)

        self.BIP44CoinTypeVLayout.addWidget(self.BIP44CoinTypeQLineEdit)


        self.BIP44HLayout.addWidget(self.BIP44CoinTypeQFrame)

        self.BIP44AccountQFrame = QFrame(self.BIP44QWidget)
        self.BIP44AccountQFrame.setObjectName(u"BIP44AccountQFrame")
        self.BIP44AccountVLayout = QVBoxLayout(self.BIP44AccountQFrame)
        self.BIP44AccountVLayout.setSpacing(5)
        self.BIP44AccountVLayout.setObjectName(u"BIP44AccountVLayout")
        self.BIP44AccountVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44AccountLabelQFrame = QFrame(self.BIP44AccountQFrame)
        self.BIP44AccountLabelQFrame.setObjectName(u"BIP44AccountLabelQFrame")
        self.BIP44AccountLabelHLayout = QHBoxLayout(self.BIP44AccountLabelQFrame)
        self.BIP44AccountLabelHLayout.setSpacing(5)
        self.BIP44AccountLabelHLayout.setObjectName(u"BIP44AccountLabelHLayout")
        self.BIP44AccountLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44AccountQLabel = QLabel(self.BIP44AccountLabelQFrame)
        self.BIP44AccountQLabel.setObjectName(u"BIP44AccountQLabel")

        self.BIP44AccountLabelHLayout.addWidget(self.BIP44AccountQLabel)

        self.BIP44AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AccountLabelHLayout.addItem(self.BIP44AccountLabelHSpacer)


        self.BIP44AccountVLayout.addWidget(self.BIP44AccountLabelQFrame)

        self.BIP44AccountQLineEdit = QLineEdit(self.BIP44AccountQFrame)
        self.BIP44AccountQLineEdit.setObjectName(u"BIP44AccountQLineEdit")

        self.BIP44AccountVLayout.addWidget(self.BIP44AccountQLineEdit)


        self.BIP44HLayout.addWidget(self.BIP44AccountQFrame)

        self.BIP44ChangeQFrame = QFrame(self.BIP44QWidget)
        self.BIP44ChangeQFrame.setObjectName(u"BIP44ChangeQFrame")
        self.BIP44ChangeVLayout = QVBoxLayout(self.BIP44ChangeQFrame)
        self.BIP44ChangeVLayout.setSpacing(5)
        self.BIP44ChangeVLayout.setObjectName(u"BIP44ChangeVLayout")
        self.BIP44ChangeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44ChangeLabelQFrame = QFrame(self.BIP44ChangeQFrame)
        self.BIP44ChangeLabelQFrame.setObjectName(u"BIP44ChangeLabelQFrame")
        self.BIP44ChangeLabelHLayout = QHBoxLayout(self.BIP44ChangeLabelQFrame)
        self.BIP44ChangeLabelHLayout.setSpacing(5)
        self.BIP44ChangeLabelHLayout.setObjectName(u"BIP44ChangeLabelHLayout")
        self.BIP44ChangeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44ChangeQLabel = QLabel(self.BIP44ChangeLabelQFrame)
        self.BIP44ChangeQLabel.setObjectName(u"BIP44ChangeQLabel")

        self.BIP44ChangeLabelHLayout.addWidget(self.BIP44ChangeQLabel)

        self.BIP44ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44ChangeLabelHLayout.addItem(self.BIP44ChangeLabelHSpacer)


        self.BIP44ChangeVLayout.addWidget(self.BIP44ChangeLabelQFrame)

        self.BIP44ChangeQComboBox = QComboBox(self.BIP44ChangeQFrame)
        self.BIP44ChangeQComboBox.addItem("")
        self.BIP44ChangeQComboBox.addItem("")
        self.BIP44ChangeQComboBox.setObjectName(u"BIP44ChangeQComboBox")

        self.BIP44ChangeVLayout.addWidget(self.BIP44ChangeQComboBox)


        self.BIP44HLayout.addWidget(self.BIP44ChangeQFrame)

        self.BIP44AddressQFrame = QFrame(self.BIP44QWidget)
        self.BIP44AddressQFrame.setObjectName(u"BIP44AddressQFrame")
        self.BIP44AddressVLayout = QVBoxLayout(self.BIP44AddressQFrame)
        self.BIP44AddressVLayout.setSpacing(5)
        self.BIP44AddressVLayout.setObjectName(u"BIP44AddressVLayout")
        self.BIP44AddressVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44AddressLabelQFrame = QFrame(self.BIP44AddressQFrame)
        self.BIP44AddressLabelQFrame.setObjectName(u"BIP44AddressLabelQFrame")
        self.BIP44AddressLabelHLayout = QHBoxLayout(self.BIP44AddressLabelQFrame)
        self.BIP44AddressLabelHLayout.setSpacing(5)
        self.BIP44AddressLabelHLayout.setObjectName(u"BIP44AddressLabelHLayout")
        self.BIP44AddressLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44AddressQLabel = QLabel(self.BIP44AddressLabelQFrame)
        self.BIP44AddressQLabel.setObjectName(u"BIP44AddressQLabel")

        self.BIP44AddressLabelHLayout.addWidget(self.BIP44AddressQLabel)

        self.BIP44AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AddressLabelHLayout.addItem(self.BIP44AddressLabelHSpacer)


        self.BIP44AddressVLayout.addWidget(self.BIP44AddressLabelQFrame)

        self.BIP44AddressQLineEdit = QLineEdit(self.BIP44AddressQFrame)
        self.BIP44AddressQLineEdit.setObjectName(u"BIP44AddressQLineEdit")

        self.BIP44AddressVLayout.addWidget(self.BIP44AddressQLineEdit)


        self.BIP44HLayout.addWidget(self.BIP44AddressQFrame)

        self.DerivationsQTabWidget.addTab(self.BIP44QWidget, "")
        self.BIP49QWidget = QWidget()
        self.BIP49QWidget.setObjectName(u"BIP49QWidget")
        self.BIP49HLayout = QHBoxLayout(self.BIP49QWidget)
        self.BIP49HLayout.setSpacing(15)
        self.BIP49HLayout.setObjectName(u"BIP49HLayout")
        self.BIP49HLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49PurposeQFrame = QFrame(self.BIP49QWidget)
        self.BIP49PurposeQFrame.setObjectName(u"BIP49PurposeQFrame")
        self.BIP49PurposeVLayout = QVBoxLayout(self.BIP49PurposeQFrame)
        self.BIP49PurposeVLayout.setSpacing(5)
        self.BIP49PurposeVLayout.setObjectName(u"BIP49PurposeVLayout")
        self.BIP49PurposeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49PurposeLabelQFrame = QFrame(self.BIP49PurposeQFrame)
        self.BIP49PurposeLabelQFrame.setObjectName(u"BIP49PurposeLabelQFrame")
        self.BIP49PurposeLabelHLayout = QHBoxLayout(self.BIP49PurposeLabelQFrame)
        self.BIP49PurposeLabelHLayout.setSpacing(5)
        self.BIP49PurposeLabelHLayout.setObjectName(u"BIP49PurposeLabelHLayout")
        self.BIP49PurposeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49PurposeQLabel = QLabel(self.BIP49PurposeLabelQFrame)
        self.BIP49PurposeQLabel.setObjectName(u"BIP49PurposeQLabel")

        self.BIP49PurposeLabelHLayout.addWidget(self.BIP49PurposeQLabel)

        self.BIP49PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP49PurposeLabelHLayout.addItem(self.BIP49PurposeLabelHSpacer)


        self.BIP49PurposeVLayout.addWidget(self.BIP49PurposeLabelQFrame)

        self.BIP49PurposeQLineEdit = QLineEdit(self.BIP49PurposeQFrame)
        self.BIP49PurposeQLineEdit.setObjectName(u"BIP49PurposeQLineEdit")
        self.BIP49PurposeQLineEdit.setEnabled(False)

        self.BIP49PurposeVLayout.addWidget(self.BIP49PurposeQLineEdit)


        self.BIP49HLayout.addWidget(self.BIP49PurposeQFrame)

        self.BIP49CoinTypeQFrame = QFrame(self.BIP49QWidget)
        self.BIP49CoinTypeQFrame.setObjectName(u"BIP49CoinTypeQFrame")
        self.BIP49CoinTypeVLayout = QVBoxLayout(self.BIP49CoinTypeQFrame)
        self.BIP49CoinTypeVLayout.setSpacing(5)
        self.BIP49CoinTypeVLayout.setObjectName(u"BIP49CoinTypeVLayout")
        self.BIP49CoinTypeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49CoinTypeLabelQFrame = QFrame(self.BIP49CoinTypeQFrame)
        self.BIP49CoinTypeLabelQFrame.setObjectName(u"BIP49CoinTypeLabelQFrame")
        self.BIP49CoinTypeLabelHLayout = QHBoxLayout(self.BIP49CoinTypeLabelQFrame)
        self.BIP49CoinTypeLabelHLayout.setSpacing(5)
        self.BIP49CoinTypeLabelHLayout.setObjectName(u"BIP49CoinTypeLabelHLayout")
        self.BIP49CoinTypeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49CoinTypeQLabel = QLabel(self.BIP49CoinTypeLabelQFrame)
        self.BIP49CoinTypeQLabel.setObjectName(u"BIP49CoinTypeQLabel")

        self.BIP49CoinTypeLabelHLayout.addWidget(self.BIP49CoinTypeQLabel)

        self.BIP49CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP49CoinTypeLabelHLayout.addItem(self.BIP49CoinTypeLabelHSpacer)


        self.BIP49CoinTypeVLayout.addWidget(self.BIP49CoinTypeLabelQFrame)

        self.BIP49CoinTypeQLineEdit = QLineEdit(self.BIP49CoinTypeQFrame)
        self.BIP49CoinTypeQLineEdit.setObjectName(u"BIP49CoinTypeQLineEdit")
        self.BIP49CoinTypeQLineEdit.setEnabled(False)

        self.BIP49CoinTypeVLayout.addWidget(self.BIP49CoinTypeQLineEdit)


        self.BIP49HLayout.addWidget(self.BIP49CoinTypeQFrame)

        self.BIP49AccountQFrame = QFrame(self.BIP49QWidget)
        self.BIP49AccountQFrame.setObjectName(u"BIP49AccountQFrame")
        self.BIP49AccountVLayout = QVBoxLayout(self.BIP49AccountQFrame)
        self.BIP49AccountVLayout.setSpacing(5)
        self.BIP49AccountVLayout.setObjectName(u"BIP49AccountVLayout")
        self.BIP49AccountVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49AccountLabelQFrame = QFrame(self.BIP49AccountQFrame)
        self.BIP49AccountLabelQFrame.setObjectName(u"BIP49AccountLabelQFrame")
        self.BIP49AccountLabelHLayout = QHBoxLayout(self.BIP49AccountLabelQFrame)
        self.BIP49AccountLabelHLayout.setSpacing(5)
        self.BIP49AccountLabelHLayout.setObjectName(u"BIP49AccountLabelHLayout")
        self.BIP49AccountLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49AccountQLabel = QLabel(self.BIP49AccountLabelQFrame)
        self.BIP49AccountQLabel.setObjectName(u"BIP49AccountQLabel")

        self.BIP49AccountLabelHLayout.addWidget(self.BIP49AccountQLabel)

        self.BIP49AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP49AccountLabelHLayout.addItem(self.BIP49AccountLabelHSpacer)


        self.BIP49AccountVLayout.addWidget(self.BIP49AccountLabelQFrame)

        self.BIP49AccountQLineEdit = QLineEdit(self.BIP49AccountQFrame)
        self.BIP49AccountQLineEdit.setObjectName(u"BIP49AccountQLineEdit")

        self.BIP49AccountVLayout.addWidget(self.BIP49AccountQLineEdit)


        self.BIP49HLayout.addWidget(self.BIP49AccountQFrame)

        self.BIP49ChangeQFrame = QFrame(self.BIP49QWidget)
        self.BIP49ChangeQFrame.setObjectName(u"BIP49ChangeQFrame")
        self.BIP49ChangeVLayout = QVBoxLayout(self.BIP49ChangeQFrame)
        self.BIP49ChangeVLayout.setSpacing(5)
        self.BIP49ChangeVLayout.setObjectName(u"BIP49ChangeVLayout")
        self.BIP49ChangeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49ChangeLabelQFrame = QFrame(self.BIP49ChangeQFrame)
        self.BIP49ChangeLabelQFrame.setObjectName(u"BIP49ChangeLabelQFrame")
        self.BIP49ChangeLabelHLayout = QHBoxLayout(self.BIP49ChangeLabelQFrame)
        self.BIP49ChangeLabelHLayout.setSpacing(5)
        self.BIP49ChangeLabelHLayout.setObjectName(u"BIP49ChangeLabelHLayout")
        self.BIP49ChangeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49ChangeQLabel = QLabel(self.BIP49ChangeLabelQFrame)
        self.BIP49ChangeQLabel.setObjectName(u"BIP49ChangeQLabel")

        self.BIP49ChangeLabelHLayout.addWidget(self.BIP49ChangeQLabel)

        self.BIP49ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP49ChangeLabelHLayout.addItem(self.BIP49ChangeLabelHSpacer)


        self.BIP49ChangeVLayout.addWidget(self.BIP49ChangeLabelQFrame)

        self.BIP49ChangeQComboBox = QComboBox(self.BIP49ChangeQFrame)
        self.BIP49ChangeQComboBox.addItem("")
        self.BIP49ChangeQComboBox.addItem("")
        self.BIP49ChangeQComboBox.setObjectName(u"BIP49ChangeQComboBox")

        self.BIP49ChangeVLayout.addWidget(self.BIP49ChangeQComboBox)


        self.BIP49HLayout.addWidget(self.BIP49ChangeQFrame)

        self.BIP49AddressQFrame = QFrame(self.BIP49QWidget)
        self.BIP49AddressQFrame.setObjectName(u"BIP49AddressQFrame")
        self.BIP49AddressVLayout = QVBoxLayout(self.BIP49AddressQFrame)
        self.BIP49AddressVLayout.setSpacing(5)
        self.BIP49AddressVLayout.setObjectName(u"BIP49AddressVLayout")
        self.BIP49AddressVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49AddressLabelQFrame = QFrame(self.BIP49AddressQFrame)
        self.BIP49AddressLabelQFrame.setObjectName(u"BIP49AddressLabelQFrame")
        self.BIP49AddressLabelHLayout = QHBoxLayout(self.BIP49AddressLabelQFrame)
        self.BIP49AddressLabelHLayout.setSpacing(5)
        self.BIP49AddressLabelHLayout.setObjectName(u"BIP49AddressLabelHLayout")
        self.BIP49AddressLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49AddressQLabel = QLabel(self.BIP49AddressLabelQFrame)
        self.BIP49AddressQLabel.setObjectName(u"BIP49AddressQLabel")

        self.BIP49AddressLabelHLayout.addWidget(self.BIP49AddressQLabel)

        self.BIP49AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP49AddressLabelHLayout.addItem(self.BIP49AddressLabelHSpacer)


        self.BIP49AddressVLayout.addWidget(self.BIP49AddressLabelQFrame)

        self.BIP49AddressQLineEdit = QLineEdit(self.BIP49AddressQFrame)
        self.BIP49AddressQLineEdit.setObjectName(u"BIP49AddressQLineEdit")

        self.BIP49AddressVLayout.addWidget(self.BIP49AddressQLineEdit)


        self.BIP49HLayout.addWidget(self.BIP49AddressQFrame)

        self.DerivationsQTabWidget.addTab(self.BIP49QWidget, "")
        self.BIP84QWidget = QWidget()
        self.BIP84QWidget.setObjectName(u"BIP84QWidget")
        self.BIP84HLayout = QHBoxLayout(self.BIP84QWidget)
        self.BIP84HLayout.setSpacing(15)
        self.BIP84HLayout.setObjectName(u"BIP84HLayout")
        self.BIP84HLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84PurposeQFrame = QFrame(self.BIP84QWidget)
        self.BIP84PurposeQFrame.setObjectName(u"BIP84PurposeQFrame")
        self.BIP84PurposeVLayout = QVBoxLayout(self.BIP84PurposeQFrame)
        self.BIP84PurposeVLayout.setSpacing(5)
        self.BIP84PurposeVLayout.setObjectName(u"BIP84PurposeVLayout")
        self.BIP84PurposeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84PurposeLabelQFrame = QFrame(self.BIP84PurposeQFrame)
        self.BIP84PurposeLabelQFrame.setObjectName(u"BIP84PurposeLabelQFrame")
        self.BIP84PurposeLabelHLayout = QHBoxLayout(self.BIP84PurposeLabelQFrame)
        self.BIP84PurposeLabelHLayout.setSpacing(5)
        self.BIP84PurposeLabelHLayout.setObjectName(u"BIP84PurposeLabelHLayout")
        self.BIP84PurposeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84PurposeQLabel = QLabel(self.BIP84PurposeLabelQFrame)
        self.BIP84PurposeQLabel.setObjectName(u"BIP84PurposeQLabel")

        self.BIP84PurposeLabelHLayout.addWidget(self.BIP84PurposeQLabel)

        self.BIP84PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84PurposeLabelHLayout.addItem(self.BIP84PurposeLabelHSpacer)


        self.BIP84PurposeVLayout.addWidget(self.BIP84PurposeLabelQFrame)

        self.BIP84PurposeQLineEdit = QLineEdit(self.BIP84PurposeQFrame)
        self.BIP84PurposeQLineEdit.setObjectName(u"BIP84PurposeQLineEdit")
        self.BIP84PurposeQLineEdit.setEnabled(False)

        self.BIP84PurposeVLayout.addWidget(self.BIP84PurposeQLineEdit)


        self.BIP84HLayout.addWidget(self.BIP84PurposeQFrame)

        self.BIP84CoinTypeQFrame = QFrame(self.BIP84QWidget)
        self.BIP84CoinTypeQFrame.setObjectName(u"BIP84CoinTypeQFrame")
        self.BIP84CoinTypeVLayout = QVBoxLayout(self.BIP84CoinTypeQFrame)
        self.BIP84CoinTypeVLayout.setSpacing(5)
        self.BIP84CoinTypeVLayout.setObjectName(u"BIP84CoinTypeVLayout")
        self.BIP84CoinTypeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84CoinTypeLabelQFrame = QFrame(self.BIP84CoinTypeQFrame)
        self.BIP84CoinTypeLabelQFrame.setObjectName(u"BIP84CoinTypeLabelQFrame")
        self.BIP84CoinTypeLabelHLayout = QHBoxLayout(self.BIP84CoinTypeLabelQFrame)
        self.BIP84CoinTypeLabelHLayout.setSpacing(5)
        self.BIP84CoinTypeLabelHLayout.setObjectName(u"BIP84CoinTypeLabelHLayout")
        self.BIP84CoinTypeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84CoinTypeQLabel = QLabel(self.BIP84CoinTypeLabelQFrame)
        self.BIP84CoinTypeQLabel.setObjectName(u"BIP84CoinTypeQLabel")

        self.BIP84CoinTypeLabelHLayout.addWidget(self.BIP84CoinTypeQLabel)

        self.BIP84CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84CoinTypeLabelHLayout.addItem(self.BIP84CoinTypeLabelHSpacer)


        self.BIP84CoinTypeVLayout.addWidget(self.BIP84CoinTypeLabelQFrame)

        self.BIP84CoinTypeQLineEdit = QLineEdit(self.BIP84CoinTypeQFrame)
        self.BIP84CoinTypeQLineEdit.setObjectName(u"BIP84CoinTypeQLineEdit")
        self.BIP84CoinTypeQLineEdit.setEnabled(False)

        self.BIP84CoinTypeVLayout.addWidget(self.BIP84CoinTypeQLineEdit)


        self.BIP84HLayout.addWidget(self.BIP84CoinTypeQFrame)

        self.BIP84AccountQFrame = QFrame(self.BIP84QWidget)
        self.BIP84AccountQFrame.setObjectName(u"BIP84AccountQFrame")
        self.BIP84AccountVLayout = QVBoxLayout(self.BIP84AccountQFrame)
        self.BIP84AccountVLayout.setSpacing(5)
        self.BIP84AccountVLayout.setObjectName(u"BIP84AccountVLayout")
        self.BIP84AccountVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84AccountLabelQFrame = QFrame(self.BIP84AccountQFrame)
        self.BIP84AccountLabelQFrame.setObjectName(u"BIP84AccountLabelQFrame")
        self.BIP84AccountLabelHLayout = QHBoxLayout(self.BIP84AccountLabelQFrame)
        self.BIP84AccountLabelHLayout.setSpacing(5)
        self.BIP84AccountLabelHLayout.setObjectName(u"BIP84AccountLabelHLayout")
        self.BIP84AccountLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84AccountQLabel = QLabel(self.BIP84AccountLabelQFrame)
        self.BIP84AccountQLabel.setObjectName(u"BIP84AccountQLabel")

        self.BIP84AccountLabelHLayout.addWidget(self.BIP84AccountQLabel)

        self.BIP84AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84AccountLabelHLayout.addItem(self.BIP84AccountLabelHSpacer)


        self.BIP84AccountVLayout.addWidget(self.BIP84AccountLabelQFrame)

        self.BIP84AccountQLineEdit = QLineEdit(self.BIP84AccountQFrame)
        self.BIP84AccountQLineEdit.setObjectName(u"BIP84AccountQLineEdit")

        self.BIP84AccountVLayout.addWidget(self.BIP84AccountQLineEdit)


        self.BIP84HLayout.addWidget(self.BIP84AccountQFrame)

        self.BIP84ChangeQFrame = QFrame(self.BIP84QWidget)
        self.BIP84ChangeQFrame.setObjectName(u"BIP84ChangeQFrame")
        self.BIP84ChangeVLayout = QVBoxLayout(self.BIP84ChangeQFrame)
        self.BIP84ChangeVLayout.setSpacing(5)
        self.BIP84ChangeVLayout.setObjectName(u"BIP84ChangeVLayout")
        self.BIP84ChangeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84ChangeLabelQFrame = QFrame(self.BIP84ChangeQFrame)
        self.BIP84ChangeLabelQFrame.setObjectName(u"BIP84ChangeLabelQFrame")
        self.BIP84ChangeLabelHLayout = QHBoxLayout(self.BIP84ChangeLabelQFrame)
        self.BIP84ChangeLabelHLayout.setSpacing(5)
        self.BIP84ChangeLabelHLayout.setObjectName(u"BIP84ChangeLabelHLayout")
        self.BIP84ChangeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84ChangeQLabel = QLabel(self.BIP84ChangeLabelQFrame)
        self.BIP84ChangeQLabel.setObjectName(u"BIP84ChangeQLabel")

        self.BIP84ChangeLabelHLayout.addWidget(self.BIP84ChangeQLabel)

        self.BIP84ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84ChangeLabelHLayout.addItem(self.BIP84ChangeLabelHSpacer)


        self.BIP84ChangeVLayout.addWidget(self.BIP84ChangeLabelQFrame)

        self.BIP84ChangeQComboBox = QComboBox(self.BIP84ChangeQFrame)
        self.BIP84ChangeQComboBox.addItem("")
        self.BIP84ChangeQComboBox.addItem("")
        self.BIP84ChangeQComboBox.setObjectName(u"BIP84ChangeQComboBox")

        self.BIP84ChangeVLayout.addWidget(self.BIP84ChangeQComboBox)


        self.BIP84HLayout.addWidget(self.BIP84ChangeQFrame)

        self.BIP84AddressQFrame = QFrame(self.BIP84QWidget)
        self.BIP84AddressQFrame.setObjectName(u"BIP84AddressQFrame")
        self.BIP84AddressVLayout = QVBoxLayout(self.BIP84AddressQFrame)
        self.BIP84AddressVLayout.setSpacing(5)
        self.BIP84AddressVLayout.setObjectName(u"BIP84AddressVLayout")
        self.BIP84AddressVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84AddressLabelQFrame = QFrame(self.BIP84AddressQFrame)
        self.BIP84AddressLabelQFrame.setObjectName(u"BIP84AddressLabelQFrame")
        self.BIP84AddressLabelHLayout = QHBoxLayout(self.BIP84AddressLabelQFrame)
        self.BIP84AddressLabelHLayout.setSpacing(5)
        self.BIP84AddressLabelHLayout.setObjectName(u"BIP84AddressLabelHLayout")
        self.BIP84AddressLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84AddressQLabel = QLabel(self.BIP84AddressLabelQFrame)
        self.BIP84AddressQLabel.setObjectName(u"BIP84AddressQLabel")

        self.BIP84AddressLabelHLayout.addWidget(self.BIP84AddressQLabel)

        self.BIP84AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84AddressLabelHLayout.addItem(self.BIP84AddressLabelHSpacer)


        self.BIP84AddressVLayout.addWidget(self.BIP84AddressLabelQFrame)

        self.BIP84AddressQLineEdit = QLineEdit(self.BIP84AddressQFrame)
        self.BIP84AddressQLineEdit.setObjectName(u"BIP84AddressQLineEdit")

        self.BIP84AddressVLayout.addWidget(self.BIP84AddressQLineEdit)


        self.BIP84HLayout.addWidget(self.BIP84AddressQFrame)

        self.DerivationsQTabWidget.addTab(self.BIP84QWidget, "")
        self.BIP86QWidget = QWidget()
        self.BIP86QWidget.setObjectName(u"BIP86QWidget")
        self.horizontalLayout_19 = QHBoxLayout(self.BIP86QWidget)
        self.horizontalLayout_19.setSpacing(15)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.BIP86PurposeQFrame = QFrame(self.BIP86QWidget)
        self.BIP86PurposeQFrame.setObjectName(u"BIP86PurposeQFrame")
        self.BIP84PurposeVLayout_2 = QVBoxLayout(self.BIP86PurposeQFrame)
        self.BIP84PurposeVLayout_2.setSpacing(5)
        self.BIP84PurposeVLayout_2.setObjectName(u"BIP84PurposeVLayout_2")
        self.BIP84PurposeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86PurposeLabelQFrame = QFrame(self.BIP86PurposeQFrame)
        self.BIP86PurposeLabelQFrame.setObjectName(u"BIP86PurposeLabelQFrame")
        self.BIP84PurposeLabelHLayout_2 = QHBoxLayout(self.BIP86PurposeLabelQFrame)
        self.BIP84PurposeLabelHLayout_2.setSpacing(5)
        self.BIP84PurposeLabelHLayout_2.setObjectName(u"BIP84PurposeLabelHLayout_2")
        self.BIP84PurposeLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86PurposeQLabel = QLabel(self.BIP86PurposeLabelQFrame)
        self.BIP86PurposeQLabel.setObjectName(u"BIP86PurposeQLabel")

        self.BIP84PurposeLabelHLayout_2.addWidget(self.BIP86PurposeQLabel)

        self.BIP86PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84PurposeLabelHLayout_2.addItem(self.BIP86PurposeLabelHSpacer)


        self.BIP84PurposeVLayout_2.addWidget(self.BIP86PurposeLabelQFrame)

        self.BIP86PurposeQLineEdit = QLineEdit(self.BIP86PurposeQFrame)
        self.BIP86PurposeQLineEdit.setObjectName(u"BIP86PurposeQLineEdit")
        self.BIP86PurposeQLineEdit.setEnabled(False)

        self.BIP84PurposeVLayout_2.addWidget(self.BIP86PurposeQLineEdit)


        self.horizontalLayout_19.addWidget(self.BIP86PurposeQFrame)

        self.BIP86CoinTypeQFrame = QFrame(self.BIP86QWidget)
        self.BIP86CoinTypeQFrame.setObjectName(u"BIP86CoinTypeQFrame")
        self.BIP84CoinTypeVLayout_2 = QVBoxLayout(self.BIP86CoinTypeQFrame)
        self.BIP84CoinTypeVLayout_2.setSpacing(5)
        self.BIP84CoinTypeVLayout_2.setObjectName(u"BIP84CoinTypeVLayout_2")
        self.BIP84CoinTypeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86CoinTypeLabelQFrame = QFrame(self.BIP86CoinTypeQFrame)
        self.BIP86CoinTypeLabelQFrame.setObjectName(u"BIP86CoinTypeLabelQFrame")
        self.BIP84CoinTypeLabelHLayout_2 = QHBoxLayout(self.BIP86CoinTypeLabelQFrame)
        self.BIP84CoinTypeLabelHLayout_2.setSpacing(5)
        self.BIP84CoinTypeLabelHLayout_2.setObjectName(u"BIP84CoinTypeLabelHLayout_2")
        self.BIP84CoinTypeLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86CoinTypeQLabel = QLabel(self.BIP86CoinTypeLabelQFrame)
        self.BIP86CoinTypeQLabel.setObjectName(u"BIP86CoinTypeQLabel")

        self.BIP84CoinTypeLabelHLayout_2.addWidget(self.BIP86CoinTypeQLabel)

        self.BIP86CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84CoinTypeLabelHLayout_2.addItem(self.BIP86CoinTypeLabelHSpacer)


        self.BIP84CoinTypeVLayout_2.addWidget(self.BIP86CoinTypeLabelQFrame)

        self.BIP86CoinTypeQLineEdit = QLineEdit(self.BIP86CoinTypeQFrame)
        self.BIP86CoinTypeQLineEdit.setObjectName(u"BIP86CoinTypeQLineEdit")
        self.BIP86CoinTypeQLineEdit.setEnabled(False)

        self.BIP84CoinTypeVLayout_2.addWidget(self.BIP86CoinTypeQLineEdit)


        self.horizontalLayout_19.addWidget(self.BIP86CoinTypeQFrame)

        self.BIP86AccountQFrame = QFrame(self.BIP86QWidget)
        self.BIP86AccountQFrame.setObjectName(u"BIP86AccountQFrame")
        self.BIP84AccountVLayout_2 = QVBoxLayout(self.BIP86AccountQFrame)
        self.BIP84AccountVLayout_2.setSpacing(5)
        self.BIP84AccountVLayout_2.setObjectName(u"BIP84AccountVLayout_2")
        self.BIP84AccountVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86AccountLabelQFrame = QFrame(self.BIP86AccountQFrame)
        self.BIP86AccountLabelQFrame.setObjectName(u"BIP86AccountLabelQFrame")
        self.BIP84AccountLabelHLayout_2 = QHBoxLayout(self.BIP86AccountLabelQFrame)
        self.BIP84AccountLabelHLayout_2.setSpacing(5)
        self.BIP84AccountLabelHLayout_2.setObjectName(u"BIP84AccountLabelHLayout_2")
        self.BIP84AccountLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86AccountQLabel = QLabel(self.BIP86AccountLabelQFrame)
        self.BIP86AccountQLabel.setObjectName(u"BIP86AccountQLabel")

        self.BIP84AccountLabelHLayout_2.addWidget(self.BIP86AccountQLabel)

        self.BIP86AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84AccountLabelHLayout_2.addItem(self.BIP86AccountLabelHSpacer)


        self.BIP84AccountVLayout_2.addWidget(self.BIP86AccountLabelQFrame)

        self.BIP86AccountQLineEdit = QLineEdit(self.BIP86AccountQFrame)
        self.BIP86AccountQLineEdit.setObjectName(u"BIP86AccountQLineEdit")

        self.BIP84AccountVLayout_2.addWidget(self.BIP86AccountQLineEdit)


        self.horizontalLayout_19.addWidget(self.BIP86AccountQFrame)

        self.BIP86ChangeQFrame = QFrame(self.BIP86QWidget)
        self.BIP86ChangeQFrame.setObjectName(u"BIP86ChangeQFrame")
        self.BIP84ChangeVLayout_2 = QVBoxLayout(self.BIP86ChangeQFrame)
        self.BIP84ChangeVLayout_2.setSpacing(5)
        self.BIP84ChangeVLayout_2.setObjectName(u"BIP84ChangeVLayout_2")
        self.BIP84ChangeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86ChangeLabelQFrame = QFrame(self.BIP86ChangeQFrame)
        self.BIP86ChangeLabelQFrame.setObjectName(u"BIP86ChangeLabelQFrame")
        self.BIP84ChangeLabelHLayout_2 = QHBoxLayout(self.BIP86ChangeLabelQFrame)
        self.BIP84ChangeLabelHLayout_2.setSpacing(5)
        self.BIP84ChangeLabelHLayout_2.setObjectName(u"BIP84ChangeLabelHLayout_2")
        self.BIP84ChangeLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86ChangeQLabel = QLabel(self.BIP86ChangeLabelQFrame)
        self.BIP86ChangeQLabel.setObjectName(u"BIP86ChangeQLabel")

        self.BIP84ChangeLabelHLayout_2.addWidget(self.BIP86ChangeQLabel)

        self.BIP86ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84ChangeLabelHLayout_2.addItem(self.BIP86ChangeLabelHSpacer)


        self.BIP84ChangeVLayout_2.addWidget(self.BIP86ChangeLabelQFrame)

        self.BIP86ChangeQComboBox = QComboBox(self.BIP86ChangeQFrame)
        self.BIP86ChangeQComboBox.addItem("")
        self.BIP86ChangeQComboBox.addItem("")
        self.BIP86ChangeQComboBox.setObjectName(u"BIP86ChangeQComboBox")

        self.BIP84ChangeVLayout_2.addWidget(self.BIP86ChangeQComboBox)


        self.horizontalLayout_19.addWidget(self.BIP86ChangeQFrame)

        self.BIP86AddressQFrame = QFrame(self.BIP86QWidget)
        self.BIP86AddressQFrame.setObjectName(u"BIP86AddressQFrame")
        self.BIP84AddressVLayout_2 = QVBoxLayout(self.BIP86AddressQFrame)
        self.BIP84AddressVLayout_2.setSpacing(5)
        self.BIP84AddressVLayout_2.setObjectName(u"BIP84AddressVLayout_2")
        self.BIP84AddressVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86AddressLabelQFrame = QFrame(self.BIP86AddressQFrame)
        self.BIP86AddressLabelQFrame.setObjectName(u"BIP86AddressLabelQFrame")
        self.BIP84AddressLabelHLayout_2 = QHBoxLayout(self.BIP86AddressLabelQFrame)
        self.BIP84AddressLabelHLayout_2.setSpacing(5)
        self.BIP84AddressLabelHLayout_2.setObjectName(u"BIP84AddressLabelHLayout_2")
        self.BIP84AddressLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86AddressQLabel = QLabel(self.BIP86AddressLabelQFrame)
        self.BIP86AddressQLabel.setObjectName(u"BIP86AddressQLabel")

        self.BIP84AddressLabelHLayout_2.addWidget(self.BIP86AddressQLabel)

        self.BIP86AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84AddressLabelHLayout_2.addItem(self.BIP86AddressLabelHSpacer)


        self.BIP84AddressVLayout_2.addWidget(self.BIP86AddressLabelQFrame)

        self.BIP86AddressQLineEdit = QLineEdit(self.BIP86AddressQFrame)
        self.BIP86AddressQLineEdit.setObjectName(u"BIP86AddressQLineEdit")

        self.BIP84AddressVLayout_2.addWidget(self.BIP86AddressQLineEdit)


        self.horizontalLayout_19.addWidget(self.BIP86AddressQFrame)

        self.DerivationsQTabWidget.addTab(self.BIP86QWidget, "")
        self.BIP141QWidget = QWidget()
        self.BIP141QWidget.setObjectName(u"BIP141QWidget")
        self.BIP141HLayout = QHBoxLayout(self.BIP141QWidget)
        self.BIP141HLayout.setSpacing(15)
        self.BIP141HLayout.setObjectName(u"BIP141HLayout")
        self.BIP141HLayout.setContentsMargins(0, 10, 0, 0)
        self.BIP141PathQFrame = QFrame(self.BIP141QWidget)
        self.BIP141PathQFrame.setObjectName(u"BIP141PathQFrame")
        self.BIP141PathVLayout = QVBoxLayout(self.BIP141PathQFrame)
        self.BIP141PathVLayout.setSpacing(5)
        self.BIP141PathVLayout.setObjectName(u"BIP141PathVLayout")
        self.BIP141PathVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP141PathLabelQFrame = QFrame(self.BIP141PathQFrame)
        self.BIP141PathLabelQFrame.setObjectName(u"BIP141PathLabelQFrame")
        self.BIP141PathLabelHLayout = QHBoxLayout(self.BIP141PathLabelQFrame)
        self.BIP141PathLabelHLayout.setSpacing(5)
        self.BIP141PathLabelHLayout.setObjectName(u"BIP141PathLabelHLayout")
        self.BIP141PathLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP141PathQLabel = QLabel(self.BIP141PathLabelQFrame)
        self.BIP141PathQLabel.setObjectName(u"BIP141PathQLabel")

        self.BIP141PathLabelHLayout.addWidget(self.BIP141PathQLabel)

        self.BIP141PathLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP141PathLabelHLayout.addItem(self.BIP141PathLabelHSpacer)


        self.BIP141PathVLayout.addWidget(self.BIP141PathLabelQFrame)

        self.BIP141PathQLineEdit = QLineEdit(self.BIP141PathQFrame)
        self.BIP141PathQLineEdit.setObjectName(u"BIP141PathQLineEdit")

        self.BIP141PathVLayout.addWidget(self.BIP141PathQLineEdit)


        self.BIP141HLayout.addWidget(self.BIP141PathQFrame)

        self.BIP141ScriptSemanticsQFrame = QFrame(self.BIP141QWidget)
        self.BIP141ScriptSemanticsQFrame.setObjectName(u"BIP141ScriptSemanticsQFrame")
        self.BIP141ScriptSemanticsVLayout = QVBoxLayout(self.BIP141ScriptSemanticsQFrame)
        self.BIP141ScriptSemanticsVLayout.setSpacing(5)
        self.BIP141ScriptSemanticsVLayout.setObjectName(u"BIP141ScriptSemanticsVLayout")
        self.BIP141ScriptSemanticsVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP141ScriptSemanticsLabelQFrame = QFrame(self.BIP141ScriptSemanticsQFrame)
        self.BIP141ScriptSemanticsLabelQFrame.setObjectName(u"BIP141ScriptSemanticsLabelQFrame")
        self.BIP141ScriptSemanticsLabelHLayout = QHBoxLayout(self.BIP141ScriptSemanticsLabelQFrame)
        self.BIP141ScriptSemanticsLabelHLayout.setSpacing(5)
        self.BIP141ScriptSemanticsLabelHLayout.setObjectName(u"BIP141ScriptSemanticsLabelHLayout")
        self.BIP141ScriptSemanticsLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP141ScriptSemanticsQLabel = QLabel(self.BIP141ScriptSemanticsLabelQFrame)
        self.BIP141ScriptSemanticsQLabel.setObjectName(u"BIP141ScriptSemanticsQLabel")

        self.BIP141ScriptSemanticsLabelHLayout.addWidget(self.BIP141ScriptSemanticsQLabel)

        self.BIP141ScriptSemanticsLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP141ScriptSemanticsLabelHLayout.addItem(self.BIP141ScriptSemanticsLabelHSpacer)


        self.BIP141ScriptSemanticsVLayout.addWidget(self.BIP141ScriptSemanticsLabelQFrame)

        self.BIP141ScriptSemanticsQComboBox = QComboBox(self.BIP141ScriptSemanticsQFrame)
        self.BIP141ScriptSemanticsQComboBox.addItem("")
        self.BIP141ScriptSemanticsQComboBox.addItem("")
        self.BIP141ScriptSemanticsQComboBox.addItem("")
        self.BIP141ScriptSemanticsQComboBox.addItem("")
        self.BIP141ScriptSemanticsQComboBox.setObjectName(u"BIP141ScriptSemanticsQComboBox")

        self.BIP141ScriptSemanticsVLayout.addWidget(self.BIP141ScriptSemanticsQComboBox)


        self.BIP141HLayout.addWidget(self.BIP141ScriptSemanticsQFrame)

        self.DerivationsQTabWidget.addTab(self.BIP141QWidget, "")
        self.CIP1852QWidget = QWidget()
        self.CIP1852QWidget.setObjectName(u"CIP1852QWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.CIP1852QWidget)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.CIP1852PurposeQFrame = QFrame(self.CIP1852QWidget)
        self.CIP1852PurposeQFrame.setObjectName(u"CIP1852PurposeQFrame")
        self.BIP44PurposeVLayout_2 = QVBoxLayout(self.CIP1852PurposeQFrame)
        self.BIP44PurposeVLayout_2.setSpacing(5)
        self.BIP44PurposeVLayout_2.setObjectName(u"BIP44PurposeVLayout_2")
        self.BIP44PurposeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852PurposeLabelQFrame = QFrame(self.CIP1852PurposeQFrame)
        self.CIP1852PurposeLabelQFrame.setObjectName(u"CIP1852PurposeLabelQFrame")
        self.BIP44PurposeLabelHLayout_2 = QHBoxLayout(self.CIP1852PurposeLabelQFrame)
        self.BIP44PurposeLabelHLayout_2.setSpacing(5)
        self.BIP44PurposeLabelHLayout_2.setObjectName(u"BIP44PurposeLabelHLayout_2")
        self.BIP44PurposeLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852PurposeQLabel = QLabel(self.CIP1852PurposeLabelQFrame)
        self.CIP1852PurposeQLabel.setObjectName(u"CIP1852PurposeQLabel")

        self.BIP44PurposeLabelHLayout_2.addWidget(self.CIP1852PurposeQLabel)

        self.CIP1852PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44PurposeLabelHLayout_2.addItem(self.CIP1852PurposeLabelHSpacer)


        self.BIP44PurposeVLayout_2.addWidget(self.CIP1852PurposeLabelQFrame)

        self.CIP1852PurposeQLineEdit = QLineEdit(self.CIP1852PurposeQFrame)
        self.CIP1852PurposeQLineEdit.setObjectName(u"CIP1852PurposeQLineEdit")
        self.CIP1852PurposeQLineEdit.setEnabled(False)

        self.BIP44PurposeVLayout_2.addWidget(self.CIP1852PurposeQLineEdit)


        self.horizontalLayout_5.addWidget(self.CIP1852PurposeQFrame)

        self.CIP1852CoinTypeQFrame = QFrame(self.CIP1852QWidget)
        self.CIP1852CoinTypeQFrame.setObjectName(u"CIP1852CoinTypeQFrame")
        self.BIP44CoinTypeVLayout_2 = QVBoxLayout(self.CIP1852CoinTypeQFrame)
        self.BIP44CoinTypeVLayout_2.setSpacing(5)
        self.BIP44CoinTypeVLayout_2.setObjectName(u"BIP44CoinTypeVLayout_2")
        self.BIP44CoinTypeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852CoinTypeLabelQFrame = QFrame(self.CIP1852CoinTypeQFrame)
        self.CIP1852CoinTypeLabelQFrame.setObjectName(u"CIP1852CoinTypeLabelQFrame")
        self.BIP44CoinTypeLabelHLayout_2 = QHBoxLayout(self.CIP1852CoinTypeLabelQFrame)
        self.BIP44CoinTypeLabelHLayout_2.setSpacing(5)
        self.BIP44CoinTypeLabelHLayout_2.setObjectName(u"BIP44CoinTypeLabelHLayout_2")
        self.BIP44CoinTypeLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852CoinTypeQLabel = QLabel(self.CIP1852CoinTypeLabelQFrame)
        self.CIP1852CoinTypeQLabel.setObjectName(u"CIP1852CoinTypeQLabel")

        self.BIP44CoinTypeLabelHLayout_2.addWidget(self.CIP1852CoinTypeQLabel)

        self.CIP1852CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44CoinTypeLabelHLayout_2.addItem(self.CIP1852CoinTypeLabelHSpacer)


        self.BIP44CoinTypeVLayout_2.addWidget(self.CIP1852CoinTypeLabelQFrame)

        self.CIP1852CoinTypeQLineEdit = QLineEdit(self.CIP1852CoinTypeQFrame)
        self.CIP1852CoinTypeQLineEdit.setObjectName(u"CIP1852CoinTypeQLineEdit")
        self.CIP1852CoinTypeQLineEdit.setEnabled(False)

        self.BIP44CoinTypeVLayout_2.addWidget(self.CIP1852CoinTypeQLineEdit)


        self.horizontalLayout_5.addWidget(self.CIP1852CoinTypeQFrame)

        self.CIP1852AccountQFrame = QFrame(self.CIP1852QWidget)
        self.CIP1852AccountQFrame.setObjectName(u"CIP1852AccountQFrame")
        self.BIP44AccountVLayout_2 = QVBoxLayout(self.CIP1852AccountQFrame)
        self.BIP44AccountVLayout_2.setSpacing(5)
        self.BIP44AccountVLayout_2.setObjectName(u"BIP44AccountVLayout_2")
        self.BIP44AccountVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852AccountLabelQFrame = QFrame(self.CIP1852AccountQFrame)
        self.CIP1852AccountLabelQFrame.setObjectName(u"CIP1852AccountLabelQFrame")
        self.BIP44AccountLabelHLayout_2 = QHBoxLayout(self.CIP1852AccountLabelQFrame)
        self.BIP44AccountLabelHLayout_2.setSpacing(5)
        self.BIP44AccountLabelHLayout_2.setObjectName(u"BIP44AccountLabelHLayout_2")
        self.BIP44AccountLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852AccountQLabel = QLabel(self.CIP1852AccountLabelQFrame)
        self.CIP1852AccountQLabel.setObjectName(u"CIP1852AccountQLabel")

        self.BIP44AccountLabelHLayout_2.addWidget(self.CIP1852AccountQLabel)

        self.CIP1852AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AccountLabelHLayout_2.addItem(self.CIP1852AccountLabelHSpacer)


        self.BIP44AccountVLayout_2.addWidget(self.CIP1852AccountLabelQFrame)

        self.CIP1852AccountQLineEdit = QLineEdit(self.CIP1852AccountQFrame)
        self.CIP1852AccountQLineEdit.setObjectName(u"CIP1852AccountQLineEdit")

        self.BIP44AccountVLayout_2.addWidget(self.CIP1852AccountQLineEdit)


        self.horizontalLayout_5.addWidget(self.CIP1852AccountQFrame)

        self.CIP1852ChangeQFrame = QFrame(self.CIP1852QWidget)
        self.CIP1852ChangeQFrame.setObjectName(u"CIP1852ChangeQFrame")
        self.BIP44ChangeVLayout_2 = QVBoxLayout(self.CIP1852ChangeQFrame)
        self.BIP44ChangeVLayout_2.setSpacing(5)
        self.BIP44ChangeVLayout_2.setObjectName(u"BIP44ChangeVLayout_2")
        self.BIP44ChangeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852ChangeLabelQFrame = QFrame(self.CIP1852ChangeQFrame)
        self.CIP1852ChangeLabelQFrame.setObjectName(u"CIP1852ChangeLabelQFrame")
        self.BIP44ChangeLabelHLayout_2 = QHBoxLayout(self.CIP1852ChangeLabelQFrame)
        self.BIP44ChangeLabelHLayout_2.setSpacing(5)
        self.BIP44ChangeLabelHLayout_2.setObjectName(u"BIP44ChangeLabelHLayout_2")
        self.BIP44ChangeLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852ChangeQLabel = QLabel(self.CIP1852ChangeLabelQFrame)
        self.CIP1852ChangeQLabel.setObjectName(u"CIP1852ChangeQLabel")

        self.BIP44ChangeLabelHLayout_2.addWidget(self.CIP1852ChangeQLabel)

        self.CIP1852ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44ChangeLabelHLayout_2.addItem(self.CIP1852ChangeLabelHSpacer)


        self.BIP44ChangeVLayout_2.addWidget(self.CIP1852ChangeLabelQFrame)

        self.CIP1852ChangeQComboBox = QComboBox(self.CIP1852ChangeQFrame)
        self.CIP1852ChangeQComboBox.addItem("")
        self.CIP1852ChangeQComboBox.addItem("")
        self.CIP1852ChangeQComboBox.addItem("")
        self.CIP1852ChangeQComboBox.setObjectName(u"CIP1852ChangeQComboBox")

        self.BIP44ChangeVLayout_2.addWidget(self.CIP1852ChangeQComboBox)


        self.horizontalLayout_5.addWidget(self.CIP1852ChangeQFrame)

        self.CIP1852AddressQFrame = QFrame(self.CIP1852QWidget)
        self.CIP1852AddressQFrame.setObjectName(u"CIP1852AddressQFrame")
        self.BIP44AddressVLayout_2 = QVBoxLayout(self.CIP1852AddressQFrame)
        self.BIP44AddressVLayout_2.setSpacing(5)
        self.BIP44AddressVLayout_2.setObjectName(u"BIP44AddressVLayout_2")
        self.BIP44AddressVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852AddressLabelQFrame = QFrame(self.CIP1852AddressQFrame)
        self.CIP1852AddressLabelQFrame.setObjectName(u"CIP1852AddressLabelQFrame")
        self.BIP44AddressLabelHLayout_2 = QHBoxLayout(self.CIP1852AddressLabelQFrame)
        self.BIP44AddressLabelHLayout_2.setSpacing(5)
        self.BIP44AddressLabelHLayout_2.setObjectName(u"BIP44AddressLabelHLayout_2")
        self.BIP44AddressLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852AddressQLabel = QLabel(self.CIP1852AddressLabelQFrame)
        self.CIP1852AddressQLabel.setObjectName(u"CIP1852AddressQLabel")

        self.BIP44AddressLabelHLayout_2.addWidget(self.CIP1852AddressQLabel)

        self.CIP1852AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AddressLabelHLayout_2.addItem(self.CIP1852AddressLabelHSpacer)


        self.BIP44AddressVLayout_2.addWidget(self.CIP1852AddressLabelQFrame)

        self.CIP1852AddressQLineEdit = QLineEdit(self.CIP1852AddressQFrame)
        self.CIP1852AddressQLineEdit.setObjectName(u"CIP1852AddressQLineEdit")

        self.BIP44AddressVLayout_2.addWidget(self.CIP1852AddressQLineEdit)


        self.horizontalLayout_5.addWidget(self.CIP1852AddressQFrame)

        self.DerivationsQTabWidget.addTab(self.CIP1852QWidget, "")

        self.DerivationVLayout.addWidget(self.DerivationsQTabWidget)


        self.verticalLayout_17.addWidget(self.DerivationQFrame)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.CryptocurrencyAndFormatQFrame = QFrame(self.frame_6)
        self.CryptocurrencyAndFormatQFrame.setObjectName(u"CryptocurrencyAndFormatQFrame")
        self.CryptocurrencyAndFormatHLayout = QHBoxLayout(self.CryptocurrencyAndFormatQFrame)
        self.CryptocurrencyAndFormatHLayout.setSpacing(15)
        self.CryptocurrencyAndFormatHLayout.setObjectName(u"CryptocurrencyAndFormatHLayout")
        self.CryptocurrencyAndFormatHLayout.setContentsMargins(0, 0, 0, 0)
        self.FormatQFrame = QFrame(self.CryptocurrencyAndFormatQFrame)
        self.FormatQFrame.setObjectName(u"FormatQFrame")
        self.FormatQFrame.setMaximumSize(QSize(100, 16777215))
        self.FormatVLayout = QVBoxLayout(self.FormatQFrame)
        self.FormatVLayout.setSpacing(5)
        self.FormatVLayout.setObjectName(u"FormatVLayout")
        self.FormatVLayout.setContentsMargins(0, 0, 0, 0)
        self.FormatLabelQFrame = QFrame(self.FormatQFrame)
        self.FormatLabelQFrame.setObjectName(u"FormatLabelQFrame")
        self.FormatLabelHLayout = QHBoxLayout(self.FormatLabelQFrame)
        self.FormatLabelHLayout.setSpacing(15)
        self.FormatLabelHLayout.setObjectName(u"FormatLabelHLayout")
        self.FormatLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.FormatLabelQLabel = QLabel(self.FormatLabelQFrame)
        self.FormatLabelQLabel.setObjectName(u"FormatLabelQLabel")

        self.FormatLabelHLayout.addWidget(self.FormatLabelQLabel)

        self.FormatLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.FormatLabelHLayout.addItem(self.FormatLabelHSpacer)


        self.FormatVLayout.addWidget(self.FormatLabelQFrame)

        self.FormatQComboBox = QComboBox(self.FormatQFrame)
        self.FormatQComboBox.addItem("")
        self.FormatQComboBox.addItem("")
        self.FormatQComboBox.setObjectName(u"FormatQComboBox")

        self.FormatVLayout.addWidget(self.FormatQComboBox)


        self.CryptocurrencyAndFormatHLayout.addWidget(self.FormatQFrame)


        self.horizontalLayout_4.addWidget(self.CryptocurrencyAndFormatQFrame)

        self.FormsQFrame = QFrame(self.frame_6)
        self.FormsQFrame.setObjectName(u"FormsQFrame")
        self.horizontalLayout_18 = QHBoxLayout(self.FormsQFrame)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.KeysQFrame = QFrame(self.FormsQFrame)
        self.KeysQFrame.setObjectName(u"KeysQFrame")
        self.KeysQFrame.setMinimumSize(QSize(288, 0))
        self.KeysVLayout = QVBoxLayout(self.KeysQFrame)
        self.KeysVLayout.setSpacing(5)
        self.KeysVLayout.setObjectName(u"KeysVLayout")
        self.KeysVLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.KeysQFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.horizontalLayout_21 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_21.setSpacing(15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.KeysQLabel = QLabel(self.frame_4)
        self.KeysQLabel.setObjectName(u"KeysQLabel")

        self.horizontalLayout_21.addWidget(self.KeysQLabel)

        self.KeysLabelHSpacer = QSpacerItem(524, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.KeysLabelHSpacer)


        self.KeysVLayout.addWidget(self.frame_4)

        self.KeysLabelQFrame = QFrame(self.KeysQFrame)
        self.KeysLabelQFrame.setObjectName(u"KeysLabelQFrame")
        self.verticalLayout_18 = QVBoxLayout(self.KeysLabelQFrame)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.KeysLabelQFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.horizontalLayout_20 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.KeysQLineEdit = QLineEdit(self.frame_2)
        self.KeysQLineEdit.setObjectName(u"KeysQLineEdit")

        self.horizontalLayout_20.addWidget(self.KeysQLineEdit)

        self.GenerateQPushButton = QPushButton(self.frame_2)
        self.GenerateQPushButton.setObjectName(u"GenerateQPushButton")
        sizePolicy1.setHeightForWidth(self.GenerateQPushButton.sizePolicy().hasHeightForWidth())
        self.GenerateQPushButton.setSizePolicy(sizePolicy1)
        self.GenerateQPushButton.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.GenerateQPushButton)


        self.verticalLayout_18.addWidget(self.frame_2)


        self.KeysVLayout.addWidget(self.KeysLabelQFrame)


        self.horizontalLayout_18.addWidget(self.KeysQFrame)


        self.horizontalLayout_4.addWidget(self.FormsQFrame)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.horizontalLayout.addWidget(self.hdWalletContainerQFrame)

        self.outputQFrame = QFrame(self.centralwidget)
        self.outputQFrame.setObjectName(u"outputQFrame")
        self.outputQFrame.setMinimumSize(QSize(400, 0))
        self.verticalLayout_2 = QVBoxLayout(self.outputQFrame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 15)
        self.frame_24 = QFrame(self.outputQFrame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 30))
        self.frame_24.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_22 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_22.setSpacing(15)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_4)

        self.expandTerminalQFrame = QFrame(self.frame_24)
        self.expandTerminalQFrame.setObjectName(u"expandTerminalQFrame")
        self.expandTerminalQFrame.setMinimumSize(QSize(20, 20))
        self.expandTerminalQFrame.setMaximumSize(QSize(20, 20))
        self.expandTerminalQFrame.setFrameShape(QFrame.StyledPanel)
        self.expandTerminalQFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.expandTerminalQFrame)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_22.addWidget(self.expandTerminalQFrame)


        self.verticalLayout_2.addWidget(self.frame_24)

        self.outputTerminalQTextEdit = QTextEdit(self.outputQFrame)
        self.outputTerminalQTextEdit.setObjectName(u"outputTerminalQTextEdit")
        self.outputTerminalQTextEdit.setEnabled(False)

        self.verticalLayout_2.addWidget(self.outputTerminalQTextEdit)

        self.outputTerminalQLineEdit = QLineEdit(self.outputQFrame)
        self.outputTerminalQLineEdit.setObjectName(u"outputTerminalQLineEdit")

        self.verticalLayout_2.addWidget(self.outputTerminalQLineEdit)


        self.horizontalLayout.addWidget(self.outputQFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.fromQStackedWidget_2.setCurrentIndex(1)
        self.fromQStackedWidget_3.setCurrentIndex(1)
        self.fromQStackedWidget_4.setCurrentIndex(1)
        self.fromQStackedWidget_5.setCurrentIndex(1)
        self.fromQStackedWidget.setCurrentIndex(0)
        self.DerivationsQTabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Donation", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HD", None))
        self.hdQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"BIP32", None))
        self.hdQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP44", None))
        self.hdQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"BIP49", None))
        self.hdQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"BIP84", None))
        self.hdQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"BIP86", None))
        self.hdQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"BIP141", None))
        self.hdQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.hdQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Electrum-V1", None))
        self.hdQComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Electrum-V2", None))
        self.hdQComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.fromQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.fromQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.fromQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Private key", None))
        self.fromQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Public key", None))
        self.fromQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Seed", None))
        self.fromQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"WIF", None))
        self.fromQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.fromQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"XPublic Key", None))

        self.CryptocurrencyLabelQLabel.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.CryptocurrencyQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"BTC - Bitcoin", None))
        self.CryptocurrencyQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BTC - Bitcoin Testnet", None))
        self.CryptocurrencyQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"QTUM - Qtum", None))
        self.CryptocurrencyQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"QTUM - Qtum Testnet", None))

        self.EntropyQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.EGenerateQPushButton_3.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ClientQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.EPassphraseQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.EPassphraseQLineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ELanguageQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.ELanguageQComboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.ELanguageQComboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.ELanguageQComboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.ELanguageQComboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.ELanguageQComboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.ELanguageQComboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.ELanguageQComboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.ELanguageQComboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.EWordsQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.EWordsQComboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.EWordsQComboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.EWordsQComboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.EWordsQComboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.EWordsQComboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.MnemonicQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.MGenerateQPushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ClientQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.MPassphraseQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.MPassphraseQLineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.MLanguageQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.MLanguageQComboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.MLanguageQComboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.MLanguageQComboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.MLanguageQComboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.MLanguageQComboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.MLanguageQComboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.MLanguageQComboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.MLanguageQComboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.MWordsQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.MWordsQComboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))

        self.ClientQLabel_6.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.SeedQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.XPrivateKeyQLabel_2.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.XPublicKeyQLabel_2.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.WIFQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.BIP38EncryptedWIFQCheckBox_2.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.PrivateKeyQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.PublicKeyQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.EntropyQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.EGenerateQPushButton_4.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ClientQLabel_7.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_7.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_7.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.EPassphraseQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.EPassphraseQLineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ELanguageQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.ELanguageQComboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.ELanguageQComboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.ELanguageQComboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.ELanguageQComboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.ELanguageQComboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.ELanguageQComboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.ELanguageQComboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.ELanguageQComboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.EWordsQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.EWordsQComboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.EWordsQComboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.EWordsQComboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.EWordsQComboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.EWordsQComboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.MnemonicQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.MGenerateQPushButton_3.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ClientQLabel_8.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_8.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_8.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_8.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.MPassphraseQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.MPassphraseQLineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.MLanguageQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.MLanguageQComboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.MLanguageQComboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.MLanguageQComboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.MLanguageQComboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.MLanguageQComboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.MLanguageQComboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.MLanguageQComboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.MLanguageQComboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.MWordsQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.MWordsQComboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))

        self.ClientQLabel_9.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_9.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_9.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_9.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.SeedQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.XPrivateKeyQLabel_3.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.XPublicKeyQLabel_3.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.WIFQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.BIP38EncryptedWIFQCheckBox_3.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.PrivateKeyQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.PublicKeyQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.EntropyQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.EGenerateQPushButton_5.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ClientQLabel_10.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_10.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_10.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_10.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_10.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.EPassphraseQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.EPassphraseQLineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ELanguageQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.ELanguageQComboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.ELanguageQComboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.ELanguageQComboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.ELanguageQComboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.ELanguageQComboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.ELanguageQComboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.ELanguageQComboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.ELanguageQComboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.EWordsQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.EWordsQComboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.EWordsQComboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.EWordsQComboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.EWordsQComboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.EWordsQComboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.MnemonicQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.MGenerateQPushButton_4.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ClientQLabel_11.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_11.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_11.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_11.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_11.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.MPassphraseQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.MPassphraseQLineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.MLanguageQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.MLanguageQComboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.MLanguageQComboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.MLanguageQComboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.MLanguageQComboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.MLanguageQComboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.MLanguageQComboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.MLanguageQComboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.MLanguageQComboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.MWordsQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.MWordsQComboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))

        self.ClientQLabel_12.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_12.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_12.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_12.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.SeedQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.XPrivateKeyQLabel_4.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.XPublicKeyQLabel_4.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.WIFQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.BIP38EncryptedWIFQCheckBox_4.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.PrivateKeyQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.PublicKeyQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.EntropyQLabel_6.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.EGenerateQPushButton_6.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ClientQLabel_13.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_13.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_13.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_13.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_13.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.EPassphraseQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.EPassphraseQLineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ELanguageQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.ELanguageQComboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.ELanguageQComboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.ELanguageQComboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.ELanguageQComboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.ELanguageQComboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.ELanguageQComboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.ELanguageQComboBox_5.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.ELanguageQComboBox_5.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.EWordsQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.EWordsQComboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.EWordsQComboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.EWordsQComboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.EWordsQComboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.EWordsQComboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.MnemonicQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.MGenerateQPushButton_5.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ClientQLabel_14.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_14.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_14.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_14.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_14.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.MPassphraseQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.MPassphraseQLineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.MLanguageQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.MLanguageQComboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.MLanguageQComboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.MLanguageQComboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.MLanguageQComboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.MLanguageQComboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.MLanguageQComboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.MLanguageQComboBox_5.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.MLanguageQComboBox_5.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.MWordsQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.MWordsQComboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))

        self.ClientQLabel_15.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_15.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_15.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_15.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_15.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_15.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.SeedQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.XPrivateKeyQLabel_5.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.XPublicKeyQLabel_5.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.WIFQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.BIP38EncryptedWIFQCheckBox_5.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.PrivateKeyQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.PublicKeyQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.EntropyQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.EGenerateQPushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.EPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.EPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ELanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.ELanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.ELanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.ELanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.ELanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.ELanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.ELanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.ELanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.ELanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.EWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.EWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.EWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.EWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.EWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.EWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.MnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.MGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ClientQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.MPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.MPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.MLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.MLanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.MLanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.MLanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.MLanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.MLanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.MLanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.MLanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.MLanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.MWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.MWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))

        self.ClientQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.SeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.XPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.XPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.WIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.BIP38EncryptedWIFQCheckBox.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.PrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.PublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.DerivationQLabel.setText(QCoreApplication.translate("MainWindow", u"Derivation", None))
        self.CustomPathQLabel.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.CustomPathQLineEdit.setText("")
        self.CustomPathQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"m/0'/0", None))
        self.CustomClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.CustomClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Custom", None))
        self.CustomClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Bitcoin Core", None))
        self.CustomClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"blockchain.info", None))
        self.CustomClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"MultiBit HD", None))
        self.CustomClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Coinomi, Ledger", None))

        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.CustomQWidget), QCoreApplication.translate("MainWindow", u"Custom", None))
        self.BIP44PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.BIP44PurposeQLineEdit.setText("")
        self.BIP44PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"44", None))
        self.BIP44CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.BIP44CoinTypeQLineEdit.setText("")
        self.BIP44CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BIP44AccountQLabel.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.BIP44AccountQLineEdit.setText("")
        self.BIP44AccountQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BIP44ChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.BIP44ChangeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"External", None))
        self.BIP44ChangeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internal", None))

        self.BIP44AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.BIP44AddressQLineEdit.setText("")
        self.BIP44AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.BIP44QWidget), QCoreApplication.translate("MainWindow", u"BIP44", None))
        self.BIP49PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.BIP49PurposeQLineEdit.setText("")
        self.BIP49PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"49", None))
        self.BIP49CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.BIP49CoinTypeQLineEdit.setText("")
        self.BIP49CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BIP49AccountQLabel.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.BIP49AccountQLineEdit.setText("")
        self.BIP49AccountQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BIP49ChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.BIP49ChangeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"External", None))
        self.BIP49ChangeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internal", None))

        self.BIP49AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.BIP49AddressQLineEdit.setText("")
        self.BIP49AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.BIP49QWidget), QCoreApplication.translate("MainWindow", u"BIP49", None))
        self.BIP84PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.BIP84PurposeQLineEdit.setText("")
        self.BIP84PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"84", None))
        self.BIP84CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.BIP84CoinTypeQLineEdit.setText("")
        self.BIP84CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BIP84AccountQLabel.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.BIP84AccountQLineEdit.setText("")
        self.BIP84AccountQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BIP84ChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.BIP84ChangeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"External", None))
        self.BIP84ChangeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internal", None))

        self.BIP84AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.BIP84AddressQLineEdit.setText("")
        self.BIP84AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.BIP84QWidget), QCoreApplication.translate("MainWindow", u"BIP84", None))
        self.BIP86PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.BIP86PurposeQLineEdit.setText("")
        self.BIP86PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"86", None))
        self.BIP86CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.BIP86CoinTypeQLineEdit.setText("")
        self.BIP86CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BIP86AccountQLabel.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.BIP86AccountQLineEdit.setText("")
        self.BIP86AccountQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BIP86ChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.BIP86ChangeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"External", None))
        self.BIP86ChangeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internal", None))

        self.BIP86AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.BIP86AddressQLineEdit.setText("")
        self.BIP86AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.BIP86QWidget), QCoreApplication.translate("MainWindow", u"BIP86", None))
        self.BIP141PathQLabel.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.BIP141PathQLineEdit.setText("")
        self.BIP141PathQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"m/0'/0", None))
        self.BIP141ScriptSemanticsQLabel.setText(QCoreApplication.translate("MainWindow", u"Script Semantics", None))
        self.BIP141ScriptSemanticsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"P2WPKH", None))
        self.BIP141ScriptSemanticsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"P2WPKH nested in P2SH", None))
        self.BIP141ScriptSemanticsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"P2WSH (1-of-1 multisig)", None))
        self.BIP141ScriptSemanticsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"P2WSH nested in P2SH (1-of-1 multisig)", None))

        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.BIP141QWidget), QCoreApplication.translate("MainWindow", u"BIP141", None))
        self.CIP1852PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.CIP1852PurposeQLineEdit.setText("")
        self.CIP1852PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1852", None))
        self.CIP1852CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.CIP1852CoinTypeQLineEdit.setText("")
        self.CIP1852CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1815", None))
        self.CIP1852AccountQLabel.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.CIP1852AccountQLineEdit.setText("")
        self.CIP1852AccountQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CIP1852ChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Role", None))
        self.CIP1852ChangeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"External", None))
        self.CIP1852ChangeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internal", None))
        self.CIP1852ChangeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Staking", None))

        self.CIP1852AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.CIP1852AddressQLineEdit.setText("")
        self.CIP1852AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.CIP1852QWidget), QCoreApplication.translate("MainWindow", u"CIP1852", None))
        self.FormatLabelQLabel.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.FormatQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"JSON", None))
        self.FormatQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CSV", None))

        self.KeysQLabel.setText(QCoreApplication.translate("MainWindow", u"Keys", None))
        self.GenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

