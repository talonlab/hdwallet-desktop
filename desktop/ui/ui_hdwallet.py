# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hdwalletvSSxGy.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

from desktop.widgets.history_lineedit import HistoryLineEdit
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 575)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidgetHLayout = QHBoxLayout(self.centralwidget)
        self.centralwidgetHLayout.setSpacing(0)
        self.centralwidgetHLayout.setObjectName(u"centralwidgetHLayout")
        self.centralwidgetHLayout.setContentsMargins(0, 0, 0, 0)
        self.hdWalletContainerQFrame = QFrame(self.centralwidget)
        self.hdWalletContainerQFrame.setObjectName(u"hdWalletContainerQFrame")
        self.hdWalletContainerQFrame.setMinimumSize(QSize(750, 0))
        self.hdWalletContainerQFrame.setMaximumSize(QSize(750, 16777215))
        self.hdWalletContainerQFrame.setFrameShadow(QFrame.Raised)
        self.hdWalletContainerQFrameVLayout = QVBoxLayout(self.hdWalletContainerQFrame)
        self.hdWalletContainerQFrameVLayout.setSpacing(0)
        self.hdWalletContainerQFrameVLayout.setObjectName(u"hdWalletContainerQFrameVLayout")
        self.hdWalletContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.hdWalletHeaderContainerQFrame = QFrame(self.hdWalletContainerQFrame)
        self.hdWalletHeaderContainerQFrame.setObjectName(u"hdWalletHeaderContainerQFrame")
        self.hdWalletHeaderContainerQFrameHLayout = QHBoxLayout(self.hdWalletHeaderContainerQFrame)
        self.hdWalletHeaderContainerQFrameHLayout.setSpacing(15)
        self.hdWalletHeaderContainerQFrameHLayout.setObjectName(u"hdWalletHeaderContainerQFrameHLayout")
        self.hdWalletHeaderContainerQFrameHLayout.setContentsMargins(15, 15, 15, 15)
        self.hdwalletLogoHLayout = QHBoxLayout()
        self.hdwalletLogoHLayout.setObjectName(u"hdwalletLogoHLayout")

        self.hdWalletHeaderContainerQFrameHLayout.addLayout(self.hdwalletLogoHLayout)

        self.hdWalletHeaderContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hdWalletHeaderContainerQFrameHLayout.addItem(self.hdWalletHeaderContainerQFrameHSpacer)

        self.generateAndDumpTabContainerQFrame = QFrame(self.hdWalletHeaderContainerQFrame)
        self.generateAndDumpTabContainerQFrame.setObjectName(u"generateAndDumpTabContainerQFrame")
        self.horizontalLayout_11 = QHBoxLayout(self.generateAndDumpTabContainerQFrame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.generateQPushButton = QPushButton(self.generateAndDumpTabContainerQFrame)
        self.generateQPushButton.setObjectName(u"generateQPushButton")

        self.horizontalLayout_11.addWidget(self.generateQPushButton)

        self.dumpQPushButton = QPushButton(self.generateAndDumpTabContainerQFrame)
        self.dumpQPushButton.setObjectName(u"dumpQPushButton")

        self.horizontalLayout_11.addWidget(self.dumpQPushButton)


        self.hdWalletHeaderContainerQFrameHLayout.addWidget(self.generateAndDumpTabContainerQFrame)

        self.donationHDWalletQPushButton = QPushButton(self.hdWalletHeaderContainerQFrame)
        self.donationHDWalletQPushButton.setObjectName(u"donationHDWalletQPushButton")

        self.hdWalletHeaderContainerQFrameHLayout.addWidget(self.donationHDWalletQPushButton)

        self.helpHDWalletQPushButton = QPushButton(self.hdWalletHeaderContainerQFrame)
        self.helpHDWalletQPushButton.setObjectName(u"helpHDWalletQPushButton")

        self.hdWalletHeaderContainerQFrameHLayout.addWidget(self.helpHDWalletQPushButton)


        self.hdWalletContainerQFrameVLayout.addWidget(self.hdWalletHeaderContainerQFrame)

        self.hdwalletMainQFrame = QFrame(self.hdWalletContainerQFrame)
        self.hdwalletMainQFrame.setObjectName(u"hdwalletMainQFrame")
        self.hdwalletMainQFrameVLayout = QVBoxLayout(self.hdwalletMainQFrame)
        self.hdwalletMainQFrameVLayout.setSpacing(0)
        self.hdwalletMainQFrameVLayout.setObjectName(u"hdwalletMainQFrameVLayout")
        self.hdwalletMainQFrameVLayout.setContentsMargins(15, 0, 15, 15)
        self.hdwalletQStackedWidget = QStackedWidget(self.hdwalletMainQFrame)
        self.hdwalletQStackedWidget.setObjectName(u"hdwalletQStackedWidget")
        self.generatePageQStackedWidget = QWidget()
        self.generatePageQStackedWidget.setObjectName(u"generatePageQStackedWidget")
        self.generatePageQStackedWidgetVLayout = QVBoxLayout(self.generatePageQStackedWidget)
        self.generatePageQStackedWidgetVLayout.setSpacing(10)
        self.generatePageQStackedWidgetVLayout.setObjectName(u"generatePageQStackedWidgetVLayout")
        self.generatePageQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateEntopyClientAndStrengthContainerQFrame = QFrame(self.generatePageQStackedWidget)
        self.generateEntopyClientAndStrengthContainerQFrame.setObjectName(u"generateEntopyClientAndStrengthContainerQFrame")
        self.generateEntopyClientAndStrengthContainerQFrame.setLineWidth(0)
        self.generateEntopyClientAndStrengthContainerQFrameVLayout = QVBoxLayout(self.generateEntopyClientAndStrengthContainerQFrame)
        self.generateEntopyClientAndStrengthContainerQFrameVLayout.setSpacing(15)
        self.generateEntopyClientAndStrengthContainerQFrameVLayout.setObjectName(u"generateEntopyClientAndStrengthContainerQFrameVLayout")
        self.generateEntopyClientAndStrengthContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateClientAndStrengthContainerQGroupBox = QGroupBox(self.generateEntopyClientAndStrengthContainerQFrame)
        self.generateClientAndStrengthContainerQGroupBox.setObjectName(u"generateClientAndStrengthContainerQGroupBox")
        self.generateClientAndStrengthContainerQFrameHLayout = QHBoxLayout(self.generateClientAndStrengthContainerQGroupBox)
        self.generateClientAndStrengthContainerQFrameHLayout.setSpacing(15)
        self.generateClientAndStrengthContainerQFrameHLayout.setObjectName(u"generateClientAndStrengthContainerQFrameHLayout")
        self.generateClientAndStrengthContainerQFrameHLayout.setContentsMargins(10, 15, 10, 10)
        self.generateEntropyClientContainerQFrame = QFrame(self.generateClientAndStrengthContainerQGroupBox)
        self.generateEntropyClientContainerQFrame.setObjectName(u"generateEntropyClientContainerQFrame")
        self.generateEntropyClientContainerQFrameVLayout = QVBoxLayout(self.generateEntropyClientContainerQFrame)
        self.generateEntropyClientContainerQFrameVLayout.setSpacing(5)
        self.generateEntropyClientContainerQFrameVLayout.setObjectName(u"generateEntropyClientContainerQFrameVLayout")
        self.generateEntropyClientContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateEntropyClientQLabel = QLabel(self.generateEntropyClientContainerQFrame)
        self.generateEntropyClientQLabel.setObjectName(u"generateEntropyClientQLabel")

        self.generateEntropyClientContainerQFrameVLayout.addWidget(self.generateEntropyClientQLabel)

        self.generateEntropyClientQComboBox = QComboBox(self.generateEntropyClientContainerQFrame)
        self.generateEntropyClientQComboBox.setObjectName(u"generateEntropyClientQComboBox")

        self.generateEntropyClientContainerQFrameVLayout.addWidget(self.generateEntropyClientQComboBox)


        self.generateClientAndStrengthContainerQFrameHLayout.addWidget(self.generateEntropyClientContainerQFrame)

        self.generateEntropyStrengthContainerQFrame = QFrame(self.generateClientAndStrengthContainerQGroupBox)
        self.generateEntropyStrengthContainerQFrame.setObjectName(u"generateEntropyStrengthContainerQFrame")
        self.generateEntropyStrengthContainerQFrameVLayout = QVBoxLayout(self.generateEntropyStrengthContainerQFrame)
        self.generateEntropyStrengthContainerQFrameVLayout.setSpacing(5)
        self.generateEntropyStrengthContainerQFrameVLayout.setObjectName(u"generateEntropyStrengthContainerQFrameVLayout")
        self.generateEntropyStrengthContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateEntropyStrengthQLabel = QLabel(self.generateEntropyStrengthContainerQFrame)
        self.generateEntropyStrengthQLabel.setObjectName(u"generateEntropyStrengthQLabel")

        self.generateEntropyStrengthContainerQFrameVLayout.addWidget(self.generateEntropyStrengthQLabel)

        self.generateEntropyStrengthQComboBox = QComboBox(self.generateEntropyStrengthContainerQFrame)
        self.generateEntropyStrengthQComboBox.setObjectName(u"generateEntropyStrengthQComboBox")
        self.generateEntropyStrengthQComboBox.setMinimumSize(QSize(275, 0))

        self.generateEntropyStrengthContainerQFrameVLayout.addWidget(self.generateEntropyStrengthQComboBox)


        self.generateClientAndStrengthContainerQFrameHLayout.addWidget(self.generateEntropyStrengthContainerQFrame)

        self.generateEntropyClientAndStrengthQPushButton = QPushButton(self.generateClientAndStrengthContainerQGroupBox)
        self.generateEntropyClientAndStrengthQPushButton.setObjectName(u"generateEntropyClientAndStrengthQPushButton")
        self.generateEntropyClientAndStrengthQPushButton.setMaximumSize(QSize(100, 16777215))

        self.generateClientAndStrengthContainerQFrameHLayout.addWidget(self.generateEntropyClientAndStrengthQPushButton, 0, Qt.AlignBottom)


        self.generateEntopyClientAndStrengthContainerQFrameVLayout.addWidget(self.generateClientAndStrengthContainerQGroupBox)


        self.generatePageQStackedWidgetVLayout.addWidget(self.generateEntopyClientAndStrengthContainerQFrame)

        self.generateMnemonicClientWordsLanguageContainerQGroupBox = QGroupBox(self.generatePageQStackedWidget)
        self.generateMnemonicClientWordsLanguageContainerQGroupBox.setObjectName(u"generateMnemonicClientWordsLanguageContainerQGroupBox")
        self.verticalLayout_6 = QVBoxLayout(self.generateMnemonicClientWordsLanguageContainerQGroupBox)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 15, 10, 10)
        self.generateMnemonicClientFromLanguageContainerQFrame = QFrame(self.generateMnemonicClientWordsLanguageContainerQGroupBox)
        self.generateMnemonicClientFromLanguageContainerQFrame.setObjectName(u"generateMnemonicClientFromLanguageContainerQFrame")
        self.generateMnemonicClientFromLanguageContainerQFrameHLayout = QHBoxLayout(self.generateMnemonicClientFromLanguageContainerQFrame)
        self.generateMnemonicClientFromLanguageContainerQFrameHLayout.setSpacing(15)
        self.generateMnemonicClientFromLanguageContainerQFrameHLayout.setObjectName(u"generateMnemonicClientFromLanguageContainerQFrameHLayout")
        self.generateMnemonicClientFromLanguageContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicClientContainerQFrame = QFrame(self.generateMnemonicClientFromLanguageContainerQFrame)
        self.generateMnemonicClientContainerQFrame.setObjectName(u"generateMnemonicClientContainerQFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateMnemonicClientContainerQFrame.sizePolicy().hasHeightForWidth())
        self.generateMnemonicClientContainerQFrame.setSizePolicy(sizePolicy)
        self.generateMnemonicClientContainerQFrameVLayout = QVBoxLayout(self.generateMnemonicClientContainerQFrame)
        self.generateMnemonicClientContainerQFrameVLayout.setSpacing(5)
        self.generateMnemonicClientContainerQFrameVLayout.setObjectName(u"generateMnemonicClientContainerQFrameVLayout")
        self.generateMnemonicClientContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicClientQLabel = QLabel(self.generateMnemonicClientContainerQFrame)
        self.generateMnemonicClientQLabel.setObjectName(u"generateMnemonicClientQLabel")

        self.generateMnemonicClientContainerQFrameVLayout.addWidget(self.generateMnemonicClientQLabel)

        self.generateMnemonicClientQComboBox = QComboBox(self.generateMnemonicClientContainerQFrame)
        self.generateMnemonicClientQComboBox.setObjectName(u"generateMnemonicClientQComboBox")

        self.generateMnemonicClientContainerQFrameVLayout.addWidget(self.generateMnemonicClientQComboBox)


        self.generateMnemonicClientFromLanguageContainerQFrameHLayout.addWidget(self.generateMnemonicClientContainerQFrame)

        self.generateMnemonicFromContainerQFrame = QFrame(self.generateMnemonicClientFromLanguageContainerQFrame)
        self.generateMnemonicFromContainerQFrame.setObjectName(u"generateMnemonicFromContainerQFrame")
        self.generateMnemonicFromContainerQFrameVLayout = QVBoxLayout(self.generateMnemonicFromContainerQFrame)
        self.generateMnemonicFromContainerQFrameVLayout.setSpacing(5)
        self.generateMnemonicFromContainerQFrameVLayout.setObjectName(u"generateMnemonicFromContainerQFrameVLayout")
        self.generateMnemonicFromContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicFromQLabel = QLabel(self.generateMnemonicFromContainerQFrame)
        self.generateMnemonicFromQLabel.setObjectName(u"generateMnemonicFromQLabel")

        self.generateMnemonicFromContainerQFrameVLayout.addWidget(self.generateMnemonicFromQLabel)

        self.generateMnemonicFromActionQFrame = QFrame(self.generateMnemonicFromContainerQFrame)
        self.generateMnemonicFromActionQFrame.setObjectName(u"generateMnemonicFromActionQFrame")
        self.generateMnemonicFromActionQFrameHLayout = QHBoxLayout(self.generateMnemonicFromActionQFrame)
        self.generateMnemonicFromActionQFrameHLayout.setSpacing(15)
        self.generateMnemonicFromActionQFrameHLayout.setObjectName(u"generateMnemonicFromActionQFrameHLayout")
        self.generateMnemonicFromActionQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicWordsQRadioButton = QRadioButton(self.generateMnemonicFromActionQFrame)
        self.generateMnemonicWordsQRadioButton.setObjectName(u"generateMnemonicWordsQRadioButton")

        self.generateMnemonicFromActionQFrameHLayout.addWidget(self.generateMnemonicWordsQRadioButton)

        self.generateMnemonicEntropyQRadioButton = QRadioButton(self.generateMnemonicFromActionQFrame)
        self.generateMnemonicEntropyQRadioButton.setObjectName(u"generateMnemonicEntropyQRadioButton")

        self.generateMnemonicFromActionQFrameHLayout.addWidget(self.generateMnemonicEntropyQRadioButton)


        self.generateMnemonicFromContainerQFrameVLayout.addWidget(self.generateMnemonicFromActionQFrame)


        self.generateMnemonicClientFromLanguageContainerQFrameHLayout.addWidget(self.generateMnemonicFromContainerQFrame)

        self.generateMnemonicTypeContainerQFrame = QFrame(self.generateMnemonicClientFromLanguageContainerQFrame)
        self.generateMnemonicTypeContainerQFrame.setObjectName(u"generateMnemonicTypeContainerQFrame")
        sizePolicy.setHeightForWidth(self.generateMnemonicTypeContainerQFrame.sizePolicy().hasHeightForWidth())
        self.generateMnemonicTypeContainerQFrame.setSizePolicy(sizePolicy)
        self.generateMnemonicWordsContainerQFrameVLayout_3 = QVBoxLayout(self.generateMnemonicTypeContainerQFrame)
        self.generateMnemonicWordsContainerQFrameVLayout_3.setSpacing(5)
        self.generateMnemonicWordsContainerQFrameVLayout_3.setObjectName(u"generateMnemonicWordsContainerQFrameVLayout_3")
        self.generateMnemonicWordsContainerQFrameVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicTypeQLabel = QLabel(self.generateMnemonicTypeContainerQFrame)
        self.generateMnemonicTypeQLabel.setObjectName(u"generateMnemonicTypeQLabel")

        self.generateMnemonicWordsContainerQFrameVLayout_3.addWidget(self.generateMnemonicTypeQLabel)

        self.generateMnemonicTypeQComboBox = QComboBox(self.generateMnemonicTypeContainerQFrame)
        self.generateMnemonicTypeQComboBox.setObjectName(u"generateMnemonicTypeQComboBox")

        self.generateMnemonicWordsContainerQFrameVLayout_3.addWidget(self.generateMnemonicTypeQComboBox)


        self.generateMnemonicClientFromLanguageContainerQFrameHLayout.addWidget(self.generateMnemonicTypeContainerQFrame)


        self.verticalLayout_6.addWidget(self.generateMnemonicClientFromLanguageContainerQFrame)

        self.generateMnemonicLanguageWordsEntropyContainerQFrame = QFrame(self.generateMnemonicClientWordsLanguageContainerQGroupBox)
        self.generateMnemonicLanguageWordsEntropyContainerQFrame.setObjectName(u"generateMnemonicLanguageWordsEntropyContainerQFrame")
        self.generateMnemonicLanguageWordsEntropyContainerQFrameHLayout = QHBoxLayout(self.generateMnemonicLanguageWordsEntropyContainerQFrame)
        self.generateMnemonicLanguageWordsEntropyContainerQFrameHLayout.setSpacing(15)
        self.generateMnemonicLanguageWordsEntropyContainerQFrameHLayout.setObjectName(u"generateMnemonicLanguageWordsEntropyContainerQFrameHLayout")
        self.generateMnemonicLanguageWordsEntropyContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicLanguageContainerQFrame = QFrame(self.generateMnemonicLanguageWordsEntropyContainerQFrame)
        self.generateMnemonicLanguageContainerQFrame.setObjectName(u"generateMnemonicLanguageContainerQFrame")
        self.generateMnemonicLanguageContainerQFrame.setMinimumSize(QSize(125, 0))
        self.generateMnemonicLanguageContainerQFrameVLayout = QVBoxLayout(self.generateMnemonicLanguageContainerQFrame)
        self.generateMnemonicLanguageContainerQFrameVLayout.setSpacing(5)
        self.generateMnemonicLanguageContainerQFrameVLayout.setObjectName(u"generateMnemonicLanguageContainerQFrameVLayout")
        self.generateMnemonicLanguageContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicLanguageQLabel = QLabel(self.generateMnemonicLanguageContainerQFrame)
        self.generateMnemonicLanguageQLabel.setObjectName(u"generateMnemonicLanguageQLabel")

        self.generateMnemonicLanguageContainerQFrameVLayout.addWidget(self.generateMnemonicLanguageQLabel)

        self.generateMnemonicLanguageQComboBox = QComboBox(self.generateMnemonicLanguageContainerQFrame)
        self.generateMnemonicLanguageQComboBox.setObjectName(u"generateMnemonicLanguageQComboBox")

        self.generateMnemonicLanguageContainerQFrameVLayout.addWidget(self.generateMnemonicLanguageQComboBox)


        self.generateMnemonicLanguageWordsEntropyContainerQFrameHLayout.addWidget(self.generateMnemonicLanguageContainerQFrame)

        self.generateMnemonicWordsContainerQFrame = QFrame(self.generateMnemonicLanguageWordsEntropyContainerQFrame)
        self.generateMnemonicWordsContainerQFrame.setObjectName(u"generateMnemonicWordsContainerQFrame")
        self.generateMnemonicWordsContainerQFrame.setMaximumSize(QSize(125, 16777215))
        self.generateMnemonicWordsContainerQFrameVLayout = QVBoxLayout(self.generateMnemonicWordsContainerQFrame)
        self.generateMnemonicWordsContainerQFrameVLayout.setSpacing(5)
        self.generateMnemonicWordsContainerQFrameVLayout.setObjectName(u"generateMnemonicWordsContainerQFrameVLayout")
        self.generateMnemonicWordsContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicWordsQLabel = QLabel(self.generateMnemonicWordsContainerQFrame)
        self.generateMnemonicWordsQLabel.setObjectName(u"generateMnemonicWordsQLabel")

        self.generateMnemonicWordsContainerQFrameVLayout.addWidget(self.generateMnemonicWordsQLabel)

        self.generateMnemonicWordsQComboBox = QComboBox(self.generateMnemonicWordsContainerQFrame)
        self.generateMnemonicWordsQComboBox.setObjectName(u"generateMnemonicWordsQComboBox")

        self.generateMnemonicWordsContainerQFrameVLayout.addWidget(self.generateMnemonicWordsQComboBox)


        self.generateMnemonicLanguageWordsEntropyContainerQFrameHLayout.addWidget(self.generateMnemonicWordsContainerQFrame)

        self.generateMnemonicEntropyQFrame = QFrame(self.generateMnemonicLanguageWordsEntropyContainerQFrame)
        self.generateMnemonicEntropyQFrame.setObjectName(u"generateMnemonicEntropyQFrame")
        self.generateMnemonicEntropyQFrame.setLineWidth(0)
        self.generateMnemonicEntropyContainerQFrameVLayout = QVBoxLayout(self.generateMnemonicEntropyQFrame)
        self.generateMnemonicEntropyContainerQFrameVLayout.setSpacing(5)
        self.generateMnemonicEntropyContainerQFrameVLayout.setObjectName(u"generateMnemonicEntropyContainerQFrameVLayout")
        self.generateMnemonicEntropyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicEntropyLabelQFrame = QFrame(self.generateMnemonicEntropyQFrame)
        self.generateMnemonicEntropyLabelQFrame.setObjectName(u"generateMnemonicEntropyLabelQFrame")
        self.generateMnemonicEntropyLabelQFrame.setEnabled(True)
        self.generateLengthLabelContainerQFrameHLayout_4 = QHBoxLayout(self.generateMnemonicEntropyLabelQFrame)
        self.generateLengthLabelContainerQFrameHLayout_4.setSpacing(15)
        self.generateLengthLabelContainerQFrameHLayout_4.setObjectName(u"generateLengthLabelContainerQFrameHLayout_4")
        self.generateLengthLabelContainerQFrameHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicEntropyLabelQLabel = QLabel(self.generateMnemonicEntropyLabelQFrame)
        self.generateMnemonicEntropyLabelQLabel.setObjectName(u"generateMnemonicEntropyLabelQLabel")

        self.generateLengthLabelContainerQFrameHLayout_4.addWidget(self.generateMnemonicEntropyLabelQLabel)

        self.generateMnemonicEntropyLabelQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generateLengthLabelContainerQFrameHLayout_4.addItem(self.generateMnemonicEntropyLabelQFrameHSpacer)


        self.generateMnemonicEntropyContainerQFrameVLayout.addWidget(self.generateMnemonicEntropyLabelQFrame)

        self.generateSeedMnemonicEntropyQLineEdit = QLineEdit(self.generateMnemonicEntropyQFrame)
        self.generateSeedMnemonicEntropyQLineEdit.setObjectName(u"generateSeedMnemonicEntropyQLineEdit")
        self.generateSeedMnemonicEntropyQLineEdit.setMinimumSize(QSize(350, 0))

        self.generateMnemonicEntropyContainerQFrameVLayout.addWidget(self.generateSeedMnemonicEntropyQLineEdit)


        self.generateMnemonicLanguageWordsEntropyContainerQFrameHLayout.addWidget(self.generateMnemonicEntropyQFrame)

        self.generateMnemonicClientWordsAndLanguageQPushButton = QPushButton(self.generateMnemonicLanguageWordsEntropyContainerQFrame)
        self.generateMnemonicClientWordsAndLanguageQPushButton.setObjectName(u"generateMnemonicClientWordsAndLanguageQPushButton")
        self.generateMnemonicClientWordsAndLanguageQPushButton.setMaximumSize(QSize(100, 16777215))

        self.generateMnemonicLanguageWordsEntropyContainerQFrameHLayout.addWidget(self.generateMnemonicClientWordsAndLanguageQPushButton, 0, Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.generateMnemonicLanguageWordsEntropyContainerQFrame)


        self.generatePageQStackedWidgetVLayout.addWidget(self.generateMnemonicClientWordsLanguageContainerQGroupBox)

        self.seedGroupBoxContainerQGroupBox = QGroupBox(self.generatePageQStackedWidget)
        self.seedGroupBoxContainerQGroupBox.setObjectName(u"seedGroupBoxContainerQGroupBox")
        self.seedGroupBoxContainerQGroupBoxVLayout = QVBoxLayout(self.seedGroupBoxContainerQGroupBox)
        self.seedGroupBoxContainerQGroupBoxVLayout.setSpacing(15)
        self.seedGroupBoxContainerQGroupBoxVLayout.setObjectName(u"seedGroupBoxContainerQGroupBoxVLayout")
        self.seedGroupBoxContainerQGroupBoxVLayout.setContentsMargins(10, 15, 10, 10)
        self.generateSeedGenerateContainerQFrame = QFrame(self.seedGroupBoxContainerQGroupBox)
        self.generateSeedGenerateContainerQFrame.setObjectName(u"generateSeedGenerateContainerQFrame")
        self.generateSeedGenerateContainerQFrame.setEnabled(True)
        self.generateSeedGenerateContainerQFrameHLayout = QHBoxLayout(self.generateSeedGenerateContainerQFrame)
        self.generateSeedGenerateContainerQFrameHLayout.setSpacing(15)
        self.generateSeedGenerateContainerQFrameHLayout.setObjectName(u"generateSeedGenerateContainerQFrameHLayout")
        self.generateSeedGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generateSeedClientContainerQFrame = QFrame(self.generateSeedGenerateContainerQFrame)
        self.generateSeedClientContainerQFrame.setObjectName(u"generateSeedClientContainerQFrame")
        self.generateSeedClientContainerQFrameVLayout = QVBoxLayout(self.generateSeedClientContainerQFrame)
        self.generateSeedClientContainerQFrameVLayout.setSpacing(5)
        self.generateSeedClientContainerQFrameVLayout.setObjectName(u"generateSeedClientContainerQFrameVLayout")
        self.generateSeedClientContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateSeedClientQLabel = QLabel(self.generateSeedClientContainerQFrame)
        self.generateSeedClientQLabel.setObjectName(u"generateSeedClientQLabel")

        self.generateSeedClientContainerQFrameVLayout.addWidget(self.generateSeedClientQLabel)

        self.generateSeedClientQComboBox = QComboBox(self.generateSeedClientContainerQFrame)
        self.generateSeedClientQComboBox.setObjectName(u"generateSeedClientQComboBox")

        self.generateSeedClientContainerQFrameVLayout.addWidget(self.generateSeedClientQComboBox)


        self.generateSeedGenerateContainerQFrameHLayout.addWidget(self.generateSeedClientContainerQFrame)

        self.generateSeedMnemonicTypeContainerQFrame = QFrame(self.generateSeedGenerateContainerQFrame)
        self.generateSeedMnemonicTypeContainerQFrame.setObjectName(u"generateSeedMnemonicTypeContainerQFrame")
        self.generateSeedMnemonicTypeContainerQFrameVLayout = QVBoxLayout(self.generateSeedMnemonicTypeContainerQFrame)
        self.generateSeedMnemonicTypeContainerQFrameVLayout.setSpacing(5)
        self.generateSeedMnemonicTypeContainerQFrameVLayout.setObjectName(u"generateSeedMnemonicTypeContainerQFrameVLayout")
        self.generateSeedMnemonicTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateSeedMnemonicTypeQLabel = QLabel(self.generateSeedMnemonicTypeContainerQFrame)
        self.generateSeedMnemonicTypeQLabel.setObjectName(u"generateSeedMnemonicTypeQLabel")

        self.generateSeedMnemonicTypeContainerQFrameVLayout.addWidget(self.generateSeedMnemonicTypeQLabel)

        self.generateSeedMnemonicTypeQComboBox = QComboBox(self.generateSeedMnemonicTypeContainerQFrame)
        self.generateSeedMnemonicTypeQComboBox.setObjectName(u"generateSeedMnemonicTypeQComboBox")

        self.generateSeedMnemonicTypeContainerQFrameVLayout.addWidget(self.generateSeedMnemonicTypeQComboBox)


        self.generateSeedGenerateContainerQFrameHLayout.addWidget(self.generateSeedMnemonicTypeContainerQFrame)

        self.generateSeedCardanoTypeContainerQFrame = QFrame(self.generateSeedGenerateContainerQFrame)
        self.generateSeedCardanoTypeContainerQFrame.setObjectName(u"generateSeedCardanoTypeContainerQFrame")
        self.generateSeedCardanoTypeContainerQFrameVLayout = QVBoxLayout(self.generateSeedCardanoTypeContainerQFrame)
        self.generateSeedCardanoTypeContainerQFrameVLayout.setSpacing(5)
        self.generateSeedCardanoTypeContainerQFrameVLayout.setObjectName(u"generateSeedCardanoTypeContainerQFrameVLayout")
        self.generateSeedCardanoTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateSeedCardanoTypeQLabel = QLabel(self.generateSeedCardanoTypeContainerQFrame)
        self.generateSeedCardanoTypeQLabel.setObjectName(u"generateSeedCardanoTypeQLabel")

        self.generateSeedCardanoTypeContainerQFrameVLayout.addWidget(self.generateSeedCardanoTypeQLabel)

        self.generateSeedCardanoTypeQComboBox = QComboBox(self.generateSeedCardanoTypeContainerQFrame)
        self.generateSeedCardanoTypeQComboBox.setObjectName(u"generateSeedCardanoTypeQComboBox")

        self.generateSeedCardanoTypeContainerQFrameVLayout.addWidget(self.generateSeedCardanoTypeQComboBox)


        self.generateSeedGenerateContainerQFrameHLayout.addWidget(self.generateSeedCardanoTypeContainerQFrame)


        self.seedGroupBoxContainerQGroupBoxVLayout.addWidget(self.generateSeedGenerateContainerQFrame)

        self.generateSeedClientMnemonicContainerQFrame = QFrame(self.seedGroupBoxContainerQGroupBox)
        self.generateSeedClientMnemonicContainerQFrame.setObjectName(u"generateSeedClientMnemonicContainerQFrame")
        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2 = QHBoxLayout(self.generateSeedClientMnemonicContainerQFrame)
        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.setSpacing(15)
        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.setObjectName(u"generateMnemonicClientWordsLanguageContainerQFrameHLayout_2")
        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.generateSeedMnemonicContainerQFrame = QFrame(self.generateSeedClientMnemonicContainerQFrame)
        self.generateSeedMnemonicContainerQFrame.setObjectName(u"generateSeedMnemonicContainerQFrame")
        self.generateSeedMnemonicContainerQFrame.setLineWidth(0)
        self.generateSeedMnemonicContainerQFrameVLayout = QVBoxLayout(self.generateSeedMnemonicContainerQFrame)
        self.generateSeedMnemonicContainerQFrameVLayout.setSpacing(5)
        self.generateSeedMnemonicContainerQFrameVLayout.setObjectName(u"generateSeedMnemonicContainerQFrameVLayout")
        self.generateSeedMnemonicContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateSeedMnemonicLabelContainerQFrame = QFrame(self.generateSeedMnemonicContainerQFrame)
        self.generateSeedMnemonicLabelContainerQFrame.setObjectName(u"generateSeedMnemonicLabelContainerQFrame")
        self.generateSeedMnemonicLabelContainerQFrame.setEnabled(True)
        self.generateSeedMnemonicLabelContainerQFrameHLayout = QHBoxLayout(self.generateSeedMnemonicLabelContainerQFrame)
        self.generateSeedMnemonicLabelContainerQFrameHLayout.setSpacing(15)
        self.generateSeedMnemonicLabelContainerQFrameHLayout.setObjectName(u"generateSeedMnemonicLabelContainerQFrameHLayout")
        self.generateSeedMnemonicLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generateSeedMnemonicQLabel = QLabel(self.generateSeedMnemonicLabelContainerQFrame)
        self.generateSeedMnemonicQLabel.setObjectName(u"generateSeedMnemonicQLabel")

        self.generateSeedMnemonicLabelContainerQFrameHLayout.addWidget(self.generateSeedMnemonicQLabel)

        self.generateSeedMnemonicContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generateSeedMnemonicLabelContainerQFrameHLayout.addItem(self.generateSeedMnemonicContainerQFrameHSpacer)


        self.generateSeedMnemonicContainerQFrameVLayout.addWidget(self.generateSeedMnemonicLabelContainerQFrame)

        self.generateSeedMnemonicQLineEdit = QLineEdit(self.generateSeedMnemonicContainerQFrame)
        self.generateSeedMnemonicQLineEdit.setObjectName(u"generateSeedMnemonicQLineEdit")
        self.generateSeedMnemonicQLineEdit.setMinimumSize(QSize(350, 0))

        self.generateSeedMnemonicContainerQFrameVLayout.addWidget(self.generateSeedMnemonicQLineEdit)


        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.addWidget(self.generateSeedMnemonicContainerQFrame)

        self.generateSeedPassphraseGenerateContainerQFrame = QFrame(self.generateSeedClientMnemonicContainerQFrame)
        self.generateSeedPassphraseGenerateContainerQFrame.setObjectName(u"generateSeedPassphraseGenerateContainerQFrame")
        self.generateSeedPassphraseGenerateContainerQFrame.setLineWidth(0)
        self.generateSeedPassphraseGenerateContainerQFrameVLayout = QVBoxLayout(self.generateSeedPassphraseGenerateContainerQFrame)
        self.generateSeedPassphraseGenerateContainerQFrameVLayout.setSpacing(5)
        self.generateSeedPassphraseGenerateContainerQFrameVLayout.setObjectName(u"generateSeedPassphraseGenerateContainerQFrameVLayout")
        self.generateSeedPassphraseGenerateContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateSeedPassphraseGenerateLabelContainerQFrame = QFrame(self.generateSeedPassphraseGenerateContainerQFrame)
        self.generateSeedPassphraseGenerateLabelContainerQFrame.setObjectName(u"generateSeedPassphraseGenerateLabelContainerQFrame")
        self.generateSeedPassphraseGenerateLabelContainerQFrame.setEnabled(True)
        self.generateSeedPassphraseGenerateLabelContainerQFrameHLayout = QHBoxLayout(self.generateSeedPassphraseGenerateLabelContainerQFrame)
        self.generateSeedPassphraseGenerateLabelContainerQFrameHLayout.setSpacing(15)
        self.generateSeedPassphraseGenerateLabelContainerQFrameHLayout.setObjectName(u"generateSeedPassphraseGenerateLabelContainerQFrameHLayout")
        self.generateSeedPassphraseGenerateLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generateSeedPassphraseGenerateQLabel = QLabel(self.generateSeedPassphraseGenerateLabelContainerQFrame)
        self.generateSeedPassphraseGenerateQLabel.setObjectName(u"generateSeedPassphraseGenerateQLabel")

        self.generateSeedPassphraseGenerateLabelContainerQFrameHLayout.addWidget(self.generateSeedPassphraseGenerateQLabel)

        self.generateSeedPassphraseGenerateLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generateSeedPassphraseGenerateLabelContainerQFrameHLayout.addItem(self.generateSeedPassphraseGenerateLabelContainerQFrameHSpacer)


        self.generateSeedPassphraseGenerateContainerQFrameVLayout.addWidget(self.generateSeedPassphraseGenerateLabelContainerQFrame)

        self.generateSeedPassphraseGenerateQLineEdit = QLineEdit(self.generateSeedPassphraseGenerateContainerQFrame)
        self.generateSeedPassphraseGenerateQLineEdit.setObjectName(u"generateSeedPassphraseGenerateQLineEdit")

        self.generateSeedPassphraseGenerateContainerQFrameVLayout.addWidget(self.generateSeedPassphraseGenerateQLineEdit)


        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.addWidget(self.generateSeedPassphraseGenerateContainerQFrame)

        self.generateSeedPassphraseGenerateQPushButton = QPushButton(self.generateSeedClientMnemonicContainerQFrame)
        self.generateSeedPassphraseGenerateQPushButton.setObjectName(u"generateSeedPassphraseGenerateQPushButton")

        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.addWidget(self.generateSeedPassphraseGenerateQPushButton, 0, Qt.AlignBottom)


        self.seedGroupBoxContainerQGroupBoxVLayout.addWidget(self.generateSeedClientMnemonicContainerQFrame)


        self.generatePageQStackedWidgetVLayout.addWidget(self.seedGroupBoxContainerQGroupBox)

        self.generateLengthAndPassphraseQGroupBox = QGroupBox(self.generatePageQStackedWidget)
        self.generateLengthAndPassphraseQGroupBox.setObjectName(u"generateLengthAndPassphraseQGroupBox")
        self.generateLengthAndPassphraseQGroupBox.setEnabled(True)
        self.generateLengthAndPassphraseQFrameHLayout = QHBoxLayout(self.generateLengthAndPassphraseQGroupBox)
        self.generateLengthAndPassphraseQFrameHLayout.setSpacing(15)
        self.generateLengthAndPassphraseQFrameHLayout.setObjectName(u"generateLengthAndPassphraseQFrameHLayout")
        self.generateLengthAndPassphraseQFrameHLayout.setContentsMargins(10, 15, 10, 10)
        self.generatePassphraseContainerQFrame = QFrame(self.generateLengthAndPassphraseQGroupBox)
        self.generatePassphraseContainerQFrame.setObjectName(u"generatePassphraseContainerQFrame")
        self.gridLayout = QGridLayout(self.generatePassphraseContainerQFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.generatePassphraseLineEditContainerQFrame = QFrame(self.generatePassphraseContainerQFrame)
        self.generatePassphraseLineEditContainerQFrame.setObjectName(u"generatePassphraseLineEditContainerQFrame")
        self.generatePassphraseLineEditContainerQFrameHLayout = QHBoxLayout(self.generatePassphraseLineEditContainerQFrame)
        self.generatePassphraseLineEditContainerQFrameHLayout.setSpacing(15)
        self.generatePassphraseLineEditContainerQFrameHLayout.setObjectName(u"generatePassphraseLineEditContainerQFrameHLayout")
        self.generatePassphraseLineEditContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generatePassphraseLowerCaseQCheckBox = QCheckBox(self.generatePassphraseLineEditContainerQFrame)
        self.generatePassphraseLowerCaseQCheckBox.setObjectName(u"generatePassphraseLowerCaseQCheckBox")

        self.generatePassphraseLineEditContainerQFrameHLayout.addWidget(self.generatePassphraseLowerCaseQCheckBox)

        self.generatePassphraseCharacterQCheckBox = QCheckBox(self.generatePassphraseLineEditContainerQFrame)
        self.generatePassphraseCharacterQCheckBox.setObjectName(u"generatePassphraseCharacterQCheckBox")

        self.generatePassphraseLineEditContainerQFrameHLayout.addWidget(self.generatePassphraseCharacterQCheckBox)


        self.gridLayout.addWidget(self.generatePassphraseLineEditContainerQFrame, 1, 0, 1, 1, Qt.AlignBottom)

        self.generatePassphraseLetterTypeContainerQFrame = QFrame(self.generatePassphraseContainerQFrame)
        self.generatePassphraseLetterTypeContainerQFrame.setObjectName(u"generatePassphraseLetterTypeContainerQFrame")
        self.generatePassphraseLetterTypeContainerQFrameHLayout = QHBoxLayout(self.generatePassphraseLetterTypeContainerQFrame)
        self.generatePassphraseLetterTypeContainerQFrameHLayout.setSpacing(15)
        self.generatePassphraseLetterTypeContainerQFrameHLayout.setObjectName(u"generatePassphraseLetterTypeContainerQFrameHLayout")
        self.generatePassphraseLetterTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generatePassphraseUpperCaseQCheckBox = QCheckBox(self.generatePassphraseLetterTypeContainerQFrame)
        self.generatePassphraseUpperCaseQCheckBox.setObjectName(u"generatePassphraseUpperCaseQCheckBox")

        self.generatePassphraseLetterTypeContainerQFrameHLayout.addWidget(self.generatePassphraseUpperCaseQCheckBox)

        self.generatePassphraseNumberQCheckBox = QCheckBox(self.generatePassphraseLetterTypeContainerQFrame)
        self.generatePassphraseNumberQCheckBox.setObjectName(u"generatePassphraseNumberQCheckBox")

        self.generatePassphraseLetterTypeContainerQFrameHLayout.addWidget(self.generatePassphraseNumberQCheckBox)


        self.gridLayout.addWidget(self.generatePassphraseLetterTypeContainerQFrame, 0, 0, 1, 1)


        self.generateLengthAndPassphraseQFrameHLayout.addWidget(self.generatePassphraseContainerQFrame)

        self.generateLengthContainerQFrame = QFrame(self.generateLengthAndPassphraseQGroupBox)
        self.generateLengthContainerQFrame.setObjectName(u"generateLengthContainerQFrame")
        self.generateLengthContainerQFrame.setLineWidth(0)
        self.generateLengthContainerQFrameVLayout = QVBoxLayout(self.generateLengthContainerQFrame)
        self.generateLengthContainerQFrameVLayout.setSpacing(5)
        self.generateLengthContainerQFrameVLayout.setObjectName(u"generateLengthContainerQFrameVLayout")
        self.generateLengthContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.generateLengthLabelContainerQFrame = QFrame(self.generateLengthContainerQFrame)
        self.generateLengthLabelContainerQFrame.setObjectName(u"generateLengthLabelContainerQFrame")
        self.generateLengthLabelContainerQFrame.setEnabled(True)
        self.generateLengthLabelContainerQFrameHLayout = QHBoxLayout(self.generateLengthLabelContainerQFrame)
        self.generateLengthLabelContainerQFrameHLayout.setSpacing(15)
        self.generateLengthLabelContainerQFrameHLayout.setObjectName(u"generateLengthLabelContainerQFrameHLayout")
        self.generateLengthLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.generateLengthQLabel = QLabel(self.generateLengthLabelContainerQFrame)
        self.generateLengthQLabel.setObjectName(u"generateLengthQLabel")

        self.generateLengthLabelContainerQFrameHLayout.addWidget(self.generateLengthQLabel)

        self.generateLengthLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generateLengthLabelContainerQFrameHLayout.addItem(self.generateLengthLabelContainerQFrameHSpacer)


        self.generateLengthContainerQFrameVLayout.addWidget(self.generateLengthLabelContainerQFrame)

        self.generateLengthQLineEdit = QLineEdit(self.generateLengthContainerQFrame)
        self.generateLengthQLineEdit.setObjectName(u"generateLengthQLineEdit")
        self.generateLengthQLineEdit.setMinimumSize(QSize(100, 0))

        self.generateLengthContainerQFrameVLayout.addWidget(self.generateLengthQLineEdit)


        self.generateLengthAndPassphraseQFrameHLayout.addWidget(self.generateLengthContainerQFrame)

        self.generatePassphraseQPushButton = QPushButton(self.generateLengthAndPassphraseQGroupBox)
        self.generatePassphraseQPushButton.setObjectName(u"generatePassphraseQPushButton")
        self.generatePassphraseQPushButton.setMaximumSize(QSize(100, 16777215))

        self.generateLengthAndPassphraseQFrameHLayout.addWidget(self.generatePassphraseQPushButton, 0, Qt.AlignBottom)


        self.generatePageQStackedWidgetVLayout.addWidget(self.generateLengthAndPassphraseQGroupBox)

        self.generatePageQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.generatePageQStackedWidgetVLayout.addItem(self.generatePageQStackedWidgetVSpacer)

        self.hdwalletQStackedWidget.addWidget(self.generatePageQStackedWidget)
        self.dumpsPageQStackedWidget = QWidget()
        self.dumpsPageQStackedWidget.setObjectName(u"dumpsPageQStackedWidget")
        self.dumpsPageQStackedWidgetVLayout = QVBoxLayout(self.dumpsPageQStackedWidget)
        self.dumpsPageQStackedWidgetVLayout.setSpacing(10)
        self.dumpsPageQStackedWidgetVLayout.setObjectName(u"dumpsPageQStackedWidgetVLayout")
        self.dumpsPageQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox = QGroupBox(self.dumpsPageQStackedWidget)
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox.setObjectName(u"dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox")
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout = QHBoxLayout(self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox)
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout.setSpacing(15)
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout.setObjectName(u"dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout")
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout.setContentsMargins(10, 10, 10, 10)
        self.dumpsCryptocurrencyContainerQFrame = QFrame(self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox)
        self.dumpsCryptocurrencyContainerQFrame.setObjectName(u"dumpsCryptocurrencyContainerQFrame")
        self.dumpsCryptocurrencyContainerQFrameVLayout = QVBoxLayout(self.dumpsCryptocurrencyContainerQFrame)
        self.dumpsCryptocurrencyContainerQFrameVLayout.setSpacing(5)
        self.dumpsCryptocurrencyContainerQFrameVLayout.setObjectName(u"dumpsCryptocurrencyContainerQFrameVLayout")
        self.dumpsCryptocurrencyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsCryptocurrencyLabelContainerQFrame = QFrame(self.dumpsCryptocurrencyContainerQFrame)
        self.dumpsCryptocurrencyLabelContainerQFrame.setObjectName(u"dumpsCryptocurrencyLabelContainerQFrame")
        self.dumpsCryptocurrencyLabelContainerQFrameHLayout = QHBoxLayout(self.dumpsCryptocurrencyLabelContainerQFrame)
        self.dumpsCryptocurrencyLabelContainerQFrameHLayout.setSpacing(15)
        self.dumpsCryptocurrencyLabelContainerQFrameHLayout.setObjectName(u"dumpsCryptocurrencyLabelContainerQFrameHLayout")
        self.dumpsCryptocurrencyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsCryptocurrencyQLabel = QLabel(self.dumpsCryptocurrencyLabelContainerQFrame)
        self.dumpsCryptocurrencyQLabel.setObjectName(u"dumpsCryptocurrencyQLabel")

        self.dumpsCryptocurrencyLabelContainerQFrameHLayout.addWidget(self.dumpsCryptocurrencyQLabel)

        self.dumpsCryptocurrencyLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dumpsCryptocurrencyLabelContainerQFrameHLayout.addItem(self.dumpsCryptocurrencyLabelContainerQFrameHSpacer)


        self.dumpsCryptocurrencyContainerQFrameVLayout.addWidget(self.dumpsCryptocurrencyLabelContainerQFrame)

        self.dumpsCryptocurrencyQComboBox = QComboBox(self.dumpsCryptocurrencyContainerQFrame)
        self.dumpsCryptocurrencyQComboBox.addItem("")
        self.dumpsCryptocurrencyQComboBox.addItem("")
        self.dumpsCryptocurrencyQComboBox.setObjectName(u"dumpsCryptocurrencyQComboBox")

        self.dumpsCryptocurrencyContainerQFrameVLayout.addWidget(self.dumpsCryptocurrencyQComboBox)


        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout.addWidget(self.dumpsCryptocurrencyContainerQFrame)

        self.dumpsNetworkContainerQFrame = QFrame(self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox)
        self.dumpsNetworkContainerQFrame.setObjectName(u"dumpsNetworkContainerQFrame")
        self.dumpsNetworkContainerQFrame.setMaximumSize(QSize(115, 16777215))
        self.dumpsNetworkContainerQFrameVLayout = QVBoxLayout(self.dumpsNetworkContainerQFrame)
        self.dumpsNetworkContainerQFrameVLayout.setSpacing(5)
        self.dumpsNetworkContainerQFrameVLayout.setObjectName(u"dumpsNetworkContainerQFrameVLayout")
        self.dumpsNetworkContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsNetworkLabelContainerQFrame = QFrame(self.dumpsNetworkContainerQFrame)
        self.dumpsNetworkLabelContainerQFrame.setObjectName(u"dumpsNetworkLabelContainerQFrame")
        self.dumpsNetworkLabelContainerQFrameHLayout = QHBoxLayout(self.dumpsNetworkLabelContainerQFrame)
        self.dumpsNetworkLabelContainerQFrameHLayout.setSpacing(15)
        self.dumpsNetworkLabelContainerQFrameHLayout.setObjectName(u"dumpsNetworkLabelContainerQFrameHLayout")
        self.dumpsNetworkLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsNetworkQLabel = QLabel(self.dumpsNetworkLabelContainerQFrame)
        self.dumpsNetworkQLabel.setObjectName(u"dumpsNetworkQLabel")

        self.dumpsNetworkLabelContainerQFrameHLayout.addWidget(self.dumpsNetworkQLabel)

        self.dumpsNetworkLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dumpsNetworkLabelContainerQFrameHLayout.addItem(self.dumpsNetworkLabelContainerQFrameHSpacer)


        self.dumpsNetworkContainerQFrameVLayout.addWidget(self.dumpsNetworkLabelContainerQFrame)

        self.dumpsNetworkQComboBox = QComboBox(self.dumpsNetworkContainerQFrame)
        self.dumpsNetworkQComboBox.addItem("")
        self.dumpsNetworkQComboBox.addItem("")
        self.dumpsNetworkQComboBox.setObjectName(u"dumpsNetworkQComboBox")

        self.dumpsNetworkContainerQFrameVLayout.addWidget(self.dumpsNetworkQComboBox)


        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout.addWidget(self.dumpsNetworkContainerQFrame)

        self.dumpsHdListComboContainerQFrame = QFrame(self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox)
        self.dumpsHdListComboContainerQFrame.setObjectName(u"dumpsHdListComboContainerQFrame")
        self.dumpsHdListComboContainerQFrameVLayout = QVBoxLayout(self.dumpsHdListComboContainerQFrame)
        self.dumpsHdListComboContainerQFrameVLayout.setSpacing(5)
        self.dumpsHdListComboContainerQFrameVLayout.setObjectName(u"dumpsHdListComboContainerQFrameVLayout")
        self.dumpsHdListComboContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsHdListLabelContainerQFrame = QFrame(self.dumpsHdListComboContainerQFrame)
        self.dumpsHdListLabelContainerQFrame.setObjectName(u"dumpsHdListLabelContainerQFrame")
        self.dumpsHdListLabelContainerQFrame.setFrameShape(QFrame.NoFrame)
        self.dumpsHdListLabelContainerQFrameHLayout = QHBoxLayout(self.dumpsHdListLabelContainerQFrame)
        self.dumpsHdListLabelContainerQFrameHLayout.setSpacing(15)
        self.dumpsHdListLabelContainerQFrameHLayout.setObjectName(u"dumpsHdListLabelContainerQFrameHLayout")
        self.dumpsHdListLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsHdListQLabel = QLabel(self.dumpsHdListLabelContainerQFrame)
        self.dumpsHdListQLabel.setObjectName(u"dumpsHdListQLabel")

        self.dumpsHdListLabelContainerQFrameHLayout.addWidget(self.dumpsHdListQLabel)

        self.dumpsHdListLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dumpsHdListLabelContainerQFrameHLayout.addItem(self.dumpsHdListLabelContainerQFrameHSpacer)


        self.dumpsHdListComboContainerQFrameVLayout.addWidget(self.dumpsHdListLabelContainerQFrame)

        self.dumpsHdQComboBox = QComboBox(self.dumpsHdListComboContainerQFrame)
        self.dumpsHdQComboBox.addItem("")
        self.dumpsHdQComboBox.addItem("")
        self.dumpsHdQComboBox.addItem("")
        self.dumpsHdQComboBox.addItem("")
        self.dumpsHdQComboBox.addItem("")
        self.dumpsHdQComboBox.addItem("")
        self.dumpsHdQComboBox.addItem("")
        self.dumpsHdQComboBox.addItem("")
        self.dumpsHdQComboBox.addItem("")
        self.dumpsHdQComboBox.addItem("")
        self.dumpsHdQComboBox.setObjectName(u"dumpsHdQComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dumpsHdQComboBox.sizePolicy().hasHeightForWidth())
        self.dumpsHdQComboBox.setSizePolicy(sizePolicy1)

        self.dumpsHdListComboContainerQFrameVLayout.addWidget(self.dumpsHdQComboBox)


        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout.addWidget(self.dumpsHdListComboContainerQFrame)

        self.dumpsFromContainerQFrame = QFrame(self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox)
        self.dumpsFromContainerQFrame.setObjectName(u"dumpsFromContainerQFrame")
        self.dumpsFromContainerQFrameVLayout = QVBoxLayout(self.dumpsFromContainerQFrame)
        self.dumpsFromContainerQFrameVLayout.setSpacing(5)
        self.dumpsFromContainerQFrameVLayout.setObjectName(u"dumpsFromContainerQFrameVLayout")
        self.dumpsFromContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsFromLabelContainerQFrame = QFrame(self.dumpsFromContainerQFrame)
        self.dumpsFromLabelContainerQFrame.setObjectName(u"dumpsFromLabelContainerQFrame")
        self.dumpsFromLabelContainerQFrame.setFrameShape(QFrame.NoFrame)
        self.dumpsFromLabelContainerQFrameHLayout = QHBoxLayout(self.dumpsFromLabelContainerQFrame)
        self.dumpsFromLabelContainerQFrameHLayout.setSpacing(15)
        self.dumpsFromLabelContainerQFrameHLayout.setObjectName(u"dumpsFromLabelContainerQFrameHLayout")
        self.dumpsFromLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsFromQLabel = QLabel(self.dumpsFromLabelContainerQFrame)
        self.dumpsFromQLabel.setObjectName(u"dumpsFromQLabel")

        self.dumpsFromLabelContainerQFrameHLayout.addWidget(self.dumpsFromQLabel)

        self.dumpsFromLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dumpsFromLabelContainerQFrameHLayout.addItem(self.dumpsFromLabelContainerQFrameHSpacer)


        self.dumpsFromContainerQFrameVLayout.addWidget(self.dumpsFromLabelContainerQFrame)

        self.dumpsFromQComboBox = QComboBox(self.dumpsFromContainerQFrame)
        self.dumpsFromQComboBox.addItem("")
        self.dumpsFromQComboBox.addItem("")
        self.dumpsFromQComboBox.addItem("")
        self.dumpsFromQComboBox.addItem("")
        self.dumpsFromQComboBox.addItem("")
        self.dumpsFromQComboBox.addItem("")
        self.dumpsFromQComboBox.addItem("")
        self.dumpsFromQComboBox.addItem("")
        self.dumpsFromQComboBox.setObjectName(u"dumpsFromQComboBox")
        sizePolicy1.setHeightForWidth(self.dumpsFromQComboBox.sizePolicy().hasHeightForWidth())
        self.dumpsFromQComboBox.setSizePolicy(sizePolicy1)

        self.dumpsFromContainerQFrameVLayout.addWidget(self.dumpsFromQComboBox)


        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout.addWidget(self.dumpsFromContainerQFrame)


        self.dumpsPageQStackedWidgetVLayout.addWidget(self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox)

        self.dumpsStackQGroupBox = QGroupBox(self.dumpsPageQStackedWidget)
        self.dumpsStackQGroupBox.setObjectName(u"dumpsStackQGroupBox")
        self.dumpsStackQGroupBoxVLayout = QVBoxLayout(self.dumpsStackQGroupBox)
        self.dumpsStackQGroupBoxVLayout.setSpacing(0)
        self.dumpsStackQGroupBoxVLayout.setObjectName(u"dumpsStackQGroupBoxVLayout")
        self.dumpsStackQGroupBoxVLayout.setContentsMargins(10, 10, 10, 10)
        self.hdQStackedWidget = QStackedWidget(self.dumpsStackQGroupBox)
        self.hdQStackedWidget.setObjectName(u"hdQStackedWidget")
        self.hdQStackedWidget.setLineWidth(0)
        self.bipsPageQWidget = QWidget()
        self.bipsPageQWidget.setObjectName(u"bipsPageQWidget")
        self.bipsPageQWidgetVLayout = QVBoxLayout(self.bipsPageQWidget)
        self.bipsPageQWidgetVLayout.setSpacing(0)
        self.bipsPageQWidgetVLayout.setObjectName(u"bipsPageQWidgetVLayout")
        self.bipsPageQWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipQStackedWidget = QStackedWidget(self.bipsPageQWidget)
        self.bipQStackedWidget.setObjectName(u"bipQStackedWidget")
        self.bipFromEntropyQStackedWidget = QWidget()
        self.bipFromEntropyQStackedWidget.setObjectName(u"bipFromEntropyQStackedWidget")
        self.bipFromEntropyQStackedWidgetVLayout = QVBoxLayout(self.bipFromEntropyQStackedWidget)
        self.bipFromEntropyQStackedWidgetVLayout.setSpacing(15)
        self.bipFromEntropyQStackedWidgetVLayout.setObjectName(u"bipFromEntropyQStackedWidgetVLayout")
        self.bipFromEntropyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyContainerQFrame = QFrame(self.bipFromEntropyQStackedWidget)
        self.bipFromEntropyContainerQFrame.setObjectName(u"bipFromEntropyContainerQFrame")
        self.bipFromEntropyContainerQFrameVLayout = QVBoxLayout(self.bipFromEntropyContainerQFrame)
        self.bipFromEntropyContainerQFrameVLayout.setSpacing(5)
        self.bipFromEntropyContainerQFrameVLayout.setObjectName(u"bipFromEntropyContainerQFrameVLayout")
        self.bipFromEntropyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyLabelContainerQFrame = QFrame(self.bipFromEntropyContainerQFrame)
        self.bipFromEntropyLabelContainerQFrame.setObjectName(u"bipFromEntropyLabelContainerQFrame")
        self.bipFromEntropyLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromEntropyLabelContainerQFrame)
        self.bipFromEntropyLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromEntropyLabelContainerQFrameHLayout.setObjectName(u"bipFromEntropyLabelContainerQFrameHLayout")
        self.bipFromEntropyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyQLabel = QLabel(self.bipFromEntropyLabelContainerQFrame)
        self.bipFromEntropyQLabel.setObjectName(u"bipFromEntropyQLabel")

        self.bipFromEntropyLabelContainerQFrameHLayout.addWidget(self.bipFromEntropyQLabel)

        self.bipFromEntropyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromEntropyLabelContainerQFrameHLayout.addItem(self.bipFromEntropyLabelContainerQFrameHSpacer)


        self.bipFromEntropyContainerQFrameVLayout.addWidget(self.bipFromEntropyLabelContainerQFrame)

        self.bipFromEntropyEntAndGenerateContainerQFrame = QFrame(self.bipFromEntropyContainerQFrame)
        self.bipFromEntropyEntAndGenerateContainerQFrame.setObjectName(u"bipFromEntropyEntAndGenerateContainerQFrame")
        self.bipFromEntropyEntAndGenerateContainerQFrameHLayout = QHBoxLayout(self.bipFromEntropyEntAndGenerateContainerQFrame)
        self.bipFromEntropyEntAndGenerateContainerQFrameHLayout.setSpacing(15)
        self.bipFromEntropyEntAndGenerateContainerQFrameHLayout.setObjectName(u"bipFromEntropyEntAndGenerateContainerQFrameHLayout")
        self.bipFromEntropyEntAndGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyGenerateQLineEdit = QLineEdit(self.bipFromEntropyEntAndGenerateContainerQFrame)
        self.bipFromEntropyGenerateQLineEdit.setObjectName(u"bipFromEntropyGenerateQLineEdit")

        self.bipFromEntropyEntAndGenerateContainerQFrameHLayout.addWidget(self.bipFromEntropyGenerateQLineEdit)


        self.bipFromEntropyContainerQFrameVLayout.addWidget(self.bipFromEntropyEntAndGenerateContainerQFrame)


        self.bipFromEntropyQStackedWidgetVLayout.addWidget(self.bipFromEntropyContainerQFrame)

        self.bipFromEntropyPublicKeyAndPassphraseContainerQFrame = QFrame(self.bipFromEntropyQStackedWidget)
        self.bipFromEntropyPublicKeyAndPassphraseContainerQFrame.setObjectName(u"bipFromEntropyPublicKeyAndPassphraseContainerQFrame")
        self.bipFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout = QHBoxLayout(self.bipFromEntropyPublicKeyAndPassphraseContainerQFrame)
        self.bipFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.setSpacing(15)
        self.bipFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.setObjectName(u"bipFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout")
        self.bipFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyPublicKeyTypeContainerQFrame = QFrame(self.bipFromEntropyPublicKeyAndPassphraseContainerQFrame)
        self.bipFromEntropyPublicKeyTypeContainerQFrame.setObjectName(u"bipFromEntropyPublicKeyTypeContainerQFrame")
        self.bipFromEntropyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.bipFromEntropyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.bipFromEntropyPublicKeyTypeContainerQFrame)
        self.bipFromEntropyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.bipFromEntropyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"bipFromEntropyPublicKeyTypeContainerQFrameVLayout")
        self.bipFromEntropyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyPublicKeyTypeLabelContainerQFrame = QFrame(self.bipFromEntropyPublicKeyTypeContainerQFrame)
        self.bipFromEntropyPublicKeyTypeLabelContainerQFrame.setObjectName(u"bipFromEntropyPublicKeyTypeLabelContainerQFrame")
        self.bipFromEntropyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromEntropyPublicKeyTypeLabelContainerQFrame)
        self.bipFromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"bipFromEntropyPublicKeyTypeLabelContainerQFrameHLayout")
        self.bipFromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyPublicKeyTypeQLabel = QLabel(self.bipFromEntropyPublicKeyTypeLabelContainerQFrame)
        self.bipFromEntropyPublicKeyTypeQLabel.setObjectName(u"bipFromEntropyPublicKeyTypeQLabel")

        self.bipFromEntropyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.bipFromEntropyPublicKeyTypeQLabel)

        self.bipFromEntropyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromEntropyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.bipFromEntropyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.bipFromEntropyPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromEntropyPublicKeyTypeLabelContainerQFrame)

        self.bipFromEntropyPublicKeyTypeQComboBox = QComboBox(self.bipFromEntropyPublicKeyTypeContainerQFrame)
        self.bipFromEntropyPublicKeyTypeQComboBox.addItem("")
        self.bipFromEntropyPublicKeyTypeQComboBox.addItem("")
        self.bipFromEntropyPublicKeyTypeQComboBox.setObjectName(u"bipFromEntropyPublicKeyTypeQComboBox")

        self.bipFromEntropyPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromEntropyPublicKeyTypeQComboBox)


        self.bipFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.addWidget(self.bipFromEntropyPublicKeyTypeContainerQFrame)

        self.bipFromEntropyLanguageContainerQFrame = QFrame(self.bipFromEntropyPublicKeyAndPassphraseContainerQFrame)
        self.bipFromEntropyLanguageContainerQFrame.setObjectName(u"bipFromEntropyLanguageContainerQFrame")
        self.bipFromEntropyLanguageContainerQFrameVLayout = QVBoxLayout(self.bipFromEntropyLanguageContainerQFrame)
        self.bipFromEntropyLanguageContainerQFrameVLayout.setSpacing(5)
        self.bipFromEntropyLanguageContainerQFrameVLayout.setObjectName(u"bipFromEntropyLanguageContainerQFrameVLayout")
        self.bipFromEntropyLanguageContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyLanguageLabelContainerQFrame = QFrame(self.bipFromEntropyLanguageContainerQFrame)
        self.bipFromEntropyLanguageLabelContainerQFrame.setObjectName(u"bipFromEntropyLanguageLabelContainerQFrame")
        self.bipFromEntropyLanguageLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromEntropyLanguageLabelContainerQFrame)
        self.bipFromEntropyLanguageLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromEntropyLanguageLabelContainerQFrameHLayout.setObjectName(u"bipFromEntropyLanguageLabelContainerQFrameHLayout")
        self.bipFromEntropyLanguageLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyLanguageQLabel = QLabel(self.bipFromEntropyLanguageLabelContainerQFrame)
        self.bipFromEntropyLanguageQLabel.setObjectName(u"bipFromEntropyLanguageQLabel")

        self.bipFromEntropyLanguageLabelContainerQFrameHLayout.addWidget(self.bipFromEntropyLanguageQLabel)

        self.bipFromEntropyLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromEntropyLanguageLabelContainerQFrameHLayout.addItem(self.bipFromEntropyLanguageLabelContainerQFrameHSpacer)


        self.bipFromEntropyLanguageContainerQFrameVLayout.addWidget(self.bipFromEntropyLanguageLabelContainerQFrame)

        self.bipFromEntropyLanguageQComboBox = QComboBox(self.bipFromEntropyLanguageContainerQFrame)
        self.bipFromEntropyLanguageQComboBox.addItem("")
        self.bipFromEntropyLanguageQComboBox.addItem("")
        self.bipFromEntropyLanguageQComboBox.addItem("")
        self.bipFromEntropyLanguageQComboBox.addItem("")
        self.bipFromEntropyLanguageQComboBox.addItem("")
        self.bipFromEntropyLanguageQComboBox.addItem("")
        self.bipFromEntropyLanguageQComboBox.addItem("")
        self.bipFromEntropyLanguageQComboBox.addItem("")
        self.bipFromEntropyLanguageQComboBox.setObjectName(u"bipFromEntropyLanguageQComboBox")

        self.bipFromEntropyLanguageContainerQFrameVLayout.addWidget(self.bipFromEntropyLanguageQComboBox)


        self.bipFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.addWidget(self.bipFromEntropyLanguageContainerQFrame)

        self.bipFromEntropyPassphraseContainerQFrame = QFrame(self.bipFromEntropyPublicKeyAndPassphraseContainerQFrame)
        self.bipFromEntropyPassphraseContainerQFrame.setObjectName(u"bipFromEntropyPassphraseContainerQFrame")
        self.bipFromEntropyPassphraseContainerQFrameVLayout = QVBoxLayout(self.bipFromEntropyPassphraseContainerQFrame)
        self.bipFromEntropyPassphraseContainerQFrameVLayout.setSpacing(5)
        self.bipFromEntropyPassphraseContainerQFrameVLayout.setObjectName(u"bipFromEntropyPassphraseContainerQFrameVLayout")
        self.bipFromEntropyPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyPassphraseLabelContainerQFrame = QFrame(self.bipFromEntropyPassphraseContainerQFrame)
        self.bipFromEntropyPassphraseLabelContainerQFrame.setObjectName(u"bipFromEntropyPassphraseLabelContainerQFrame")
        self.bipFromEntropyPassphraseLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromEntropyPassphraseLabelContainerQFrame)
        self.bipFromEntropyPassphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromEntropyPassphraseLabelContainerQFrameHLayout.setObjectName(u"bipFromEntropyPassphraseLabelContainerQFrameHLayout")
        self.bipFromEntropyPassphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyPassphraseQLabel = QLabel(self.bipFromEntropyPassphraseLabelContainerQFrame)
        self.bipFromEntropyPassphraseQLabel.setObjectName(u"bipFromEntropyPassphraseQLabel")

        self.bipFromEntropyPassphraseLabelContainerQFrameHLayout.addWidget(self.bipFromEntropyPassphraseQLabel)

        self.bipFromEntropyPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromEntropyPassphraseLabelContainerQFrameHLayout.addItem(self.bipFromEntropyPassphraseLabelContainerQFrameHSpacer)


        self.bipFromEntropyPassphraseContainerQFrameVLayout.addWidget(self.bipFromEntropyPassphraseLabelContainerQFrame)

        self.bipFromEntropyPassphraseGenerateContainerQFrame = QFrame(self.bipFromEntropyPassphraseContainerQFrame)
        self.bipFromEntropyPassphraseGenerateContainerQFrame.setObjectName(u"bipFromEntropyPassphraseGenerateContainerQFrame")
        self.bipFromEntropyPassphraseGenerateContainerQFrameHLayout = QHBoxLayout(self.bipFromEntropyPassphraseGenerateContainerQFrame)
        self.bipFromEntropyPassphraseGenerateContainerQFrameHLayout.setSpacing(15)
        self.bipFromEntropyPassphraseGenerateContainerQFrameHLayout.setObjectName(u"bipFromEntropyPassphraseGenerateContainerQFrameHLayout")
        self.bipFromEntropyPassphraseGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromEntropyPassphraseQLineEdit = QLineEdit(self.bipFromEntropyPassphraseGenerateContainerQFrame)
        self.bipFromEntropyPassphraseQLineEdit.setObjectName(u"bipFromEntropyPassphraseQLineEdit")

        self.bipFromEntropyPassphraseGenerateContainerQFrameHLayout.addWidget(self.bipFromEntropyPassphraseQLineEdit)


        self.bipFromEntropyPassphraseContainerQFrameVLayout.addWidget(self.bipFromEntropyPassphraseGenerateContainerQFrame)


        self.bipFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.addWidget(self.bipFromEntropyPassphraseContainerQFrame)


        self.bipFromEntropyQStackedWidgetVLayout.addWidget(self.bipFromEntropyPublicKeyAndPassphraseContainerQFrame)

        self.bipFromEntropyPassphraseContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.bipFromEntropyQStackedWidgetVLayout.addItem(self.bipFromEntropyPassphraseContainerQFrameVSpacer)

        self.bipQStackedWidget.addWidget(self.bipFromEntropyQStackedWidget)
        self.bipFromMnemonicQStackedWidget = QWidget()
        self.bipFromMnemonicQStackedWidget.setObjectName(u"bipFromMnemonicQStackedWidget")
        self.bipFromMnemonicQStackedWidgetVLayout = QVBoxLayout(self.bipFromMnemonicQStackedWidget)
        self.bipFromMnemonicQStackedWidgetVLayout.setSpacing(15)
        self.bipFromMnemonicQStackedWidgetVLayout.setObjectName(u"bipFromMnemonicQStackedWidgetVLayout")
        self.bipFromMnemonicQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromMnemonicContainerQFrame = QFrame(self.bipFromMnemonicQStackedWidget)
        self.bipFromMnemonicContainerQFrame.setObjectName(u"bipFromMnemonicContainerQFrame")
        self.bipFromMnemonicContainerQFrameVLayout = QVBoxLayout(self.bipFromMnemonicContainerQFrame)
        self.bipFromMnemonicContainerQFrameVLayout.setSpacing(5)
        self.bipFromMnemonicContainerQFrameVLayout.setObjectName(u"bipFromMnemonicContainerQFrameVLayout")
        self.bipFromMnemonicContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromMnemonicLabelContainerQFrame = QFrame(self.bipFromMnemonicContainerQFrame)
        self.bipFromMnemonicLabelContainerQFrame.setObjectName(u"bipFromMnemonicLabelContainerQFrame")
        self.bipFromMnemonicLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromMnemonicLabelContainerQFrame)
        self.bipFromMnemonicLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromMnemonicLabelContainerQFrameHLayout.setObjectName(u"bipFromMnemonicLabelContainerQFrameHLayout")
        self.bipFromMnemonicLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromMnemonicQLabel = QLabel(self.bipFromMnemonicLabelContainerQFrame)
        self.bipFromMnemonicQLabel.setObjectName(u"bipFromMnemonicQLabel")

        self.bipFromMnemonicLabelContainerQFrameHLayout.addWidget(self.bipFromMnemonicQLabel)

        self.bipFromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromMnemonicLabelContainerQFrameHLayout.addItem(self.bipFromMnemonicLabelContainerQFrameHSpacer)


        self.bipFromMnemonicContainerQFrameVLayout.addWidget(self.bipFromMnemonicLabelContainerQFrame)

        self.bipFromMnemonicLabelGenerateContainerQFrame = QFrame(self.bipFromMnemonicContainerQFrame)
        self.bipFromMnemonicLabelGenerateContainerQFrame.setObjectName(u"bipFromMnemonicLabelGenerateContainerQFrame")
        self.bipFromMnemonicLabelGenerateContainerQFrameHLayout = QHBoxLayout(self.bipFromMnemonicLabelGenerateContainerQFrame)
        self.bipFromMnemonicLabelGenerateContainerQFrameHLayout.setSpacing(15)
        self.bipFromMnemonicLabelGenerateContainerQFrameHLayout.setObjectName(u"bipFromMnemonicLabelGenerateContainerQFrameHLayout")
        self.bipFromMnemonicLabelGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromMnemonicQLineEdit = QLineEdit(self.bipFromMnemonicLabelGenerateContainerQFrame)
        self.bipFromMnemonicQLineEdit.setObjectName(u"bipFromMnemonicQLineEdit")

        self.bipFromMnemonicLabelGenerateContainerQFrameHLayout.addWidget(self.bipFromMnemonicQLineEdit)


        self.bipFromMnemonicContainerQFrameVLayout.addWidget(self.bipFromMnemonicLabelGenerateContainerQFrame)


        self.bipFromMnemonicQStackedWidgetVLayout.addWidget(self.bipFromMnemonicContainerQFrame)

        self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrame = QFrame(self.bipFromMnemonicQStackedWidget)
        self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrame.setObjectName(u"bipFromMnemonicPublicKeyTypeAndPassphraseQFrame")
        self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout = QHBoxLayout(self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrame)
        self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout.setSpacing(15)
        self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout.setObjectName(u"bipFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout")
        self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromMnemonicPublicKeyTypeContainerQFrame = QFrame(self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrame)
        self.bipFromMnemonicPublicKeyTypeContainerQFrame.setObjectName(u"bipFromMnemonicPublicKeyTypeContainerQFrame")
        self.bipFromMnemonicPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.bipFromMnemonicPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.bipFromMnemonicPublicKeyTypeContainerQFrame)
        self.bipFromMnemonicPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.bipFromMnemonicPublicKeyTypeContainerQFrameVLayout.setObjectName(u"bipFromMnemonicPublicKeyTypeContainerQFrameVLayout")
        self.bipFromMnemonicPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromMnemonicPublicKeyTypeLabelContainerQFrame = QFrame(self.bipFromMnemonicPublicKeyTypeContainerQFrame)
        self.bipFromMnemonicPublicKeyTypeLabelContainerQFrame.setObjectName(u"bipFromMnemonicPublicKeyTypeLabelContainerQFrame")
        self.bipFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.bipFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"bipFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout")
        self.bipFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromMnemonicPublicKeyTypeQLabel = QLabel(self.bipFromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.bipFromMnemonicPublicKeyTypeQLabel.setObjectName(u"bipFromMnemonicPublicKeyTypeQLabel")

        self.bipFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.bipFromMnemonicPublicKeyTypeQLabel)

        self.bipFromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.bipFromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer)


        self.bipFromMnemonicPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromMnemonicPublicKeyTypeLabelContainerQFrame)

        self.bipFromMnemonicPublicKeyTypeQComboBox = QComboBox(self.bipFromMnemonicPublicKeyTypeContainerQFrame)
        self.bipFromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.bipFromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.bipFromMnemonicPublicKeyTypeQComboBox.setObjectName(u"bipFromMnemonicPublicKeyTypeQComboBox")

        self.bipFromMnemonicPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromMnemonicPublicKeyTypeQComboBox)


        self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout.addWidget(self.bipFromMnemonicPublicKeyTypeContainerQFrame)

        self.bipFromMnemonicPassphraseContainerQFrame = QFrame(self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrame)
        self.bipFromMnemonicPassphraseContainerQFrame.setObjectName(u"bipFromMnemonicPassphraseContainerQFrame")
        self.bipFromMnemonicPassphraseContainerQFrameVLayout = QVBoxLayout(self.bipFromMnemonicPassphraseContainerQFrame)
        self.bipFromMnemonicPassphraseContainerQFrameVLayout.setSpacing(5)
        self.bipFromMnemonicPassphraseContainerQFrameVLayout.setObjectName(u"bipFromMnemonicPassphraseContainerQFrameVLayout")
        self.bipFromMnemonicPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromMnemonicPassphraseLabelContainerQFrame = QFrame(self.bipFromMnemonicPassphraseContainerQFrame)
        self.bipFromMnemonicPassphraseLabelContainerQFrame.setObjectName(u"bipFromMnemonicPassphraseLabelContainerQFrame")
        self.bipFromMnemonicPassphraseLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromMnemonicPassphraseLabelContainerQFrame)
        self.bipFromMnemonicPassphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromMnemonicPassphraseLabelContainerQFrameHLayout.setObjectName(u"bipFromMnemonicPassphraseLabelContainerQFrameHLayout")
        self.bipFromMnemonicPassphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromMnemonicPassphraseQLabel = QLabel(self.bipFromMnemonicPassphraseLabelContainerQFrame)
        self.bipFromMnemonicPassphraseQLabel.setObjectName(u"bipFromMnemonicPassphraseQLabel")

        self.bipFromMnemonicPassphraseLabelContainerQFrameHLayout.addWidget(self.bipFromMnemonicPassphraseQLabel)

        self.bipFromMnemonicPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromMnemonicPassphraseLabelContainerQFrameHLayout.addItem(self.bipFromMnemonicPassphraseLabelContainerQFrameHSpacer)


        self.bipFromMnemonicPassphraseContainerQFrameVLayout.addWidget(self.bipFromMnemonicPassphraseLabelContainerQFrame)

        self.bipFromMnemonicPassphraseGeneratelContainerQFrame = QFrame(self.bipFromMnemonicPassphraseContainerQFrame)
        self.bipFromMnemonicPassphraseGeneratelContainerQFrame.setObjectName(u"bipFromMnemonicPassphraseGeneratelContainerQFrame")
        self.bipFromMnemonicPassphraseGeneratelContainerQFrameHLayout = QHBoxLayout(self.bipFromMnemonicPassphraseGeneratelContainerQFrame)
        self.bipFromMnemonicPassphraseGeneratelContainerQFrameHLayout.setSpacing(15)
        self.bipFromMnemonicPassphraseGeneratelContainerQFrameHLayout.setObjectName(u"bipFromMnemonicPassphraseGeneratelContainerQFrameHLayout")
        self.bipFromMnemonicPassphraseGeneratelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromMnemonicPassphraseQLineEdit = QLineEdit(self.bipFromMnemonicPassphraseGeneratelContainerQFrame)
        self.bipFromMnemonicPassphraseQLineEdit.setObjectName(u"bipFromMnemonicPassphraseQLineEdit")

        self.bipFromMnemonicPassphraseGeneratelContainerQFrameHLayout.addWidget(self.bipFromMnemonicPassphraseQLineEdit)


        self.bipFromMnemonicPassphraseContainerQFrameVLayout.addWidget(self.bipFromMnemonicPassphraseGeneratelContainerQFrame)


        self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout.addWidget(self.bipFromMnemonicPassphraseContainerQFrame)


        self.bipFromMnemonicQStackedWidgetVLayout.addWidget(self.bipFromMnemonicPublicKeyTypeAndPassphraseQFrame)

        self.bipFromMnemonicQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.bipFromMnemonicQStackedWidgetVLayout.addItem(self.bipFromMnemonicQStackedWidgetVSpacer)

        self.bipQStackedWidget.addWidget(self.bipFromMnemonicQStackedWidget)
        self.bipFromSeedQStackedWidget = QWidget()
        self.bipFromSeedQStackedWidget.setObjectName(u"bipFromSeedQStackedWidget")
        self.bipFromSeedQStackedWidgetVLayout = QVBoxLayout(self.bipFromSeedQStackedWidget)
        self.bipFromSeedQStackedWidgetVLayout.setSpacing(15)
        self.bipFromSeedQStackedWidgetVLayout.setObjectName(u"bipFromSeedQStackedWidgetVLayout")
        self.bipFromSeedQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromSeedContainerQFrame = QFrame(self.bipFromSeedQStackedWidget)
        self.bipFromSeedContainerQFrame.setObjectName(u"bipFromSeedContainerQFrame")
        self.bipFromSeedContainerQFrame.setMinimumSize(QSize(400, 0))
        self.bipFromSeedContainerQFrameVLayout = QVBoxLayout(self.bipFromSeedContainerQFrame)
        self.bipFromSeedContainerQFrameVLayout.setSpacing(5)
        self.bipFromSeedContainerQFrameVLayout.setObjectName(u"bipFromSeedContainerQFrameVLayout")
        self.bipFromSeedContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromSeedAndPublicKeyTypeContainerQFrame = QFrame(self.bipFromSeedContainerQFrame)
        self.bipFromSeedAndPublicKeyTypeContainerQFrame.setObjectName(u"bipFromSeedAndPublicKeyTypeContainerQFrame")
        self.bipFromSeedAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.bipFromSeedAndPublicKeyTypeContainerQFrame)
        self.bipFromSeedAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.bipFromSeedAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"bipFromSeedAndPublicKeyTypeContainerQFrameHLayout")
        self.bipFromSeedAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromSeedsContainerQFrame = QFrame(self.bipFromSeedAndPublicKeyTypeContainerQFrame)
        self.bipFromSeedsContainerQFrame.setObjectName(u"bipFromSeedsContainerQFrame")
        self.bipFromSeedsContainerQFrameVLayout = QVBoxLayout(self.bipFromSeedsContainerQFrame)
        self.bipFromSeedsContainerQFrameVLayout.setSpacing(5)
        self.bipFromSeedsContainerQFrameVLayout.setObjectName(u"bipFromSeedsContainerQFrameVLayout")
        self.bipFromSeedsContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromSeedsLabelContainerQFrame = QFrame(self.bipFromSeedsContainerQFrame)
        self.bipFromSeedsLabelContainerQFrame.setObjectName(u"bipFromSeedsLabelContainerQFrame")
        self.bipFromSeedsLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromSeedsLabelContainerQFrame)
        self.bipFromSeedsLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromSeedsLabelContainerQFrameHLayout.setObjectName(u"bipFromSeedsLabelContainerQFrameHLayout")
        self.bipFromSeedsLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromSeedsQLabel = QLabel(self.bipFromSeedsLabelContainerQFrame)
        self.bipFromSeedsQLabel.setObjectName(u"bipFromSeedsQLabel")

        self.bipFromSeedsLabelContainerQFrameHLayout.addWidget(self.bipFromSeedsQLabel)

        self.bipFromSeedsLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromSeedsLabelContainerQFrameHLayout.addItem(self.bipFromSeedsLabelContainerQFrameHSpacer)


        self.bipFromSeedsContainerQFrameVLayout.addWidget(self.bipFromSeedsLabelContainerQFrame)

        self.bipFromSeedsQLineEdit = QLineEdit(self.bipFromSeedsContainerQFrame)
        self.bipFromSeedsQLineEdit.setObjectName(u"bipFromSeedsQLineEdit")

        self.bipFromSeedsContainerQFrameVLayout.addWidget(self.bipFromSeedsQLineEdit)


        self.bipFromSeedAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.bipFromSeedsContainerQFrame)

        self.bipFromSeedPublicKeyTypeContainerQFrame = QFrame(self.bipFromSeedAndPublicKeyTypeContainerQFrame)
        self.bipFromSeedPublicKeyTypeContainerQFrame.setObjectName(u"bipFromSeedPublicKeyTypeContainerQFrame")
        self.bipFromSeedPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.bipFromSeedPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.bipFromSeedPublicKeyTypeContainerQFrame)
        self.bipFromSeedPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.bipFromSeedPublicKeyTypeContainerQFrameVLayout.setObjectName(u"bipFromSeedPublicKeyTypeContainerQFrameVLayout")
        self.bipFromSeedPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromSeedPublicKeyTypeLabelContainerQFrame = QFrame(self.bipFromSeedPublicKeyTypeContainerQFrame)
        self.bipFromSeedPublicKeyTypeLabelContainerQFrame.setObjectName(u"bipFromSeedPublicKeyTypeLabelContainerQFrame")
        self.bipFromSeedPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromSeedPublicKeyTypeLabelContainerQFrame)
        self.bipFromSeedPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromSeedPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"bipFromSeedPublicKeyTypeLabelContainerQFrameHLayout")
        self.bipFromSeedPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromSeedPublicKeyTypeQLabel = QLabel(self.bipFromSeedPublicKeyTypeLabelContainerQFrame)
        self.bipFromSeedPublicKeyTypeQLabel.setObjectName(u"bipFromSeedPublicKeyTypeQLabel")

        self.bipFromSeedPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.bipFromSeedPublicKeyTypeQLabel)

        self.bipFromSeedPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromSeedPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.bipFromSeedPublicKeyTypeLabelContainerQFrameHSpacer)


        self.bipFromSeedPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromSeedPublicKeyTypeLabelContainerQFrame)

        self.bipFromSeedPublicKeyTypeQComboBox = QComboBox(self.bipFromSeedPublicKeyTypeContainerQFrame)
        self.bipFromSeedPublicKeyTypeQComboBox.addItem("")
        self.bipFromSeedPublicKeyTypeQComboBox.addItem("")
        self.bipFromSeedPublicKeyTypeQComboBox.setObjectName(u"bipFromSeedPublicKeyTypeQComboBox")

        self.bipFromSeedPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromSeedPublicKeyTypeQComboBox)


        self.bipFromSeedAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.bipFromSeedPublicKeyTypeContainerQFrame)


        self.bipFromSeedContainerQFrameVLayout.addWidget(self.bipFromSeedAndPublicKeyTypeContainerQFrame)

        self.bipFromSeedContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.bipFromSeedContainerQFrameVLayout.addItem(self.bipFromSeedContainerQFrameVSpacer)


        self.bipFromSeedQStackedWidgetVLayout.addWidget(self.bipFromSeedContainerQFrame)

        self.bipQStackedWidget.addWidget(self.bipFromSeedQStackedWidget)
        self.bipFromXPrivateKeyQStackedWidget = QWidget()
        self.bipFromXPrivateKeyQStackedWidget.setObjectName(u"bipFromXPrivateKeyQStackedWidget")
        self.bipFromXPrivateKeyQStackedWidgetVLayout = QVBoxLayout(self.bipFromXPrivateKeyQStackedWidget)
        self.bipFromXPrivateKeyQStackedWidgetVLayout.setSpacing(15)
        self.bipFromXPrivateKeyQStackedWidgetVLayout.setObjectName(u"bipFromXPrivateKeyQStackedWidgetVLayout")
        self.bipFromXPrivateKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPrivateKeyAndPublicKeyTypeQFrame = QFrame(self.bipFromXPrivateKeyQStackedWidget)
        self.bipFromXPrivateKeyAndPublicKeyTypeQFrame.setObjectName(u"bipFromXPrivateKeyAndPublicKeyTypeQFrame")
        self.bipFromXPrivateKeyAndPublicKeyTypeQFrameHLayout = QHBoxLayout(self.bipFromXPrivateKeyAndPublicKeyTypeQFrame)
        self.bipFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.setSpacing(15)
        self.bipFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.setObjectName(u"bipFromXPrivateKeyAndPublicKeyTypeQFrameHLayout")
        self.bipFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPrivateKeyContainerQFrame = QFrame(self.bipFromXPrivateKeyAndPublicKeyTypeQFrame)
        self.bipFromXPrivateKeyContainerQFrame.setObjectName(u"bipFromXPrivateKeyContainerQFrame")
        self.bipFromXPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.bipFromXPrivateKeyContainerQFrame)
        self.bipFromXPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.bipFromXPrivateKeyContainerQFrameVLayout.setObjectName(u"bipFromXPrivateKeyContainerQFrameVLayout")
        self.bipFromXPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPrivateKeyLabelContainerQFrame = QFrame(self.bipFromXPrivateKeyContainerQFrame)
        self.bipFromXPrivateKeyLabelContainerQFrame.setObjectName(u"bipFromXPrivateKeyLabelContainerQFrame")
        self.bipFromXPrivateKeyLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromXPrivateKeyLabelContainerQFrame)
        self.bipFromXPrivateKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromXPrivateKeyLabelContainerQFrameHLayout.setObjectName(u"bipFromXPrivateKeyLabelContainerQFrameHLayout")
        self.bipFromXPrivateKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPrivateKeyQLabel = QLabel(self.bipFromXPrivateKeyLabelContainerQFrame)
        self.bipFromXPrivateKeyQLabel.setObjectName(u"bipFromXPrivateKeyQLabel")

        self.bipFromXPrivateKeyLabelContainerQFrameHLayout.addWidget(self.bipFromXPrivateKeyQLabel)

        self.bipFromXPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromXPrivateKeyLabelContainerQFrameHLayout.addItem(self.bipFromXPrivateKeyLabelContainerQFrameHSpacer)


        self.bipFromXPrivateKeyContainerQFrameVLayout.addWidget(self.bipFromXPrivateKeyLabelContainerQFrame)

        self.bipFromXPrivateKeyQLineEdit = QLineEdit(self.bipFromXPrivateKeyContainerQFrame)
        self.bipFromXPrivateKeyQLineEdit.setObjectName(u"bipFromXPrivateKeyQLineEdit")

        self.bipFromXPrivateKeyContainerQFrameVLayout.addWidget(self.bipFromXPrivateKeyQLineEdit)


        self.bipFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.addWidget(self.bipFromXPrivateKeyContainerQFrame)

        self.bipFromXPrivateKeyStrictQCheckBox = QCheckBox(self.bipFromXPrivateKeyAndPublicKeyTypeQFrame)
        self.bipFromXPrivateKeyStrictQCheckBox.setObjectName(u"bipFromXPrivateKeyStrictQCheckBox")

        self.bipFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.addWidget(self.bipFromXPrivateKeyStrictQCheckBox, 0, Qt.AlignBottom)

        self.bipFromXPrivateKeyPublicKeyTypeContainerQFrame = QFrame(self.bipFromXPrivateKeyAndPublicKeyTypeQFrame)
        self.bipFromXPrivateKeyPublicKeyTypeContainerQFrame.setObjectName(u"bipFromXPrivateKeyPublicKeyTypeContainerQFrame")
        self.bipFromXPrivateKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.bipFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.bipFromXPrivateKeyPublicKeyTypeContainerQFrame)
        self.bipFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.bipFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"bipFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout")
        self.bipFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.bipFromXPrivateKeyPublicKeyTypeContainerQFrame)
        self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrame")
        self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrame)
        self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout")
        self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPrivateKeyPublicKeyTypeQLabel = QLabel(self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrame)
        self.bipFromXPrivateKeyPublicKeyTypeQLabel.setObjectName(u"bipFromXPrivateKeyPublicKeyTypeQLabel")

        self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.bipFromXPrivateKeyPublicKeyTypeQLabel)

        self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.bipFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromXPrivateKeyPublicKeyTypeLabelContainerQFrame)

        self.bipFromXPrivateKeyPublicKeyTypeQComboBox = QComboBox(self.bipFromXPrivateKeyPublicKeyTypeContainerQFrame)
        self.bipFromXPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.bipFromXPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.bipFromXPrivateKeyPublicKeyTypeQComboBox.setObjectName(u"bipFromXPrivateKeyPublicKeyTypeQComboBox")

        self.bipFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromXPrivateKeyPublicKeyTypeQComboBox)


        self.bipFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.addWidget(self.bipFromXPrivateKeyPublicKeyTypeContainerQFrame)


        self.bipFromXPrivateKeyQStackedWidgetVLayout.addWidget(self.bipFromXPrivateKeyAndPublicKeyTypeQFrame)

        self.bipFromXPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.bipFromXPrivateKeyQStackedWidgetVLayout.addItem(self.bipFromXPrivateKeyQStackedWidgetVSpacer)

        self.bipQStackedWidget.addWidget(self.bipFromXPrivateKeyQStackedWidget)
        self.bipFromXPublicKeyQStackedWidget = QWidget()
        self.bipFromXPublicKeyQStackedWidget.setObjectName(u"bipFromXPublicKeyQStackedWidget")
        self.bipFromXPublicKeyQStackedWidgetVLayout = QVBoxLayout(self.bipFromXPublicKeyQStackedWidget)
        self.bipFromXPublicKeyQStackedWidgetVLayout.setSpacing(15)
        self.bipFromXPublicKeyQStackedWidgetVLayout.setObjectName(u"bipFromXPublicKeyQStackedWidgetVLayout")
        self.bipFromXPublicKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrame = QFrame(self.bipFromXPublicKeyQStackedWidget)
        self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"bipFromXPublicKeyAndPublicKeyTypeContainerQFrame")
        self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"bipFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout")
        self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPublicKeyContainerQFrame = QFrame(self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromXPublicKeyContainerQFrame.setObjectName(u"bipFromXPublicKeyContainerQFrame")
        self.bipFromXPublicKeyContainerQFrameVLayout = QVBoxLayout(self.bipFromXPublicKeyContainerQFrame)
        self.bipFromXPublicKeyContainerQFrameVLayout.setSpacing(5)
        self.bipFromXPublicKeyContainerQFrameVLayout.setObjectName(u"bipFromXPublicKeyContainerQFrameVLayout")
        self.bipFromXPublicKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPublicKeyLabelContainerQFrame = QFrame(self.bipFromXPublicKeyContainerQFrame)
        self.bipFromXPublicKeyLabelContainerQFrame.setObjectName(u"bipFromXPublicKeyLabelContainerQFrame")
        self.bipFromXPublicKeyLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromXPublicKeyLabelContainerQFrame)
        self.bipFromXPublicKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromXPublicKeyLabelContainerQFrameHLayout.setObjectName(u"bipFromXPublicKeyLabelContainerQFrameHLayout")
        self.bipFromXPublicKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPublicKeyQLabel = QLabel(self.bipFromXPublicKeyLabelContainerQFrame)
        self.bipFromXPublicKeyQLabel.setObjectName(u"bipFromXPublicKeyQLabel")

        self.bipFromXPublicKeyLabelContainerQFrameHLayout.addWidget(self.bipFromXPublicKeyQLabel)

        self.bipFromXPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromXPublicKeyLabelContainerQFrameHLayout.addItem(self.bipFromXPublicKeyLabelContainerQFrameHSpacer)


        self.bipFromXPublicKeyContainerQFrameVLayout.addWidget(self.bipFromXPublicKeyLabelContainerQFrame)

        self.bipFromXPublicKeyQLineEdit = QLineEdit(self.bipFromXPublicKeyContainerQFrame)
        self.bipFromXPublicKeyQLineEdit.setObjectName(u"bipFromXPublicKeyQLineEdit")

        self.bipFromXPublicKeyContainerQFrameVLayout.addWidget(self.bipFromXPublicKeyQLineEdit)


        self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.bipFromXPublicKeyContainerQFrame)

        self.bipFromXPublicKeyStrictQCheckBox = QCheckBox(self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromXPublicKeyStrictQCheckBox.setObjectName(u"bipFromXPublicKeyStrictQCheckBox")

        self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.bipFromXPublicKeyStrictQCheckBox, 0, Qt.AlignBottom)

        self.bipFromXPublicKeyStrictContainerQFrame = QFrame(self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromXPublicKeyStrictContainerQFrame.setObjectName(u"bipFromXPublicKeyStrictContainerQFrame")
        self.bipFromXPublicKeyStrictContainerQFrameVLayout = QVBoxLayout(self.bipFromXPublicKeyStrictContainerQFrame)
        self.bipFromXPublicKeyStrictContainerQFrameVLayout.setSpacing(5)
        self.bipFromXPublicKeyStrictContainerQFrameVLayout.setObjectName(u"bipFromXPublicKeyStrictContainerQFrameVLayout")
        self.bipFromXPublicKeyStrictContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPublicKeyStrictLabelContainerQFrame = QFrame(self.bipFromXPublicKeyStrictContainerQFrame)
        self.bipFromXPublicKeyStrictLabelContainerQFrame.setObjectName(u"bipFromXPublicKeyStrictLabelContainerQFrame")
        self.bipFromXPublicKeyStrictLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromXPublicKeyStrictLabelContainerQFrame)
        self.bipFromXPublicKeyStrictLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromXPublicKeyStrictLabelContainerQFrameHLayout.setObjectName(u"bipFromXPublicKeyStrictLabelContainerQFrameHLayout")
        self.bipFromXPublicKeyStrictLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPublicKeyStrictLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromXPublicKeyStrictLabelContainerQFrameHLayout.addItem(self.bipFromXPublicKeyStrictLabelContainerQFrameHSpacer)


        self.bipFromXPublicKeyStrictContainerQFrameVLayout.addWidget(self.bipFromXPublicKeyStrictLabelContainerQFrame)


        self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.bipFromXPublicKeyStrictContainerQFrame)

        self.bipFromXPublicKeyPublicKeyTypeContainerQFrame = QFrame(self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromXPublicKeyPublicKeyTypeContainerQFrame.setObjectName(u"bipFromXPublicKeyPublicKeyTypeContainerQFrame")
        self.bipFromXPublicKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.bipFromXPublicKeyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.bipFromXPublicKeyPublicKeyTypeContainerQFrame)
        self.bipFromXPublicKeyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.bipFromXPublicKeyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"bipFromXPublicKeyPublicKeyTypeContainerQFrameVLayout")
        self.bipFromXPublicKeyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.bipFromXPublicKeyPublicKeyTypeContainerQFrame)
        self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"bipFromXPublicKeyPublicKeyTypeLabelContainerQFrame")
        self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"bipFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout")
        self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromXPublicKeyPublicKeyTypeQLabel = QLabel(self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.bipFromXPublicKeyPublicKeyTypeQLabel.setObjectName(u"bipFromXPublicKeyPublicKeyTypeQLabel")

        self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.bipFromXPublicKeyPublicKeyTypeQLabel)

        self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.bipFromXPublicKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromXPublicKeyPublicKeyTypeLabelContainerQFrame)

        self.bipFromXPublicKeyPublicKeyTypeQComboBox = QComboBox(self.bipFromXPublicKeyPublicKeyTypeContainerQFrame)
        self.bipFromXPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.bipFromXPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.bipFromXPublicKeyPublicKeyTypeQComboBox.setObjectName(u"bipFromXPublicKeyPublicKeyTypeQComboBox")

        self.bipFromXPublicKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromXPublicKeyPublicKeyTypeQComboBox)


        self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.bipFromXPublicKeyPublicKeyTypeContainerQFrame)


        self.bipFromXPublicKeyQStackedWidgetVLayout.addWidget(self.bipFromXPublicKeyAndPublicKeyTypeContainerQFrame)

        self.bipFromXPublicKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.bipFromXPublicKeyQStackedWidgetVLayout.addItem(self.bipFromXPublicKeyQStackedWidgetVSpacer)

        self.bipQStackedWidget.addWidget(self.bipFromXPublicKeyQStackedWidget)
        self.bipFromWIFQStackedWidget = QWidget()
        self.bipFromWIFQStackedWidget.setObjectName(u"bipFromWIFQStackedWidget")
        self.bipFromWIFQStackedWidgetVLayout = QVBoxLayout(self.bipFromWIFQStackedWidget)
        self.bipFromWIFQStackedWidgetVLayout.setSpacing(15)
        self.bipFromWIFQStackedWidgetVLayout.setObjectName(u"bipFromWIFQStackedWidgetVLayout")
        self.bipFromWIFQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromWIFContainerQFrame = QFrame(self.bipFromWIFQStackedWidget)
        self.bipFromWIFContainerQFrame.setObjectName(u"bipFromWIFContainerQFrame")
        self.bipFromWIFContainerQFrame.setMinimumSize(QSize(400, 0))
        self.bipFromWIFContainerQFrameVLayout = QVBoxLayout(self.bipFromWIFContainerQFrame)
        self.bipFromWIFContainerQFrameVLayout.setSpacing(5)
        self.bipFromWIFContainerQFrameVLayout.setObjectName(u"bipFromWIFContainerQFrameVLayout")
        self.bipFromWIFContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromWIFLabelContainerQFrame = QFrame(self.bipFromWIFContainerQFrame)
        self.bipFromWIFLabelContainerQFrame.setObjectName(u"bipFromWIFLabelContainerQFrame")
        self.bipFromWIFLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromWIFLabelContainerQFrame)
        self.bipFromWIFLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromWIFLabelContainerQFrameHLayout.setObjectName(u"bipFromWIFLabelContainerQFrameHLayout")
        self.bipFromWIFLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromWIFQLabel = QLabel(self.bipFromWIFLabelContainerQFrame)
        self.bipFromWIFQLabel.setObjectName(u"bipFromWIFQLabel")

        self.bipFromWIFLabelContainerQFrameHLayout.addWidget(self.bipFromWIFQLabel)

        self.bipFromWIFLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromWIFLabelContainerQFrameHLayout.addItem(self.bipFromWIFLabelContainerQFrameHSpacer)


        self.bipFromWIFContainerQFrameVLayout.addWidget(self.bipFromWIFLabelContainerQFrame)

        self.bipFromWIFQLineEdit = QLineEdit(self.bipFromWIFContainerQFrame)
        self.bipFromWIFQLineEdit.setObjectName(u"bipFromWIFQLineEdit")

        self.bipFromWIFContainerQFrameVLayout.addWidget(self.bipFromWIFQLineEdit)


        self.bipFromWIFQStackedWidgetVLayout.addWidget(self.bipFromWIFContainerQFrame)

        self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrame = QFrame(self.bipFromWIFQStackedWidget)
        self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrame.setObjectName(u"bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrame")
        self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout = QHBoxLayout(self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)
        self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout.setSpacing(15)
        self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout.setObjectName(u"bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout")
        self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromWIFPublicKeyTypeContainerQFrame = QFrame(self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)
        self.bipFromWIFPublicKeyTypeContainerQFrame.setObjectName(u"bipFromWIFPublicKeyTypeContainerQFrame")
        self.bipFromWIFPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.bipFromWIFPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.bipFromWIFPublicKeyTypeContainerQFrame)
        self.bipFromWIFPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.bipFromWIFPublicKeyTypeContainerQFrameVLayout.setObjectName(u"bipFromWIFPublicKeyTypeContainerQFrameVLayout")
        self.bipFromWIFPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromWIFPublicKeyTypeLabelContainerQFrame = QFrame(self.bipFromWIFPublicKeyTypeContainerQFrame)
        self.bipFromWIFPublicKeyTypeLabelContainerQFrame.setObjectName(u"bipFromWIFPublicKeyTypeLabelContainerQFrame")
        self.bipFromWIFPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromWIFPublicKeyTypeLabelContainerQFrame)
        self.bipFromWIFPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromWIFPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"bipFromWIFPublicKeyTypeLabelContainerQFrameHLayout")
        self.bipFromWIFPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromWIFPublicKeyTypeQLabel = QLabel(self.bipFromWIFPublicKeyTypeLabelContainerQFrame)
        self.bipFromWIFPublicKeyTypeQLabel.setObjectName(u"bipFromWIFPublicKeyTypeQLabel")

        self.bipFromWIFPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.bipFromWIFPublicKeyTypeQLabel)

        self.bipFromWIFPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromWIFPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.bipFromWIFPublicKeyTypeLabelContainerQFrameHSpacer)


        self.bipFromWIFPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromWIFPublicKeyTypeLabelContainerQFrame)

        self.bipFromWIFPublicKeyTypeQComboBox = QComboBox(self.bipFromWIFPublicKeyTypeContainerQFrame)
        self.bipFromWIFPublicKeyTypeQComboBox.addItem("")
        self.bipFromWIFPublicKeyTypeQComboBox.addItem("")
        self.bipFromWIFPublicKeyTypeQComboBox.setObjectName(u"bipFromWIFPublicKeyTypeQComboBox")

        self.bipFromWIFPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromWIFPublicKeyTypeQComboBox)


        self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout.addWidget(self.bipFromWIFPublicKeyTypeContainerQFrame)

        self.bipFromWIFBIP38PassphraseContainerQFrame = QFrame(self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)
        self.bipFromWIFBIP38PassphraseContainerQFrame.setObjectName(u"bipFromWIFBIP38PassphraseContainerQFrame")
        self.bipFromWIFBIP38PassphraseContainerQFrameVLayout = QVBoxLayout(self.bipFromWIFBIP38PassphraseContainerQFrame)
        self.bipFromWIFBIP38PassphraseContainerQFrameVLayout.setSpacing(5)
        self.bipFromWIFBIP38PassphraseContainerQFrameVLayout.setObjectName(u"bipFromWIFBIP38PassphraseContainerQFrameVLayout")
        self.bipFromWIFBIP38PassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrame = QFrame(self.bipFromWIFBIP38PassphraseContainerQFrame)
        self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrame.setObjectName(u"bipFromWIFBIP38PassphraseCheckBoxContainerQFrame")
        self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout = QHBoxLayout(self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrame)
        self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.setSpacing(15)
        self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.setObjectName(u"bipFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout")
        self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromWIFBIP38PassphraseQCheckBox = QCheckBox(self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrame)
        self.bipFromWIFBIP38PassphraseQCheckBox.setObjectName(u"bipFromWIFBIP38PassphraseQCheckBox")

        self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.addWidget(self.bipFromWIFBIP38PassphraseQCheckBox)

        self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.addItem(self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrameHSpacer)


        self.bipFromWIFBIP38PassphraseContainerQFrameVLayout.addWidget(self.bipFromWIFBIP38PassphraseCheckBoxContainerQFrame)

        self.bipFromWIFBIP38PassphraseQLineEdit = QLineEdit(self.bipFromWIFBIP38PassphraseContainerQFrame)
        self.bipFromWIFBIP38PassphraseQLineEdit.setObjectName(u"bipFromWIFBIP38PassphraseQLineEdit")

        self.bipFromWIFBIP38PassphraseContainerQFrameVLayout.addWidget(self.bipFromWIFBIP38PassphraseQLineEdit)


        self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout.addWidget(self.bipFromWIFBIP38PassphraseContainerQFrame)


        self.bipFromWIFQStackedWidgetVLayout.addWidget(self.bipFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)

        self.bipFromWIFQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.bipFromWIFQStackedWidgetVLayout.addItem(self.bipFromWIFQStackedWidgetVSpacer)

        self.bipQStackedWidget.addWidget(self.bipFromWIFQStackedWidget)
        self.bipFromPrivateKeyQStackedWidget = QWidget()
        self.bipFromPrivateKeyQStackedWidget.setObjectName(u"bipFromPrivateKeyQStackedWidget")
        self.bipFromPrivateKeyQStackedWidgetVLayout = QVBoxLayout(self.bipFromPrivateKeyQStackedWidget)
        self.bipFromPrivateKeyQStackedWidgetVLayout.setSpacing(15)
        self.bipFromPrivateKeyQStackedWidgetVLayout.setObjectName(u"bipFromPrivateKeyQStackedWidgetVLayout")
        self.bipFromPrivateKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrame = QFrame(self.bipFromPrivateKeyQStackedWidget)
        self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"bipFromPrivateKeyAndPublicKeyTypeContainerQFrame")
        self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"bipFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout")
        self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPrivateKeyContainerQFrame = QFrame(self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromPrivateKeyContainerQFrame.setObjectName(u"bipFromPrivateKeyContainerQFrame")
        self.bipFromPrivateKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.bipFromPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.bipFromPrivateKeyContainerQFrame)
        self.bipFromPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.bipFromPrivateKeyContainerQFrameVLayout.setObjectName(u"bipFromPrivateKeyContainerQFrameVLayout")
        self.bipFromPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPrivateKeyLabelContainerQFrame = QFrame(self.bipFromPrivateKeyContainerQFrame)
        self.bipFromPrivateKeyLabelContainerQFrame.setObjectName(u"bipFromPrivateKeyLabelContainerQFrame")
        self.bipFromPrivateKeyLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromPrivateKeyLabelContainerQFrame)
        self.bipFromPrivateKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromPrivateKeyLabelContainerQFrameHLayout.setObjectName(u"bipFromPrivateKeyLabelContainerQFrameHLayout")
        self.bipFromPrivateKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPrivateKeyQLabel = QLabel(self.bipFromPrivateKeyLabelContainerQFrame)
        self.bipFromPrivateKeyQLabel.setObjectName(u"bipFromPrivateKeyQLabel")

        self.bipFromPrivateKeyLabelContainerQFrameHLayout.addWidget(self.bipFromPrivateKeyQLabel)

        self.bipFromPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromPrivateKeyLabelContainerQFrameHLayout.addItem(self.bipFromPrivateKeyLabelContainerQFrameHSpacer)


        self.bipFromPrivateKeyContainerQFrameVLayout.addWidget(self.bipFromPrivateKeyLabelContainerQFrame)

        self.bipFromPrivateKeyQLineEdit = QLineEdit(self.bipFromPrivateKeyContainerQFrame)
        self.bipFromPrivateKeyQLineEdit.setObjectName(u"bipFromPrivateKeyQLineEdit")

        self.bipFromPrivateKeyContainerQFrameVLayout.addWidget(self.bipFromPrivateKeyQLineEdit)


        self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.bipFromPrivateKeyContainerQFrame)

        self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrame = QFrame(self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrame.setObjectName(u"bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrame")
        self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrame.setMinimumSize(QSize(150, 0))
        self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout = QVBoxLayout(self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrame)
        self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout.setSpacing(5)
        self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout.setObjectName(u"bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout")
        self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrame = QFrame(self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrame)
        self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrame.setObjectName(u"bipFromPrivateKeyAndPublicKeyTypeLabelQFrame")
        self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout = QHBoxLayout(self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrame)
        self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout.setSpacing(15)
        self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout.setObjectName(u"bipFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout")
        self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPrivateKeyPublicKeyTypeQLabel = QLabel(self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrame)
        self.bipFromPrivateKeyPublicKeyTypeQLabel.setObjectName(u"bipFromPrivateKeyPublicKeyTypeQLabel")

        self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout.addWidget(self.bipFromPrivateKeyPublicKeyTypeQLabel)

        self.bipFromPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout.addItem(self.bipFromPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout.addWidget(self.bipFromPrivateKeyAndPublicKeyTypeLabelQFrame)

        self.bipFromPrivateKeyPublicKeyTypeQComboBox = QComboBox(self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrame)
        self.bipFromPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.bipFromPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.bipFromPrivateKeyPublicKeyTypeQComboBox.setObjectName(u"bipFromPrivateKeyPublicKeyTypeQComboBox")

        self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout.addWidget(self.bipFromPrivateKeyPublicKeyTypeQComboBox)


        self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.bipFromPrivateKeyAndPublicKeyTypeLineContainerQFrame)


        self.bipFromPrivateKeyQStackedWidgetVLayout.addWidget(self.bipFromPrivateKeyAndPublicKeyTypeContainerQFrame)

        self.bipFromPrivateKeyContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.bipFromPrivateKeyQStackedWidgetVLayout.addItem(self.bipFromPrivateKeyContainerQFrameVSpacer)

        self.bipQStackedWidget.addWidget(self.bipFromPrivateKeyQStackedWidget)
        self.bipFromPublicKeyQStackedWidget = QWidget()
        self.bipFromPublicKeyQStackedWidget.setObjectName(u"bipFromPublicKeyQStackedWidget")
        self.bipFromPublicKeyQStackedWidgetVLayout = QVBoxLayout(self.bipFromPublicKeyQStackedWidget)
        self.bipFromPublicKeyQStackedWidgetVLayout.setSpacing(15)
        self.bipFromPublicKeyQStackedWidgetVLayout.setObjectName(u"bipFromPublicKeyQStackedWidgetVLayout")
        self.bipFromPublicKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPublicKeyAndPublicKeyTypeContainerQFrame = QFrame(self.bipFromPublicKeyQStackedWidget)
        self.bipFromPublicKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"bipFromPublicKeyAndPublicKeyTypeContainerQFrame")
        self.bipFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.bipFromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.bipFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"bipFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout")
        self.bipFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPublicKeyContainerQFrame = QFrame(self.bipFromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromPublicKeyContainerQFrame.setObjectName(u"bipFromPublicKeyContainerQFrame")
        self.bipFromPublicKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.bipFromPublicKeyContainerQFrameVLayout = QVBoxLayout(self.bipFromPublicKeyContainerQFrame)
        self.bipFromPublicKeyContainerQFrameVLayout.setSpacing(5)
        self.bipFromPublicKeyContainerQFrameVLayout.setObjectName(u"bipFromPublicKeyContainerQFrameVLayout")
        self.bipFromPublicKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPublicKeyLabelContainerQFrame = QFrame(self.bipFromPublicKeyContainerQFrame)
        self.bipFromPublicKeyLabelContainerQFrame.setObjectName(u"bipFromPublicKeyLabelContainerQFrame")
        self.bipFromPublicKeyLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromPublicKeyLabelContainerQFrame)
        self.bipFromPublicKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromPublicKeyLabelContainerQFrameHLayout.setObjectName(u"bipFromPublicKeyLabelContainerQFrameHLayout")
        self.bipFromPublicKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPublicKeyQLabel = QLabel(self.bipFromPublicKeyLabelContainerQFrame)
        self.bipFromPublicKeyQLabel.setObjectName(u"bipFromPublicKeyQLabel")

        self.bipFromPublicKeyLabelContainerQFrameHLayout.addWidget(self.bipFromPublicKeyQLabel)

        self.bipFromPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromPublicKeyLabelContainerQFrameHLayout.addItem(self.bipFromPublicKeyLabelContainerQFrameHSpacer)


        self.bipFromPublicKeyContainerQFrameVLayout.addWidget(self.bipFromPublicKeyLabelContainerQFrame)

        self.bipFromPublicKeyQLineEdit = QLineEdit(self.bipFromPublicKeyContainerQFrame)
        self.bipFromPublicKeyQLineEdit.setObjectName(u"bipFromPublicKeyQLineEdit")

        self.bipFromPublicKeyContainerQFrameVLayout.addWidget(self.bipFromPublicKeyQLineEdit)


        self.bipFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.bipFromPublicKeyContainerQFrame)

        self.bipFromPublicKeyPublicKeyTypeContainerQFrame = QFrame(self.bipFromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.bipFromPublicKeyPublicKeyTypeContainerQFrame.setObjectName(u"bipFromPublicKeyPublicKeyTypeContainerQFrame")
        self.bipFromPublicKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.bipFromPublicKeyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.bipFromPublicKeyPublicKeyTypeContainerQFrame)
        self.bipFromPublicKeyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.bipFromPublicKeyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"bipFromPublicKeyPublicKeyTypeContainerQFrameVLayout")
        self.bipFromPublicKeyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.bipFromPublicKeyPublicKeyTypeContainerQFrame)
        self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"bipFromPublicKeyPublicKeyTypeLabelContainerQFrame")
        self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"bipFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout")
        self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bipFromPublicKeyPublicKeyTypeQLabel = QLabel(self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.bipFromPublicKeyPublicKeyTypeQLabel.setObjectName(u"bipFromPublicKeyPublicKeyTypeQLabel")

        self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.bipFromPublicKeyPublicKeyTypeQLabel)

        self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.bipFromPublicKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromPublicKeyPublicKeyTypeLabelContainerQFrame)

        self.bipFromPublicKeyPublicKeyTypeQComboBox = QComboBox(self.bipFromPublicKeyPublicKeyTypeContainerQFrame)
        self.bipFromPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.bipFromPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.bipFromPublicKeyPublicKeyTypeQComboBox.setObjectName(u"bipFromPublicKeyPublicKeyTypeQComboBox")

        self.bipFromPublicKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.bipFromPublicKeyPublicKeyTypeQComboBox)


        self.bipFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.bipFromPublicKeyPublicKeyTypeContainerQFrame)


        self.bipFromPublicKeyQStackedWidgetVLayout.addWidget(self.bipFromPublicKeyAndPublicKeyTypeContainerQFrame)

        self.bipFromPublicKeyContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.bipFromPublicKeyQStackedWidgetVLayout.addItem(self.bipFromPublicKeyContainerQFrameVSpacer)

        self.bipQStackedWidget.addWidget(self.bipFromPublicKeyQStackedWidget)

        self.bipsPageQWidgetVLayout.addWidget(self.bipQStackedWidget)

        self.hdQStackedWidget.addWidget(self.bipsPageQWidget)
        self.cardanoPageQWidget = QWidget()
        self.cardanoPageQWidget.setObjectName(u"cardanoPageQWidget")
        self.cardanoPageQWidgetVLayout = QVBoxLayout(self.cardanoPageQWidget)
        self.cardanoPageQWidgetVLayout.setSpacing(0)
        self.cardanoPageQWidgetVLayout.setObjectName(u"cardanoPageQWidgetVLayout")
        self.cardanoPageQWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoQStackedWidget = QStackedWidget(self.cardanoPageQWidget)
        self.cardanoQStackedWidget.setObjectName(u"cardanoQStackedWidget")
        self.cardanoFromEntropyQStackedWidget = QWidget()
        self.cardanoFromEntropyQStackedWidget.setObjectName(u"cardanoFromEntropyQStackedWidget")
        self.cardanoFromEntropyQStackedWidgetVLayout = QVBoxLayout(self.cardanoFromEntropyQStackedWidget)
        self.cardanoFromEntropyQStackedWidgetVLayout.setSpacing(15)
        self.cardanoFromEntropyQStackedWidgetVLayout.setObjectName(u"cardanoFromEntropyQStackedWidgetVLayout")
        self.cardanoFromEntropyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyAndCardanoTypeQFrame = QFrame(self.cardanoFromEntropyQStackedWidget)
        self.cardanoFromEntropyAndCardanoTypeQFrame.setObjectName(u"cardanoFromEntropyAndCardanoTypeQFrame")
        self.cardanoFromEntropyAndCardanoTypeQFrameHLayout = QHBoxLayout(self.cardanoFromEntropyAndCardanoTypeQFrame)
        self.cardanoFromEntropyAndCardanoTypeQFrameHLayout.setSpacing(15)
        self.cardanoFromEntropyAndCardanoTypeQFrameHLayout.setObjectName(u"cardanoFromEntropyAndCardanoTypeQFrameHLayout")
        self.cardanoFromEntropyAndCardanoTypeQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyContainerQFrame = QFrame(self.cardanoFromEntropyAndCardanoTypeQFrame)
        self.cardanoFromEntropyContainerQFrame.setObjectName(u"cardanoFromEntropyContainerQFrame")
        self.verticalLayout_35 = QVBoxLayout(self.cardanoFromEntropyContainerQFrame)
        self.verticalLayout_35.setSpacing(5)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyLabelContainerQFrame = QFrame(self.cardanoFromEntropyContainerQFrame)
        self.cardanoFromEntropyLabelContainerQFrame.setObjectName(u"cardanoFromEntropyLabelContainerQFrame")
        self.EntropyLabelHLayout_4 = QHBoxLayout(self.cardanoFromEntropyLabelContainerQFrame)
        self.EntropyLabelHLayout_4.setSpacing(15)
        self.EntropyLabelHLayout_4.setObjectName(u"EntropyLabelHLayout_4")
        self.EntropyLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyQLabel = QLabel(self.cardanoFromEntropyLabelContainerQFrame)
        self.cardanoFromEntropyQLabel.setObjectName(u"cardanoFromEntropyQLabel")

        self.EntropyLabelHLayout_4.addWidget(self.cardanoFromEntropyQLabel)

        self.cardanoFromEntropyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_4.addItem(self.cardanoFromEntropyLabelContainerQFrameHSpacer)


        self.verticalLayout_35.addWidget(self.cardanoFromEntropyLabelContainerQFrame)

        self.cardanoFromEntropyGenerateContainerQFrame = QFrame(self.cardanoFromEntropyContainerQFrame)
        self.cardanoFromEntropyGenerateContainerQFrame.setObjectName(u"cardanoFromEntropyGenerateContainerQFrame")
        self.horizontalLayout_33 = QHBoxLayout(self.cardanoFromEntropyGenerateContainerQFrame)
        self.horizontalLayout_33.setSpacing(15)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyGenerateQLineEdit = QLineEdit(self.cardanoFromEntropyGenerateContainerQFrame)
        self.cardanoFromEntropyGenerateQLineEdit.setObjectName(u"cardanoFromEntropyGenerateQLineEdit")

        self.horizontalLayout_33.addWidget(self.cardanoFromEntropyGenerateQLineEdit)


        self.verticalLayout_35.addWidget(self.cardanoFromEntropyGenerateContainerQFrame)


        self.cardanoFromEntropyAndCardanoTypeQFrameHLayout.addWidget(self.cardanoFromEntropyContainerQFrame)

        self.cardanoFromEntropyLanguageContainerQFrame = QFrame(self.cardanoFromEntropyAndCardanoTypeQFrame)
        self.cardanoFromEntropyLanguageContainerQFrame.setObjectName(u"cardanoFromEntropyLanguageContainerQFrame")
        self.ELanguageVLayout_3 = QVBoxLayout(self.cardanoFromEntropyLanguageContainerQFrame)
        self.ELanguageVLayout_3.setSpacing(5)
        self.ELanguageVLayout_3.setObjectName(u"ELanguageVLayout_3")
        self.ELanguageVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyLanguageLabelContainerQFrame = QFrame(self.cardanoFromEntropyLanguageContainerQFrame)
        self.cardanoFromEntropyLanguageLabelContainerQFrame.setObjectName(u"cardanoFromEntropyLanguageLabelContainerQFrame")
        self.ELanguageLabelHLayout_3 = QHBoxLayout(self.cardanoFromEntropyLanguageLabelContainerQFrame)
        self.ELanguageLabelHLayout_3.setSpacing(15)
        self.ELanguageLabelHLayout_3.setObjectName(u"ELanguageLabelHLayout_3")
        self.ELanguageLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyLanguageQLabel = QLabel(self.cardanoFromEntropyLanguageLabelContainerQFrame)
        self.cardanoFromEntropyLanguageQLabel.setObjectName(u"cardanoFromEntropyLanguageQLabel")

        self.ELanguageLabelHLayout_3.addWidget(self.cardanoFromEntropyLanguageQLabel)

        self.cardanoFromEntropyLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout_3.addItem(self.cardanoFromEntropyLanguageLabelContainerQFrameHSpacer)


        self.ELanguageVLayout_3.addWidget(self.cardanoFromEntropyLanguageLabelContainerQFrame)

        self.cardanoFromEntropyLanguageQComboBox = QComboBox(self.cardanoFromEntropyLanguageContainerQFrame)
        self.cardanoFromEntropyLanguageQComboBox.addItem("")
        self.cardanoFromEntropyLanguageQComboBox.addItem("")
        self.cardanoFromEntropyLanguageQComboBox.addItem("")
        self.cardanoFromEntropyLanguageQComboBox.addItem("")
        self.cardanoFromEntropyLanguageQComboBox.addItem("")
        self.cardanoFromEntropyLanguageQComboBox.addItem("")
        self.cardanoFromEntropyLanguageQComboBox.addItem("")
        self.cardanoFromEntropyLanguageQComboBox.addItem("")
        self.cardanoFromEntropyLanguageQComboBox.setObjectName(u"cardanoFromEntropyLanguageQComboBox")

        self.ELanguageVLayout_3.addWidget(self.cardanoFromEntropyLanguageQComboBox)


        self.cardanoFromEntropyAndCardanoTypeQFrameHLayout.addWidget(self.cardanoFromEntropyLanguageContainerQFrame)

        self.cardanoFromEntropyCardanoTypeContainerQFrame = QFrame(self.cardanoFromEntropyAndCardanoTypeQFrame)
        self.cardanoFromEntropyCardanoTypeContainerQFrame.setObjectName(u"cardanoFromEntropyCardanoTypeContainerQFrame")
        self.cardanoFromEntropyCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromEntropyCardanoTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromEntropyCardanoTypeContainerQFrame)
        self.cardanoFromEntropyCardanoTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromEntropyCardanoTypeContainerQFrameVLayout.setObjectName(u"cardanoFromEntropyCardanoTypeContainerQFrameVLayout")
        self.cardanoFromEntropyCardanoTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromEntropyCardanoTypeContainerQFrame)
        self.cardanoFromEntropyCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromEntropyCardanoTypeLabelContainerQFrame")
        self.cardanoFromEntropyCardanoTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromEntropyCardanoTypeLabelContainerQFrame)
        self.cardanoFromEntropyCardanoTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromEntropyCardanoTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromEntropyCardanoTypeLabelContainerQFrameHLayout")
        self.cardanoFromEntropyCardanoTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyCardanoTypeQLabel = QLabel(self.cardanoFromEntropyCardanoTypeLabelContainerQFrame)
        self.cardanoFromEntropyCardanoTypeQLabel.setObjectName(u"cardanoFromEntropyCardanoTypeQLabel")

        self.cardanoFromEntropyCardanoTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromEntropyCardanoTypeQLabel)

        self.cardanoFromEntropyCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromEntropyCardanoTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromEntropyCardanoTypeLabelContainerQFrameHSpacer)


        self.cardanoFromEntropyCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromEntropyCardanoTypeLabelContainerQFrame)

        self.cardanoFromEntropyCardanoTypeQComboBox = QComboBox(self.cardanoFromEntropyCardanoTypeContainerQFrame)
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.setObjectName(u"cardanoFromEntropyCardanoTypeQComboBox")

        self.cardanoFromEntropyCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromEntropyCardanoTypeQComboBox)


        self.cardanoFromEntropyAndCardanoTypeQFrameHLayout.addWidget(self.cardanoFromEntropyCardanoTypeContainerQFrame)


        self.cardanoFromEntropyQStackedWidgetVLayout.addWidget(self.cardanoFromEntropyAndCardanoTypeQFrame)

        self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame = QFrame(self.cardanoFromEntropyQStackedWidget)
        self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame.setObjectName(u"cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame")
        self.horizontalLayout_36 = QHBoxLayout(self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame)
        self.horizontalLayout_36.setSpacing(15)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyStakingContainerQFrame = QFrame(self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame)
        self.cardanoFromEntropyStakingContainerQFrame.setObjectName(u"cardanoFromEntropyStakingContainerQFrame")
        self.XPublicKeyVLayout_11 = QVBoxLayout(self.cardanoFromEntropyStakingContainerQFrame)
        self.XPublicKeyVLayout_11.setSpacing(5)
        self.XPublicKeyVLayout_11.setObjectName(u"XPublicKeyVLayout_11")
        self.XPublicKeyVLayout_11.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyStakingLabelContainerQFrame = QFrame(self.cardanoFromEntropyStakingContainerQFrame)
        self.cardanoFromEntropyStakingLabelContainerQFrame.setObjectName(u"cardanoFromEntropyStakingLabelContainerQFrame")
        self.XPublicKeyLabelHLayout_11 = QHBoxLayout(self.cardanoFromEntropyStakingLabelContainerQFrame)
        self.XPublicKeyLabelHLayout_11.setSpacing(15)
        self.XPublicKeyLabelHLayout_11.setObjectName(u"XPublicKeyLabelHLayout_11")
        self.XPublicKeyLabelHLayout_11.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyStakingQLabel = QLabel(self.cardanoFromEntropyStakingLabelContainerQFrame)
        self.cardanoFromEntropyStakingQLabel.setObjectName(u"cardanoFromEntropyStakingQLabel")

        self.XPublicKeyLabelHLayout_11.addWidget(self.cardanoFromEntropyStakingQLabel)

        self.cardanoFromEntropyStakingLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPublicKeyLabelHLayout_11.addItem(self.cardanoFromEntropyStakingLabelContainerQFrameHSpacer)


        self.XPublicKeyVLayout_11.addWidget(self.cardanoFromEntropyStakingLabelContainerQFrame)

        self.cardanoFromEntropyStakingQLineEdit = QLineEdit(self.cardanoFromEntropyStakingContainerQFrame)
        self.cardanoFromEntropyStakingQLineEdit.setObjectName(u"cardanoFromEntropyStakingQLineEdit")

        self.XPublicKeyVLayout_11.addWidget(self.cardanoFromEntropyStakingQLineEdit)


        self.horizontalLayout_36.addWidget(self.cardanoFromEntropyStakingContainerQFrame)

        self.cardanoFromEntropyPassphraseContainerQFrame = QFrame(self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame)
        self.cardanoFromEntropyPassphraseContainerQFrame.setObjectName(u"cardanoFromEntropyPassphraseContainerQFrame")
        self.EPassphraseVLayout_5 = QVBoxLayout(self.cardanoFromEntropyPassphraseContainerQFrame)
        self.EPassphraseVLayout_5.setSpacing(5)
        self.EPassphraseVLayout_5.setObjectName(u"EPassphraseVLayout_5")
        self.EPassphraseVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyPassphraseLabelContainerQFrame = QFrame(self.cardanoFromEntropyPassphraseContainerQFrame)
        self.cardanoFromEntropyPassphraseLabelContainerQFrame.setObjectName(u"cardanoFromEntropyPassphraseLabelContainerQFrame")
        self.EPassphraseLabelHLayout_5 = QHBoxLayout(self.cardanoFromEntropyPassphraseLabelContainerQFrame)
        self.EPassphraseLabelHLayout_5.setSpacing(15)
        self.EPassphraseLabelHLayout_5.setObjectName(u"EPassphraseLabelHLayout_5")
        self.EPassphraseLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyPassphraseQLabel = QLabel(self.cardanoFromEntropyPassphraseLabelContainerQFrame)
        self.cardanoFromEntropyPassphraseQLabel.setObjectName(u"cardanoFromEntropyPassphraseQLabel")

        self.EPassphraseLabelHLayout_5.addWidget(self.cardanoFromEntropyPassphraseQLabel)

        self.cardanoFromEntropyPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_5.addItem(self.cardanoFromEntropyPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout_5.addWidget(self.cardanoFromEntropyPassphraseLabelContainerQFrame)

        self.cardanoFromEntropyPassphraseQLineEdit = QLineEdit(self.cardanoFromEntropyPassphraseContainerQFrame)
        self.cardanoFromEntropyPassphraseQLineEdit.setObjectName(u"cardanoFromEntropyPassphraseQLineEdit")

        self.EPassphraseVLayout_5.addWidget(self.cardanoFromEntropyPassphraseQLineEdit)


        self.horizontalLayout_36.addWidget(self.cardanoFromEntropyPassphraseContainerQFrame)

        self.cardanoFromEntropyAddressTypeContainerQFrame = QFrame(self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame)
        self.cardanoFromEntropyAddressTypeContainerQFrame.setObjectName(u"cardanoFromEntropyAddressTypeContainerQFrame")
        self.verticalLayout_89 = QVBoxLayout(self.cardanoFromEntropyAddressTypeContainerQFrame)
        self.verticalLayout_89.setSpacing(5)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromEntropyAddressTypeContainerQFrame)
        self.cardanoFromEntropyAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromEntropyAddressTypeLabelContainerQFrame")
        self.horizontalLayout_96 = QHBoxLayout(self.cardanoFromEntropyAddressTypeLabelContainerQFrame)
        self.horizontalLayout_96.setSpacing(15)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyAddressTypeQLabel = QLabel(self.cardanoFromEntropyAddressTypeLabelContainerQFrame)
        self.cardanoFromEntropyAddressTypeQLabel.setObjectName(u"cardanoFromEntropyAddressTypeQLabel")

        self.horizontalLayout_96.addWidget(self.cardanoFromEntropyAddressTypeQLabel)

        self.cardanoFromEntropyAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_96.addItem(self.cardanoFromEntropyAddressTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_89.addWidget(self.cardanoFromEntropyAddressTypeLabelContainerQFrame)

        self.cardanoFromEntropyAddressTypeQComboBox = QComboBox(self.cardanoFromEntropyAddressTypeContainerQFrame)
        self.cardanoFromEntropyAddressTypeQComboBox.setObjectName(u"cardanoFromEntropyAddressTypeQComboBox")

        self.verticalLayout_89.addWidget(self.cardanoFromEntropyAddressTypeQComboBox)


        self.horizontalLayout_36.addWidget(self.cardanoFromEntropyAddressTypeContainerQFrame)


        self.cardanoFromEntropyQStackedWidgetVLayout.addWidget(self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.cardanoFromEntropyQStackedWidgetVLayout.addItem(self.verticalSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromEntropyQStackedWidget)
        self.cardanoFromMnemonicQStackedWidget = QWidget()
        self.cardanoFromMnemonicQStackedWidget.setObjectName(u"cardanoFromMnemonicQStackedWidget")
        self.cardanoFromMnemonicQStackedWidgetVLayout = QVBoxLayout(self.cardanoFromMnemonicQStackedWidget)
        self.cardanoFromMnemonicQStackedWidgetVLayout.setSpacing(15)
        self.cardanoFromMnemonicQStackedWidgetVLayout.setObjectName(u"cardanoFromMnemonicQStackedWidgetVLayout")
        self.cardanoFromMnemonicQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicAndCardanoTypeQFrame = QFrame(self.cardanoFromMnemonicQStackedWidget)
        self.cardanoFromMnemonicAndCardanoTypeQFrame.setObjectName(u"cardanoFromMnemonicAndCardanoTypeQFrame")
        self.cardanoFromMnemonicAndCardanoTypeQFrameHLayout = QHBoxLayout(self.cardanoFromMnemonicAndCardanoTypeQFrame)
        self.cardanoFromMnemonicAndCardanoTypeQFrameHLayout.setSpacing(15)
        self.cardanoFromMnemonicAndCardanoTypeQFrameHLayout.setObjectName(u"cardanoFromMnemonicAndCardanoTypeQFrameHLayout")
        self.cardanoFromMnemonicAndCardanoTypeQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicContainerQFrame = QFrame(self.cardanoFromMnemonicAndCardanoTypeQFrame)
        self.cardanoFromMnemonicContainerQFrame.setObjectName(u"cardanoFromMnemonicContainerQFrame")
        self.cardanoFromMnemonicContainerQFrameVLayout = QVBoxLayout(self.cardanoFromMnemonicContainerQFrame)
        self.cardanoFromMnemonicContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromMnemonicContainerQFrameVLayout.setObjectName(u"cardanoFromMnemonicContainerQFrameVLayout")
        self.cardanoFromMnemonicContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicLabelContainerQFrame = QFrame(self.cardanoFromMnemonicContainerQFrame)
        self.cardanoFromMnemonicLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicLabelContainerQFrame")
        self.cardanoFromMnemonicLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromMnemonicLabelContainerQFrame)
        self.cardanoFromMnemonicLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromMnemonicLabelContainerQFrameHLayout.setObjectName(u"cardanoFromMnemonicLabelContainerQFrameHLayout")
        self.cardanoFromMnemonicLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicQLabel = QLabel(self.cardanoFromMnemonicLabelContainerQFrame)
        self.cardanoFromMnemonicQLabel.setObjectName(u"cardanoFromMnemonicQLabel")

        self.cardanoFromMnemonicLabelContainerQFrameHLayout.addWidget(self.cardanoFromMnemonicQLabel)

        self.cardanoFromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromMnemonicLabelContainerQFrameHLayout.addItem(self.cardanoFromMnemonicLabelContainerQFrameHSpacer)


        self.cardanoFromMnemonicContainerQFrameVLayout.addWidget(self.cardanoFromMnemonicLabelContainerQFrame)

        self.cardanoFromMnemonicGenerateContainerQFrame = QFrame(self.cardanoFromMnemonicContainerQFrame)
        self.cardanoFromMnemonicGenerateContainerQFrame.setObjectName(u"cardanoFromMnemonicGenerateContainerQFrame")
        self.cardanoFromMnemonicGenerateContainerQFrameHLayout = QHBoxLayout(self.cardanoFromMnemonicGenerateContainerQFrame)
        self.cardanoFromMnemonicGenerateContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromMnemonicGenerateContainerQFrameHLayout.setObjectName(u"cardanoFromMnemonicGenerateContainerQFrameHLayout")
        self.cardanoFromMnemonicGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicGenerateQLineEdit = QLineEdit(self.cardanoFromMnemonicGenerateContainerQFrame)
        self.cardanoFromMnemonicGenerateQLineEdit.setObjectName(u"cardanoFromMnemonicGenerateQLineEdit")

        self.cardanoFromMnemonicGenerateContainerQFrameHLayout.addWidget(self.cardanoFromMnemonicGenerateQLineEdit)


        self.cardanoFromMnemonicContainerQFrameVLayout.addWidget(self.cardanoFromMnemonicGenerateContainerQFrame)


        self.cardanoFromMnemonicAndCardanoTypeQFrameHLayout.addWidget(self.cardanoFromMnemonicContainerQFrame)

        self.cardanoFromMnemonicCardanoTypeContainerQFrame = QFrame(self.cardanoFromMnemonicAndCardanoTypeQFrame)
        self.cardanoFromMnemonicCardanoTypeContainerQFrame.setObjectName(u"cardanoFromMnemonicCardanoTypeContainerQFrame")
        self.cardanoFromMnemonicCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromMnemonicCardanoTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromMnemonicCardanoTypeContainerQFrame)
        self.cardanoFromMnemonicCardanoTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromMnemonicCardanoTypeContainerQFrameVLayout.setObjectName(u"cardanoFromMnemonicCardanoTypeContainerQFrameVLayout")
        self.cardanoFromMnemonicCardanoTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromMnemonicCardanoTypeContainerQFrame)
        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicCardanoTypeLabelContainerQFrame")
        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromMnemonicCardanoTypeLabelContainerQFrame)
        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromMnemonicCardanoTypeLabelContainerQFrameHLayout")
        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicCardanoTypeQLabel = QLabel(self.cardanoFromMnemonicCardanoTypeLabelContainerQFrame)
        self.cardanoFromMnemonicCardanoTypeQLabel.setObjectName(u"cardanoFromMnemonicCardanoTypeQLabel")

        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromMnemonicCardanoTypeQLabel)

        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromMnemonicCardanoTypeLabelContainerQFrameHSpacer)


        self.cardanoFromMnemonicCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromMnemonicCardanoTypeLabelContainerQFrame)

        self.cardanoFromMnemonicCardanoTypeQComboBox = QComboBox(self.cardanoFromMnemonicCardanoTypeContainerQFrame)
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.setObjectName(u"cardanoFromMnemonicCardanoTypeQComboBox")

        self.cardanoFromMnemonicCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromMnemonicCardanoTypeQComboBox)


        self.cardanoFromMnemonicAndCardanoTypeQFrameHLayout.addWidget(self.cardanoFromMnemonicCardanoTypeContainerQFrame)


        self.cardanoFromMnemonicQStackedWidgetVLayout.addWidget(self.cardanoFromMnemonicAndCardanoTypeQFrame)

        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame = QFrame(self.cardanoFromMnemonicQStackedWidget)
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame.setObjectName(u"cardanoFromMnemonicClientAndPassphraseContainerQFrame")
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrameHLayout = QHBoxLayout(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame)
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrameHLayout.setObjectName(u"cardanoFromMnemonicClientAndPassphraseContainerQFrameHLayout")
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicStakingContainerQFrame = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame)
        self.cardanoFromMnemonicStakingContainerQFrame.setObjectName(u"cardanoFromMnemonicStakingContainerQFrame")
        self.cardanoFromMnemonicStakingContainerQFrameVLayout = QVBoxLayout(self.cardanoFromMnemonicStakingContainerQFrame)
        self.cardanoFromMnemonicStakingContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromMnemonicStakingContainerQFrameVLayout.setObjectName(u"cardanoFromMnemonicStakingContainerQFrameVLayout")
        self.cardanoFromMnemonicStakingContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicStakingLabelContainerQFrame = QFrame(self.cardanoFromMnemonicStakingContainerQFrame)
        self.cardanoFromMnemonicStakingLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicStakingLabelContainerQFrame")
        self.cardanoFromMnemonicStakingLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromMnemonicStakingLabelContainerQFrame)
        self.cardanoFromMnemonicStakingLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromMnemonicStakingLabelContainerQFrameHLayout.setObjectName(u"cardanoFromMnemonicStakingLabelContainerQFrameHLayout")
        self.cardanoFromMnemonicStakingLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicStakingQLabel = QLabel(self.cardanoFromMnemonicStakingLabelContainerQFrame)
        self.cardanoFromMnemonicStakingQLabel.setObjectName(u"cardanoFromMnemonicStakingQLabel")

        self.cardanoFromMnemonicStakingLabelContainerQFrameHLayout.addWidget(self.cardanoFromMnemonicStakingQLabel)

        self.cardanoFromMnemonicStakingLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromMnemonicStakingLabelContainerQFrameHLayout.addItem(self.cardanoFromMnemonicStakingLabelContainerQFrameHSpacer)


        self.cardanoFromMnemonicStakingContainerQFrameVLayout.addWidget(self.cardanoFromMnemonicStakingLabelContainerQFrame)

        self.cardanoFromMnemonicStakingQLineEdit = QLineEdit(self.cardanoFromMnemonicStakingContainerQFrame)
        self.cardanoFromMnemonicStakingQLineEdit.setObjectName(u"cardanoFromMnemonicStakingQLineEdit")

        self.cardanoFromMnemonicStakingContainerQFrameVLayout.addWidget(self.cardanoFromMnemonicStakingQLineEdit)


        self.cardanoFromMnemonicClientAndPassphraseContainerQFrameHLayout.addWidget(self.cardanoFromMnemonicStakingContainerQFrame)

        self.cardanoFromMnemonicAddressTypeContainerQFrame = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame)
        self.cardanoFromMnemonicAddressTypeContainerQFrame.setObjectName(u"cardanoFromMnemonicAddressTypeContainerQFrame")
        self.cardanoFromMnemonicAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromMnemonicAddressTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromMnemonicAddressTypeContainerQFrame)
        self.cardanoFromMnemonicAddressTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromMnemonicAddressTypeContainerQFrameVLayout.setObjectName(u"cardanoFromMnemonicAddressTypeContainerQFrameVLayout")
        self.cardanoFromMnemonicAddressTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromMnemonicAddressTypeContainerQFrame)
        self.cardanoFromMnemonicAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicAddressTypeLabelContainerQFrame")
        self.cardanoFromMnemonicAddressTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromMnemonicAddressTypeLabelContainerQFrame)
        self.cardanoFromMnemonicAddressTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromMnemonicAddressTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromMnemonicAddressTypeLabelContainerQFrameHLayout")
        self.cardanoFromMnemonicAddressTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicAddressTypeQLabel = QLabel(self.cardanoFromMnemonicAddressTypeLabelContainerQFrame)
        self.cardanoFromMnemonicAddressTypeQLabel.setObjectName(u"cardanoFromMnemonicAddressTypeQLabel")

        self.cardanoFromMnemonicAddressTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromMnemonicAddressTypeQLabel)

        self.cardanoFromMnemonicAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromMnemonicAddressTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromMnemonicAddressTypeLabelContainerQFrameHSpacer)


        self.cardanoFromMnemonicAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromMnemonicAddressTypeLabelContainerQFrame)

        self.cardanoFromMnemonicAddressTypeQComboBox = QComboBox(self.cardanoFromMnemonicAddressTypeContainerQFrame)
        self.cardanoFromMnemonicAddressTypeQComboBox.setObjectName(u"cardanoFromMnemonicAddressTypeQComboBox")

        self.cardanoFromMnemonicAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromMnemonicAddressTypeQComboBox)


        self.cardanoFromMnemonicClientAndPassphraseContainerQFrameHLayout.addWidget(self.cardanoFromMnemonicAddressTypeContainerQFrame)

        self.cardanoFromMnemonicPassphraseContainerQFrame = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame)
        self.cardanoFromMnemonicPassphraseContainerQFrame.setObjectName(u"cardanoFromMnemonicPassphraseContainerQFrame")
        self.cardanoFromMnemonicPassphraseContainerQFrameVLayout = QVBoxLayout(self.cardanoFromMnemonicPassphraseContainerQFrame)
        self.cardanoFromMnemonicPassphraseContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromMnemonicPassphraseContainerQFrameVLayout.setObjectName(u"cardanoFromMnemonicPassphraseContainerQFrameVLayout")
        self.cardanoFromMnemonicPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicPassphraseLabelContainerQFrame = QFrame(self.cardanoFromMnemonicPassphraseContainerQFrame)
        self.cardanoFromMnemonicPassphraseLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicPassphraseLabelContainerQFrame")
        self.cardanoFromMnemonicPassphraseLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromMnemonicPassphraseLabelContainerQFrame)
        self.cardanoFromMnemonicPassphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromMnemonicPassphraseLabelContainerQFrameHLayout.setObjectName(u"cardanoFromMnemonicPassphraseLabelContainerQFrameHLayout")
        self.cardanoFromMnemonicPassphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicPassphraseQLabel = QLabel(self.cardanoFromMnemonicPassphraseLabelContainerQFrame)
        self.cardanoFromMnemonicPassphraseQLabel.setObjectName(u"cardanoFromMnemonicPassphraseQLabel")

        self.cardanoFromMnemonicPassphraseLabelContainerQFrameHLayout.addWidget(self.cardanoFromMnemonicPassphraseQLabel)

        self.cardanoFromMnemonicPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromMnemonicPassphraseLabelContainerQFrameHLayout.addItem(self.cardanoFromMnemonicPassphraseLabelContainerQFrameHSpacer)


        self.cardanoFromMnemonicPassphraseContainerQFrameVLayout.addWidget(self.cardanoFromMnemonicPassphraseLabelContainerQFrame)

        self.cardanoFromMnemonicPassphraseGenerateContainerQFrame = QFrame(self.cardanoFromMnemonicPassphraseContainerQFrame)
        self.cardanoFromMnemonicPassphraseGenerateContainerQFrame.setObjectName(u"cardanoFromMnemonicPassphraseGenerateContainerQFrame")
        self.cardanoFromMnemonicPassphraseGenerateContainerQFrameHLayout = QHBoxLayout(self.cardanoFromMnemonicPassphraseGenerateContainerQFrame)
        self.cardanoFromMnemonicPassphraseGenerateContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromMnemonicPassphraseGenerateContainerQFrameHLayout.setObjectName(u"cardanoFromMnemonicPassphraseGenerateContainerQFrameHLayout")
        self.cardanoFromMnemonicPassphraseGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicPassphraseQLineEdit = QLineEdit(self.cardanoFromMnemonicPassphraseGenerateContainerQFrame)
        self.cardanoFromMnemonicPassphraseQLineEdit.setObjectName(u"cardanoFromMnemonicPassphraseQLineEdit")

        self.cardanoFromMnemonicPassphraseGenerateContainerQFrameHLayout.addWidget(self.cardanoFromMnemonicPassphraseQLineEdit)


        self.cardanoFromMnemonicPassphraseContainerQFrameVLayout.addWidget(self.cardanoFromMnemonicPassphraseGenerateContainerQFrame)


        self.cardanoFromMnemonicClientAndPassphraseContainerQFrameHLayout.addWidget(self.cardanoFromMnemonicPassphraseContainerQFrame)


        self.cardanoFromMnemonicQStackedWidgetVLayout.addWidget(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame)

        self.cardanoFromMnemonicClientAndPassphraseContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.cardanoFromMnemonicQStackedWidgetVLayout.addItem(self.cardanoFromMnemonicClientAndPassphraseContainerQFrameVSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromMnemonicQStackedWidget)
        self.cardanoFromSeedQStackedWidget = QWidget()
        self.cardanoFromSeedQStackedWidget.setObjectName(u"cardanoFromSeedQStackedWidget")
        self.cardanoFromSeedQStackedWidgetVLayout = QVBoxLayout(self.cardanoFromSeedQStackedWidget)
        self.cardanoFromSeedQStackedWidgetVLayout.setSpacing(15)
        self.cardanoFromSeedQStackedWidgetVLayout.setObjectName(u"cardanoFromSeedQStackedWidgetVLayout")
        self.cardanoFromSeedQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedAndCardanoContainerQFrame = QFrame(self.cardanoFromSeedQStackedWidget)
        self.cardanoFromSeedAndCardanoContainerQFrame.setObjectName(u"cardanoFromSeedAndCardanoContainerQFrame")
        self.cardanoFromSeedAndCardanoContainerQFrameHLayout = QHBoxLayout(self.cardanoFromSeedAndCardanoContainerQFrame)
        self.cardanoFromSeedAndCardanoContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromSeedAndCardanoContainerQFrameHLayout.setObjectName(u"cardanoFromSeedAndCardanoContainerQFrameHLayout")
        self.cardanoFromSeedAndCardanoContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedContainerQFrame = QFrame(self.cardanoFromSeedAndCardanoContainerQFrame)
        self.cardanoFromSeedContainerQFrame.setObjectName(u"cardanoFromSeedContainerQFrame")
        self.cardanoFromSeedContainerQFrameVLayout = QVBoxLayout(self.cardanoFromSeedContainerQFrame)
        self.cardanoFromSeedContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromSeedContainerQFrameVLayout.setObjectName(u"cardanoFromSeedContainerQFrameVLayout")
        self.cardanoFromSeedContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedLabelContainerQFrame = QFrame(self.cardanoFromSeedContainerQFrame)
        self.cardanoFromSeedLabelContainerQFrame.setObjectName(u"cardanoFromSeedLabelContainerQFrame")
        self.cardanoFromSeedLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromSeedLabelContainerQFrame)
        self.cardanoFromSeedLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromSeedLabelContainerQFrameHLayout.setObjectName(u"cardanoFromSeedLabelContainerQFrameHLayout")
        self.cardanoFromSeedLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedQLabel = QLabel(self.cardanoFromSeedLabelContainerQFrame)
        self.cardanoFromSeedQLabel.setObjectName(u"cardanoFromSeedQLabel")

        self.cardanoFromSeedLabelContainerQFrameHLayout.addWidget(self.cardanoFromSeedQLabel)

        self.cardanoFromSeedLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromSeedLabelContainerQFrameHLayout.addItem(self.cardanoFromSeedLabelContainerQFrameHSpacer)


        self.cardanoFromSeedContainerQFrameVLayout.addWidget(self.cardanoFromSeedLabelContainerQFrame)

        self.cardanoFromSeedQLineEdit = QLineEdit(self.cardanoFromSeedContainerQFrame)
        self.cardanoFromSeedQLineEdit.setObjectName(u"cardanoFromSeedQLineEdit")

        self.cardanoFromSeedContainerQFrameVLayout.addWidget(self.cardanoFromSeedQLineEdit)


        self.cardanoFromSeedAndCardanoContainerQFrameHLayout.addWidget(self.cardanoFromSeedContainerQFrame)

        self.cardanoFromSeedCardanoTypeContainerQFrame = QFrame(self.cardanoFromSeedAndCardanoContainerQFrame)
        self.cardanoFromSeedCardanoTypeContainerQFrame.setObjectName(u"cardanoFromSeedCardanoTypeContainerQFrame")
        self.cardanoFromSeedCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromSeedCardanoTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromSeedCardanoTypeContainerQFrame)
        self.cardanoFromSeedCardanoTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromSeedCardanoTypeContainerQFrameVLayout.setObjectName(u"cardanoFromSeedCardanoTypeContainerQFrameVLayout")
        self.cardanoFromSeedCardanoTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromSeedCardanoTypeContainerQFrame)
        self.cardanoFromSeedCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromSeedCardanoTypeLabelContainerQFrame")
        self.cardanoFromSeedCardanoTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromSeedCardanoTypeLabelContainerQFrame)
        self.cardanoFromSeedCardanoTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromSeedCardanoTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromSeedCardanoTypeLabelContainerQFrameHLayout")
        self.cardanoFromSeedCardanoTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedCardanoTypeQLabel = QLabel(self.cardanoFromSeedCardanoTypeLabelContainerQFrame)
        self.cardanoFromSeedCardanoTypeQLabel.setObjectName(u"cardanoFromSeedCardanoTypeQLabel")

        self.cardanoFromSeedCardanoTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromSeedCardanoTypeQLabel)

        self.cardanoFromSeedCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromSeedCardanoTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromSeedCardanoTypeLabelContainerQFrameHSpacer)


        self.cardanoFromSeedCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromSeedCardanoTypeLabelContainerQFrame)

        self.cardanoFromSeedCardanoTypeQComboBox = QComboBox(self.cardanoFromSeedCardanoTypeContainerQFrame)
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.setObjectName(u"cardanoFromSeedCardanoTypeQComboBox")

        self.cardanoFromSeedCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromSeedCardanoTypeQComboBox)


        self.cardanoFromSeedAndCardanoContainerQFrameHLayout.addWidget(self.cardanoFromSeedCardanoTypeContainerQFrame)


        self.cardanoFromSeedQStackedWidgetVLayout.addWidget(self.cardanoFromSeedAndCardanoContainerQFrame)

        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame = QFrame(self.cardanoFromSeedQStackedWidget)
        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame.setObjectName(u"cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame")
        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrameHLayout = QHBoxLayout(self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame)
        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrameHLayout.setObjectName(u"cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrameHLayout")
        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedStakingContainerQFrame = QFrame(self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame)
        self.cardanoFromSeedStakingContainerQFrame.setObjectName(u"cardanoFromSeedStakingContainerQFrame")
        self.cardanoFromSeedStakingContainerQFrameVLayout = QVBoxLayout(self.cardanoFromSeedStakingContainerQFrame)
        self.cardanoFromSeedStakingContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromSeedStakingContainerQFrameVLayout.setObjectName(u"cardanoFromSeedStakingContainerQFrameVLayout")
        self.cardanoFromSeedStakingContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedStakingLabelContainerQFrame = QFrame(self.cardanoFromSeedStakingContainerQFrame)
        self.cardanoFromSeedStakingLabelContainerQFrame.setObjectName(u"cardanoFromSeedStakingLabelContainerQFrame")
        self.cardanoFromSeedStakingLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromSeedStakingLabelContainerQFrame)
        self.cardanoFromSeedStakingLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromSeedStakingLabelContainerQFrameHLayout.setObjectName(u"cardanoFromSeedStakingLabelContainerQFrameHLayout")
        self.cardanoFromSeedStakingLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedStakingQLabel = QLabel(self.cardanoFromSeedStakingLabelContainerQFrame)
        self.cardanoFromSeedStakingQLabel.setObjectName(u"cardanoFromSeedStakingQLabel")

        self.cardanoFromSeedStakingLabelContainerQFrameHLayout.addWidget(self.cardanoFromSeedStakingQLabel)

        self.cardanoFromSeedStakingLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromSeedStakingLabelContainerQFrameHLayout.addItem(self.cardanoFromSeedStakingLabelContainerQFrameHSpacer)


        self.cardanoFromSeedStakingContainerQFrameVLayout.addWidget(self.cardanoFromSeedStakingLabelContainerQFrame)

        self.cardanoFromSeedStakingQLineEdit = QLineEdit(self.cardanoFromSeedStakingContainerQFrame)
        self.cardanoFromSeedStakingQLineEdit.setObjectName(u"cardanoFromSeedStakingQLineEdit")

        self.cardanoFromSeedStakingContainerQFrameVLayout.addWidget(self.cardanoFromSeedStakingQLineEdit)


        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrameHLayout.addWidget(self.cardanoFromSeedStakingContainerQFrame)

        self.cardanoFromSeedAddressTypeContainerQFrame = QFrame(self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame)
        self.cardanoFromSeedAddressTypeContainerQFrame.setObjectName(u"cardanoFromSeedAddressTypeContainerQFrame")
        self.cardanoFromSeedAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromSeedAddressTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromSeedAddressTypeContainerQFrame)
        self.cardanoFromSeedAddressTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromSeedAddressTypeContainerQFrameVLayout.setObjectName(u"cardanoFromSeedAddressTypeContainerQFrameVLayout")
        self.cardanoFromSeedAddressTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromSeedAddressTypeContainerQFrame)
        self.cardanoFromSeedAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromSeedAddressTypeLabelContainerQFrame")
        self.cardanoFromSeedAddressTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromSeedAddressTypeLabelContainerQFrame)
        self.cardanoFromSeedAddressTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromSeedAddressTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromSeedAddressTypeLabelContainerQFrameHLayout")
        self.cardanoFromSeedAddressTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedAddressTypeQLabel = QLabel(self.cardanoFromSeedAddressTypeLabelContainerQFrame)
        self.cardanoFromSeedAddressTypeQLabel.setObjectName(u"cardanoFromSeedAddressTypeQLabel")

        self.cardanoFromSeedAddressTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromSeedAddressTypeQLabel)

        self.cardanoFromSeedAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromSeedAddressTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromSeedAddressTypeLabelContainerQFrameHSpacer)


        self.cardanoFromSeedAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromSeedAddressTypeLabelContainerQFrame)

        self.cardanoFromSeedAddressTypeQComboBox = QComboBox(self.cardanoFromSeedAddressTypeContainerQFrame)
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.setObjectName(u"cardanoFromSeedAddressTypeQComboBox")

        self.cardanoFromSeedAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromSeedAddressTypeQComboBox)


        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrameHLayout.addWidget(self.cardanoFromSeedAddressTypeContainerQFrame)

        self.cardanoFromSeedPassphraseContainerQFrame = QFrame(self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame)
        self.cardanoFromSeedPassphraseContainerQFrame.setObjectName(u"cardanoFromSeedPassphraseContainerQFrame")
        self.cardanoFromSeedPassphraseContainerQFrameVLayout = QVBoxLayout(self.cardanoFromSeedPassphraseContainerQFrame)
        self.cardanoFromSeedPassphraseContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromSeedPassphraseContainerQFrameVLayout.setObjectName(u"cardanoFromSeedPassphraseContainerQFrameVLayout")
        self.cardanoFromSeedPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedPassphraseLabelContainerQFrame = QFrame(self.cardanoFromSeedPassphraseContainerQFrame)
        self.cardanoFromSeedPassphraseLabelContainerQFrame.setObjectName(u"cardanoFromSeedPassphraseLabelContainerQFrame")
        self.cardanoFromSeedPassphraseLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromSeedPassphraseLabelContainerQFrame)
        self.cardanoFromSeedPassphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromSeedPassphraseLabelContainerQFrameHLayout.setObjectName(u"cardanoFromSeedPassphraseLabelContainerQFrameHLayout")
        self.cardanoFromSeedPassphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedPassphraseQLabel = QLabel(self.cardanoFromSeedPassphraseLabelContainerQFrame)
        self.cardanoFromSeedPassphraseQLabel.setObjectName(u"cardanoFromSeedPassphraseQLabel")

        self.cardanoFromSeedPassphraseLabelContainerQFrameHLayout.addWidget(self.cardanoFromSeedPassphraseQLabel)

        self.cardanoFromSeedPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromSeedPassphraseLabelContainerQFrameHLayout.addItem(self.cardanoFromSeedPassphraseLabelContainerQFrameHSpacer)


        self.cardanoFromSeedPassphraseContainerQFrameVLayout.addWidget(self.cardanoFromSeedPassphraseLabelContainerQFrame)

        self.cardanoFromSeedPassphraseQLineEdit = QLineEdit(self.cardanoFromSeedPassphraseContainerQFrame)
        self.cardanoFromSeedPassphraseQLineEdit.setObjectName(u"cardanoFromSeedPassphraseQLineEdit")

        self.cardanoFromSeedPassphraseContainerQFrameVLayout.addWidget(self.cardanoFromSeedPassphraseQLineEdit)


        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrameHLayout.addWidget(self.cardanoFromSeedPassphraseContainerQFrame)


        self.cardanoFromSeedQStackedWidgetVLayout.addWidget(self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame)

        self.cardanoFromSeedQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.cardanoFromSeedQStackedWidgetVLayout.addItem(self.cardanoFromSeedQStackedWidgetVSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromSeedQStackedWidget)
        self.cardanoFromXPrivateKeyQStackedWidget = QWidget()
        self.cardanoFromXPrivateKeyQStackedWidget.setObjectName(u"cardanoFromXPrivateKeyQStackedWidget")
        self.cardanoFromXPrivateKeyQStackedWidgetVLayout = QVBoxLayout(self.cardanoFromXPrivateKeyQStackedWidget)
        self.cardanoFromXPrivateKeyQStackedWidgetVLayout.setSpacing(15)
        self.cardanoFromXPrivateKeyQStackedWidgetVLayout.setObjectName(u"cardanoFromXPrivateKeyQStackedWidgetVLayout")
        self.cardanoFromXPrivateKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrame = QFrame(self.cardanoFromXPrivateKeyQStackedWidget)
        self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrame")
        self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrame)
        self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrameHLayout.setObjectName(u"cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrameHLayout")
        self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyContainerQFrame = QFrame(self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrame)
        self.cardanoFromXPrivateKeyContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyContainerQFrame")
        self.cardanoFromXPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.cardanoFromXPrivateKeyContainerQFrame)
        self.cardanoFromXPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromXPrivateKeyContainerQFrameVLayout.setObjectName(u"cardanoFromXPrivateKeyContainerQFrameVLayout")
        self.cardanoFromXPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyLabelContainerQFrame = QFrame(self.cardanoFromXPrivateKeyContainerQFrame)
        self.cardanoFromXPrivateKeyLabelContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyLabelContainerQFrame")
        self.cardanoFromXPrivateKeyLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPrivateKeyLabelContainerQFrame)
        self.cardanoFromXPrivateKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPrivateKeyLabelContainerQFrameHLayout.setObjectName(u"cardanoFromXPrivateKeyLabelContainerQFrameHLayout")
        self.cardanoFromXPrivateKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyQLabel = QLabel(self.cardanoFromXPrivateKeyLabelContainerQFrame)
        self.cardanoFromXPrivateKeyQLabel.setObjectName(u"cardanoFromXPrivateKeyQLabel")

        self.cardanoFromXPrivateKeyLabelContainerQFrameHLayout.addWidget(self.cardanoFromXPrivateKeyQLabel)

        self.cardanoFromXPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromXPrivateKeyLabelContainerQFrameHLayout.addItem(self.cardanoFromXPrivateKeyLabelContainerQFrameHSpacer)


        self.cardanoFromXPrivateKeyContainerQFrameVLayout.addWidget(self.cardanoFromXPrivateKeyLabelContainerQFrame)

        self.cardanoFromXPrivateKeyQLineEdit = QLineEdit(self.cardanoFromXPrivateKeyContainerQFrame)
        self.cardanoFromXPrivateKeyQLineEdit.setObjectName(u"cardanoFromXPrivateKeyQLineEdit")

        self.cardanoFromXPrivateKeyContainerQFrameVLayout.addWidget(self.cardanoFromXPrivateKeyQLineEdit)


        self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrameHLayout.addWidget(self.cardanoFromXPrivateKeyContainerQFrame)

        self.cardanoFromXPrivateKeyStrictQCheckBox = QCheckBox(self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrame)
        self.cardanoFromXPrivateKeyStrictQCheckBox.setObjectName(u"cardanoFromXPrivateKeyStrictQCheckBox")

        self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrameHLayout.addWidget(self.cardanoFromXPrivateKeyStrictQCheckBox, 0, Qt.AlignVCenter)

        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame = QFrame(self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeContainerQFrame")
        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrameVLayout.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeContainerQFrameVLayout")
        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame")
        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHLayout")
        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyCardanoTypeQLabel = QLabel(self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeQLabel.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeQLabel")

        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromXPrivateKeyCardanoTypeQLabel)

        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHSpacer)


        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame)

        self.cardanoFromXPrivateKeyCardanoTypeQComboBox = QComboBox(self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeQComboBox")

        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromXPrivateKeyCardanoTypeQComboBox)


        self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrameHLayout.addWidget(self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame)


        self.cardanoFromXPrivateKeyQStackedWidgetVLayout.addWidget(self.cardanoFromXPrivateKeyStrictXPrivateKeyContainerQFrame)

        self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame = QFrame(self.cardanoFromXPrivateKeyQStackedWidget)
        self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame")
        self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout")
        self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyStakingContainerQFrame = QFrame(self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromXPrivateKeyStakingContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyStakingContainerQFrame")
        self.cardanoFromXPrivateKeyStakingContainerQFrameVLayout = QVBoxLayout(self.cardanoFromXPrivateKeyStakingContainerQFrame)
        self.cardanoFromXPrivateKeyStakingContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromXPrivateKeyStakingContainerQFrameVLayout.setObjectName(u"cardanoFromXPrivateKeyStakingContainerQFrameVLayout")
        self.cardanoFromXPrivateKeyStakingContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyStakingLabelContainerQFrame = QFrame(self.cardanoFromXPrivateKeyStakingContainerQFrame)
        self.cardanoFromXPrivateKeyStakingLabelContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyStakingLabelContainerQFrame")
        self.cardanoFromXPrivateKeyStakingLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPrivateKeyStakingLabelContainerQFrame)
        self.cardanoFromXPrivateKeyStakingLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPrivateKeyStakingLabelContainerQFrameHLayout.setObjectName(u"cardanoFromXPrivateKeyStakingLabelContainerQFrameHLayout")
        self.cardanoFromXPrivateKeyStakingLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyStakingQLabel = QLabel(self.cardanoFromXPrivateKeyStakingLabelContainerQFrame)
        self.cardanoFromXPrivateKeyStakingQLabel.setObjectName(u"cardanoFromXPrivateKeyStakingQLabel")

        self.cardanoFromXPrivateKeyStakingLabelContainerQFrameHLayout.addWidget(self.cardanoFromXPrivateKeyStakingQLabel)

        self.cardanoFromXPrivateKeyStakingLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromXPrivateKeyStakingLabelContainerQFrameHLayout.addItem(self.cardanoFromXPrivateKeyStakingLabelContainerQFrameHSpacer)


        self.cardanoFromXPrivateKeyStakingContainerQFrameVLayout.addWidget(self.cardanoFromXPrivateKeyStakingLabelContainerQFrame)

        self.cardanoFromXPrivateKeyStakingQLineEdit = QLineEdit(self.cardanoFromXPrivateKeyStakingContainerQFrame)
        self.cardanoFromXPrivateKeyStakingQLineEdit.setObjectName(u"cardanoFromXPrivateKeyStakingQLineEdit")

        self.cardanoFromXPrivateKeyStakingContainerQFrameVLayout.addWidget(self.cardanoFromXPrivateKeyStakingQLineEdit)


        self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.addWidget(self.cardanoFromXPrivateKeyStakingContainerQFrame)

        self.cardanoFromXPrivateKeyAddressTypeContainerQFrame = QFrame(self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromXPrivateKeyAddressTypeContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyAddressTypeContainerQFrame")
        self.cardanoFromXPrivateKeyAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromXPrivateKeyAddressTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromXPrivateKeyAddressTypeContainerQFrame)
        self.cardanoFromXPrivateKeyAddressTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromXPrivateKeyAddressTypeContainerQFrameVLayout.setObjectName(u"cardanoFromXPrivateKeyAddressTypeContainerQFrameVLayout")
        self.cardanoFromXPrivateKeyAddressTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromXPrivateKeyAddressTypeContainerQFrame)
        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame")
        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHLayout")
        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyAddressTypeQLabel = QLabel(self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromXPrivateKeyAddressTypeQLabel.setObjectName(u"cardanoFromXPrivateKeyAddressTypeQLabel")

        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromXPrivateKeyAddressTypeQLabel)

        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHSpacer)


        self.cardanoFromXPrivateKeyAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame)

        self.cardanoFromXPrivateKeyAddressTypeQComboBox = QComboBox(self.cardanoFromXPrivateKeyAddressTypeContainerQFrame)
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setObjectName(u"cardanoFromXPrivateKeyAddressTypeQComboBox")

        self.cardanoFromXPrivateKeyAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromXPrivateKeyAddressTypeQComboBox)


        self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.addWidget(self.cardanoFromXPrivateKeyAddressTypeContainerQFrame)


        self.cardanoFromXPrivateKeyQStackedWidgetVLayout.addWidget(self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)

        self.cardanoFromXPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.cardanoFromXPrivateKeyQStackedWidgetVLayout.addItem(self.cardanoFromXPrivateKeyQStackedWidgetVSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromXPrivateKeyQStackedWidget)
        self.cardanoFromXPublicKeyQStackedWidget = QWidget()
        self.cardanoFromXPublicKeyQStackedWidget.setObjectName(u"cardanoFromXPublicKeyQStackedWidget")
        self.cardanoFromXPublicKeyQStackedWidgetVLayout = QVBoxLayout(self.cardanoFromXPublicKeyQStackedWidget)
        self.cardanoFromXPublicKeyQStackedWidgetVLayout.setSpacing(15)
        self.cardanoFromXPublicKeyQStackedWidgetVLayout.setObjectName(u"cardanoFromXPublicKeyQStackedWidgetVLayout")
        self.cardanoFromXPublicKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrame = QFrame(self.cardanoFromXPublicKeyQStackedWidget)
        self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrame.setObjectName(u"cardanoFromXPublicKeyStrictXPublicKeyContainerQFrame")
        self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrame)
        self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrameHLayout.setObjectName(u"cardanoFromXPublicKeyStrictXPublicKeyContainerQFrameHLayout")
        self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyContainerQFrame = QFrame(self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrame)
        self.cardanoFromXPublicKeyContainerQFrame.setObjectName(u"cardanoFromXPublicKeyContainerQFrame")
        self.cardanoFromXPublicKeyContainerQFrameVLayout = QVBoxLayout(self.cardanoFromXPublicKeyContainerQFrame)
        self.cardanoFromXPublicKeyContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromXPublicKeyContainerQFrameVLayout.setObjectName(u"cardanoFromXPublicKeyContainerQFrameVLayout")
        self.cardanoFromXPublicKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyLabelContainerQFrame = QFrame(self.cardanoFromXPublicKeyContainerQFrame)
        self.cardanoFromXPublicKeyLabelContainerQFrame.setObjectName(u"cardanoFromXPublicKeyLabelContainerQFrame")
        self.cardanoFromXPublicKeyLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPublicKeyLabelContainerQFrame)
        self.cardanoFromXPublicKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPublicKeyLabelContainerQFrameHLayout.setObjectName(u"cardanoFromXPublicKeyLabelContainerQFrameHLayout")
        self.cardanoFromXPublicKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 15, 0)
        self.cardanoFromXPublicKeyQLabel = QLabel(self.cardanoFromXPublicKeyLabelContainerQFrame)
        self.cardanoFromXPublicKeyQLabel.setObjectName(u"cardanoFromXPublicKeyQLabel")

        self.cardanoFromXPublicKeyLabelContainerQFrameHLayout.addWidget(self.cardanoFromXPublicKeyQLabel)

        self.cardanoFromXPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromXPublicKeyLabelContainerQFrameHLayout.addItem(self.cardanoFromXPublicKeyLabelContainerQFrameHSpacer)

        self.cardanoFromXPublicKeyStrictQCheckBox = QCheckBox(self.cardanoFromXPublicKeyLabelContainerQFrame)
        self.cardanoFromXPublicKeyStrictQCheckBox.setObjectName(u"cardanoFromXPublicKeyStrictQCheckBox")

        self.cardanoFromXPublicKeyLabelContainerQFrameHLayout.addWidget(self.cardanoFromXPublicKeyStrictQCheckBox)


        self.cardanoFromXPublicKeyContainerQFrameVLayout.addWidget(self.cardanoFromXPublicKeyLabelContainerQFrame)

        self.cardanoFromXPublicKeyQLineEdit = QLineEdit(self.cardanoFromXPublicKeyContainerQFrame)
        self.cardanoFromXPublicKeyQLineEdit.setObjectName(u"cardanoFromXPublicKeyQLineEdit")

        self.cardanoFromXPublicKeyContainerQFrameVLayout.addWidget(self.cardanoFromXPublicKeyQLineEdit)


        self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrameHLayout.addWidget(self.cardanoFromXPublicKeyContainerQFrame)

        self.cardanoFromXPublicKeyCardanoTypeContainerQFrame = QFrame(self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeContainerQFrame.setObjectName(u"cardanoFromXPublicKeyCardanoTypeContainerQFrame")
        self.cardanoFromXPublicKeyCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromXPublicKeyCardanoTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromXPublicKeyCardanoTypeContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromXPublicKeyCardanoTypeContainerQFrameVLayout.setObjectName(u"cardanoFromXPublicKeyCardanoTypeContainerQFrameVLayout")
        self.cardanoFromXPublicKeyCardanoTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromXPublicKeyCardanoTypeContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame")
        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHLayout")
        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyCardanoTypeQLabel = QLabel(self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeQLabel.setObjectName(u"cardanoFromXPublicKeyCardanoTypeQLabel")

        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromXPublicKeyCardanoTypeQLabel)

        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHSpacer)


        self.cardanoFromXPublicKeyCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame)

        self.cardanoFromXPublicKeyCardanoTypeQComboBox = QComboBox(self.cardanoFromXPublicKeyCardanoTypeContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setObjectName(u"cardanoFromXPublicKeyCardanoTypeQComboBox")

        self.cardanoFromXPublicKeyCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromXPublicKeyCardanoTypeQComboBox)


        self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrameHLayout.addWidget(self.cardanoFromXPublicKeyCardanoTypeContainerQFrame)


        self.cardanoFromXPublicKeyQStackedWidgetVLayout.addWidget(self.cardanoFromXPublicKeyStrictXPublicKeyContainerQFrame)

        self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame = QFrame(self.cardanoFromXPublicKeyQStackedWidget)
        self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame.setObjectName(u"cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame")
        self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setObjectName(u"cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout")
        self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyStakingContainerQFrame = QFrame(self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromXPublicKeyStakingContainerQFrame.setObjectName(u"cardanoFromXPublicKeyStakingContainerQFrame")
        self.cardanoFromXPublicKeyStakingContainerQFrameVLayout = QVBoxLayout(self.cardanoFromXPublicKeyStakingContainerQFrame)
        self.cardanoFromXPublicKeyStakingContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromXPublicKeyStakingContainerQFrameVLayout.setObjectName(u"cardanoFromXPublicKeyStakingContainerQFrameVLayout")
        self.cardanoFromXPublicKeyStakingContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyStakingLabelContainerQFrame = QFrame(self.cardanoFromXPublicKeyStakingContainerQFrame)
        self.cardanoFromXPublicKeyStakingLabelContainerQFrame.setObjectName(u"cardanoFromXPublicKeyStakingLabelContainerQFrame")
        self.cardanoFromXPublicKeyStakingLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPublicKeyStakingLabelContainerQFrame)
        self.cardanoFromXPublicKeyStakingLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPublicKeyStakingLabelContainerQFrameHLayout.setObjectName(u"cardanoFromXPublicKeyStakingLabelContainerQFrameHLayout")
        self.cardanoFromXPublicKeyStakingLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyStakingQLabel = QLabel(self.cardanoFromXPublicKeyStakingLabelContainerQFrame)
        self.cardanoFromXPublicKeyStakingQLabel.setObjectName(u"cardanoFromXPublicKeyStakingQLabel")

        self.cardanoFromXPublicKeyStakingLabelContainerQFrameHLayout.addWidget(self.cardanoFromXPublicKeyStakingQLabel)

        self.cardanoFromXPublicKeyStakingLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromXPublicKeyStakingLabelContainerQFrameHLayout.addItem(self.cardanoFromXPublicKeyStakingLabelContainerQFrameHSpacer)


        self.cardanoFromXPublicKeyStakingContainerQFrameVLayout.addWidget(self.cardanoFromXPublicKeyStakingLabelContainerQFrame)

        self.cardanoFromXPublicKeyStakingQLineEdit = QLineEdit(self.cardanoFromXPublicKeyStakingContainerQFrame)
        self.cardanoFromXPublicKeyStakingQLineEdit.setObjectName(u"cardanoFromXPublicKeyStakingQLineEdit")

        self.cardanoFromXPublicKeyStakingContainerQFrameVLayout.addWidget(self.cardanoFromXPublicKeyStakingQLineEdit)


        self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.addWidget(self.cardanoFromXPublicKeyStakingContainerQFrame)

        self.cardanoFromXPublicKeyAddressTypeContainerQFrame = QFrame(self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromXPublicKeyAddressTypeContainerQFrame.setObjectName(u"cardanoFromXPublicKeyAddressTypeContainerQFrame")
        self.cardanoFromXPublicKeyAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromXPublicKeyAddressTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromXPublicKeyAddressTypeContainerQFrame)
        self.cardanoFromXPublicKeyAddressTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromXPublicKeyAddressTypeContainerQFrameVLayout.setObjectName(u"cardanoFromXPublicKeyAddressTypeContainerQFrameVLayout")
        self.cardanoFromXPublicKeyAddressTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromXPublicKeyAddressTypeContainerQFrame)
        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromXPublicKeyAddressTypeLabelContainerQFrame")
        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHLayout")
        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyAddressTypeQLabel = QLabel(self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromXPublicKeyAddressTypeQLabel.setObjectName(u"cardanoFromXPublicKeyAddressTypeQLabel")

        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromXPublicKeyAddressTypeQLabel)

        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHSpacer)


        self.cardanoFromXPublicKeyAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrame)

        self.cardanoFromXPublicKeyAddressTypeQComboBox = QComboBox(self.cardanoFromXPublicKeyAddressTypeContainerQFrame)
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setObjectName(u"cardanoFromXPublicKeyAddressTypeQComboBox")

        self.cardanoFromXPublicKeyAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromXPublicKeyAddressTypeQComboBox)


        self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.addWidget(self.cardanoFromXPublicKeyAddressTypeContainerQFrame)


        self.cardanoFromXPublicKeyQStackedWidgetVLayout.addWidget(self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame)

        self.cardanoFromXPublicKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.cardanoFromXPublicKeyQStackedWidgetVLayout.addItem(self.cardanoFromXPublicKeyQStackedWidgetVSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromXPublicKeyQStackedWidget)
        self.cardanoFromPrivateKeyQStackedWidget = QWidget()
        self.cardanoFromPrivateKeyQStackedWidget.setObjectName(u"cardanoFromPrivateKeyQStackedWidget")
        self.cardanoFromPrivateKeyQStackedWidgetVLayout = QVBoxLayout(self.cardanoFromPrivateKeyQStackedWidget)
        self.cardanoFromPrivateKeyQStackedWidgetVLayout.setSpacing(15)
        self.cardanoFromPrivateKeyQStackedWidgetVLayout.setObjectName(u"cardanoFromPrivateKeyQStackedWidgetVLayout")
        self.cardanoFromPrivateKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyAndCardanoTypeQFrame = QFrame(self.cardanoFromPrivateKeyQStackedWidget)
        self.cardanoFromPrivateKeyAndCardanoTypeQFrame.setObjectName(u"cardanoFromPrivateKeyAndCardanoTypeQFrame")
        self.cardanoFromPrivateKeyAndCardanoTypeQFrameHLayout = QHBoxLayout(self.cardanoFromPrivateKeyAndCardanoTypeQFrame)
        self.cardanoFromPrivateKeyAndCardanoTypeQFrameHLayout.setSpacing(15)
        self.cardanoFromPrivateKeyAndCardanoTypeQFrameHLayout.setObjectName(u"cardanoFromPrivateKeyAndCardanoTypeQFrameHLayout")
        self.cardanoFromPrivateKeyAndCardanoTypeQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyContainerQFrame = QFrame(self.cardanoFromPrivateKeyAndCardanoTypeQFrame)
        self.cardanoFromPrivateKeyContainerQFrame.setObjectName(u"cardanoFromPrivateKeyContainerQFrame")
        self.cardanoFromPrivateKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.cardanoFromPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.cardanoFromPrivateKeyContainerQFrame)
        self.cardanoFromPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromPrivateKeyContainerQFrameVLayout.setObjectName(u"cardanoFromPrivateKeyContainerQFrameVLayout")
        self.cardanoFromPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyContainerLabelQFrame = QFrame(self.cardanoFromPrivateKeyContainerQFrame)
        self.cardanoFromPrivateKeyContainerLabelQFrame.setObjectName(u"cardanoFromPrivateKeyContainerLabelQFrame")
        self.cardanoFromPrivateKeyContainerLabelQFrameHLayout = QHBoxLayout(self.cardanoFromPrivateKeyContainerLabelQFrame)
        self.cardanoFromPrivateKeyContainerLabelQFrameHLayout.setSpacing(15)
        self.cardanoFromPrivateKeyContainerLabelQFrameHLayout.setObjectName(u"cardanoFromPrivateKeyContainerLabelQFrameHLayout")
        self.cardanoFromPrivateKeyContainerLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyContainerQLabel = QLabel(self.cardanoFromPrivateKeyContainerLabelQFrame)
        self.cardanoFromPrivateKeyContainerQLabel.setObjectName(u"cardanoFromPrivateKeyContainerQLabel")

        self.cardanoFromPrivateKeyContainerLabelQFrameHLayout.addWidget(self.cardanoFromPrivateKeyContainerQLabel)

        self.cardanoFromPrivateKeyContainerLabelQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromPrivateKeyContainerLabelQFrameHLayout.addItem(self.cardanoFromPrivateKeyContainerLabelQFrameHSpacer)


        self.cardanoFromPrivateKeyContainerQFrameVLayout.addWidget(self.cardanoFromPrivateKeyContainerLabelQFrame)

        self.cardanoFromPrivateKeyQLineEdit = QLineEdit(self.cardanoFromPrivateKeyContainerQFrame)
        self.cardanoFromPrivateKeyQLineEdit.setObjectName(u"cardanoFromPrivateKeyQLineEdit")

        self.cardanoFromPrivateKeyContainerQFrameVLayout.addWidget(self.cardanoFromPrivateKeyQLineEdit)


        self.cardanoFromPrivateKeyAndCardanoTypeQFrameHLayout.addWidget(self.cardanoFromPrivateKeyContainerQFrame)

        self.cardanoFromPrivateKeyCardanoTypeContainerQFrame = QFrame(self.cardanoFromPrivateKeyAndCardanoTypeQFrame)
        self.cardanoFromPrivateKeyCardanoTypeContainerQFrame.setObjectName(u"cardanoFromPrivateKeyCardanoTypeContainerQFrame")
        self.cardanoFromPrivateKeyCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromPrivateKeyCardanoTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromPrivateKeyCardanoTypeContainerQFrame)
        self.cardanoFromPrivateKeyCardanoTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromPrivateKeyCardanoTypeContainerQFrameVLayout.setObjectName(u"cardanoFromPrivateKeyCardanoTypeContainerQFrameVLayout")
        self.cardanoFromPrivateKeyCardanoTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromPrivateKeyCardanoTypeContainerQFrame)
        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame")
        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHLayout")
        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyCardanoTypeQLabel = QLabel(self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromPrivateKeyCardanoTypeQLabel.setObjectName(u"cardanoFromPrivateKeyCardanoTypeQLabel")

        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromPrivateKeyCardanoTypeQLabel)

        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHSpacer)


        self.cardanoFromPrivateKeyCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame)

        self.cardanoFromPrivateKeyCardanoTypeQComboBox = QComboBox(self.cardanoFromPrivateKeyCardanoTypeContainerQFrame)
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setObjectName(u"cardanoFromPrivateKeyCardanoTypeQComboBox")

        self.cardanoFromPrivateKeyCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromPrivateKeyCardanoTypeQComboBox)


        self.cardanoFromPrivateKeyAndCardanoTypeQFrameHLayout.addWidget(self.cardanoFromPrivateKeyCardanoTypeContainerQFrame)


        self.cardanoFromPrivateKeyQStackedWidgetVLayout.addWidget(self.cardanoFromPrivateKeyAndCardanoTypeQFrame)

        self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame = QFrame(self.cardanoFromPrivateKeyQStackedWidget)
        self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame.setObjectName(u"cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame")
        self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout = QHBoxLayout(self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setObjectName(u"cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout")
        self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyStakingContainerQFrame = QFrame(self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromPrivateKeyStakingContainerQFrame.setObjectName(u"cardanoFromPrivateKeyStakingContainerQFrame")
        self.cardanoFromPrivateKeyStakingContainerQFrameVLayout = QVBoxLayout(self.cardanoFromPrivateKeyStakingContainerQFrame)
        self.cardanoFromPrivateKeyStakingContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromPrivateKeyStakingContainerQFrameVLayout.setObjectName(u"cardanoFromPrivateKeyStakingContainerQFrameVLayout")
        self.cardanoFromPrivateKeyStakingContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyStakingLabelContainerQFrame = QFrame(self.cardanoFromPrivateKeyStakingContainerQFrame)
        self.cardanoFromPrivateKeyStakingLabelContainerQFrame.setObjectName(u"cardanoFromPrivateKeyStakingLabelContainerQFrame")
        self.cardanoFromPrivateKeyStakingLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromPrivateKeyStakingLabelContainerQFrame)
        self.cardanoFromPrivateKeyStakingLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromPrivateKeyStakingLabelContainerQFrameHLayout.setObjectName(u"cardanoFromPrivateKeyStakingLabelContainerQFrameHLayout")
        self.cardanoFromPrivateKeyStakingLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateStakingQLabel = QLabel(self.cardanoFromPrivateKeyStakingLabelContainerQFrame)
        self.cardanoFromPrivateStakingQLabel.setObjectName(u"cardanoFromPrivateStakingQLabel")

        self.cardanoFromPrivateKeyStakingLabelContainerQFrameHLayout.addWidget(self.cardanoFromPrivateStakingQLabel)

        self.cardanoFromPrivateKeyStakingLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromPrivateKeyStakingLabelContainerQFrameHLayout.addItem(self.cardanoFromPrivateKeyStakingLabelContainerQFrameHSpacer)


        self.cardanoFromPrivateKeyStakingContainerQFrameVLayout.addWidget(self.cardanoFromPrivateKeyStakingLabelContainerQFrame)

        self.cardanoFromPrivateKeyStakingQLineEdit = QLineEdit(self.cardanoFromPrivateKeyStakingContainerQFrame)
        self.cardanoFromPrivateKeyStakingQLineEdit.setObjectName(u"cardanoFromPrivateKeyStakingQLineEdit")

        self.cardanoFromPrivateKeyStakingContainerQFrameVLayout.addWidget(self.cardanoFromPrivateKeyStakingQLineEdit)


        self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.addWidget(self.cardanoFromPrivateKeyStakingContainerQFrame)

        self.cardanoFromPrivateKeyAddressTypeContainerQFrame = QFrame(self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromPrivateKeyAddressTypeContainerQFrame.setObjectName(u"cardanoFromPrivateKeyAddressTypeContainerQFrame")
        self.cardanoFromPrivateKeyAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromPrivateKeyAddressTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromPrivateKeyAddressTypeContainerQFrame)
        self.cardanoFromPrivateKeyAddressTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromPrivateKeyAddressTypeContainerQFrameVLayout.setObjectName(u"cardanoFromPrivateKeyAddressTypeContainerQFrameVLayout")
        self.cardanoFromPrivateKeyAddressTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromPrivateKeyAddressTypeContainerQFrame)
        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromPrivateKeyAddressTypeLabelContainerQFrame")
        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHLayout")
        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyAddressTypeQLabel = QLabel(self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromPrivateKeyAddressTypeQLabel.setObjectName(u"cardanoFromPrivateKeyAddressTypeQLabel")

        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromPrivateKeyAddressTypeQLabel)

        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHSpacer)


        self.cardanoFromPrivateKeyAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrame)

        self.cardanoFromPrivateKeyAddressTypeQComboBox = QComboBox(self.cardanoFromPrivateKeyAddressTypeContainerQFrame)
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setObjectName(u"cardanoFromPrivateKeyAddressTypeQComboBox")

        self.cardanoFromPrivateKeyAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromPrivateKeyAddressTypeQComboBox)


        self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.addWidget(self.cardanoFromPrivateKeyAddressTypeContainerQFrame)


        self.cardanoFromPrivateKeyQStackedWidgetVLayout.addWidget(self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)

        self.cardanoFromPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.cardanoFromPrivateKeyQStackedWidgetVLayout.addItem(self.cardanoFromPrivateKeyQStackedWidgetVSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromPrivateKeyQStackedWidget)
        self.cardanoFromPublicKeyQStackedWidget = QWidget()
        self.cardanoFromPublicKeyQStackedWidget.setObjectName(u"cardanoFromPublicKeyQStackedWidget")
        self.cardanoFromPublicKeyQStackedWidgetVLayout = QVBoxLayout(self.cardanoFromPublicKeyQStackedWidget)
        self.cardanoFromPublicKeyQStackedWidgetVLayout.setSpacing(15)
        self.cardanoFromPublicKeyQStackedWidgetVLayout.setObjectName(u"cardanoFromPublicKeyQStackedWidgetVLayout")
        self.cardanoFromPublicKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyAndCardanoTypeQFrame = QFrame(self.cardanoFromPublicKeyQStackedWidget)
        self.cardanoFromPublicKeyAndCardanoTypeQFrame.setObjectName(u"cardanoFromPublicKeyAndCardanoTypeQFrame")
        self.cardanoFromPublicKeyAndCardanoTypeQFrameHLayout = QHBoxLayout(self.cardanoFromPublicKeyAndCardanoTypeQFrame)
        self.cardanoFromPublicKeyAndCardanoTypeQFrameHLayout.setSpacing(15)
        self.cardanoFromPublicKeyAndCardanoTypeQFrameHLayout.setObjectName(u"cardanoFromPublicKeyAndCardanoTypeQFrameHLayout")
        self.cardanoFromPublicKeyAndCardanoTypeQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyContainerQFrame = QFrame(self.cardanoFromPublicKeyAndCardanoTypeQFrame)
        self.cardanoFromPublicKeyContainerQFrame.setObjectName(u"cardanoFromPublicKeyContainerQFrame")
        self.cardanoFromPublicKeyContainerQFrameVLayout = QVBoxLayout(self.cardanoFromPublicKeyContainerQFrame)
        self.cardanoFromPublicKeyContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromPublicKeyContainerQFrameVLayout.setObjectName(u"cardanoFromPublicKeyContainerQFrameVLayout")
        self.cardanoFromPublicKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyLabelContainerQFrame = QFrame(self.cardanoFromPublicKeyContainerQFrame)
        self.cardanoFromPublicKeyLabelContainerQFrame.setObjectName(u"cardanoFromPublicKeyLabelContainerQFrame")
        self.cardanoFromPublicKeyLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromPublicKeyLabelContainerQFrame)
        self.cardanoFromPublicKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromPublicKeyLabelContainerQFrameHLayout.setObjectName(u"cardanoFromPublicKeyLabelContainerQFrameHLayout")
        self.cardanoFromPublicKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyQLabel = QLabel(self.cardanoFromPublicKeyLabelContainerQFrame)
        self.cardanoFromPublicKeyQLabel.setObjectName(u"cardanoFromPublicKeyQLabel")

        self.cardanoFromPublicKeyLabelContainerQFrameHLayout.addWidget(self.cardanoFromPublicKeyQLabel)

        self.cardanoFromPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromPublicKeyLabelContainerQFrameHLayout.addItem(self.cardanoFromPublicKeyLabelContainerQFrameHSpacer)


        self.cardanoFromPublicKeyContainerQFrameVLayout.addWidget(self.cardanoFromPublicKeyLabelContainerQFrame)

        self.cardanoFromPublicKeyQLineEdit = QLineEdit(self.cardanoFromPublicKeyContainerQFrame)
        self.cardanoFromPublicKeyQLineEdit.setObjectName(u"cardanoFromPublicKeyQLineEdit")

        self.cardanoFromPublicKeyContainerQFrameVLayout.addWidget(self.cardanoFromPublicKeyQLineEdit)


        self.cardanoFromPublicKeyAndCardanoTypeQFrameHLayout.addWidget(self.cardanoFromPublicKeyContainerQFrame)

        self.cardanoFromPublicKeyCardanoTypeContainerQFrame = QFrame(self.cardanoFromPublicKeyAndCardanoTypeQFrame)
        self.cardanoFromPublicKeyCardanoTypeContainerQFrame.setObjectName(u"cardanoFromPublicKeyCardanoTypeContainerQFrame")
        self.cardanoFromPublicKeyCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromPublicKeyCardanoTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromPublicKeyCardanoTypeContainerQFrame)
        self.cardanoFromPublicKeyCardanoTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromPublicKeyCardanoTypeContainerQFrameVLayout.setObjectName(u"cardanoFromPublicKeyCardanoTypeContainerQFrameVLayout")
        self.cardanoFromPublicKeyCardanoTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromPublicKeyCardanoTypeContainerQFrame)
        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromPublicKeyCardanoTypeLabelContainerQFrame")
        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHLayout")
        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyCardanoTypeQLabel = QLabel(self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromPublicKeyCardanoTypeQLabel.setObjectName(u"cardanoFromPublicKeyCardanoTypeQLabel")

        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromPublicKeyCardanoTypeQLabel)

        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHSpacer)


        self.cardanoFromPublicKeyCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrame)

        self.cardanoFromPublicKeyCardanoTypeQComboBox = QComboBox(self.cardanoFromPublicKeyCardanoTypeContainerQFrame)
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setObjectName(u"cardanoFromPublicKeyCardanoTypeQComboBox")

        self.cardanoFromPublicKeyCardanoTypeContainerQFrameVLayout.addWidget(self.cardanoFromPublicKeyCardanoTypeQComboBox)


        self.cardanoFromPublicKeyAndCardanoTypeQFrameHLayout.addWidget(self.cardanoFromPublicKeyCardanoTypeContainerQFrame)


        self.cardanoFromPublicKeyQStackedWidgetVLayout.addWidget(self.cardanoFromPublicKeyAndCardanoTypeQFrame)

        self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame = QFrame(self.cardanoFromPublicKeyQStackedWidget)
        self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame.setObjectName(u"cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame")
        self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout = QHBoxLayout(self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setObjectName(u"cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout")
        self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyStakingContainerQFrame = QFrame(self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromPublicKeyStakingContainerQFrame.setObjectName(u"cardanoFromPublicKeyStakingContainerQFrame")
        self.cardanoFromPublicKeyStakingContainerQFrameVLayout = QVBoxLayout(self.cardanoFromPublicKeyStakingContainerQFrame)
        self.cardanoFromPublicKeyStakingContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromPublicKeyStakingContainerQFrameVLayout.setObjectName(u"cardanoFromPublicKeyStakingContainerQFrameVLayout")
        self.cardanoFromPublicKeyStakingContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyStakingLabelContainerQFrame = QFrame(self.cardanoFromPublicKeyStakingContainerQFrame)
        self.cardanoFromPublicKeyStakingLabelContainerQFrame.setObjectName(u"cardanoFromPublicKeyStakingLabelContainerQFrame")
        self.cardanoFromPublicKeyStakingLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromPublicKeyStakingLabelContainerQFrame)
        self.cardanoFromPublicKeyStakingLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromPublicKeyStakingLabelContainerQFrameHLayout.setObjectName(u"cardanoFromPublicKeyStakingLabelContainerQFrameHLayout")
        self.cardanoFromPublicKeyStakingLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicStakingQLabel = QLabel(self.cardanoFromPublicKeyStakingLabelContainerQFrame)
        self.cardanoFromPublicStakingQLabel.setObjectName(u"cardanoFromPublicStakingQLabel")

        self.cardanoFromPublicKeyStakingLabelContainerQFrameHLayout.addWidget(self.cardanoFromPublicStakingQLabel)

        self.cardanoFromPublicKeyStakingLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromPublicKeyStakingLabelContainerQFrameHLayout.addItem(self.cardanoFromPublicKeyStakingLabelContainerQFrameHSpacer)


        self.cardanoFromPublicKeyStakingContainerQFrameVLayout.addWidget(self.cardanoFromPublicKeyStakingLabelContainerQFrame)

        self.cardanoFromPublicKeyStakingQLineEdit = QLineEdit(self.cardanoFromPublicKeyStakingContainerQFrame)
        self.cardanoFromPublicKeyStakingQLineEdit.setObjectName(u"cardanoFromPublicKeyStakingQLineEdit")

        self.cardanoFromPublicKeyStakingContainerQFrameVLayout.addWidget(self.cardanoFromPublicKeyStakingQLineEdit)


        self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.addWidget(self.cardanoFromPublicKeyStakingContainerQFrame)

        self.cardanoFromPublicKeyAddressTypeContainerQFrame = QFrame(self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromPublicKeyAddressTypeContainerQFrame.setObjectName(u"cardanoFromPublicKeyAddressTypeContainerQFrame")
        self.cardanoFromPublicKeyAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.cardanoFromPublicKeyAddressTypeContainerQFrameVLayout = QVBoxLayout(self.cardanoFromPublicKeyAddressTypeContainerQFrame)
        self.cardanoFromPublicKeyAddressTypeContainerQFrameVLayout.setSpacing(5)
        self.cardanoFromPublicKeyAddressTypeContainerQFrameVLayout.setObjectName(u"cardanoFromPublicKeyAddressTypeContainerQFrameVLayout")
        self.cardanoFromPublicKeyAddressTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromPublicKeyAddressTypeContainerQFrame)
        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromPublicKeyAddressTypeLabelContainerQFrame")
        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrameHLayout = QHBoxLayout(self.cardanoFromPublicKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrameHLayout.setObjectName(u"cardanoFromPublicKeyAddressTypeLabelContainerQFrameHLayout")
        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyAddressTypeQLabel = QLabel(self.cardanoFromPublicKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromPublicKeyAddressTypeQLabel.setObjectName(u"cardanoFromPublicKeyAddressTypeQLabel")

        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrameHLayout.addWidget(self.cardanoFromPublicKeyAddressTypeQLabel)

        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrameHLayout.addItem(self.cardanoFromPublicKeyAddressTypeLabelContainerQFrameHSpacer)


        self.cardanoFromPublicKeyAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromPublicKeyAddressTypeLabelContainerQFrame)

        self.cardanoFromPublicKeyAddressTypeQComboBox = QComboBox(self.cardanoFromPublicKeyAddressTypeContainerQFrame)
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.setObjectName(u"cardanoFromPublicKeyAddressTypeQComboBox")

        self.cardanoFromPublicKeyAddressTypeContainerQFrameVLayout.addWidget(self.cardanoFromPublicKeyAddressTypeQComboBox)


        self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrameHLayout.addWidget(self.cardanoFromPublicKeyAddressTypeContainerQFrame)


        self.cardanoFromPublicKeyQStackedWidgetVLayout.addWidget(self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame)

        self.cardanoFromPublicKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.cardanoFromPublicKeyQStackedWidgetVLayout.addItem(self.cardanoFromPublicKeyQStackedWidgetVSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromPublicKeyQStackedWidget)

        self.cardanoPageQWidgetVLayout.addWidget(self.cardanoQStackedWidget)

        self.hdQStackedWidget.addWidget(self.cardanoPageQWidget)
        self.electrumV1PageQWidget = QWidget()
        self.electrumV1PageQWidget.setObjectName(u"electrumV1PageQWidget")
        self.electrumV1PageQWidgetVLayout = QVBoxLayout(self.electrumV1PageQWidget)
        self.electrumV1PageQWidgetVLayout.setSpacing(0)
        self.electrumV1PageQWidgetVLayout.setObjectName(u"electrumV1PageQWidgetVLayout")
        self.electrumV1PageQWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1QStackedWidget = QStackedWidget(self.electrumV1PageQWidget)
        self.electrumV1QStackedWidget.setObjectName(u"electrumV1QStackedWidget")
        self.electrumV1FromEntropyQStackedWidget = QWidget()
        self.electrumV1FromEntropyQStackedWidget.setObjectName(u"electrumV1FromEntropyQStackedWidget")
        self.electrumV1FromEntropyQStackedWidgetVLayout = QVBoxLayout(self.electrumV1FromEntropyQStackedWidget)
        self.electrumV1FromEntropyQStackedWidgetVLayout.setSpacing(15)
        self.electrumV1FromEntropyQStackedWidgetVLayout.setObjectName(u"electrumV1FromEntropyQStackedWidgetVLayout")
        self.electrumV1FromEntropyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyContainerQFrame = QFrame(self.electrumV1FromEntropyQStackedWidget)
        self.electrumV1FromEntropyContainerQFrame.setObjectName(u"electrumV1FromEntropyContainerQFrame")
        self.electrumV1FromEntropyContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromEntropyContainerQFrame)
        self.electrumV1FromEntropyContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromEntropyContainerQFrameVLayout.setObjectName(u"electrumV1FromEntropyContainerQFrameVLayout")
        self.electrumV1FromEntropyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyLabelContainerQFrame = QFrame(self.electrumV1FromEntropyContainerQFrame)
        self.electrumV1FromEntropyLabelContainerQFrame.setObjectName(u"electrumV1FromEntropyLabelContainerQFrame")
        self.electrumV1FromEntropyLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromEntropyLabelContainerQFrame)
        self.electrumV1FromEntropyLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromEntropyLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromEntropyLabelContainerQFrameHLayout")
        self.electrumV1FromEntropyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyQLabel = QLabel(self.electrumV1FromEntropyLabelContainerQFrame)
        self.electrumV1FromEntropyQLabel.setObjectName(u"electrumV1FromEntropyQLabel")

        self.electrumV1FromEntropyLabelContainerQFrameHLayout.addWidget(self.electrumV1FromEntropyQLabel)

        self.electrumV1FromEntropyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromEntropyLabelContainerQFrameHLayout.addItem(self.electrumV1FromEntropyLabelContainerQFrameHSpacer)


        self.electrumV1FromEntropyContainerQFrameVLayout.addWidget(self.electrumV1FromEntropyLabelContainerQFrame)

        self.electrumV1FromEntropyGenerateContainerQFrame = QFrame(self.electrumV1FromEntropyContainerQFrame)
        self.electrumV1FromEntropyGenerateContainerQFrame.setObjectName(u"electrumV1FromEntropyGenerateContainerQFrame")
        self.electrumV1FromEntropyGenerateContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromEntropyGenerateContainerQFrame)
        self.electrumV1FromEntropyGenerateContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromEntropyGenerateContainerQFrameHLayout.setObjectName(u"electrumV1FromEntropyGenerateContainerQFrameHLayout")
        self.electrumV1FromEntropyGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyQLineEdit = QLineEdit(self.electrumV1FromEntropyGenerateContainerQFrame)
        self.electrumV1FromEntropyQLineEdit.setObjectName(u"electrumV1FromEntropyQLineEdit")

        self.electrumV1FromEntropyGenerateContainerQFrameHLayout.addWidget(self.electrumV1FromEntropyQLineEdit)


        self.electrumV1FromEntropyContainerQFrameVLayout.addWidget(self.electrumV1FromEntropyGenerateContainerQFrame)


        self.electrumV1FromEntropyQStackedWidgetVLayout.addWidget(self.electrumV1FromEntropyContainerQFrame)

        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame = QFrame(self.electrumV1FromEntropyQStackedWidget)
        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame.setObjectName(u"electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame")
        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrameHLayout.setObjectName(u"electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrameHLayout")
        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromEntropyPublicKeyTypeContainerQFrame")
        self.electrumV1FromEntropyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.electrumV1FromEntropyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromEntropyPublicKeyTypeContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromEntropyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"electrumV1FromEntropyPublicKeyTypeContainerQFrameVLayout")
        self.electrumV1FromEntropyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromEntropyPublicKeyTypeContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame")
        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHLayout")
        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPublicKeyTypeQLabel = QLabel(self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeQLabel.setObjectName(u"electrumV1FromEntropyPublicKeyTypeQLabel")

        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.electrumV1FromEntropyPublicKeyTypeQLabel)

        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.electrumV1FromEntropyPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromEntropyPublicKeyTypeQComboBox = QComboBox(self.electrumV1FromEntropyPublicKeyTypeContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromEntropyPublicKeyTypeQComboBox")

        self.electrumV1FromEntropyPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromEntropyPublicKeyTypeQComboBox)


        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV1FromEntropyPublicKeyTypeContainerQFrame)

        self.electrumV1FromEntropyLanguageContainerQFrame = QFrame(self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromEntropyLanguageContainerQFrame.setObjectName(u"electrumV1FromEntropyLanguageContainerQFrame")
        self.electrumV1FromEntropyLanguageContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromEntropyLanguageContainerQFrame)
        self.electrumV1FromEntropyLanguageContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromEntropyLanguageContainerQFrameVLayout.setObjectName(u"electrumV1FromEntropyLanguageContainerQFrameVLayout")
        self.electrumV1FromEntropyLanguageContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyLanguageLabelContainerQFrame = QFrame(self.electrumV1FromEntropyLanguageContainerQFrame)
        self.electrumV1FromEntropyLanguageLabelContainerQFrame.setObjectName(u"electrumV1FromEntropyLanguageLabelContainerQFrame")
        self.electrumV1FromEntropyLanguageLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromEntropyLanguageLabelContainerQFrame)
        self.electrumV1FromEntropyLanguageLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromEntropyLanguageLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromEntropyLanguageLabelContainerQFrameHLayout")
        self.electrumV1FromEntropyLanguageLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyLanguageQLabel = QLabel(self.electrumV1FromEntropyLanguageLabelContainerQFrame)
        self.electrumV1FromEntropyLanguageQLabel.setObjectName(u"electrumV1FromEntropyLanguageQLabel")

        self.electrumV1FromEntropyLanguageLabelContainerQFrameHLayout.addWidget(self.electrumV1FromEntropyLanguageQLabel)

        self.electrumV1FromEntropyLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromEntropyLanguageLabelContainerQFrameHLayout.addItem(self.electrumV1FromEntropyLanguageLabelContainerQFrameHSpacer)


        self.electrumV1FromEntropyLanguageContainerQFrameVLayout.addWidget(self.electrumV1FromEntropyLanguageLabelContainerQFrame)

        self.electrumV1FromEntropyLanguageQComboBox = QComboBox(self.electrumV1FromEntropyLanguageContainerQFrame)
        self.electrumV1FromEntropyLanguageQComboBox.addItem("")
        self.electrumV1FromEntropyLanguageQComboBox.addItem("")
        self.electrumV1FromEntropyLanguageQComboBox.addItem("")
        self.electrumV1FromEntropyLanguageQComboBox.addItem("")
        self.electrumV1FromEntropyLanguageQComboBox.addItem("")
        self.electrumV1FromEntropyLanguageQComboBox.addItem("")
        self.electrumV1FromEntropyLanguageQComboBox.addItem("")
        self.electrumV1FromEntropyLanguageQComboBox.addItem("")
        self.electrumV1FromEntropyLanguageQComboBox.setObjectName(u"electrumV1FromEntropyLanguageQComboBox")

        self.electrumV1FromEntropyLanguageContainerQFrameVLayout.addWidget(self.electrumV1FromEntropyLanguageQComboBox)


        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV1FromEntropyLanguageContainerQFrame)

        self.electrumV1FromEntropyPassphraseContainerQFrame = QFrame(self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromEntropyPassphraseContainerQFrame.setObjectName(u"electrumV1FromEntropyPassphraseContainerQFrame")
        self.electrumV1FromEntropyPassphraseContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromEntropyPassphraseContainerQFrame)
        self.electrumV1FromEntropyPassphraseContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromEntropyPassphraseContainerQFrameVLayout.setObjectName(u"electrumV1FromEntropyPassphraseContainerQFrameVLayout")
        self.electrumV1FromEntropyPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPassphraseLabelContainerQFrame = QFrame(self.electrumV1FromEntropyPassphraseContainerQFrame)
        self.electrumV1FromEntropyPassphraseLabelContainerQFrame.setObjectName(u"electrumV1FromEntropyPassphraseLabelContainerQFrame")
        self.electrumV1FromEntropyPassphraseLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromEntropyPassphraseLabelContainerQFrame)
        self.electrumV1FromEntropyPassphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromEntropyPassphraseLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromEntropyPassphraseLabelContainerQFrameHLayout")
        self.electrumV1FromEntropyPassphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPassphraseQLabel = QLabel(self.electrumV1FromEntropyPassphraseLabelContainerQFrame)
        self.electrumV1FromEntropyPassphraseQLabel.setObjectName(u"electrumV1FromEntropyPassphraseQLabel")

        self.electrumV1FromEntropyPassphraseLabelContainerQFrameHLayout.addWidget(self.electrumV1FromEntropyPassphraseQLabel)

        self.electrumV1FromEntropyPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromEntropyPassphraseLabelContainerQFrameHLayout.addItem(self.electrumV1FromEntropyPassphraseLabelContainerQFrameHSpacer)


        self.electrumV1FromEntropyPassphraseContainerQFrameVLayout.addWidget(self.electrumV1FromEntropyPassphraseLabelContainerQFrame)

        self.electrumV1FromEntropyPassphraseGenerateContainerQFrame = QFrame(self.electrumV1FromEntropyPassphraseContainerQFrame)
        self.electrumV1FromEntropyPassphraseGenerateContainerQFrame.setObjectName(u"electrumV1FromEntropyPassphraseGenerateContainerQFrame")
        self.electrumV1FromEntropyPassphraseGenerateContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromEntropyPassphraseGenerateContainerQFrame)
        self.electrumV1FromEntropyPassphraseGenerateContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromEntropyPassphraseGenerateContainerQFrameHLayout.setObjectName(u"electrumV1FromEntropyPassphraseGenerateContainerQFrameHLayout")
        self.electrumV1FromEntropyPassphraseGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPassphraseGenerateQLineEdit = QLineEdit(self.electrumV1FromEntropyPassphraseGenerateContainerQFrame)
        self.electrumV1FromEntropyPassphraseGenerateQLineEdit.setObjectName(u"electrumV1FromEntropyPassphraseGenerateQLineEdit")

        self.electrumV1FromEntropyPassphraseGenerateContainerQFrameHLayout.addWidget(self.electrumV1FromEntropyPassphraseGenerateQLineEdit)


        self.electrumV1FromEntropyPassphraseContainerQFrameVLayout.addWidget(self.electrumV1FromEntropyPassphraseGenerateContainerQFrame)


        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV1FromEntropyPassphraseContainerQFrame)


        self.electrumV1FromEntropyQStackedWidgetVLayout.addWidget(self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame)

        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.electrumV1FromEntropyQStackedWidgetVLayout.addItem(self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrameVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromEntropyQStackedWidget)
        self.electrumV1FromMnemonicQStackedWidget = QWidget()
        self.electrumV1FromMnemonicQStackedWidget.setObjectName(u"electrumV1FromMnemonicQStackedWidget")
        self.electrumV1FromMnemonicQStackedWidgetVLayout = QVBoxLayout(self.electrumV1FromMnemonicQStackedWidget)
        self.electrumV1FromMnemonicQStackedWidgetVLayout.setSpacing(15)
        self.electrumV1FromMnemonicQStackedWidgetVLayout.setObjectName(u"electrumV1FromMnemonicQStackedWidgetVLayout")
        self.electrumV1FromMnemonicQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicContainerQFrame = QFrame(self.electrumV1FromMnemonicQStackedWidget)
        self.electrumV1FromMnemonicContainerQFrame.setObjectName(u"electrumV1FromMnemonicContainerQFrame")
        self.electrumV1FromMnemonicContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromMnemonicContainerQFrame)
        self.electrumV1FromMnemonicContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromMnemonicContainerQFrameVLayout.setObjectName(u"electrumV1FromMnemonicContainerQFrameVLayout")
        self.electrumV1FromMnemonicContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicLabelContainerQFrame = QFrame(self.electrumV1FromMnemonicContainerQFrame)
        self.electrumV1FromMnemonicLabelContainerQFrame.setObjectName(u"electrumV1FromMnemonicLabelContainerQFrame")
        self.electrumV1FromMnemonicLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromMnemonicLabelContainerQFrame)
        self.electrumV1FromMnemonicLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromMnemonicLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromMnemonicLabelContainerQFrameHLayout")
        self.electrumV1FromMnemonicLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicQLabel = QLabel(self.electrumV1FromMnemonicLabelContainerQFrame)
        self.electrumV1FromMnemonicQLabel.setObjectName(u"electrumV1FromMnemonicQLabel")

        self.electrumV1FromMnemonicLabelContainerQFrameHLayout.addWidget(self.electrumV1FromMnemonicQLabel)

        self.electrumV1FromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromMnemonicLabelContainerQFrameHLayout.addItem(self.electrumV1FromMnemonicLabelContainerQFrameHSpacer)


        self.electrumV1FromMnemonicContainerQFrameVLayout.addWidget(self.electrumV1FromMnemonicLabelContainerQFrame)

        self.electrumV1FromMnemonicGenerateContainerQFrame = QFrame(self.electrumV1FromMnemonicContainerQFrame)
        self.electrumV1FromMnemonicGenerateContainerQFrame.setObjectName(u"electrumV1FromMnemonicGenerateContainerQFrame")
        self.electrumV1FromMnemonicGenerateContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromMnemonicGenerateContainerQFrame)
        self.electrumV1FromMnemonicGenerateContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromMnemonicGenerateContainerQFrameHLayout.setObjectName(u"electrumV1FromMnemonicGenerateContainerQFrameHLayout")
        self.electrumV1FromMnemonicGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicGenerateQLineEdit = QLineEdit(self.electrumV1FromMnemonicGenerateContainerQFrame)
        self.electrumV1FromMnemonicGenerateQLineEdit.setObjectName(u"electrumV1FromMnemonicGenerateQLineEdit")

        self.electrumV1FromMnemonicGenerateContainerQFrameHLayout.addWidget(self.electrumV1FromMnemonicGenerateQLineEdit)


        self.electrumV1FromMnemonicContainerQFrameVLayout.addWidget(self.electrumV1FromMnemonicGenerateContainerQFrame)


        self.electrumV1FromMnemonicQStackedWidgetVLayout.addWidget(self.electrumV1FromMnemonicContainerQFrame)

        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame = QFrame(self.electrumV1FromMnemonicQStackedWidget)
        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame")
        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrameHLayout.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrameHLayout")
        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeContainerQFrame")
        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrameVLayout.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeContainerQFrameVLayout")
        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame")
        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout")
        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPublicKeyTypeQLabel = QLabel(self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeQLabel.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeQLabel")

        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.electrumV1FromMnemonicPublicKeyTypeQLabel)

        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer)


        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromMnemonicPublicKeyTypeQComboBox = QComboBox(self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeQComboBox")

        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromMnemonicPublicKeyTypeQComboBox)


        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame)

        self.electrumV1FromMnemonicLanguageContainerQFrame = QFrame(self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromMnemonicLanguageContainerQFrame.setObjectName(u"electrumV1FromMnemonicLanguageContainerQFrame")
        self.electrumV1FromMnemonicLanguageContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromMnemonicLanguageContainerQFrame)
        self.electrumV1FromMnemonicLanguageContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromMnemonicLanguageContainerQFrameVLayout.setObjectName(u"electrumV1FromMnemonicLanguageContainerQFrameVLayout")
        self.electrumV1FromMnemonicLanguageContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicLanguageLabelContainerQFrame = QWidget(self.electrumV1FromMnemonicLanguageContainerQFrame)
        self.electrumV1FromMnemonicLanguageLabelContainerQFrame.setObjectName(u"electrumV1FromMnemonicLanguageLabelContainerQFrame")
        self.electrumV1FromMnemonicLanguageLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromMnemonicLanguageLabelContainerQFrame)
        self.electrumV1FromMnemonicLanguageLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromMnemonicLanguageLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromMnemonicLanguageLabelContainerQFrameHLayout")
        self.electrumV1FromMnemonicLanguageLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicLanguageQLabel = QLabel(self.electrumV1FromMnemonicLanguageLabelContainerQFrame)
        self.electrumV1FromMnemonicLanguageQLabel.setObjectName(u"electrumV1FromMnemonicLanguageQLabel")

        self.electrumV1FromMnemonicLanguageLabelContainerQFrameHLayout.addWidget(self.electrumV1FromMnemonicLanguageQLabel)

        self.electrumV1FromMnemonicLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromMnemonicLanguageLabelContainerQFrameHLayout.addItem(self.electrumV1FromMnemonicLanguageLabelContainerQFrameHSpacer)


        self.electrumV1FromMnemonicLanguageContainerQFrameVLayout.addWidget(self.electrumV1FromMnemonicLanguageLabelContainerQFrame)

        self.electrumV1FromMnemonicLanguageQComboBox = QComboBox(self.electrumV1FromMnemonicLanguageContainerQFrame)
        self.electrumV1FromMnemonicLanguageQComboBox.addItem("")
        self.electrumV1FromMnemonicLanguageQComboBox.addItem("")
        self.electrumV1FromMnemonicLanguageQComboBox.addItem("")
        self.electrumV1FromMnemonicLanguageQComboBox.addItem("")
        self.electrumV1FromMnemonicLanguageQComboBox.addItem("")
        self.electrumV1FromMnemonicLanguageQComboBox.addItem("")
        self.electrumV1FromMnemonicLanguageQComboBox.addItem("")
        self.electrumV1FromMnemonicLanguageQComboBox.addItem("")
        self.electrumV1FromMnemonicLanguageQComboBox.setObjectName(u"electrumV1FromMnemonicLanguageQComboBox")

        self.electrumV1FromMnemonicLanguageContainerQFrameVLayout.addWidget(self.electrumV1FromMnemonicLanguageQComboBox)


        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV1FromMnemonicLanguageContainerQFrame)

        self.electrumV1FromMnemonicPassphraseContainerQFrame = QFrame(self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromMnemonicPassphraseContainerQFrame.setObjectName(u"electrumV1FromMnemonicPassphraseContainerQFrame")
        self.electrumV1FromMnemonicPassphraseContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromMnemonicPassphraseContainerQFrame)
        self.electrumV1FromMnemonicPassphraseContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromMnemonicPassphraseContainerQFrameVLayout.setObjectName(u"electrumV1FromMnemonicPassphraseContainerQFrameVLayout")
        self.electrumV1FromMnemonicPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPassphraseLabelContainerQFrame = QFrame(self.electrumV1FromMnemonicPassphraseContainerQFrame)
        self.electrumV1FromMnemonicPassphraseLabelContainerQFrame.setObjectName(u"electrumV1FromMnemonicPassphraseLabelContainerQFrame")
        self.electrumV1FromMnemonicPassphraseLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromMnemonicPassphraseLabelContainerQFrame)
        self.electrumV1FromMnemonicPassphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromMnemonicPassphraseLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromMnemonicPassphraseLabelContainerQFrameHLayout")
        self.electrumV1FromMnemonicPassphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPassphraseQLabel = QLabel(self.electrumV1FromMnemonicPassphraseLabelContainerQFrame)
        self.electrumV1FromMnemonicPassphraseQLabel.setObjectName(u"electrumV1FromMnemonicPassphraseQLabel")

        self.electrumV1FromMnemonicPassphraseLabelContainerQFrameHLayout.addWidget(self.electrumV1FromMnemonicPassphraseQLabel)

        self.electrumV1FromMnemonicPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromMnemonicPassphraseLabelContainerQFrameHLayout.addItem(self.electrumV1FromMnemonicPassphraseLabelContainerQFrameHSpacer)


        self.electrumV1FromMnemonicPassphraseContainerQFrameVLayout.addWidget(self.electrumV1FromMnemonicPassphraseLabelContainerQFrame)

        self.electrumV1FromMnemonicPassphraseGenerateContainerQFrame = QFrame(self.electrumV1FromMnemonicPassphraseContainerQFrame)
        self.electrumV1FromMnemonicPassphraseGenerateContainerQFrame.setObjectName(u"electrumV1FromMnemonicPassphraseGenerateContainerQFrame")
        self.electrumV1FromMnemonicPassphraseGenerateContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromMnemonicPassphraseGenerateContainerQFrame)
        self.electrumV1FromMnemonicPassphraseGenerateContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromMnemonicPassphraseGenerateContainerQFrameHLayout.setObjectName(u"electrumV1FromMnemonicPassphraseGenerateContainerQFrameHLayout")
        self.electrumV1FromMnemonicPassphraseGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPassphraseGenerateQLineEdit = QLineEdit(self.electrumV1FromMnemonicPassphraseGenerateContainerQFrame)
        self.electrumV1FromMnemonicPassphraseGenerateQLineEdit.setObjectName(u"electrumV1FromMnemonicPassphraseGenerateQLineEdit")

        self.electrumV1FromMnemonicPassphraseGenerateContainerQFrameHLayout.addWidget(self.electrumV1FromMnemonicPassphraseGenerateQLineEdit)


        self.electrumV1FromMnemonicPassphraseContainerQFrameVLayout.addWidget(self.electrumV1FromMnemonicPassphraseGenerateContainerQFrame)


        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV1FromMnemonicPassphraseContainerQFrame)


        self.electrumV1FromMnemonicQStackedWidgetVLayout.addWidget(self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromMnemonicQStackedWidget)
        self.electrumV1FromSeedQStackedWidget = QWidget()
        self.electrumV1FromSeedQStackedWidget.setObjectName(u"electrumV1FromSeedQStackedWidget")
        self.electrumV1FromSeedQStackedWidgetVLayout = QVBoxLayout(self.electrumV1FromSeedQStackedWidget)
        self.electrumV1FromSeedQStackedWidgetVLayout.setSpacing(15)
        self.electrumV1FromSeedQStackedWidgetVLayout.setObjectName(u"electrumV1FromSeedQStackedWidgetVLayout")
        self.electrumV1FromSeedQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromSeedQStackedWidget)
        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromSeedAndPublicKeyTypeContainerQFrame")
        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"electrumV1FromSeedAndPublicKeyTypeContainerQFrameHLayout")
        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedContainerQFrame = QFrame(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromSeedContainerQFrame.setObjectName(u"electrumV1FromSeedContainerQFrame")
        self.electrumV1FromSeedContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromSeedContainerQFrame)
        self.electrumV1FromSeedContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromSeedContainerQFrameVLayout.setObjectName(u"electrumV1FromSeedContainerQFrameVLayout")
        self.electrumV1FromSeedContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedLabelContainerQFrame = QFrame(self.electrumV1FromSeedContainerQFrame)
        self.electrumV1FromSeedLabelContainerQFrame.setObjectName(u"electrumV1FromSeedLabelContainerQFrame")
        self.electrumV1FromSeedLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromSeedLabelContainerQFrame)
        self.electrumV1FromSeedLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromSeedLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromSeedLabelContainerQFrameHLayout")
        self.electrumV1FromSeedLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedQLabel = QLabel(self.electrumV1FromSeedLabelContainerQFrame)
        self.electrumV1FromSeedQLabel.setObjectName(u"electrumV1FromSeedQLabel")

        self.electrumV1FromSeedLabelContainerQFrameHLayout.addWidget(self.electrumV1FromSeedQLabel)

        self.electrumV1FromSeedLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromSeedLabelContainerQFrameHLayout.addItem(self.electrumV1FromSeedLabelContainerQFrameHSpacer)


        self.electrumV1FromSeedContainerQFrameVLayout.addWidget(self.electrumV1FromSeedLabelContainerQFrame)

        self.electrumV1FromSeedQLineEdit = QLineEdit(self.electrumV1FromSeedContainerQFrame)
        self.electrumV1FromSeedQLineEdit.setObjectName(u"electrumV1FromSeedQLineEdit")

        self.electrumV1FromSeedContainerQFrameVLayout.addWidget(self.electrumV1FromSeedQLineEdit)


        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV1FromSeedContainerQFrame)

        self.electrumV1FromSeedsPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromSeedsPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromSeedsPublicKeyTypeContainerQFrame")
        self.electrumV1FromSeedsPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.electrumV1FromSeedsPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromSeedsPublicKeyTypeContainerQFrame)
        self.electrumV1FromSeedsPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromSeedsPublicKeyTypeContainerQFrameVLayout.setObjectName(u"electrumV1FromSeedsPublicKeyTypeContainerQFrameVLayout")
        self.electrumV1FromSeedsPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromSeedsPublicKeyTypeContainerQFrame)
        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromSeedPublicKeyTypeLabelContainerQFrame")
        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHLayout")
        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedPublicKeyTypeQLabel = QLabel(self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromSeedPublicKeyTypeQLabel.setObjectName(u"electrumV1FromSeedPublicKeyTypeQLabel")

        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.electrumV1FromSeedPublicKeyTypeQLabel)

        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHSpacer)


        self.electrumV1FromSeedsPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromClientQComboBox = QComboBox(self.electrumV1FromSeedsPublicKeyTypeContainerQFrame)
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.setObjectName(u"electrumV1FromClientQComboBox")

        self.electrumV1FromSeedsPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromClientQComboBox)


        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV1FromSeedsPublicKeyTypeContainerQFrame)


        self.electrumV1FromSeedQStackedWidgetVLayout.addWidget(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)

        self.electrumV1FromSeedQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.electrumV1FromSeedQStackedWidgetVLayout.addItem(self.electrumV1FromSeedQStackedWidgetVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromSeedQStackedWidget)
        self.electrumV1FromWIFQStackedWidget = QWidget()
        self.electrumV1FromWIFQStackedWidget.setObjectName(u"electrumV1FromWIFQStackedWidget")
        self.electrumV1FromWIFQStackedWidgetVLayout = QVBoxLayout(self.electrumV1FromWIFQStackedWidget)
        self.electrumV1FromWIFQStackedWidgetVLayout.setSpacing(15)
        self.electrumV1FromWIFQStackedWidgetVLayout.setObjectName(u"electrumV1FromWIFQStackedWidgetVLayout")
        self.electrumV1FromWIFQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFContainerQFrame = QFrame(self.electrumV1FromWIFQStackedWidget)
        self.electrumV1FromWIFContainerQFrame.setObjectName(u"electrumV1FromWIFContainerQFrame")
        self.electrumV1FromWIFContainerQFrame.setMinimumSize(QSize(400, 0))
        self.electrumV1FromWIFContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromWIFContainerQFrame)
        self.electrumV1FromWIFContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromWIFContainerQFrameVLayout.setObjectName(u"electrumV1FromWIFContainerQFrameVLayout")
        self.electrumV1FromWIFContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFLabelContainerQFrame = QFrame(self.electrumV1FromWIFContainerQFrame)
        self.electrumV1FromWIFLabelContainerQFrame.setObjectName(u"electrumV1FromWIFLabelContainerQFrame")
        self.electrumV1FromWIFLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromWIFLabelContainerQFrame)
        self.electrumV1FromWIFLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromWIFLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromWIFLabelContainerQFrameHLayout")
        self.electrumV1FromWIFLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFQLabel = QLabel(self.electrumV1FromWIFLabelContainerQFrame)
        self.electrumV1FromWIFQLabel.setObjectName(u"electrumV1FromWIFQLabel")

        self.electrumV1FromWIFLabelContainerQFrameHLayout.addWidget(self.electrumV1FromWIFQLabel)

        self.electrumV1FromWIFLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromWIFLabelContainerQFrameHLayout.addItem(self.electrumV1FromWIFLabelContainerQFrameHSpacer)


        self.electrumV1FromWIFContainerQFrameVLayout.addWidget(self.electrumV1FromWIFLabelContainerQFrame)

        self.electrumV1FromWIFQLineEdit = QLineEdit(self.electrumV1FromWIFContainerQFrame)
        self.electrumV1FromWIFQLineEdit.setObjectName(u"electrumV1FromWIFQLineEdit")

        self.electrumV1FromWIFContainerQFrameVLayout.addWidget(self.electrumV1FromWIFQLineEdit)


        self.electrumV1FromWIFQStackedWidgetVLayout.addWidget(self.electrumV1FromWIFContainerQFrame)

        self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromWIFQStackedWidget)
        self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame")
        self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrameHLayout")
        self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromWIFPublicKeyTypeContainerQFrame")
        self.electrumV1FromWIFPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.electrumV1FromWIFPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromWIFPublicKeyTypeContainerQFrameVLayout.setObjectName(u"electrumV1FromWIFPublicKeyTypeContainerQFrameVLayout")
        self.electrumV1FromWIFPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromWIFPublicKeyTypeLabelContainerQFrame")
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHLayout")
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFPublicKeyTypeQLabel = QLabel(self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeQLabel.setObjectName(u"electrumV1FromWIFPublicKeyTypeQLabel")

        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.electrumV1FromWIFPublicKeyTypeQLabel)

        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHSpacer)


        self.electrumV1FromWIFPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromWIFPublicKeyTypeQComboBox = QComboBox(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromWIFPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromWIFPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromWIFPublicKeyTypeQComboBox")

        self.electrumV1FromWIFPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromWIFPublicKeyTypeQComboBox)


        self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)

        self.electrumV1FromWIFBIP38PassphraseContainerQFrame = QFrame(self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseContainerQFrame.setObjectName(u"electrumV1FromWIFBIP38PassphraseContainerQFrame")
        self.electrumV1FromWIFBIP38PassphraseContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromWIFBIP38PassphraseContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromWIFBIP38PassphraseContainerQFrameVLayout.setObjectName(u"electrumV1FromWIFBIP38PassphraseContainerQFrameVLayout")
        self.electrumV1FromWIFBIP38PassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame = QFrame(self.electrumV1FromWIFBIP38PassphraseContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame.setObjectName(u"electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame")
        self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.setObjectName(u"electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout")
        self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFBIP38PassphraseQCheckBox = QCheckBox(self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseQCheckBox.setObjectName(u"electrumV1FromWIFBIP38PassphraseQCheckBox")

        self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.addWidget(self.electrumV1FromWIFBIP38PassphraseQCheckBox)

        self.electrumV1FromWIFBIP38PassphraseContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.addItem(self.electrumV1FromWIFBIP38PassphraseContainerQFrameHSpacer)


        self.electrumV1FromWIFBIP38PassphraseContainerQFrameVLayout.addWidget(self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame)

        self.electrumV1FromWIFBIP38PassphraseQLineEdit = QLineEdit(self.electrumV1FromWIFBIP38PassphraseContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseQLineEdit.setObjectName(u"electrumV1FromWIFBIP38PassphraseQLineEdit")

        self.electrumV1FromWIFBIP38PassphraseContainerQFrameVLayout.addWidget(self.electrumV1FromWIFBIP38PassphraseQLineEdit)


        self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV1FromWIFBIP38PassphraseContainerQFrame)


        self.electrumV1FromWIFQStackedWidgetVLayout.addWidget(self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame)

        self.electrumV1FromWIFQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.electrumV1FromWIFQStackedWidgetVLayout.addItem(self.electrumV1FromWIFQStackedWidgetVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromWIFQStackedWidget)
        self.electrumV1FromPrivateKeyQStackedWidget = QWidget()
        self.electrumV1FromPrivateKeyQStackedWidget.setObjectName(u"electrumV1FromPrivateKeyQStackedWidget")
        self.electrumV1FromPrivateKeyQStackedWidgetVLayout = QVBoxLayout(self.electrumV1FromPrivateKeyQStackedWidget)
        self.electrumV1FromPrivateKeyQStackedWidgetVLayout.setSpacing(15)
        self.electrumV1FromPrivateKeyQStackedWidgetVLayout.setObjectName(u"electrumV1FromPrivateKeyQStackedWidgetVLayout")
        self.electrumV1FromPrivateKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromPrivateKeyQStackedWidget)
        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame")
        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame.setFrameShadow(QFrame.Raised)
        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout")
        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyContainerQFrame = QFrame(self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromPrivateKeyContainerQFrame.setObjectName(u"electrumV1FromPrivateKeyContainerQFrame")
        self.electrumV1FromPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromPrivateKeyContainerQFrame)
        self.electrumV1FromPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromPrivateKeyContainerQFrameVLayout.setObjectName(u"electrumV1FromPrivateKeyContainerQFrameVLayout")
        self.electrumV1FromPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyLabelContainerQFrame = QFrame(self.electrumV1FromPrivateKeyContainerQFrame)
        self.electrumV1FromPrivateKeyLabelContainerQFrame.setObjectName(u"electrumV1FromPrivateKeyLabelContainerQFrame")
        self.electrumV1FromPrivateKeyLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromPrivateKeyLabelContainerQFrame)
        self.electrumV1FromPrivateKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromPrivateKeyLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromPrivateKeyLabelContainerQFrameHLayout")
        self.electrumV1FromPrivateKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyQLabel = QLabel(self.electrumV1FromPrivateKeyLabelContainerQFrame)
        self.electrumV1FromPrivateKeyQLabel.setObjectName(u"electrumV1FromPrivateKeyQLabel")

        self.electrumV1FromPrivateKeyLabelContainerQFrameHLayout.addWidget(self.electrumV1FromPrivateKeyQLabel)

        self.electrumV1FromPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromPrivateKeyLabelContainerQFrameHLayout.addItem(self.electrumV1FromPrivateKeyLabelContainerQFrameHSpacer)


        self.electrumV1FromPrivateKeyContainerQFrameVLayout.addWidget(self.electrumV1FromPrivateKeyLabelContainerQFrame)

        self.electrumV1FromPrivateKeyQLineEdit = QLineEdit(self.electrumV1FromPrivateKeyContainerQFrame)
        self.electrumV1FromPrivateKeyQLineEdit.setObjectName(u"electrumV1FromPrivateKeyQLineEdit")

        self.electrumV1FromPrivateKeyContainerQFrameVLayout.addWidget(self.electrumV1FromPrivateKeyQLineEdit)


        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV1FromPrivateKeyContainerQFrame)

        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame")
        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"electrumV1FromPrivateKeyPublicKeyTypeContainerQFrameVLayout")
        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame")
        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout")
        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyPublicKeyTypeQLabel = QLabel(self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromPrivateKeyPublicKeyTypeQLabel.setObjectName(u"electrumV1FromPrivateKeyPublicKeyTypeQLabel")

        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.electrumV1FromPrivateKeyPublicKeyTypeQLabel)

        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox = QComboBox(self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromPrivateKeyPublicKeyTypeQComboBox")

        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox)


        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame)


        self.electrumV1FromPrivateKeyQStackedWidgetVLayout.addWidget(self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame)

        self.electrumV1FromPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.electrumV1FromPrivateKeyQStackedWidgetVLayout.addItem(self.electrumV1FromPrivateKeyQStackedWidgetVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromPrivateKeyQStackedWidget)
        self.electrumV1FromPublicKeyQStackedWidget = QWidget()
        self.electrumV1FromPublicKeyQStackedWidget.setObjectName(u"electrumV1FromPublicKeyQStackedWidget")
        self.electrumV1FromPublicKeyQStackedWidgetVLayout = QVBoxLayout(self.electrumV1FromPublicKeyQStackedWidget)
        self.electrumV1FromPublicKeyQStackedWidgetVLayout.setSpacing(15)
        self.electrumV1FromPublicKeyQStackedWidgetVLayout.setObjectName(u"electrumV1FromPublicKeyQStackedWidgetVLayout")
        self.electrumV1FromPublicKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromPublicKeyQStackedWidget)
        self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame")
        self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrameHLayout")
        self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyContainerQFrame = QFrame(self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyContainerQFrame.setObjectName(u"electrumV1FromPublicKeyContainerQFrame")
        self.electrumV1FromPublicKeyContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromPublicKeyContainerQFrame)
        self.electrumV1FromPublicKeyContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromPublicKeyContainerQFrameVLayout.setObjectName(u"electrumV1FromPublicKeyContainerQFrameVLayout")
        self.electrumV1FromPublicKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyLabelContainerQFrame = QFrame(self.electrumV1FromPublicKeyContainerQFrame)
        self.electrumV1FromPublicKeyLabelContainerQFrame.setObjectName(u"electrumV1FromPublicKeyLabelContainerQFrame")
        self.electrumV1FromPublicKeyLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromPublicKeyLabelContainerQFrame)
        self.electrumV1FromPublicKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromPublicKeyLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromPublicKeyLabelContainerQFrameHLayout")
        self.electrumV1FromPublicKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyQLabel = QLabel(self.electrumV1FromPublicKeyLabelContainerQFrame)
        self.electrumV1FromPublicKeyQLabel.setObjectName(u"electrumV1FromPublicKeyQLabel")

        self.electrumV1FromPublicKeyLabelContainerQFrameHLayout.addWidget(self.electrumV1FromPublicKeyQLabel)

        self.electrumV1FromPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromPublicKeyLabelContainerQFrameHLayout.addItem(self.electrumV1FromPublicKeyLabelContainerQFrameHSpacer)


        self.electrumV1FromPublicKeyContainerQFrameVLayout.addWidget(self.electrumV1FromPublicKeyLabelContainerQFrame)

        self.electrumV1FromPublicKeyQLineEdit = QLineEdit(self.electrumV1FromPublicKeyContainerQFrame)
        self.electrumV1FromPublicKeyQLineEdit.setObjectName(u"electrumV1FromPublicKeyQLineEdit")

        self.electrumV1FromPublicKeyContainerQFrameVLayout.addWidget(self.electrumV1FromPublicKeyQLineEdit)


        self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV1FromPublicKeyContainerQFrame)

        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeContainerQFrame")
        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeContainerQFrameVLayout")
        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame")
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout")
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyPublicKeyTypeQLabel = QLabel(self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeQLabel.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeQLabel")

        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.electrumV1FromPublicKeyPublicKeyTypeQLabel)

        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox = QComboBox(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeQComboBox")

        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV1FromPublicKeyPublicKeyTypeQComboBox)


        self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)


        self.electrumV1FromPublicKeyQStackedWidgetVLayout.addWidget(self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame)

        self.electrumV1FromPublicKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.electrumV1FromPublicKeyQStackedWidgetVLayout.addItem(self.electrumV1FromPublicKeyQStackedWidgetVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromPublicKeyQStackedWidget)

        self.electrumV1PageQWidgetVLayout.addWidget(self.electrumV1QStackedWidget)

        self.hdQStackedWidget.addWidget(self.electrumV1PageQWidget)
        self.electrumV2PageQWidget = QWidget()
        self.electrumV2PageQWidget.setObjectName(u"electrumV2PageQWidget")
        self.electrumV2PageQWidgetVLayout = QVBoxLayout(self.electrumV2PageQWidget)
        self.electrumV2PageQWidgetVLayout.setSpacing(0)
        self.electrumV2PageQWidgetVLayout.setObjectName(u"electrumV2PageQWidgetVLayout")
        self.electrumV2PageQWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2QStackedWidget = QStackedWidget(self.electrumV2PageQWidget)
        self.electrumV2QStackedWidget.setObjectName(u"electrumV2QStackedWidget")
        self.electrumV2FromEntropyQStackedWidget = QWidget()
        self.electrumV2FromEntropyQStackedWidget.setObjectName(u"electrumV2FromEntropyQStackedWidget")
        self.electrumV2FromEntropyQStackedWidgetVLayout = QVBoxLayout(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromEntropyQStackedWidgetVLayout.setSpacing(15)
        self.electrumV2FromEntropyQStackedWidgetVLayout.setObjectName(u"electrumV2FromEntropyQStackedWidgetVLayout")
        self.electrumV2FromEntropyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame = QFrame(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame.setObjectName(u"electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame")
        self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrameHLayout.setObjectName(u"electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrameHLayout")
        self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyContainerQFrame = QFrame(self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromEntropyContainerQFrame.setObjectName(u"electrumV2FromEntropyContainerQFrame")
        self.electrumV2FromEntropyContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromEntropyContainerQFrame)
        self.electrumV2FromEntropyContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromEntropyContainerQFrameVLayout.setObjectName(u"electrumV2FromEntropyContainerQFrameVLayout")
        self.electrumV2FromEntropyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyLabelContainerQFrame = QFrame(self.electrumV2FromEntropyContainerQFrame)
        self.electrumV2FromEntropyLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyLabelContainerQFrame")
        self.electrumV2FromEntropyLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromEntropyLabelContainerQFrame)
        self.electrumV2FromEntropyLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromEntropyLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromEntropyLabelContainerQFrameHLayout")
        self.electrumV2FromEntropyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyQLabel = QLabel(self.electrumV2FromEntropyLabelContainerQFrame)
        self.electrumV2FromEntropyQLabel.setObjectName(u"electrumV2FromEntropyQLabel")

        self.electrumV2FromEntropyLabelContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyQLabel)

        self.electrumV2FromEntropyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromEntropyLabelContainerQFrameHLayout.addItem(self.electrumV2FromEntropyLabelContainerQFrameHSpacer)


        self.electrumV2FromEntropyContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyLabelContainerQFrame)

        self.electrumV2FromEntropyGenerateContainerQFrame = QFrame(self.electrumV2FromEntropyContainerQFrame)
        self.electrumV2FromEntropyGenerateContainerQFrame.setObjectName(u"electrumV2FromEntropyGenerateContainerQFrame")
        self.electrumV2FromEntropyGenerateContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromEntropyGenerateContainerQFrame)
        self.electrumV2FromEntropyGenerateContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromEntropyGenerateContainerQFrameHLayout.setObjectName(u"electrumV2FromEntropyGenerateContainerQFrameHLayout")
        self.electrumV2FromEntropyGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyGenerateQLineEdit = QLineEdit(self.electrumV2FromEntropyGenerateContainerQFrame)
        self.electrumV2FromEntropyGenerateQLineEdit.setObjectName(u"electrumV2FromEntropyGenerateQLineEdit")

        self.electrumV2FromEntropyGenerateContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyGenerateQLineEdit)


        self.electrumV2FromEntropyContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyGenerateContainerQFrame)


        self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyContainerQFrame)

        self.electrumV2FromEntropyPublicKeyTypeContainerQFrame = QFrame(self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromEntropyPublicKeyTypeContainerQFrame.setObjectName(u"electrumV2FromEntropyPublicKeyTypeContainerQFrame")
        self.electrumV2FromEntropyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.electrumV2FromEntropyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromEntropyPublicKeyTypeContainerQFrame)
        self.electrumV2FromEntropyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromEntropyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"electrumV2FromEntropyPublicKeyTypeContainerQFrameVLayout")
        self.electrumV2FromEntropyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV2FromEntropyPublicKeyTypeContainerQFrame)
        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame")
        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame)
        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHLayout")
        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyPublicKeyTypeQLabel = QLabel(self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame)
        self.electrumV2FromEntropyPublicKeyTypeQLabel.setObjectName(u"electrumV2FromEntropyPublicKeyTypeQLabel")

        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyPublicKeyTypeQLabel)

        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.electrumV2FromEntropyPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame)

        self.electrumV2FromEntropyPublicKeyTypeQComboBox = QComboBox(self.electrumV2FromEntropyPublicKeyTypeContainerQFrame)
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setObjectName(u"electrumV2FromEntropyPublicKeyTypeQComboBox")

        self.electrumV2FromEntropyPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyPublicKeyTypeQComboBox)


        self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyPublicKeyTypeContainerQFrame)


        self.electrumV2FromEntropyQStackedWidgetVLayout.addWidget(self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame)

        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame = QFrame(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame.setObjectName(u"electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame")
        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)
        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrameHLayout.setObjectName(u"electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrameHLayout")
        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyModeContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)
        self.electrumV2FromEntropyModeContainerQFrame.setObjectName(u"electrumV2FromEntropyModeContainerQFrame")
        self.electrumV2FromEntropyModeContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromEntropyModeContainerQFrame)
        self.electrumV2FromEntropyModeContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromEntropyModeContainerQFrameVLayout.setObjectName(u"electrumV2FromEntropyModeContainerQFrameVLayout")
        self.electrumV2FromEntropyModeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyModeLabelContainerQFrame = QFrame(self.electrumV2FromEntropyModeContainerQFrame)
        self.electrumV2FromEntropyModeLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyModeLabelContainerQFrame")
        self.electrumV2FromEntropyModeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromEntropyModeLabelContainerQFrame)
        self.electrumV2FromEntropyModeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromEntropyModeLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromEntropyModeLabelContainerQFrameHLayout")
        self.electrumV2FromEntropyModeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyModeQLabel = QLabel(self.electrumV2FromEntropyModeLabelContainerQFrame)
        self.electrumV2FromEntropyModeQLabel.setObjectName(u"electrumV2FromEntropyModeQLabel")

        self.electrumV2FromEntropyModeLabelContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyModeQLabel)

        self.electrumV2FromEntropyModeLabelContainerQFrameHSpacer = QSpacerItem(16, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromEntropyModeLabelContainerQFrameHLayout.addItem(self.electrumV2FromEntropyModeLabelContainerQFrameHSpacer)


        self.electrumV2FromEntropyModeContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyModeLabelContainerQFrame)

        self.electrumV2FromEntropyModeQComboBox = QComboBox(self.electrumV2FromEntropyModeContainerQFrame)
        self.electrumV2FromEntropyModeQComboBox.setObjectName(u"electrumV2FromEntropyModeQComboBox")

        self.electrumV2FromEntropyModeContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyModeQComboBox)


        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyModeContainerQFrame)

        self.electrumV2FromEntropyLanguageContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)
        self.electrumV2FromEntropyLanguageContainerQFrame.setObjectName(u"electrumV2FromEntropyLanguageContainerQFrame")
        self.electrumV2FromEntropyLanguageContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromEntropyLanguageContainerQFrame)
        self.electrumV2FromEntropyLanguageContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromEntropyLanguageContainerQFrameVLayout.setObjectName(u"electrumV2FromEntropyLanguageContainerQFrameVLayout")
        self.electrumV2FromEntropyLanguageContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyLanguageLabelContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageContainerQFrame)
        self.electrumV2FromEntropyLanguageLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyLanguageLabelContainerQFrame")
        self.electrumV2FromEntropyLanguageLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromEntropyLanguageLabelContainerQFrame)
        self.electrumV2FromEntropyLanguageLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromEntropyLanguageLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromEntropyLanguageLabelContainerQFrameHLayout")
        self.electrumV2FromEntropyLanguageLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyLanguageQLabel = QLabel(self.electrumV2FromEntropyLanguageLabelContainerQFrame)
        self.electrumV2FromEntropyLanguageQLabel.setObjectName(u"electrumV2FromEntropyLanguageQLabel")

        self.electrumV2FromEntropyLanguageLabelContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyLanguageQLabel)


        self.electrumV2FromEntropyLanguageContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyLanguageLabelContainerQFrame)

        self.electrumV2FromEntropyLanguageQComboBox = QComboBox(self.electrumV2FromEntropyLanguageContainerQFrame)
        self.electrumV2FromEntropyLanguageQComboBox.addItem("")
        self.electrumV2FromEntropyLanguageQComboBox.addItem("")
        self.electrumV2FromEntropyLanguageQComboBox.addItem("")
        self.electrumV2FromEntropyLanguageQComboBox.addItem("")
        self.electrumV2FromEntropyLanguageQComboBox.addItem("")
        self.electrumV2FromEntropyLanguageQComboBox.addItem("")
        self.electrumV2FromEntropyLanguageQComboBox.addItem("")
        self.electrumV2FromEntropyLanguageQComboBox.addItem("")
        self.electrumV2FromEntropyLanguageQComboBox.setObjectName(u"electrumV2FromEntropyLanguageQComboBox")

        self.electrumV2FromEntropyLanguageContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyLanguageQComboBox)


        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyLanguageContainerQFrame)

        self.electrumV2FromEntropyMnemonicTypeContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)
        self.electrumV2FromEntropyMnemonicTypeContainerQFrame.setObjectName(u"electrumV2FromEntropyMnemonicTypeContainerQFrame")
        self.electrumV2FromEntropyMnemonicTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromEntropyMnemonicTypeContainerQFrame)
        self.electrumV2FromEntropyMnemonicTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromEntropyMnemonicTypeContainerQFrameVLayout.setObjectName(u"electrumV2FromEntropyMnemonicTypeContainerQFrameVLayout")
        self.electrumV2FromEntropyMnemonicTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyMnemonicTypeQLabel = QLabel(self.electrumV2FromEntropyMnemonicTypeContainerQFrame)
        self.electrumV2FromEntropyMnemonicTypeQLabel.setObjectName(u"electrumV2FromEntropyMnemonicTypeQLabel")

        self.electrumV2FromEntropyMnemonicTypeContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyMnemonicTypeQLabel)

        self.electrumV2FromEntropyMnemonicTypeQComboBox = QComboBox(self.electrumV2FromEntropyMnemonicTypeContainerQFrame)
        self.electrumV2FromEntropyMnemonicTypeQComboBox.setObjectName(u"electrumV2FromEntropyMnemonicTypeQComboBox")

        self.electrumV2FromEntropyMnemonicTypeContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyMnemonicTypeQComboBox)


        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyMnemonicTypeContainerQFrame)

        self.electrumV2FromEntropyPassphraseContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)
        self.electrumV2FromEntropyPassphraseContainerQFrame.setObjectName(u"electrumV2FromEntropyPassphraseContainerQFrame")
        self.electrumV2FromEntropyPassphraseContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromEntropyPassphraseContainerQFrame)
        self.electrumV2FromEntropyPassphraseContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromEntropyPassphraseContainerQFrameVLayout.setObjectName(u"electrumV2FromEntropyPassphraseContainerQFrameVLayout")
        self.electrumV2FromEntropyPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyPassphraseLabelContainerQFrame = QFrame(self.electrumV2FromEntropyPassphraseContainerQFrame)
        self.electrumV2FromEntropyPassphraseLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyPassphraseLabelContainerQFrame")
        self.electrumV2FromEntropyPassphraseLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromEntropyPassphraseLabelContainerQFrame)
        self.electrumV2FromEntropyPassphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromEntropyPassphraseLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromEntropyPassphraseLabelContainerQFrameHLayout")
        self.electrumV2FromEntropyPassphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyPassphraseQLabel = QLabel(self.electrumV2FromEntropyPassphraseLabelContainerQFrame)
        self.electrumV2FromEntropyPassphraseQLabel.setObjectName(u"electrumV2FromEntropyPassphraseQLabel")

        self.electrumV2FromEntropyPassphraseLabelContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyPassphraseQLabel)

        self.electrumV2FromEntropyPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromEntropyPassphraseLabelContainerQFrameHLayout.addItem(self.electrumV2FromEntropyPassphraseLabelContainerQFrameHSpacer)


        self.electrumV2FromEntropyPassphraseContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyPassphraseLabelContainerQFrame)

        self.electrumV2FromEntropyPassphraseGenerateContainerQFrame = QFrame(self.electrumV2FromEntropyPassphraseContainerQFrame)
        self.electrumV2FromEntropyPassphraseGenerateContainerQFrame.setObjectName(u"electrumV2FromEntropyPassphraseGenerateContainerQFrame")
        self.electrumV2FromEntropyPassphraseGenerateContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromEntropyPassphraseGenerateContainerQFrame)
        self.electrumV2FromEntropyPassphraseGenerateContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromEntropyPassphraseGenerateContainerQFrameHLayout.setObjectName(u"electrumV2FromEntropyPassphraseGenerateContainerQFrameHLayout")
        self.electrumV2FromEntropyPassphraseGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyPassphraseGenerateQLineEdit = QLineEdit(self.electrumV2FromEntropyPassphraseGenerateContainerQFrame)
        self.electrumV2FromEntropyPassphraseGenerateQLineEdit.setObjectName(u"electrumV2FromEntropyPassphraseGenerateQLineEdit")

        self.electrumV2FromEntropyPassphraseGenerateContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyPassphraseGenerateQLineEdit)


        self.electrumV2FromEntropyPassphraseContainerQFrameVLayout.addWidget(self.electrumV2FromEntropyPassphraseGenerateContainerQFrame)


        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrameHLayout.addWidget(self.electrumV2FromEntropyPassphraseContainerQFrame)


        self.electrumV2FromEntropyQStackedWidgetVLayout.addWidget(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.electrumV2FromEntropyQStackedWidgetVLayout.addItem(self.verticalSpacer_3)

        self.electrumV2QStackedWidget.addWidget(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromMnemonicQStackedWidget = QWidget()
        self.electrumV2FromMnemonicQStackedWidget.setObjectName(u"electrumV2FromMnemonicQStackedWidget")
        self.electrumV2FromMnemonicQStackedWidgetVLayout = QVBoxLayout(self.electrumV2FromMnemonicQStackedWidget)
        self.electrumV2FromMnemonicQStackedWidgetVLayout.setSpacing(15)
        self.electrumV2FromMnemonicQStackedWidgetVLayout.setObjectName(u"electrumV2FromMnemonicQStackedWidgetVLayout")
        self.electrumV2FromMnemonicQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame = QFrame(self.electrumV2FromMnemonicQStackedWidget)
        self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame.setObjectName(u"electrumV2FromMnemonicAndMnemonicTypeContainerQFrame")
        self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame)
        self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrameHLayout.setObjectName(u"electrumV2FromMnemonicAndMnemonicTypeContainerQFrameHLayout")
        self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicContainerQFrame = QFrame(self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame)
        self.electrumV2FromMnemonicContainerQFrame.setObjectName(u"electrumV2FromMnemonicContainerQFrame")
        self.electrumV2FromMnemonicContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromMnemonicContainerQFrame)
        self.electrumV2FromMnemonicContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromMnemonicContainerQFrameVLayout.setObjectName(u"electrumV2FromMnemonicContainerQFrameVLayout")
        self.electrumV2FromMnemonicContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicContainerQFrame)
        self.electrumV2FromMnemonicLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicLabelContainerQFrame")
        self.electrumV2FromMnemonicLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromMnemonicLabelContainerQFrame)
        self.electrumV2FromMnemonicLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromMnemonicLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromMnemonicLabelContainerQFrameHLayout")
        self.electrumV2FromMnemonicLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicQLabel = QLabel(self.electrumV2FromMnemonicLabelContainerQFrame)
        self.electrumV2FromMnemonicQLabel.setObjectName(u"electrumV2FromMnemonicQLabel")

        self.electrumV2FromMnemonicLabelContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicQLabel)

        self.electrumV2FromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromMnemonicLabelContainerQFrameHLayout.addItem(self.electrumV2FromMnemonicLabelContainerQFrameHSpacer)


        self.electrumV2FromMnemonicContainerQFrameVLayout.addWidget(self.electrumV2FromMnemonicLabelContainerQFrame)

        self.electrumV2FromMnemonicGenerateContainerQFrame = QFrame(self.electrumV2FromMnemonicContainerQFrame)
        self.electrumV2FromMnemonicGenerateContainerQFrame.setObjectName(u"electrumV2FromMnemonicGenerateContainerQFrame")
        self.electrumV2FromMnemonicGenerateContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromMnemonicGenerateContainerQFrame)
        self.electrumV2FromMnemonicGenerateContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromMnemonicGenerateContainerQFrameHLayout.setObjectName(u"electrumV2FromMnemonicGenerateContainerQFrameHLayout")
        self.electrumV2FromMnemonicGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicGenerateQLineEdit = QLineEdit(self.electrumV2FromMnemonicGenerateContainerQFrame)
        self.electrumV2FromMnemonicGenerateQLineEdit.setObjectName(u"electrumV2FromMnemonicGenerateQLineEdit")

        self.electrumV2FromMnemonicGenerateContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicGenerateQLineEdit)


        self.electrumV2FromMnemonicContainerQFrameVLayout.addWidget(self.electrumV2FromMnemonicGenerateContainerQFrame)


        self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicContainerQFrame)

        self.electrumV2FromMnemonicMnemonicTypeContainerQFrame = QFrame(self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame)
        self.electrumV2FromMnemonicMnemonicTypeContainerQFrame.setObjectName(u"electrumV2FromMnemonicMnemonicTypeContainerQFrame")
        self.electrumV2FromMnemonicMnemonicTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromMnemonicMnemonicTypeContainerQFrame)
        self.electrumV2FromMnemonicMnemonicTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromMnemonicMnemonicTypeContainerQFrameVLayout.setObjectName(u"electrumV2FromMnemonicMnemonicTypeContainerQFrameVLayout")
        self.electrumV2FromMnemonicMnemonicTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicMnemonicTypeContainerQFrame)
        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame")
        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame)
        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHLayout")
        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicMnemonicTypeQLabel = QLabel(self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame)
        self.electrumV2FromMnemonicMnemonicTypeQLabel.setObjectName(u"electrumV2FromMnemonicMnemonicTypeQLabel")

        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicMnemonicTypeQLabel)

        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHSpacer = QSpacerItem(49, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHLayout.addItem(self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHSpacer)


        self.electrumV2FromMnemonicMnemonicTypeContainerQFrameVLayout.addWidget(self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame)

        self.electrumV2FromMnemonicMnemonicTypeQComboBox = QComboBox(self.electrumV2FromMnemonicMnemonicTypeContainerQFrame)
        self.electrumV2FromMnemonicMnemonicTypeQComboBox.setObjectName(u"electrumV2FromMnemonicMnemonicTypeQComboBox")

        self.electrumV2FromMnemonicMnemonicTypeContainerQFrameVLayout.addWidget(self.electrumV2FromMnemonicMnemonicTypeQComboBox)


        self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicMnemonicTypeContainerQFrame)


        self.electrumV2FromMnemonicQStackedWidgetVLayout.addWidget(self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame)

        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame = QFrame(self.electrumV2FromMnemonicQStackedWidget)
        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame.setObjectName(u"electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame")
        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrameHLayout.setObjectName(u"electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrameHLayout")
        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicModeContainerQFrame = QFrame(self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromMnemonicModeContainerQFrame.setObjectName(u"electrumV2FromMnemonicModeContainerQFrame")
        self.electrumV2FromMnemonicModeContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromMnemonicModeContainerQFrame)
        self.electrumV2FromMnemonicModeContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromMnemonicModeContainerQFrameVLayout.setObjectName(u"electrumV2FromMnemonicModeContainerQFrameVLayout")
        self.electrumV2FromMnemonicModeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicModeLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicModeContainerQFrame)
        self.electrumV2FromMnemonicModeLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicModeLabelContainerQFrame")
        self.electrumV2FromMnemonicModeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromMnemonicModeLabelContainerQFrame)
        self.electrumV2FromMnemonicModeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromMnemonicModeLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromMnemonicModeLabelContainerQFrameHLayout")
        self.electrumV2FromMnemonicModeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicModeQLabel = QLabel(self.electrumV2FromMnemonicModeLabelContainerQFrame)
        self.electrumV2FromMnemonicModeQLabel.setObjectName(u"electrumV2FromMnemonicModeQLabel")

        self.electrumV2FromMnemonicModeLabelContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicModeQLabel)

        self.electrumV2FromMnemonicModeLabelContainerQFrameHSpacer = QSpacerItem(49, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromMnemonicModeLabelContainerQFrameHLayout.addItem(self.electrumV2FromMnemonicModeLabelContainerQFrameHSpacer)


        self.electrumV2FromMnemonicModeContainerQFrameVLayout.addWidget(self.electrumV2FromMnemonicModeLabelContainerQFrame)

        self.electrumV2FromMnemonicModeQComboBox = QComboBox(self.electrumV2FromMnemonicModeContainerQFrame)
        self.electrumV2FromMnemonicModeQComboBox.setObjectName(u"electrumV2FromMnemonicModeQComboBox")

        self.electrumV2FromMnemonicModeContainerQFrameVLayout.addWidget(self.electrumV2FromMnemonicModeQComboBox)


        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicModeContainerQFrame)

        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame = QFrame(self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame.setObjectName(u"electrumV2FromMnemonicPublicKeyTypeContainerQFrame")
        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame)
        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrameVLayout.setObjectName(u"electrumV2FromMnemonicPublicKeyTypeContainerQFrameVLayout")
        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame)
        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame")
        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout")
        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicPublicKeyTypeQLabel = QLabel(self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.electrumV2FromMnemonicPublicKeyTypeQLabel.setObjectName(u"electrumV2FromMnemonicPublicKeyTypeQLabel")

        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicPublicKeyTypeQLabel)

        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer)


        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame)

        self.electrumV2FromMnemonicPublicKeyTypeQComboBox = QComboBox(self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame)
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setObjectName(u"electrumV2FromMnemonicPublicKeyTypeQComboBox")

        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV2FromMnemonicPublicKeyTypeQComboBox)


        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame)

        self.electrumV2FromMnemonicPassphraseContainerQFrame = QFrame(self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromMnemonicPassphraseContainerQFrame.setObjectName(u"electrumV2FromMnemonicPassphraseContainerQFrame")
        self.electrumV2FromMnemonicPassphraseContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromMnemonicPassphraseContainerQFrame)
        self.electrumV2FromMnemonicPassphraseContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromMnemonicPassphraseContainerQFrameVLayout.setObjectName(u"electrumV2FromMnemonicPassphraseContainerQFrameVLayout")
        self.electrumV2FromMnemonicPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicPassphraseLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicPassphraseContainerQFrame)
        self.electrumV2FromMnemonicPassphraseLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicPassphraseLabelContainerQFrame")
        self.electrumV2FromMnemonicPassphraseLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromMnemonicPassphraseLabelContainerQFrame)
        self.electrumV2FromMnemonicPassphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromMnemonicPassphraseLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromMnemonicPassphraseLabelContainerQFrameHLayout")
        self.electrumV2FromMnemonicPassphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicPassphraseQLabel = QLabel(self.electrumV2FromMnemonicPassphraseLabelContainerQFrame)
        self.electrumV2FromMnemonicPassphraseQLabel.setObjectName(u"electrumV2FromMnemonicPassphraseQLabel")

        self.electrumV2FromMnemonicPassphraseLabelContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicPassphraseQLabel)

        self.electrumV2FromMnemonicPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromMnemonicPassphraseLabelContainerQFrameHLayout.addItem(self.electrumV2FromMnemonicPassphraseLabelContainerQFrameHSpacer)


        self.electrumV2FromMnemonicPassphraseContainerQFrameVLayout.addWidget(self.electrumV2FromMnemonicPassphraseLabelContainerQFrame)

        self.electrumV2FromMnemonicPassphraseGenerateContainerQFrame = QFrame(self.electrumV2FromMnemonicPassphraseContainerQFrame)
        self.electrumV2FromMnemonicPassphraseGenerateContainerQFrame.setObjectName(u"electrumV2FromMnemonicPassphraseGenerateContainerQFrame")
        self.electrumV2FromMnemonicPassphraseGenerateContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromMnemonicPassphraseGenerateContainerQFrame)
        self.electrumV2FromMnemonicPassphraseGenerateContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromMnemonicPassphraseGenerateContainerQFrameHLayout.setObjectName(u"electrumV2FromMnemonicPassphraseGenerateContainerQFrameHLayout")
        self.electrumV2FromMnemonicPassphraseGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicPassphraseGenerateQLineEdit = QLineEdit(self.electrumV2FromMnemonicPassphraseGenerateContainerQFrame)
        self.electrumV2FromMnemonicPassphraseGenerateQLineEdit.setObjectName(u"electrumV2FromMnemonicPassphraseGenerateQLineEdit")

        self.electrumV2FromMnemonicPassphraseGenerateContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicPassphraseGenerateQLineEdit)


        self.electrumV2FromMnemonicPassphraseContainerQFrameVLayout.addWidget(self.electrumV2FromMnemonicPassphraseGenerateContainerQFrame)


        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrameHLayout.addWidget(self.electrumV2FromMnemonicPassphraseContainerQFrame)


        self.electrumV2FromMnemonicQStackedWidgetVLayout.addWidget(self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame)

        self.electrumV2FromMnemonicQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.electrumV2FromMnemonicQStackedWidgetVLayout.addItem(self.electrumV2FromMnemonicQStackedWidgetVSpacer)

        self.electrumV2QStackedWidget.addWidget(self.electrumV2FromMnemonicQStackedWidget)
        self.electrumV2FromSeedQStackedWidget = QWidget()
        self.electrumV2FromSeedQStackedWidget.setObjectName(u"electrumV2FromSeedQStackedWidget")
        self.electrumV2FromSeedQStackedWidgetVLayout = QVBoxLayout(self.electrumV2FromSeedQStackedWidget)
        self.electrumV2FromSeedQStackedWidgetVLayout.setSpacing(15)
        self.electrumV2FromSeedQStackedWidgetVLayout.setObjectName(u"electrumV2FromSeedQStackedWidgetVLayout")
        self.electrumV2FromSeedQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedContainerQFrame = QFrame(self.electrumV2FromSeedQStackedWidget)
        self.electrumV2FromSeedContainerQFrame.setObjectName(u"electrumV2FromSeedContainerQFrame")
        self.electrumV2FromSeedContainerQFrame.setMinimumSize(QSize(400, 0))
        self.electrumV2FromSeedContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromSeedContainerQFrame)
        self.electrumV2FromSeedContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromSeedContainerQFrameVLayout.setObjectName(u"electrumV2FromSeedContainerQFrameVLayout")
        self.electrumV2FromSeedContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame = QFrame(self.electrumV2FromSeedContainerQFrame)
        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame")
        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"electrumV2FromSeedModeAndPublicKeyTypeContainerQFrameHLayout")
        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedsContainerQFrame = QFrame(self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedsContainerQFrame.setObjectName(u"electrumV2FromSeedsContainerQFrame")
        self.electrumV2FromSeedsContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromSeedsContainerQFrame)
        self.electrumV2FromSeedsContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromSeedsContainerQFrameVLayout.setObjectName(u"electrumV2FromSeedsContainerQFrameVLayout")
        self.electrumV2FromSeedsContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedsLabelContainerQFrame = QFrame(self.electrumV2FromSeedsContainerQFrame)
        self.electrumV2FromSeedsLabelContainerQFrame.setObjectName(u"electrumV2FromSeedsLabelContainerQFrame")
        self.electrumV2FromSeedsLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromSeedsLabelContainerQFrame)
        self.electrumV2FromSeedsLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromSeedsLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromSeedsLabelContainerQFrameHLayout")
        self.electrumV2FromSeedsLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedsQLabel = QLabel(self.electrumV2FromSeedsLabelContainerQFrame)
        self.electrumV2FromSeedsQLabel.setObjectName(u"electrumV2FromSeedsQLabel")

        self.electrumV2FromSeedsLabelContainerQFrameHLayout.addWidget(self.electrumV2FromSeedsQLabel)

        self.electrumV2FromSeedsLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromSeedsLabelContainerQFrameHLayout.addItem(self.electrumV2FromSeedsLabelContainerQFrameHSpacer)


        self.electrumV2FromSeedsContainerQFrameVLayout.addWidget(self.electrumV2FromSeedsLabelContainerQFrame)

        self.electrumV2FromSeedsQLineEdit = QLineEdit(self.electrumV2FromSeedsContainerQFrame)
        self.electrumV2FromSeedsQLineEdit.setObjectName(u"electrumV2FromSeedsQLineEdit")

        self.electrumV2FromSeedsContainerQFrameVLayout.addWidget(self.electrumV2FromSeedsQLineEdit)


        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV2FromSeedsContainerQFrame)

        self.electrumV2FromSeedModeContainerQFrame = QFrame(self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedModeContainerQFrame.setObjectName(u"electrumV2FromSeedModeContainerQFrame")
        self.electrumV2FromSeedModeContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromSeedModeContainerQFrame)
        self.electrumV2FromSeedModeContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromSeedModeContainerQFrameVLayout.setObjectName(u"electrumV2FromSeedModeContainerQFrameVLayout")
        self.electrumV2FromSeedModeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedModeQLabel = QLabel(self.electrumV2FromSeedModeContainerQFrame)
        self.electrumV2FromSeedModeQLabel.setObjectName(u"electrumV2FromSeedModeQLabel")

        self.electrumV2FromSeedModeContainerQFrameVLayout.addWidget(self.electrumV2FromSeedModeQLabel)

        self.electrumV2FromSeedModeQComboBox = QComboBox(self.electrumV2FromSeedModeContainerQFrame)
        self.electrumV2FromSeedModeQComboBox.setObjectName(u"electrumV2FromSeedModeQComboBox")

        self.electrumV2FromSeedModeContainerQFrameVLayout.addWidget(self.electrumV2FromSeedModeQComboBox)


        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV2FromSeedModeContainerQFrame)

        self.electrumV2FromSeedPublicKeyTypeContainerQFrame = QFrame(self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedPublicKeyTypeContainerQFrame.setObjectName(u"electrumV2FromSeedPublicKeyTypeContainerQFrame")
        self.electrumV2FromSeedPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.electrumV2FromSeedPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.electrumV2FromSeedPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.electrumV2FromSeedPublicKeyTypeContainerQFrameVLayout.setObjectName(u"electrumV2FromSeedPublicKeyTypeContainerQFrameVLayout")
        self.electrumV2FromSeedPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV2FromSeedPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV2FromSeedPublicKeyTypeLabelContainerQFrame")
        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrame)
        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHLayout")
        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedPublicKeyTypeQLabel = QLabel(self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrame)
        self.electrumV2FromSeedPublicKeyTypeQLabel.setObjectName(u"electrumV2FromSeedPublicKeyTypeQLabel")

        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.electrumV2FromSeedPublicKeyTypeQLabel)

        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHSpacer)


        self.electrumV2FromSeedPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrame)

        self.electrumV2FromSeedPublicKeyTypeQComboBox = QComboBox(self.electrumV2FromSeedPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromSeedPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromSeedPublicKeyTypeQComboBox.setObjectName(u"electrumV2FromSeedPublicKeyTypeQComboBox")

        self.electrumV2FromSeedPublicKeyTypeContainerQFrameVLayout.addWidget(self.electrumV2FromSeedPublicKeyTypeQComboBox)


        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.electrumV2FromSeedPublicKeyTypeContainerQFrame)


        self.electrumV2FromSeedContainerQFrameVLayout.addWidget(self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame)

        self.electrumV2FromSeedContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.electrumV2FromSeedContainerQFrameVLayout.addItem(self.electrumV2FromSeedContainerQFrameVSpacer)


        self.electrumV2FromSeedQStackedWidgetVLayout.addWidget(self.electrumV2FromSeedContainerQFrame)

        self.electrumV2QStackedWidget.addWidget(self.electrumV2FromSeedQStackedWidget)

        self.electrumV2PageQWidgetVLayout.addWidget(self.electrumV2QStackedWidget)

        self.hdQStackedWidget.addWidget(self.electrumV2PageQWidget)
        self.moneroPageQWidget = QWidget()
        self.moneroPageQWidget.setObjectName(u"moneroPageQWidget")
        self.moneroPageQWidgetVLayout = QVBoxLayout(self.moneroPageQWidget)
        self.moneroPageQWidgetVLayout.setSpacing(0)
        self.moneroPageQWidgetVLayout.setObjectName(u"moneroPageQWidgetVLayout")
        self.moneroPageQWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroQStackedWidget = QStackedWidget(self.moneroPageQWidget)
        self.moneroQStackedWidget.setObjectName(u"moneroQStackedWidget")
        self.moneroFromEntropyQStackedWidget = QWidget()
        self.moneroFromEntropyQStackedWidget.setObjectName(u"moneroFromEntropyQStackedWidget")
        self.moneroFromEntropyQStackedWidgetVLayout = QVBoxLayout(self.moneroFromEntropyQStackedWidget)
        self.moneroFromEntropyQStackedWidgetVLayout.setSpacing(15)
        self.moneroFromEntropyQStackedWidgetVLayout.setObjectName(u"moneroFromEntropyQStackedWidgetVLayout")
        self.moneroFromEntropyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyContainerQFrame = QFrame(self.moneroFromEntropyQStackedWidget)
        self.moneroFromEntropyContainerQFrame.setObjectName(u"moneroFromEntropyContainerQFrame")
        self.moneroFromEntropyContainerQFrameVLayout = QVBoxLayout(self.moneroFromEntropyContainerQFrame)
        self.moneroFromEntropyContainerQFrameVLayout.setSpacing(5)
        self.moneroFromEntropyContainerQFrameVLayout.setObjectName(u"moneroFromEntropyContainerQFrameVLayout")
        self.moneroFromEntropyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyLabelContainerQFrame = QFrame(self.moneroFromEntropyContainerQFrame)
        self.moneroFromEntropyLabelContainerQFrame.setObjectName(u"moneroFromEntropyLabelContainerQFrame")
        self.moneroFromEntropyLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromEntropyLabelContainerQFrame)
        self.moneroFromEntropyLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromEntropyLabelContainerQFrameHLayout.setObjectName(u"moneroFromEntropyLabelContainerQFrameHLayout")
        self.moneroFromEntropyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyQLabel = QLabel(self.moneroFromEntropyLabelContainerQFrame)
        self.moneroFromEntropyQLabel.setObjectName(u"moneroFromEntropyQLabel")

        self.moneroFromEntropyLabelContainerQFrameHLayout.addWidget(self.moneroFromEntropyQLabel)

        self.moneroFromEntropyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroFromEntropyLabelContainerQFrameHLayout.addItem(self.moneroFromEntropyLabelContainerQFrameHSpacer)


        self.moneroFromEntropyContainerQFrameVLayout.addWidget(self.moneroFromEntropyLabelContainerQFrame)

        self.moneroFromEntropyLineEditContainerQFrame = QFrame(self.moneroFromEntropyContainerQFrame)
        self.moneroFromEntropyLineEditContainerQFrame.setObjectName(u"moneroFromEntropyLineEditContainerQFrame")
        self.moneroFromEntropyLineEditContainerQFrameHLayout = QHBoxLayout(self.moneroFromEntropyLineEditContainerQFrame)
        self.moneroFromEntropyLineEditContainerQFrameHLayout.setSpacing(15)
        self.moneroFromEntropyLineEditContainerQFrameHLayout.setObjectName(u"moneroFromEntropyLineEditContainerQFrameHLayout")
        self.moneroFromEntropyLineEditContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyQLineEdit = QLineEdit(self.moneroFromEntropyLineEditContainerQFrame)
        self.moneroFromEntropyQLineEdit.setObjectName(u"moneroFromEntropyQLineEdit")

        self.moneroFromEntropyLineEditContainerQFrameHLayout.addWidget(self.moneroFromEntropyQLineEdit)


        self.moneroFromEntropyContainerQFrameVLayout.addWidget(self.moneroFromEntropyLineEditContainerQFrame)


        self.moneroFromEntropyQStackedWidgetVLayout.addWidget(self.moneroFromEntropyContainerQFrame)

        self.moneroFromEntropyPassphrasePaymentIDContainerQFrame = QFrame(self.moneroFromEntropyQStackedWidget)
        self.moneroFromEntropyPassphrasePaymentIDContainerQFrame.setObjectName(u"moneroFromEntropyPassphrasePaymentIDContainerQFrame")
        self.moneroFromEntropyPassphrasePaymentIDContainerQFrameHLayout = QHBoxLayout(self.moneroFromEntropyPassphrasePaymentIDContainerQFrame)
        self.moneroFromEntropyPassphrasePaymentIDContainerQFrameHLayout.setSpacing(15)
        self.moneroFromEntropyPassphrasePaymentIDContainerQFrameHLayout.setObjectName(u"moneroFromEntropyPassphrasePaymentIDContainerQFrameHLayout")
        self.moneroFromEntropyPassphrasePaymentIDContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyLanguageContainerQFrame = QFrame(self.moneroFromEntropyPassphrasePaymentIDContainerQFrame)
        self.moneroFromEntropyLanguageContainerQFrame.setObjectName(u"moneroFromEntropyLanguageContainerQFrame")
        self.moneroFromEntropyLanguageContainerQFrameVLayout = QVBoxLayout(self.moneroFromEntropyLanguageContainerQFrame)
        self.moneroFromEntropyLanguageContainerQFrameVLayout.setSpacing(5)
        self.moneroFromEntropyLanguageContainerQFrameVLayout.setObjectName(u"moneroFromEntropyLanguageContainerQFrameVLayout")
        self.moneroFromEntropyLanguageContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyLanguageLabelContainerQFrame = QFrame(self.moneroFromEntropyLanguageContainerQFrame)
        self.moneroFromEntropyLanguageLabelContainerQFrame.setObjectName(u"moneroFromEntropyLanguageLabelContainerQFrame")
        self.moneroFromEntropyLanguageLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromEntropyLanguageLabelContainerQFrame)
        self.moneroFromEntropyLanguageLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromEntropyLanguageLabelContainerQFrameHLayout.setObjectName(u"moneroFromEntropyLanguageLabelContainerQFrameHLayout")
        self.moneroFromEntropyLanguageLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyLanguageQLabel = QLabel(self.moneroFromEntropyLanguageLabelContainerQFrame)
        self.moneroFromEntropyLanguageQLabel.setObjectName(u"moneroFromEntropyLanguageQLabel")

        self.moneroFromEntropyLanguageLabelContainerQFrameHLayout.addWidget(self.moneroFromEntropyLanguageQLabel)

        self.moneroFromEntropyLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroFromEntropyLanguageLabelContainerQFrameHLayout.addItem(self.moneroFromEntropyLanguageLabelContainerQFrameHSpacer)


        self.moneroFromEntropyLanguageContainerQFrameVLayout.addWidget(self.moneroFromEntropyLanguageLabelContainerQFrame)

        self.moneroFromEntropyLanguageQComboBox = QComboBox(self.moneroFromEntropyLanguageContainerQFrame)
        self.moneroFromEntropyLanguageQComboBox.addItem("")
        self.moneroFromEntropyLanguageQComboBox.addItem("")
        self.moneroFromEntropyLanguageQComboBox.addItem("")
        self.moneroFromEntropyLanguageQComboBox.addItem("")
        self.moneroFromEntropyLanguageQComboBox.addItem("")
        self.moneroFromEntropyLanguageQComboBox.addItem("")
        self.moneroFromEntropyLanguageQComboBox.addItem("")
        self.moneroFromEntropyLanguageQComboBox.addItem("")
        self.moneroFromEntropyLanguageQComboBox.setObjectName(u"moneroFromEntropyLanguageQComboBox")

        self.moneroFromEntropyLanguageContainerQFrameVLayout.addWidget(self.moneroFromEntropyLanguageQComboBox)


        self.moneroFromEntropyPassphrasePaymentIDContainerQFrameHLayout.addWidget(self.moneroFromEntropyLanguageContainerQFrame)

        self.moneroFromEntropyPaymentIDContainerQFrame = QFrame(self.moneroFromEntropyPassphrasePaymentIDContainerQFrame)
        self.moneroFromEntropyPaymentIDContainerQFrame.setObjectName(u"moneroFromEntropyPaymentIDContainerQFrame")
        self.moneroFromEntropyPaymentIDContainerQFrameVLayout = QVBoxLayout(self.moneroFromEntropyPaymentIDContainerQFrame)
        self.moneroFromEntropyPaymentIDContainerQFrameVLayout.setSpacing(5)
        self.moneroFromEntropyPaymentIDContainerQFrameVLayout.setObjectName(u"moneroFromEntropyPaymentIDContainerQFrameVLayout")
        self.moneroFromEntropyPaymentIDContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyPaymentIDLabelContainerQFrame = QFrame(self.moneroFromEntropyPaymentIDContainerQFrame)
        self.moneroFromEntropyPaymentIDLabelContainerQFrame.setObjectName(u"moneroFromEntropyPaymentIDLabelContainerQFrame")
        self.moneroFromEntropyPaymentIDLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromEntropyPaymentIDLabelContainerQFrame)
        self.moneroFromEntropyPaymentIDLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromEntropyPaymentIDLabelContainerQFrameHLayout.setObjectName(u"moneroFromEntropyPaymentIDLabelContainerQFrameHLayout")
        self.moneroFromEntropyPaymentIDLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyPaymentIDQLabel = QLabel(self.moneroFromEntropyPaymentIDLabelContainerQFrame)
        self.moneroFromEntropyPaymentIDQLabel.setObjectName(u"moneroFromEntropyPaymentIDQLabel")

        self.moneroFromEntropyPaymentIDLabelContainerQFrameHLayout.addWidget(self.moneroFromEntropyPaymentIDQLabel)

        self.moneroFromEntropyPaymentIDLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroFromEntropyPaymentIDLabelContainerQFrameHLayout.addItem(self.moneroFromEntropyPaymentIDLabelContainerQFrameHSpacer)


        self.moneroFromEntropyPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromEntropyPaymentIDLabelContainerQFrame)

        self.moneroFromEntropyPaymentIDQLineEdit = QLineEdit(self.moneroFromEntropyPaymentIDContainerQFrame)
        self.moneroFromEntropyPaymentIDQLineEdit.setObjectName(u"moneroFromEntropyPaymentIDQLineEdit")

        self.moneroFromEntropyPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromEntropyPaymentIDQLineEdit)


        self.moneroFromEntropyPassphrasePaymentIDContainerQFrameHLayout.addWidget(self.moneroFromEntropyPaymentIDContainerQFrame)


        self.moneroFromEntropyQStackedWidgetVLayout.addWidget(self.moneroFromEntropyPassphrasePaymentIDContainerQFrame)

        self.moneroFromEntropyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.moneroFromEntropyQStackedWidgetVLayout.addItem(self.moneroFromEntropyQStackedWidgetVSpacer)

        self.moneroQStackedWidget.addWidget(self.moneroFromEntropyQStackedWidget)
        self.moneroFromMnemonicQStackedWidget = QWidget()
        self.moneroFromMnemonicQStackedWidget.setObjectName(u"moneroFromMnemonicQStackedWidget")
        self.moneroFromMnemonicQStackedWidgetVLayout = QVBoxLayout(self.moneroFromMnemonicQStackedWidget)
        self.moneroFromMnemonicQStackedWidgetVLayout.setSpacing(15)
        self.moneroFromMnemonicQStackedWidgetVLayout.setObjectName(u"moneroFromMnemonicQStackedWidgetVLayout")
        self.moneroFromMnemonicQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicContainerQFrame = QFrame(self.moneroFromMnemonicQStackedWidget)
        self.moneroFromMnemonicContainerQFrame.setObjectName(u"moneroFromMnemonicContainerQFrame")
        self.moneroFromMnemonicContainerQFrameVLayout = QVBoxLayout(self.moneroFromMnemonicContainerQFrame)
        self.moneroFromMnemonicContainerQFrameVLayout.setSpacing(5)
        self.moneroFromMnemonicContainerQFrameVLayout.setObjectName(u"moneroFromMnemonicContainerQFrameVLayout")
        self.moneroFromMnemonicContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicLabelContainerQFrame = QFrame(self.moneroFromMnemonicContainerQFrame)
        self.moneroFromMnemonicLabelContainerQFrame.setObjectName(u"moneroFromMnemonicLabelContainerQFrame")
        self.moneroFromMnemonicLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromMnemonicLabelContainerQFrame)
        self.moneroFromMnemonicLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromMnemonicLabelContainerQFrameHLayout.setObjectName(u"moneroFromMnemonicLabelContainerQFrameHLayout")
        self.moneroFromMnemonicLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicQLabel = QLabel(self.moneroFromMnemonicLabelContainerQFrame)
        self.moneroFromMnemonicQLabel.setObjectName(u"moneroFromMnemonicQLabel")

        self.moneroFromMnemonicLabelContainerQFrameHLayout.addWidget(self.moneroFromMnemonicQLabel)

        self.moneroFromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroFromMnemonicLabelContainerQFrameHLayout.addItem(self.moneroFromMnemonicLabelContainerQFrameHSpacer)


        self.moneroFromMnemonicContainerQFrameVLayout.addWidget(self.moneroFromMnemonicLabelContainerQFrame)

        self.moneroFromMnemonicLineEditContainerQFrame = QFrame(self.moneroFromMnemonicContainerQFrame)
        self.moneroFromMnemonicLineEditContainerQFrame.setObjectName(u"moneroFromMnemonicLineEditContainerQFrame")
        self.moneroFromMnemonicLineEditContainerQFrameHLayout = QHBoxLayout(self.moneroFromMnemonicLineEditContainerQFrame)
        self.moneroFromMnemonicLineEditContainerQFrameHLayout.setSpacing(15)
        self.moneroFromMnemonicLineEditContainerQFrameHLayout.setObjectName(u"moneroFromMnemonicLineEditContainerQFrameHLayout")
        self.moneroFromMnemonicLineEditContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicQLineEdit = QLineEdit(self.moneroFromMnemonicLineEditContainerQFrame)
        self.moneroFromMnemonicQLineEdit.setObjectName(u"moneroFromMnemonicQLineEdit")

        self.moneroFromMnemonicLineEditContainerQFrameHLayout.addWidget(self.moneroFromMnemonicQLineEdit)


        self.moneroFromMnemonicContainerQFrameVLayout.addWidget(self.moneroFromMnemonicLineEditContainerQFrame)


        self.moneroFromMnemonicQStackedWidgetVLayout.addWidget(self.moneroFromMnemonicContainerQFrame)

        self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame = QFrame(self.moneroFromMnemonicQStackedWidget)
        self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame.setObjectName(u"moneroFromMnemonicPaymentIDPassphraseContainerQFrame")
        self.moneroFromMnemonicPaymentIDPassphraseContainerQFrameHLayout = QHBoxLayout(self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame)
        self.moneroFromMnemonicPaymentIDPassphraseContainerQFrameHLayout.setSpacing(15)
        self.moneroFromMnemonicPaymentIDPassphraseContainerQFrameHLayout.setObjectName(u"moneroFromMnemonicPaymentIDPassphraseContainerQFrameHLayout")
        self.moneroFromMnemonicPaymentIDPassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicPaymentIDContainerQFrame = QFrame(self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame)
        self.moneroFromMnemonicPaymentIDContainerQFrame.setObjectName(u"moneroFromMnemonicPaymentIDContainerQFrame")
        self.moneroFromMnemonicPaymentIDContainerQFrame.setMinimumSize(QSize(150, 0))
        self.moneroFromMnemonicPaymentIDContainerQFrameVLayout = QVBoxLayout(self.moneroFromMnemonicPaymentIDContainerQFrame)
        self.moneroFromMnemonicPaymentIDContainerQFrameVLayout.setSpacing(5)
        self.moneroFromMnemonicPaymentIDContainerQFrameVLayout.setObjectName(u"moneroFromMnemonicPaymentIDContainerQFrameVLayout")
        self.moneroFromMnemonicPaymentIDContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicPaymentIDLabelContainerQFrame = QFrame(self.moneroFromMnemonicPaymentIDContainerQFrame)
        self.moneroFromMnemonicPaymentIDLabelContainerQFrame.setObjectName(u"moneroFromMnemonicPaymentIDLabelContainerQFrame")
        self.moneroFromMnemonicPaymentIDLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromMnemonicPaymentIDLabelContainerQFrame)
        self.moneroFromMnemonicPaymentIDLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromMnemonicPaymentIDLabelContainerQFrameHLayout.setObjectName(u"moneroFromMnemonicPaymentIDLabelContainerQFrameHLayout")
        self.moneroFromMnemonicPaymentIDLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicPaymentIDQLabel = QLabel(self.moneroFromMnemonicPaymentIDLabelContainerQFrame)
        self.moneroFromMnemonicPaymentIDQLabel.setObjectName(u"moneroFromMnemonicPaymentIDQLabel")

        self.moneroFromMnemonicPaymentIDLabelContainerQFrameHLayout.addWidget(self.moneroFromMnemonicPaymentIDQLabel)

        self.moneroFromMnemonicPaymentIDLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroFromMnemonicPaymentIDLabelContainerQFrameHLayout.addItem(self.moneroFromMnemonicPaymentIDLabelContainerQFrameHSpacer)


        self.moneroFromMnemonicPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromMnemonicPaymentIDLabelContainerQFrame)

        self.moneroFromMnemonicPaymentIDQLineEdit = QLineEdit(self.moneroFromMnemonicPaymentIDContainerQFrame)
        self.moneroFromMnemonicPaymentIDQLineEdit.setObjectName(u"moneroFromMnemonicPaymentIDQLineEdit")

        self.moneroFromMnemonicPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromMnemonicPaymentIDQLineEdit)


        self.moneroFromMnemonicPaymentIDPassphraseContainerQFrameHLayout.addWidget(self.moneroFromMnemonicPaymentIDContainerQFrame)


        self.moneroFromMnemonicQStackedWidgetVLayout.addWidget(self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame)

        self.moneroFromMnemonicQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.moneroFromMnemonicQStackedWidgetVLayout.addItem(self.moneroFromMnemonicQStackedWidgetVSpacer)

        self.moneroQStackedWidget.addWidget(self.moneroFromMnemonicQStackedWidget)
        self.moneroFromSeedQStackedWidget = QWidget()
        self.moneroFromSeedQStackedWidget.setObjectName(u"moneroFromSeedQStackedWidget")
        self.moneroFromSeedQStackedWidgetVLayout = QVBoxLayout(self.moneroFromSeedQStackedWidget)
        self.moneroFromSeedQStackedWidgetVLayout.setSpacing(15)
        self.moneroFromSeedQStackedWidgetVLayout.setObjectName(u"moneroFromSeedQStackedWidgetVLayout")
        self.moneroFromSeedQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedSpacerContainerQFrame = QFrame(self.moneroFromSeedQStackedWidget)
        self.moneroFromSeedSpacerContainerQFrame.setObjectName(u"moneroFromSeedSpacerContainerQFrame")
        self.moneroFromSeedSpacerContainerQFrame.setMinimumSize(QSize(400, 0))
        self.moneroFromSeedSpacerContainerQFrameVLayout = QVBoxLayout(self.moneroFromSeedSpacerContainerQFrame)
        self.moneroFromSeedSpacerContainerQFrameVLayout.setSpacing(5)
        self.moneroFromSeedSpacerContainerQFrameVLayout.setObjectName(u"moneroFromSeedSpacerContainerQFrameVLayout")
        self.moneroFromSeedSpacerContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedAndPaymentIDContainerQFrame = QFrame(self.moneroFromSeedSpacerContainerQFrame)
        self.moneroFromSeedAndPaymentIDContainerQFrame.setObjectName(u"moneroFromSeedAndPaymentIDContainerQFrame")
        self.moneroFromSeedAndPaymentIDContainerQFrameHLayout = QHBoxLayout(self.moneroFromSeedAndPaymentIDContainerQFrame)
        self.moneroFromSeedAndPaymentIDContainerQFrameHLayout.setSpacing(15)
        self.moneroFromSeedAndPaymentIDContainerQFrameHLayout.setObjectName(u"moneroFromSeedAndPaymentIDContainerQFrameHLayout")
        self.moneroFromSeedAndPaymentIDContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedContainerQFrame = QFrame(self.moneroFromSeedAndPaymentIDContainerQFrame)
        self.moneroFromSeedContainerQFrame.setObjectName(u"moneroFromSeedContainerQFrame")
        self.moneroFromSeedContainerQFrameVLayout = QVBoxLayout(self.moneroFromSeedContainerQFrame)
        self.moneroFromSeedContainerQFrameVLayout.setSpacing(5)
        self.moneroFromSeedContainerQFrameVLayout.setObjectName(u"moneroFromSeedContainerQFrameVLayout")
        self.moneroFromSeedContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedLabelContainerQFrame = QFrame(self.moneroFromSeedContainerQFrame)
        self.moneroFromSeedLabelContainerQFrame.setObjectName(u"moneroFromSeedLabelContainerQFrame")
        self.moneroFromSeedLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromSeedLabelContainerQFrame)
        self.moneroFromSeedLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromSeedLabelContainerQFrameHLayout.setObjectName(u"moneroFromSeedLabelContainerQFrameHLayout")
        self.moneroFromSeedLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedQLabel = QLabel(self.moneroFromSeedLabelContainerQFrame)
        self.moneroFromSeedQLabel.setObjectName(u"moneroFromSeedQLabel")

        self.moneroFromSeedLabelContainerQFrameHLayout.addWidget(self.moneroFromSeedQLabel)

        self.moneroFromSeedLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroFromSeedLabelContainerQFrameHLayout.addItem(self.moneroFromSeedLabelContainerQFrameHSpacer)


        self.moneroFromSeedContainerQFrameVLayout.addWidget(self.moneroFromSeedLabelContainerQFrame)

        self.moneroFromSeedQLineEdit = QLineEdit(self.moneroFromSeedContainerQFrame)
        self.moneroFromSeedQLineEdit.setObjectName(u"moneroFromSeedQLineEdit")

        self.moneroFromSeedContainerQFrameVLayout.addWidget(self.moneroFromSeedQLineEdit)


        self.moneroFromSeedAndPaymentIDContainerQFrameHLayout.addWidget(self.moneroFromSeedContainerQFrame)

        self.moneroFromSeedPaymentIDContainerQFrame = QFrame(self.moneroFromSeedAndPaymentIDContainerQFrame)
        self.moneroFromSeedPaymentIDContainerQFrame.setObjectName(u"moneroFromSeedPaymentIDContainerQFrame")
        self.moneroFromSeedPaymentIDContainerQFrame.setMinimumSize(QSize(150, 0))
        self.moneroFromSeedPaymentIDContainerQFrameVLayout = QVBoxLayout(self.moneroFromSeedPaymentIDContainerQFrame)
        self.moneroFromSeedPaymentIDContainerQFrameVLayout.setSpacing(5)
        self.moneroFromSeedPaymentIDContainerQFrameVLayout.setObjectName(u"moneroFromSeedPaymentIDContainerQFrameVLayout")
        self.moneroFromSeedPaymentIDContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedPaymentIDLabelContainerQFrame = QFrame(self.moneroFromSeedPaymentIDContainerQFrame)
        self.moneroFromSeedPaymentIDLabelContainerQFrame.setObjectName(u"moneroFromSeedPaymentIDLabelContainerQFrame")
        self.moneroFromSeedPaymentIDLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromSeedPaymentIDLabelContainerQFrame)
        self.moneroFromSeedPaymentIDLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromSeedPaymentIDLabelContainerQFrameHLayout.setObjectName(u"moneroFromSeedPaymentIDLabelContainerQFrameHLayout")
        self.moneroFromSeedPaymentIDLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedPaymentIDQLabel = QLabel(self.moneroFromSeedPaymentIDLabelContainerQFrame)
        self.moneroFromSeedPaymentIDQLabel.setObjectName(u"moneroFromSeedPaymentIDQLabel")

        self.moneroFromSeedPaymentIDLabelContainerQFrameHLayout.addWidget(self.moneroFromSeedPaymentIDQLabel)

        self.moneroFromSeedPaymentIDLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroFromSeedPaymentIDLabelContainerQFrameHLayout.addItem(self.moneroFromSeedPaymentIDLabelContainerQFrameHSpacer)


        self.moneroFromSeedPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromSeedPaymentIDLabelContainerQFrame)

        self.moneroFromSeedPaymentIDQLineEdit = QLineEdit(self.moneroFromSeedPaymentIDContainerQFrame)
        self.moneroFromSeedPaymentIDQLineEdit.setObjectName(u"moneroFromSeedPaymentIDQLineEdit")

        self.moneroFromSeedPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromSeedPaymentIDQLineEdit)


        self.moneroFromSeedAndPaymentIDContainerQFrameHLayout.addWidget(self.moneroFromSeedPaymentIDContainerQFrame)


        self.moneroFromSeedSpacerContainerQFrameVLayout.addWidget(self.moneroFromSeedAndPaymentIDContainerQFrame)

        self.moneroFromSeedSpacerContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.moneroFromSeedSpacerContainerQFrameVLayout.addItem(self.moneroFromSeedSpacerContainerQFrameVSpacer)


        self.moneroFromSeedQStackedWidgetVLayout.addWidget(self.moneroFromSeedSpacerContainerQFrame)

        self.moneroQStackedWidget.addWidget(self.moneroFromSeedQStackedWidget)
        self.moneroFromSpendPrivateKeyQStackedWidget = QWidget()
        self.moneroFromSpendPrivateKeyQStackedWidget.setObjectName(u"moneroFromSpendPrivateKeyQStackedWidget")
        self.moneroFromSpendPrivateKeyQStackedWidgetVLayout = QVBoxLayout(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.moneroFromSpendPrivateKeyQStackedWidgetVLayout.setSpacing(15)
        self.moneroFromSpendPrivateKeyQStackedWidgetVLayout.setObjectName(u"moneroFromSpendPrivateKeyQStackedWidgetVLayout")
        self.moneroFromSpendPrivateKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSpendPrivateKeyContainerQFrame = QFrame(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.moneroFromSpendPrivateKeyContainerQFrame.setObjectName(u"moneroFromSpendPrivateKeyContainerQFrame")
        self.moneroFromSpendPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.moneroFromSpendPrivateKeyContainerQFrame)
        self.moneroFromSpendPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.moneroFromSpendPrivateKeyContainerQFrameVLayout.setObjectName(u"moneroFromSpendPrivateKeyContainerQFrameVLayout")
        self.moneroFromSpendPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSpendPrivateKeyLabelContainerQFrame = QFrame(self.moneroFromSpendPrivateKeyContainerQFrame)
        self.moneroFromSpendPrivateKeyLabelContainerQFrame.setObjectName(u"moneroFromSpendPrivateKeyLabelContainerQFrame")
        self.moneroFromSpendPrivateKeyLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromSpendPrivateKeyLabelContainerQFrame)
        self.moneroFromSpendPrivateKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromSpendPrivateKeyLabelContainerQFrameHLayout.setObjectName(u"moneroFromSpendPrivateKeyLabelContainerQFrameHLayout")
        self.moneroFromSpendPrivateKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSpendPrivateKeyQLabel = QLabel(self.moneroFromSpendPrivateKeyLabelContainerQFrame)
        self.moneroFromSpendPrivateKeyQLabel.setObjectName(u"moneroFromSpendPrivateKeyQLabel")

        self.moneroFromSpendPrivateKeyLabelContainerQFrameHLayout.addWidget(self.moneroFromSpendPrivateKeyQLabel)

        self.moneroFromSpendPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroFromSpendPrivateKeyLabelContainerQFrameHLayout.addItem(self.moneroFromSpendPrivateKeyLabelContainerQFrameHSpacer)


        self.moneroFromSpendPrivateKeyContainerQFrameVLayout.addWidget(self.moneroFromSpendPrivateKeyLabelContainerQFrame)

        self.moneroFromSpendPrivateKeyQLineEdit = QLineEdit(self.moneroFromSpendPrivateKeyContainerQFrame)
        self.moneroFromSpendPrivateKeyQLineEdit.setObjectName(u"moneroFromSpendPrivateKeyQLineEdit")

        self.moneroFromSpendPrivateKeyContainerQFrameVLayout.addWidget(self.moneroFromSpendPrivateKeyQLineEdit)


        self.moneroFromSpendPrivateKeyQStackedWidgetVLayout.addWidget(self.moneroFromSpendPrivateKeyContainerQFrame)

        self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame = QFrame(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame.setObjectName(u"moneroFromSpendPrivateKeyPaymentIDContainerQFrame")
        self.moneroFromSpendPrivateKeyPaymentIDContainerQFrameVLayout = QVBoxLayout(self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame)
        self.moneroFromSpendPrivateKeyPaymentIDContainerQFrameVLayout.setSpacing(5)
        self.moneroFromSpendPrivateKeyPaymentIDContainerQFrameVLayout.setObjectName(u"moneroFromSpendPrivateKeyPaymentIDContainerQFrameVLayout")
        self.moneroFromSpendPrivateKeyPaymentIDContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSpendPrivateKeyPaymentIDQLabel = QLabel(self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame)
        self.moneroFromSpendPrivateKeyPaymentIDQLabel.setObjectName(u"moneroFromSpendPrivateKeyPaymentIDQLabel")

        self.moneroFromSpendPrivateKeyPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromSpendPrivateKeyPaymentIDQLabel)

        self.moneroFromSpendPrivateKeyPaymentIDQLineEdit = QLineEdit(self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame)
        self.moneroFromSpendPrivateKeyPaymentIDQLineEdit.setObjectName(u"moneroFromSpendPrivateKeyPaymentIDQLineEdit")

        self.moneroFromSpendPrivateKeyPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromSpendPrivateKeyPaymentIDQLineEdit)


        self.moneroFromSpendPrivateKeyQStackedWidgetVLayout.addWidget(self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame)

        self.moneroFromSpendPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.moneroFromSpendPrivateKeyQStackedWidgetVLayout.addItem(self.moneroFromSpendPrivateKeyQStackedWidgetVSpacer)

        self.moneroQStackedWidget.addWidget(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.moneroFromPrivateKeyQStackedWidget = QWidget()
        self.moneroFromPrivateKeyQStackedWidget.setObjectName(u"moneroFromPrivateKeyQStackedWidget")
        self.moneroFromPrivateKeyQStackedWidgetVLayout = QVBoxLayout(self.moneroFromPrivateKeyQStackedWidget)
        self.moneroFromPrivateKeyQStackedWidgetVLayout.setSpacing(15)
        self.moneroFromPrivateKeyQStackedWidgetVLayout.setObjectName(u"moneroFromPrivateKeyQStackedWidgetVLayout")
        self.moneroFromPrivateKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromPrivateKeyContainerQFrame = QFrame(self.moneroFromPrivateKeyQStackedWidget)
        self.moneroFromPrivateKeyContainerQFrame.setObjectName(u"moneroFromPrivateKeyContainerQFrame")
        self.moneroFromPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.moneroFromPrivateKeyContainerQFrame)
        self.moneroFromPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.moneroFromPrivateKeyContainerQFrameVLayout.setObjectName(u"moneroFromPrivateKeyContainerQFrameVLayout")
        self.moneroFromPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromPrivateKeyLabelContainerQFrame = QFrame(self.moneroFromPrivateKeyContainerQFrame)
        self.moneroFromPrivateKeyLabelContainerQFrame.setObjectName(u"moneroFromPrivateKeyLabelContainerQFrame")
        self.moneroFromPrivateKeyLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromPrivateKeyLabelContainerQFrame)
        self.moneroFromPrivateKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromPrivateKeyLabelContainerQFrameHLayout.setObjectName(u"moneroFromPrivateKeyLabelContainerQFrameHLayout")
        self.moneroFromPrivateKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromPrivateKeyQLabel = QLabel(self.moneroFromPrivateKeyLabelContainerQFrame)
        self.moneroFromPrivateKeyQLabel.setObjectName(u"moneroFromPrivateKeyQLabel")

        self.moneroFromPrivateKeyLabelContainerQFrameHLayout.addWidget(self.moneroFromPrivateKeyQLabel)

        self.moneroFromPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroFromPrivateKeyLabelContainerQFrameHLayout.addItem(self.moneroFromPrivateKeyLabelContainerQFrameHSpacer)


        self.moneroFromPrivateKeyContainerQFrameVLayout.addWidget(self.moneroFromPrivateKeyLabelContainerQFrame)

        self.moneroFromPrivateKeyQLineEdit = QLineEdit(self.moneroFromPrivateKeyContainerQFrame)
        self.moneroFromPrivateKeyQLineEdit.setObjectName(u"moneroFromPrivateKeyQLineEdit")

        self.moneroFromPrivateKeyContainerQFrameVLayout.addWidget(self.moneroFromPrivateKeyQLineEdit)


        self.moneroFromPrivateKeyQStackedWidgetVLayout.addWidget(self.moneroFromPrivateKeyContainerQFrame)

        self.moneroFromPrivateKeyPaymentIDContainerQFrame = QFrame(self.moneroFromPrivateKeyQStackedWidget)
        self.moneroFromPrivateKeyPaymentIDContainerQFrame.setObjectName(u"moneroFromPrivateKeyPaymentIDContainerQFrame")
        self.moneroFromPrivateKeyPaymentIDContainerQFrameVLayout = QVBoxLayout(self.moneroFromPrivateKeyPaymentIDContainerQFrame)
        self.moneroFromPrivateKeyPaymentIDContainerQFrameVLayout.setSpacing(5)
        self.moneroFromPrivateKeyPaymentIDContainerQFrameVLayout.setObjectName(u"moneroFromPrivateKeyPaymentIDContainerQFrameVLayout")
        self.moneroFromPrivateKeyPaymentIDContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromPrivateKeyPaymentIDQLabel = QLabel(self.moneroFromPrivateKeyPaymentIDContainerQFrame)
        self.moneroFromPrivateKeyPaymentIDQLabel.setObjectName(u"moneroFromPrivateKeyPaymentIDQLabel")

        self.moneroFromPrivateKeyPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromPrivateKeyPaymentIDQLabel)

        self.moneroFromPrivateKeyPaymentIDQLineEdit = QLineEdit(self.moneroFromPrivateKeyPaymentIDContainerQFrame)
        self.moneroFromPrivateKeyPaymentIDQLineEdit.setObjectName(u"moneroFromPrivateKeyPaymentIDQLineEdit")

        self.moneroFromPrivateKeyPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromPrivateKeyPaymentIDQLineEdit)


        self.moneroFromPrivateKeyQStackedWidgetVLayout.addWidget(self.moneroFromPrivateKeyPaymentIDContainerQFrame)

        self.moneroFromPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.moneroFromPrivateKeyQStackedWidgetVLayout.addItem(self.moneroFromPrivateKeyQStackedWidgetVSpacer)

        self.moneroQStackedWidget.addWidget(self.moneroFromPrivateKeyQStackedWidget)
        self.moneroFromWatchOnlyQStackedWidget = QWidget()
        self.moneroFromWatchOnlyQStackedWidget.setObjectName(u"moneroFromWatchOnlyQStackedWidget")
        self.moneroFromWatchOnlyQStackedWidgetVLayout = QVBoxLayout(self.moneroFromWatchOnlyQStackedWidget)
        self.moneroFromWatchOnlyQStackedWidgetVLayout.setSpacing(15)
        self.moneroFromWatchOnlyQStackedWidgetVLayout.setObjectName(u"moneroFromWatchOnlyQStackedWidgetVLayout")
        self.moneroFromWatchOnlyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame = QFrame(self.moneroFromWatchOnlyQStackedWidget)
        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame.setObjectName(u"moneroFromWatchOnlyViewPrivateKeyContainerQFrame")
        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame)
        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrameVLayout.setObjectName(u"moneroFromWatchOnlyViewPrivateKeyContainerQFrameVLayout")
        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame = QFrame(self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame)
        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame.setObjectName(u"moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame")
        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame)
        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHLayout.setObjectName(u"moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHLayout")
        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlyViewPrivateKeyQLabel = QLabel(self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame)
        self.moneroFromWatchOnlyViewPrivateKeyQLabel.setObjectName(u"moneroFromWatchOnlyViewPrivateKeyQLabel")

        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHLayout.addWidget(self.moneroFromWatchOnlyViewPrivateKeyQLabel)

        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHLayout.addItem(self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHSpacer)


        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrameVLayout.addWidget(self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame)

        self.moneroFromWatchOnlyViewPrivateKeyQLIneEdit = QLineEdit(self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame)
        self.moneroFromWatchOnlyViewPrivateKeyQLIneEdit.setObjectName(u"moneroFromWatchOnlyViewPrivateKeyQLIneEdit")

        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrameVLayout.addWidget(self.moneroFromWatchOnlyViewPrivateKeyQLIneEdit)

        self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrame = QFrame(self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame)
        self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrame.setObjectName(u"moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrame")
        self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrameHLayout = QHBoxLayout(self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrame)
        self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrameHLayout.setSpacing(15)
        self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrameHLayout.setObjectName(u"moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrameHLayout")
        self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlySpendPublicKeyContainerQFrame = QFrame(self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrame)
        self.moneroFromWatchOnlySpendPublicKeyContainerQFrame.setObjectName(u"moneroFromWatchOnlySpendPublicKeyContainerQFrame")
        self.moneroFromWatchOnlySpendPublicKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.moneroFromWatchOnlySpendPublicKeyContainerQFrameVLayout = QVBoxLayout(self.moneroFromWatchOnlySpendPublicKeyContainerQFrame)
        self.moneroFromWatchOnlySpendPublicKeyContainerQFrameVLayout.setSpacing(5)
        self.moneroFromWatchOnlySpendPublicKeyContainerQFrameVLayout.setObjectName(u"moneroFromWatchOnlySpendPublicKeyContainerQFrameVLayout")
        self.moneroFromWatchOnlySpendPublicKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame = QFrame(self.moneroFromWatchOnlySpendPublicKeyContainerQFrame)
        self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame.setObjectName(u"moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame")
        self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrameHLayout = QHBoxLayout(self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame)
        self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrameHLayout.setObjectName(u"moneroFromWatchOnlySpendPublicKeyLabelContainerQFrameHLayout")
        self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlySpendPublicKeyQLabel = QLabel(self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame)
        self.moneroFromWatchOnlySpendPublicKeyQLabel.setObjectName(u"moneroFromWatchOnlySpendPublicKeyQLabel")

        self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrameHLayout.addWidget(self.moneroFromWatchOnlySpendPublicKeyQLabel)


        self.moneroFromWatchOnlySpendPublicKeyContainerQFrameVLayout.addWidget(self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame)

        self.moneroFromWatchOnlySpendPublicKeyQLineEdit = QLineEdit(self.moneroFromWatchOnlySpendPublicKeyContainerQFrame)
        self.moneroFromWatchOnlySpendPublicKeyQLineEdit.setObjectName(u"moneroFromWatchOnlySpendPublicKeyQLineEdit")

        self.moneroFromWatchOnlySpendPublicKeyContainerQFrameVLayout.addWidget(self.moneroFromWatchOnlySpendPublicKeyQLineEdit)


        self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrameHLayout.addWidget(self.moneroFromWatchOnlySpendPublicKeyContainerQFrame)

        self.moneroFromWatchOnlyPaymentIDContainerQFrame = QFrame(self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrame)
        self.moneroFromWatchOnlyPaymentIDContainerQFrame.setObjectName(u"moneroFromWatchOnlyPaymentIDContainerQFrame")
        self.moneroFromWatchOnlyPaymentIDContainerQFrameVLayout = QVBoxLayout(self.moneroFromWatchOnlyPaymentIDContainerQFrame)
        self.moneroFromWatchOnlyPaymentIDContainerQFrameVLayout.setSpacing(5)
        self.moneroFromWatchOnlyPaymentIDContainerQFrameVLayout.setObjectName(u"moneroFromWatchOnlyPaymentIDContainerQFrameVLayout")
        self.moneroFromWatchOnlyPaymentIDContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlyPaymentIDQLabel = QLabel(self.moneroFromWatchOnlyPaymentIDContainerQFrame)
        self.moneroFromWatchOnlyPaymentIDQLabel.setObjectName(u"moneroFromWatchOnlyPaymentIDQLabel")

        self.moneroFromWatchOnlyPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromWatchOnlyPaymentIDQLabel)

        self.moneroFromWatchOnlyPaymentIDQLineEdit = QLineEdit(self.moneroFromWatchOnlyPaymentIDContainerQFrame)
        self.moneroFromWatchOnlyPaymentIDQLineEdit.setObjectName(u"moneroFromWatchOnlyPaymentIDQLineEdit")

        self.moneroFromWatchOnlyPaymentIDContainerQFrameVLayout.addWidget(self.moneroFromWatchOnlyPaymentIDQLineEdit)


        self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrameHLayout.addWidget(self.moneroFromWatchOnlyPaymentIDContainerQFrame)


        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrameVLayout.addWidget(self.moneroFromWatchOnlySpendKeyAndPaymentIDContainerQFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrameVLayout.addItem(self.verticalSpacer_2)


        self.moneroFromWatchOnlyQStackedWidgetVLayout.addWidget(self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame)

        self.moneroQStackedWidget.addWidget(self.moneroFromWatchOnlyQStackedWidget)

        self.moneroPageQWidgetVLayout.addWidget(self.moneroQStackedWidget)

        self.hdQStackedWidget.addWidget(self.moneroPageQWidget)

        self.dumpsStackQGroupBoxVLayout.addWidget(self.hdQStackedWidget)


        self.dumpsPageQStackedWidgetVLayout.addWidget(self.dumpsStackQGroupBox)

        self.dumpsDerivationContainerQFrame = QFrame(self.dumpsPageQStackedWidget)
        self.dumpsDerivationContainerQFrame.setObjectName(u"dumpsDerivationContainerQFrame")
        self.dumpsDerivationContainerQFrameVLayout = QVBoxLayout(self.dumpsDerivationContainerQFrame)
        self.dumpsDerivationContainerQFrameVLayout.setSpacing(15)
        self.dumpsDerivationContainerQFrameVLayout.setObjectName(u"dumpsDerivationContainerQFrameVLayout")
        self.dumpsDerivationContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.derivationQGroupBox = QGroupBox(self.dumpsDerivationContainerQFrame)
        self.derivationQGroupBox.setObjectName(u"derivationQGroupBox")
        self.derivationQGroupBoxVLayout = QVBoxLayout(self.derivationQGroupBox)
        self.derivationQGroupBoxVLayout.setSpacing(5)
        self.derivationQGroupBoxVLayout.setObjectName(u"derivationQGroupBoxVLayout")
        self.derivationQGroupBoxVLayout.setContentsMargins(10, 15, 10, 10)
        self.derivationTabButtonsContainerQFrame = QFrame(self.derivationQGroupBox)
        self.derivationTabButtonsContainerQFrame.setObjectName(u"derivationTabButtonsContainerQFrame")
        self.derivationTabButtonsContainerQFrameHLayout = QHBoxLayout(self.derivationTabButtonsContainerQFrame)
        self.derivationTabButtonsContainerQFrameHLayout.setSpacing(0)
        self.derivationTabButtonsContainerQFrameHLayout.setObjectName(u"derivationTabButtonsContainerQFrameHLayout")
        self.derivationTabButtonsContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.customTabQPushButton = QPushButton(self.derivationTabButtonsContainerQFrame)
        self.customTabQPushButton.setObjectName(u"customTabQPushButton")

        self.derivationTabButtonsContainerQFrameHLayout.addWidget(self.customTabQPushButton)

        self.bip44TabQPushButton = QPushButton(self.derivationTabButtonsContainerQFrame)
        self.bip44TabQPushButton.setObjectName(u"bip44TabQPushButton")

        self.derivationTabButtonsContainerQFrameHLayout.addWidget(self.bip44TabQPushButton)

        self.bip49TabQPushButton = QPushButton(self.derivationTabButtonsContainerQFrame)
        self.bip49TabQPushButton.setObjectName(u"bip49TabQPushButton")

        self.derivationTabButtonsContainerQFrameHLayout.addWidget(self.bip49TabQPushButton)

        self.bip84TabQPushButton = QPushButton(self.derivationTabButtonsContainerQFrame)
        self.bip84TabQPushButton.setObjectName(u"bip84TabQPushButton")

        self.derivationTabButtonsContainerQFrameHLayout.addWidget(self.bip84TabQPushButton)

        self.bip86TabQPushButton = QPushButton(self.derivationTabButtonsContainerQFrame)
        self.bip86TabQPushButton.setObjectName(u"bip86TabQPushButton")

        self.derivationTabButtonsContainerQFrameHLayout.addWidget(self.bip86TabQPushButton)

        self.bip141TabQPushButton = QPushButton(self.derivationTabButtonsContainerQFrame)
        self.bip141TabQPushButton.setObjectName(u"bip141TabQPushButton")

        self.derivationTabButtonsContainerQFrameHLayout.addWidget(self.bip141TabQPushButton)

        self.cip1852TabQPushButton = QPushButton(self.derivationTabButtonsContainerQFrame)
        self.cip1852TabQPushButton.setObjectName(u"cip1852TabQPushButton")

        self.derivationTabButtonsContainerQFrameHLayout.addWidget(self.cip1852TabQPushButton)

        self.electrumTabQPushButton = QPushButton(self.derivationTabButtonsContainerQFrame)
        self.electrumTabQPushButton.setObjectName(u"electrumTabQPushButton")

        self.derivationTabButtonsContainerQFrameHLayout.addWidget(self.electrumTabQPushButton)

        self.moneroTabQPushButton = QPushButton(self.derivationTabButtonsContainerQFrame)
        self.moneroTabQPushButton.setObjectName(u"moneroTabQPushButton")

        self.derivationTabButtonsContainerQFrameHLayout.addWidget(self.moneroTabQPushButton)

        self.derivationTabButtonsContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.derivationTabButtonsContainerQFrameHLayout.addItem(self.derivationTabButtonsContainerQFrameHSpacer)


        self.derivationQGroupBoxVLayout.addWidget(self.derivationTabButtonsContainerQFrame)

        self.derivationsQStackedWidget = QStackedWidget(self.derivationQGroupBox)
        self.derivationsQStackedWidget.setObjectName(u"derivationsQStackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.derivationsQStackedWidget.sizePolicy().hasHeightForWidth())
        self.derivationsQStackedWidget.setSizePolicy(sizePolicy2)
        self.customQStackedWidgetPage = QWidget()
        self.customQStackedWidgetPage.setObjectName(u"customQStackedWidgetPage")
        self.customQStackedWidgetPageHLayout = QHBoxLayout(self.customQStackedWidgetPage)
        self.customQStackedWidgetPageHLayout.setSpacing(15)
        self.customQStackedWidgetPageHLayout.setObjectName(u"customQStackedWidgetPageHLayout")
        self.customQStackedWidgetPageHLayout.setContentsMargins(0, 5, 0, 0)
        self.customPathQFrame = QFrame(self.customQStackedWidgetPage)
        self.customPathQFrame.setObjectName(u"customPathQFrame")
        self.customPathQFrameVLayout = QVBoxLayout(self.customPathQFrame)
        self.customPathQFrameVLayout.setSpacing(5)
        self.customPathQFrameVLayout.setObjectName(u"customPathQFrameVLayout")
        self.customPathQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.customPathLabelQFrame = QFrame(self.customPathQFrame)
        self.customPathLabelQFrame.setObjectName(u"customPathLabelQFrame")
        self.customPathLabelQFrameHLayout = QHBoxLayout(self.customPathLabelQFrame)
        self.customPathLabelQFrameHLayout.setSpacing(15)
        self.customPathLabelQFrameHLayout.setObjectName(u"customPathLabelQFrameHLayout")
        self.customPathLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.customPathQLabel = QLabel(self.customPathLabelQFrame)
        self.customPathQLabel.setObjectName(u"customPathQLabel")

        self.customPathLabelQFrameHLayout.addWidget(self.customPathQLabel)

        self.customPathLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.customPathLabelQFrameHLayout.addItem(self.customPathLabelHSpacer)


        self.customPathQFrameVLayout.addWidget(self.customPathLabelQFrame)

        self.customPathQLineEdit = QLineEdit(self.customPathQFrame)
        self.customPathQLineEdit.setObjectName(u"customPathQLineEdit")

        self.customPathQFrameVLayout.addWidget(self.customPathQLineEdit)


        self.customQStackedWidgetPageHLayout.addWidget(self.customPathQFrame)

        self.customClientQFrame = QFrame(self.customQStackedWidgetPage)
        self.customClientQFrame.setObjectName(u"customClientQFrame")
        self.customClientQFrame.setMinimumSize(QSize(175, 0))
        self.customClientQFrame.setMaximumSize(QSize(300, 16777215))
        self.customClientQFrameVLayout = QVBoxLayout(self.customClientQFrame)
        self.customClientQFrameVLayout.setSpacing(5)
        self.customClientQFrameVLayout.setObjectName(u"customClientQFrameVLayout")
        self.customClientQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.customClientLabelQFrame = QFrame(self.customClientQFrame)
        self.customClientLabelQFrame.setObjectName(u"customClientLabelQFrame")
        self.customClientLabelQFrameHLayout = QHBoxLayout(self.customClientLabelQFrame)
        self.customClientLabelQFrameHLayout.setSpacing(15)
        self.customClientLabelQFrameHLayout.setObjectName(u"customClientLabelQFrameHLayout")
        self.customClientLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.customClientQLabel = QLabel(self.customClientLabelQFrame)
        self.customClientQLabel.setObjectName(u"customClientQLabel")

        self.customClientLabelQFrameHLayout.addWidget(self.customClientQLabel)

        self.customClientLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.customClientLabelQFrameHLayout.addItem(self.customClientLabelHSpacer)


        self.customClientQFrameVLayout.addWidget(self.customClientLabelQFrame)

        self.customClientQComboBox = QComboBox(self.customClientQFrame)
        self.customClientQComboBox.addItem("")
        self.customClientQComboBox.addItem("")
        self.customClientQComboBox.addItem("")
        self.customClientQComboBox.addItem("")
        self.customClientQComboBox.addItem("")
        self.customClientQComboBox.setObjectName(u"customClientQComboBox")

        self.customClientQFrameVLayout.addWidget(self.customClientQComboBox)


        self.customQStackedWidgetPageHLayout.addWidget(self.customClientQFrame)

        self.derivationsQStackedWidget.addWidget(self.customQStackedWidgetPage)
        self.bip44QStackedWidgetPage = QWidget()
        self.bip44QStackedWidgetPage.setObjectName(u"bip44QStackedWidgetPage")
        self.bip44QStackedWidgetPageHLayout = QHBoxLayout(self.bip44QStackedWidgetPage)
        self.bip44QStackedWidgetPageHLayout.setSpacing(15)
        self.bip44QStackedWidgetPageHLayout.setObjectName(u"bip44QStackedWidgetPageHLayout")
        self.bip44QStackedWidgetPageHLayout.setContentsMargins(0, 5, 0, 0)
        self.bip44PurposeQFrame = QFrame(self.bip44QStackedWidgetPage)
        self.bip44PurposeQFrame.setObjectName(u"bip44PurposeQFrame")
        self.bip44PurposeQFrameVLayout = QVBoxLayout(self.bip44PurposeQFrame)
        self.bip44PurposeQFrameVLayout.setSpacing(5)
        self.bip44PurposeQFrameVLayout.setObjectName(u"bip44PurposeQFrameVLayout")
        self.bip44PurposeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip44PurposeLabelQFrame = QFrame(self.bip44PurposeQFrame)
        self.bip44PurposeLabelQFrame.setObjectName(u"bip44PurposeLabelQFrame")
        self.bip44PurposeLabelQFrameHLayout = QHBoxLayout(self.bip44PurposeLabelQFrame)
        self.bip44PurposeLabelQFrameHLayout.setSpacing(15)
        self.bip44PurposeLabelQFrameHLayout.setObjectName(u"bip44PurposeLabelQFrameHLayout")
        self.bip44PurposeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip44PurposeQLabel = QLabel(self.bip44PurposeLabelQFrame)
        self.bip44PurposeQLabel.setObjectName(u"bip44PurposeQLabel")

        self.bip44PurposeLabelQFrameHLayout.addWidget(self.bip44PurposeQLabel)

        self.bip44PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip44PurposeLabelQFrameHLayout.addItem(self.bip44PurposeLabelHSpacer)


        self.bip44PurposeQFrameVLayout.addWidget(self.bip44PurposeLabelQFrame)

        self.bip44PurposeQLineEdit = QLineEdit(self.bip44PurposeQFrame)
        self.bip44PurposeQLineEdit.setObjectName(u"bip44PurposeQLineEdit")
        self.bip44PurposeQLineEdit.setEnabled(False)

        self.bip44PurposeQFrameVLayout.addWidget(self.bip44PurposeQLineEdit)


        self.bip44QStackedWidgetPageHLayout.addWidget(self.bip44PurposeQFrame)

        self.bip44CoinTypeQFrame = QFrame(self.bip44QStackedWidgetPage)
        self.bip44CoinTypeQFrame.setObjectName(u"bip44CoinTypeQFrame")
        self.bip44CoinTypeQFrameVLayout = QVBoxLayout(self.bip44CoinTypeQFrame)
        self.bip44CoinTypeQFrameVLayout.setSpacing(5)
        self.bip44CoinTypeQFrameVLayout.setObjectName(u"bip44CoinTypeQFrameVLayout")
        self.bip44CoinTypeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip44CoinTypeLabelQFrame = QFrame(self.bip44CoinTypeQFrame)
        self.bip44CoinTypeLabelQFrame.setObjectName(u"bip44CoinTypeLabelQFrame")
        self.bip44CoinTypeLabelQFrameHLayout = QHBoxLayout(self.bip44CoinTypeLabelQFrame)
        self.bip44CoinTypeLabelQFrameHLayout.setSpacing(15)
        self.bip44CoinTypeLabelQFrameHLayout.setObjectName(u"bip44CoinTypeLabelQFrameHLayout")
        self.bip44CoinTypeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip44CoinTypeQLabel = QLabel(self.bip44CoinTypeLabelQFrame)
        self.bip44CoinTypeQLabel.setObjectName(u"bip44CoinTypeQLabel")

        self.bip44CoinTypeLabelQFrameHLayout.addWidget(self.bip44CoinTypeQLabel)

        self.bip44CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip44CoinTypeLabelQFrameHLayout.addItem(self.bip44CoinTypeLabelHSpacer)


        self.bip44CoinTypeQFrameVLayout.addWidget(self.bip44CoinTypeLabelQFrame)

        self.bip44CoinTypeQLineEdit = QLineEdit(self.bip44CoinTypeQFrame)
        self.bip44CoinTypeQLineEdit.setObjectName(u"bip44CoinTypeQLineEdit")
        self.bip44CoinTypeQLineEdit.setEnabled(False)

        self.bip44CoinTypeQFrameVLayout.addWidget(self.bip44CoinTypeQLineEdit)


        self.bip44QStackedWidgetPageHLayout.addWidget(self.bip44CoinTypeQFrame)

        self.bip44AccountQFrame = QFrame(self.bip44QStackedWidgetPage)
        self.bip44AccountQFrame.setObjectName(u"bip44AccountQFrame")
        self.bip44AccountQFrameVLayout = QVBoxLayout(self.bip44AccountQFrame)
        self.bip44AccountQFrameVLayout.setSpacing(5)
        self.bip44AccountQFrameVLayout.setObjectName(u"bip44AccountQFrameVLayout")
        self.bip44AccountQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip44AccountLabelQFrame = QFrame(self.bip44AccountQFrame)
        self.bip44AccountLabelQFrame.setObjectName(u"bip44AccountLabelQFrame")
        self.bip44AccountLabelQFrameHLayout = QHBoxLayout(self.bip44AccountLabelQFrame)
        self.bip44AccountLabelQFrameHLayout.setSpacing(15)
        self.bip44AccountLabelQFrameHLayout.setObjectName(u"bip44AccountLabelQFrameHLayout")
        self.bip44AccountLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip44AccountQLabel = QLabel(self.bip44AccountLabelQFrame)
        self.bip44AccountQLabel.setObjectName(u"bip44AccountQLabel")

        self.bip44AccountLabelQFrameHLayout.addWidget(self.bip44AccountQLabel)

        self.bip44AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip44AccountLabelQFrameHLayout.addItem(self.bip44AccountLabelHSpacer)


        self.bip44AccountQFrameVLayout.addWidget(self.bip44AccountLabelQFrame)

        self.bip44AccountQLineEdit = QLineEdit(self.bip44AccountQFrame)
        self.bip44AccountQLineEdit.setObjectName(u"bip44AccountQLineEdit")

        self.bip44AccountQFrameVLayout.addWidget(self.bip44AccountQLineEdit)


        self.bip44QStackedWidgetPageHLayout.addWidget(self.bip44AccountQFrame)

        self.bip44ChangeQFrame = QFrame(self.bip44QStackedWidgetPage)
        self.bip44ChangeQFrame.setObjectName(u"bip44ChangeQFrame")
        self.bip44ChangeQFrameVLayout = QVBoxLayout(self.bip44ChangeQFrame)
        self.bip44ChangeQFrameVLayout.setSpacing(5)
        self.bip44ChangeQFrameVLayout.setObjectName(u"bip44ChangeQFrameVLayout")
        self.bip44ChangeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip44ChangeLabelQFrame = QFrame(self.bip44ChangeQFrame)
        self.bip44ChangeLabelQFrame.setObjectName(u"bip44ChangeLabelQFrame")
        self.bip44ChangeLabelQFrameHLayout = QHBoxLayout(self.bip44ChangeLabelQFrame)
        self.bip44ChangeLabelQFrameHLayout.setSpacing(15)
        self.bip44ChangeLabelQFrameHLayout.setObjectName(u"bip44ChangeLabelQFrameHLayout")
        self.bip44ChangeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip44ChangeQLabel = QLabel(self.bip44ChangeLabelQFrame)
        self.bip44ChangeQLabel.setObjectName(u"bip44ChangeQLabel")

        self.bip44ChangeLabelQFrameHLayout.addWidget(self.bip44ChangeQLabel)

        self.bip44ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip44ChangeLabelQFrameHLayout.addItem(self.bip44ChangeLabelHSpacer)


        self.bip44ChangeQFrameVLayout.addWidget(self.bip44ChangeLabelQFrame)

        self.bip44ChangeQComboBox = QComboBox(self.bip44ChangeQFrame)
        self.bip44ChangeQComboBox.addItem("")
        self.bip44ChangeQComboBox.addItem("")
        self.bip44ChangeQComboBox.setObjectName(u"bip44ChangeQComboBox")

        self.bip44ChangeQFrameVLayout.addWidget(self.bip44ChangeQComboBox)


        self.bip44QStackedWidgetPageHLayout.addWidget(self.bip44ChangeQFrame)

        self.bip44AddressQFrame = QFrame(self.bip44QStackedWidgetPage)
        self.bip44AddressQFrame.setObjectName(u"bip44AddressQFrame")
        self.bip44AddressQFrameVLayout = QVBoxLayout(self.bip44AddressQFrame)
        self.bip44AddressQFrameVLayout.setSpacing(5)
        self.bip44AddressQFrameVLayout.setObjectName(u"bip44AddressQFrameVLayout")
        self.bip44AddressQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip44AddressLabelQFrame = QFrame(self.bip44AddressQFrame)
        self.bip44AddressLabelQFrame.setObjectName(u"bip44AddressLabelQFrame")
        self.bip44AddressLabelQFrameHLayout = QHBoxLayout(self.bip44AddressLabelQFrame)
        self.bip44AddressLabelQFrameHLayout.setSpacing(15)
        self.bip44AddressLabelQFrameHLayout.setObjectName(u"bip44AddressLabelQFrameHLayout")
        self.bip44AddressLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip44AddressQLabel = QLabel(self.bip44AddressLabelQFrame)
        self.bip44AddressQLabel.setObjectName(u"bip44AddressQLabel")

        self.bip44AddressLabelQFrameHLayout.addWidget(self.bip44AddressQLabel)

        self.bip44AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip44AddressLabelQFrameHLayout.addItem(self.bip44AddressLabelHSpacer)


        self.bip44AddressQFrameVLayout.addWidget(self.bip44AddressLabelQFrame)

        self.bip44AddressQLineEdit = QLineEdit(self.bip44AddressQFrame)
        self.bip44AddressQLineEdit.setObjectName(u"bip44AddressQLineEdit")

        self.bip44AddressQFrameVLayout.addWidget(self.bip44AddressQLineEdit)


        self.bip44QStackedWidgetPageHLayout.addWidget(self.bip44AddressQFrame)

        self.derivationsQStackedWidget.addWidget(self.bip44QStackedWidgetPage)
        self.bip49QStackedWidgetPage = QWidget()
        self.bip49QStackedWidgetPage.setObjectName(u"bip49QStackedWidgetPage")
        self.bip49QStackedWidgetPageHLayout = QHBoxLayout(self.bip49QStackedWidgetPage)
        self.bip49QStackedWidgetPageHLayout.setSpacing(15)
        self.bip49QStackedWidgetPageHLayout.setObjectName(u"bip49QStackedWidgetPageHLayout")
        self.bip49QStackedWidgetPageHLayout.setContentsMargins(0, 5, 0, 0)
        self.bip49PurposeQFrame = QFrame(self.bip49QStackedWidgetPage)
        self.bip49PurposeQFrame.setObjectName(u"bip49PurposeQFrame")
        self.bip49PurposeQFrameVLayout = QVBoxLayout(self.bip49PurposeQFrame)
        self.bip49PurposeQFrameVLayout.setSpacing(5)
        self.bip49PurposeQFrameVLayout.setObjectName(u"bip49PurposeQFrameVLayout")
        self.bip49PurposeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip49PurposeLabelQFrame = QFrame(self.bip49PurposeQFrame)
        self.bip49PurposeLabelQFrame.setObjectName(u"bip49PurposeLabelQFrame")
        self.bip49PurposeLabelQFrameHLayout = QHBoxLayout(self.bip49PurposeLabelQFrame)
        self.bip49PurposeLabelQFrameHLayout.setSpacing(15)
        self.bip49PurposeLabelQFrameHLayout.setObjectName(u"bip49PurposeLabelQFrameHLayout")
        self.bip49PurposeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip49PurposeQLabel = QLabel(self.bip49PurposeLabelQFrame)
        self.bip49PurposeQLabel.setObjectName(u"bip49PurposeQLabel")

        self.bip49PurposeLabelQFrameHLayout.addWidget(self.bip49PurposeQLabel)

        self.bip49PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip49PurposeLabelQFrameHLayout.addItem(self.bip49PurposeLabelHSpacer)


        self.bip49PurposeQFrameVLayout.addWidget(self.bip49PurposeLabelQFrame)

        self.bip49PurposeQLineEdit = QLineEdit(self.bip49PurposeQFrame)
        self.bip49PurposeQLineEdit.setObjectName(u"bip49PurposeQLineEdit")
        self.bip49PurposeQLineEdit.setEnabled(False)

        self.bip49PurposeQFrameVLayout.addWidget(self.bip49PurposeQLineEdit)


        self.bip49QStackedWidgetPageHLayout.addWidget(self.bip49PurposeQFrame)

        self.bip49CoinTypeQFrame = QFrame(self.bip49QStackedWidgetPage)
        self.bip49CoinTypeQFrame.setObjectName(u"bip49CoinTypeQFrame")
        self.bip49CoinTypeQFrameVLayout = QVBoxLayout(self.bip49CoinTypeQFrame)
        self.bip49CoinTypeQFrameVLayout.setSpacing(5)
        self.bip49CoinTypeQFrameVLayout.setObjectName(u"bip49CoinTypeQFrameVLayout")
        self.bip49CoinTypeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip49CoinTypeLabelQFrame = QFrame(self.bip49CoinTypeQFrame)
        self.bip49CoinTypeLabelQFrame.setObjectName(u"bip49CoinTypeLabelQFrame")
        self.bip49CoinTypeLabelQFrameHLayout = QHBoxLayout(self.bip49CoinTypeLabelQFrame)
        self.bip49CoinTypeLabelQFrameHLayout.setSpacing(15)
        self.bip49CoinTypeLabelQFrameHLayout.setObjectName(u"bip49CoinTypeLabelQFrameHLayout")
        self.bip49CoinTypeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip49CoinTypeQLabel = QLabel(self.bip49CoinTypeLabelQFrame)
        self.bip49CoinTypeQLabel.setObjectName(u"bip49CoinTypeQLabel")

        self.bip49CoinTypeLabelQFrameHLayout.addWidget(self.bip49CoinTypeQLabel)

        self.bip49CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip49CoinTypeLabelQFrameHLayout.addItem(self.bip49CoinTypeLabelHSpacer)


        self.bip49CoinTypeQFrameVLayout.addWidget(self.bip49CoinTypeLabelQFrame)

        self.bip49CoinTypeQLineEdit = QLineEdit(self.bip49CoinTypeQFrame)
        self.bip49CoinTypeQLineEdit.setObjectName(u"bip49CoinTypeQLineEdit")
        self.bip49CoinTypeQLineEdit.setEnabled(False)

        self.bip49CoinTypeQFrameVLayout.addWidget(self.bip49CoinTypeQLineEdit)


        self.bip49QStackedWidgetPageHLayout.addWidget(self.bip49CoinTypeQFrame)

        self.bip49AccountQFrame = QFrame(self.bip49QStackedWidgetPage)
        self.bip49AccountQFrame.setObjectName(u"bip49AccountQFrame")
        self.bip49AccountQFrameVLayout = QVBoxLayout(self.bip49AccountQFrame)
        self.bip49AccountQFrameVLayout.setSpacing(5)
        self.bip49AccountQFrameVLayout.setObjectName(u"bip49AccountQFrameVLayout")
        self.bip49AccountQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip49AccountLabelQFrame = QFrame(self.bip49AccountQFrame)
        self.bip49AccountLabelQFrame.setObjectName(u"bip49AccountLabelQFrame")
        self.bip49AccountLabelQFrameHLayout = QHBoxLayout(self.bip49AccountLabelQFrame)
        self.bip49AccountLabelQFrameHLayout.setSpacing(15)
        self.bip49AccountLabelQFrameHLayout.setObjectName(u"bip49AccountLabelQFrameHLayout")
        self.bip49AccountLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip49AccountQLabel = QLabel(self.bip49AccountLabelQFrame)
        self.bip49AccountQLabel.setObjectName(u"bip49AccountQLabel")

        self.bip49AccountLabelQFrameHLayout.addWidget(self.bip49AccountQLabel)

        self.bip49AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip49AccountLabelQFrameHLayout.addItem(self.bip49AccountLabelHSpacer)


        self.bip49AccountQFrameVLayout.addWidget(self.bip49AccountLabelQFrame)

        self.bip49AccountQLineEdit = QLineEdit(self.bip49AccountQFrame)
        self.bip49AccountQLineEdit.setObjectName(u"bip49AccountQLineEdit")

        self.bip49AccountQFrameVLayout.addWidget(self.bip49AccountQLineEdit)


        self.bip49QStackedWidgetPageHLayout.addWidget(self.bip49AccountQFrame)

        self.bip49ChangeQFrame = QFrame(self.bip49QStackedWidgetPage)
        self.bip49ChangeQFrame.setObjectName(u"bip49ChangeQFrame")
        self.bip49ChangeQFrameVLayout = QVBoxLayout(self.bip49ChangeQFrame)
        self.bip49ChangeQFrameVLayout.setSpacing(5)
        self.bip49ChangeQFrameVLayout.setObjectName(u"bip49ChangeQFrameVLayout")
        self.bip49ChangeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip49ChangeLabelQFrame = QFrame(self.bip49ChangeQFrame)
        self.bip49ChangeLabelQFrame.setObjectName(u"bip49ChangeLabelQFrame")
        self.bip49ChangeLabelQFrameHLayout = QHBoxLayout(self.bip49ChangeLabelQFrame)
        self.bip49ChangeLabelQFrameHLayout.setSpacing(15)
        self.bip49ChangeLabelQFrameHLayout.setObjectName(u"bip49ChangeLabelQFrameHLayout")
        self.bip49ChangeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip49ChangeQLabel = QLabel(self.bip49ChangeLabelQFrame)
        self.bip49ChangeQLabel.setObjectName(u"bip49ChangeQLabel")

        self.bip49ChangeLabelQFrameHLayout.addWidget(self.bip49ChangeQLabel)

        self.bip49ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip49ChangeLabelQFrameHLayout.addItem(self.bip49ChangeLabelHSpacer)


        self.bip49ChangeQFrameVLayout.addWidget(self.bip49ChangeLabelQFrame)

        self.bip49ChangeQComboBox = QComboBox(self.bip49ChangeQFrame)
        self.bip49ChangeQComboBox.addItem("")
        self.bip49ChangeQComboBox.addItem("")
        self.bip49ChangeQComboBox.setObjectName(u"bip49ChangeQComboBox")

        self.bip49ChangeQFrameVLayout.addWidget(self.bip49ChangeQComboBox)


        self.bip49QStackedWidgetPageHLayout.addWidget(self.bip49ChangeQFrame)

        self.bip49AddressQFrame = QFrame(self.bip49QStackedWidgetPage)
        self.bip49AddressQFrame.setObjectName(u"bip49AddressQFrame")
        self.bip49AddressQFrameVLayout = QVBoxLayout(self.bip49AddressQFrame)
        self.bip49AddressQFrameVLayout.setSpacing(5)
        self.bip49AddressQFrameVLayout.setObjectName(u"bip49AddressQFrameVLayout")
        self.bip49AddressQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip49AddressLabelQFrame = QFrame(self.bip49AddressQFrame)
        self.bip49AddressLabelQFrame.setObjectName(u"bip49AddressLabelQFrame")
        self.bip49AddressLabelQFrameHLayout = QHBoxLayout(self.bip49AddressLabelQFrame)
        self.bip49AddressLabelQFrameHLayout.setSpacing(15)
        self.bip49AddressLabelQFrameHLayout.setObjectName(u"bip49AddressLabelQFrameHLayout")
        self.bip49AddressLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip49AddressQLabel = QLabel(self.bip49AddressLabelQFrame)
        self.bip49AddressQLabel.setObjectName(u"bip49AddressQLabel")

        self.bip49AddressLabelQFrameHLayout.addWidget(self.bip49AddressQLabel)

        self.bip49AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip49AddressLabelQFrameHLayout.addItem(self.bip49AddressLabelHSpacer)


        self.bip49AddressQFrameVLayout.addWidget(self.bip49AddressLabelQFrame)

        self.bip49AddressQLineEdit = QLineEdit(self.bip49AddressQFrame)
        self.bip49AddressQLineEdit.setObjectName(u"bip49AddressQLineEdit")

        self.bip49AddressQFrameVLayout.addWidget(self.bip49AddressQLineEdit)


        self.bip49QStackedWidgetPageHLayout.addWidget(self.bip49AddressQFrame)

        self.derivationsQStackedWidget.addWidget(self.bip49QStackedWidgetPage)
        self.bip84QStackedWidgetPage = QWidget()
        self.bip84QStackedWidgetPage.setObjectName(u"bip84QStackedWidgetPage")
        self.bip84QStackedWidgetPageHLayout = QHBoxLayout(self.bip84QStackedWidgetPage)
        self.bip84QStackedWidgetPageHLayout.setSpacing(15)
        self.bip84QStackedWidgetPageHLayout.setObjectName(u"bip84QStackedWidgetPageHLayout")
        self.bip84QStackedWidgetPageHLayout.setContentsMargins(0, 5, 0, 0)
        self.bip84PurposeQFrame = QFrame(self.bip84QStackedWidgetPage)
        self.bip84PurposeQFrame.setObjectName(u"bip84PurposeQFrame")
        self.bip84PurposeQFrameVLayout = QVBoxLayout(self.bip84PurposeQFrame)
        self.bip84PurposeQFrameVLayout.setSpacing(5)
        self.bip84PurposeQFrameVLayout.setObjectName(u"bip84PurposeQFrameVLayout")
        self.bip84PurposeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip84PurposeLabelQFrame = QFrame(self.bip84PurposeQFrame)
        self.bip84PurposeLabelQFrame.setObjectName(u"bip84PurposeLabelQFrame")
        self.bip84PurposeLabelQFrameHLayout = QHBoxLayout(self.bip84PurposeLabelQFrame)
        self.bip84PurposeLabelQFrameHLayout.setSpacing(15)
        self.bip84PurposeLabelQFrameHLayout.setObjectName(u"bip84PurposeLabelQFrameHLayout")
        self.bip84PurposeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip84PurposeQLabel = QLabel(self.bip84PurposeLabelQFrame)
        self.bip84PurposeQLabel.setObjectName(u"bip84PurposeQLabel")

        self.bip84PurposeLabelQFrameHLayout.addWidget(self.bip84PurposeQLabel)

        self.bip84PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip84PurposeLabelQFrameHLayout.addItem(self.bip84PurposeLabelHSpacer)


        self.bip84PurposeQFrameVLayout.addWidget(self.bip84PurposeLabelQFrame)

        self.bip84PurposeQLineEdit = QLineEdit(self.bip84PurposeQFrame)
        self.bip84PurposeQLineEdit.setObjectName(u"bip84PurposeQLineEdit")
        self.bip84PurposeQLineEdit.setEnabled(False)

        self.bip84PurposeQFrameVLayout.addWidget(self.bip84PurposeQLineEdit)


        self.bip84QStackedWidgetPageHLayout.addWidget(self.bip84PurposeQFrame)

        self.bip84CoinTypeQFrame = QFrame(self.bip84QStackedWidgetPage)
        self.bip84CoinTypeQFrame.setObjectName(u"bip84CoinTypeQFrame")
        self.bip84CoinTypeQFrameVLayout = QVBoxLayout(self.bip84CoinTypeQFrame)
        self.bip84CoinTypeQFrameVLayout.setSpacing(5)
        self.bip84CoinTypeQFrameVLayout.setObjectName(u"bip84CoinTypeQFrameVLayout")
        self.bip84CoinTypeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip84CoinTypeLabelQFrame = QFrame(self.bip84CoinTypeQFrame)
        self.bip84CoinTypeLabelQFrame.setObjectName(u"bip84CoinTypeLabelQFrame")
        self.bip84CoinTypeLabelQFrameHLayout = QHBoxLayout(self.bip84CoinTypeLabelQFrame)
        self.bip84CoinTypeLabelQFrameHLayout.setSpacing(15)
        self.bip84CoinTypeLabelQFrameHLayout.setObjectName(u"bip84CoinTypeLabelQFrameHLayout")
        self.bip84CoinTypeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip84CoinTypeQLabel = QLabel(self.bip84CoinTypeLabelQFrame)
        self.bip84CoinTypeQLabel.setObjectName(u"bip84CoinTypeQLabel")

        self.bip84CoinTypeLabelQFrameHLayout.addWidget(self.bip84CoinTypeQLabel)

        self.bip84CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip84CoinTypeLabelQFrameHLayout.addItem(self.bip84CoinTypeLabelHSpacer)


        self.bip84CoinTypeQFrameVLayout.addWidget(self.bip84CoinTypeLabelQFrame)

        self.bip84CoinTypeQLineEdit = QLineEdit(self.bip84CoinTypeQFrame)
        self.bip84CoinTypeQLineEdit.setObjectName(u"bip84CoinTypeQLineEdit")
        self.bip84CoinTypeQLineEdit.setEnabled(False)

        self.bip84CoinTypeQFrameVLayout.addWidget(self.bip84CoinTypeQLineEdit)


        self.bip84QStackedWidgetPageHLayout.addWidget(self.bip84CoinTypeQFrame)

        self.bip84AccountQFrame = QFrame(self.bip84QStackedWidgetPage)
        self.bip84AccountQFrame.setObjectName(u"bip84AccountQFrame")
        self.bip84AccountQFrameVLayout = QVBoxLayout(self.bip84AccountQFrame)
        self.bip84AccountQFrameVLayout.setSpacing(5)
        self.bip84AccountQFrameVLayout.setObjectName(u"bip84AccountQFrameVLayout")
        self.bip84AccountQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip84AccountLabelQFrame = QFrame(self.bip84AccountQFrame)
        self.bip84AccountLabelQFrame.setObjectName(u"bip84AccountLabelQFrame")
        self.bip84AccountLabelQFrameHLayout = QHBoxLayout(self.bip84AccountLabelQFrame)
        self.bip84AccountLabelQFrameHLayout.setSpacing(15)
        self.bip84AccountLabelQFrameHLayout.setObjectName(u"bip84AccountLabelQFrameHLayout")
        self.bip84AccountLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip84AccountQLabel = QLabel(self.bip84AccountLabelQFrame)
        self.bip84AccountQLabel.setObjectName(u"bip84AccountQLabel")

        self.bip84AccountLabelQFrameHLayout.addWidget(self.bip84AccountQLabel)

        self.bip84AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip84AccountLabelQFrameHLayout.addItem(self.bip84AccountLabelHSpacer)


        self.bip84AccountQFrameVLayout.addWidget(self.bip84AccountLabelQFrame)

        self.bip84AccountQLineEdit = QLineEdit(self.bip84AccountQFrame)
        self.bip84AccountQLineEdit.setObjectName(u"bip84AccountQLineEdit")

        self.bip84AccountQFrameVLayout.addWidget(self.bip84AccountQLineEdit)


        self.bip84QStackedWidgetPageHLayout.addWidget(self.bip84AccountQFrame)

        self.bip84ChangeQFrame = QFrame(self.bip84QStackedWidgetPage)
        self.bip84ChangeQFrame.setObjectName(u"bip84ChangeQFrame")
        self.bip84ChangeQFrameVLayout = QVBoxLayout(self.bip84ChangeQFrame)
        self.bip84ChangeQFrameVLayout.setSpacing(5)
        self.bip84ChangeQFrameVLayout.setObjectName(u"bip84ChangeQFrameVLayout")
        self.bip84ChangeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip84ChangeLabelQFrame = QFrame(self.bip84ChangeQFrame)
        self.bip84ChangeLabelQFrame.setObjectName(u"bip84ChangeLabelQFrame")
        self.bip84ChangeLabelQFrameHLayout = QHBoxLayout(self.bip84ChangeLabelQFrame)
        self.bip84ChangeLabelQFrameHLayout.setSpacing(15)
        self.bip84ChangeLabelQFrameHLayout.setObjectName(u"bip84ChangeLabelQFrameHLayout")
        self.bip84ChangeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip84ChangeQLabel = QLabel(self.bip84ChangeLabelQFrame)
        self.bip84ChangeQLabel.setObjectName(u"bip84ChangeQLabel")

        self.bip84ChangeLabelQFrameHLayout.addWidget(self.bip84ChangeQLabel)

        self.bip84ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip84ChangeLabelQFrameHLayout.addItem(self.bip84ChangeLabelHSpacer)


        self.bip84ChangeQFrameVLayout.addWidget(self.bip84ChangeLabelQFrame)

        self.bip84ChangeQComboBox = QComboBox(self.bip84ChangeQFrame)
        self.bip84ChangeQComboBox.addItem("")
        self.bip84ChangeQComboBox.addItem("")
        self.bip84ChangeQComboBox.setObjectName(u"bip84ChangeQComboBox")

        self.bip84ChangeQFrameVLayout.addWidget(self.bip84ChangeQComboBox)


        self.bip84QStackedWidgetPageHLayout.addWidget(self.bip84ChangeQFrame)

        self.bip84AddressQFrame = QFrame(self.bip84QStackedWidgetPage)
        self.bip84AddressQFrame.setObjectName(u"bip84AddressQFrame")
        self.bip84AddressQFrameVLayout = QVBoxLayout(self.bip84AddressQFrame)
        self.bip84AddressQFrameVLayout.setSpacing(5)
        self.bip84AddressQFrameVLayout.setObjectName(u"bip84AddressQFrameVLayout")
        self.bip84AddressQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip84AddressLabelQFrame = QFrame(self.bip84AddressQFrame)
        self.bip84AddressLabelQFrame.setObjectName(u"bip84AddressLabelQFrame")
        self.bip84AddressLabelQFrameHLayout = QHBoxLayout(self.bip84AddressLabelQFrame)
        self.bip84AddressLabelQFrameHLayout.setSpacing(15)
        self.bip84AddressLabelQFrameHLayout.setObjectName(u"bip84AddressLabelQFrameHLayout")
        self.bip84AddressLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip84AddressQLabel = QLabel(self.bip84AddressLabelQFrame)
        self.bip84AddressQLabel.setObjectName(u"bip84AddressQLabel")

        self.bip84AddressLabelQFrameHLayout.addWidget(self.bip84AddressQLabel)

        self.bip84AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip84AddressLabelQFrameHLayout.addItem(self.bip84AddressLabelHSpacer)


        self.bip84AddressQFrameVLayout.addWidget(self.bip84AddressLabelQFrame)

        self.bip84AddressQLineEdit = QLineEdit(self.bip84AddressQFrame)
        self.bip84AddressQLineEdit.setObjectName(u"bip84AddressQLineEdit")

        self.bip84AddressQFrameVLayout.addWidget(self.bip84AddressQLineEdit)


        self.bip84QStackedWidgetPageHLayout.addWidget(self.bip84AddressQFrame)

        self.derivationsQStackedWidget.addWidget(self.bip84QStackedWidgetPage)
        self.bip86QStackedWidgetPage = QWidget()
        self.bip86QStackedWidgetPage.setObjectName(u"bip86QStackedWidgetPage")
        self.bip86QStackedWidgetPageHLayout = QHBoxLayout(self.bip86QStackedWidgetPage)
        self.bip86QStackedWidgetPageHLayout.setSpacing(15)
        self.bip86QStackedWidgetPageHLayout.setObjectName(u"bip86QStackedWidgetPageHLayout")
        self.bip86QStackedWidgetPageHLayout.setContentsMargins(0, 5, 0, 0)
        self.bip86PurposeQFrame = QFrame(self.bip86QStackedWidgetPage)
        self.bip86PurposeQFrame.setObjectName(u"bip86PurposeQFrame")
        self.bip86PurposeQFrameVLayout = QVBoxLayout(self.bip86PurposeQFrame)
        self.bip86PurposeQFrameVLayout.setSpacing(5)
        self.bip86PurposeQFrameVLayout.setObjectName(u"bip86PurposeQFrameVLayout")
        self.bip86PurposeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip86PurposeLabelQFrame = QFrame(self.bip86PurposeQFrame)
        self.bip86PurposeLabelQFrame.setObjectName(u"bip86PurposeLabelQFrame")
        self.bip86PurposeLabelQFrameHLayout = QHBoxLayout(self.bip86PurposeLabelQFrame)
        self.bip86PurposeLabelQFrameHLayout.setSpacing(15)
        self.bip86PurposeLabelQFrameHLayout.setObjectName(u"bip86PurposeLabelQFrameHLayout")
        self.bip86PurposeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip86PurposeQLabel = QLabel(self.bip86PurposeLabelQFrame)
        self.bip86PurposeQLabel.setObjectName(u"bip86PurposeQLabel")

        self.bip86PurposeLabelQFrameHLayout.addWidget(self.bip86PurposeQLabel)

        self.bip86PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip86PurposeLabelQFrameHLayout.addItem(self.bip86PurposeLabelHSpacer)


        self.bip86PurposeQFrameVLayout.addWidget(self.bip86PurposeLabelQFrame)

        self.bip86PurposeQLineEdit = QLineEdit(self.bip86PurposeQFrame)
        self.bip86PurposeQLineEdit.setObjectName(u"bip86PurposeQLineEdit")
        self.bip86PurposeQLineEdit.setEnabled(False)

        self.bip86PurposeQFrameVLayout.addWidget(self.bip86PurposeQLineEdit)


        self.bip86QStackedWidgetPageHLayout.addWidget(self.bip86PurposeQFrame)

        self.bip86CoinTypeQFrame = QFrame(self.bip86QStackedWidgetPage)
        self.bip86CoinTypeQFrame.setObjectName(u"bip86CoinTypeQFrame")
        self.bip86CoinTypeQFrameVLayout = QVBoxLayout(self.bip86CoinTypeQFrame)
        self.bip86CoinTypeQFrameVLayout.setSpacing(5)
        self.bip86CoinTypeQFrameVLayout.setObjectName(u"bip86CoinTypeQFrameVLayout")
        self.bip86CoinTypeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip86CoinTypeLabelContainerQFrame = QFrame(self.bip86CoinTypeQFrame)
        self.bip86CoinTypeLabelContainerQFrame.setObjectName(u"bip86CoinTypeLabelContainerQFrame")
        self.bip86CoinTypeLabelContainerQFrameHLayout = QHBoxLayout(self.bip86CoinTypeLabelContainerQFrame)
        self.bip86CoinTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.bip86CoinTypeLabelContainerQFrameHLayout.setObjectName(u"bip86CoinTypeLabelContainerQFrameHLayout")
        self.bip86CoinTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip86CoinTypeQLabel = QLabel(self.bip86CoinTypeLabelContainerQFrame)
        self.bip86CoinTypeQLabel.setObjectName(u"bip86CoinTypeQLabel")

        self.bip86CoinTypeLabelContainerQFrameHLayout.addWidget(self.bip86CoinTypeQLabel)

        self.bip86CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip86CoinTypeLabelContainerQFrameHLayout.addItem(self.bip86CoinTypeLabelHSpacer)


        self.bip86CoinTypeQFrameVLayout.addWidget(self.bip86CoinTypeLabelContainerQFrame)

        self.bip86CoinTypeQLineEdit = QLineEdit(self.bip86CoinTypeQFrame)
        self.bip86CoinTypeQLineEdit.setObjectName(u"bip86CoinTypeQLineEdit")
        self.bip86CoinTypeQLineEdit.setEnabled(False)

        self.bip86CoinTypeQFrameVLayout.addWidget(self.bip86CoinTypeQLineEdit)


        self.bip86QStackedWidgetPageHLayout.addWidget(self.bip86CoinTypeQFrame)

        self.bip86AccountQFrame = QFrame(self.bip86QStackedWidgetPage)
        self.bip86AccountQFrame.setObjectName(u"bip86AccountQFrame")
        self.bip86AccountQFrameVLayout = QVBoxLayout(self.bip86AccountQFrame)
        self.bip86AccountQFrameVLayout.setSpacing(5)
        self.bip86AccountQFrameVLayout.setObjectName(u"bip86AccountQFrameVLayout")
        self.bip86AccountQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip86AccountLabelQFrame = QFrame(self.bip86AccountQFrame)
        self.bip86AccountLabelQFrame.setObjectName(u"bip86AccountLabelQFrame")
        self.bip86AccountLabelQFrameHLayout = QHBoxLayout(self.bip86AccountLabelQFrame)
        self.bip86AccountLabelQFrameHLayout.setSpacing(15)
        self.bip86AccountLabelQFrameHLayout.setObjectName(u"bip86AccountLabelQFrameHLayout")
        self.bip86AccountLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip86AccountQLabel = QLabel(self.bip86AccountLabelQFrame)
        self.bip86AccountQLabel.setObjectName(u"bip86AccountQLabel")

        self.bip86AccountLabelQFrameHLayout.addWidget(self.bip86AccountQLabel)

        self.bip86AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip86AccountLabelQFrameHLayout.addItem(self.bip86AccountLabelHSpacer)


        self.bip86AccountQFrameVLayout.addWidget(self.bip86AccountLabelQFrame)

        self.bip86AccountQLineEdit = QLineEdit(self.bip86AccountQFrame)
        self.bip86AccountQLineEdit.setObjectName(u"bip86AccountQLineEdit")

        self.bip86AccountQFrameVLayout.addWidget(self.bip86AccountQLineEdit)


        self.bip86QStackedWidgetPageHLayout.addWidget(self.bip86AccountQFrame)

        self.bip86ChangeQFrame = QFrame(self.bip86QStackedWidgetPage)
        self.bip86ChangeQFrame.setObjectName(u"bip86ChangeQFrame")
        self.bip86ChangeQFrameVLayout = QVBoxLayout(self.bip86ChangeQFrame)
        self.bip86ChangeQFrameVLayout.setSpacing(5)
        self.bip86ChangeQFrameVLayout.setObjectName(u"bip86ChangeQFrameVLayout")
        self.bip86ChangeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip86ChangeLabelQFrame = QFrame(self.bip86ChangeQFrame)
        self.bip86ChangeLabelQFrame.setObjectName(u"bip86ChangeLabelQFrame")
        self.bip86ChangeLabelQFrameHLayout = QHBoxLayout(self.bip86ChangeLabelQFrame)
        self.bip86ChangeLabelQFrameHLayout.setSpacing(15)
        self.bip86ChangeLabelQFrameHLayout.setObjectName(u"bip86ChangeLabelQFrameHLayout")
        self.bip86ChangeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip86ChangeQLabel = QLabel(self.bip86ChangeLabelQFrame)
        self.bip86ChangeQLabel.setObjectName(u"bip86ChangeQLabel")

        self.bip86ChangeLabelQFrameHLayout.addWidget(self.bip86ChangeQLabel)

        self.bip86ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip86ChangeLabelQFrameHLayout.addItem(self.bip86ChangeLabelHSpacer)


        self.bip86ChangeQFrameVLayout.addWidget(self.bip86ChangeLabelQFrame)

        self.bip86ChangeQComboBox = QComboBox(self.bip86ChangeQFrame)
        self.bip86ChangeQComboBox.addItem("")
        self.bip86ChangeQComboBox.addItem("")
        self.bip86ChangeQComboBox.setObjectName(u"bip86ChangeQComboBox")

        self.bip86ChangeQFrameVLayout.addWidget(self.bip86ChangeQComboBox)


        self.bip86QStackedWidgetPageHLayout.addWidget(self.bip86ChangeQFrame)

        self.bip86AddressQFrame = QFrame(self.bip86QStackedWidgetPage)
        self.bip86AddressQFrame.setObjectName(u"bip86AddressQFrame")
        self.bip86AddressQFrameVLayout = QVBoxLayout(self.bip86AddressQFrame)
        self.bip86AddressQFrameVLayout.setSpacing(5)
        self.bip86AddressQFrameVLayout.setObjectName(u"bip86AddressQFrameVLayout")
        self.bip86AddressQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip86AddressLabelQFrame = QFrame(self.bip86AddressQFrame)
        self.bip86AddressLabelQFrame.setObjectName(u"bip86AddressLabelQFrame")
        self.bip86AddressLabelQFrameHLayout = QHBoxLayout(self.bip86AddressLabelQFrame)
        self.bip86AddressLabelQFrameHLayout.setSpacing(15)
        self.bip86AddressLabelQFrameHLayout.setObjectName(u"bip86AddressLabelQFrameHLayout")
        self.bip86AddressLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip86AddressQLabel = QLabel(self.bip86AddressLabelQFrame)
        self.bip86AddressQLabel.setObjectName(u"bip86AddressQLabel")

        self.bip86AddressLabelQFrameHLayout.addWidget(self.bip86AddressQLabel)

        self.bip86AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bip86AddressLabelQFrameHLayout.addItem(self.bip86AddressLabelHSpacer)


        self.bip86AddressQFrameVLayout.addWidget(self.bip86AddressLabelQFrame)

        self.bip86AddressQLineEdit = QLineEdit(self.bip86AddressQFrame)
        self.bip86AddressQLineEdit.setObjectName(u"bip86AddressQLineEdit")

        self.bip86AddressQFrameVLayout.addWidget(self.bip86AddressQLineEdit)


        self.bip86QStackedWidgetPageHLayout.addWidget(self.bip86AddressQFrame)

        self.derivationsQStackedWidget.addWidget(self.bip86QStackedWidgetPage)
        self.bip141QStackedWidgetPage = QWidget()
        self.bip141QStackedWidgetPage.setObjectName(u"bip141QStackedWidgetPage")
        self.bip141QStackedWidgetPageHLayout = QHBoxLayout(self.bip141QStackedWidgetPage)
        self.bip141QStackedWidgetPageHLayout.setSpacing(15)
        self.bip141QStackedWidgetPageHLayout.setObjectName(u"bip141QStackedWidgetPageHLayout")
        self.bip141QStackedWidgetPageHLayout.setContentsMargins(0, 5, 0, 0)
        self.bip141PathQFrame = QFrame(self.bip141QStackedWidgetPage)
        self.bip141PathQFrame.setObjectName(u"bip141PathQFrame")
        self.BIP141PathVLayout = QVBoxLayout(self.bip141PathQFrame)
        self.BIP141PathVLayout.setSpacing(5)
        self.BIP141PathVLayout.setObjectName(u"BIP141PathVLayout")
        self.BIP141PathVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip141PathLabelQFrame = QFrame(self.bip141PathQFrame)
        self.bip141PathLabelQFrame.setObjectName(u"bip141PathLabelQFrame")
        self.BIP141PathLabelHLayout = QHBoxLayout(self.bip141PathLabelQFrame)
        self.BIP141PathLabelHLayout.setSpacing(15)
        self.BIP141PathLabelHLayout.setObjectName(u"BIP141PathLabelHLayout")
        self.BIP141PathLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip141PathQLabel = QLabel(self.bip141PathLabelQFrame)
        self.bip141PathQLabel.setObjectName(u"bip141PathQLabel")

        self.BIP141PathLabelHLayout.addWidget(self.bip141PathQLabel)

        self.bip141PathLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP141PathLabelHLayout.addItem(self.bip141PathLabelHSpacer)


        self.BIP141PathVLayout.addWidget(self.bip141PathLabelQFrame)

        self.bip141PathQLineEdit = QLineEdit(self.bip141PathQFrame)
        self.bip141PathQLineEdit.setObjectName(u"bip141PathQLineEdit")

        self.BIP141PathVLayout.addWidget(self.bip141PathQLineEdit)


        self.bip141QStackedWidgetPageHLayout.addWidget(self.bip141PathQFrame)

        self.bip141ScriptSemanticsQFrame = QFrame(self.bip141QStackedWidgetPage)
        self.bip141ScriptSemanticsQFrame.setObjectName(u"bip141ScriptSemanticsQFrame")
        self.BIP141ScriptSemanticsVLayout = QVBoxLayout(self.bip141ScriptSemanticsQFrame)
        self.BIP141ScriptSemanticsVLayout.setSpacing(5)
        self.BIP141ScriptSemanticsVLayout.setObjectName(u"BIP141ScriptSemanticsVLayout")
        self.BIP141ScriptSemanticsVLayout.setContentsMargins(0, 0, 0, 0)
        self.bip141ScriptSemanticsLabelQFrame = QFrame(self.bip141ScriptSemanticsQFrame)
        self.bip141ScriptSemanticsLabelQFrame.setObjectName(u"bip141ScriptSemanticsLabelQFrame")
        self.BIP141ScriptSemanticsLabelHLayout = QHBoxLayout(self.bip141ScriptSemanticsLabelQFrame)
        self.BIP141ScriptSemanticsLabelHLayout.setSpacing(15)
        self.BIP141ScriptSemanticsLabelHLayout.setObjectName(u"BIP141ScriptSemanticsLabelHLayout")
        self.BIP141ScriptSemanticsLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.bip141ScriptSemanticsQLabel = QLabel(self.bip141ScriptSemanticsLabelQFrame)
        self.bip141ScriptSemanticsQLabel.setObjectName(u"bip141ScriptSemanticsQLabel")

        self.BIP141ScriptSemanticsLabelHLayout.addWidget(self.bip141ScriptSemanticsQLabel)

        self.bip141ScriptSemanticsLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP141ScriptSemanticsLabelHLayout.addItem(self.bip141ScriptSemanticsLabelHSpacer)


        self.BIP141ScriptSemanticsVLayout.addWidget(self.bip141ScriptSemanticsLabelQFrame)

        self.bip141ScriptSemanticsQComboBox = QComboBox(self.bip141ScriptSemanticsQFrame)
        self.bip141ScriptSemanticsQComboBox.addItem("")
        self.bip141ScriptSemanticsQComboBox.addItem("")
        self.bip141ScriptSemanticsQComboBox.addItem("")
        self.bip141ScriptSemanticsQComboBox.addItem("")
        self.bip141ScriptSemanticsQComboBox.setObjectName(u"bip141ScriptSemanticsQComboBox")

        self.BIP141ScriptSemanticsVLayout.addWidget(self.bip141ScriptSemanticsQComboBox)


        self.bip141QStackedWidgetPageHLayout.addWidget(self.bip141ScriptSemanticsQFrame)

        self.derivationsQStackedWidget.addWidget(self.bip141QStackedWidgetPage)
        self.cip1852QStackedWidgetPage = QWidget()
        self.cip1852QStackedWidgetPage.setObjectName(u"cip1852QStackedWidgetPage")
        self.cip1852QStackedWidgetPageHLayout = QHBoxLayout(self.cip1852QStackedWidgetPage)
        self.cip1852QStackedWidgetPageHLayout.setSpacing(15)
        self.cip1852QStackedWidgetPageHLayout.setObjectName(u"cip1852QStackedWidgetPageHLayout")
        self.cip1852QStackedWidgetPageHLayout.setContentsMargins(0, 5, 0, 0)
        self.cip1852PurposeQFrame = QFrame(self.cip1852QStackedWidgetPage)
        self.cip1852PurposeQFrame.setObjectName(u"cip1852PurposeQFrame")
        self.cip1852PurposeQFrameVLayout = QVBoxLayout(self.cip1852PurposeQFrame)
        self.cip1852PurposeQFrameVLayout.setSpacing(5)
        self.cip1852PurposeQFrameVLayout.setObjectName(u"cip1852PurposeQFrameVLayout")
        self.cip1852PurposeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cip1852PurposeLabelQFrame = QFrame(self.cip1852PurposeQFrame)
        self.cip1852PurposeLabelQFrame.setObjectName(u"cip1852PurposeLabelQFrame")
        self.cip1852PurposeLabelQFrameHLayout = QHBoxLayout(self.cip1852PurposeLabelQFrame)
        self.cip1852PurposeLabelQFrameHLayout.setSpacing(15)
        self.cip1852PurposeLabelQFrameHLayout.setObjectName(u"cip1852PurposeLabelQFrameHLayout")
        self.cip1852PurposeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cip1852PurposeQLabel = QLabel(self.cip1852PurposeLabelQFrame)
        self.cip1852PurposeQLabel.setObjectName(u"cip1852PurposeQLabel")

        self.cip1852PurposeLabelQFrameHLayout.addWidget(self.cip1852PurposeQLabel)

        self.cip1852PurposeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cip1852PurposeLabelQFrameHLayout.addItem(self.cip1852PurposeLabelHSpacer)


        self.cip1852PurposeQFrameVLayout.addWidget(self.cip1852PurposeLabelQFrame)

        self.cip1852PurposeQLineEdit = QLineEdit(self.cip1852PurposeQFrame)
        self.cip1852PurposeQLineEdit.setObjectName(u"cip1852PurposeQLineEdit")
        self.cip1852PurposeQLineEdit.setEnabled(False)

        self.cip1852PurposeQFrameVLayout.addWidget(self.cip1852PurposeQLineEdit)


        self.cip1852QStackedWidgetPageHLayout.addWidget(self.cip1852PurposeQFrame)

        self.cip1852CoinTypeQFrame = QFrame(self.cip1852QStackedWidgetPage)
        self.cip1852CoinTypeQFrame.setObjectName(u"cip1852CoinTypeQFrame")
        self.cip1852CoinTypeQFrameVLayout = QVBoxLayout(self.cip1852CoinTypeQFrame)
        self.cip1852CoinTypeQFrameVLayout.setSpacing(5)
        self.cip1852CoinTypeQFrameVLayout.setObjectName(u"cip1852CoinTypeQFrameVLayout")
        self.cip1852CoinTypeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cip1852CoinTypeLabelQFrame = QFrame(self.cip1852CoinTypeQFrame)
        self.cip1852CoinTypeLabelQFrame.setObjectName(u"cip1852CoinTypeLabelQFrame")
        self.cip1852CoinTypeLabelQFrameHLayout = QHBoxLayout(self.cip1852CoinTypeLabelQFrame)
        self.cip1852CoinTypeLabelQFrameHLayout.setSpacing(15)
        self.cip1852CoinTypeLabelQFrameHLayout.setObjectName(u"cip1852CoinTypeLabelQFrameHLayout")
        self.cip1852CoinTypeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cip1852CoinTypeQLabel = QLabel(self.cip1852CoinTypeLabelQFrame)
        self.cip1852CoinTypeQLabel.setObjectName(u"cip1852CoinTypeQLabel")

        self.cip1852CoinTypeLabelQFrameHLayout.addWidget(self.cip1852CoinTypeQLabel)

        self.cip1852CoinTypeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cip1852CoinTypeLabelQFrameHLayout.addItem(self.cip1852CoinTypeLabelHSpacer)


        self.cip1852CoinTypeQFrameVLayout.addWidget(self.cip1852CoinTypeLabelQFrame)

        self.cip1852CoinTypeQLineEdit = QLineEdit(self.cip1852CoinTypeQFrame)
        self.cip1852CoinTypeQLineEdit.setObjectName(u"cip1852CoinTypeQLineEdit")
        self.cip1852CoinTypeQLineEdit.setEnabled(False)

        self.cip1852CoinTypeQFrameVLayout.addWidget(self.cip1852CoinTypeQLineEdit)


        self.cip1852QStackedWidgetPageHLayout.addWidget(self.cip1852CoinTypeQFrame)

        self.cip1852AccountQFrame = QFrame(self.cip1852QStackedWidgetPage)
        self.cip1852AccountQFrame.setObjectName(u"cip1852AccountQFrame")
        self.cip1852AccountQFrameVLayout = QVBoxLayout(self.cip1852AccountQFrame)
        self.cip1852AccountQFrameVLayout.setSpacing(5)
        self.cip1852AccountQFrameVLayout.setObjectName(u"cip1852AccountQFrameVLayout")
        self.cip1852AccountQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cip1852AccountLabelQFrame = QFrame(self.cip1852AccountQFrame)
        self.cip1852AccountLabelQFrame.setObjectName(u"cip1852AccountLabelQFrame")
        self.cip1852AccountLabelQFrameHLayout = QHBoxLayout(self.cip1852AccountLabelQFrame)
        self.cip1852AccountLabelQFrameHLayout.setSpacing(15)
        self.cip1852AccountLabelQFrameHLayout.setObjectName(u"cip1852AccountLabelQFrameHLayout")
        self.cip1852AccountLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cip1852AccountQLabel = QLabel(self.cip1852AccountLabelQFrame)
        self.cip1852AccountQLabel.setObjectName(u"cip1852AccountQLabel")

        self.cip1852AccountLabelQFrameHLayout.addWidget(self.cip1852AccountQLabel)

        self.cip1852AccountLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cip1852AccountLabelQFrameHLayout.addItem(self.cip1852AccountLabelHSpacer)


        self.cip1852AccountQFrameVLayout.addWidget(self.cip1852AccountLabelQFrame)

        self.cip1852AccountQLineEdit = QLineEdit(self.cip1852AccountQFrame)
        self.cip1852AccountQLineEdit.setObjectName(u"cip1852AccountQLineEdit")

        self.cip1852AccountQFrameVLayout.addWidget(self.cip1852AccountQLineEdit)


        self.cip1852QStackedWidgetPageHLayout.addWidget(self.cip1852AccountQFrame)

        self.cip1852ChangeQFrame = QFrame(self.cip1852QStackedWidgetPage)
        self.cip1852ChangeQFrame.setObjectName(u"cip1852ChangeQFrame")
        self.cip1852ChangeQFrameVLayout = QVBoxLayout(self.cip1852ChangeQFrame)
        self.cip1852ChangeQFrameVLayout.setSpacing(5)
        self.cip1852ChangeQFrameVLayout.setObjectName(u"cip1852ChangeQFrameVLayout")
        self.cip1852ChangeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cip1852ChangeLabelQFrame = QFrame(self.cip1852ChangeQFrame)
        self.cip1852ChangeLabelQFrame.setObjectName(u"cip1852ChangeLabelQFrame")
        self.cip1852ChangeLabelQFrameHLayout = QHBoxLayout(self.cip1852ChangeLabelQFrame)
        self.cip1852ChangeLabelQFrameHLayout.setSpacing(15)
        self.cip1852ChangeLabelQFrameHLayout.setObjectName(u"cip1852ChangeLabelQFrameHLayout")
        self.cip1852ChangeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cip1852ChangeQLabel = QLabel(self.cip1852ChangeLabelQFrame)
        self.cip1852ChangeQLabel.setObjectName(u"cip1852ChangeQLabel")

        self.cip1852ChangeLabelQFrameHLayout.addWidget(self.cip1852ChangeQLabel)

        self.cip1852ChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cip1852ChangeLabelQFrameHLayout.addItem(self.cip1852ChangeLabelHSpacer)


        self.cip1852ChangeQFrameVLayout.addWidget(self.cip1852ChangeLabelQFrame)

        self.cip1852ChangeQComboBox = QComboBox(self.cip1852ChangeQFrame)
        self.cip1852ChangeQComboBox.addItem("")
        self.cip1852ChangeQComboBox.addItem("")
        self.cip1852ChangeQComboBox.addItem("")
        self.cip1852ChangeQComboBox.setObjectName(u"cip1852ChangeQComboBox")

        self.cip1852ChangeQFrameVLayout.addWidget(self.cip1852ChangeQComboBox)


        self.cip1852QStackedWidgetPageHLayout.addWidget(self.cip1852ChangeQFrame)

        self.cip1852AddressQFrame = QFrame(self.cip1852QStackedWidgetPage)
        self.cip1852AddressQFrame.setObjectName(u"cip1852AddressQFrame")
        self.cip1852AddressQFrameVLayout = QVBoxLayout(self.cip1852AddressQFrame)
        self.cip1852AddressQFrameVLayout.setSpacing(5)
        self.cip1852AddressQFrameVLayout.setObjectName(u"cip1852AddressQFrameVLayout")
        self.cip1852AddressQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cip1852AddressLabelQFrame = QFrame(self.cip1852AddressQFrame)
        self.cip1852AddressLabelQFrame.setObjectName(u"cip1852AddressLabelQFrame")
        self.cip1852AddressLabelQFrameHLayout = QHBoxLayout(self.cip1852AddressLabelQFrame)
        self.cip1852AddressLabelQFrameHLayout.setSpacing(15)
        self.cip1852AddressLabelQFrameHLayout.setObjectName(u"cip1852AddressLabelQFrameHLayout")
        self.cip1852AddressLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cip1852AddressQLabel = QLabel(self.cip1852AddressLabelQFrame)
        self.cip1852AddressQLabel.setObjectName(u"cip1852AddressQLabel")

        self.cip1852AddressLabelQFrameHLayout.addWidget(self.cip1852AddressQLabel)

        self.cip1852AddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cip1852AddressLabelQFrameHLayout.addItem(self.cip1852AddressLabelHSpacer)


        self.cip1852AddressQFrameVLayout.addWidget(self.cip1852AddressLabelQFrame)

        self.cip1852AddressQLineEdit = QLineEdit(self.cip1852AddressQFrame)
        self.cip1852AddressQLineEdit.setObjectName(u"cip1852AddressQLineEdit")

        self.cip1852AddressQFrameVLayout.addWidget(self.cip1852AddressQLineEdit)


        self.cip1852QStackedWidgetPageHLayout.addWidget(self.cip1852AddressQFrame)

        self.derivationsQStackedWidget.addWidget(self.cip1852QStackedWidgetPage)
        self.electrumQStackedWidgetPage = QWidget()
        self.electrumQStackedWidgetPage.setObjectName(u"electrumQStackedWidgetPage")
        self.electrumQStackedWidgetPageHLayout = QHBoxLayout(self.electrumQStackedWidgetPage)
        self.electrumQStackedWidgetPageHLayout.setSpacing(15)
        self.electrumQStackedWidgetPageHLayout.setObjectName(u"electrumQStackedWidgetPageHLayout")
        self.electrumQStackedWidgetPageHLayout.setContentsMargins(0, 5, 0, 0)
        self.electrumChangeQFrame = QFrame(self.electrumQStackedWidgetPage)
        self.electrumChangeQFrame.setObjectName(u"electrumChangeQFrame")
        self.electrumChangeQFrameVLayout = QVBoxLayout(self.electrumChangeQFrame)
        self.electrumChangeQFrameVLayout.setSpacing(5)
        self.electrumChangeQFrameVLayout.setObjectName(u"electrumChangeQFrameVLayout")
        self.electrumChangeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumChangeLabelQFrame = QFrame(self.electrumChangeQFrame)
        self.electrumChangeLabelQFrame.setObjectName(u"electrumChangeLabelQFrame")
        self.electrumChangeLabelQFrameHLayout = QHBoxLayout(self.electrumChangeLabelQFrame)
        self.electrumChangeLabelQFrameHLayout.setSpacing(15)
        self.electrumChangeLabelQFrameHLayout.setObjectName(u"electrumChangeLabelQFrameHLayout")
        self.electrumChangeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumChangeQLabel = QLabel(self.electrumChangeLabelQFrame)
        self.electrumChangeQLabel.setObjectName(u"electrumChangeQLabel")

        self.electrumChangeLabelQFrameHLayout.addWidget(self.electrumChangeQLabel)

        self.electrumChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumChangeLabelQFrameHLayout.addItem(self.electrumChangeLabelHSpacer)


        self.electrumChangeQFrameVLayout.addWidget(self.electrumChangeLabelQFrame)

        self.electrumChangeQLineEdit = QLineEdit(self.electrumChangeQFrame)
        self.electrumChangeQLineEdit.setObjectName(u"electrumChangeQLineEdit")

        self.electrumChangeQFrameVLayout.addWidget(self.electrumChangeQLineEdit)


        self.electrumQStackedWidgetPageHLayout.addWidget(self.electrumChangeQFrame)

        self.electrumAddressQFrame = QFrame(self.electrumQStackedWidgetPage)
        self.electrumAddressQFrame.setObjectName(u"electrumAddressQFrame")
        self.electrumAddressQFrameVLayout = QVBoxLayout(self.electrumAddressQFrame)
        self.electrumAddressQFrameVLayout.setSpacing(5)
        self.electrumAddressQFrameVLayout.setObjectName(u"electrumAddressQFrameVLayout")
        self.electrumAddressQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumAddressLabelQFrame = QFrame(self.electrumAddressQFrame)
        self.electrumAddressLabelQFrame.setObjectName(u"electrumAddressLabelQFrame")
        self.electrumAddressLabelQFrameHLayout = QHBoxLayout(self.electrumAddressLabelQFrame)
        self.electrumAddressLabelQFrameHLayout.setSpacing(15)
        self.electrumAddressLabelQFrameHLayout.setObjectName(u"electrumAddressLabelQFrameHLayout")
        self.electrumAddressLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.electrumAddressQLabel = QLabel(self.electrumAddressLabelQFrame)
        self.electrumAddressQLabel.setObjectName(u"electrumAddressQLabel")

        self.electrumAddressLabelQFrameHLayout.addWidget(self.electrumAddressQLabel)

        self.electrumAddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.electrumAddressLabelQFrameHLayout.addItem(self.electrumAddressLabelHSpacer)


        self.electrumAddressQFrameVLayout.addWidget(self.electrumAddressLabelQFrame)

        self.electrumAddressQLineEdit = QLineEdit(self.electrumAddressQFrame)
        self.electrumAddressQLineEdit.setObjectName(u"electrumAddressQLineEdit")

        self.electrumAddressQFrameVLayout.addWidget(self.electrumAddressQLineEdit)


        self.electrumQStackedWidgetPageHLayout.addWidget(self.electrumAddressQFrame)

        self.derivationsQStackedWidget.addWidget(self.electrumQStackedWidgetPage)
        self.moneroQStackedWidgetPage = QWidget()
        self.moneroQStackedWidgetPage.setObjectName(u"moneroQStackedWidgetPage")
        self.moneroQStackedWidgetPageHLayout = QHBoxLayout(self.moneroQStackedWidgetPage)
        self.moneroQStackedWidgetPageHLayout.setSpacing(15)
        self.moneroQStackedWidgetPageHLayout.setObjectName(u"moneroQStackedWidgetPageHLayout")
        self.moneroQStackedWidgetPageHLayout.setContentsMargins(0, 5, 0, 0)
        self.moneroMinorQFrame = QFrame(self.moneroQStackedWidgetPage)
        self.moneroMinorQFrame.setObjectName(u"moneroMinorQFrame")
        self.moneroMinorQFrameVLayout = QVBoxLayout(self.moneroMinorQFrame)
        self.moneroMinorQFrameVLayout.setSpacing(5)
        self.moneroMinorQFrameVLayout.setObjectName(u"moneroMinorQFrameVLayout")
        self.moneroMinorQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroMinorLabelQFrame = QFrame(self.moneroMinorQFrame)
        self.moneroMinorLabelQFrame.setObjectName(u"moneroMinorLabelQFrame")
        self.moneroMinorLabelQFrameHLayout = QHBoxLayout(self.moneroMinorLabelQFrame)
        self.moneroMinorLabelQFrameHLayout.setSpacing(15)
        self.moneroMinorLabelQFrameHLayout.setObjectName(u"moneroMinorLabelQFrameHLayout")
        self.moneroMinorLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroMinorQLabel = QLabel(self.moneroMinorLabelQFrame)
        self.moneroMinorQLabel.setObjectName(u"moneroMinorQLabel")

        self.moneroMinorLabelQFrameHLayout.addWidget(self.moneroMinorQLabel)

        self.moneroMinorLabelLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroMinorLabelQFrameHLayout.addItem(self.moneroMinorLabelLabelHSpacer)


        self.moneroMinorQFrameVLayout.addWidget(self.moneroMinorLabelQFrame)

        self.moneroMinorQLineEdit = QLineEdit(self.moneroMinorQFrame)
        self.moneroMinorQLineEdit.setObjectName(u"moneroMinorQLineEdit")

        self.moneroMinorQFrameVLayout.addWidget(self.moneroMinorQLineEdit)


        self.moneroQStackedWidgetPageHLayout.addWidget(self.moneroMinorQFrame)

        self.moneroMajorQFrame = QFrame(self.moneroQStackedWidgetPage)
        self.moneroMajorQFrame.setObjectName(u"moneroMajorQFrame")
        self.moneroMajorQFrameVLayout = QVBoxLayout(self.moneroMajorQFrame)
        self.moneroMajorQFrameVLayout.setSpacing(5)
        self.moneroMajorQFrameVLayout.setObjectName(u"moneroMajorQFrameVLayout")
        self.moneroMajorQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroMajorLabelQFrame = QFrame(self.moneroMajorQFrame)
        self.moneroMajorLabelQFrame.setObjectName(u"moneroMajorLabelQFrame")
        self.moneroMajorLabelQFrameHLayout = QHBoxLayout(self.moneroMajorLabelQFrame)
        self.moneroMajorLabelQFrameHLayout.setSpacing(15)
        self.moneroMajorLabelQFrameHLayout.setObjectName(u"moneroMajorLabelQFrameHLayout")
        self.moneroMajorLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroMajorQLabel = QLabel(self.moneroMajorLabelQFrame)
        self.moneroMajorQLabel.setObjectName(u"moneroMajorQLabel")

        self.moneroMajorLabelQFrameHLayout.addWidget(self.moneroMajorQLabel)

        self.moneroMajorLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.moneroMajorLabelQFrameHLayout.addItem(self.moneroMajorLabelHSpacer)


        self.moneroMajorQFrameVLayout.addWidget(self.moneroMajorLabelQFrame)

        self.moneroMajorQLineEdit = QLineEdit(self.moneroMajorQFrame)
        self.moneroMajorQLineEdit.setObjectName(u"moneroMajorQLineEdit")

        self.moneroMajorQFrameVLayout.addWidget(self.moneroMajorQLineEdit)


        self.moneroQStackedWidgetPageHLayout.addWidget(self.moneroMajorQFrame)

        self.derivationsQStackedWidget.addWidget(self.moneroQStackedWidgetPage)

        self.derivationQGroupBoxVLayout.addWidget(self.derivationsQStackedWidget)


        self.dumpsDerivationContainerQFrameVLayout.addWidget(self.derivationQGroupBox)


        self.dumpsPageQStackedWidgetVLayout.addWidget(self.dumpsDerivationContainerQFrame)

        self.dumpsFormatKeysContainerQGroupBox = QGroupBox(self.dumpsPageQStackedWidget)
        self.dumpsFormatKeysContainerQGroupBox.setObjectName(u"dumpsFormatKeysContainerQGroupBox")
        self.dumpsFormatKeysContainerQGroupBoxHLayout = QHBoxLayout(self.dumpsFormatKeysContainerQGroupBox)
        self.dumpsFormatKeysContainerQGroupBoxHLayout.setSpacing(15)
        self.dumpsFormatKeysContainerQGroupBoxHLayout.setObjectName(u"dumpsFormatKeysContainerQGroupBoxHLayout")
        self.dumpsFormatKeysContainerQGroupBoxHLayout.setContentsMargins(10, 10, 10, 10)
        self.dumpsFormatContainerQFrame = QFrame(self.dumpsFormatKeysContainerQGroupBox)
        self.dumpsFormatContainerQFrame.setObjectName(u"dumpsFormatContainerQFrame")
        self.dumpsFormatContainerQFrameHLayout = QHBoxLayout(self.dumpsFormatContainerQFrame)
        self.dumpsFormatContainerQFrameHLayout.setSpacing(15)
        self.dumpsFormatContainerQFrameHLayout.setObjectName(u"dumpsFormatContainerQFrameHLayout")
        self.dumpsFormatContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsformatQFrame = QFrame(self.dumpsFormatContainerQFrame)
        self.dumpsformatQFrame.setObjectName(u"dumpsformatQFrame")
        self.dumpsformatQFrame.setMaximumSize(QSize(100, 16777215))
        self.dumpsformatQFrameVLayout = QVBoxLayout(self.dumpsformatQFrame)
        self.dumpsformatQFrameVLayout.setSpacing(5)
        self.dumpsformatQFrameVLayout.setObjectName(u"dumpsformatQFrameVLayout")
        self.dumpsformatQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsFormatLabelContainerQFrame = QFrame(self.dumpsformatQFrame)
        self.dumpsFormatLabelContainerQFrame.setObjectName(u"dumpsFormatLabelContainerQFrame")
        self.dumpsFormatLabelContainerQFrameHLayout = QHBoxLayout(self.dumpsFormatLabelContainerQFrame)
        self.dumpsFormatLabelContainerQFrameHLayout.setSpacing(15)
        self.dumpsFormatLabelContainerQFrameHLayout.setObjectName(u"dumpsFormatLabelContainerQFrameHLayout")
        self.dumpsFormatLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsFormatQLabel = QLabel(self.dumpsFormatLabelContainerQFrame)
        self.dumpsFormatQLabel.setObjectName(u"dumpsFormatQLabel")

        self.dumpsFormatLabelContainerQFrameHLayout.addWidget(self.dumpsFormatQLabel)

        self.dumpsFormatLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dumpsFormatLabelContainerQFrameHLayout.addItem(self.dumpsFormatLabelContainerQFrameHSpacer)


        self.dumpsformatQFrameVLayout.addWidget(self.dumpsFormatLabelContainerQFrame)

        self.dumpsFormatQComboBox = QComboBox(self.dumpsformatQFrame)
        self.dumpsFormatQComboBox.addItem("")
        self.dumpsFormatQComboBox.addItem("")
        self.dumpsFormatQComboBox.setObjectName(u"dumpsFormatQComboBox")

        self.dumpsformatQFrameVLayout.addWidget(self.dumpsFormatQComboBox)


        self.dumpsFormatContainerQFrameHLayout.addWidget(self.dumpsformatQFrame)


        self.dumpsFormatKeysContainerQGroupBoxHLayout.addWidget(self.dumpsFormatContainerQFrame)

        self.dumpsExcludeOrIncludeQFrame = QFrame(self.dumpsFormatKeysContainerQGroupBox)
        self.dumpsExcludeOrIncludeQFrame.setObjectName(u"dumpsExcludeOrIncludeQFrame")
        self.dumpsExcludeOrIncludeQFrame.setMinimumSize(QSize(288, 0))
        self.dumpsExcludeOrIncludeQFrameVLayout = QVBoxLayout(self.dumpsExcludeOrIncludeQFrame)
        self.dumpsExcludeOrIncludeQFrameVLayout.setSpacing(5)
        self.dumpsExcludeOrIncludeQFrameVLayout.setObjectName(u"dumpsExcludeOrIncludeQFrameVLayout")
        self.dumpsExcludeOrIncludeQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsExcludeOrIncludeLabelContainerQFrame = QFrame(self.dumpsExcludeOrIncludeQFrame)
        self.dumpsExcludeOrIncludeLabelContainerQFrame.setObjectName(u"dumpsExcludeOrIncludeLabelContainerQFrame")
        self.dumpsExcludeOrIncludeLabelContainerQFrameHLayout = QHBoxLayout(self.dumpsExcludeOrIncludeLabelContainerQFrame)
        self.dumpsExcludeOrIncludeLabelContainerQFrameHLayout.setSpacing(15)
        self.dumpsExcludeOrIncludeLabelContainerQFrameHLayout.setObjectName(u"dumpsExcludeOrIncludeLabelContainerQFrameHLayout")
        self.dumpsExcludeOrIncludeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsExcludeOrIncludeQLabel = QLabel(self.dumpsExcludeOrIncludeLabelContainerQFrame)
        self.dumpsExcludeOrIncludeQLabel.setObjectName(u"dumpsExcludeOrIncludeQLabel")

        self.dumpsExcludeOrIncludeLabelContainerQFrameHLayout.addWidget(self.dumpsExcludeOrIncludeQLabel)

        self.dumpsExcludeOrIncludeLabelContainerQFrameHSpacer = QSpacerItem(524, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dumpsExcludeOrIncludeLabelContainerQFrameHLayout.addItem(self.dumpsExcludeOrIncludeLabelContainerQFrameHSpacer)


        self.dumpsExcludeOrIncludeQFrameVLayout.addWidget(self.dumpsExcludeOrIncludeLabelContainerQFrame)

        self.dumpsExcludeOrIncludeLabelQFrame = QFrame(self.dumpsExcludeOrIncludeQFrame)
        self.dumpsExcludeOrIncludeLabelQFrame.setObjectName(u"dumpsExcludeOrIncludeLabelQFrame")
        self.dumpsExcludeOrIncludeLabelQFrameVLayout = QVBoxLayout(self.dumpsExcludeOrIncludeLabelQFrame)
        self.dumpsExcludeOrIncludeLabelQFrameVLayout.setSpacing(5)
        self.dumpsExcludeOrIncludeLabelQFrameVLayout.setObjectName(u"dumpsExcludeOrIncludeLabelQFrameVLayout")
        self.dumpsExcludeOrIncludeLabelQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsExcludeOrIncludeLineEditContainerQFrame = QFrame(self.dumpsExcludeOrIncludeLabelQFrame)
        self.dumpsExcludeOrIncludeLineEditContainerQFrame.setObjectName(u"dumpsExcludeOrIncludeLineEditContainerQFrame")
        self.dumpsExcludeOrIncludeLineEditContainerQFrameHLayout = QHBoxLayout(self.dumpsExcludeOrIncludeLineEditContainerQFrame)
        self.dumpsExcludeOrIncludeLineEditContainerQFrameHLayout.setSpacing(15)
        self.dumpsExcludeOrIncludeLineEditContainerQFrameHLayout.setObjectName(u"dumpsExcludeOrIncludeLineEditContainerQFrameHLayout")
        self.dumpsExcludeOrIncludeLineEditContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsExcludeOrIncludeQLineEdit = QLineEdit(self.dumpsExcludeOrIncludeLineEditContainerQFrame)
        self.dumpsExcludeOrIncludeQLineEdit.setObjectName(u"dumpsExcludeOrIncludeQLineEdit")

        self.dumpsExcludeOrIncludeLineEditContainerQFrameHLayout.addWidget(self.dumpsExcludeOrIncludeQLineEdit)


        self.dumpsExcludeOrIncludeLabelQFrameVLayout.addWidget(self.dumpsExcludeOrIncludeLineEditContainerQFrame)


        self.dumpsExcludeOrIncludeQFrameVLayout.addWidget(self.dumpsExcludeOrIncludeLabelQFrame)


        self.dumpsFormatKeysContainerQGroupBoxHLayout.addWidget(self.dumpsExcludeOrIncludeQFrame)

        self.dumpsGenerateQPushButton = QPushButton(self.dumpsFormatKeysContainerQGroupBox)
        self.dumpsGenerateQPushButton.setObjectName(u"dumpsGenerateQPushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dumpsGenerateQPushButton.sizePolicy().hasHeightForWidth())
        self.dumpsGenerateQPushButton.setSizePolicy(sizePolicy3)
        self.dumpsGenerateQPushButton.setStyleSheet(u"")

        self.dumpsFormatKeysContainerQGroupBoxHLayout.addWidget(self.dumpsGenerateQPushButton, 0, Qt.AlignBottom)

        self.dumpsSaveAndGenerateQPushButton = QPushButton(self.dumpsFormatKeysContainerQGroupBox)
        self.dumpsSaveAndGenerateQPushButton.setObjectName(u"dumpsSaveAndGenerateQPushButton")

        self.dumpsFormatKeysContainerQGroupBoxHLayout.addWidget(self.dumpsSaveAndGenerateQPushButton, 0, Qt.AlignBottom)


        self.dumpsPageQStackedWidgetVLayout.addWidget(self.dumpsFormatKeysContainerQGroupBox)

        self.hdwalletQStackedWidget.addWidget(self.dumpsPageQStackedWidget)

        self.hdwalletMainQFrameVLayout.addWidget(self.hdwalletQStackedWidget)


        self.hdWalletContainerQFrameVLayout.addWidget(self.hdwalletMainQFrame)

        self.hdWalletContainerQFrameVSpacerB = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.hdWalletContainerQFrameVLayout.addItem(self.hdWalletContainerQFrameVSpacerB)


        self.centralwidgetHLayout.addWidget(self.hdWalletContainerQFrame)

        self.outputQFrame = QFrame(self.centralwidget)
        self.outputQFrame.setObjectName(u"outputQFrame")
        self.outputQFrame.setMinimumSize(QSize(600, 0))
        self.outputQFrameVLayout = QVBoxLayout(self.outputQFrame)
        self.outputQFrameVLayout.setSpacing(0)
        self.outputQFrameVLayout.setObjectName(u"outputQFrameVLayout")
        self.outputQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.noLayoutQWidget = QWidget(self.outputQFrame)
        self.noLayoutQWidget.setObjectName(u"noLayoutQWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.noLayoutQWidget.sizePolicy().hasHeightForWidth())
        self.noLayoutQWidget.setSizePolicy(sizePolicy4)
        self.outputTerminalQWidget = QWidget(self.noLayoutQWidget)
        self.outputTerminalQWidget.setObjectName(u"outputTerminalQWidget")
        self.outputTerminalQWidget.setGeometry(QRect(0, 0, 601, 541))
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.outputTerminalQWidget.sizePolicy().hasHeightForWidth())
        self.outputTerminalQWidget.setSizePolicy(sizePolicy5)
        self.outputTerminalQFrameVLayout = QVBoxLayout(self.outputTerminalQWidget)
        self.outputTerminalQFrameVLayout.setSpacing(0)
        self.outputTerminalQFrameVLayout.setObjectName(u"outputTerminalQFrameVLayout")
        self.outputTerminalQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.outputTerminalQPlainTextEdit = QPlainTextEdit(self.outputTerminalQWidget)
        self.outputTerminalQPlainTextEdit.setObjectName(u"outputTerminalQPlainTextEdit")
        self.outputTerminalQPlainTextEdit.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.outputTerminalQPlainTextEdit.sizePolicy().hasHeightForWidth())
        self.outputTerminalQPlainTextEdit.setSizePolicy(sizePolicy5)
        self.outputTerminalQPlainTextEdit.setFrameShape(QFrame.NoFrame)
        self.outputTerminalQPlainTextEdit.setFrameShadow(QFrame.Plain)
        self.outputTerminalQPlainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.outputTerminalQPlainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.outputTerminalQPlainTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.outputTerminalQPlainTextEdit.setReadOnly(True)
        self.outputTerminalQPlainTextEdit.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.outputTerminalQPlainTextEdit.setMaximumBlockCount(2500)

        self.outputTerminalQFrameVLayout.addWidget(self.outputTerminalQPlainTextEdit)

        self.outputWidgetTopContainerQWidget = QWidget(self.noLayoutQWidget)
        self.outputWidgetTopContainerQWidget.setObjectName(u"outputWidgetTopContainerQWidget")
        self.outputWidgetTopContainerQWidget.setGeometry(QRect(0, 0, 600, 55))
        sizePolicy1.setHeightForWidth(self.outputWidgetTopContainerQWidget.sizePolicy().hasHeightForWidth())
        self.outputWidgetTopContainerQWidget.setSizePolicy(sizePolicy1)
        self.outputFrameTopContainerQFrameHLayout = QHBoxLayout(self.outputWidgetTopContainerQWidget)
        self.outputFrameTopContainerQFrameHLayout.setSpacing(15)
        self.outputFrameTopContainerQFrameHLayout.setObjectName(u"outputFrameTopContainerQFrameHLayout")
        self.outputFrameTopContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.outputWidgetTopContainerQFrame = QFrame(self.outputWidgetTopContainerQWidget)
        self.outputWidgetTopContainerQFrame.setObjectName(u"outputWidgetTopContainerQFrame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.outputWidgetTopContainerQFrame.sizePolicy().hasHeightForWidth())
        self.outputWidgetTopContainerQFrame.setSizePolicy(sizePolicy6)
        self.outputWidgetTopContainerQFrame.setMinimumSize(QSize(40, 0))
        self.outputWidgetTopContainerQFrameHLayout = QHBoxLayout(self.outputWidgetTopContainerQFrame)
        self.outputWidgetTopContainerQFrameHLayout.setSpacing(20)
        self.outputWidgetTopContainerQFrameHLayout.setObjectName(u"outputWidgetTopContainerQFrameHLayout")
        self.outputWidgetTopContainerQFrameHLayout.setContentsMargins(5, 15, 5, 15)
        self.expandAndCollapseTerminalQFrame = QFrame(self.outputWidgetTopContainerQFrame)
        self.expandAndCollapseTerminalQFrame.setObjectName(u"expandAndCollapseTerminalQFrame")
        self.expandAndCollapseTerminalQFrame.setMinimumSize(QSize(20, 20))
        self.expandAndCollapseTerminalQFrame.setMaximumSize(QSize(20, 20))
        self.expandAndCollapseTerminalQFrame.setFrameShape(QFrame.StyledPanel)
        self.expandAndCollapseTerminalQFrame.setFrameShadow(QFrame.Raised)
        self.expandAndCollapseTerminalQFrameVLayout = QVBoxLayout(self.expandAndCollapseTerminalQFrame)
        self.expandAndCollapseTerminalQFrameVLayout.setSpacing(0)
        self.expandAndCollapseTerminalQFrameVLayout.setObjectName(u"expandAndCollapseTerminalQFrameVLayout")
        self.expandAndCollapseTerminalQFrameVLayout.setContentsMargins(0, 0, 0, 0)

        self.outputWidgetTopContainerQFrameHLayout.addWidget(self.expandAndCollapseTerminalQFrame)


        self.outputFrameTopContainerQFrameHLayout.addWidget(self.outputWidgetTopContainerQFrame)


        self.outputQFrameVLayout.addWidget(self.noLayoutQWidget)

        self.outputTerminalActionQWidget = QWidget(self.outputQFrame)
        self.outputTerminalActionQWidget.setObjectName(u"outputTerminalActionQWidget")
        self.outputTerminalActionQWidgetHLayout = QHBoxLayout(self.outputTerminalActionQWidget)
        self.outputTerminalActionQWidgetHLayout.setSpacing(15)
        self.outputTerminalActionQWidgetHLayout.setObjectName(u"outputTerminalActionQWidgetHLayout")
        self.outputTerminalActionQWidgetHLayout.setContentsMargins(15, 10, 15, 15)
        self.outputTerminalQLineEdit = HistoryLineEdit(self.outputTerminalActionQWidget)
        self.outputTerminalQLineEdit.setObjectName(u"outputTerminalQLineEdit")

        self.outputTerminalActionQWidgetHLayout.addWidget(self.outputTerminalQLineEdit)

        self.outputTerminalQPushButton = QPushButton(self.outputTerminalActionQWidget)
        self.outputTerminalQPushButton.setObjectName(u"outputTerminalQPushButton")

        self.outputTerminalActionQWidgetHLayout.addWidget(self.outputTerminalQPushButton)

        self.clearTerminalQPushButton = QPushButton(self.outputTerminalActionQWidget)
        self.clearTerminalQPushButton.setObjectName(u"clearTerminalQPushButton")

        self.outputTerminalActionQWidgetHLayout.addWidget(self.clearTerminalQPushButton)


        self.outputQFrameVLayout.addWidget(self.outputTerminalActionQWidget)


        self.centralwidgetHLayout.addWidget(self.outputQFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.hdwalletQStackedWidget.setCurrentIndex(0)
        self.hdQStackedWidget.setCurrentIndex(1)
        self.bipQStackedWidget.setCurrentIndex(4)
        self.cardanoQStackedWidget.setCurrentIndex(4)
        self.electrumV1QStackedWidget.setCurrentIndex(2)
        self.electrumV2QStackedWidget.setCurrentIndex(0)
        self.moneroQStackedWidget.setCurrentIndex(5)
        self.derivationsQStackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.generateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.dumpQPushButton.setText(QCoreApplication.translate("MainWindow", u"Dumps", None))
        self.donationHDWalletQPushButton.setText(QCoreApplication.translate("MainWindow", u"Donation", None))
        self.helpHDWalletQPushButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.generateClientAndStrengthContainerQGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.generateEntropyClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.generateEntropyClientQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.generateEntropyStrengthQLabel.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.generateEntropyStrengthQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.generateEntropyClientAndStrengthQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.generateMnemonicClientWordsLanguageContainerQGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.generateMnemonicClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.generateMnemonicClientQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.generateMnemonicFromQLabel.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.generateMnemonicWordsQRadioButton.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.generateMnemonicEntropyQRadioButton.setText(QCoreApplication.translate("MainWindow", u"Entopy", None))
        self.generateMnemonicTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic Type", None))
        self.generateMnemonicTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.generateMnemonicLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.generateMnemonicLanguageQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.generateMnemonicWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.generateMnemonicWordsQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.generateMnemonicEntropyLabelQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.generateMnemonicClientWordsAndLanguageQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.seedGroupBoxContainerQGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.generateSeedClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.generateSeedClientQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.generateSeedMnemonicTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic Type", None))
        self.generateSeedMnemonicTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.generateSeedCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.generateSeedCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.generateSeedMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.generateSeedPassphraseGenerateQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.generateSeedPassphraseGenerateQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.generateSeedPassphraseGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.generateLengthAndPassphraseQGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.generatePassphraseLowerCaseQCheckBox.setText(QCoreApplication.translate("MainWindow", u"Lower Case", None))
        self.generatePassphraseCharacterQCheckBox.setText(QCoreApplication.translate("MainWindow", u"Characters", None))
        self.generatePassphraseUpperCaseQCheckBox.setText(QCoreApplication.translate("MainWindow", u"Upper Case", None))
        self.generatePassphraseNumberQCheckBox.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.generateLengthQLabel.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.generatePassphraseQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.dumpsCryptocurrencyQLabel.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.dumpsCryptocurrencyQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Bitcoin", None))
        self.dumpsCryptocurrencyQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Qtum", None))

        self.dumpsCryptocurrencyQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.dumpsNetworkQLabel.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.dumpsNetworkQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Mainnet", None))
        self.dumpsNetworkQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Testnet", None))

        self.dumpsNetworkQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.dumpsHdListQLabel.setText(QCoreApplication.translate("MainWindow", u"HD", None))
        self.dumpsHdQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"BIP32", None))
        self.dumpsHdQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP44", None))
        self.dumpsHdQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"BIP49", None))
        self.dumpsHdQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"BIP84", None))
        self.dumpsHdQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"BIP86", None))
        self.dumpsHdQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"BIP141", None))
        self.dumpsHdQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.dumpsHdQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Electrum-V1", None))
        self.dumpsHdQComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Electrum-V2", None))
        self.dumpsHdQComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.dumpsHdQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.dumpsFromQLabel.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.dumpsFromQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.dumpsFromQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.dumpsFromQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Private key", None))
        self.dumpsFromQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Public key", None))
        self.dumpsFromQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Seed", None))
        self.dumpsFromQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"WIF", None))
        self.dumpsFromQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.dumpsFromQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"XPublic Key", None))

        self.dumpsFromQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.dumpsStackQGroupBox.setTitle("")
        self.bipFromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.bipFromEntropyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.bipFromEntropyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.bipFromEntropyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.bipFromEntropyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bipFromEntropyLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.bipFromEntropyLanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.bipFromEntropyLanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.bipFromEntropyLanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.bipFromEntropyLanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.bipFromEntropyLanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.bipFromEntropyLanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.bipFromEntropyLanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.bipFromEntropyLanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.bipFromEntropyPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.bipFromEntropyPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.bipFromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.bipFromMnemonicPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.bipFromMnemonicPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.bipFromMnemonicPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.bipFromMnemonicPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bipFromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.bipFromMnemonicPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.bipFromSeedsQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.bipFromSeedPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.bipFromSeedPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.bipFromSeedPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.bipFromSeedPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bipFromXPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.bipFromXPrivateKeyStrictQCheckBox.setText(QCoreApplication.translate("MainWindow", u"Strict", None))
        self.bipFromXPrivateKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.bipFromXPrivateKeyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.bipFromXPrivateKeyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.bipFromXPrivateKeyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bipFromXPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.bipFromXPublicKeyStrictQCheckBox.setText(QCoreApplication.translate("MainWindow", u"Strict", None))
        self.bipFromXPublicKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.bipFromXPublicKeyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.bipFromXPublicKeyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.bipFromXPublicKeyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bipFromWIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.bipFromWIFPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.bipFromWIFPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.bipFromWIFPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.bipFromWIFPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bipFromWIFBIP38PassphraseQCheckBox.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.bipFromPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.bipFromPrivateKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.bipFromPrivateKeyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.bipFromPrivateKeyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.bipFromPrivateKeyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bipFromPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.bipFromPublicKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.bipFromPublicKeyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.bipFromPublicKeyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.bipFromPublicKeyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.cardanoFromEntropyLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.cardanoFromEntropyLanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.cardanoFromEntropyLanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.cardanoFromEntropyLanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.cardanoFromEntropyLanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.cardanoFromEntropyLanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.cardanoFromEntropyLanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.cardanoFromEntropyLanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.cardanoFromEntropyLanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.cardanoFromEntropyLanguageQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromEntropyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromEntropyCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromEntropyStakingQLabel.setText(QCoreApplication.translate("MainWindow", u"Staking Public Key", None))
        self.cardanoFromEntropyPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.cardanoFromEntropyPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.cardanoFromEntropyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromEntropyAddressTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.cardanoFromMnemonicCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromMnemonicCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromMnemonicStakingQLabel.setText(QCoreApplication.translate("MainWindow", u"Staking Public Key", None))
        self.cardanoFromMnemonicAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromMnemonicAddressTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.cardanoFromMnemonicPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.cardanoFromSeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.cardanoFromSeedCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromSeedCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromSeedStakingQLabel.setText(QCoreApplication.translate("MainWindow", u"Staking Public Key", None))
        self.cardanoFromSeedAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromSeedAddressTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromSeedPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.cardanoFromSeedPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.cardanoFromXPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.cardanoFromXPrivateKeyStrictQCheckBox.setText(QCoreApplication.translate("MainWindow", u"Strict", None))
        self.cardanoFromXPrivateKeyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromXPrivateKeyStakingQLabel.setText(QCoreApplication.translate("MainWindow", u"Staking Public Key", None))
        self.cardanoFromXPrivateKeyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromXPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.cardanoFromXPublicKeyStrictQCheckBox.setText(QCoreApplication.translate("MainWindow", u"Strict", None))
        self.cardanoFromXPublicKeyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromXPublicKeyStakingQLabel.setText(QCoreApplication.translate("MainWindow", u"Staking Public Key", None))
        self.cardanoFromXPublicKeyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromXPublicKeyAddressTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromPrivateKeyContainerQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.cardanoFromPrivateKeyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromPrivateStakingQLabel.setText(QCoreApplication.translate("MainWindow", u"Staking Public Key", None))
        self.cardanoFromPrivateKeyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromPrivateKeyAddressTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.cardanoFromPublicKeyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromPublicKeyCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromPublicStakingQLabel.setText(QCoreApplication.translate("MainWindow", u"Staking Public Key", None))
        self.cardanoFromPublicKeyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromPublicKeyAddressTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV1FromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.electrumV1FromEntropyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV1FromEntropyLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.electrumV1FromEntropyLanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.electrumV1FromEntropyLanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.electrumV1FromEntropyLanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.electrumV1FromEntropyLanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.electrumV1FromEntropyLanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.electrumV1FromEntropyLanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.electrumV1FromEntropyLanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.electrumV1FromEntropyLanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.electrumV1FromEntropyLanguageQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV1FromEntropyPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.electrumV1FromEntropyPassphraseGenerateQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.electrumV1FromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.electrumV1FromMnemonicPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV1FromMnemonicLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.electrumV1FromMnemonicLanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.electrumV1FromMnemonicLanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.electrumV1FromMnemonicLanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.electrumV1FromMnemonicLanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.electrumV1FromMnemonicLanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.electrumV1FromMnemonicLanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.electrumV1FromMnemonicLanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.electrumV1FromMnemonicLanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.electrumV1FromMnemonicLanguageQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV1FromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.electrumV1FromMnemonicPassphraseGenerateQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.electrumV1FromSeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.electrumV1FromSeedPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV1FromClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV1FromClientQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV1FromWIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.electrumV1FromWIFPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromWIFPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV1FromWIFPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV1FromWIFPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV1FromWIFBIP38PassphraseQCheckBox.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.electrumV1FromPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.electrumV1FromPrivateKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV1FromPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.electrumV1FromPublicKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.electrumV2FromEntropyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromEntropyModeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.electrumV2FromEntropyModeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromEntropyLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.electrumV2FromEntropyLanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.electrumV2FromEntropyLanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.electrumV2FromEntropyLanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.electrumV2FromEntropyLanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.electrumV2FromEntropyLanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.electrumV2FromEntropyLanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.electrumV2FromEntropyLanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.electrumV2FromEntropyLanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.electrumV2FromEntropyLanguageQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromEntropyMnemonicTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic Type", None))
        self.electrumV2FromEntropyMnemonicTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromEntropyPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.electrumV2FromEntropyPassphraseGenerateQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.electrumV2FromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.electrumV2FromMnemonicMnemonicTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic Type", None))
        self.electrumV2FromMnemonicModeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.electrumV2FromMnemonicModeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromMnemonicPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.electrumV2FromMnemonicPassphraseGenerateQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.electrumV2FromSeedsQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.electrumV2FromSeedModeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.electrumV2FromSeedModeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromSeedPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromSeedPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV2FromSeedPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV2FromSeedPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.moneroFromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.moneroFromEntropyLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.moneroFromEntropyLanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.moneroFromEntropyLanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.moneroFromEntropyLanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.moneroFromEntropyLanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.moneroFromEntropyLanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.moneroFromEntropyLanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.moneroFromEntropyLanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.moneroFromEntropyLanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.moneroFromEntropyLanguageQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.moneroFromEntropyPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.moneroFromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.moneroFromMnemonicPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.moneroFromSeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.moneroFromSeedPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.moneroFromSpendPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Spend Private Key", None))
        self.moneroFromSpendPrivateKeyPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.moneroFromPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.moneroFromPrivateKeyPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.moneroFromWatchOnlyViewPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"View Private key", None))
        self.moneroFromWatchOnlySpendPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Spend Public Key", None))
        self.moneroFromWatchOnlyPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.derivationQGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Derivation", None))
        self.customTabQPushButton.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.bip44TabQPushButton.setText(QCoreApplication.translate("MainWindow", u"BIP44", None))
        self.bip49TabQPushButton.setText(QCoreApplication.translate("MainWindow", u"BIP49", None))
        self.bip84TabQPushButton.setText(QCoreApplication.translate("MainWindow", u"BIP84", None))
        self.bip86TabQPushButton.setText(QCoreApplication.translate("MainWindow", u"BIP86", None))
        self.bip141TabQPushButton.setText(QCoreApplication.translate("MainWindow", u"BIP141", None))
        self.cip1852TabQPushButton.setText(QCoreApplication.translate("MainWindow", u"CIP1852", None))
        self.electrumTabQPushButton.setText(QCoreApplication.translate("MainWindow", u"Electrum", None))
        self.moneroTabQPushButton.setText(QCoreApplication.translate("MainWindow", u"Monero", None))
        self.customPathQLabel.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.customPathQLineEdit.setText("")
        self.customPathQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"m/0'/0", None))
        self.customClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.customClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Custom", None))
        self.customClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Bitcoin Core", None))
        self.customClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"blockchain.info", None))
        self.customClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"MultiBit HD", None))
        self.customClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Coinomi, Ledger", None))

        self.customClientQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bip44PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.bip44PurposeQLineEdit.setText("")
        self.bip44PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"44", None))
        self.bip44CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.bip44CoinTypeQLineEdit.setText("")
        self.bip44CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip44AccountQLabel.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.bip44AccountQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip44AccountQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip44ChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.bip44ChangeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"External", None))
        self.bip44ChangeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internal", None))

        self.bip44ChangeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bip44AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.bip44AddressQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0-10", None))
        self.bip44AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip49PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.bip49PurposeQLineEdit.setText("")
        self.bip49PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"49", None))
        self.bip49CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.bip49CoinTypeQLineEdit.setText("")
        self.bip49CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip49AccountQLabel.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.bip49AccountQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip49AccountQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip49ChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.bip49ChangeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"External", None))
        self.bip49ChangeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internal", None))

        self.bip49ChangeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bip49AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.bip49AddressQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0-10", None))
        self.bip49AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip84PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.bip84PurposeQLineEdit.setText("")
        self.bip84PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"84", None))
        self.bip84CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.bip84CoinTypeQLineEdit.setText("")
        self.bip84CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip84AccountQLabel.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.bip84AccountQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip84AccountQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip84ChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.bip84ChangeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"External", None))
        self.bip84ChangeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internal", None))

        self.bip84ChangeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bip84AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.bip84AddressQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0-10", None))
        self.bip84AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip86PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.bip86PurposeQLineEdit.setText("")
        self.bip86PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"86", None))
        self.bip86CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.bip86CoinTypeQLineEdit.setText("")
        self.bip86CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip86AccountQLabel.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.bip86AccountQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip86AccountQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip86ChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.bip86ChangeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"External", None))
        self.bip86ChangeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internal", None))

        self.bip86ChangeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.bip86AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.bip86AddressQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0-10", None))
        self.bip86AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bip141PathQLabel.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.bip141PathQLineEdit.setText("")
        self.bip141PathQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"m/0'/0", None))
        self.bip141ScriptSemanticsQLabel.setText(QCoreApplication.translate("MainWindow", u"Script Semantics", None))
        self.bip141ScriptSemanticsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"P2WPKH", None))
        self.bip141ScriptSemanticsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"P2WPKH nested in P2SH", None))
        self.bip141ScriptSemanticsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"P2WSH (1-of-1 multisig)", None))
        self.bip141ScriptSemanticsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"P2WSH nested in P2SH (1-of-1 multisig)", None))

        self.bip141ScriptSemanticsQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cip1852PurposeQLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose", None))
        self.cip1852PurposeQLineEdit.setText("")
        self.cip1852PurposeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1852", None))
        self.cip1852CoinTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Coin Type", None))
        self.cip1852CoinTypeQLineEdit.setText("")
        self.cip1852CoinTypeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1815", None))
        self.cip1852AccountQLabel.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.cip1852AccountQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cip1852AccountQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cip1852ChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Role", None))
        self.cip1852ChangeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"External", None))
        self.cip1852ChangeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internal", None))
        self.cip1852ChangeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Staking", None))

        self.cip1852ChangeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cip1852AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.cip1852AddressQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0-10", None))
        self.cip1852AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.electrumChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.electrumChangeQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.electrumChangeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.electrumAddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.electrumAddressQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0-10", None))
        self.electrumAddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.moneroMinorQLabel.setText(QCoreApplication.translate("MainWindow", u"Minor", None))
        self.moneroMinorQLineEdit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.moneroMinorQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1", None))
        self.moneroMajorQLabel.setText(QCoreApplication.translate("MainWindow", u"Major", None))
        self.moneroMajorQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.moneroMajorQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.dumpsFormatQLabel.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.dumpsFormatQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"JSON", None))
        self.dumpsFormatQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CSV", None))

        self.dumpsFormatQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.dumpsExcludeOrIncludeQLabel.setText(QCoreApplication.translate("MainWindow", u"Exclude / Include", None))
        self.dumpsGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.dumpsSaveAndGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate And Save", None))
        self.outputTerminalQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Command Line Interface (CLI)", None))
        self.outputTerminalQPushButton.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.clearTerminalQPushButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

