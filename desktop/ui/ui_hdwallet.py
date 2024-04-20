# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hdwalletcVrpGt.ui'
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
        MainWindow.resize(951, 444)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.hdWalletContainerQFrame = QFrame(self.centralwidget)
        self.hdWalletContainerQFrame.setObjectName(u"hdWalletContainerQFrame")
        self.hdWalletContainerQFrame.setMaximumSize(QSize(625, 16777215))
        self.hdWalletContainerQFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.hdWalletContainerQFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.frame = QFrame(self.hdWalletContainerQFrame)
        self.frame.setObjectName(u"frame")
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
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

        self.fromQStackedWidget = QStackedWidget(self.frame)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
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

        self.verticalLayout_3.addWidget(self.fromQStackedWidget)

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
        self.BIP141HLayout.setContentsMargins(0, 0, 0, 0)
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
        self.outputQFrame.setMinimumSize(QSize(200, 0))
        self.outputQFrame.setFrameShape(QFrame.StyledPanel)
        self.outputQFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.outputQFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.expandTerminalQFrame = QFrame(self.outputQFrame)
        self.expandTerminalQFrame.setObjectName(u"expandTerminalQFrame")
        self.expandTerminalQFrame.setMinimumSize(QSize(20, 20))
        self.expandTerminalQFrame.setMaximumSize(QSize(20, 20))
        self.expandTerminalQFrame.setFrameShape(QFrame.StyledPanel)
        self.expandTerminalQFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.expandTerminalQFrame)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.expandTerminalQFrame, 0, Qt.AlignRight)

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

        self.fromQStackedWidget.setCurrentIndex(0)
        self.DerivationsQTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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

