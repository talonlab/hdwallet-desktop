# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hdwalletNIhzTb.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1123, 769)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(625, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 15, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.hdQComboBox = QComboBox(self.frame_4)
        self.hdQComboBox.setObjectName(u"hdQComboBox")

        self.verticalLayout_5.addWidget(self.hdQComboBox)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
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

        self.fromQComboBox = QComboBox(self.frame_10)
        self.fromQComboBox.setObjectName(u"fromQComboBox")

        self.verticalLayout_6.addWidget(self.fromQComboBox)


        self.horizontalLayout_2.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_3)

        self.fromQStackedWidget = QStackedWidget(self.frame)
        self.fromQStackedWidget.setObjectName(u"fromQStackedWidget")
        self.fromQStackedWidget.setFrameShape(QFrame.StyledPanel)
        self.fromQStackedWidget.setFrameShadow(QFrame.Raised)
        self.fromEntropyQStackedWidget = QWidget()
        self.fromEntropyQStackedWidget.setObjectName(u"fromEntropyQStackedWidget")
        self.verticalLayout_4 = QVBoxLayout(self.fromEntropyQStackedWidget)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.fromEntropyQStackedWidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.EntropyQWidget = QWidget(self.frame_16)
        self.EntropyQWidget.setObjectName(u"EntropyQWidget")
        self.EntropyQWidget.setMinimumSize(QSize(400, 0))
        self.EntropyVLayout_2 = QVBoxLayout(self.EntropyQWidget)
        self.EntropyVLayout_2.setSpacing(15)
        self.EntropyVLayout_2.setObjectName(u"EntropyVLayout_2")
        self.EntropyVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.EntropyLabelQWidget_2 = QWidget(self.EntropyQWidget)
        self.EntropyLabelQWidget_2.setObjectName(u"EntropyLabelQWidget_2")
        self.EntropyLabelHLayout_2 = QHBoxLayout(self.EntropyLabelQWidget_2)
        self.EntropyLabelHLayout_2.setSpacing(5)
        self.EntropyLabelHLayout_2.setObjectName(u"EntropyLabelHLayout_2")
        self.EntropyLabelHLayout_2.setContentsMargins(0, 10, 0, 10)
        self.EntropyQLabel_2 = QLabel(self.EntropyLabelQWidget_2)
        self.EntropyQLabel_2.setObjectName(u"EntropyQLabel_2")

        self.EntropyLabelHLayout_2.addWidget(self.EntropyQLabel_2)

        self.EntropyLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_2.addItem(self.EntropyLabelHSpacer_2)


        self.EntropyVLayout_2.addWidget(self.EntropyLabelQWidget_2)


        self.verticalLayout_8.addWidget(self.EntropyQWidget)

        self.EGenerateQWidget = QWidget(self.frame_16)
        self.EGenerateQWidget.setObjectName(u"EGenerateQWidget")
        self.horizontalLayout_13 = QHBoxLayout(self.EGenerateQWidget)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.EntropyQLineEdit_2 = QLineEdit(self.EGenerateQWidget)
        self.EntropyQLineEdit_2.setObjectName(u"EntropyQLineEdit_2")
        self.EntropyQLineEdit_2.setStyleSheet(u"padding: 0 10px;")

        self.horizontalLayout_13.addWidget(self.EntropyQLineEdit_2)

        self.EGenerateQPushButton_2 = QPushButton(self.EGenerateQWidget)
        self.EGenerateQPushButton_2.setObjectName(u"EGenerateQPushButton_2")

        self.horizontalLayout_13.addWidget(self.EGenerateQPushButton_2)


        self.verticalLayout_8.addWidget(self.EGenerateQWidget)


        self.horizontalLayout_6.addWidget(self.frame_16)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.fromEntropyQStackedWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQWidget = QWidget(self.frame_8)
        self.ELanguageQWidget.setObjectName(u"ELanguageQWidget")
        self.ELanguageVLayout = QVBoxLayout(self.ELanguageQWidget)
        self.ELanguageVLayout.setSpacing(5)
        self.ELanguageVLayout.setObjectName(u"ELanguageVLayout")
        self.ELanguageVLayout.setContentsMargins(0, 0, 0, 0)
        self.ELanguageLabelQWidget = QWidget(self.ELanguageQWidget)
        self.ELanguageLabelQWidget.setObjectName(u"ELanguageLabelQWidget")
        self.ELanguageLabelHLayout = QHBoxLayout(self.ELanguageLabelQWidget)
        self.ELanguageLabelHLayout.setSpacing(5)
        self.ELanguageLabelHLayout.setObjectName(u"ELanguageLabelHLayout")
        self.ELanguageLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.ELanguageQLabel = QLabel(self.ELanguageLabelQWidget)
        self.ELanguageQLabel.setObjectName(u"ELanguageQLabel")

        self.ELanguageLabelHLayout.addWidget(self.ELanguageQLabel)

        self.ELanguageLabelHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout.addItem(self.ELanguageLabelHSpacer)


        self.ELanguageVLayout.addWidget(self.ELanguageLabelQWidget)

        self.ELanguageQComboBox = QComboBox(self.ELanguageQWidget)
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


        self.horizontalLayout_7.addWidget(self.ELanguageQWidget)

        self.EWordsQWidget = QWidget(self.frame_8)
        self.EWordsQWidget.setObjectName(u"EWordsQWidget")
        self.EStrengthVLayout = QVBoxLayout(self.EWordsQWidget)
        self.EStrengthVLayout.setSpacing(5)
        self.EStrengthVLayout.setObjectName(u"EStrengthVLayout")
        self.EStrengthVLayout.setContentsMargins(0, 0, 0, 0)
        self.EWordsLabelQWidget = QWidget(self.EWordsQWidget)
        self.EWordsLabelQWidget.setObjectName(u"EWordsLabelQWidget")
        self.EStrengthLabelHLayout = QHBoxLayout(self.EWordsLabelQWidget)
        self.EStrengthLabelHLayout.setSpacing(5)
        self.EStrengthLabelHLayout.setObjectName(u"EStrengthLabelHLayout")
        self.EStrengthLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.EWordsQLabel = QLabel(self.EWordsLabelQWidget)
        self.EWordsQLabel.setObjectName(u"EWordsQLabel")

        self.EStrengthLabelHLayout.addWidget(self.EWordsQLabel)

        self.EWordsLabelHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout.addItem(self.EWordsLabelHSpacer)


        self.EStrengthVLayout.addWidget(self.EWordsLabelQWidget)

        self.EWordsQComboBox = QComboBox(self.EWordsQWidget)
        self.EWordsQComboBox.addItem("")
        self.EWordsQComboBox.addItem("")
        self.EWordsQComboBox.addItem("")
        self.EWordsQComboBox.addItem("")
        self.EWordsQComboBox.addItem("")
        self.EWordsQComboBox.setObjectName(u"EWordsQComboBox")

        self.EStrengthVLayout.addWidget(self.EWordsQComboBox)


        self.horizontalLayout_7.addWidget(self.EWordsQWidget)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.EPassphraseQWidget = QWidget(self.fromEntropyQStackedWidget)
        self.EPassphraseQWidget.setObjectName(u"EPassphraseQWidget")
        self.EPassphraseVLayout = QVBoxLayout(self.EPassphraseQWidget)
        self.EPassphraseVLayout.setSpacing(5)
        self.EPassphraseVLayout.setObjectName(u"EPassphraseVLayout")
        self.EPassphraseVLayout.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseLabelQWidget = QWidget(self.EPassphraseQWidget)
        self.EPassphraseLabelQWidget.setObjectName(u"EPassphraseLabelQWidget")
        self.EPassphraseLabelHLayout = QHBoxLayout(self.EPassphraseLabelQWidget)
        self.EPassphraseLabelHLayout.setSpacing(5)
        self.EPassphraseLabelHLayout.setObjectName(u"EPassphraseLabelHLayout")
        self.EPassphraseLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLabel = QLabel(self.EPassphraseLabelQWidget)
        self.EPassphraseQLabel.setObjectName(u"EPassphraseQLabel")

        self.EPassphraseLabelHLayout.addWidget(self.EPassphraseQLabel)

        self.EPassphraseLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout.addItem(self.EPassphraseLabelHSpacer)


        self.EPassphraseVLayout.addWidget(self.EPassphraseLabelQWidget)

        self.frame_12 = QFrame(self.EPassphraseQWidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.EPassphraseQLineEdit = QLineEdit(self.frame_12)
        self.EPassphraseQLineEdit.setObjectName(u"EPassphraseQLineEdit")
        self.EPassphraseQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.horizontalLayout_9.addWidget(self.EPassphraseQLineEdit)

        self.pushButton = QPushButton(self.frame_12)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_9.addWidget(self.pushButton)


        self.EPassphraseVLayout.addWidget(self.frame_12)


        self.verticalLayout_4.addWidget(self.EPassphraseQWidget)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.fromQStackedWidget.addWidget(self.fromEntropyQStackedWidget)
        self.fromMnemonicQStackedWidget = QWidget()
        self.fromMnemonicQStackedWidget.setObjectName(u"fromMnemonicQStackedWidget")
        self.verticalLayout_7 = QVBoxLayout(self.fromMnemonicQStackedWidget)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQWidget = QWidget(self.fromMnemonicQStackedWidget)
        self.MnemonicQWidget.setObjectName(u"MnemonicQWidget")
        self.MnemonicVLayout = QVBoxLayout(self.MnemonicQWidget)
        self.MnemonicVLayout.setSpacing(5)
        self.MnemonicVLayout.setObjectName(u"MnemonicVLayout")
        self.MnemonicVLayout.setContentsMargins(0, 0, 0, 0)
        self.MnemonicLabelQWidget = QWidget(self.MnemonicQWidget)
        self.MnemonicLabelQWidget.setObjectName(u"MnemonicLabelQWidget")
        self.MnemonicLabelHLayout = QHBoxLayout(self.MnemonicLabelQWidget)
        self.MnemonicLabelHLayout.setSpacing(5)
        self.MnemonicLabelHLayout.setObjectName(u"MnemonicLabelHLayout")
        self.MnemonicLabelHLayout.setContentsMargins(0, 10, 0, 10)
        self.MnemonicQLabel = QLabel(self.MnemonicLabelQWidget)
        self.MnemonicQLabel.setObjectName(u"MnemonicQLabel")

        self.MnemonicLabelHLayout.addWidget(self.MnemonicQLabel)

        self.MnemonicLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout.addItem(self.MnemonicLabelHSpacer)


        self.MnemonicVLayout.addWidget(self.MnemonicLabelQWidget)

        self.frame_13 = QFrame(self.MnemonicQWidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQLineEdit = QLineEdit(self.frame_13)
        self.MnemonicQLineEdit.setObjectName(u"MnemonicQLineEdit")
        self.MnemonicQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.horizontalLayout_10.addWidget(self.MnemonicQLineEdit)

        self.MGenerateQWidget = QWidget(self.frame_13)
        self.MGenerateQWidget.setObjectName(u"MGenerateQWidget")
        self.GenerateMnemonicVLayout = QVBoxLayout(self.MGenerateQWidget)
        self.GenerateMnemonicVLayout.setSpacing(15)
        self.GenerateMnemonicVLayout.setObjectName(u"GenerateMnemonicVLayout")
        self.GenerateMnemonicVLayout.setContentsMargins(0, 0, 0, 0)
        self.MGenerateQPushButton = QPushButton(self.MGenerateQWidget)
        self.MGenerateQPushButton.setObjectName(u"MGenerateQPushButton")

        self.GenerateMnemonicVLayout.addWidget(self.MGenerateQPushButton)


        self.horizontalLayout_10.addWidget(self.MGenerateQWidget)


        self.MnemonicVLayout.addWidget(self.frame_13)


        self.verticalLayout_7.addWidget(self.MnemonicQWidget)

        self.frame_14 = QFrame(self.fromMnemonicQStackedWidget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQWidget = QWidget(self.frame_14)
        self.MLanguageQWidget.setObjectName(u"MLanguageQWidget")
        self.MLanguageVLayout = QVBoxLayout(self.MLanguageQWidget)
        self.MLanguageVLayout.setSpacing(5)
        self.MLanguageVLayout.setObjectName(u"MLanguageVLayout")
        self.MLanguageVLayout.setContentsMargins(0, 0, 0, 0)
        self.MLanguageLabelQWidget = QWidget(self.MLanguageQWidget)
        self.MLanguageLabelQWidget.setObjectName(u"MLanguageLabelQWidget")
        self.MLanguageLabelHLayout = QHBoxLayout(self.MLanguageLabelQWidget)
        self.MLanguageLabelHLayout.setSpacing(5)
        self.MLanguageLabelHLayout.setObjectName(u"MLanguageLabelHLayout")
        self.MLanguageLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.MLanguageQLabel = QLabel(self.MLanguageLabelQWidget)
        self.MLanguageQLabel.setObjectName(u"MLanguageQLabel")

        self.MLanguageLabelHLayout.addWidget(self.MLanguageQLabel)

        self.MLanguageLabelHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MLanguageLabelHLayout.addItem(self.MLanguageLabelHSpacer)


        self.MLanguageVLayout.addWidget(self.MLanguageLabelQWidget)

        self.MLanguageQComboBox = QComboBox(self.MLanguageQWidget)
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


        self.horizontalLayout_11.addWidget(self.MLanguageQWidget)

        self.MWordsQWidget = QWidget(self.frame_14)
        self.MWordsQWidget.setObjectName(u"MWordsQWidget")
        self.MStrengthVLayout = QVBoxLayout(self.MWordsQWidget)
        self.MStrengthVLayout.setSpacing(5)
        self.MStrengthVLayout.setObjectName(u"MStrengthVLayout")
        self.MStrengthVLayout.setContentsMargins(0, 0, 0, 0)
        self.MWordsLabelQWidget = QWidget(self.MWordsQWidget)
        self.MWordsLabelQWidget.setObjectName(u"MWordsLabelQWidget")
        self.MStrengthLabelHLayout = QHBoxLayout(self.MWordsLabelQWidget)
        self.MStrengthLabelHLayout.setSpacing(5)
        self.MStrengthLabelHLayout.setObjectName(u"MStrengthLabelHLayout")
        self.MStrengthLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.MWordsQLabel = QLabel(self.MWordsLabelQWidget)
        self.MWordsQLabel.setObjectName(u"MWordsQLabel")

        self.MStrengthLabelHLayout.addWidget(self.MWordsQLabel)

        self.MWordsLabelHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout.addItem(self.MWordsLabelHSpacer)


        self.MStrengthVLayout.addWidget(self.MWordsLabelQWidget)

        self.MWordsQComboBox = QComboBox(self.MWordsQWidget)
        self.MWordsQComboBox.addItem("")
        self.MWordsQComboBox.setObjectName(u"MWordsQComboBox")

        self.MStrengthVLayout.addWidget(self.MWordsQComboBox)


        self.horizontalLayout_11.addWidget(self.MWordsQWidget)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.MPassphraseQWidget = QWidget(self.fromMnemonicQStackedWidget)
        self.MPassphraseQWidget.setObjectName(u"MPassphraseQWidget")
        self.EPassphraseVLayout_2 = QVBoxLayout(self.MPassphraseQWidget)
        self.EPassphraseVLayout_2.setSpacing(5)
        self.EPassphraseVLayout_2.setObjectName(u"EPassphraseVLayout_2")
        self.EPassphraseVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseLabelQWidget = QWidget(self.MPassphraseQWidget)
        self.MPassphraseLabelQWidget.setObjectName(u"MPassphraseLabelQWidget")
        self.MPassphraseLabelHLayout = QHBoxLayout(self.MPassphraseLabelQWidget)
        self.MPassphraseLabelHLayout.setSpacing(5)
        self.MPassphraseLabelHLayout.setObjectName(u"MPassphraseLabelHLayout")
        self.MPassphraseLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLabel = QLabel(self.MPassphraseLabelQWidget)
        self.MPassphraseQLabel.setObjectName(u"MPassphraseQLabel")

        self.MPassphraseLabelHLayout.addWidget(self.MPassphraseQLabel)

        self.MPassphraseLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout.addItem(self.MPassphraseLabelHSpacer)


        self.EPassphraseVLayout_2.addWidget(self.MPassphraseLabelQWidget)

        self.frame_15 = QFrame(self.MPassphraseQWidget)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.MPassphraseQLineEdit = QLineEdit(self.frame_15)
        self.MPassphraseQLineEdit.setObjectName(u"MPassphraseQLineEdit")
        self.MPassphraseQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.horizontalLayout_12.addWidget(self.MPassphraseQLineEdit)

        self.pushButton_2 = QPushButton(self.frame_15)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_12.addWidget(self.pushButton_2)


        self.EPassphraseVLayout_2.addWidget(self.frame_15)


        self.verticalLayout_7.addWidget(self.MPassphraseQWidget)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.fromQStackedWidget.addWidget(self.fromMnemonicQStackedWidget)
        self.fromSeedQStackedWidget = QWidget()
        self.fromSeedQStackedWidget.setObjectName(u"fromSeedQStackedWidget")
        self.verticalLayout_9 = QVBoxLayout(self.fromSeedQStackedWidget)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.SeedQWidget = QWidget(self.fromSeedQStackedWidget)
        self.SeedQWidget.setObjectName(u"SeedQWidget")
        self.SeedQWidget.setMinimumSize(QSize(400, 0))
        self.SeedVLayout = QVBoxLayout(self.SeedQWidget)
        self.SeedVLayout.setSpacing(5)
        self.SeedVLayout.setObjectName(u"SeedVLayout")
        self.SeedVLayout.setContentsMargins(0, 0, 0, 0)
        self.SeedLabelQWidget = QWidget(self.SeedQWidget)
        self.SeedLabelQWidget.setObjectName(u"SeedLabelQWidget")
        self.SeedLabelHLayout = QHBoxLayout(self.SeedLabelQWidget)
        self.SeedLabelHLayout.setSpacing(5)
        self.SeedLabelHLayout.setObjectName(u"SeedLabelHLayout")
        self.SeedLabelHLayout.setContentsMargins(0, 10, 0, 10)
        self.SeedQLabel = QLabel(self.SeedLabelQWidget)
        self.SeedQLabel.setObjectName(u"SeedQLabel")

        self.SeedLabelHLayout.addWidget(self.SeedQLabel)

        self.SeedLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout.addItem(self.SeedLabelHSpacer)


        self.SeedVLayout.addWidget(self.SeedLabelQWidget)

        self.SeedQLineEdit = QLineEdit(self.SeedQWidget)
        self.SeedQLineEdit.setObjectName(u"SeedQLineEdit")
        self.SeedQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.SeedVLayout.addWidget(self.SeedQLineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout.addItem(self.verticalSpacer)


        self.verticalLayout_9.addWidget(self.SeedQWidget)

        self.fromQStackedWidget.addWidget(self.fromSeedQStackedWidget)
        self.fromXPrivateKeyQStackedWidget = QWidget()
        self.fromXPrivateKeyQStackedWidget.setObjectName(u"fromXPrivateKeyQStackedWidget")
        self.verticalLayout_10 = QVBoxLayout(self.fromXPrivateKeyQStackedWidget)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQWidget = QWidget(self.fromXPrivateKeyQStackedWidget)
        self.XPrivateKeyQWidget.setObjectName(u"XPrivateKeyQWidget")
        self.XPrivateKeyQWidget.setMinimumSize(QSize(400, 0))
        self.XPrivateKeyVLayout = QVBoxLayout(self.XPrivateKeyQWidget)
        self.XPrivateKeyVLayout.setSpacing(5)
        self.XPrivateKeyVLayout.setObjectName(u"XPrivateKeyVLayout")
        self.XPrivateKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyLabelQWidget = QWidget(self.XPrivateKeyQWidget)
        self.XPrivateKeyLabelQWidget.setObjectName(u"XPrivateKeyLabelQWidget")
        self.XPrivateKeyLabelHLayout = QHBoxLayout(self.XPrivateKeyLabelQWidget)
        self.XPrivateKeyLabelHLayout.setSpacing(5)
        self.XPrivateKeyLabelHLayout.setObjectName(u"XPrivateKeyLabelHLayout")
        self.XPrivateKeyLabelHLayout.setContentsMargins(0, 10, 0, 10)
        self.XPrivateKeyQLabel = QLabel(self.XPrivateKeyLabelQWidget)
        self.XPrivateKeyQLabel.setObjectName(u"XPrivateKeyQLabel")

        self.XPrivateKeyLabelHLayout.addWidget(self.XPrivateKeyQLabel)

        self.XPrivateKeyLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPrivateKeyLabelHLayout.addItem(self.XPrivateKeyLabelHSpacer)


        self.XPrivateKeyVLayout.addWidget(self.XPrivateKeyLabelQWidget)

        self.XPrivateKeyQLineEdit = QLineEdit(self.XPrivateKeyQWidget)
        self.XPrivateKeyQLineEdit.setObjectName(u"XPrivateKeyQLineEdit")
        self.XPrivateKeyQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.XPrivateKeyVLayout.addWidget(self.XPrivateKeyQLineEdit)


        self.verticalLayout_10.addWidget(self.XPrivateKeyQWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.fromQStackedWidget.addWidget(self.fromXPrivateKeyQStackedWidget)
        self.fromXPublicKeyQStackedWidget = QWidget()
        self.fromXPublicKeyQStackedWidget.setObjectName(u"fromXPublicKeyQStackedWidget")
        self.verticalLayout_11 = QVBoxLayout(self.fromXPublicKeyQStackedWidget)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQWidget = QWidget(self.fromXPublicKeyQStackedWidget)
        self.XPublicKeyQWidget.setObjectName(u"XPublicKeyQWidget")
        self.XPublicKeyQWidget.setMinimumSize(QSize(400, 0))
        self.XPublicKeyVLayout = QVBoxLayout(self.XPublicKeyQWidget)
        self.XPublicKeyVLayout.setSpacing(5)
        self.XPublicKeyVLayout.setObjectName(u"XPublicKeyVLayout")
        self.XPublicKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyLabelQWidget = QWidget(self.XPublicKeyQWidget)
        self.XPublicKeyLabelQWidget.setObjectName(u"XPublicKeyLabelQWidget")
        self.XPublicKeyLabelHLayout = QHBoxLayout(self.XPublicKeyLabelQWidget)
        self.XPublicKeyLabelHLayout.setSpacing(5)
        self.XPublicKeyLabelHLayout.setObjectName(u"XPublicKeyLabelHLayout")
        self.XPublicKeyLabelHLayout.setContentsMargins(0, 10, 0, 10)
        self.XPublicKeyQLabel = QLabel(self.XPublicKeyLabelQWidget)
        self.XPublicKeyQLabel.setObjectName(u"XPublicKeyQLabel")

        self.XPublicKeyLabelHLayout.addWidget(self.XPublicKeyQLabel)

        self.XPublicKeyLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPublicKeyLabelHLayout.addItem(self.XPublicKeyLabelHSpacer)


        self.XPublicKeyVLayout.addWidget(self.XPublicKeyLabelQWidget)

        self.XPublicKeyQLineEdit = QLineEdit(self.XPublicKeyQWidget)
        self.XPublicKeyQLineEdit.setObjectName(u"XPublicKeyQLineEdit")
        self.XPublicKeyQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.XPublicKeyVLayout.addWidget(self.XPublicKeyQLineEdit)


        self.verticalLayout_11.addWidget(self.XPublicKeyQWidget)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.fromQStackedWidget.addWidget(self.fromXPublicKeyQStackedWidget)
        self.fromWIFQStackedWidget = QWidget()
        self.fromWIFQStackedWidget.setObjectName(u"fromWIFQStackedWidget")
        self.verticalLayout_12 = QVBoxLayout(self.fromWIFQStackedWidget)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.WIFQWidget = QWidget(self.fromWIFQStackedWidget)
        self.WIFQWidget.setObjectName(u"WIFQWidget")
        self.WIFQWidget.setMinimumSize(QSize(400, 0))
        self.WIFVLayout = QVBoxLayout(self.WIFQWidget)
        self.WIFVLayout.setSpacing(5)
        self.WIFVLayout.setObjectName(u"WIFVLayout")
        self.WIFVLayout.setContentsMargins(0, 0, 0, 0)
        self.WIFLabelQWidget = QWidget(self.WIFQWidget)
        self.WIFLabelQWidget.setObjectName(u"WIFLabelQWidget")
        self.WIFLabelHLayout = QHBoxLayout(self.WIFLabelQWidget)
        self.WIFLabelHLayout.setSpacing(5)
        self.WIFLabelHLayout.setObjectName(u"WIFLabelHLayout")
        self.WIFLabelHLayout.setContentsMargins(0, 10, 0, 10)
        self.WIFQLabel = QLabel(self.WIFLabelQWidget)
        self.WIFQLabel.setObjectName(u"WIFQLabel")

        self.WIFLabelHLayout.addWidget(self.WIFQLabel)

        self.WIFLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WIFLabelHLayout.addItem(self.WIFLabelHSpacer)


        self.WIFVLayout.addWidget(self.WIFLabelQWidget)

        self.WIFQLineEdit = QLineEdit(self.WIFQWidget)
        self.WIFQLineEdit.setObjectName(u"WIFQLineEdit")
        self.WIFQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.WIFVLayout.addWidget(self.WIFQLineEdit)

        self.BIP38EncryptedWIFQCheckBox = QCheckBox(self.WIFQWidget)
        self.BIP38EncryptedWIFQCheckBox.setObjectName(u"BIP38EncryptedWIFQCheckBox")

        self.WIFVLayout.addWidget(self.BIP38EncryptedWIFQCheckBox)


        self.verticalLayout_12.addWidget(self.WIFQWidget)

        self.BIP38EncryptedWIFPassphraseQWidget = QWidget(self.fromWIFQStackedWidget)
        self.BIP38EncryptedWIFPassphraseQWidget.setObjectName(u"BIP38EncryptedWIFPassphraseQWidget")
        self.BIP38EncryptedWIFPassphraseQWidget.setEnabled(False)
        self.EPassphraseVLayout_3 = QVBoxLayout(self.BIP38EncryptedWIFPassphraseQWidget)
        self.EPassphraseVLayout_3.setSpacing(5)
        self.EPassphraseVLayout_3.setObjectName(u"EPassphraseVLayout_3")
        self.EPassphraseVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.BIP38EncryptedWIFPassphraseQWidget)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFPassphraseLabelQWidget = QWidget(self.frame_17)
        self.BIP38EncryptedWIFPassphraseLabelQWidget.setObjectName(u"BIP38EncryptedWIFPassphraseLabelQWidget")
        self.EPassphraseLabelHLayout_2 = QHBoxLayout(self.BIP38EncryptedWIFPassphraseLabelQWidget)
        self.EPassphraseLabelHLayout_2.setSpacing(5)
        self.EPassphraseLabelHLayout_2.setObjectName(u"EPassphraseLabelHLayout_2")
        self.EPassphraseLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP38EncryptedWIFPassphraseQLabel = QLabel(self.BIP38EncryptedWIFPassphraseLabelQWidget)
        self.BIP38EncryptedWIFPassphraseQLabel.setObjectName(u"BIP38EncryptedWIFPassphraseQLabel")

        self.EPassphraseLabelHLayout_2.addWidget(self.BIP38EncryptedWIFPassphraseQLabel)

        self.BIP38EncryptedWIFPassphraseLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_2.addItem(self.BIP38EncryptedWIFPassphraseLabelHSpacer)


        self.verticalLayout_15.addWidget(self.BIP38EncryptedWIFPassphraseLabelQWidget)


        self.EPassphraseVLayout_3.addWidget(self.frame_17)


        self.verticalLayout_12.addWidget(self.BIP38EncryptedWIFPassphraseQWidget)

        self.frame_18 = QFrame(self.fromWIFQStackedWidget)
        self.frame_18.setObjectName(u"frame_18")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.BIP38PassphraseQLineEdit = QLineEdit(self.frame_18)
        self.BIP38PassphraseQLineEdit.setObjectName(u"BIP38PassphraseQLineEdit")

        self.horizontalLayout_14.addWidget(self.BIP38PassphraseQLineEdit)

        self.pushButton_3 = QPushButton(self.frame_18)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_14.addWidget(self.pushButton_3)


        self.verticalLayout_12.addWidget(self.frame_18)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.fromQStackedWidget.addWidget(self.fromWIFQStackedWidget)
        self.fromPrivateKeyQStackedWidget = QWidget()
        self.fromPrivateKeyQStackedWidget.setObjectName(u"fromPrivateKeyQStackedWidget")
        self.verticalLayout_13 = QVBoxLayout(self.fromPrivateKeyQStackedWidget)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQWidget = QWidget(self.fromPrivateKeyQStackedWidget)
        self.PrivateKeyQWidget.setObjectName(u"PrivateKeyQWidget")
        self.PrivateKeyQWidget.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout = QVBoxLayout(self.PrivateKeyQWidget)
        self.PrivateKeyVLayout.setSpacing(5)
        self.PrivateKeyVLayout.setObjectName(u"PrivateKeyVLayout")
        self.PrivateKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyLabelQWidget = QWidget(self.PrivateKeyQWidget)
        self.PrivateKeyLabelQWidget.setObjectName(u"PrivateKeyLabelQWidget")
        self.PrivateKeyLabelHLayout = QHBoxLayout(self.PrivateKeyLabelQWidget)
        self.PrivateKeyLabelHLayout.setSpacing(5)
        self.PrivateKeyLabelHLayout.setObjectName(u"PrivateKeyLabelHLayout")
        self.PrivateKeyLabelHLayout.setContentsMargins(0, 10, 0, 10)
        self.PrivateKeyQLabel = QLabel(self.PrivateKeyLabelQWidget)
        self.PrivateKeyQLabel.setObjectName(u"PrivateKeyQLabel")

        self.PrivateKeyLabelHLayout.addWidget(self.PrivateKeyQLabel)

        self.PrivateKeyLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout.addItem(self.PrivateKeyLabelHSpacer)


        self.PrivateKeyVLayout.addWidget(self.PrivateKeyLabelQWidget)

        self.PrivateKeyQLineEdit = QLineEdit(self.PrivateKeyQWidget)
        self.PrivateKeyQLineEdit.setObjectName(u"PrivateKeyQLineEdit")
        self.PrivateKeyQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.PrivateKeyVLayout.addWidget(self.PrivateKeyQLineEdit)


        self.verticalLayout_13.addWidget(self.PrivateKeyQWidget)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.fromQStackedWidget.addWidget(self.fromPrivateKeyQStackedWidget)
        self.fromPublicKeyQStackedWidget = QWidget()
        self.fromPublicKeyQStackedWidget.setObjectName(u"fromPublicKeyQStackedWidget")
        self.verticalLayout_14 = QVBoxLayout(self.fromPublicKeyQStackedWidget)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyQWidget = QWidget(self.fromPublicKeyQStackedWidget)
        self.PublicKeyQWidget.setObjectName(u"PublicKeyQWidget")
        self.PublicKeyQWidget.setMinimumSize(QSize(400, 0))
        self.PublicKeyVLayout = QVBoxLayout(self.PublicKeyQWidget)
        self.PublicKeyVLayout.setSpacing(5)
        self.PublicKeyVLayout.setObjectName(u"PublicKeyVLayout")
        self.PublicKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.PublicKeyLabelQWidget = QWidget(self.PublicKeyQWidget)
        self.PublicKeyLabelQWidget.setObjectName(u"PublicKeyLabelQWidget")
        self.PublicKeyLabelHLayout = QHBoxLayout(self.PublicKeyLabelQWidget)
        self.PublicKeyLabelHLayout.setSpacing(5)
        self.PublicKeyLabelHLayout.setObjectName(u"PublicKeyLabelHLayout")
        self.PublicKeyLabelHLayout.setContentsMargins(0, 10, 0, 10)
        self.PublicKeyQLabel = QLabel(self.PublicKeyLabelQWidget)
        self.PublicKeyQLabel.setObjectName(u"PublicKeyQLabel")

        self.PublicKeyLabelHLayout.addWidget(self.PublicKeyQLabel)

        self.PublicKeyLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PublicKeyLabelHLayout.addItem(self.PublicKeyLabelHSpacer)


        self.PublicKeyVLayout.addWidget(self.PublicKeyLabelQWidget)

        self.PublicKeyQLineEdit = QLineEdit(self.PublicKeyQWidget)
        self.PublicKeyQLineEdit.setObjectName(u"PublicKeyQLineEdit")
        self.PublicKeyQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.PublicKeyVLayout.addWidget(self.PublicKeyQLineEdit)


        self.verticalLayout_14.addWidget(self.PublicKeyQWidget)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.fromQStackedWidget.addWidget(self.fromPublicKeyQStackedWidget)

        self.verticalLayout.addWidget(self.fromQStackedWidget)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.FormsQWidget = QWidget(self.frame_6)
        self.FormsQWidget.setObjectName(u"FormsQWidget")
        self.FormsVLayout = QVBoxLayout(self.FormsQWidget)
        self.FormsVLayout.setSpacing(15)
        self.FormsVLayout.setObjectName(u"FormsVLayout")
        self.FormsVLayout.setContentsMargins(0, 0, 0, 0)
        self.CryptocurrencyAndFormatQWidget = QWidget(self.FormsQWidget)
        self.CryptocurrencyAndFormatQWidget.setObjectName(u"CryptocurrencyAndFormatQWidget")
        self.CryptocurrencyAndFormatHLayout = QHBoxLayout(self.CryptocurrencyAndFormatQWidget)
        self.CryptocurrencyAndFormatHLayout.setSpacing(15)
        self.CryptocurrencyAndFormatHLayout.setObjectName(u"CryptocurrencyAndFormatHLayout")
        self.CryptocurrencyAndFormatHLayout.setContentsMargins(0, 0, 0, 0)
        self.ClientQWidget = QWidget(self.CryptocurrencyAndFormatQWidget)
        self.ClientQWidget.setObjectName(u"ClientQWidget")
        self.ClientQWidget.setMinimumSize(QSize(150, 0))
        self.ClientVLayout = QVBoxLayout(self.ClientQWidget)
        self.ClientVLayout.setSpacing(15)
        self.ClientVLayout.setObjectName(u"ClientVLayout")
        self.ClientVLayout.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQWidget = QWidget(self.ClientQWidget)
        self.ClientLabelQWidget.setObjectName(u"ClientLabelQWidget")
        self.MStrengthLabelHLayout_3 = QHBoxLayout(self.ClientLabelQWidget)
        self.MStrengthLabelHLayout_3.setSpacing(5)
        self.MStrengthLabelHLayout_3.setObjectName(u"MStrengthLabelHLayout_3")
        self.MStrengthLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel = QLabel(self.ClientLabelQWidget)
        self.ClientQLabel.setObjectName(u"ClientQLabel")

        self.MStrengthLabelHLayout_3.addWidget(self.ClientQLabel)

        self.ClientLabelHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_3.addItem(self.ClientLabelHSpacer)


        self.ClientVLayout.addWidget(self.ClientLabelQWidget)

        self.ClientQComboBox = QComboBox(self.ClientQWidget)
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.addItem("")
        self.ClientQComboBox.setObjectName(u"ClientQComboBox")

        self.ClientVLayout.addWidget(self.ClientQComboBox)


        self.CryptocurrencyAndFormatHLayout.addWidget(self.ClientQWidget)

        self.CryptocurrencyQWidget = QWidget(self.CryptocurrencyAndFormatQWidget)
        self.CryptocurrencyQWidget.setObjectName(u"CryptocurrencyQWidget")
        self.CryptocurrencyVLayout = QVBoxLayout(self.CryptocurrencyQWidget)
        self.CryptocurrencyVLayout.setSpacing(15)
        self.CryptocurrencyVLayout.setObjectName(u"CryptocurrencyVLayout")
        self.CryptocurrencyVLayout.setContentsMargins(0, 0, 0, 0)
        self.CryptocurrencyLabelQWidget = QWidget(self.CryptocurrencyQWidget)
        self.CryptocurrencyLabelQWidget.setObjectName(u"CryptocurrencyLabelQWidget")
        self.CryptocurrencyLabelHLayout = QHBoxLayout(self.CryptocurrencyLabelQWidget)
        self.CryptocurrencyLabelHLayout.setSpacing(5)
        self.CryptocurrencyLabelHLayout.setObjectName(u"CryptocurrencyLabelHLayout")
        self.CryptocurrencyLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.CryptocurrencyLabelQLabel = QLabel(self.CryptocurrencyLabelQWidget)
        self.CryptocurrencyLabelQLabel.setObjectName(u"CryptocurrencyLabelQLabel")

        self.CryptocurrencyLabelHLayout.addWidget(self.CryptocurrencyLabelQLabel)

        self.CryptocurrencyLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.CryptocurrencyLabelHLayout.addItem(self.CryptocurrencyLabelHSpacer)


        self.CryptocurrencyVLayout.addWidget(self.CryptocurrencyLabelQWidget)

        self.CryptocurrencyQComboBox = QComboBox(self.CryptocurrencyQWidget)
        self.CryptocurrencyQComboBox.addItem("")
        self.CryptocurrencyQComboBox.addItem("")
        self.CryptocurrencyQComboBox.addItem("")
        self.CryptocurrencyQComboBox.addItem("")
        self.CryptocurrencyQComboBox.setObjectName(u"CryptocurrencyQComboBox")
        self.CryptocurrencyQComboBox.setMinimumSize(QSize(300, 0))
        self.CryptocurrencyQComboBox.setStyleSheet(u"padding: 0 10px;")

        self.CryptocurrencyVLayout.addWidget(self.CryptocurrencyQComboBox)


        self.CryptocurrencyAndFormatHLayout.addWidget(self.CryptocurrencyQWidget)

        self.FormatQWidget = QWidget(self.CryptocurrencyAndFormatQWidget)
        self.FormatQWidget.setObjectName(u"FormatQWidget")
        self.FormatVLayout = QVBoxLayout(self.FormatQWidget)
        self.FormatVLayout.setSpacing(15)
        self.FormatVLayout.setObjectName(u"FormatVLayout")
        self.FormatVLayout.setContentsMargins(0, 0, 0, 0)
        self.FormatLabelQWidget = QWidget(self.FormatQWidget)
        self.FormatLabelQWidget.setObjectName(u"FormatLabelQWidget")
        self.FormatLabelHLayout = QHBoxLayout(self.FormatLabelQWidget)
        self.FormatLabelHLayout.setSpacing(5)
        self.FormatLabelHLayout.setObjectName(u"FormatLabelHLayout")
        self.FormatLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.FormatLabelQLabel = QLabel(self.FormatLabelQWidget)
        self.FormatLabelQLabel.setObjectName(u"FormatLabelQLabel")

        self.FormatLabelHLayout.addWidget(self.FormatLabelQLabel)

        self.FormatLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.FormatLabelHLayout.addItem(self.FormatLabelHSpacer)


        self.FormatVLayout.addWidget(self.FormatLabelQWidget)

        self.FormatQComboBox = QComboBox(self.FormatQWidget)
        self.FormatQComboBox.addItem("")
        self.FormatQComboBox.addItem("")
        self.FormatQComboBox.setObjectName(u"FormatQComboBox")
        self.FormatQComboBox.setStyleSheet(u"padding: 0 10px;")

        self.FormatVLayout.addWidget(self.FormatQComboBox)


        self.CryptocurrencyAndFormatHLayout.addWidget(self.FormatQWidget)


        self.FormsVLayout.addWidget(self.CryptocurrencyAndFormatQWidget)

        self.KeysQWidget = QWidget(self.FormsQWidget)
        self.KeysQWidget.setObjectName(u"KeysQWidget")
        self.KeysQWidget.setMinimumSize(QSize(288, 0))
        self.KeysVLayout = QVBoxLayout(self.KeysQWidget)
        self.KeysVLayout.setSpacing(15)
        self.KeysVLayout.setObjectName(u"KeysVLayout")
        self.KeysVLayout.setContentsMargins(0, 0, 0, 0)
        self.KeysLabelQWidget = QWidget(self.KeysQWidget)
        self.KeysLabelQWidget.setObjectName(u"KeysLabelQWidget")
        self.KeysLabelHLayout = QHBoxLayout(self.KeysLabelQWidget)
        self.KeysLabelHLayout.setSpacing(5)
        self.KeysLabelHLayout.setObjectName(u"KeysLabelHLayout")
        self.KeysLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.KeysQLabel = QLabel(self.KeysLabelQWidget)
        self.KeysQLabel.setObjectName(u"KeysQLabel")

        self.KeysLabelHLayout.addWidget(self.KeysQLabel)

        self.KeysLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.KeysLabelHLayout.addItem(self.KeysLabelHSpacer)


        self.KeysVLayout.addWidget(self.KeysLabelQWidget)

        self.KeysQLineEdit = QLineEdit(self.KeysQWidget)
        self.KeysQLineEdit.setObjectName(u"KeysQLineEdit")
        self.KeysQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.KeysVLayout.addWidget(self.KeysQLineEdit)


        self.FormsVLayout.addWidget(self.KeysQWidget)


        self.horizontalLayout_4.addWidget(self.FormsQWidget)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.DerivationQWidget = QWidget(self.frame_5)
        self.DerivationQWidget.setObjectName(u"DerivationQWidget")
        self.DerivationVLayout = QVBoxLayout(self.DerivationQWidget)
        self.DerivationVLayout.setSpacing(0)
        self.DerivationVLayout.setObjectName(u"DerivationVLayout")
        self.DerivationVLayout.setContentsMargins(0, 0, 0, 0)
        self.DerivationLabelQWidget = QWidget(self.DerivationQWidget)
        self.DerivationLabelQWidget.setObjectName(u"DerivationLabelQWidget")
        self.DerivationLabelHLayout = QHBoxLayout(self.DerivationLabelQWidget)
        self.DerivationLabelHLayout.setSpacing(5)
        self.DerivationLabelHLayout.setObjectName(u"DerivationLabelHLayout")
        self.DerivationLabelHLayout.setContentsMargins(0, 11, 0, 11)
        self.DerivationQLabel = QLabel(self.DerivationLabelQWidget)
        self.DerivationQLabel.setObjectName(u"DerivationQLabel")

        self.DerivationLabelHLayout.addWidget(self.DerivationQLabel)

        self.DerivationLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.DerivationLabelHLayout.addItem(self.DerivationLabelHSpacer)


        self.DerivationVLayout.addWidget(self.DerivationLabelQWidget)

        self.DerivationsQTabWidget = QTabWidget(self.DerivationQWidget)
        self.DerivationsQTabWidget.setObjectName(u"DerivationsQTabWidget")
        self.CustomQWidget = QWidget()
        self.CustomQWidget.setObjectName(u"CustomQWidget")
        self.BIP32HLayout = QHBoxLayout(self.CustomQWidget)
        self.BIP32HLayout.setSpacing(15)
        self.BIP32HLayout.setObjectName(u"BIP32HLayout")
        self.BIP32HLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomPathQWidget = QWidget(self.CustomQWidget)
        self.CustomPathQWidget.setObjectName(u"CustomPathQWidget")
        self.BIP32DerivationPathVLayout = QVBoxLayout(self.CustomPathQWidget)
        self.BIP32DerivationPathVLayout.setSpacing(5)
        self.BIP32DerivationPathVLayout.setObjectName(u"BIP32DerivationPathVLayout")
        self.BIP32DerivationPathVLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomPathLabelQWidget = QWidget(self.CustomPathQWidget)
        self.CustomPathLabelQWidget.setObjectName(u"CustomPathLabelQWidget")
        self.BIP32DerivationPathLabelHLayout = QHBoxLayout(self.CustomPathLabelQWidget)
        self.BIP32DerivationPathLabelHLayout.setSpacing(5)
        self.BIP32DerivationPathLabelHLayout.setObjectName(u"BIP32DerivationPathLabelHLayout")
        self.BIP32DerivationPathLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomPathQLabel = QLabel(self.CustomPathLabelQWidget)
        self.CustomPathQLabel.setObjectName(u"CustomPathQLabel")

        self.BIP32DerivationPathLabelHLayout.addWidget(self.CustomPathQLabel)

        self.CustomPathLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP32DerivationPathLabelHLayout.addItem(self.CustomPathLabelHSpacer)


        self.BIP32DerivationPathVLayout.addWidget(self.CustomPathLabelQWidget)

        self.CustomPathQLineEdit = QLineEdit(self.CustomPathQWidget)
        self.CustomPathQLineEdit.setObjectName(u"CustomPathQLineEdit")
        self.CustomPathQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP32DerivationPathVLayout.addWidget(self.CustomPathQLineEdit)


        self.BIP32HLayout.addWidget(self.CustomPathQWidget)

        self.CustomClientQWidget = QWidget(self.CustomQWidget)
        self.CustomClientQWidget.setObjectName(u"CustomClientQWidget")
        self.CustomClientQWidget.setMinimumSize(QSize(175, 0))
        self.CustomClientQWidget.setMaximumSize(QSize(300, 16777215))
        self.BIP32ClientVLayout = QVBoxLayout(self.CustomClientQWidget)
        self.BIP32ClientVLayout.setSpacing(5)
        self.BIP32ClientVLayout.setObjectName(u"BIP32ClientVLayout")
        self.BIP32ClientVLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomClientLabelQWidget = QWidget(self.CustomClientQWidget)
        self.CustomClientLabelQWidget.setObjectName(u"CustomClientLabelQWidget")
        self.BIP32ClientLabelHLayout = QHBoxLayout(self.CustomClientLabelQWidget)
        self.BIP32ClientLabelHLayout.setSpacing(5)
        self.BIP32ClientLabelHLayout.setObjectName(u"BIP32ClientLabelHLayout")
        self.BIP32ClientLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomClientQLabel = QLabel(self.CustomClientLabelQWidget)
        self.CustomClientQLabel.setObjectName(u"CustomClientQLabel")

        self.BIP32ClientLabelHLayout.addWidget(self.CustomClientQLabel)

        self.CustomClientLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP32ClientLabelHLayout.addItem(self.CustomClientLabelHSpacer)


        self.BIP32ClientVLayout.addWidget(self.CustomClientLabelQWidget)

        self.CustomClientQComboBox = QComboBox(self.CustomClientQWidget)
        self.CustomClientQComboBox.addItem("")
        self.CustomClientQComboBox.addItem("")
        self.CustomClientQComboBox.addItem("")
        self.CustomClientQComboBox.addItem("")
        self.CustomClientQComboBox.addItem("")
        self.CustomClientQComboBox.setObjectName(u"CustomClientQComboBox")
        self.CustomClientQComboBox.setStyleSheet(u"padding: 0 10px;")

        self.BIP32ClientVLayout.addWidget(self.CustomClientQComboBox)


        self.BIP32HLayout.addWidget(self.CustomClientQWidget)

        self.DerivationsQTabWidget.addTab(self.CustomQWidget, "")
        self.BIP44QWidget = QWidget()
        self.BIP44QWidget.setObjectName(u"BIP44QWidget")
        self.BIP44HLayout = QHBoxLayout(self.BIP44QWidget)
        self.BIP44HLayout.setSpacing(15)
        self.BIP44HLayout.setObjectName(u"BIP44HLayout")
        self.BIP44HLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44PurposeQWidget = QWidget(self.BIP44QWidget)
        self.BIP44PurposeQWidget.setObjectName(u"BIP44PurposeQWidget")
        self.BIP44PurposeVLayout = QVBoxLayout(self.BIP44PurposeQWidget)
        self.BIP44PurposeVLayout.setSpacing(5)
        self.BIP44PurposeVLayout.setObjectName(u"BIP44PurposeVLayout")
        self.BIP44PurposeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44PurposeLabelQWidget = QWidget(self.BIP44PurposeQWidget)
        self.BIP44PurposeLabelQWidget.setObjectName(u"BIP44PurposeLabelQWidget")
        self.BIP44PurposeLabelHLayout = QHBoxLayout(self.BIP44PurposeLabelQWidget)
        self.BIP44PurposeLabelHLayout.setSpacing(5)
        self.BIP44PurposeLabelHLayout.setObjectName(u"BIP44PurposeLabelHLayout")
        self.BIP44PurposeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44PurposeQLabel = QLabel(self.BIP44PurposeLabelQWidget)
        self.BIP44PurposeQLabel.setObjectName(u"BIP44PurposeQLabel")

        self.BIP44PurposeLabelHLayout.addWidget(self.BIP44PurposeQLabel)

        self.BIP44PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44PurposeLabelHLayout.addItem(self.BIP44PurposeLabelHSpacer)


        self.BIP44PurposeVLayout.addWidget(self.BIP44PurposeLabelQWidget)

        self.BIP44PurposeQLineEdit = QLineEdit(self.BIP44PurposeQWidget)
        self.BIP44PurposeQLineEdit.setObjectName(u"BIP44PurposeQLineEdit")
        self.BIP44PurposeQLineEdit.setEnabled(False)
        self.BIP44PurposeQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP44PurposeVLayout.addWidget(self.BIP44PurposeQLineEdit)


        self.BIP44HLayout.addWidget(self.BIP44PurposeQWidget)

        self.BIP44CoinTypeQWidget = QWidget(self.BIP44QWidget)
        self.BIP44CoinTypeQWidget.setObjectName(u"BIP44CoinTypeQWidget")
        self.BIP44CoinTypeVLayout = QVBoxLayout(self.BIP44CoinTypeQWidget)
        self.BIP44CoinTypeVLayout.setSpacing(5)
        self.BIP44CoinTypeVLayout.setObjectName(u"BIP44CoinTypeVLayout")
        self.BIP44CoinTypeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44CoinTypeLabelQWidget = QWidget(self.BIP44CoinTypeQWidget)
        self.BIP44CoinTypeLabelQWidget.setObjectName(u"BIP44CoinTypeLabelQWidget")
        self.BIP44CoinTypeLabelHLayout = QHBoxLayout(self.BIP44CoinTypeLabelQWidget)
        self.BIP44CoinTypeLabelHLayout.setSpacing(5)
        self.BIP44CoinTypeLabelHLayout.setObjectName(u"BIP44CoinTypeLabelHLayout")
        self.BIP44CoinTypeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44CoinTypeQLabel = QLabel(self.BIP44CoinTypeLabelQWidget)
        self.BIP44CoinTypeQLabel.setObjectName(u"BIP44CoinTypeQLabel")

        self.BIP44CoinTypeLabelHLayout.addWidget(self.BIP44CoinTypeQLabel)

        self.BIP44CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44CoinTypeLabelHLayout.addItem(self.BIP44CoinTypeLabelHSpacer)


        self.BIP44CoinTypeVLayout.addWidget(self.BIP44CoinTypeLabelQWidget)

        self.BIP44CoinTypeQLineEdit = QLineEdit(self.BIP44CoinTypeQWidget)
        self.BIP44CoinTypeQLineEdit.setObjectName(u"BIP44CoinTypeQLineEdit")
        self.BIP44CoinTypeQLineEdit.setEnabled(False)
        self.BIP44CoinTypeQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP44CoinTypeVLayout.addWidget(self.BIP44CoinTypeQLineEdit)


        self.BIP44HLayout.addWidget(self.BIP44CoinTypeQWidget)

        self.BIP44AccountQWidget = QWidget(self.BIP44QWidget)
        self.BIP44AccountQWidget.setObjectName(u"BIP44AccountQWidget")
        self.BIP44AccountVLayout = QVBoxLayout(self.BIP44AccountQWidget)
        self.BIP44AccountVLayout.setSpacing(5)
        self.BIP44AccountVLayout.setObjectName(u"BIP44AccountVLayout")
        self.BIP44AccountVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44AccountLabelQWidget = QWidget(self.BIP44AccountQWidget)
        self.BIP44AccountLabelQWidget.setObjectName(u"BIP44AccountLabelQWidget")
        self.BIP44AccountLabelHLayout = QHBoxLayout(self.BIP44AccountLabelQWidget)
        self.BIP44AccountLabelHLayout.setSpacing(5)
        self.BIP44AccountLabelHLayout.setObjectName(u"BIP44AccountLabelHLayout")
        self.BIP44AccountLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44AccountQLabel = QLabel(self.BIP44AccountLabelQWidget)
        self.BIP44AccountQLabel.setObjectName(u"BIP44AccountQLabel")

        self.BIP44AccountLabelHLayout.addWidget(self.BIP44AccountQLabel)

        self.BIP44AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AccountLabelHLayout.addItem(self.BIP44AccountLabelHSpacer)


        self.BIP44AccountVLayout.addWidget(self.BIP44AccountLabelQWidget)

        self.BIP44AccountQLineEdit = QLineEdit(self.BIP44AccountQWidget)
        self.BIP44AccountQLineEdit.setObjectName(u"BIP44AccountQLineEdit")
        self.BIP44AccountQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP44AccountVLayout.addWidget(self.BIP44AccountQLineEdit)


        self.BIP44HLayout.addWidget(self.BIP44AccountQWidget)

        self.BIP44ChangeQWidget = QWidget(self.BIP44QWidget)
        self.BIP44ChangeQWidget.setObjectName(u"BIP44ChangeQWidget")
        self.BIP44ChangeVLayout = QVBoxLayout(self.BIP44ChangeQWidget)
        self.BIP44ChangeVLayout.setSpacing(5)
        self.BIP44ChangeVLayout.setObjectName(u"BIP44ChangeVLayout")
        self.BIP44ChangeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44ChangeLabelQWidget = QWidget(self.BIP44ChangeQWidget)
        self.BIP44ChangeLabelQWidget.setObjectName(u"BIP44ChangeLabelQWidget")
        self.BIP44ChangeLabelHLayout = QHBoxLayout(self.BIP44ChangeLabelQWidget)
        self.BIP44ChangeLabelHLayout.setSpacing(5)
        self.BIP44ChangeLabelHLayout.setObjectName(u"BIP44ChangeLabelHLayout")
        self.BIP44ChangeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44ChangeQLabel = QLabel(self.BIP44ChangeLabelQWidget)
        self.BIP44ChangeQLabel.setObjectName(u"BIP44ChangeQLabel")

        self.BIP44ChangeLabelHLayout.addWidget(self.BIP44ChangeQLabel)

        self.BIP44ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44ChangeLabelHLayout.addItem(self.BIP44ChangeLabelHSpacer)


        self.BIP44ChangeVLayout.addWidget(self.BIP44ChangeLabelQWidget)

        self.BIP44ChangeQComboBox = QComboBox(self.BIP44ChangeQWidget)
        self.BIP44ChangeQComboBox.addItem("")
        self.BIP44ChangeQComboBox.addItem("")
        self.BIP44ChangeQComboBox.setObjectName(u"BIP44ChangeQComboBox")
        self.BIP44ChangeQComboBox.setStyleSheet(u"padding: 0 10px;")

        self.BIP44ChangeVLayout.addWidget(self.BIP44ChangeQComboBox)


        self.BIP44HLayout.addWidget(self.BIP44ChangeQWidget)

        self.BIP44AddressQWidget = QWidget(self.BIP44QWidget)
        self.BIP44AddressQWidget.setObjectName(u"BIP44AddressQWidget")
        self.BIP44AddressVLayout = QVBoxLayout(self.BIP44AddressQWidget)
        self.BIP44AddressVLayout.setSpacing(5)
        self.BIP44AddressVLayout.setObjectName(u"BIP44AddressVLayout")
        self.BIP44AddressVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44AddressLabelQWidget = QWidget(self.BIP44AddressQWidget)
        self.BIP44AddressLabelQWidget.setObjectName(u"BIP44AddressLabelQWidget")
        self.BIP44AddressLabelHLayout = QHBoxLayout(self.BIP44AddressLabelQWidget)
        self.BIP44AddressLabelHLayout.setSpacing(5)
        self.BIP44AddressLabelHLayout.setObjectName(u"BIP44AddressLabelHLayout")
        self.BIP44AddressLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44AddressQLabel = QLabel(self.BIP44AddressLabelQWidget)
        self.BIP44AddressQLabel.setObjectName(u"BIP44AddressQLabel")

        self.BIP44AddressLabelHLayout.addWidget(self.BIP44AddressQLabel)

        self.BIP44AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AddressLabelHLayout.addItem(self.BIP44AddressLabelHSpacer)


        self.BIP44AddressVLayout.addWidget(self.BIP44AddressLabelQWidget)

        self.BIP44AddressQLineEdit = QLineEdit(self.BIP44AddressQWidget)
        self.BIP44AddressQLineEdit.setObjectName(u"BIP44AddressQLineEdit")
        self.BIP44AddressQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP44AddressVLayout.addWidget(self.BIP44AddressQLineEdit)


        self.BIP44HLayout.addWidget(self.BIP44AddressQWidget)

        self.DerivationsQTabWidget.addTab(self.BIP44QWidget, "")
        self.BIP49QWidget = QWidget()
        self.BIP49QWidget.setObjectName(u"BIP49QWidget")
        self.BIP49HLayout = QHBoxLayout(self.BIP49QWidget)
        self.BIP49HLayout.setSpacing(15)
        self.BIP49HLayout.setObjectName(u"BIP49HLayout")
        self.BIP49HLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49PurposeQWidget = QWidget(self.BIP49QWidget)
        self.BIP49PurposeQWidget.setObjectName(u"BIP49PurposeQWidget")
        self.BIP49PurposeVLayout = QVBoxLayout(self.BIP49PurposeQWidget)
        self.BIP49PurposeVLayout.setSpacing(5)
        self.BIP49PurposeVLayout.setObjectName(u"BIP49PurposeVLayout")
        self.BIP49PurposeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49PurposeLabelQWidget = QWidget(self.BIP49PurposeQWidget)
        self.BIP49PurposeLabelQWidget.setObjectName(u"BIP49PurposeLabelQWidget")
        self.BIP49PurposeLabelHLayout = QHBoxLayout(self.BIP49PurposeLabelQWidget)
        self.BIP49PurposeLabelHLayout.setSpacing(5)
        self.BIP49PurposeLabelHLayout.setObjectName(u"BIP49PurposeLabelHLayout")
        self.BIP49PurposeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49PurposeQLabel = QLabel(self.BIP49PurposeLabelQWidget)
        self.BIP49PurposeQLabel.setObjectName(u"BIP49PurposeQLabel")

        self.BIP49PurposeLabelHLayout.addWidget(self.BIP49PurposeQLabel)

        self.BIP49PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP49PurposeLabelHLayout.addItem(self.BIP49PurposeLabelHSpacer)


        self.BIP49PurposeVLayout.addWidget(self.BIP49PurposeLabelQWidget)

        self.BIP49PurposeQLineEdit = QLineEdit(self.BIP49PurposeQWidget)
        self.BIP49PurposeQLineEdit.setObjectName(u"BIP49PurposeQLineEdit")
        self.BIP49PurposeQLineEdit.setEnabled(False)
        self.BIP49PurposeQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP49PurposeVLayout.addWidget(self.BIP49PurposeQLineEdit)


        self.BIP49HLayout.addWidget(self.BIP49PurposeQWidget)

        self.BIP49CoinTypeQWidget = QWidget(self.BIP49QWidget)
        self.BIP49CoinTypeQWidget.setObjectName(u"BIP49CoinTypeQWidget")
        self.BIP49CoinTypeVLayout = QVBoxLayout(self.BIP49CoinTypeQWidget)
        self.BIP49CoinTypeVLayout.setSpacing(5)
        self.BIP49CoinTypeVLayout.setObjectName(u"BIP49CoinTypeVLayout")
        self.BIP49CoinTypeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49CoinTypeLabelQWidget = QWidget(self.BIP49CoinTypeQWidget)
        self.BIP49CoinTypeLabelQWidget.setObjectName(u"BIP49CoinTypeLabelQWidget")
        self.BIP49CoinTypeLabelHLayout = QHBoxLayout(self.BIP49CoinTypeLabelQWidget)
        self.BIP49CoinTypeLabelHLayout.setSpacing(5)
        self.BIP49CoinTypeLabelHLayout.setObjectName(u"BIP49CoinTypeLabelHLayout")
        self.BIP49CoinTypeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49CoinTypeQLabel = QLabel(self.BIP49CoinTypeLabelQWidget)
        self.BIP49CoinTypeQLabel.setObjectName(u"BIP49CoinTypeQLabel")

        self.BIP49CoinTypeLabelHLayout.addWidget(self.BIP49CoinTypeQLabel)

        self.BIP49CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP49CoinTypeLabelHLayout.addItem(self.BIP49CoinTypeLabelHSpacer)


        self.BIP49CoinTypeVLayout.addWidget(self.BIP49CoinTypeLabelQWidget)

        self.BIP49CoinTypeQLineEdit = QLineEdit(self.BIP49CoinTypeQWidget)
        self.BIP49CoinTypeQLineEdit.setObjectName(u"BIP49CoinTypeQLineEdit")
        self.BIP49CoinTypeQLineEdit.setEnabled(False)
        self.BIP49CoinTypeQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP49CoinTypeVLayout.addWidget(self.BIP49CoinTypeQLineEdit)


        self.BIP49HLayout.addWidget(self.BIP49CoinTypeQWidget)

        self.BIP49AccountQWidget = QWidget(self.BIP49QWidget)
        self.BIP49AccountQWidget.setObjectName(u"BIP49AccountQWidget")
        self.BIP49AccountVLayout = QVBoxLayout(self.BIP49AccountQWidget)
        self.BIP49AccountVLayout.setSpacing(5)
        self.BIP49AccountVLayout.setObjectName(u"BIP49AccountVLayout")
        self.BIP49AccountVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49AccountLabelQWidget = QWidget(self.BIP49AccountQWidget)
        self.BIP49AccountLabelQWidget.setObjectName(u"BIP49AccountLabelQWidget")
        self.BIP49AccountLabelHLayout = QHBoxLayout(self.BIP49AccountLabelQWidget)
        self.BIP49AccountLabelHLayout.setSpacing(5)
        self.BIP49AccountLabelHLayout.setObjectName(u"BIP49AccountLabelHLayout")
        self.BIP49AccountLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49AccountQLabel = QLabel(self.BIP49AccountLabelQWidget)
        self.BIP49AccountQLabel.setObjectName(u"BIP49AccountQLabel")

        self.BIP49AccountLabelHLayout.addWidget(self.BIP49AccountQLabel)

        self.BIP49AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP49AccountLabelHLayout.addItem(self.BIP49AccountLabelHSpacer)


        self.BIP49AccountVLayout.addWidget(self.BIP49AccountLabelQWidget)

        self.BIP49AccountQLineEdit = QLineEdit(self.BIP49AccountQWidget)
        self.BIP49AccountQLineEdit.setObjectName(u"BIP49AccountQLineEdit")
        self.BIP49AccountQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP49AccountVLayout.addWidget(self.BIP49AccountQLineEdit)


        self.BIP49HLayout.addWidget(self.BIP49AccountQWidget)

        self.BIP49ChangeQWidget = QWidget(self.BIP49QWidget)
        self.BIP49ChangeQWidget.setObjectName(u"BIP49ChangeQWidget")
        self.BIP49ChangeVLayout = QVBoxLayout(self.BIP49ChangeQWidget)
        self.BIP49ChangeVLayout.setSpacing(5)
        self.BIP49ChangeVLayout.setObjectName(u"BIP49ChangeVLayout")
        self.BIP49ChangeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49ChangeLabelQWidget = QWidget(self.BIP49ChangeQWidget)
        self.BIP49ChangeLabelQWidget.setObjectName(u"BIP49ChangeLabelQWidget")
        self.BIP49ChangeLabelHLayout = QHBoxLayout(self.BIP49ChangeLabelQWidget)
        self.BIP49ChangeLabelHLayout.setSpacing(5)
        self.BIP49ChangeLabelHLayout.setObjectName(u"BIP49ChangeLabelHLayout")
        self.BIP49ChangeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49ChangeQLabel = QLabel(self.BIP49ChangeLabelQWidget)
        self.BIP49ChangeQLabel.setObjectName(u"BIP49ChangeQLabel")

        self.BIP49ChangeLabelHLayout.addWidget(self.BIP49ChangeQLabel)

        self.BIP49ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP49ChangeLabelHLayout.addItem(self.BIP49ChangeLabelHSpacer)


        self.BIP49ChangeVLayout.addWidget(self.BIP49ChangeLabelQWidget)

        self.BIP49ChangeQComboBox = QComboBox(self.BIP49ChangeQWidget)
        self.BIP49ChangeQComboBox.addItem("")
        self.BIP49ChangeQComboBox.addItem("")
        self.BIP49ChangeQComboBox.setObjectName(u"BIP49ChangeQComboBox")
        self.BIP49ChangeQComboBox.setStyleSheet(u"padding: 0 10px;")

        self.BIP49ChangeVLayout.addWidget(self.BIP49ChangeQComboBox)


        self.BIP49HLayout.addWidget(self.BIP49ChangeQWidget)

        self.BIP49AddressQWidget = QWidget(self.BIP49QWidget)
        self.BIP49AddressQWidget.setObjectName(u"BIP49AddressQWidget")
        self.BIP49AddressVLayout = QVBoxLayout(self.BIP49AddressQWidget)
        self.BIP49AddressVLayout.setSpacing(5)
        self.BIP49AddressVLayout.setObjectName(u"BIP49AddressVLayout")
        self.BIP49AddressVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49AddressLabelQWidget = QWidget(self.BIP49AddressQWidget)
        self.BIP49AddressLabelQWidget.setObjectName(u"BIP49AddressLabelQWidget")
        self.BIP49AddressLabelHLayout = QHBoxLayout(self.BIP49AddressLabelQWidget)
        self.BIP49AddressLabelHLayout.setSpacing(5)
        self.BIP49AddressLabelHLayout.setObjectName(u"BIP49AddressLabelHLayout")
        self.BIP49AddressLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49AddressQLabel = QLabel(self.BIP49AddressLabelQWidget)
        self.BIP49AddressQLabel.setObjectName(u"BIP49AddressQLabel")

        self.BIP49AddressLabelHLayout.addWidget(self.BIP49AddressQLabel)

        self.BIP49AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP49AddressLabelHLayout.addItem(self.BIP49AddressLabelHSpacer)


        self.BIP49AddressVLayout.addWidget(self.BIP49AddressLabelQWidget)

        self.BIP49AddressQLineEdit = QLineEdit(self.BIP49AddressQWidget)
        self.BIP49AddressQLineEdit.setObjectName(u"BIP49AddressQLineEdit")
        self.BIP49AddressQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP49AddressVLayout.addWidget(self.BIP49AddressQLineEdit)


        self.BIP49HLayout.addWidget(self.BIP49AddressQWidget)

        self.DerivationsQTabWidget.addTab(self.BIP49QWidget, "")
        self.BIP84QWidget = QWidget()
        self.BIP84QWidget.setObjectName(u"BIP84QWidget")
        self.BIP84HLayout = QHBoxLayout(self.BIP84QWidget)
        self.BIP84HLayout.setSpacing(15)
        self.BIP84HLayout.setObjectName(u"BIP84HLayout")
        self.BIP84HLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84PurposeQWidget = QWidget(self.BIP84QWidget)
        self.BIP84PurposeQWidget.setObjectName(u"BIP84PurposeQWidget")
        self.BIP84PurposeVLayout = QVBoxLayout(self.BIP84PurposeQWidget)
        self.BIP84PurposeVLayout.setSpacing(5)
        self.BIP84PurposeVLayout.setObjectName(u"BIP84PurposeVLayout")
        self.BIP84PurposeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84PurposeLabelQWidget = QWidget(self.BIP84PurposeQWidget)
        self.BIP84PurposeLabelQWidget.setObjectName(u"BIP84PurposeLabelQWidget")
        self.BIP84PurposeLabelHLayout = QHBoxLayout(self.BIP84PurposeLabelQWidget)
        self.BIP84PurposeLabelHLayout.setSpacing(5)
        self.BIP84PurposeLabelHLayout.setObjectName(u"BIP84PurposeLabelHLayout")
        self.BIP84PurposeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84PurposeQLabel = QLabel(self.BIP84PurposeLabelQWidget)
        self.BIP84PurposeQLabel.setObjectName(u"BIP84PurposeQLabel")

        self.BIP84PurposeLabelHLayout.addWidget(self.BIP84PurposeQLabel)

        self.BIP84PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84PurposeLabelHLayout.addItem(self.BIP84PurposeLabelHSpacer)


        self.BIP84PurposeVLayout.addWidget(self.BIP84PurposeLabelQWidget)

        self.BIP84PurposeQLineEdit = QLineEdit(self.BIP84PurposeQWidget)
        self.BIP84PurposeQLineEdit.setObjectName(u"BIP84PurposeQLineEdit")
        self.BIP84PurposeQLineEdit.setEnabled(False)
        self.BIP84PurposeQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP84PurposeVLayout.addWidget(self.BIP84PurposeQLineEdit)


        self.BIP84HLayout.addWidget(self.BIP84PurposeQWidget)

        self.BIP84CoinTypeQWidget = QWidget(self.BIP84QWidget)
        self.BIP84CoinTypeQWidget.setObjectName(u"BIP84CoinTypeQWidget")
        self.BIP84CoinTypeVLayout = QVBoxLayout(self.BIP84CoinTypeQWidget)
        self.BIP84CoinTypeVLayout.setSpacing(5)
        self.BIP84CoinTypeVLayout.setObjectName(u"BIP84CoinTypeVLayout")
        self.BIP84CoinTypeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84CoinTypeLabelQWidget = QWidget(self.BIP84CoinTypeQWidget)
        self.BIP84CoinTypeLabelQWidget.setObjectName(u"BIP84CoinTypeLabelQWidget")
        self.BIP84CoinTypeLabelHLayout = QHBoxLayout(self.BIP84CoinTypeLabelQWidget)
        self.BIP84CoinTypeLabelHLayout.setSpacing(5)
        self.BIP84CoinTypeLabelHLayout.setObjectName(u"BIP84CoinTypeLabelHLayout")
        self.BIP84CoinTypeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84CoinTypeQLabel = QLabel(self.BIP84CoinTypeLabelQWidget)
        self.BIP84CoinTypeQLabel.setObjectName(u"BIP84CoinTypeQLabel")

        self.BIP84CoinTypeLabelHLayout.addWidget(self.BIP84CoinTypeQLabel)

        self.BIP84CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84CoinTypeLabelHLayout.addItem(self.BIP84CoinTypeLabelHSpacer)


        self.BIP84CoinTypeVLayout.addWidget(self.BIP84CoinTypeLabelQWidget)

        self.BIP84CoinTypeQLineEdit = QLineEdit(self.BIP84CoinTypeQWidget)
        self.BIP84CoinTypeQLineEdit.setObjectName(u"BIP84CoinTypeQLineEdit")
        self.BIP84CoinTypeQLineEdit.setEnabled(False)
        self.BIP84CoinTypeQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP84CoinTypeVLayout.addWidget(self.BIP84CoinTypeQLineEdit)


        self.BIP84HLayout.addWidget(self.BIP84CoinTypeQWidget)

        self.BIP84AccountQWidget = QWidget(self.BIP84QWidget)
        self.BIP84AccountQWidget.setObjectName(u"BIP84AccountQWidget")
        self.BIP84AccountVLayout = QVBoxLayout(self.BIP84AccountQWidget)
        self.BIP84AccountVLayout.setSpacing(5)
        self.BIP84AccountVLayout.setObjectName(u"BIP84AccountVLayout")
        self.BIP84AccountVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84AccountLabelQWidget = QWidget(self.BIP84AccountQWidget)
        self.BIP84AccountLabelQWidget.setObjectName(u"BIP84AccountLabelQWidget")
        self.BIP84AccountLabelHLayout = QHBoxLayout(self.BIP84AccountLabelQWidget)
        self.BIP84AccountLabelHLayout.setSpacing(5)
        self.BIP84AccountLabelHLayout.setObjectName(u"BIP84AccountLabelHLayout")
        self.BIP84AccountLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84AccountQLabel = QLabel(self.BIP84AccountLabelQWidget)
        self.BIP84AccountQLabel.setObjectName(u"BIP84AccountQLabel")

        self.BIP84AccountLabelHLayout.addWidget(self.BIP84AccountQLabel)

        self.BIP84AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84AccountLabelHLayout.addItem(self.BIP84AccountLabelHSpacer)


        self.BIP84AccountVLayout.addWidget(self.BIP84AccountLabelQWidget)

        self.BIP84AccountQLineEdit = QLineEdit(self.BIP84AccountQWidget)
        self.BIP84AccountQLineEdit.setObjectName(u"BIP84AccountQLineEdit")
        self.BIP84AccountQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP84AccountVLayout.addWidget(self.BIP84AccountQLineEdit)


        self.BIP84HLayout.addWidget(self.BIP84AccountQWidget)

        self.BIP84ChangeQWidget = QWidget(self.BIP84QWidget)
        self.BIP84ChangeQWidget.setObjectName(u"BIP84ChangeQWidget")
        self.BIP84ChangeVLayout = QVBoxLayout(self.BIP84ChangeQWidget)
        self.BIP84ChangeVLayout.setSpacing(5)
        self.BIP84ChangeVLayout.setObjectName(u"BIP84ChangeVLayout")
        self.BIP84ChangeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84ChangeLabelQWidget = QWidget(self.BIP84ChangeQWidget)
        self.BIP84ChangeLabelQWidget.setObjectName(u"BIP84ChangeLabelQWidget")
        self.BIP84ChangeLabelHLayout = QHBoxLayout(self.BIP84ChangeLabelQWidget)
        self.BIP84ChangeLabelHLayout.setSpacing(5)
        self.BIP84ChangeLabelHLayout.setObjectName(u"BIP84ChangeLabelHLayout")
        self.BIP84ChangeLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84ChangeQLabel = QLabel(self.BIP84ChangeLabelQWidget)
        self.BIP84ChangeQLabel.setObjectName(u"BIP84ChangeQLabel")

        self.BIP84ChangeLabelHLayout.addWidget(self.BIP84ChangeQLabel)

        self.BIP84ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84ChangeLabelHLayout.addItem(self.BIP84ChangeLabelHSpacer)


        self.BIP84ChangeVLayout.addWidget(self.BIP84ChangeLabelQWidget)

        self.BIP84ChangeQComboBox = QComboBox(self.BIP84ChangeQWidget)
        self.BIP84ChangeQComboBox.addItem("")
        self.BIP84ChangeQComboBox.addItem("")
        self.BIP84ChangeQComboBox.setObjectName(u"BIP84ChangeQComboBox")
        self.BIP84ChangeQComboBox.setStyleSheet(u"padding: 0 10px;")

        self.BIP84ChangeVLayout.addWidget(self.BIP84ChangeQComboBox)


        self.BIP84HLayout.addWidget(self.BIP84ChangeQWidget)

        self.BIP84AddressQWidget = QWidget(self.BIP84QWidget)
        self.BIP84AddressQWidget.setObjectName(u"BIP84AddressQWidget")
        self.BIP84AddressVLayout = QVBoxLayout(self.BIP84AddressQWidget)
        self.BIP84AddressVLayout.setSpacing(5)
        self.BIP84AddressVLayout.setObjectName(u"BIP84AddressVLayout")
        self.BIP84AddressVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84AddressLabelQWidget = QWidget(self.BIP84AddressQWidget)
        self.BIP84AddressLabelQWidget.setObjectName(u"BIP84AddressLabelQWidget")
        self.BIP84AddressLabelHLayout = QHBoxLayout(self.BIP84AddressLabelQWidget)
        self.BIP84AddressLabelHLayout.setSpacing(5)
        self.BIP84AddressLabelHLayout.setObjectName(u"BIP84AddressLabelHLayout")
        self.BIP84AddressLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84AddressQLabel = QLabel(self.BIP84AddressLabelQWidget)
        self.BIP84AddressQLabel.setObjectName(u"BIP84AddressQLabel")

        self.BIP84AddressLabelHLayout.addWidget(self.BIP84AddressQLabel)

        self.BIP84AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP84AddressLabelHLayout.addItem(self.BIP84AddressLabelHSpacer)


        self.BIP84AddressVLayout.addWidget(self.BIP84AddressLabelQWidget)

        self.BIP84AddressQLineEdit = QLineEdit(self.BIP84AddressQWidget)
        self.BIP84AddressQLineEdit.setObjectName(u"BIP84AddressQLineEdit")
        self.BIP84AddressQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP84AddressVLayout.addWidget(self.BIP84AddressQLineEdit)


        self.BIP84HLayout.addWidget(self.BIP84AddressQWidget)

        self.DerivationsQTabWidget.addTab(self.BIP84QWidget, "")
        self.CIP1852QWidget = QWidget()
        self.CIP1852QWidget.setObjectName(u"CIP1852QWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.CIP1852QWidget)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.CIP1852PurposeQWidget = QWidget(self.CIP1852QWidget)
        self.CIP1852PurposeQWidget.setObjectName(u"CIP1852PurposeQWidget")
        self.BIP44PurposeVLayout_2 = QVBoxLayout(self.CIP1852PurposeQWidget)
        self.BIP44PurposeVLayout_2.setSpacing(5)
        self.BIP44PurposeVLayout_2.setObjectName(u"BIP44PurposeVLayout_2")
        self.BIP44PurposeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852PurposeLabelQWidget = QWidget(self.CIP1852PurposeQWidget)
        self.CIP1852PurposeLabelQWidget.setObjectName(u"CIP1852PurposeLabelQWidget")
        self.BIP44PurposeLabelHLayout_2 = QHBoxLayout(self.CIP1852PurposeLabelQWidget)
        self.BIP44PurposeLabelHLayout_2.setSpacing(5)
        self.BIP44PurposeLabelHLayout_2.setObjectName(u"BIP44PurposeLabelHLayout_2")
        self.BIP44PurposeLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852PurposeQLabel = QLabel(self.CIP1852PurposeLabelQWidget)
        self.CIP1852PurposeQLabel.setObjectName(u"CIP1852PurposeQLabel")

        self.BIP44PurposeLabelHLayout_2.addWidget(self.CIP1852PurposeQLabel)

        self.CIP1852PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44PurposeLabelHLayout_2.addItem(self.CIP1852PurposeLabelHSpacer)


        self.BIP44PurposeVLayout_2.addWidget(self.CIP1852PurposeLabelQWidget)

        self.CIP1852PurposeQLineEdit = QLineEdit(self.CIP1852PurposeQWidget)
        self.CIP1852PurposeQLineEdit.setObjectName(u"CIP1852PurposeQLineEdit")
        self.CIP1852PurposeQLineEdit.setEnabled(False)
        self.CIP1852PurposeQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP44PurposeVLayout_2.addWidget(self.CIP1852PurposeQLineEdit)


        self.horizontalLayout_5.addWidget(self.CIP1852PurposeQWidget)

        self.CIP1852CoinTypeQWidget = QWidget(self.CIP1852QWidget)
        self.CIP1852CoinTypeQWidget.setObjectName(u"CIP1852CoinTypeQWidget")
        self.BIP44CoinTypeVLayout_2 = QVBoxLayout(self.CIP1852CoinTypeQWidget)
        self.BIP44CoinTypeVLayout_2.setSpacing(5)
        self.BIP44CoinTypeVLayout_2.setObjectName(u"BIP44CoinTypeVLayout_2")
        self.BIP44CoinTypeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852CoinTypeLabelQWidget = QWidget(self.CIP1852CoinTypeQWidget)
        self.CIP1852CoinTypeLabelQWidget.setObjectName(u"CIP1852CoinTypeLabelQWidget")
        self.BIP44CoinTypeLabelHLayout_2 = QHBoxLayout(self.CIP1852CoinTypeLabelQWidget)
        self.BIP44CoinTypeLabelHLayout_2.setSpacing(5)
        self.BIP44CoinTypeLabelHLayout_2.setObjectName(u"BIP44CoinTypeLabelHLayout_2")
        self.BIP44CoinTypeLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852CoinTypeQLabel = QLabel(self.CIP1852CoinTypeLabelQWidget)
        self.CIP1852CoinTypeQLabel.setObjectName(u"CIP1852CoinTypeQLabel")

        self.BIP44CoinTypeLabelHLayout_2.addWidget(self.CIP1852CoinTypeQLabel)

        self.CIP1852CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44CoinTypeLabelHLayout_2.addItem(self.CIP1852CoinTypeLabelHSpacer)


        self.BIP44CoinTypeVLayout_2.addWidget(self.CIP1852CoinTypeLabelQWidget)

        self.CIP1852CoinTypeQLineEdit = QLineEdit(self.CIP1852CoinTypeQWidget)
        self.CIP1852CoinTypeQLineEdit.setObjectName(u"CIP1852CoinTypeQLineEdit")
        self.CIP1852CoinTypeQLineEdit.setEnabled(False)
        self.CIP1852CoinTypeQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP44CoinTypeVLayout_2.addWidget(self.CIP1852CoinTypeQLineEdit)


        self.horizontalLayout_5.addWidget(self.CIP1852CoinTypeQWidget)

        self.CIP1852AccountQWidget = QWidget(self.CIP1852QWidget)
        self.CIP1852AccountQWidget.setObjectName(u"CIP1852AccountQWidget")
        self.BIP44AccountVLayout_2 = QVBoxLayout(self.CIP1852AccountQWidget)
        self.BIP44AccountVLayout_2.setSpacing(5)
        self.BIP44AccountVLayout_2.setObjectName(u"BIP44AccountVLayout_2")
        self.BIP44AccountVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852AccountLabelQWidget = QWidget(self.CIP1852AccountQWidget)
        self.CIP1852AccountLabelQWidget.setObjectName(u"CIP1852AccountLabelQWidget")
        self.BIP44AccountLabelHLayout_2 = QHBoxLayout(self.CIP1852AccountLabelQWidget)
        self.BIP44AccountLabelHLayout_2.setSpacing(5)
        self.BIP44AccountLabelHLayout_2.setObjectName(u"BIP44AccountLabelHLayout_2")
        self.BIP44AccountLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852AccountQLabel = QLabel(self.CIP1852AccountLabelQWidget)
        self.CIP1852AccountQLabel.setObjectName(u"CIP1852AccountQLabel")

        self.BIP44AccountLabelHLayout_2.addWidget(self.CIP1852AccountQLabel)

        self.CIP1852AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AccountLabelHLayout_2.addItem(self.CIP1852AccountLabelHSpacer)


        self.BIP44AccountVLayout_2.addWidget(self.CIP1852AccountLabelQWidget)

        self.CIP1852AccountQLineEdit = QLineEdit(self.CIP1852AccountQWidget)
        self.CIP1852AccountQLineEdit.setObjectName(u"CIP1852AccountQLineEdit")
        self.CIP1852AccountQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP44AccountVLayout_2.addWidget(self.CIP1852AccountQLineEdit)


        self.horizontalLayout_5.addWidget(self.CIP1852AccountQWidget)

        self.CIP1852ChangeQWidget = QWidget(self.CIP1852QWidget)
        self.CIP1852ChangeQWidget.setObjectName(u"CIP1852ChangeQWidget")
        self.BIP44ChangeVLayout_2 = QVBoxLayout(self.CIP1852ChangeQWidget)
        self.BIP44ChangeVLayout_2.setSpacing(5)
        self.BIP44ChangeVLayout_2.setObjectName(u"BIP44ChangeVLayout_2")
        self.BIP44ChangeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852ChangeLabelQWidget = QWidget(self.CIP1852ChangeQWidget)
        self.CIP1852ChangeLabelQWidget.setObjectName(u"CIP1852ChangeLabelQWidget")
        self.BIP44ChangeLabelHLayout_2 = QHBoxLayout(self.CIP1852ChangeLabelQWidget)
        self.BIP44ChangeLabelHLayout_2.setSpacing(5)
        self.BIP44ChangeLabelHLayout_2.setObjectName(u"BIP44ChangeLabelHLayout_2")
        self.BIP44ChangeLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852ChangeQLabel = QLabel(self.CIP1852ChangeLabelQWidget)
        self.CIP1852ChangeQLabel.setObjectName(u"CIP1852ChangeQLabel")

        self.BIP44ChangeLabelHLayout_2.addWidget(self.CIP1852ChangeQLabel)

        self.CIP1852ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44ChangeLabelHLayout_2.addItem(self.CIP1852ChangeLabelHSpacer)


        self.BIP44ChangeVLayout_2.addWidget(self.CIP1852ChangeLabelQWidget)

        self.CIP1852ChangeQComboBox = QComboBox(self.CIP1852ChangeQWidget)
        self.CIP1852ChangeQComboBox.addItem("")
        self.CIP1852ChangeQComboBox.addItem("")
        self.CIP1852ChangeQComboBox.addItem("")
        self.CIP1852ChangeQComboBox.setObjectName(u"CIP1852ChangeQComboBox")
        self.CIP1852ChangeQComboBox.setStyleSheet(u"padding: 0 10px;")

        self.BIP44ChangeVLayout_2.addWidget(self.CIP1852ChangeQComboBox)


        self.horizontalLayout_5.addWidget(self.CIP1852ChangeQWidget)

        self.CIP1852AddressQWidget = QWidget(self.CIP1852QWidget)
        self.CIP1852AddressQWidget.setObjectName(u"CIP1852AddressQWidget")
        self.BIP44AddressVLayout_2 = QVBoxLayout(self.CIP1852AddressQWidget)
        self.BIP44AddressVLayout_2.setSpacing(5)
        self.BIP44AddressVLayout_2.setObjectName(u"BIP44AddressVLayout_2")
        self.BIP44AddressVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852AddressLabelQWidget = QWidget(self.CIP1852AddressQWidget)
        self.CIP1852AddressLabelQWidget.setObjectName(u"CIP1852AddressLabelQWidget")
        self.BIP44AddressLabelHLayout_2 = QHBoxLayout(self.CIP1852AddressLabelQWidget)
        self.BIP44AddressLabelHLayout_2.setSpacing(5)
        self.BIP44AddressLabelHLayout_2.setObjectName(u"BIP44AddressLabelHLayout_2")
        self.BIP44AddressLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852AddressQLabel = QLabel(self.CIP1852AddressLabelQWidget)
        self.CIP1852AddressQLabel.setObjectName(u"CIP1852AddressQLabel")

        self.BIP44AddressLabelHLayout_2.addWidget(self.CIP1852AddressQLabel)

        self.CIP1852AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AddressLabelHLayout_2.addItem(self.CIP1852AddressLabelHSpacer)


        self.BIP44AddressVLayout_2.addWidget(self.CIP1852AddressLabelQWidget)

        self.CIP1852AddressQLineEdit = QLineEdit(self.CIP1852AddressQWidget)
        self.CIP1852AddressQLineEdit.setObjectName(u"CIP1852AddressQLineEdit")
        self.CIP1852AddressQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP44AddressVLayout_2.addWidget(self.CIP1852AddressQLineEdit)


        self.horizontalLayout_5.addWidget(self.CIP1852AddressQWidget)

        self.DerivationsQTabWidget.addTab(self.CIP1852QWidget, "")
        self.BIP141QWidget = QWidget()
        self.BIP141QWidget.setObjectName(u"BIP141QWidget")
        self.BIP141HLayout = QHBoxLayout(self.BIP141QWidget)
        self.BIP141HLayout.setSpacing(15)
        self.BIP141HLayout.setObjectName(u"BIP141HLayout")
        self.BIP141HLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP141PathQWidget = QWidget(self.BIP141QWidget)
        self.BIP141PathQWidget.setObjectName(u"BIP141PathQWidget")
        self.BIP141PathVLayout = QVBoxLayout(self.BIP141PathQWidget)
        self.BIP141PathVLayout.setSpacing(5)
        self.BIP141PathVLayout.setObjectName(u"BIP141PathVLayout")
        self.BIP141PathVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP141PathLabelQWidget = QWidget(self.BIP141PathQWidget)
        self.BIP141PathLabelQWidget.setObjectName(u"BIP141PathLabelQWidget")
        self.BIP141PathLabelHLayout = QHBoxLayout(self.BIP141PathLabelQWidget)
        self.BIP141PathLabelHLayout.setSpacing(5)
        self.BIP141PathLabelHLayout.setObjectName(u"BIP141PathLabelHLayout")
        self.BIP141PathLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP141PathQLabel = QLabel(self.BIP141PathLabelQWidget)
        self.BIP141PathQLabel.setObjectName(u"BIP141PathQLabel")

        self.BIP141PathLabelHLayout.addWidget(self.BIP141PathQLabel)

        self.BIP141PathLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP141PathLabelHLayout.addItem(self.BIP141PathLabelHSpacer)


        self.BIP141PathVLayout.addWidget(self.BIP141PathLabelQWidget)

        self.BIP141PathQLineEdit = QLineEdit(self.BIP141PathQWidget)
        self.BIP141PathQLineEdit.setObjectName(u"BIP141PathQLineEdit")
        self.BIP141PathQLineEdit.setStyleSheet(u"padding: 0 10px;")

        self.BIP141PathVLayout.addWidget(self.BIP141PathQLineEdit)


        self.BIP141HLayout.addWidget(self.BIP141PathQWidget)

        self.BIP141ScriptSemanticsQWidget = QWidget(self.BIP141QWidget)
        self.BIP141ScriptSemanticsQWidget.setObjectName(u"BIP141ScriptSemanticsQWidget")
        self.BIP141ScriptSemanticsVLayout = QVBoxLayout(self.BIP141ScriptSemanticsQWidget)
        self.BIP141ScriptSemanticsVLayout.setSpacing(5)
        self.BIP141ScriptSemanticsVLayout.setObjectName(u"BIP141ScriptSemanticsVLayout")
        self.BIP141ScriptSemanticsVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP141ScriptSemanticsLabelQWidget = QWidget(self.BIP141ScriptSemanticsQWidget)
        self.BIP141ScriptSemanticsLabelQWidget.setObjectName(u"BIP141ScriptSemanticsLabelQWidget")
        self.BIP141ScriptSemanticsLabelHLayout = QHBoxLayout(self.BIP141ScriptSemanticsLabelQWidget)
        self.BIP141ScriptSemanticsLabelHLayout.setSpacing(5)
        self.BIP141ScriptSemanticsLabelHLayout.setObjectName(u"BIP141ScriptSemanticsLabelHLayout")
        self.BIP141ScriptSemanticsLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP141ScriptSemanticsQLabel = QLabel(self.BIP141ScriptSemanticsLabelQWidget)
        self.BIP141ScriptSemanticsQLabel.setObjectName(u"BIP141ScriptSemanticsQLabel")

        self.BIP141ScriptSemanticsLabelHLayout.addWidget(self.BIP141ScriptSemanticsQLabel)

        self.BIP141ScriptSemanticsLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP141ScriptSemanticsLabelHLayout.addItem(self.BIP141ScriptSemanticsLabelHSpacer)


        self.BIP141ScriptSemanticsVLayout.addWidget(self.BIP141ScriptSemanticsLabelQWidget)

        self.BIP141ScriptSemanticsQComboBox = QComboBox(self.BIP141ScriptSemanticsQWidget)
        self.BIP141ScriptSemanticsQComboBox.addItem("")
        self.BIP141ScriptSemanticsQComboBox.addItem("")
        self.BIP141ScriptSemanticsQComboBox.addItem("")
        self.BIP141ScriptSemanticsQComboBox.addItem("")
        self.BIP141ScriptSemanticsQComboBox.setObjectName(u"BIP141ScriptSemanticsQComboBox")
        self.BIP141ScriptSemanticsQComboBox.setStyleSheet(u"padding: 0 10px;")

        self.BIP141ScriptSemanticsVLayout.addWidget(self.BIP141ScriptSemanticsQComboBox)


        self.BIP141HLayout.addWidget(self.BIP141ScriptSemanticsQWidget)

        self.DerivationsQTabWidget.addTab(self.BIP141QWidget, "")

        self.DerivationVLayout.addWidget(self.DerivationsQTabWidget)


        self.verticalLayout_3.addWidget(self.DerivationQWidget)


        self.verticalLayout.addWidget(self.frame_5)

        self.ActionsQWidget = QWidget(self.frame)
        self.ActionsQWidget.setObjectName(u"ActionsQWidget")
        self.ActionsQWidget.setMaximumSize(QSize(16777215, 60))
        self.ActionsHLayout = QHBoxLayout(self.ActionsQWidget)
        self.ActionsHLayout.setSpacing(15)
        self.ActionsHLayout.setObjectName(u"ActionsHLayout")
        self.ActionsHLayout.setContentsMargins(0, 15, 0, 10)
        self.OutputQLabel = QLabel(self.ActionsQWidget)
        self.OutputQLabel.setObjectName(u"OutputQLabel")

        self.ActionsHLayout.addWidget(self.OutputQLabel)

        self.ActionsHSpacer = QSpacerItem(560, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ActionsHLayout.addItem(self.ActionsHSpacer)

        self.GenerateQPushButton = QPushButton(self.ActionsQWidget)
        self.GenerateQPushButton.setObjectName(u"GenerateQPushButton")
        self.GenerateQPushButton.setStyleSheet(u"")

        self.ActionsHLayout.addWidget(self.GenerateQPushButton)

        self.CopyQPushButton = QPushButton(self.ActionsQWidget)
        self.CopyQPushButton.setObjectName(u"CopyQPushButton")

        self.ActionsHLayout.addWidget(self.CopyQPushButton)

        self.ClearQPushButton = QPushButton(self.ActionsQWidget)
        self.ClearQPushButton.setObjectName(u"ClearQPushButton")

        self.ActionsHLayout.addWidget(self.ClearQPushButton)

        self.SaveAsQPushButton = QPushButton(self.ActionsQWidget)
        self.SaveAsQPushButton.setObjectName(u"SaveAsQPushButton")

        self.ActionsHLayout.addWidget(self.SaveAsQPushButton)


        self.verticalLayout.addWidget(self.ActionsQWidget)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.horizontalLayout.addWidget(self.frame)

        self.outputQFrame = QFrame(self.centralwidget)
        self.outputQFrame.setObjectName(u"outputQFrame")
        self.outputQFrame.setMinimumSize(QSize(200, 0))
        self.outputQFrame.setFrameShape(QFrame.StyledPanel)
        self.outputQFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.outputQFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addWidget(self.outputQFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1123, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuDonation = QMenu(self.menubar)
        self.menuDonation.setObjectName(u"menuDonation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuDonation.menuAction())

        self.retranslateUi(MainWindow)

        self.fromQStackedWidget.setCurrentIndex(0)
        self.DerivationsQTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HD", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.EntropyQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.EGenerateQPushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
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

        self.EPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.EPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.MnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.MGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
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

        self.MPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.MPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.SeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.XPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.XPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.WIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.BIP38EncryptedWIFQCheckBox.setText(QCoreApplication.translate("MainWindow", u"BIP38 Encrypted WIF", None))
        self.BIP38EncryptedWIFPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"BIP 38 Passphrase", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.PrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.PublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.ClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.ClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.CryptocurrencyLabelQLabel.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.CryptocurrencyQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"BTC - Bitcoin", None))
        self.CryptocurrencyQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BTC - Bitcoin Testnet", None))
        self.CryptocurrencyQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"QTUM - Qtum", None))
        self.CryptocurrencyQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"QTUM - Qtum Testnet", None))

        self.FormatLabelQLabel.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.FormatQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"JSON", None))
        self.FormatQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CSV", None))

        self.KeysQLabel.setText(QCoreApplication.translate("MainWindow", u"Keys", None))
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
        self.BIP44PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"44'", None))
        self.BIP44CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.BIP44CoinTypeQLineEdit.setText("")
        self.BIP44CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0'", None))
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
        self.BIP49PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"49'", None))
        self.BIP49CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.BIP49CoinTypeQLineEdit.setText("")
        self.BIP49CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0'", None))
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
        self.BIP84PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"84'", None))
        self.BIP84CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.BIP84CoinTypeQLineEdit.setText("")
        self.BIP84CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0'", None))
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
        self.CIP1852PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.CIP1852PurposeQLineEdit.setText("")
        self.CIP1852PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1852'", None))
        self.CIP1852CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.CIP1852CoinTypeQLineEdit.setText("")
        self.CIP1852CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1815'", None))
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
        self.BIP141PathQLabel.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.BIP141PathQLineEdit.setText("")
        self.BIP141PathQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"m/0'/0", None))
        self.BIP141ScriptSemanticsQLabel.setText(QCoreApplication.translate("MainWindow", u"Script Semantics", None))
        self.BIP141ScriptSemanticsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"P2WPKH", None))
        self.BIP141ScriptSemanticsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"P2WPKH nested in P2SH", None))
        self.BIP141ScriptSemanticsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"P2WSH (1-of-1 multisig)", None))
        self.BIP141ScriptSemanticsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"P2WSH nested in P2SH (1-of-1 multisig)", None))

        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.BIP141QWidget), QCoreApplication.translate("MainWindow", u"BIP141", None))
        self.OutputQLabel.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.GenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.CopyQPushButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.ClearQPushButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.SaveAsQPushButton.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuDonation.setTitle(QCoreApplication.translate("MainWindow", u"Donation", None))
    # retranslateUi

