# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hdwalletsvUdDA.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 637)
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
        self.hdWalletHeaderContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hdWalletHeaderContainerQFrameHLayout.addItem(self.hdWalletHeaderContainerQFrameHSpacer)

        self.generateQPushButton = QPushButton(self.hdWalletHeaderContainerQFrame)
        self.generateQPushButton.setObjectName(u"generateQPushButton")

        self.hdWalletHeaderContainerQFrameHLayout.addWidget(self.generateQPushButton)

        self.dumpQPushButton = QPushButton(self.hdWalletHeaderContainerQFrame)
        self.dumpQPushButton.setObjectName(u"dumpQPushButton")

        self.hdWalletHeaderContainerQFrameHLayout.addWidget(self.dumpQPushButton)

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
        self.generateMnemonicFromActionQFrameHLayout.setSpacing(0)
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
        self.generateMnemonicWordsContainerQFrame.setMaximumSize(QSize(100, 16777215))
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

        self.groupBox = QGroupBox(self.generatePageQStackedWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 15, 10, 10)
        self.generateSeedGenerateContainerQFrame = QFrame(self.groupBox)
        self.generateSeedGenerateContainerQFrame.setObjectName(u"generateSeedGenerateContainerQFrame")
        self.generateSeedGenerateContainerQFrame.setEnabled(True)
        self.generateLengthAndPassphraseQFrameHLayout_2 = QHBoxLayout(self.generateSeedGenerateContainerQFrame)
        self.generateLengthAndPassphraseQFrameHLayout_2.setSpacing(15)
        self.generateLengthAndPassphraseQFrameHLayout_2.setObjectName(u"generateLengthAndPassphraseQFrameHLayout_2")
        self.generateLengthAndPassphraseQFrameHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.generateSeedClientContainerQFrame = QFrame(self.generateSeedGenerateContainerQFrame)
        self.generateSeedClientContainerQFrame.setObjectName(u"generateSeedClientContainerQFrame")
        self.generateMnemonicClientContainerQFrameVLayout_2 = QVBoxLayout(self.generateSeedClientContainerQFrame)
        self.generateMnemonicClientContainerQFrameVLayout_2.setSpacing(5)
        self.generateMnemonicClientContainerQFrameVLayout_2.setObjectName(u"generateMnemonicClientContainerQFrameVLayout_2")
        self.generateMnemonicClientContainerQFrameVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.generateSeedClientQLabel = QLabel(self.generateSeedClientContainerQFrame)
        self.generateSeedClientQLabel.setObjectName(u"generateSeedClientQLabel")

        self.generateMnemonicClientContainerQFrameVLayout_2.addWidget(self.generateSeedClientQLabel)

        self.generateSeedClientQComboBox = QComboBox(self.generateSeedClientContainerQFrame)
        self.generateSeedClientQComboBox.setObjectName(u"generateSeedClientQComboBox")

        self.generateMnemonicClientContainerQFrameVLayout_2.addWidget(self.generateSeedClientQComboBox)


        self.generateLengthAndPassphraseQFrameHLayout_2.addWidget(self.generateSeedClientContainerQFrame)

        self.generateSeedMnemonicTypeContainerQFrame = QFrame(self.generateSeedGenerateContainerQFrame)
        self.generateSeedMnemonicTypeContainerQFrame.setObjectName(u"generateSeedMnemonicTypeContainerQFrame")
        self.generateMnemonicWordsContainerQFrameVLayout_2 = QVBoxLayout(self.generateSeedMnemonicTypeContainerQFrame)
        self.generateMnemonicWordsContainerQFrameVLayout_2.setSpacing(5)
        self.generateMnemonicWordsContainerQFrameVLayout_2.setObjectName(u"generateMnemonicWordsContainerQFrameVLayout_2")
        self.generateMnemonicWordsContainerQFrameVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.generateSeedMnemonicTypeQLabel = QLabel(self.generateSeedMnemonicTypeContainerQFrame)
        self.generateSeedMnemonicTypeQLabel.setObjectName(u"generateSeedMnemonicTypeQLabel")

        self.generateMnemonicWordsContainerQFrameVLayout_2.addWidget(self.generateSeedMnemonicTypeQLabel)

        self.generateSeedMnemonicTypeQComboBox = QComboBox(self.generateSeedMnemonicTypeContainerQFrame)
        self.generateSeedMnemonicTypeQComboBox.setObjectName(u"generateSeedMnemonicTypeQComboBox")

        self.generateMnemonicWordsContainerQFrameVLayout_2.addWidget(self.generateSeedMnemonicTypeQComboBox)


        self.generateLengthAndPassphraseQFrameHLayout_2.addWidget(self.generateSeedMnemonicTypeContainerQFrame)

        self.generateSeedCardanoTypeContainerQFrame = QFrame(self.generateSeedGenerateContainerQFrame)
        self.generateSeedCardanoTypeContainerQFrame.setObjectName(u"generateSeedCardanoTypeContainerQFrame")
        self.generateMnemonicLanguageContainerQFrameVLayout_2 = QVBoxLayout(self.generateSeedCardanoTypeContainerQFrame)
        self.generateMnemonicLanguageContainerQFrameVLayout_2.setSpacing(5)
        self.generateMnemonicLanguageContainerQFrameVLayout_2.setObjectName(u"generateMnemonicLanguageContainerQFrameVLayout_2")
        self.generateMnemonicLanguageContainerQFrameVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.generateSeedCardanoTypeQLabel = QLabel(self.generateSeedCardanoTypeContainerQFrame)
        self.generateSeedCardanoTypeQLabel.setObjectName(u"generateSeedCardanoTypeQLabel")

        self.generateMnemonicLanguageContainerQFrameVLayout_2.addWidget(self.generateSeedCardanoTypeQLabel)

        self.generateSeedCardanoTypeQComboBox = QComboBox(self.generateSeedCardanoTypeContainerQFrame)
        self.generateSeedCardanoTypeQComboBox.setObjectName(u"generateSeedCardanoTypeQComboBox")

        self.generateMnemonicLanguageContainerQFrameVLayout_2.addWidget(self.generateSeedCardanoTypeQComboBox)


        self.generateLengthAndPassphraseQFrameHLayout_2.addWidget(self.generateSeedCardanoTypeContainerQFrame)


        self.verticalLayout.addWidget(self.generateSeedGenerateContainerQFrame)

        self.generateSeedClientMnemonicContainerQFrame = QFrame(self.groupBox)
        self.generateSeedClientMnemonicContainerQFrame.setObjectName(u"generateSeedClientMnemonicContainerQFrame")
        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2 = QHBoxLayout(self.generateSeedClientMnemonicContainerQFrame)
        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.setSpacing(15)
        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.setObjectName(u"generateMnemonicClientWordsLanguageContainerQFrameHLayout_2")
        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.generateSeedMnemonicContainerQFrame = QFrame(self.generateSeedClientMnemonicContainerQFrame)
        self.generateSeedMnemonicContainerQFrame.setObjectName(u"generateSeedMnemonicContainerQFrame")
        self.generateSeedMnemonicContainerQFrame.setLineWidth(0)
        self.generateLengthContainerQFrameVLayout_3 = QVBoxLayout(self.generateSeedMnemonicContainerQFrame)
        self.generateLengthContainerQFrameVLayout_3.setSpacing(5)
        self.generateLengthContainerQFrameVLayout_3.setObjectName(u"generateLengthContainerQFrameVLayout_3")
        self.generateLengthContainerQFrameVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.generateSeedMnemonicLabelContainerQFrame = QFrame(self.generateSeedMnemonicContainerQFrame)
        self.generateSeedMnemonicLabelContainerQFrame.setObjectName(u"generateSeedMnemonicLabelContainerQFrame")
        self.generateSeedMnemonicLabelContainerQFrame.setEnabled(True)
        self.generateLengthLabelContainerQFrameHLayout_3 = QHBoxLayout(self.generateSeedMnemonicLabelContainerQFrame)
        self.generateLengthLabelContainerQFrameHLayout_3.setSpacing(15)
        self.generateLengthLabelContainerQFrameHLayout_3.setObjectName(u"generateLengthLabelContainerQFrameHLayout_3")
        self.generateLengthLabelContainerQFrameHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.generateSeedMnemonicQLabel = QLabel(self.generateSeedMnemonicLabelContainerQFrame)
        self.generateSeedMnemonicQLabel.setObjectName(u"generateSeedMnemonicQLabel")

        self.generateLengthLabelContainerQFrameHLayout_3.addWidget(self.generateSeedMnemonicQLabel)

        self.generateSeedMnemonicContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generateLengthLabelContainerQFrameHLayout_3.addItem(self.generateSeedMnemonicContainerQFrameHSpacer)


        self.generateLengthContainerQFrameVLayout_3.addWidget(self.generateSeedMnemonicLabelContainerQFrame)

        self.generateSeedMnemonicQLineEdit = QLineEdit(self.generateSeedMnemonicContainerQFrame)
        self.generateSeedMnemonicQLineEdit.setObjectName(u"generateSeedMnemonicQLineEdit")
        self.generateSeedMnemonicQLineEdit.setMinimumSize(QSize(350, 0))

        self.generateLengthContainerQFrameVLayout_3.addWidget(self.generateSeedMnemonicQLineEdit)


        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.addWidget(self.generateSeedMnemonicContainerQFrame)

        self.generateSeedPassphraseGenerateContainerQFrame = QFrame(self.generateSeedClientMnemonicContainerQFrame)
        self.generateSeedPassphraseGenerateContainerQFrame.setObjectName(u"generateSeedPassphraseGenerateContainerQFrame")
        self.generateSeedPassphraseGenerateContainerQFrame.setLineWidth(0)
        self.generateLengthContainerQFrameVLayout_2 = QVBoxLayout(self.generateSeedPassphraseGenerateContainerQFrame)
        self.generateLengthContainerQFrameVLayout_2.setSpacing(5)
        self.generateLengthContainerQFrameVLayout_2.setObjectName(u"generateLengthContainerQFrameVLayout_2")
        self.generateLengthContainerQFrameVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.generateSeedPassphraseGenerateLabelContainerQFrame = QFrame(self.generateSeedPassphraseGenerateContainerQFrame)
        self.generateSeedPassphraseGenerateLabelContainerQFrame.setObjectName(u"generateSeedPassphraseGenerateLabelContainerQFrame")
        self.generateSeedPassphraseGenerateLabelContainerQFrame.setEnabled(True)
        self.generateLengthLabelContainerQFrameHLayout_2 = QHBoxLayout(self.generateSeedPassphraseGenerateLabelContainerQFrame)
        self.generateLengthLabelContainerQFrameHLayout_2.setSpacing(15)
        self.generateLengthLabelContainerQFrameHLayout_2.setObjectName(u"generateLengthLabelContainerQFrameHLayout_2")
        self.generateLengthLabelContainerQFrameHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.generateSeedPassphraseGenerateQLabel = QLabel(self.generateSeedPassphraseGenerateLabelContainerQFrame)
        self.generateSeedPassphraseGenerateQLabel.setObjectName(u"generateSeedPassphraseGenerateQLabel")

        self.generateLengthLabelContainerQFrameHLayout_2.addWidget(self.generateSeedPassphraseGenerateQLabel)

        self.generateSeedPassphraseGenerateLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generateLengthLabelContainerQFrameHLayout_2.addItem(self.generateSeedPassphraseGenerateLabelContainerQFrameHSpacer)


        self.generateLengthContainerQFrameVLayout_2.addWidget(self.generateSeedPassphraseGenerateLabelContainerQFrame)

        self.generateSeedPassphraseGenerateQLineEdit = QLineEdit(self.generateSeedPassphraseGenerateContainerQFrame)
        self.generateSeedPassphraseGenerateQLineEdit.setObjectName(u"generateSeedPassphraseGenerateQLineEdit")

        self.generateLengthContainerQFrameVLayout_2.addWidget(self.generateSeedPassphraseGenerateQLineEdit)


        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.addWidget(self.generateSeedPassphraseGenerateContainerQFrame)

        self.generateSeedPassphraseGenerateQPushButton = QPushButton(self.generateSeedClientMnemonicContainerQFrame)
        self.generateSeedPassphraseGenerateQPushButton.setObjectName(u"generateSeedPassphraseGenerateQPushButton")

        self.generateMnemonicClientWordsLanguageContainerQFrameHLayout_2.addWidget(self.generateSeedPassphraseGenerateQPushButton, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.generateSeedClientMnemonicContainerQFrame)


        self.generatePageQStackedWidgetVLayout.addWidget(self.groupBox)

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
        self.verticalLayout_3 = QVBoxLayout(self.dumpsPageQStackedWidget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox = QGroupBox(self.dumpsPageQStackedWidget)
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox.setObjectName(u"dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox")
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout = QHBoxLayout(self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox)
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout.setSpacing(15)
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout.setObjectName(u"dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout")
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrameHLayout.setContentsMargins(10, 10, 10, 10)
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


        self.verticalLayout_3.addWidget(self.dumpsHDFromCryptocurrencyAndNetworkContainerQGroupBox)

        self.dumpsStackQGroupBox = QGroupBox(self.dumpsPageQStackedWidget)
        self.dumpsStackQGroupBox.setObjectName(u"dumpsStackQGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.dumpsStackQGroupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.hdQStackedWidget = QStackedWidget(self.dumpsStackQGroupBox)
        self.hdQStackedWidget.setObjectName(u"hdQStackedWidget")
        self.hdQStackedWidget.setLineWidth(0)
        self.BIPsPageQWidget = QWidget()
        self.BIPsPageQWidget.setObjectName(u"BIPsPageQWidget")
        self.BIPsPageQWidgetVLayout = QVBoxLayout(self.BIPsPageQWidget)
        self.BIPsPageQWidgetVLayout.setSpacing(0)
        self.BIPsPageQWidgetVLayout.setObjectName(u"BIPsPageQWidgetVLayout")
        self.BIPsPageQWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPQStackedWidget = QStackedWidget(self.BIPsPageQWidget)
        self.BIPQStackedWidget.setObjectName(u"BIPQStackedWidget")
        self.BIPFromEntropyQStackedWidget = QWidget()
        self.BIPFromEntropyQStackedWidget.setObjectName(u"BIPFromEntropyQStackedWidget")
        self.BIPFromEntropyQStackedWidgetVLayout = QVBoxLayout(self.BIPFromEntropyQStackedWidget)
        self.BIPFromEntropyQStackedWidgetVLayout.setSpacing(15)
        self.BIPFromEntropyQStackedWidgetVLayout.setObjectName(u"BIPFromEntropyQStackedWidgetVLayout")
        self.BIPFromEntropyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyContainerQFrame = QFrame(self.BIPFromEntropyQStackedWidget)
        self.BIPFromEntropyContainerQFrame.setObjectName(u"BIPFromEntropyContainerQFrame")
        self.BIPFromEntropyContainerQFrameVLayout = QVBoxLayout(self.BIPFromEntropyContainerQFrame)
        self.BIPFromEntropyContainerQFrameVLayout.setSpacing(5)
        self.BIPFromEntropyContainerQFrameVLayout.setObjectName(u"BIPFromEntropyContainerQFrameVLayout")
        self.BIPFromEntropyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyLabelContainerQFrame = QFrame(self.BIPFromEntropyContainerQFrame)
        self.BIPFromEntropyLabelContainerQFrame.setObjectName(u"BIPFromEntropyLabelContainerQFrame")
        self.BIPFromEntropyLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromEntropyLabelContainerQFrame)
        self.BIPFromEntropyLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromEntropyLabelContainerQFrameHLayout.setObjectName(u"BIPFromEntropyLabelContainerQFrameHLayout")
        self.BIPFromEntropyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyQLabel = QLabel(self.BIPFromEntropyLabelContainerQFrame)
        self.BIPFromEntropyQLabel.setObjectName(u"BIPFromEntropyQLabel")

        self.BIPFromEntropyLabelContainerQFrameHLayout.addWidget(self.BIPFromEntropyQLabel)

        self.BIPFromEntropyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromEntropyLabelContainerQFrameHLayout.addItem(self.BIPFromEntropyLabelContainerQFrameHSpacer)


        self.BIPFromEntropyContainerQFrameVLayout.addWidget(self.BIPFromEntropyLabelContainerQFrame)

        self.BIPFromEntropyEntAndGenerateContainerQFrame = QFrame(self.BIPFromEntropyContainerQFrame)
        self.BIPFromEntropyEntAndGenerateContainerQFrame.setObjectName(u"BIPFromEntropyEntAndGenerateContainerQFrame")
        self.BIPFromEntropyEntAndGenerateContainerQFrameHLayout = QHBoxLayout(self.BIPFromEntropyEntAndGenerateContainerQFrame)
        self.BIPFromEntropyEntAndGenerateContainerQFrameHLayout.setSpacing(15)
        self.BIPFromEntropyEntAndGenerateContainerQFrameHLayout.setObjectName(u"BIPFromEntropyEntAndGenerateContainerQFrameHLayout")
        self.BIPFromEntropyEntAndGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyGenerateQLineEdit = QLineEdit(self.BIPFromEntropyEntAndGenerateContainerQFrame)
        self.BIPFromEntropyGenerateQLineEdit.setObjectName(u"BIPFromEntropyGenerateQLineEdit")

        self.BIPFromEntropyEntAndGenerateContainerQFrameHLayout.addWidget(self.BIPFromEntropyGenerateQLineEdit)


        self.BIPFromEntropyContainerQFrameVLayout.addWidget(self.BIPFromEntropyEntAndGenerateContainerQFrame)


        self.BIPFromEntropyQStackedWidgetVLayout.addWidget(self.BIPFromEntropyContainerQFrame)

        self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame = QFrame(self.BIPFromEntropyQStackedWidget)
        self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame.setObjectName(u"BIPFromEntropyPublicKeyAndPassphraseContainerQFrame")
        self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout = QHBoxLayout(self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame)
        self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.setSpacing(15)
        self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.setObjectName(u"BIPFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout")
        self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPublicKeyTypeContainerQFrame = QFrame(self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame)
        self.BIPFromEntropyPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromEntropyPublicKeyTypeContainerQFrame")
        self.BIPFromEntropyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.BIPFromEntropyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.BIPFromEntropyPublicKeyTypeContainerQFrame)
        self.BIPFromEntropyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.BIPFromEntropyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"BIPFromEntropyPublicKeyTypeContainerQFrameVLayout")
        self.BIPFromEntropyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromEntropyPublicKeyTypeContainerQFrame)
        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromEntropyPublicKeyTypeLabelContainerQFrame")
        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromEntropyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"BIPFromEntropyPublicKeyTypeLabelContainerQFrameHLayout")
        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPublicKeyTypeQLabel = QLabel(self.BIPFromEntropyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromEntropyPublicKeyTypeQLabel.setObjectName(u"BIPFromEntropyPublicKeyTypeQLabel")

        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.BIPFromEntropyPublicKeyTypeQLabel)

        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.BIPFromEntropyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.BIPFromEntropyPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromEntropyPublicKeyTypeLabelContainerQFrame)

        self.BIPFromEntropyPublicKeyTypeQComboBox = QComboBox(self.BIPFromEntropyPublicKeyTypeContainerQFrame)
        self.BIPFromEntropyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromEntropyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromEntropyPublicKeyTypeQComboBox.setObjectName(u"BIPFromEntropyPublicKeyTypeQComboBox")

        self.BIPFromEntropyPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromEntropyPublicKeyTypeQComboBox)


        self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.addWidget(self.BIPFromEntropyPublicKeyTypeContainerQFrame)

        self.BIPFromEntropyPassphraseContainerQFrame = QFrame(self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame)
        self.BIPFromEntropyPassphraseContainerQFrame.setObjectName(u"BIPFromEntropyPassphraseContainerQFrame")
        self.BIPFromEntropyPassphraseContainerQFrameVLayout = QVBoxLayout(self.BIPFromEntropyPassphraseContainerQFrame)
        self.BIPFromEntropyPassphraseContainerQFrameVLayout.setSpacing(5)
        self.BIPFromEntropyPassphraseContainerQFrameVLayout.setObjectName(u"BIPFromEntropyPassphraseContainerQFrameVLayout")
        self.BIPFromEntropyPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPassphraseLabelContainerQFrame = QFrame(self.BIPFromEntropyPassphraseContainerQFrame)
        self.BIPFromEntropyPassphraseLabelContainerQFrame.setObjectName(u"BIPFromEntropyPassphraseLabelContainerQFrame")
        self.BIPFromEntropyPassphraseLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromEntropyPassphraseLabelContainerQFrame)
        self.BIPFromEntropyPassphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromEntropyPassphraseLabelContainerQFrameHLayout.setObjectName(u"BIPFromEntropyPassphraseLabelContainerQFrameHLayout")
        self.BIPFromEntropyPassphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPassphraseQLabel = QLabel(self.BIPFromEntropyPassphraseLabelContainerQFrame)
        self.BIPFromEntropyPassphraseQLabel.setObjectName(u"BIPFromEntropyPassphraseQLabel")

        self.BIPFromEntropyPassphraseLabelContainerQFrameHLayout.addWidget(self.BIPFromEntropyPassphraseQLabel)

        self.BIPFromEntropyPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromEntropyPassphraseLabelContainerQFrameHLayout.addItem(self.BIPFromEntropyPassphraseLabelContainerQFrameHSpacer)


        self.BIPFromEntropyPassphraseContainerQFrameVLayout.addWidget(self.BIPFromEntropyPassphraseLabelContainerQFrame)

        self.BIPFromEntropyPassphraseGenerateContainerQFrame = QFrame(self.BIPFromEntropyPassphraseContainerQFrame)
        self.BIPFromEntropyPassphraseGenerateContainerQFrame.setObjectName(u"BIPFromEntropyPassphraseGenerateContainerQFrame")
        self.BIPFromEntropyPassphraseGenerateContainerQFrameHLayout = QHBoxLayout(self.BIPFromEntropyPassphraseGenerateContainerQFrame)
        self.BIPFromEntropyPassphraseGenerateContainerQFrameHLayout.setSpacing(15)
        self.BIPFromEntropyPassphraseGenerateContainerQFrameHLayout.setObjectName(u"BIPFromEntropyPassphraseGenerateContainerQFrameHLayout")
        self.BIPFromEntropyPassphraseGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPassphraseQLineEdit = QLineEdit(self.BIPFromEntropyPassphraseGenerateContainerQFrame)
        self.BIPFromEntropyPassphraseQLineEdit.setObjectName(u"BIPFromEntropyPassphraseQLineEdit")

        self.BIPFromEntropyPassphraseGenerateContainerQFrameHLayout.addWidget(self.BIPFromEntropyPassphraseQLineEdit)


        self.BIPFromEntropyPassphraseContainerQFrameVLayout.addWidget(self.BIPFromEntropyPassphraseGenerateContainerQFrame)


        self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrameHLayout.addWidget(self.BIPFromEntropyPassphraseContainerQFrame)


        self.BIPFromEntropyQStackedWidgetVLayout.addWidget(self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame)

        self.BIPFromEntropyLanguageAndWordsContainerQFrame = QFrame(self.BIPFromEntropyQStackedWidget)
        self.BIPFromEntropyLanguageAndWordsContainerQFrame.setObjectName(u"BIPFromEntropyLanguageAndWordsContainerQFrame")
        self.BIPFromEntropyLanguageAndWordsContainerQFrameHLayout = QHBoxLayout(self.BIPFromEntropyLanguageAndWordsContainerQFrame)
        self.BIPFromEntropyLanguageAndWordsContainerQFrameHLayout.setSpacing(15)
        self.BIPFromEntropyLanguageAndWordsContainerQFrameHLayout.setObjectName(u"BIPFromEntropyLanguageAndWordsContainerQFrameHLayout")
        self.BIPFromEntropyLanguageAndWordsContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyLanguageContainerQFrame = QFrame(self.BIPFromEntropyLanguageAndWordsContainerQFrame)
        self.BIPFromEntropyLanguageContainerQFrame.setObjectName(u"BIPFromEntropyLanguageContainerQFrame")
        self.BIPFromEntropyLanguageContainerQFrameVLayout = QVBoxLayout(self.BIPFromEntropyLanguageContainerQFrame)
        self.BIPFromEntropyLanguageContainerQFrameVLayout.setSpacing(5)
        self.BIPFromEntropyLanguageContainerQFrameVLayout.setObjectName(u"BIPFromEntropyLanguageContainerQFrameVLayout")
        self.BIPFromEntropyLanguageContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyLanguageLabelContainerQFrame = QFrame(self.BIPFromEntropyLanguageContainerQFrame)
        self.BIPFromEntropyLanguageLabelContainerQFrame.setObjectName(u"BIPFromEntropyLanguageLabelContainerQFrame")
        self.BIPFromEntropyLanguageLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromEntropyLanguageLabelContainerQFrame)
        self.BIPFromEntropyLanguageLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromEntropyLanguageLabelContainerQFrameHLayout.setObjectName(u"BIPFromEntropyLanguageLabelContainerQFrameHLayout")
        self.BIPFromEntropyLanguageLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyLanguageQLabel = QLabel(self.BIPFromEntropyLanguageLabelContainerQFrame)
        self.BIPFromEntropyLanguageQLabel.setObjectName(u"BIPFromEntropyLanguageQLabel")

        self.BIPFromEntropyLanguageLabelContainerQFrameHLayout.addWidget(self.BIPFromEntropyLanguageQLabel)

        self.BIPFromEntropyLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromEntropyLanguageLabelContainerQFrameHLayout.addItem(self.BIPFromEntropyLanguageLabelContainerQFrameHSpacer)


        self.BIPFromEntropyLanguageContainerQFrameVLayout.addWidget(self.BIPFromEntropyLanguageLabelContainerQFrame)

        self.BIPFromEntropyLanguageQComboBox = QComboBox(self.BIPFromEntropyLanguageContainerQFrame)
        self.BIPFromEntropyLanguageQComboBox.addItem("")
        self.BIPFromEntropyLanguageQComboBox.addItem("")
        self.BIPFromEntropyLanguageQComboBox.addItem("")
        self.BIPFromEntropyLanguageQComboBox.addItem("")
        self.BIPFromEntropyLanguageQComboBox.addItem("")
        self.BIPFromEntropyLanguageQComboBox.addItem("")
        self.BIPFromEntropyLanguageQComboBox.addItem("")
        self.BIPFromEntropyLanguageQComboBox.addItem("")
        self.BIPFromEntropyLanguageQComboBox.setObjectName(u"BIPFromEntropyLanguageQComboBox")

        self.BIPFromEntropyLanguageContainerQFrameVLayout.addWidget(self.BIPFromEntropyLanguageQComboBox)


        self.BIPFromEntropyLanguageAndWordsContainerQFrameHLayout.addWidget(self.BIPFromEntropyLanguageContainerQFrame)

        self.BIPFromEntropyWordsContainerQFrame = QFrame(self.BIPFromEntropyLanguageAndWordsContainerQFrame)
        self.BIPFromEntropyWordsContainerQFrame.setObjectName(u"BIPFromEntropyWordsContainerQFrame")
        self.BIPFromEntropyWordsContainerQFrameVLayout = QVBoxLayout(self.BIPFromEntropyWordsContainerQFrame)
        self.BIPFromEntropyWordsContainerQFrameVLayout.setSpacing(5)
        self.BIPFromEntropyWordsContainerQFrameVLayout.setObjectName(u"BIPFromEntropyWordsContainerQFrameVLayout")
        self.BIPFromEntropyWordsContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyWordsLabelContainerQFrame = QFrame(self.BIPFromEntropyWordsContainerQFrame)
        self.BIPFromEntropyWordsLabelContainerQFrame.setObjectName(u"BIPFromEntropyWordsLabelContainerQFrame")
        self.BIPFromEntropyWordsLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromEntropyWordsLabelContainerQFrame)
        self.BIPFromEntropyWordsLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromEntropyWordsLabelContainerQFrameHLayout.setObjectName(u"BIPFromEntropyWordsLabelContainerQFrameHLayout")
        self.BIPFromEntropyWordsLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyWordsQLabel = QLabel(self.BIPFromEntropyWordsLabelContainerQFrame)
        self.BIPFromEntropyWordsQLabel.setObjectName(u"BIPFromEntropyWordsQLabel")

        self.BIPFromEntropyWordsLabelContainerQFrameHLayout.addWidget(self.BIPFromEntropyWordsQLabel)

        self.BIPFromEntropyWordsLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromEntropyWordsLabelContainerQFrameHLayout.addItem(self.BIPFromEntropyWordsLabelContainerQFrameHSpacer)


        self.BIPFromEntropyWordsContainerQFrameVLayout.addWidget(self.BIPFromEntropyWordsLabelContainerQFrame)

        self.BIPFromEntropyWordsQComboBox = QComboBox(self.BIPFromEntropyWordsContainerQFrame)
        self.BIPFromEntropyWordsQComboBox.addItem("")
        self.BIPFromEntropyWordsQComboBox.addItem("")
        self.BIPFromEntropyWordsQComboBox.addItem("")
        self.BIPFromEntropyWordsQComboBox.addItem("")
        self.BIPFromEntropyWordsQComboBox.addItem("")
        self.BIPFromEntropyWordsQComboBox.setObjectName(u"BIPFromEntropyWordsQComboBox")

        self.BIPFromEntropyWordsContainerQFrameVLayout.addWidget(self.BIPFromEntropyWordsQComboBox)


        self.BIPFromEntropyLanguageAndWordsContainerQFrameHLayout.addWidget(self.BIPFromEntropyWordsContainerQFrame)


        self.BIPFromEntropyQStackedWidgetVLayout.addWidget(self.BIPFromEntropyLanguageAndWordsContainerQFrame)

        self.BIPQStackedWidget.addWidget(self.BIPFromEntropyQStackedWidget)
        self.BIPFromMnemonicQStackedWidget = QWidget()
        self.BIPFromMnemonicQStackedWidget.setObjectName(u"BIPFromMnemonicQStackedWidget")
        self.BIPFromMnemonicQStackedWidgetVLayout = QVBoxLayout(self.BIPFromMnemonicQStackedWidget)
        self.BIPFromMnemonicQStackedWidgetVLayout.setSpacing(15)
        self.BIPFromMnemonicQStackedWidgetVLayout.setObjectName(u"BIPFromMnemonicQStackedWidgetVLayout")
        self.BIPFromMnemonicQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicContainerQFrame = QFrame(self.BIPFromMnemonicQStackedWidget)
        self.BIPFromMnemonicContainerQFrame.setObjectName(u"BIPFromMnemonicContainerQFrame")
        self.BIPFromMnemonicContainerQFrameVLayout = QVBoxLayout(self.BIPFromMnemonicContainerQFrame)
        self.BIPFromMnemonicContainerQFrameVLayout.setSpacing(5)
        self.BIPFromMnemonicContainerQFrameVLayout.setObjectName(u"BIPFromMnemonicContainerQFrameVLayout")
        self.BIPFromMnemonicContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicLabelContainerQFrame = QFrame(self.BIPFromMnemonicContainerQFrame)
        self.BIPFromMnemonicLabelContainerQFrame.setObjectName(u"BIPFromMnemonicLabelContainerQFrame")
        self.BIPFromMnemonicLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromMnemonicLabelContainerQFrame)
        self.BIPFromMnemonicLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromMnemonicLabelContainerQFrameHLayout.setObjectName(u"BIPFromMnemonicLabelContainerQFrameHLayout")
        self.BIPFromMnemonicLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicQLabel = QLabel(self.BIPFromMnemonicLabelContainerQFrame)
        self.BIPFromMnemonicQLabel.setObjectName(u"BIPFromMnemonicQLabel")

        self.BIPFromMnemonicLabelContainerQFrameHLayout.addWidget(self.BIPFromMnemonicQLabel)

        self.BIPFromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromMnemonicLabelContainerQFrameHLayout.addItem(self.BIPFromMnemonicLabelContainerQFrameHSpacer)


        self.BIPFromMnemonicContainerQFrameVLayout.addWidget(self.BIPFromMnemonicLabelContainerQFrame)

        self.BIPFromMnemonicLabelGenerateContainerQFrame = QFrame(self.BIPFromMnemonicContainerQFrame)
        self.BIPFromMnemonicLabelGenerateContainerQFrame.setObjectName(u"BIPFromMnemonicLabelGenerateContainerQFrame")
        self.BIPFromMnemonicLabelGenerateContainerQFrameHLayout = QHBoxLayout(self.BIPFromMnemonicLabelGenerateContainerQFrame)
        self.BIPFromMnemonicLabelGenerateContainerQFrameHLayout.setSpacing(15)
        self.BIPFromMnemonicLabelGenerateContainerQFrameHLayout.setObjectName(u"BIPFromMnemonicLabelGenerateContainerQFrameHLayout")
        self.BIPFromMnemonicLabelGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicQLineEdit = QLineEdit(self.BIPFromMnemonicLabelGenerateContainerQFrame)
        self.BIPFromMnemonicQLineEdit.setObjectName(u"BIPFromMnemonicQLineEdit")

        self.BIPFromMnemonicLabelGenerateContainerQFrameHLayout.addWidget(self.BIPFromMnemonicQLineEdit)


        self.BIPFromMnemonicContainerQFrameVLayout.addWidget(self.BIPFromMnemonicLabelGenerateContainerQFrame)


        self.BIPFromMnemonicQStackedWidgetVLayout.addWidget(self.BIPFromMnemonicContainerQFrame)

        self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame = QFrame(self.BIPFromMnemonicQStackedWidget)
        self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame.setObjectName(u"BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame")
        self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout = QHBoxLayout(self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame)
        self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout.setSpacing(15)
        self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout.setObjectName(u"BIPFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout")
        self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPublicKeyTypeContainerQFrame = QFrame(self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame)
        self.BIPFromMnemonicPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromMnemonicPublicKeyTypeContainerQFrame")
        self.BIPFromMnemonicPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.BIPFromMnemonicPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.BIPFromMnemonicPublicKeyTypeContainerQFrame)
        self.BIPFromMnemonicPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.BIPFromMnemonicPublicKeyTypeContainerQFrameVLayout.setObjectName(u"BIPFromMnemonicPublicKeyTypeContainerQFrameVLayout")
        self.BIPFromMnemonicPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromMnemonicPublicKeyTypeContainerQFrame)
        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromMnemonicPublicKeyTypeLabelContainerQFrame")
        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout")
        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPublicKeyTypeQLabel = QLabel(self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.BIPFromMnemonicPublicKeyTypeQLabel.setObjectName(u"BIPFromMnemonicPublicKeyTypeQLabel")

        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.BIPFromMnemonicPublicKeyTypeQLabel)

        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer)


        self.BIPFromMnemonicPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrame)

        self.BIPFromMnemonicPublicKeyTypeQComboBox = QComboBox(self.BIPFromMnemonicPublicKeyTypeContainerQFrame)
        self.BIPFromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.BIPFromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.BIPFromMnemonicPublicKeyTypeQComboBox.setObjectName(u"BIPFromMnemonicPublicKeyTypeQComboBox")

        self.BIPFromMnemonicPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromMnemonicPublicKeyTypeQComboBox)


        self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout.addWidget(self.BIPFromMnemonicPublicKeyTypeContainerQFrame)

        self.BIPFromMnemonicPassphraseContainerQFrame = QFrame(self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame)
        self.BIPFromMnemonicPassphraseContainerQFrame.setObjectName(u"BIPFromMnemonicPassphraseContainerQFrame")
        self.BIPFromMnemonicPassphraseContainerQFrameVLayout = QVBoxLayout(self.BIPFromMnemonicPassphraseContainerQFrame)
        self.BIPFromMnemonicPassphraseContainerQFrameVLayout.setSpacing(5)
        self.BIPFromMnemonicPassphraseContainerQFrameVLayout.setObjectName(u"BIPFromMnemonicPassphraseContainerQFrameVLayout")
        self.BIPFromMnemonicPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPassphraseLabelContainerQFrame = QFrame(self.BIPFromMnemonicPassphraseContainerQFrame)
        self.BIPFromMnemonicPassphraseLabelContainerQFrame.setObjectName(u"BIPFromMnemonicPassphraseLabelContainerQFrame")
        self.BIPFromMnemonicPassphraseLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromMnemonicPassphraseLabelContainerQFrame)
        self.BIPFromMnemonicPassphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromMnemonicPassphraseLabelContainerQFrameHLayout.setObjectName(u"BIPFromMnemonicPassphraseLabelContainerQFrameHLayout")
        self.BIPFromMnemonicPassphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPassphraseQLabel = QLabel(self.BIPFromMnemonicPassphraseLabelContainerQFrame)
        self.BIPFromMnemonicPassphraseQLabel.setObjectName(u"BIPFromMnemonicPassphraseQLabel")

        self.BIPFromMnemonicPassphraseLabelContainerQFrameHLayout.addWidget(self.BIPFromMnemonicPassphraseQLabel)

        self.BIPFromMnemonicPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromMnemonicPassphraseLabelContainerQFrameHLayout.addItem(self.BIPFromMnemonicPassphraseLabelContainerQFrameHSpacer)


        self.BIPFromMnemonicPassphraseContainerQFrameVLayout.addWidget(self.BIPFromMnemonicPassphraseLabelContainerQFrame)

        self.BIPFromMnemonicPassphraseGeneratelContainerQFrame = QFrame(self.BIPFromMnemonicPassphraseContainerQFrame)
        self.BIPFromMnemonicPassphraseGeneratelContainerQFrame.setObjectName(u"BIPFromMnemonicPassphraseGeneratelContainerQFrame")
        self.BIPFromMnemonicPassphraseGeneratelContainerQFrameHLayout = QHBoxLayout(self.BIPFromMnemonicPassphraseGeneratelContainerQFrame)
        self.BIPFromMnemonicPassphraseGeneratelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromMnemonicPassphraseGeneratelContainerQFrameHLayout.setObjectName(u"BIPFromMnemonicPassphraseGeneratelContainerQFrameHLayout")
        self.BIPFromMnemonicPassphraseGeneratelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPassphraseQLineEdit = QLineEdit(self.BIPFromMnemonicPassphraseGeneratelContainerQFrame)
        self.BIPFromMnemonicPassphraseQLineEdit.setObjectName(u"BIPFromMnemonicPassphraseQLineEdit")

        self.BIPFromMnemonicPassphraseGeneratelContainerQFrameHLayout.addWidget(self.BIPFromMnemonicPassphraseQLineEdit)


        self.BIPFromMnemonicPassphraseContainerQFrameVLayout.addWidget(self.BIPFromMnemonicPassphraseGeneratelContainerQFrame)


        self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrameHLayout.addWidget(self.BIPFromMnemonicPassphraseContainerQFrame)


        self.BIPFromMnemonicQStackedWidgetVLayout.addWidget(self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame)

        self.BIPFromMnemonicQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.BIPFromMnemonicQStackedWidgetVLayout.addItem(self.BIPFromMnemonicQStackedWidgetVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromMnemonicQStackedWidget)
        self.BIPFromSeedQStackedWidget = QWidget()
        self.BIPFromSeedQStackedWidget.setObjectName(u"BIPFromSeedQStackedWidget")
        self.BIPFromSeedQStackedWidgetVLayout = QVBoxLayout(self.BIPFromSeedQStackedWidget)
        self.BIPFromSeedQStackedWidgetVLayout.setSpacing(15)
        self.BIPFromSeedQStackedWidgetVLayout.setObjectName(u"BIPFromSeedQStackedWidgetVLayout")
        self.BIPFromSeedQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedContainerQFrame = QFrame(self.BIPFromSeedQStackedWidget)
        self.BIPFromSeedContainerQFrame.setObjectName(u"BIPFromSeedContainerQFrame")
        self.BIPFromSeedContainerQFrame.setMinimumSize(QSize(400, 0))
        self.BIPFromSeedContainerQFrameVLayout = QVBoxLayout(self.BIPFromSeedContainerQFrame)
        self.BIPFromSeedContainerQFrameVLayout.setSpacing(5)
        self.BIPFromSeedContainerQFrameVLayout.setObjectName(u"BIPFromSeedContainerQFrameVLayout")
        self.BIPFromSeedContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedAndPublicKeyTypeContainerQFrame = QFrame(self.BIPFromSeedContainerQFrame)
        self.BIPFromSeedAndPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromSeedAndPublicKeyTypeContainerQFrame")
        self.BIPFromSeedAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.BIPFromSeedAndPublicKeyTypeContainerQFrame)
        self.BIPFromSeedAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.BIPFromSeedAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"BIPFromSeedAndPublicKeyTypeContainerQFrameHLayout")
        self.BIPFromSeedAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedsContainerQFrame = QFrame(self.BIPFromSeedAndPublicKeyTypeContainerQFrame)
        self.BIPFromSeedsContainerQFrame.setObjectName(u"BIPFromSeedsContainerQFrame")
        self.BIPFromSeedsContainerQFrameVLayout = QVBoxLayout(self.BIPFromSeedsContainerQFrame)
        self.BIPFromSeedsContainerQFrameVLayout.setSpacing(5)
        self.BIPFromSeedsContainerQFrameVLayout.setObjectName(u"BIPFromSeedsContainerQFrameVLayout")
        self.BIPFromSeedsContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedsLabelContainerQFrame = QFrame(self.BIPFromSeedsContainerQFrame)
        self.BIPFromSeedsLabelContainerQFrame.setObjectName(u"BIPFromSeedsLabelContainerQFrame")
        self.BIPFromSeedsLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromSeedsLabelContainerQFrame)
        self.BIPFromSeedsLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromSeedsLabelContainerQFrameHLayout.setObjectName(u"BIPFromSeedsLabelContainerQFrameHLayout")
        self.BIPFromSeedsLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedsQLabel = QLabel(self.BIPFromSeedsLabelContainerQFrame)
        self.BIPFromSeedsQLabel.setObjectName(u"BIPFromSeedsQLabel")

        self.BIPFromSeedsLabelContainerQFrameHLayout.addWidget(self.BIPFromSeedsQLabel)

        self.BIPFromSeedsLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromSeedsLabelContainerQFrameHLayout.addItem(self.BIPFromSeedsLabelContainerQFrameHSpacer)


        self.BIPFromSeedsContainerQFrameVLayout.addWidget(self.BIPFromSeedsLabelContainerQFrame)

        self.BIPFromSeedsQLineEdit = QLineEdit(self.BIPFromSeedsContainerQFrame)
        self.BIPFromSeedsQLineEdit.setObjectName(u"BIPFromSeedsQLineEdit")

        self.BIPFromSeedsContainerQFrameVLayout.addWidget(self.BIPFromSeedsQLineEdit)


        self.BIPFromSeedAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.BIPFromSeedsContainerQFrame)

        self.BIPFromSeedPublicKeyTypeContainerQFrame = QFrame(self.BIPFromSeedAndPublicKeyTypeContainerQFrame)
        self.BIPFromSeedPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromSeedPublicKeyTypeContainerQFrame")
        self.BIPFromSeedPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.BIPFromSeedPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.BIPFromSeedPublicKeyTypeContainerQFrame)
        self.BIPFromSeedPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.BIPFromSeedPublicKeyTypeContainerQFrameVLayout.setObjectName(u"BIPFromSeedPublicKeyTypeContainerQFrameVLayout")
        self.BIPFromSeedPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromSeedPublicKeyTypeContainerQFrame)
        self.BIPFromSeedPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromSeedPublicKeyTypeLabelContainerQFrame")
        self.BIPFromSeedPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromSeedPublicKeyTypeLabelContainerQFrame)
        self.BIPFromSeedPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromSeedPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"BIPFromSeedPublicKeyTypeLabelContainerQFrameHLayout")
        self.BIPFromSeedPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedPublicKeyTypeQLabel = QLabel(self.BIPFromSeedPublicKeyTypeLabelContainerQFrame)
        self.BIPFromSeedPublicKeyTypeQLabel.setObjectName(u"BIPFromSeedPublicKeyTypeQLabel")

        self.BIPFromSeedPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.BIPFromSeedPublicKeyTypeQLabel)

        self.BIPFromSeedPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromSeedPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.BIPFromSeedPublicKeyTypeLabelContainerQFrameHSpacer)


        self.BIPFromSeedPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromSeedPublicKeyTypeLabelContainerQFrame)

        self.BIPFromSeedPublicKeyTypeQComboBox = QComboBox(self.BIPFromSeedPublicKeyTypeContainerQFrame)
        self.BIPFromSeedPublicKeyTypeQComboBox.addItem("")
        self.BIPFromSeedPublicKeyTypeQComboBox.addItem("")
        self.BIPFromSeedPublicKeyTypeQComboBox.setObjectName(u"BIPFromSeedPublicKeyTypeQComboBox")

        self.BIPFromSeedPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromSeedPublicKeyTypeQComboBox)


        self.BIPFromSeedAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.BIPFromSeedPublicKeyTypeContainerQFrame)


        self.BIPFromSeedContainerQFrameVLayout.addWidget(self.BIPFromSeedAndPublicKeyTypeContainerQFrame)

        self.BIPFromSeedContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.BIPFromSeedContainerQFrameVLayout.addItem(self.BIPFromSeedContainerQFrameVSpacer)


        self.BIPFromSeedQStackedWidgetVLayout.addWidget(self.BIPFromSeedContainerQFrame)

        self.BIPQStackedWidget.addWidget(self.BIPFromSeedQStackedWidget)
        self.BIPFromXPrivateKeyQStackedWidget = QWidget()
        self.BIPFromXPrivateKeyQStackedWidget.setObjectName(u"BIPFromXPrivateKeyQStackedWidget")
        self.BIPFromXPrivateKeyQStackedWidgetVLayout = QVBoxLayout(self.BIPFromXPrivateKeyQStackedWidget)
        self.BIPFromXPrivateKeyQStackedWidgetVLayout.setSpacing(15)
        self.BIPFromXPrivateKeyQStackedWidgetVLayout.setObjectName(u"BIPFromXPrivateKeyQStackedWidgetVLayout")
        self.BIPFromXPrivateKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame = QFrame(self.BIPFromXPrivateKeyQStackedWidget)
        self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame.setObjectName(u"BIPFromXPrivateKeyAndPublicKeyTypeQFrame")
        self.BIPFromXPrivateKeyAndPublicKeyTypeQFrameHLayout = QHBoxLayout(self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame)
        self.BIPFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.setSpacing(15)
        self.BIPFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.setObjectName(u"BIPFromXPrivateKeyAndPublicKeyTypeQFrameHLayout")
        self.BIPFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyContainerQFrame = QFrame(self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame)
        self.BIPFromXPrivateKeyContainerQFrame.setObjectName(u"BIPFromXPrivateKeyContainerQFrame")
        self.BIPFromXPrivateKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.BIPFromXPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.BIPFromXPrivateKeyContainerQFrame)
        self.BIPFromXPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.BIPFromXPrivateKeyContainerQFrameVLayout.setObjectName(u"BIPFromXPrivateKeyContainerQFrameVLayout")
        self.BIPFromXPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyLabelContainerQFrame = QFrame(self.BIPFromXPrivateKeyContainerQFrame)
        self.BIPFromXPrivateKeyLabelContainerQFrame.setObjectName(u"BIPFromXPrivateKeyLabelContainerQFrame")
        self.BIPFromXPrivateKeyLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromXPrivateKeyLabelContainerQFrame)
        self.BIPFromXPrivateKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromXPrivateKeyLabelContainerQFrameHLayout.setObjectName(u"BIPFromXPrivateKeyLabelContainerQFrameHLayout")
        self.BIPFromXPrivateKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyQLabel = QLabel(self.BIPFromXPrivateKeyLabelContainerQFrame)
        self.BIPFromXPrivateKeyQLabel.setObjectName(u"BIPFromXPrivateKeyQLabel")

        self.BIPFromXPrivateKeyLabelContainerQFrameHLayout.addWidget(self.BIPFromXPrivateKeyQLabel)

        self.BIPFromXPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromXPrivateKeyLabelContainerQFrameHLayout.addItem(self.BIPFromXPrivateKeyLabelContainerQFrameHSpacer)


        self.BIPFromXPrivateKeyContainerQFrameVLayout.addWidget(self.BIPFromXPrivateKeyLabelContainerQFrame)

        self.BIPFromXPrivateKeyQLineEdit = QLineEdit(self.BIPFromXPrivateKeyContainerQFrame)
        self.BIPFromXPrivateKeyQLineEdit.setObjectName(u"BIPFromXPrivateKeyQLineEdit")

        self.BIPFromXPrivateKeyContainerQFrameVLayout.addWidget(self.BIPFromXPrivateKeyQLineEdit)


        self.BIPFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.addWidget(self.BIPFromXPrivateKeyContainerQFrame)

        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame = QFrame(self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame)
        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromXPrivateKeyPublicKeyTypeContainerQFrame")
        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame)
        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"BIPFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout")
        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame)
        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame")
        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout")
        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyPublicKeyTypeQLabel = QLabel(self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromXPrivateKeyPublicKeyTypeQLabel.setObjectName(u"BIPFromXPrivateKeyPublicKeyTypeQLabel")

        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.BIPFromXPrivateKeyPublicKeyTypeQLabel)

        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame)

        self.BIPFromXPrivateKeyPublicKeyTypeQComboBox = QComboBox(self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame)
        self.BIPFromXPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromXPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromXPrivateKeyPublicKeyTypeQComboBox.setObjectName(u"BIPFromXPrivateKeyPublicKeyTypeQComboBox")

        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromXPrivateKeyPublicKeyTypeQComboBox)


        self.BIPFromXPrivateKeyAndPublicKeyTypeQFrameHLayout.addWidget(self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame)


        self.BIPFromXPrivateKeyQStackedWidgetVLayout.addWidget(self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame)

        self.BIPFromXPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.BIPFromXPrivateKeyQStackedWidgetVLayout.addItem(self.BIPFromXPrivateKeyQStackedWidgetVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromXPrivateKeyQStackedWidget)
        self.BIPFromXPublicKeyQStackedWidget = QWidget()
        self.BIPFromXPublicKeyQStackedWidget.setObjectName(u"BIPFromXPublicKeyQStackedWidget")
        self.BIPFromXPublicKeyQStackedWidgetVLayout = QVBoxLayout(self.BIPFromXPublicKeyQStackedWidget)
        self.BIPFromXPublicKeyQStackedWidgetVLayout.setSpacing(15)
        self.BIPFromXPublicKeyQStackedWidgetVLayout.setObjectName(u"BIPFromXPublicKeyQStackedWidgetVLayout")
        self.BIPFromXPublicKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame = QFrame(self.BIPFromXPublicKeyQStackedWidget)
        self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame")
        self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"BIPFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout")
        self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyContainerQFrame = QFrame(self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromXPublicKeyContainerQFrame.setObjectName(u"BIPFromXPublicKeyContainerQFrame")
        self.BIPFromXPublicKeyContainerQFrameVLayout = QVBoxLayout(self.BIPFromXPublicKeyContainerQFrame)
        self.BIPFromXPublicKeyContainerQFrameVLayout.setSpacing(5)
        self.BIPFromXPublicKeyContainerQFrameVLayout.setObjectName(u"BIPFromXPublicKeyContainerQFrameVLayout")
        self.BIPFromXPublicKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyLabelContainerQFrame = QFrame(self.BIPFromXPublicKeyContainerQFrame)
        self.BIPFromXPublicKeyLabelContainerQFrame.setObjectName(u"BIPFromXPublicKeyLabelContainerQFrame")
        self.BIPFromXPublicKeyLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromXPublicKeyLabelContainerQFrame)
        self.BIPFromXPublicKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromXPublicKeyLabelContainerQFrameHLayout.setObjectName(u"BIPFromXPublicKeyLabelContainerQFrameHLayout")
        self.BIPFromXPublicKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyQLabel = QLabel(self.BIPFromXPublicKeyLabelContainerQFrame)
        self.BIPFromXPublicKeyQLabel.setObjectName(u"BIPFromXPublicKeyQLabel")

        self.BIPFromXPublicKeyLabelContainerQFrameHLayout.addWidget(self.BIPFromXPublicKeyQLabel)

        self.BIPFromXPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromXPublicKeyLabelContainerQFrameHLayout.addItem(self.BIPFromXPublicKeyLabelContainerQFrameHSpacer)


        self.BIPFromXPublicKeyContainerQFrameVLayout.addWidget(self.BIPFromXPublicKeyLabelContainerQFrame)

        self.BIPFromXPublicKeyQLineEdit = QLineEdit(self.BIPFromXPublicKeyContainerQFrame)
        self.BIPFromXPublicKeyQLineEdit.setObjectName(u"BIPFromXPublicKeyQLineEdit")

        self.BIPFromXPublicKeyContainerQFrameVLayout.addWidget(self.BIPFromXPublicKeyQLineEdit)


        self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.BIPFromXPublicKeyContainerQFrame)

        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame = QFrame(self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromXPublicKeyPublicKeyTypeContainerQFrame")
        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame)
        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"BIPFromXPublicKeyPublicKeyTypeContainerQFrameVLayout")
        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame)
        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame")
        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout")
        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyPublicKeyTypeQLabel = QLabel(self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromXPublicKeyPublicKeyTypeQLabel.setObjectName(u"BIPFromXPublicKeyPublicKeyTypeQLabel")

        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.BIPFromXPublicKeyPublicKeyTypeQLabel)

        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame)

        self.BIPFromXPublicKeyPublicKeyTypeQComboBox = QComboBox(self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame)
        self.BIPFromXPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromXPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromXPublicKeyPublicKeyTypeQComboBox.setObjectName(u"BIPFromXPublicKeyPublicKeyTypeQComboBox")

        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromXPublicKeyPublicKeyTypeQComboBox)


        self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame)


        self.BIPFromXPublicKeyQStackedWidgetVLayout.addWidget(self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame)

        self.BIPFromXPublicKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.BIPFromXPublicKeyQStackedWidgetVLayout.addItem(self.BIPFromXPublicKeyQStackedWidgetVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromXPublicKeyQStackedWidget)
        self.BIPFromWIFQStackedWidget = QWidget()
        self.BIPFromWIFQStackedWidget.setObjectName(u"BIPFromWIFQStackedWidget")
        self.BIPFromWIFQStackedWidgetVLayout = QVBoxLayout(self.BIPFromWIFQStackedWidget)
        self.BIPFromWIFQStackedWidgetVLayout.setSpacing(15)
        self.BIPFromWIFQStackedWidgetVLayout.setObjectName(u"BIPFromWIFQStackedWidgetVLayout")
        self.BIPFromWIFQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFContainerQFrame = QFrame(self.BIPFromWIFQStackedWidget)
        self.BIPFromWIFContainerQFrame.setObjectName(u"BIPFromWIFContainerQFrame")
        self.BIPFromWIFContainerQFrame.setMinimumSize(QSize(400, 0))
        self.BIPFromWIFContainerQFrameVLayout = QVBoxLayout(self.BIPFromWIFContainerQFrame)
        self.BIPFromWIFContainerQFrameVLayout.setSpacing(5)
        self.BIPFromWIFContainerQFrameVLayout.setObjectName(u"BIPFromWIFContainerQFrameVLayout")
        self.BIPFromWIFContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFLabelContainerQFrame = QFrame(self.BIPFromWIFContainerQFrame)
        self.BIPFromWIFLabelContainerQFrame.setObjectName(u"BIPFromWIFLabelContainerQFrame")
        self.BIPFromWIFLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromWIFLabelContainerQFrame)
        self.BIPFromWIFLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromWIFLabelContainerQFrameHLayout.setObjectName(u"BIPFromWIFLabelContainerQFrameHLayout")
        self.BIPFromWIFLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFQLabel = QLabel(self.BIPFromWIFLabelContainerQFrame)
        self.BIPFromWIFQLabel.setObjectName(u"BIPFromWIFQLabel")

        self.BIPFromWIFLabelContainerQFrameHLayout.addWidget(self.BIPFromWIFQLabel)

        self.BIPFromWIFLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromWIFLabelContainerQFrameHLayout.addItem(self.BIPFromWIFLabelContainerQFrameHSpacer)


        self.BIPFromWIFContainerQFrameVLayout.addWidget(self.BIPFromWIFLabelContainerQFrame)

        self.BIPFromWIFQLineEdit = QLineEdit(self.BIPFromWIFContainerQFrame)
        self.BIPFromWIFQLineEdit.setObjectName(u"BIPFromWIFQLineEdit")

        self.BIPFromWIFContainerQFrameVLayout.addWidget(self.BIPFromWIFQLineEdit)


        self.BIPFromWIFQStackedWidgetVLayout.addWidget(self.BIPFromWIFContainerQFrame)

        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame = QFrame(self.BIPFromWIFQStackedWidget)
        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame.setObjectName(u"BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame")
        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout = QHBoxLayout(self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)
        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout.setSpacing(15)
        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout.setObjectName(u"BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout")
        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFPublicKeyTypeContainerQFrame = QFrame(self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)
        self.BIPFromWIFPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromWIFPublicKeyTypeContainerQFrame")
        self.BIPFromWIFPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.BIPFromWIFPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.BIPFromWIFPublicKeyTypeContainerQFrame)
        self.BIPFromWIFPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.BIPFromWIFPublicKeyTypeContainerQFrameVLayout.setObjectName(u"BIPFromWIFPublicKeyTypeContainerQFrameVLayout")
        self.BIPFromWIFPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromWIFPublicKeyTypeContainerQFrame)
        self.BIPFromWIFPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromWIFPublicKeyTypeLabelContainerQFrame")
        self.BIPFromWIFPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromWIFPublicKeyTypeLabelContainerQFrame)
        self.BIPFromWIFPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromWIFPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"BIPFromWIFPublicKeyTypeLabelContainerQFrameHLayout")
        self.BIPFromWIFPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFPublicKeyTypeQLabel = QLabel(self.BIPFromWIFPublicKeyTypeLabelContainerQFrame)
        self.BIPFromWIFPublicKeyTypeQLabel.setObjectName(u"BIPFromWIFPublicKeyTypeQLabel")

        self.BIPFromWIFPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.BIPFromWIFPublicKeyTypeQLabel)

        self.BIPFromWIFPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromWIFPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.BIPFromWIFPublicKeyTypeLabelContainerQFrameHSpacer)


        self.BIPFromWIFPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromWIFPublicKeyTypeLabelContainerQFrame)

        self.BIPFromWIFPublicKeyTypeQComboBox = QComboBox(self.BIPFromWIFPublicKeyTypeContainerQFrame)
        self.BIPFromWIFPublicKeyTypeQComboBox.addItem("")
        self.BIPFromWIFPublicKeyTypeQComboBox.addItem("")
        self.BIPFromWIFPublicKeyTypeQComboBox.setObjectName(u"BIPFromWIFPublicKeyTypeQComboBox")

        self.BIPFromWIFPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromWIFPublicKeyTypeQComboBox)


        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout.addWidget(self.BIPFromWIFPublicKeyTypeContainerQFrame)

        self.BIPFromWIFBIP38PassphraseContainerQFrame = QFrame(self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)
        self.BIPFromWIFBIP38PassphraseContainerQFrame.setObjectName(u"BIPFromWIFBIP38PassphraseContainerQFrame")
        self.BIPFromWIFBIP38PassphraseContainerQFrameVLayout = QVBoxLayout(self.BIPFromWIFBIP38PassphraseContainerQFrame)
        self.BIPFromWIFBIP38PassphraseContainerQFrameVLayout.setSpacing(5)
        self.BIPFromWIFBIP38PassphraseContainerQFrameVLayout.setObjectName(u"BIPFromWIFBIP38PassphraseContainerQFrameVLayout")
        self.BIPFromWIFBIP38PassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame = QFrame(self.BIPFromWIFBIP38PassphraseContainerQFrame)
        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame.setObjectName(u"BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame")
        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout = QHBoxLayout(self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame)
        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.setSpacing(15)
        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.setObjectName(u"BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout")
        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFBIP38PassphraseQCheckBox = QCheckBox(self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame)
        self.BIPFromWIFBIP38PassphraseQCheckBox.setObjectName(u"BIPFromWIFBIP38PassphraseQCheckBox")

        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.addWidget(self.BIPFromWIFBIP38PassphraseQCheckBox)

        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHLayout.addItem(self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHSpacer)


        self.BIPFromWIFBIP38PassphraseContainerQFrameVLayout.addWidget(self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame)

        self.BIPFromWIFBIP38PassphraseQLineEdit = QLineEdit(self.BIPFromWIFBIP38PassphraseContainerQFrame)
        self.BIPFromWIFBIP38PassphraseQLineEdit.setObjectName(u"BIPFromWIFBIP38PassphraseQLineEdit")

        self.BIPFromWIFBIP38PassphraseContainerQFrameVLayout.addWidget(self.BIPFromWIFBIP38PassphraseQLineEdit)


        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrameHLayout.addWidget(self.BIPFromWIFBIP38PassphraseContainerQFrame)


        self.BIPFromWIFQStackedWidgetVLayout.addWidget(self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)

        self.BIPFromWIFQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.BIPFromWIFQStackedWidgetVLayout.addItem(self.BIPFromWIFQStackedWidgetVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromWIFQStackedWidget)
        self.BIPFromPrivateKeyQStackedWidget = QWidget()
        self.BIPFromPrivateKeyQStackedWidget.setObjectName(u"BIPFromPrivateKeyQStackedWidget")
        self.BIPFromPrivateKeyQStackedWidgetVLayout = QVBoxLayout(self.BIPFromPrivateKeyQStackedWidget)
        self.BIPFromPrivateKeyQStackedWidgetVLayout.setSpacing(15)
        self.BIPFromPrivateKeyQStackedWidgetVLayout.setObjectName(u"BIPFromPrivateKeyQStackedWidgetVLayout")
        self.BIPFromPrivateKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame = QFrame(self.BIPFromPrivateKeyQStackedWidget)
        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame")
        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"BIPFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout")
        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyContainerQFrame = QFrame(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromPrivateKeyContainerQFrame.setObjectName(u"BIPFromPrivateKeyContainerQFrame")
        self.BIPFromPrivateKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.BIPFromPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.BIPFromPrivateKeyContainerQFrame)
        self.BIPFromPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.BIPFromPrivateKeyContainerQFrameVLayout.setObjectName(u"BIPFromPrivateKeyContainerQFrameVLayout")
        self.BIPFromPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyLabelContainerQFrame = QFrame(self.BIPFromPrivateKeyContainerQFrame)
        self.BIPFromPrivateKeyLabelContainerQFrame.setObjectName(u"BIPFromPrivateKeyLabelContainerQFrame")
        self.BIPFromPrivateKeyLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromPrivateKeyLabelContainerQFrame)
        self.BIPFromPrivateKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromPrivateKeyLabelContainerQFrameHLayout.setObjectName(u"BIPFromPrivateKeyLabelContainerQFrameHLayout")
        self.BIPFromPrivateKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyQLabel = QLabel(self.BIPFromPrivateKeyLabelContainerQFrame)
        self.BIPFromPrivateKeyQLabel.setObjectName(u"BIPFromPrivateKeyQLabel")

        self.BIPFromPrivateKeyLabelContainerQFrameHLayout.addWidget(self.BIPFromPrivateKeyQLabel)

        self.BIPFromPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromPrivateKeyLabelContainerQFrameHLayout.addItem(self.BIPFromPrivateKeyLabelContainerQFrameHSpacer)


        self.BIPFromPrivateKeyContainerQFrameVLayout.addWidget(self.BIPFromPrivateKeyLabelContainerQFrame)

        self.BIPFromPrivateKeyQLineEdit = QLineEdit(self.BIPFromPrivateKeyContainerQFrame)
        self.BIPFromPrivateKeyQLineEdit.setObjectName(u"BIPFromPrivateKeyQLineEdit")

        self.BIPFromPrivateKeyContainerQFrameVLayout.addWidget(self.BIPFromPrivateKeyQLineEdit)


        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.BIPFromPrivateKeyContainerQFrame)

        self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrame = QFrame(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrame.setObjectName(u"BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrame")
        self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrame.setMinimumSize(QSize(150, 0))
        self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout = QVBoxLayout(self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrame)
        self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout.setSpacing(5)
        self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout.setObjectName(u"BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout")
        self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrame = QFrame(self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrame)
        self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrame.setObjectName(u"BIPFromPrivateKeyAndPublicKeyTypeLabelQFrame")
        self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout = QHBoxLayout(self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrame)
        self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout.setSpacing(15)
        self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout.setObjectName(u"BIPFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout")
        self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyPublicKeyTypeQLabel = QLabel(self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrame)
        self.BIPFromPrivateKeyPublicKeyTypeQLabel.setObjectName(u"BIPFromPrivateKeyPublicKeyTypeQLabel")

        self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout.addWidget(self.BIPFromPrivateKeyPublicKeyTypeQLabel)

        self.BIPFromPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrameHLayout.addItem(self.BIPFromPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout.addWidget(self.BIPFromPrivateKeyAndPublicKeyTypeLabelQFrame)

        self.BIPFromPrivateKeyPublicKeyTypeQComboBox = QComboBox(self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrame)
        self.BIPFromPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromPrivateKeyPublicKeyTypeQComboBox.setObjectName(u"BIPFromPrivateKeyPublicKeyTypeQComboBox")

        self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrameVLayout.addWidget(self.BIPFromPrivateKeyPublicKeyTypeQComboBox)


        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.BIPFromPrivateKeyAndPublicKeyTypeLineContainerQFrame)


        self.BIPFromPrivateKeyQStackedWidgetVLayout.addWidget(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame)

        self.BIPFromPrivateKeyContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.BIPFromPrivateKeyQStackedWidgetVLayout.addItem(self.BIPFromPrivateKeyContainerQFrameVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromPrivateKeyQStackedWidget)
        self.BIPFromPublicKeyQStackedWidget = QWidget()
        self.BIPFromPublicKeyQStackedWidget.setObjectName(u"BIPFromPublicKeyQStackedWidget")
        self.BIPFromPublicKeyQStackedWidgetVLayout = QVBoxLayout(self.BIPFromPublicKeyQStackedWidget)
        self.BIPFromPublicKeyQStackedWidgetVLayout.setSpacing(15)
        self.BIPFromPublicKeyQStackedWidgetVLayout.setObjectName(u"BIPFromPublicKeyQStackedWidgetVLayout")
        self.BIPFromPublicKeyQStackedWidgetVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame = QFrame(self.BIPFromPublicKeyQStackedWidget)
        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromPublicKeyAndPublicKeyTypeContainerQFrame")
        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout = QHBoxLayout(self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setSpacing(15)
        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setObjectName(u"BIPFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout")
        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyContainerQFrame = QFrame(self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromPublicKeyContainerQFrame.setObjectName(u"BIPFromPublicKeyContainerQFrame")
        self.BIPFromPublicKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.BIPFromPublicKeyContainerQFrameVLayout = QVBoxLayout(self.BIPFromPublicKeyContainerQFrame)
        self.BIPFromPublicKeyContainerQFrameVLayout.setSpacing(5)
        self.BIPFromPublicKeyContainerQFrameVLayout.setObjectName(u"BIPFromPublicKeyContainerQFrameVLayout")
        self.BIPFromPublicKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyLabelContainerQFrame = QFrame(self.BIPFromPublicKeyContainerQFrame)
        self.BIPFromPublicKeyLabelContainerQFrame.setObjectName(u"BIPFromPublicKeyLabelContainerQFrame")
        self.BIPFromPublicKeyLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromPublicKeyLabelContainerQFrame)
        self.BIPFromPublicKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromPublicKeyLabelContainerQFrameHLayout.setObjectName(u"BIPFromPublicKeyLabelContainerQFrameHLayout")
        self.BIPFromPublicKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyQLabel = QLabel(self.BIPFromPublicKeyLabelContainerQFrame)
        self.BIPFromPublicKeyQLabel.setObjectName(u"BIPFromPublicKeyQLabel")

        self.BIPFromPublicKeyLabelContainerQFrameHLayout.addWidget(self.BIPFromPublicKeyQLabel)

        self.BIPFromPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromPublicKeyLabelContainerQFrameHLayout.addItem(self.BIPFromPublicKeyLabelContainerQFrameHSpacer)


        self.BIPFromPublicKeyContainerQFrameVLayout.addWidget(self.BIPFromPublicKeyLabelContainerQFrame)

        self.BIPFromPublicKeyQLineEdit = QLineEdit(self.BIPFromPublicKeyContainerQFrame)
        self.BIPFromPublicKeyQLineEdit.setObjectName(u"BIPFromPublicKeyQLineEdit")

        self.BIPFromPublicKeyContainerQFrameVLayout.addWidget(self.BIPFromPublicKeyQLineEdit)


        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.BIPFromPublicKeyContainerQFrame)

        self.BIPFromPublicKeyPublicKeyTypeContainerQFrame = QFrame(self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromPublicKeyPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromPublicKeyPublicKeyTypeContainerQFrame")
        self.BIPFromPublicKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.BIPFromPublicKeyPublicKeyTypeContainerQFrameVLayout = QVBoxLayout(self.BIPFromPublicKeyPublicKeyTypeContainerQFrame)
        self.BIPFromPublicKeyPublicKeyTypeContainerQFrameVLayout.setSpacing(5)
        self.BIPFromPublicKeyPublicKeyTypeContainerQFrameVLayout.setObjectName(u"BIPFromPublicKeyPublicKeyTypeContainerQFrameVLayout")
        self.BIPFromPublicKeyPublicKeyTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromPublicKeyPublicKeyTypeContainerQFrame)
        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame")
        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout = QHBoxLayout(self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setObjectName(u"BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout")
        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyPublicKeyTypeQLabel = QLabel(self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromPublicKeyPublicKeyTypeQLabel.setObjectName(u"BIPFromPublicKeyPublicKeyTypeQLabel")

        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.addWidget(self.BIPFromPublicKeyPublicKeyTypeQLabel)

        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHLayout.addItem(self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.BIPFromPublicKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame)

        self.BIPFromPublicKeyPublicKeyTypeQComboBox = QComboBox(self.BIPFromPublicKeyPublicKeyTypeContainerQFrame)
        self.BIPFromPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromPublicKeyPublicKeyTypeQComboBox.setObjectName(u"BIPFromPublicKeyPublicKeyTypeQComboBox")

        self.BIPFromPublicKeyPublicKeyTypeContainerQFrameVLayout.addWidget(self.BIPFromPublicKeyPublicKeyTypeQComboBox)


        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrameHLayout.addWidget(self.BIPFromPublicKeyPublicKeyTypeContainerQFrame)


        self.BIPFromPublicKeyQStackedWidgetVLayout.addWidget(self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame)

        self.BIPFromPublicKeyContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.BIPFromPublicKeyQStackedWidgetVLayout.addItem(self.BIPFromPublicKeyContainerQFrameVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromPublicKeyQStackedWidget)

        self.BIPsPageQWidgetVLayout.addWidget(self.BIPQStackedWidget)

        self.hdQStackedWidget.addWidget(self.BIPsPageQWidget)
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
        self.cardanoFromEntropyContainerQFrame = QFrame(self.cardanoFromEntropyQStackedWidget)
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


        self.cardanoFromEntropyQStackedWidgetVLayout.addWidget(self.cardanoFromEntropyContainerQFrame)

        self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame = QFrame(self.cardanoFromEntropyQStackedWidget)
        self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame.setObjectName(u"cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame")
        self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrameHLayout = QHBoxLayout(self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame)
        self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrameHLayout.setSpacing(15)
        self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrameHLayout.setObjectName(u"cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrameHLayout")
        self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyCardanoTypeContainerQFrame = QFrame(self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame)
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


        self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrameHLayout.addWidget(self.cardanoFromEntropyCardanoTypeContainerQFrame)

        self.cardanoFromEntropyPassphraseContainerQFrame = QFrame(self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame)
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

        self.cardanoFromEntropyPassphraseGenerateContainerQFrame = QFrame(self.cardanoFromEntropyPassphraseContainerQFrame)
        self.cardanoFromEntropyPassphraseGenerateContainerQFrame.setObjectName(u"cardanoFromEntropyPassphraseGenerateContainerQFrame")
        self.horizontalLayout_35 = QHBoxLayout(self.cardanoFromEntropyPassphraseGenerateContainerQFrame)
        self.horizontalLayout_35.setSpacing(15)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyPassphraseQLineEdit = QLineEdit(self.cardanoFromEntropyPassphraseGenerateContainerQFrame)
        self.cardanoFromEntropyPassphraseQLineEdit.setObjectName(u"cardanoFromEntropyPassphraseQLineEdit")

        self.horizontalLayout_35.addWidget(self.cardanoFromEntropyPassphraseQLineEdit)


        self.EPassphraseVLayout_5.addWidget(self.cardanoFromEntropyPassphraseGenerateContainerQFrame)


        self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrameHLayout.addWidget(self.cardanoFromEntropyPassphraseContainerQFrame)


        self.cardanoFromEntropyQStackedWidgetVLayout.addWidget(self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame)

        self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame = QFrame(self.cardanoFromEntropyQStackedWidget)
        self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame.setObjectName(u"cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame")
        self.horizontalLayout_36 = QHBoxLayout(self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame)
        self.horizontalLayout_36.setSpacing(15)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyLanguageContainerQFrame = QFrame(self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame)
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


        self.horizontalLayout_36.addWidget(self.cardanoFromEntropyLanguageContainerQFrame)

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

        self.cardanoFromEntropyWordsContainerQFrame = QFrame(self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame)
        self.cardanoFromEntropyWordsContainerQFrame.setObjectName(u"cardanoFromEntropyWordsContainerQFrame")
        self.EStrengthVLayout_3 = QVBoxLayout(self.cardanoFromEntropyWordsContainerQFrame)
        self.EStrengthVLayout_3.setSpacing(5)
        self.EStrengthVLayout_3.setObjectName(u"EStrengthVLayout_3")
        self.EStrengthVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyWordsLabelContainerQFrame = QFrame(self.cardanoFromEntropyWordsContainerQFrame)
        self.cardanoFromEntropyWordsLabelContainerQFrame.setObjectName(u"cardanoFromEntropyWordsLabelContainerQFrame")
        self.EStrengthLabelHLayout_3 = QHBoxLayout(self.cardanoFromEntropyWordsLabelContainerQFrame)
        self.EStrengthLabelHLayout_3.setSpacing(15)
        self.EStrengthLabelHLayout_3.setObjectName(u"EStrengthLabelHLayout_3")
        self.EStrengthLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyWordsQLabel = QLabel(self.cardanoFromEntropyWordsLabelContainerQFrame)
        self.cardanoFromEntropyWordsQLabel.setObjectName(u"cardanoFromEntropyWordsQLabel")

        self.EStrengthLabelHLayout_3.addWidget(self.cardanoFromEntropyWordsQLabel)

        self.cardanoFromEntropyWordsLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout_3.addItem(self.cardanoFromEntropyWordsLabelContainerQFrameHSpacer)


        self.EStrengthVLayout_3.addWidget(self.cardanoFromEntropyWordsLabelContainerQFrame)

        self.cardanoFromEntropyWordsQComboBox = QComboBox(self.cardanoFromEntropyWordsContainerQFrame)
        self.cardanoFromEntropyWordsQComboBox.addItem("")
        self.cardanoFromEntropyWordsQComboBox.addItem("")
        self.cardanoFromEntropyWordsQComboBox.addItem("")
        self.cardanoFromEntropyWordsQComboBox.addItem("")
        self.cardanoFromEntropyWordsQComboBox.addItem("")
        self.cardanoFromEntropyWordsQComboBox.setObjectName(u"cardanoFromEntropyWordsQComboBox")

        self.EStrengthVLayout_3.addWidget(self.cardanoFromEntropyWordsQComboBox)


        self.horizontalLayout_36.addWidget(self.cardanoFromEntropyWordsContainerQFrame)


        self.cardanoFromEntropyQStackedWidgetVLayout.addWidget(self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromEntropyQStackedWidget)
        self.cardanoFromMnemonicQStackedWidget = QWidget()
        self.cardanoFromMnemonicQStackedWidget.setObjectName(u"cardanoFromMnemonicQStackedWidget")
        self.verticalLayout_36 = QVBoxLayout(self.cardanoFromMnemonicQStackedWidget)
        self.verticalLayout_36.setSpacing(15)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicContainerQFrame = QFrame(self.cardanoFromMnemonicQStackedWidget)
        self.cardanoFromMnemonicContainerQFrame.setObjectName(u"cardanoFromMnemonicContainerQFrame")
        self.MnemonicVLayout_3 = QVBoxLayout(self.cardanoFromMnemonicContainerQFrame)
        self.MnemonicVLayout_3.setSpacing(5)
        self.MnemonicVLayout_3.setObjectName(u"MnemonicVLayout_3")
        self.MnemonicVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicLabelContainerQFrame = QFrame(self.cardanoFromMnemonicContainerQFrame)
        self.cardanoFromMnemonicLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicLabelContainerQFrame")
        self.MnemonicLabelHLayout_3 = QHBoxLayout(self.cardanoFromMnemonicLabelContainerQFrame)
        self.MnemonicLabelHLayout_3.setSpacing(15)
        self.MnemonicLabelHLayout_3.setObjectName(u"MnemonicLabelHLayout_3")
        self.MnemonicLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicQLabel = QLabel(self.cardanoFromMnemonicLabelContainerQFrame)
        self.cardanoFromMnemonicQLabel.setObjectName(u"cardanoFromMnemonicQLabel")

        self.MnemonicLabelHLayout_3.addWidget(self.cardanoFromMnemonicQLabel)

        self.cardanoFromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout_3.addItem(self.cardanoFromMnemonicLabelContainerQFrameHSpacer)


        self.MnemonicVLayout_3.addWidget(self.cardanoFromMnemonicLabelContainerQFrame)

        self.cardanoFromMnemonicGenerateContainerQFrame = QFrame(self.cardanoFromMnemonicContainerQFrame)
        self.cardanoFromMnemonicGenerateContainerQFrame.setObjectName(u"cardanoFromMnemonicGenerateContainerQFrame")
        self.horizontalLayout_37 = QHBoxLayout(self.cardanoFromMnemonicGenerateContainerQFrame)
        self.horizontalLayout_37.setSpacing(15)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicGenerateQLineEdit = QLineEdit(self.cardanoFromMnemonicGenerateContainerQFrame)
        self.cardanoFromMnemonicGenerateQLineEdit.setObjectName(u"cardanoFromMnemonicGenerateQLineEdit")

        self.horizontalLayout_37.addWidget(self.cardanoFromMnemonicGenerateQLineEdit)


        self.MnemonicVLayout_3.addWidget(self.cardanoFromMnemonicGenerateContainerQFrame)


        self.verticalLayout_36.addWidget(self.cardanoFromMnemonicContainerQFrame)

        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame = QFrame(self.cardanoFromMnemonicQStackedWidget)
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame.setObjectName(u"cardanoFromMnemonicClientAndPassphraseContainerQFrame")
        self.horizontalLayout_38 = QHBoxLayout(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame)
        self.horizontalLayout_38.setSpacing(15)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicCardanoTypeContainerQFrame = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame)
        self.cardanoFromMnemonicCardanoTypeContainerQFrame.setObjectName(u"cardanoFromMnemonicCardanoTypeContainerQFrame")
        self.cardanoFromMnemonicCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_8 = QVBoxLayout(self.cardanoFromMnemonicCardanoTypeContainerQFrame)
        self.ClientVLayout_8.setSpacing(5)
        self.ClientVLayout_8.setObjectName(u"ClientVLayout_8")
        self.ClientVLayout_8.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromMnemonicCardanoTypeContainerQFrame)
        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicCardanoTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_10 = QHBoxLayout(self.cardanoFromMnemonicCardanoTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_10.setSpacing(15)
        self.MStrengthLabelHLayout_10.setObjectName(u"MStrengthLabelHLayout_10")
        self.MStrengthLabelHLayout_10.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicCardanoTypeQLabel = QLabel(self.cardanoFromMnemonicCardanoTypeLabelContainerQFrame)
        self.cardanoFromMnemonicCardanoTypeQLabel.setObjectName(u"cardanoFromMnemonicCardanoTypeQLabel")

        self.MStrengthLabelHLayout_10.addWidget(self.cardanoFromMnemonicCardanoTypeQLabel)

        self.cardanoFromMnemonicCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_10.addItem(self.cardanoFromMnemonicCardanoTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_8.addWidget(self.cardanoFromMnemonicCardanoTypeLabelContainerQFrame)

        self.cardanoFromMnemonicCardanoTypeQComboBox = QComboBox(self.cardanoFromMnemonicCardanoTypeContainerQFrame)
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.addItem("")
        self.cardanoFromMnemonicCardanoTypeQComboBox.setObjectName(u"cardanoFromMnemonicCardanoTypeQComboBox")

        self.ClientVLayout_8.addWidget(self.cardanoFromMnemonicCardanoTypeQComboBox)


        self.horizontalLayout_38.addWidget(self.cardanoFromMnemonicCardanoTypeContainerQFrame)

        self.cardanoFromMnemonicPassphraseContainerQFrame = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame)
        self.cardanoFromMnemonicPassphraseContainerQFrame.setObjectName(u"cardanoFromMnemonicPassphraseContainerQFrame")
        self.EPassphraseVLayout_6 = QVBoxLayout(self.cardanoFromMnemonicPassphraseContainerQFrame)
        self.EPassphraseVLayout_6.setSpacing(5)
        self.EPassphraseVLayout_6.setObjectName(u"EPassphraseVLayout_6")
        self.EPassphraseVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicPassphraseLabelContainerQFrame = QFrame(self.cardanoFromMnemonicPassphraseContainerQFrame)
        self.cardanoFromMnemonicPassphraseLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicPassphraseLabelContainerQFrame")
        self.MPassphraseLabelHLayout_3 = QHBoxLayout(self.cardanoFromMnemonicPassphraseLabelContainerQFrame)
        self.MPassphraseLabelHLayout_3.setSpacing(15)
        self.MPassphraseLabelHLayout_3.setObjectName(u"MPassphraseLabelHLayout_3")
        self.MPassphraseLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicPassphraseQLabel = QLabel(self.cardanoFromMnemonicPassphraseLabelContainerQFrame)
        self.cardanoFromMnemonicPassphraseQLabel.setObjectName(u"cardanoFromMnemonicPassphraseQLabel")

        self.MPassphraseLabelHLayout_3.addWidget(self.cardanoFromMnemonicPassphraseQLabel)

        self.cardanoFromMnemonicPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout_3.addItem(self.cardanoFromMnemonicPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout_6.addWidget(self.cardanoFromMnemonicPassphraseLabelContainerQFrame)

        self.cardanoFromMnemonicPassphraseGenerateContainerQFrame = QFrame(self.cardanoFromMnemonicPassphraseContainerQFrame)
        self.cardanoFromMnemonicPassphraseGenerateContainerQFrame.setObjectName(u"cardanoFromMnemonicPassphraseGenerateContainerQFrame")
        self.horizontalLayout_39 = QHBoxLayout(self.cardanoFromMnemonicPassphraseGenerateContainerQFrame)
        self.horizontalLayout_39.setSpacing(15)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicPassphraseQLineEdit = QLineEdit(self.cardanoFromMnemonicPassphraseGenerateContainerQFrame)
        self.cardanoFromMnemonicPassphraseQLineEdit.setObjectName(u"cardanoFromMnemonicPassphraseQLineEdit")

        self.horizontalLayout_39.addWidget(self.cardanoFromMnemonicPassphraseQLineEdit)


        self.EPassphraseVLayout_6.addWidget(self.cardanoFromMnemonicPassphraseGenerateContainerQFrame)


        self.horizontalLayout_38.addWidget(self.cardanoFromMnemonicPassphraseContainerQFrame)


        self.verticalLayout_36.addWidget(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame)

        self.cardanoFromMnemonicLanguageAddressTypeAndWordsContainerQFrame = QFrame(self.cardanoFromMnemonicQStackedWidget)
        self.cardanoFromMnemonicLanguageAddressTypeAndWordsContainerQFrame.setObjectName(u"cardanoFromMnemonicLanguageAddressTypeAndWordsContainerQFrame")
        self.horizontalLayout_40 = QHBoxLayout(self.cardanoFromMnemonicLanguageAddressTypeAndWordsContainerQFrame)
        self.horizontalLayout_40.setSpacing(15)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicLanguageContainerQFrame = QFrame(self.cardanoFromMnemonicLanguageAddressTypeAndWordsContainerQFrame)
        self.cardanoFromMnemonicLanguageContainerQFrame.setObjectName(u"cardanoFromMnemonicLanguageContainerQFrame")
        self.ELanguageVLayout_6 = QVBoxLayout(self.cardanoFromMnemonicLanguageContainerQFrame)
        self.ELanguageVLayout_6.setSpacing(5)
        self.ELanguageVLayout_6.setObjectName(u"ELanguageVLayout_6")
        self.ELanguageVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicLanguageLabelContainerQFrame = QFrame(self.cardanoFromMnemonicLanguageContainerQFrame)
        self.cardanoFromMnemonicLanguageLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicLanguageLabelContainerQFrame")
        self.ELanguageLabelHLayout_6 = QHBoxLayout(self.cardanoFromMnemonicLanguageLabelContainerQFrame)
        self.ELanguageLabelHLayout_6.setSpacing(15)
        self.ELanguageLabelHLayout_6.setObjectName(u"ELanguageLabelHLayout_6")
        self.ELanguageLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicLanguageQLabel = QLabel(self.cardanoFromMnemonicLanguageLabelContainerQFrame)
        self.cardanoFromMnemonicLanguageQLabel.setObjectName(u"cardanoFromMnemonicLanguageQLabel")

        self.ELanguageLabelHLayout_6.addWidget(self.cardanoFromMnemonicLanguageQLabel)

        self.cardanoFromMnemonicLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout_6.addItem(self.cardanoFromMnemonicLanguageLabelContainerQFrameHSpacer)


        self.ELanguageVLayout_6.addWidget(self.cardanoFromMnemonicLanguageLabelContainerQFrame)

        self.cardanoFromMnemonicLanguageQComboBox = QComboBox(self.cardanoFromMnemonicLanguageContainerQFrame)
        self.cardanoFromMnemonicLanguageQComboBox.addItem("")
        self.cardanoFromMnemonicLanguageQComboBox.addItem("")
        self.cardanoFromMnemonicLanguageQComboBox.addItem("")
        self.cardanoFromMnemonicLanguageQComboBox.addItem("")
        self.cardanoFromMnemonicLanguageQComboBox.addItem("")
        self.cardanoFromMnemonicLanguageQComboBox.addItem("")
        self.cardanoFromMnemonicLanguageQComboBox.addItem("")
        self.cardanoFromMnemonicLanguageQComboBox.addItem("")
        self.cardanoFromMnemonicLanguageQComboBox.setObjectName(u"cardanoFromMnemonicLanguageQComboBox")

        self.ELanguageVLayout_6.addWidget(self.cardanoFromMnemonicLanguageQComboBox)


        self.horizontalLayout_40.addWidget(self.cardanoFromMnemonicLanguageContainerQFrame)

        self.cardanoFromMnemonicAddressTypeContainerQFrame = QFrame(self.cardanoFromMnemonicLanguageAddressTypeAndWordsContainerQFrame)
        self.cardanoFromMnemonicAddressTypeContainerQFrame.setObjectName(u"cardanoFromMnemonicAddressTypeContainerQFrame")
        self.verticalLayout_93 = QVBoxLayout(self.cardanoFromMnemonicAddressTypeContainerQFrame)
        self.verticalLayout_93.setSpacing(5)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromMnemonicAddressTypeContainerQFrame)
        self.cardanoFromMnemonicAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicAddressTypeLabelContainerQFrame")
        self.horizontalLayout_97 = QHBoxLayout(self.cardanoFromMnemonicAddressTypeLabelContainerQFrame)
        self.horizontalLayout_97.setSpacing(15)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicAddressTypeQLabel = QLabel(self.cardanoFromMnemonicAddressTypeLabelContainerQFrame)
        self.cardanoFromMnemonicAddressTypeQLabel.setObjectName(u"cardanoFromMnemonicAddressTypeQLabel")

        self.horizontalLayout_97.addWidget(self.cardanoFromMnemonicAddressTypeQLabel)

        self.cardanoFromMnemonicAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.cardanoFromMnemonicAddressTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_93.addWidget(self.cardanoFromMnemonicAddressTypeLabelContainerQFrame)

        self.cardanoFromMnemonicAddressTypeQComboBox = QComboBox(self.cardanoFromMnemonicAddressTypeContainerQFrame)
        self.cardanoFromMnemonicAddressTypeQComboBox.setObjectName(u"cardanoFromMnemonicAddressTypeQComboBox")

        self.verticalLayout_93.addWidget(self.cardanoFromMnemonicAddressTypeQComboBox)


        self.horizontalLayout_40.addWidget(self.cardanoFromMnemonicAddressTypeContainerQFrame)

        self.cardanoFromMnemonicWordsContainerQFrame = QFrame(self.cardanoFromMnemonicLanguageAddressTypeAndWordsContainerQFrame)
        self.cardanoFromMnemonicWordsContainerQFrame.setObjectName(u"cardanoFromMnemonicWordsContainerQFrame")
        self.EStrengthVLayout_6 = QVBoxLayout(self.cardanoFromMnemonicWordsContainerQFrame)
        self.EStrengthVLayout_6.setSpacing(5)
        self.EStrengthVLayout_6.setObjectName(u"EStrengthVLayout_6")
        self.EStrengthVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicWordsLabelContainerQFrame = QFrame(self.cardanoFromMnemonicWordsContainerQFrame)
        self.cardanoFromMnemonicWordsLabelContainerQFrame.setObjectName(u"cardanoFromMnemonicWordsLabelContainerQFrame")
        self.EStrengthLabelHLayout_6 = QHBoxLayout(self.cardanoFromMnemonicWordsLabelContainerQFrame)
        self.EStrengthLabelHLayout_6.setSpacing(15)
        self.EStrengthLabelHLayout_6.setObjectName(u"EStrengthLabelHLayout_6")
        self.EStrengthLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicWordsQLabel = QLabel(self.cardanoFromMnemonicWordsLabelContainerQFrame)
        self.cardanoFromMnemonicWordsQLabel.setObjectName(u"cardanoFromMnemonicWordsQLabel")

        self.EStrengthLabelHLayout_6.addWidget(self.cardanoFromMnemonicWordsQLabel)

        self.cardanoFromMnemonicWordsLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout_6.addItem(self.cardanoFromMnemonicWordsLabelContainerQFrameHSpacer)


        self.EStrengthVLayout_6.addWidget(self.cardanoFromMnemonicWordsLabelContainerQFrame)

        self.cardanoFromMnemonicWordsQComboBox = QComboBox(self.cardanoFromMnemonicWordsContainerQFrame)
        self.cardanoFromMnemonicWordsQComboBox.addItem("")
        self.cardanoFromMnemonicWordsQComboBox.addItem("")
        self.cardanoFromMnemonicWordsQComboBox.addItem("")
        self.cardanoFromMnemonicWordsQComboBox.addItem("")
        self.cardanoFromMnemonicWordsQComboBox.addItem("")
        self.cardanoFromMnemonicWordsQComboBox.setObjectName(u"cardanoFromMnemonicWordsQComboBox")

        self.EStrengthVLayout_6.addWidget(self.cardanoFromMnemonicWordsQComboBox)


        self.horizontalLayout_40.addWidget(self.cardanoFromMnemonicWordsContainerQFrame)


        self.verticalLayout_36.addWidget(self.cardanoFromMnemonicLanguageAddressTypeAndWordsContainerQFrame)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromMnemonicQStackedWidget)
        self.cardanoFromSeedQStackedWidget = QWidget()
        self.cardanoFromSeedQStackedWidget.setObjectName(u"cardanoFromSeedQStackedWidget")
        self.verticalLayout_37 = QVBoxLayout(self.cardanoFromSeedQStackedWidget)
        self.verticalLayout_37.setSpacing(15)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedContainerQFrame = QFrame(self.cardanoFromSeedQStackedWidget)
        self.cardanoFromSeedContainerQFrame.setObjectName(u"cardanoFromSeedContainerQFrame")
        self.verticalLayout_38 = QVBoxLayout(self.cardanoFromSeedContainerQFrame)
        self.verticalLayout_38.setSpacing(5)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedLabelContainerQFrame = QFrame(self.cardanoFromSeedContainerQFrame)
        self.cardanoFromSeedLabelContainerQFrame.setObjectName(u"cardanoFromSeedLabelContainerQFrame")
        self.SeedLabelHLayout_3 = QHBoxLayout(self.cardanoFromSeedLabelContainerQFrame)
        self.SeedLabelHLayout_3.setSpacing(15)
        self.SeedLabelHLayout_3.setObjectName(u"SeedLabelHLayout_3")
        self.SeedLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedQLabel = QLabel(self.cardanoFromSeedLabelContainerQFrame)
        self.cardanoFromSeedQLabel.setObjectName(u"cardanoFromSeedQLabel")

        self.SeedLabelHLayout_3.addWidget(self.cardanoFromSeedQLabel)

        self.cardanoFromSeedLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout_3.addItem(self.cardanoFromSeedLabelContainerQFrameHSpacer)


        self.verticalLayout_38.addWidget(self.cardanoFromSeedLabelContainerQFrame)

        self.cardanoFromSeedQLineEdit = QLineEdit(self.cardanoFromSeedContainerQFrame)
        self.cardanoFromSeedQLineEdit.setObjectName(u"cardanoFromSeedQLineEdit")

        self.verticalLayout_38.addWidget(self.cardanoFromSeedQLineEdit)


        self.verticalLayout_37.addWidget(self.cardanoFromSeedContainerQFrame)

        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame = QFrame(self.cardanoFromSeedQStackedWidget)
        self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame.setObjectName(u"cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame")
        self.horizontalLayout_42 = QHBoxLayout(self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame)
        self.horizontalLayout_42.setSpacing(15)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedCardanoTypeContainerQFrame = QFrame(self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame)
        self.cardanoFromSeedCardanoTypeContainerQFrame.setObjectName(u"cardanoFromSeedCardanoTypeContainerQFrame")
        self.cardanoFromSeedCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_16 = QVBoxLayout(self.cardanoFromSeedCardanoTypeContainerQFrame)
        self.ClientVLayout_16.setSpacing(5)
        self.ClientVLayout_16.setObjectName(u"ClientVLayout_16")
        self.ClientVLayout_16.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromSeedCardanoTypeContainerQFrame)
        self.cardanoFromSeedCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromSeedCardanoTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_21 = QHBoxLayout(self.cardanoFromSeedCardanoTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_21.setSpacing(15)
        self.MStrengthLabelHLayout_21.setObjectName(u"MStrengthLabelHLayout_21")
        self.MStrengthLabelHLayout_21.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedCardanoTypeQLabel = QLabel(self.cardanoFromSeedCardanoTypeLabelContainerQFrame)
        self.cardanoFromSeedCardanoTypeQLabel.setObjectName(u"cardanoFromSeedCardanoTypeQLabel")

        self.MStrengthLabelHLayout_21.addWidget(self.cardanoFromSeedCardanoTypeQLabel)

        self.cardanoFromSeedCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_21.addItem(self.cardanoFromSeedCardanoTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_16.addWidget(self.cardanoFromSeedCardanoTypeLabelContainerQFrame)

        self.cardanoFromSeedCardanoTypeQComboBox = QComboBox(self.cardanoFromSeedCardanoTypeContainerQFrame)
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.addItem("")
        self.cardanoFromSeedCardanoTypeQComboBox.setObjectName(u"cardanoFromSeedCardanoTypeQComboBox")

        self.ClientVLayout_16.addWidget(self.cardanoFromSeedCardanoTypeQComboBox)


        self.horizontalLayout_42.addWidget(self.cardanoFromSeedCardanoTypeContainerQFrame)

        self.cardanoFromSeedAddressTypeContainerQFrame = QFrame(self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame)
        self.cardanoFromSeedAddressTypeContainerQFrame.setObjectName(u"cardanoFromSeedAddressTypeContainerQFrame")
        self.cardanoFromSeedAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_9 = QVBoxLayout(self.cardanoFromSeedAddressTypeContainerQFrame)
        self.ClientVLayout_9.setSpacing(5)
        self.ClientVLayout_9.setObjectName(u"ClientVLayout_9")
        self.ClientVLayout_9.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromSeedAddressTypeContainerQFrame)
        self.cardanoFromSeedAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromSeedAddressTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_12 = QHBoxLayout(self.cardanoFromSeedAddressTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_12.setSpacing(15)
        self.MStrengthLabelHLayout_12.setObjectName(u"MStrengthLabelHLayout_12")
        self.MStrengthLabelHLayout_12.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedAddressTypeQLabel = QLabel(self.cardanoFromSeedAddressTypeLabelContainerQFrame)
        self.cardanoFromSeedAddressTypeQLabel.setObjectName(u"cardanoFromSeedAddressTypeQLabel")

        self.MStrengthLabelHLayout_12.addWidget(self.cardanoFromSeedAddressTypeQLabel)

        self.cardanoFromSeedAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_12.addItem(self.cardanoFromSeedAddressTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_9.addWidget(self.cardanoFromSeedAddressTypeLabelContainerQFrame)

        self.cardanoFromSeedAddressTypeQComboBox = QComboBox(self.cardanoFromSeedAddressTypeContainerQFrame)
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.addItem("")
        self.cardanoFromSeedAddressTypeQComboBox.setObjectName(u"cardanoFromSeedAddressTypeQComboBox")

        self.ClientVLayout_9.addWidget(self.cardanoFromSeedAddressTypeQComboBox)


        self.horizontalLayout_42.addWidget(self.cardanoFromSeedAddressTypeContainerQFrame)

        self.cardanoFromSeedPassphraseContainerQFrame = QFrame(self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame)
        self.cardanoFromSeedPassphraseContainerQFrame.setObjectName(u"cardanoFromSeedPassphraseContainerQFrame")
        self.EPassphraseVLayout_11 = QVBoxLayout(self.cardanoFromSeedPassphraseContainerQFrame)
        self.EPassphraseVLayout_11.setSpacing(5)
        self.EPassphraseVLayout_11.setObjectName(u"EPassphraseVLayout_11")
        self.EPassphraseVLayout_11.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedPassphraseLabelContainerQFrame = QFrame(self.cardanoFromSeedPassphraseContainerQFrame)
        self.cardanoFromSeedPassphraseLabelContainerQFrame.setObjectName(u"cardanoFromSeedPassphraseLabelContainerQFrame")
        self.MPassphraseLabelHLayout_6 = QHBoxLayout(self.cardanoFromSeedPassphraseLabelContainerQFrame)
        self.MPassphraseLabelHLayout_6.setSpacing(15)
        self.MPassphraseLabelHLayout_6.setObjectName(u"MPassphraseLabelHLayout_6")
        self.MPassphraseLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedPassphraseQLabel = QLabel(self.cardanoFromSeedPassphraseLabelContainerQFrame)
        self.cardanoFromSeedPassphraseQLabel.setObjectName(u"cardanoFromSeedPassphraseQLabel")

        self.MPassphraseLabelHLayout_6.addWidget(self.cardanoFromSeedPassphraseQLabel)

        self.cardanoFromSeedPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout_6.addItem(self.cardanoFromSeedPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout_11.addWidget(self.cardanoFromSeedPassphraseLabelContainerQFrame)

        self.cardanoFromSeedPassphraseLineEditContainerQFrame = QFrame(self.cardanoFromSeedPassphraseContainerQFrame)
        self.cardanoFromSeedPassphraseLineEditContainerQFrame.setObjectName(u"cardanoFromSeedPassphraseLineEditContainerQFrame")
        self.horizontalLayout_62 = QHBoxLayout(self.cardanoFromSeedPassphraseLineEditContainerQFrame)
        self.horizontalLayout_62.setSpacing(15)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedPassphraseQLineEdit = QLineEdit(self.cardanoFromSeedPassphraseLineEditContainerQFrame)
        self.cardanoFromSeedPassphraseQLineEdit.setObjectName(u"cardanoFromSeedPassphraseQLineEdit")

        self.horizontalLayout_62.addWidget(self.cardanoFromSeedPassphraseQLineEdit)

        self.cardanoFromSeedPassphraseGenerateQPushButton = QPushButton(self.cardanoFromSeedPassphraseLineEditContainerQFrame)
        self.cardanoFromSeedPassphraseGenerateQPushButton.setObjectName(u"cardanoFromSeedPassphraseGenerateQPushButton")

        self.horizontalLayout_62.addWidget(self.cardanoFromSeedPassphraseGenerateQPushButton)


        self.EPassphraseVLayout_11.addWidget(self.cardanoFromSeedPassphraseLineEditContainerQFrame)


        self.horizontalLayout_42.addWidget(self.cardanoFromSeedPassphraseContainerQFrame)


        self.verticalLayout_37.addWidget(self.cardanoFromSeedCardanoTypeAddressTypeAndPassphraseContainerQFrame)

        self.cardanoFromSeedQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.cardanoFromSeedQStackedWidgetVSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromSeedQStackedWidget)
        self.cardanoFromXPrivateKeyQStackedWidget = QWidget()
        self.cardanoFromXPrivateKeyQStackedWidget.setObjectName(u"cardanoFromXPrivateKeyQStackedWidget")
        self.verticalLayout_39 = QVBoxLayout(self.cardanoFromXPrivateKeyQStackedWidget)
        self.verticalLayout_39.setSpacing(15)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyContainerQFrame = QFrame(self.cardanoFromXPrivateKeyQStackedWidget)
        self.cardanoFromXPrivateKeyContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyContainerQFrame")
        self.XPrivateKeyVLayout_3 = QVBoxLayout(self.cardanoFromXPrivateKeyContainerQFrame)
        self.XPrivateKeyVLayout_3.setSpacing(5)
        self.XPrivateKeyVLayout_3.setObjectName(u"XPrivateKeyVLayout_3")
        self.XPrivateKeyVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyLabelContainerQFrame = QFrame(self.cardanoFromXPrivateKeyContainerQFrame)
        self.cardanoFromXPrivateKeyLabelContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyLabelContainerQFrame")
        self.XPrivateKeyLabelHLayout_3 = QHBoxLayout(self.cardanoFromXPrivateKeyLabelContainerQFrame)
        self.XPrivateKeyLabelHLayout_3.setSpacing(15)
        self.XPrivateKeyLabelHLayout_3.setObjectName(u"XPrivateKeyLabelHLayout_3")
        self.XPrivateKeyLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyQLabel = QLabel(self.cardanoFromXPrivateKeyLabelContainerQFrame)
        self.cardanoFromXPrivateKeyQLabel.setObjectName(u"cardanoFromXPrivateKeyQLabel")

        self.XPrivateKeyLabelHLayout_3.addWidget(self.cardanoFromXPrivateKeyQLabel)

        self.cardanoFromXPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPrivateKeyLabelHLayout_3.addItem(self.cardanoFromXPrivateKeyLabelContainerQFrameHSpacer)


        self.XPrivateKeyVLayout_3.addWidget(self.cardanoFromXPrivateKeyLabelContainerQFrame)

        self.cardanoFromXPrivateKeyQLineEdit = QLineEdit(self.cardanoFromXPrivateKeyContainerQFrame)
        self.cardanoFromXPrivateKeyQLineEdit.setObjectName(u"cardanoFromXPrivateKeyQLineEdit")

        self.XPrivateKeyVLayout_3.addWidget(self.cardanoFromXPrivateKeyQLineEdit)


        self.verticalLayout_39.addWidget(self.cardanoFromXPrivateKeyContainerQFrame)

        self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame = QFrame(self.cardanoFromXPrivateKeyQStackedWidget)
        self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame")
        self.horizontalLayout_63 = QHBoxLayout(self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.horizontalLayout_63.setSpacing(15)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame = QFrame(self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeContainerQFrame")
        self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_19 = QVBoxLayout(self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame)
        self.ClientVLayout_19.setSpacing(5)
        self.ClientVLayout_19.setObjectName(u"ClientVLayout_19")
        self.ClientVLayout_19.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_24 = QHBoxLayout(self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_24.setSpacing(15)
        self.MStrengthLabelHLayout_24.setObjectName(u"MStrengthLabelHLayout_24")
        self.MStrengthLabelHLayout_24.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyCardanoTypeQLabel = QLabel(self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeQLabel.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeQLabel")

        self.MStrengthLabelHLayout_24.addWidget(self.cardanoFromXPrivateKeyCardanoTypeQLabel)

        self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_24.addItem(self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_19.addWidget(self.cardanoFromXPrivateKeyCardanoTypeLabelContainerQFrame)

        self.cardanoFromXPrivateKeyCardanoTypeQComboBox = QComboBox(self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame)
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setObjectName(u"cardanoFromXPrivateKeyCardanoTypeQComboBox")

        self.ClientVLayout_19.addWidget(self.cardanoFromXPrivateKeyCardanoTypeQComboBox)


        self.horizontalLayout_63.addWidget(self.cardanoFromXPrivateKeyCardanoTypeContainerQFrame)

        self.cardanoFromXPrivateKeyAddressTypeContainerQFrame = QFrame(self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromXPrivateKeyAddressTypeContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyAddressTypeContainerQFrame")
        self.cardanoFromXPrivateKeyAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_17 = QVBoxLayout(self.cardanoFromXPrivateKeyAddressTypeContainerQFrame)
        self.ClientVLayout_17.setSpacing(5)
        self.ClientVLayout_17.setObjectName(u"ClientVLayout_17")
        self.ClientVLayout_17.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromXPrivateKeyAddressTypeContainerQFrame)
        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_22 = QHBoxLayout(self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_22.setSpacing(15)
        self.MStrengthLabelHLayout_22.setObjectName(u"MStrengthLabelHLayout_22")
        self.MStrengthLabelHLayout_22.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPrivateKeyAddressTypeQLabel = QLabel(self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromXPrivateKeyAddressTypeQLabel.setObjectName(u"cardanoFromXPrivateKeyAddressTypeQLabel")

        self.MStrengthLabelHLayout_22.addWidget(self.cardanoFromXPrivateKeyAddressTypeQLabel)

        self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_22.addItem(self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_17.addWidget(self.cardanoFromXPrivateKeyAddressTypeLabelContainerQFrame)

        self.cardanoFromXPrivateKeyAddressTypeQComboBox = QComboBox(self.cardanoFromXPrivateKeyAddressTypeContainerQFrame)
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setObjectName(u"cardanoFromXPrivateKeyAddressTypeQComboBox")

        self.ClientVLayout_17.addWidget(self.cardanoFromXPrivateKeyAddressTypeQComboBox)


        self.horizontalLayout_63.addWidget(self.cardanoFromXPrivateKeyAddressTypeContainerQFrame)


        self.verticalLayout_39.addWidget(self.cardanoFromXPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)

        self.cardanoFromXPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.cardanoFromXPrivateKeyQStackedWidgetVSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromXPrivateKeyQStackedWidget)
        self.cardanoFromXPublicKeyQStackedWidget = QWidget()
        self.cardanoFromXPublicKeyQStackedWidget.setObjectName(u"cardanoFromXPublicKeyQStackedWidget")
        self.verticalLayout_40 = QVBoxLayout(self.cardanoFromXPublicKeyQStackedWidget)
        self.verticalLayout_40.setSpacing(15)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyContainerQFrame = QFrame(self.cardanoFromXPublicKeyQStackedWidget)
        self.cardanoFromXPublicKeyContainerQFrame.setObjectName(u"cardanoFromXPublicKeyContainerQFrame")
        self.XPublicKeyVLayout_3 = QVBoxLayout(self.cardanoFromXPublicKeyContainerQFrame)
        self.XPublicKeyVLayout_3.setSpacing(5)
        self.XPublicKeyVLayout_3.setObjectName(u"XPublicKeyVLayout_3")
        self.XPublicKeyVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyLabelContainerQFrame = QFrame(self.cardanoFromXPublicKeyContainerQFrame)
        self.cardanoFromXPublicKeyLabelContainerQFrame.setObjectName(u"cardanoFromXPublicKeyLabelContainerQFrame")
        self.XPublicKeyLabelHLayout_3 = QHBoxLayout(self.cardanoFromXPublicKeyLabelContainerQFrame)
        self.XPublicKeyLabelHLayout_3.setSpacing(15)
        self.XPublicKeyLabelHLayout_3.setObjectName(u"XPublicKeyLabelHLayout_3")
        self.XPublicKeyLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyQLabel = QLabel(self.cardanoFromXPublicKeyLabelContainerQFrame)
        self.cardanoFromXPublicKeyQLabel.setObjectName(u"cardanoFromXPublicKeyQLabel")

        self.XPublicKeyLabelHLayout_3.addWidget(self.cardanoFromXPublicKeyQLabel)

        self.cardanoFromXPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPublicKeyLabelHLayout_3.addItem(self.cardanoFromXPublicKeyLabelContainerQFrameHSpacer)


        self.XPublicKeyVLayout_3.addWidget(self.cardanoFromXPublicKeyLabelContainerQFrame)

        self.cardanoFromXPublicKeyQLineEdit = QLineEdit(self.cardanoFromXPublicKeyContainerQFrame)
        self.cardanoFromXPublicKeyQLineEdit.setObjectName(u"cardanoFromXPublicKeyQLineEdit")

        self.XPublicKeyVLayout_3.addWidget(self.cardanoFromXPublicKeyQLineEdit)


        self.verticalLayout_40.addWidget(self.cardanoFromXPublicKeyContainerQFrame)

        self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame = QFrame(self.cardanoFromXPublicKeyQStackedWidget)
        self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame.setObjectName(u"cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame")
        self.horizontalLayout_64 = QHBoxLayout(self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.horizontalLayout_64.setSpacing(15)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyCardanoTypeContainerQFrame = QFrame(self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeContainerQFrame.setObjectName(u"cardanoFromXPublicKeyCardanoTypeContainerQFrame")
        self.cardanoFromXPublicKeyCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_18 = QVBoxLayout(self.cardanoFromXPublicKeyCardanoTypeContainerQFrame)
        self.ClientVLayout_18.setSpacing(5)
        self.ClientVLayout_18.setObjectName(u"ClientVLayout_18")
        self.ClientVLayout_18.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromXPublicKeyCardanoTypeContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_23 = QHBoxLayout(self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_23.setSpacing(15)
        self.MStrengthLabelHLayout_23.setObjectName(u"MStrengthLabelHLayout_23")
        self.MStrengthLabelHLayout_23.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyCardanoTypeQLabel = QLabel(self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeQLabel.setObjectName(u"cardanoFromXPublicKeyCardanoTypeQLabel")

        self.MStrengthLabelHLayout_23.addWidget(self.cardanoFromXPublicKeyCardanoTypeQLabel)

        self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_23.addItem(self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_18.addWidget(self.cardanoFromXPublicKeyCardanoTypeLabelContainerQFrame)

        self.cardanoFromXPublicKeyCardanoTypeQComboBox = QComboBox(self.cardanoFromXPublicKeyCardanoTypeContainerQFrame)
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setObjectName(u"cardanoFromXPublicKeyCardanoTypeQComboBox")

        self.ClientVLayout_18.addWidget(self.cardanoFromXPublicKeyCardanoTypeQComboBox)


        self.horizontalLayout_64.addWidget(self.cardanoFromXPublicKeyCardanoTypeContainerQFrame)

        self.cardanoFromXPublicKeyAddressTypeContainerQFrame = QFrame(self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromXPublicKeyAddressTypeContainerQFrame.setObjectName(u"cardanoFromXPublicKeyAddressTypeContainerQFrame")
        self.cardanoFromXPublicKeyAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_20 = QVBoxLayout(self.cardanoFromXPublicKeyAddressTypeContainerQFrame)
        self.ClientVLayout_20.setSpacing(5)
        self.ClientVLayout_20.setObjectName(u"ClientVLayout_20")
        self.ClientVLayout_20.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromXPublicKeyAddressTypeContainerQFrame)
        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromXPublicKeyAddressTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_25 = QHBoxLayout(self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_25.setSpacing(15)
        self.MStrengthLabelHLayout_25.setObjectName(u"MStrengthLabelHLayout_25")
        self.MStrengthLabelHLayout_25.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromXPublicKeyAddressTypeQLabel = QLabel(self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromXPublicKeyAddressTypeQLabel.setObjectName(u"cardanoFromXPublicKeyAddressTypeQLabel")

        self.MStrengthLabelHLayout_25.addWidget(self.cardanoFromXPublicKeyAddressTypeQLabel)

        self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_25.addItem(self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_20.addWidget(self.cardanoFromXPublicKeyAddressTypeLabelContainerQFrame)

        self.cardanoFromXPublicKeyAddressTypeQComboBox = QComboBox(self.cardanoFromXPublicKeyAddressTypeContainerQFrame)
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setObjectName(u"cardanoFromXPublicKeyAddressTypeQComboBox")

        self.ClientVLayout_20.addWidget(self.cardanoFromXPublicKeyAddressTypeQComboBox)


        self.horizontalLayout_64.addWidget(self.cardanoFromXPublicKeyAddressTypeContainerQFrame)


        self.verticalLayout_40.addWidget(self.cardanoFromXPublicKeyCardanoTypeAndAddressTypeContainerQFrame)

        self.cardanoFromXPublicKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.cardanoFromXPublicKeyQStackedWidgetVSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromXPublicKeyQStackedWidget)
        self.cardanoFromPrivateKeyQStackedWidget = QWidget()
        self.cardanoFromPrivateKeyQStackedWidget.setObjectName(u"cardanoFromPrivateKeyQStackedWidget")
        self.verticalLayout_43 = QVBoxLayout(self.cardanoFromPrivateKeyQStackedWidget)
        self.verticalLayout_43.setSpacing(15)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyContainerQFrame = QFrame(self.cardanoFromPrivateKeyQStackedWidget)
        self.cardanoFromPrivateKeyContainerQFrame.setObjectName(u"cardanoFromPrivateKeyContainerQFrame")
        self.cardanoFromPrivateKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_3 = QVBoxLayout(self.cardanoFromPrivateKeyContainerQFrame)
        self.PrivateKeyVLayout_3.setSpacing(5)
        self.PrivateKeyVLayout_3.setObjectName(u"PrivateKeyVLayout_3")
        self.PrivateKeyVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyContainerLabelQFrame = QFrame(self.cardanoFromPrivateKeyContainerQFrame)
        self.cardanoFromPrivateKeyContainerLabelQFrame.setObjectName(u"cardanoFromPrivateKeyContainerLabelQFrame")
        self.PrivateKeyLabelHLayout_3 = QHBoxLayout(self.cardanoFromPrivateKeyContainerLabelQFrame)
        self.PrivateKeyLabelHLayout_3.setSpacing(15)
        self.PrivateKeyLabelHLayout_3.setObjectName(u"PrivateKeyLabelHLayout_3")
        self.PrivateKeyLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyContainerQLabel = QLabel(self.cardanoFromPrivateKeyContainerLabelQFrame)
        self.cardanoFromPrivateKeyContainerQLabel.setObjectName(u"cardanoFromPrivateKeyContainerQLabel")

        self.PrivateKeyLabelHLayout_3.addWidget(self.cardanoFromPrivateKeyContainerQLabel)

        self.cardanoFromPrivateKeyContainerLabelQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_3.addItem(self.cardanoFromPrivateKeyContainerLabelQFrameHSpacer)


        self.PrivateKeyVLayout_3.addWidget(self.cardanoFromPrivateKeyContainerLabelQFrame)

        self.cardanoFromPrivateKeyQLineEdit = QLineEdit(self.cardanoFromPrivateKeyContainerQFrame)
        self.cardanoFromPrivateKeyQLineEdit.setObjectName(u"cardanoFromPrivateKeyQLineEdit")

        self.PrivateKeyVLayout_3.addWidget(self.cardanoFromPrivateKeyQLineEdit)


        self.verticalLayout_43.addWidget(self.cardanoFromPrivateKeyContainerQFrame)

        self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame = QFrame(self.cardanoFromPrivateKeyQStackedWidget)
        self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame.setObjectName(u"cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame")
        self.horizontalLayout_65 = QHBoxLayout(self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.horizontalLayout_65.setSpacing(15)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyCardanoTypeContainerQFrame = QFrame(self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromPrivateKeyCardanoTypeContainerQFrame.setObjectName(u"cardanoFromPrivateKeyCardanoTypeContainerQFrame")
        self.cardanoFromPrivateKeyCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_21 = QVBoxLayout(self.cardanoFromPrivateKeyCardanoTypeContainerQFrame)
        self.ClientVLayout_21.setSpacing(5)
        self.ClientVLayout_21.setObjectName(u"ClientVLayout_21")
        self.ClientVLayout_21.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromPrivateKeyCardanoTypeContainerQFrame)
        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_26 = QHBoxLayout(self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_26.setSpacing(15)
        self.MStrengthLabelHLayout_26.setObjectName(u"MStrengthLabelHLayout_26")
        self.MStrengthLabelHLayout_26.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyCardanoTypeQLabel = QLabel(self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromPrivateKeyCardanoTypeQLabel.setObjectName(u"cardanoFromPrivateKeyCardanoTypeQLabel")

        self.MStrengthLabelHLayout_26.addWidget(self.cardanoFromPrivateKeyCardanoTypeQLabel)

        self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_26.addItem(self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_21.addWidget(self.cardanoFromPrivateKeyCardanoTypeLabelContainerQFrame)

        self.cardanoFromPrivateKeyCardanoTypeQComboBox = QComboBox(self.cardanoFromPrivateKeyCardanoTypeContainerQFrame)
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setObjectName(u"cardanoFromPrivateKeyCardanoTypeQComboBox")

        self.ClientVLayout_21.addWidget(self.cardanoFromPrivateKeyCardanoTypeQComboBox)


        self.horizontalLayout_65.addWidget(self.cardanoFromPrivateKeyCardanoTypeContainerQFrame)

        self.cardanoFromPrivateKeyAddressTypeContainerQFrame = QFrame(self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromPrivateKeyAddressTypeContainerQFrame.setObjectName(u"cardanoFromPrivateKeyAddressTypeContainerQFrame")
        self.cardanoFromPrivateKeyAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_22 = QVBoxLayout(self.cardanoFromPrivateKeyAddressTypeContainerQFrame)
        self.ClientVLayout_22.setSpacing(5)
        self.ClientVLayout_22.setObjectName(u"ClientVLayout_22")
        self.ClientVLayout_22.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromPrivateKeyAddressTypeContainerQFrame)
        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromPrivateKeyAddressTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_27 = QHBoxLayout(self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_27.setSpacing(15)
        self.MStrengthLabelHLayout_27.setObjectName(u"MStrengthLabelHLayout_27")
        self.MStrengthLabelHLayout_27.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPrivateKeyAddressTypeQLabel = QLabel(self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromPrivateKeyAddressTypeQLabel.setObjectName(u"cardanoFromPrivateKeyAddressTypeQLabel")

        self.MStrengthLabelHLayout_27.addWidget(self.cardanoFromPrivateKeyAddressTypeQLabel)

        self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_27.addItem(self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_22.addWidget(self.cardanoFromPrivateKeyAddressTypeLabelContainerQFrame)

        self.cardanoFromPrivateKeyAddressTypeQComboBox = QComboBox(self.cardanoFromPrivateKeyAddressTypeContainerQFrame)
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setObjectName(u"cardanoFromPrivateKeyAddressTypeQComboBox")

        self.ClientVLayout_22.addWidget(self.cardanoFromPrivateKeyAddressTypeQComboBox)


        self.horizontalLayout_65.addWidget(self.cardanoFromPrivateKeyAddressTypeContainerQFrame)


        self.verticalLayout_43.addWidget(self.cardanoFromPrivateKeyCardanoTypeAndAddressTypeContainerQFrame)

        self.cardanoFromPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.cardanoFromPrivateKeyQStackedWidgetVSpacer)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromPrivateKeyQStackedWidget)
        self.cardanoFromPublicKeyQStackedWidget = QWidget()
        self.cardanoFromPublicKeyQStackedWidget.setObjectName(u"cardanoFromPublicKeyQStackedWidget")
        self.verticalLayout_44 = QVBoxLayout(self.cardanoFromPublicKeyQStackedWidget)
        self.verticalLayout_44.setSpacing(15)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyContainerQFrame = QFrame(self.cardanoFromPublicKeyQStackedWidget)
        self.cardanoFromPublicKeyContainerQFrame.setObjectName(u"cardanoFromPublicKeyContainerQFrame")
        self.PublicKeyVLayout_3 = QVBoxLayout(self.cardanoFromPublicKeyContainerQFrame)
        self.PublicKeyVLayout_3.setSpacing(5)
        self.PublicKeyVLayout_3.setObjectName(u"PublicKeyVLayout_3")
        self.PublicKeyVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyLabelContainerQFrame = QFrame(self.cardanoFromPublicKeyContainerQFrame)
        self.cardanoFromPublicKeyLabelContainerQFrame.setObjectName(u"cardanoFromPublicKeyLabelContainerQFrame")
        self.PublicKeyLabelHLayout_3 = QHBoxLayout(self.cardanoFromPublicKeyLabelContainerQFrame)
        self.PublicKeyLabelHLayout_3.setSpacing(15)
        self.PublicKeyLabelHLayout_3.setObjectName(u"PublicKeyLabelHLayout_3")
        self.PublicKeyLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyQLabel = QLabel(self.cardanoFromPublicKeyLabelContainerQFrame)
        self.cardanoFromPublicKeyQLabel.setObjectName(u"cardanoFromPublicKeyQLabel")

        self.PublicKeyLabelHLayout_3.addWidget(self.cardanoFromPublicKeyQLabel)

        self.cardanoFromPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PublicKeyLabelHLayout_3.addItem(self.cardanoFromPublicKeyLabelContainerQFrameHSpacer)


        self.PublicKeyVLayout_3.addWidget(self.cardanoFromPublicKeyLabelContainerQFrame)

        self.cardanoFromPublicKeyQLineEdit = QLineEdit(self.cardanoFromPublicKeyContainerQFrame)
        self.cardanoFromPublicKeyQLineEdit.setObjectName(u"cardanoFromPublicKeyQLineEdit")

        self.PublicKeyVLayout_3.addWidget(self.cardanoFromPublicKeyQLineEdit)


        self.verticalLayout_44.addWidget(self.cardanoFromPublicKeyContainerQFrame)

        self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame = QFrame(self.cardanoFromPublicKeyQStackedWidget)
        self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame.setObjectName(u"cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame")
        self.horizontalLayout_66 = QHBoxLayout(self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.horizontalLayout_66.setSpacing(15)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyCardanoTypeContainerQFrame = QFrame(self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromPublicKeyCardanoTypeContainerQFrame.setObjectName(u"cardanoFromPublicKeyCardanoTypeContainerQFrame")
        self.cardanoFromPublicKeyCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_23 = QVBoxLayout(self.cardanoFromPublicKeyCardanoTypeContainerQFrame)
        self.ClientVLayout_23.setSpacing(5)
        self.ClientVLayout_23.setObjectName(u"ClientVLayout_23")
        self.ClientVLayout_23.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromPublicKeyCardanoTypeContainerQFrame)
        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromPublicKeyCardanoTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_28 = QHBoxLayout(self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_28.setSpacing(15)
        self.MStrengthLabelHLayout_28.setObjectName(u"MStrengthLabelHLayout_28")
        self.MStrengthLabelHLayout_28.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyCardanoTypeQLabel = QLabel(self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrame)
        self.cardanoFromPublicKeyCardanoTypeQLabel.setObjectName(u"cardanoFromPublicKeyCardanoTypeQLabel")

        self.MStrengthLabelHLayout_28.addWidget(self.cardanoFromPublicKeyCardanoTypeQLabel)

        self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_28.addItem(self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_23.addWidget(self.cardanoFromPublicKeyCardanoTypeLabelContainerQFrame)

        self.cardanoFromPublicKeyCardanoTypeQComboBox = QComboBox(self.cardanoFromPublicKeyCardanoTypeContainerQFrame)
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setObjectName(u"cardanoFromPublicKeyCardanoTypeQComboBox")

        self.ClientVLayout_23.addWidget(self.cardanoFromPublicKeyCardanoTypeQComboBox)


        self.horizontalLayout_66.addWidget(self.cardanoFromPublicKeyCardanoTypeContainerQFrame)

        self.cardanoFromPublicKeyAddressTypeContainerQFrame = QFrame(self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame)
        self.cardanoFromPublicKeyAddressTypeContainerQFrame.setObjectName(u"cardanoFromPublicKeyAddressTypeContainerQFrame")
        self.cardanoFromPublicKeyAddressTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_24 = QVBoxLayout(self.cardanoFromPublicKeyAddressTypeContainerQFrame)
        self.ClientVLayout_24.setSpacing(5)
        self.ClientVLayout_24.setObjectName(u"ClientVLayout_24")
        self.ClientVLayout_24.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrame = QFrame(self.cardanoFromPublicKeyAddressTypeContainerQFrame)
        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrame.setObjectName(u"cardanoFromPublicKeyAddressTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_29 = QHBoxLayout(self.cardanoFromPublicKeyAddressTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_29.setSpacing(15)
        self.MStrengthLabelHLayout_29.setObjectName(u"MStrengthLabelHLayout_29")
        self.MStrengthLabelHLayout_29.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromPublicKeyAddressTypeQLabel = QLabel(self.cardanoFromPublicKeyAddressTypeLabelContainerQFrame)
        self.cardanoFromPublicKeyAddressTypeQLabel.setObjectName(u"cardanoFromPublicKeyAddressTypeQLabel")

        self.MStrengthLabelHLayout_29.addWidget(self.cardanoFromPublicKeyAddressTypeQLabel)

        self.cardanoFromPublicKeyAddressTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_29.addItem(self.cardanoFromPublicKeyAddressTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_24.addWidget(self.cardanoFromPublicKeyAddressTypeLabelContainerQFrame)

        self.cardanoFromPublicKeyAddressTypeQComboBox = QComboBox(self.cardanoFromPublicKeyAddressTypeContainerQFrame)
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.addItem("")
        self.cardanoFromPublicKeyAddressTypeQComboBox.setObjectName(u"cardanoFromPublicKeyAddressTypeQComboBox")

        self.ClientVLayout_24.addWidget(self.cardanoFromPublicKeyAddressTypeQComboBox)


        self.horizontalLayout_66.addWidget(self.cardanoFromPublicKeyAddressTypeContainerQFrame)


        self.verticalLayout_44.addWidget(self.cardanoFromPublicKeyCardanoTypeAndAddressTypeContainerQFrame)

        self.cardanoFromPublicKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_44.addItem(self.cardanoFromPublicKeyQStackedWidgetVSpacer)

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
        self.verticalLayout_46 = QVBoxLayout(self.electrumV1FromEntropyQStackedWidget)
        self.verticalLayout_46.setSpacing(15)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyContainerQFrame = QFrame(self.electrumV1FromEntropyQStackedWidget)
        self.electrumV1FromEntropyContainerQFrame.setObjectName(u"electrumV1FromEntropyContainerQFrame")
        self.verticalLayout_47 = QVBoxLayout(self.electrumV1FromEntropyContainerQFrame)
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyLabelContainerQFrame = QFrame(self.electrumV1FromEntropyContainerQFrame)
        self.electrumV1FromEntropyLabelContainerQFrame.setObjectName(u"electrumV1FromEntropyLabelContainerQFrame")
        self.EntropyLabelHLayout_5 = QHBoxLayout(self.electrumV1FromEntropyLabelContainerQFrame)
        self.EntropyLabelHLayout_5.setSpacing(15)
        self.EntropyLabelHLayout_5.setObjectName(u"EntropyLabelHLayout_5")
        self.EntropyLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyQLabel = QLabel(self.electrumV1FromEntropyLabelContainerQFrame)
        self.electrumV1FromEntropyQLabel.setObjectName(u"electrumV1FromEntropyQLabel")

        self.EntropyLabelHLayout_5.addWidget(self.electrumV1FromEntropyQLabel)

        self.electrumV1FromEntropyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_5.addItem(self.electrumV1FromEntropyLabelContainerQFrameHSpacer)


        self.verticalLayout_47.addWidget(self.electrumV1FromEntropyLabelContainerQFrame)

        self.electrumV1FromEntropyGenerateContainerQFrame = QFrame(self.electrumV1FromEntropyContainerQFrame)
        self.electrumV1FromEntropyGenerateContainerQFrame.setObjectName(u"electrumV1FromEntropyGenerateContainerQFrame")
        self.horizontalLayout_43 = QHBoxLayout(self.electrumV1FromEntropyGenerateContainerQFrame)
        self.horizontalLayout_43.setSpacing(15)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyQLineEdit = QLineEdit(self.electrumV1FromEntropyGenerateContainerQFrame)
        self.electrumV1FromEntropyQLineEdit.setObjectName(u"electrumV1FromEntropyQLineEdit")

        self.horizontalLayout_43.addWidget(self.electrumV1FromEntropyQLineEdit)


        self.verticalLayout_47.addWidget(self.electrumV1FromEntropyGenerateContainerQFrame)


        self.verticalLayout_46.addWidget(self.electrumV1FromEntropyContainerQFrame)

        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame = QFrame(self.electrumV1FromEntropyQStackedWidget)
        self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame.setObjectName(u"electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame")
        self.horizontalLayout_44 = QHBoxLayout(self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame)
        self.horizontalLayout_44.setSpacing(15)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromEntropyPublicKeyTypeContainerQFrame")
        self.electrumV1FromEntropyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_10 = QVBoxLayout(self.electrumV1FromEntropyPublicKeyTypeContainerQFrame)
        self.ClientVLayout_10.setSpacing(5)
        self.ClientVLayout_10.setObjectName(u"ClientVLayout_10")
        self.ClientVLayout_10.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromEntropyPublicKeyTypeContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_13 = QHBoxLayout(self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_13.setSpacing(15)
        self.MStrengthLabelHLayout_13.setObjectName(u"MStrengthLabelHLayout_13")
        self.MStrengthLabelHLayout_13.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPublicKeyTypeQLabel = QLabel(self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeQLabel.setObjectName(u"electrumV1FromEntropyPublicKeyTypeQLabel")

        self.MStrengthLabelHLayout_13.addWidget(self.electrumV1FromEntropyPublicKeyTypeQLabel)

        self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_13.addItem(self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_10.addWidget(self.electrumV1FromEntropyPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromEntropyPublicKeyTypeQComboBox = QComboBox(self.electrumV1FromEntropyPublicKeyTypeContainerQFrame)
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromEntropyPublicKeyTypeQComboBox")

        self.ClientVLayout_10.addWidget(self.electrumV1FromEntropyPublicKeyTypeQComboBox)


        self.horizontalLayout_44.addWidget(self.electrumV1FromEntropyPublicKeyTypeContainerQFrame)

        self.electrumV1FromEntropyPassphraseContainerQFrame = QFrame(self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromEntropyPassphraseContainerQFrame.setObjectName(u"electrumV1FromEntropyPassphraseContainerQFrame")
        self.EPassphraseVLayout_7 = QVBoxLayout(self.electrumV1FromEntropyPassphraseContainerQFrame)
        self.EPassphraseVLayout_7.setSpacing(5)
        self.EPassphraseVLayout_7.setObjectName(u"EPassphraseVLayout_7")
        self.EPassphraseVLayout_7.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPassphraseLabelContainerQFrame = QFrame(self.electrumV1FromEntropyPassphraseContainerQFrame)
        self.electrumV1FromEntropyPassphraseLabelContainerQFrame.setObjectName(u"electrumV1FromEntropyPassphraseLabelContainerQFrame")
        self.EPassphraseLabelHLayout_7 = QHBoxLayout(self.electrumV1FromEntropyPassphraseLabelContainerQFrame)
        self.EPassphraseLabelHLayout_7.setSpacing(15)
        self.EPassphraseLabelHLayout_7.setObjectName(u"EPassphraseLabelHLayout_7")
        self.EPassphraseLabelHLayout_7.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPassphraseQLabel = QLabel(self.electrumV1FromEntropyPassphraseLabelContainerQFrame)
        self.electrumV1FromEntropyPassphraseQLabel.setObjectName(u"electrumV1FromEntropyPassphraseQLabel")

        self.EPassphraseLabelHLayout_7.addWidget(self.electrumV1FromEntropyPassphraseQLabel)

        self.electrumV1FromEntropyPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_7.addItem(self.electrumV1FromEntropyPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout_7.addWidget(self.electrumV1FromEntropyPassphraseLabelContainerQFrame)

        self.electrumV1FromEntropyPassphraseGenerateContainerQFrame = QFrame(self.electrumV1FromEntropyPassphraseContainerQFrame)
        self.electrumV1FromEntropyPassphraseGenerateContainerQFrame.setObjectName(u"electrumV1FromEntropyPassphraseGenerateContainerQFrame")
        self.horizontalLayout_45 = QHBoxLayout(self.electrumV1FromEntropyPassphraseGenerateContainerQFrame)
        self.horizontalLayout_45.setSpacing(15)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyPassphraseGenerateQLineEdit = QLineEdit(self.electrumV1FromEntropyPassphraseGenerateContainerQFrame)
        self.electrumV1FromEntropyPassphraseGenerateQLineEdit.setObjectName(u"electrumV1FromEntropyPassphraseGenerateQLineEdit")

        self.horizontalLayout_45.addWidget(self.electrumV1FromEntropyPassphraseGenerateQLineEdit)


        self.EPassphraseVLayout_7.addWidget(self.electrumV1FromEntropyPassphraseGenerateContainerQFrame)


        self.horizontalLayout_44.addWidget(self.electrumV1FromEntropyPassphraseContainerQFrame)


        self.verticalLayout_46.addWidget(self.electrumV1FromEntropyPublicKeyTypeAndPassphraseContainerQFrame)

        self.electrumV1FromEntropyLanguageAndWordsContainerQFrame = QFrame(self.electrumV1FromEntropyQStackedWidget)
        self.electrumV1FromEntropyLanguageAndWordsContainerQFrame.setObjectName(u"electrumV1FromEntropyLanguageAndWordsContainerQFrame")
        self.horizontalLayout_46 = QHBoxLayout(self.electrumV1FromEntropyLanguageAndWordsContainerQFrame)
        self.horizontalLayout_46.setSpacing(15)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyLanguageContainerQFrame = QFrame(self.electrumV1FromEntropyLanguageAndWordsContainerQFrame)
        self.electrumV1FromEntropyLanguageContainerQFrame.setObjectName(u"electrumV1FromEntropyLanguageContainerQFrame")
        self.ELanguageVLayout_4 = QVBoxLayout(self.electrumV1FromEntropyLanguageContainerQFrame)
        self.ELanguageVLayout_4.setSpacing(5)
        self.ELanguageVLayout_4.setObjectName(u"ELanguageVLayout_4")
        self.ELanguageVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyLanguageLabelContainerQFrame = QFrame(self.electrumV1FromEntropyLanguageContainerQFrame)
        self.electrumV1FromEntropyLanguageLabelContainerQFrame.setObjectName(u"electrumV1FromEntropyLanguageLabelContainerQFrame")
        self.ELanguageLabelHLayout_4 = QHBoxLayout(self.electrumV1FromEntropyLanguageLabelContainerQFrame)
        self.ELanguageLabelHLayout_4.setSpacing(15)
        self.ELanguageLabelHLayout_4.setObjectName(u"ELanguageLabelHLayout_4")
        self.ELanguageLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyLanguageQLabel = QLabel(self.electrumV1FromEntropyLanguageLabelContainerQFrame)
        self.electrumV1FromEntropyLanguageQLabel.setObjectName(u"electrumV1FromEntropyLanguageQLabel")

        self.ELanguageLabelHLayout_4.addWidget(self.electrumV1FromEntropyLanguageQLabel)

        self.electrumV1FromEntropyLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout_4.addItem(self.electrumV1FromEntropyLanguageLabelContainerQFrameHSpacer)


        self.ELanguageVLayout_4.addWidget(self.electrumV1FromEntropyLanguageLabelContainerQFrame)

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

        self.ELanguageVLayout_4.addWidget(self.electrumV1FromEntropyLanguageQComboBox)


        self.horizontalLayout_46.addWidget(self.electrumV1FromEntropyLanguageContainerQFrame)

        self.electrumV1FromEntropyWordsContainerQFrame = QFrame(self.electrumV1FromEntropyLanguageAndWordsContainerQFrame)
        self.electrumV1FromEntropyWordsContainerQFrame.setObjectName(u"electrumV1FromEntropyWordsContainerQFrame")
        self.EStrengthVLayout_4 = QVBoxLayout(self.electrumV1FromEntropyWordsContainerQFrame)
        self.EStrengthVLayout_4.setSpacing(5)
        self.EStrengthVLayout_4.setObjectName(u"EStrengthVLayout_4")
        self.EStrengthVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyWordsLabelContainerQFrame = QFrame(self.electrumV1FromEntropyWordsContainerQFrame)
        self.electrumV1FromEntropyWordsLabelContainerQFrame.setObjectName(u"electrumV1FromEntropyWordsLabelContainerQFrame")
        self.EStrengthLabelHLayout_4 = QHBoxLayout(self.electrumV1FromEntropyWordsLabelContainerQFrame)
        self.EStrengthLabelHLayout_4.setSpacing(15)
        self.EStrengthLabelHLayout_4.setObjectName(u"EStrengthLabelHLayout_4")
        self.EStrengthLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyWordsQLabel = QLabel(self.electrumV1FromEntropyWordsLabelContainerQFrame)
        self.electrumV1FromEntropyWordsQLabel.setObjectName(u"electrumV1FromEntropyWordsQLabel")

        self.EStrengthLabelHLayout_4.addWidget(self.electrumV1FromEntropyWordsQLabel)

        self.electrumV1FromEntropyWordsLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout_4.addItem(self.electrumV1FromEntropyWordsLabelContainerQFrameHSpacer)


        self.EStrengthVLayout_4.addWidget(self.electrumV1FromEntropyWordsLabelContainerQFrame)

        self.electrumV1FromEntropyWordsQComboBox = QComboBox(self.electrumV1FromEntropyWordsContainerQFrame)
        self.electrumV1FromEntropyWordsQComboBox.addItem("")
        self.electrumV1FromEntropyWordsQComboBox.addItem("")
        self.electrumV1FromEntropyWordsQComboBox.addItem("")
        self.electrumV1FromEntropyWordsQComboBox.addItem("")
        self.electrumV1FromEntropyWordsQComboBox.addItem("")
        self.electrumV1FromEntropyWordsQComboBox.setObjectName(u"electrumV1FromEntropyWordsQComboBox")

        self.EStrengthVLayout_4.addWidget(self.electrumV1FromEntropyWordsQComboBox)


        self.horizontalLayout_46.addWidget(self.electrumV1FromEntropyWordsContainerQFrame)


        self.verticalLayout_46.addWidget(self.electrumV1FromEntropyLanguageAndWordsContainerQFrame)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromEntropyQStackedWidget)
        self.electrumV1FromMnemonicQStackedWidget = QWidget()
        self.electrumV1FromMnemonicQStackedWidget.setObjectName(u"electrumV1FromMnemonicQStackedWidget")
        self.verticalLayout_48 = QVBoxLayout(self.electrumV1FromMnemonicQStackedWidget)
        self.verticalLayout_48.setSpacing(15)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicContainerQFrame = QFrame(self.electrumV1FromMnemonicQStackedWidget)
        self.electrumV1FromMnemonicContainerQFrame.setObjectName(u"electrumV1FromMnemonicContainerQFrame")
        self.MnemonicVLayout_4 = QVBoxLayout(self.electrumV1FromMnemonicContainerQFrame)
        self.MnemonicVLayout_4.setSpacing(5)
        self.MnemonicVLayout_4.setObjectName(u"MnemonicVLayout_4")
        self.MnemonicVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicLabelContainerQFrame = QFrame(self.electrumV1FromMnemonicContainerQFrame)
        self.electrumV1FromMnemonicLabelContainerQFrame.setObjectName(u"electrumV1FromMnemonicLabelContainerQFrame")
        self.MnemonicLabelHLayout_4 = QHBoxLayout(self.electrumV1FromMnemonicLabelContainerQFrame)
        self.MnemonicLabelHLayout_4.setSpacing(15)
        self.MnemonicLabelHLayout_4.setObjectName(u"MnemonicLabelHLayout_4")
        self.MnemonicLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicQLabel = QLabel(self.electrumV1FromMnemonicLabelContainerQFrame)
        self.electrumV1FromMnemonicQLabel.setObjectName(u"electrumV1FromMnemonicQLabel")

        self.MnemonicLabelHLayout_4.addWidget(self.electrumV1FromMnemonicQLabel)

        self.electrumV1FromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout_4.addItem(self.electrumV1FromMnemonicLabelContainerQFrameHSpacer)


        self.MnemonicVLayout_4.addWidget(self.electrumV1FromMnemonicLabelContainerQFrame)

        self.electrumV1FromMnemonicGenerateContainerQFrame = QFrame(self.electrumV1FromMnemonicContainerQFrame)
        self.electrumV1FromMnemonicGenerateContainerQFrame.setObjectName(u"electrumV1FromMnemonicGenerateContainerQFrame")
        self.horizontalLayout_47 = QHBoxLayout(self.electrumV1FromMnemonicGenerateContainerQFrame)
        self.horizontalLayout_47.setSpacing(15)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicGenerateQLineEdit = QLineEdit(self.electrumV1FromMnemonicGenerateContainerQFrame)
        self.electrumV1FromMnemonicGenerateQLineEdit.setObjectName(u"electrumV1FromMnemonicGenerateQLineEdit")

        self.horizontalLayout_47.addWidget(self.electrumV1FromMnemonicGenerateQLineEdit)


        self.MnemonicVLayout_4.addWidget(self.electrumV1FromMnemonicGenerateContainerQFrame)


        self.verticalLayout_48.addWidget(self.electrumV1FromMnemonicContainerQFrame)

        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame = QFrame(self.electrumV1FromMnemonicQStackedWidget)
        self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame")
        self.horizontalLayout_48 = QHBoxLayout(self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame)
        self.horizontalLayout_48.setSpacing(15)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeContainerQFrame")
        self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_11 = QVBoxLayout(self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame)
        self.ClientVLayout_11.setSpacing(5)
        self.ClientVLayout_11.setObjectName(u"ClientVLayout_11")
        self.ClientVLayout_11.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_14 = QHBoxLayout(self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_14.setSpacing(15)
        self.MStrengthLabelHLayout_14.setObjectName(u"MStrengthLabelHLayout_14")
        self.MStrengthLabelHLayout_14.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPublicKeyTypeQLabel = QLabel(self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeQLabel.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeQLabel")

        self.MStrengthLabelHLayout_14.addWidget(self.electrumV1FromMnemonicPublicKeyTypeQLabel)

        self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_14.addItem(self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_11.addWidget(self.electrumV1FromMnemonicPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromMnemonicPublicKeyTypeQComboBox = QComboBox(self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame)
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromMnemonicPublicKeyTypeQComboBox")

        self.ClientVLayout_11.addWidget(self.electrumV1FromMnemonicPublicKeyTypeQComboBox)


        self.horizontalLayout_48.addWidget(self.electrumV1FromMnemonicPublicKeyTypeContainerQFrame)

        self.electrumV1FromMnemonicPassphraseContainerQFrame = QFrame(self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV1FromMnemonicPassphraseContainerQFrame.setObjectName(u"electrumV1FromMnemonicPassphraseContainerQFrame")
        self.EPassphraseVLayout_8 = QVBoxLayout(self.electrumV1FromMnemonicPassphraseContainerQFrame)
        self.EPassphraseVLayout_8.setSpacing(5)
        self.EPassphraseVLayout_8.setObjectName(u"EPassphraseVLayout_8")
        self.EPassphraseVLayout_8.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPassphraseLabelContainerQFrame = QFrame(self.electrumV1FromMnemonicPassphraseContainerQFrame)
        self.electrumV1FromMnemonicPassphraseLabelContainerQFrame.setObjectName(u"electrumV1FromMnemonicPassphraseLabelContainerQFrame")
        self.MPassphraseLabelHLayout_4 = QHBoxLayout(self.electrumV1FromMnemonicPassphraseLabelContainerQFrame)
        self.MPassphraseLabelHLayout_4.setSpacing(15)
        self.MPassphraseLabelHLayout_4.setObjectName(u"MPassphraseLabelHLayout_4")
        self.MPassphraseLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPassphraseQLabel = QLabel(self.electrumV1FromMnemonicPassphraseLabelContainerQFrame)
        self.electrumV1FromMnemonicPassphraseQLabel.setObjectName(u"electrumV1FromMnemonicPassphraseQLabel")

        self.MPassphraseLabelHLayout_4.addWidget(self.electrumV1FromMnemonicPassphraseQLabel)

        self.electrumV1FromMnemonicPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout_4.addItem(self.electrumV1FromMnemonicPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout_8.addWidget(self.electrumV1FromMnemonicPassphraseLabelContainerQFrame)

        self.electrumV1FromMnemonicPassphraseGenerateContainerQFrame = QFrame(self.electrumV1FromMnemonicPassphraseContainerQFrame)
        self.electrumV1FromMnemonicPassphraseGenerateContainerQFrame.setObjectName(u"electrumV1FromMnemonicPassphraseGenerateContainerQFrame")
        self.horizontalLayout_49 = QHBoxLayout(self.electrumV1FromMnemonicPassphraseGenerateContainerQFrame)
        self.horizontalLayout_49.setSpacing(15)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicPassphraseGenerateQLineEdit = QLineEdit(self.electrumV1FromMnemonicPassphraseGenerateContainerQFrame)
        self.electrumV1FromMnemonicPassphraseGenerateQLineEdit.setObjectName(u"electrumV1FromMnemonicPassphraseGenerateQLineEdit")

        self.horizontalLayout_49.addWidget(self.electrumV1FromMnemonicPassphraseGenerateQLineEdit)


        self.EPassphraseVLayout_8.addWidget(self.electrumV1FromMnemonicPassphraseGenerateContainerQFrame)


        self.horizontalLayout_48.addWidget(self.electrumV1FromMnemonicPassphraseContainerQFrame)


        self.verticalLayout_48.addWidget(self.electrumV1FromMnemonicPublicKeyTypeAndPassphraseContainerQFrame)

        self.electrumV1FromMnemonicLanguageAndWordsContainerQFrame = QFrame(self.electrumV1FromMnemonicQStackedWidget)
        self.electrumV1FromMnemonicLanguageAndWordsContainerQFrame.setObjectName(u"electrumV1FromMnemonicLanguageAndWordsContainerQFrame")
        self.electrumV1FromMnemonicLanguageAndWordsContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.electrumV1FromMnemonicLanguageAndWordsContainerQFrame)
        self.horizontalLayout_50.setSpacing(15)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicLanguageContainerQFrame = QFrame(self.electrumV1FromMnemonicLanguageAndWordsContainerQFrame)
        self.electrumV1FromMnemonicLanguageContainerQFrame.setObjectName(u"electrumV1FromMnemonicLanguageContainerQFrame")
        self.MLanguageVLayout_4 = QVBoxLayout(self.electrumV1FromMnemonicLanguageContainerQFrame)
        self.MLanguageVLayout_4.setSpacing(5)
        self.MLanguageVLayout_4.setObjectName(u"MLanguageVLayout_4")
        self.MLanguageVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicLanguageLabelContainerQFrame = QWidget(self.electrumV1FromMnemonicLanguageContainerQFrame)
        self.electrumV1FromMnemonicLanguageLabelContainerQFrame.setObjectName(u"electrumV1FromMnemonicLanguageLabelContainerQFrame")
        self.MLanguageLabelHLayout_4 = QHBoxLayout(self.electrumV1FromMnemonicLanguageLabelContainerQFrame)
        self.MLanguageLabelHLayout_4.setSpacing(15)
        self.MLanguageLabelHLayout_4.setObjectName(u"MLanguageLabelHLayout_4")
        self.MLanguageLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicLanguageQLabel = QLabel(self.electrumV1FromMnemonicLanguageLabelContainerQFrame)
        self.electrumV1FromMnemonicLanguageQLabel.setObjectName(u"electrumV1FromMnemonicLanguageQLabel")

        self.MLanguageLabelHLayout_4.addWidget(self.electrumV1FromMnemonicLanguageQLabel)

        self.electrumV1FromMnemonicLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MLanguageLabelHLayout_4.addItem(self.electrumV1FromMnemonicLanguageLabelContainerQFrameHSpacer)


        self.MLanguageVLayout_4.addWidget(self.electrumV1FromMnemonicLanguageLabelContainerQFrame)

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

        self.MLanguageVLayout_4.addWidget(self.electrumV1FromMnemonicLanguageQComboBox)


        self.horizontalLayout_50.addWidget(self.electrumV1FromMnemonicLanguageContainerQFrame)

        self.electrumV1FromMnemonicWordsContainerQFrame = QFrame(self.electrumV1FromMnemonicLanguageAndWordsContainerQFrame)
        self.electrumV1FromMnemonicWordsContainerQFrame.setObjectName(u"electrumV1FromMnemonicWordsContainerQFrame")
        self.MStrengthVLayout_4 = QVBoxLayout(self.electrumV1FromMnemonicWordsContainerQFrame)
        self.MStrengthVLayout_4.setSpacing(5)
        self.MStrengthVLayout_4.setObjectName(u"MStrengthVLayout_4")
        self.MStrengthVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicWordsLabelContainerQFrame = QFrame(self.electrumV1FromMnemonicWordsContainerQFrame)
        self.electrumV1FromMnemonicWordsLabelContainerQFrame.setObjectName(u"electrumV1FromMnemonicWordsLabelContainerQFrame")
        self.MStrengthLabelHLayout_15 = QHBoxLayout(self.electrumV1FromMnemonicWordsLabelContainerQFrame)
        self.MStrengthLabelHLayout_15.setSpacing(15)
        self.MStrengthLabelHLayout_15.setObjectName(u"MStrengthLabelHLayout_15")
        self.MStrengthLabelHLayout_15.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicWordsQLabel = QLabel(self.electrumV1FromMnemonicWordsLabelContainerQFrame)
        self.electrumV1FromMnemonicWordsQLabel.setObjectName(u"electrumV1FromMnemonicWordsQLabel")

        self.MStrengthLabelHLayout_15.addWidget(self.electrumV1FromMnemonicWordsQLabel)

        self.electrumV1FromMnemonicWordsLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_15.addItem(self.electrumV1FromMnemonicWordsLabelContainerQFrameHSpacer)


        self.MStrengthVLayout_4.addWidget(self.electrumV1FromMnemonicWordsLabelContainerQFrame)

        self.electrumV1FromMnemonicWordsQComboBox = QComboBox(self.electrumV1FromMnemonicWordsContainerQFrame)
        self.electrumV1FromMnemonicWordsQComboBox.addItem("")
        self.electrumV1FromMnemonicWordsQComboBox.setObjectName(u"electrumV1FromMnemonicWordsQComboBox")

        self.MStrengthVLayout_4.addWidget(self.electrumV1FromMnemonicWordsQComboBox)


        self.horizontalLayout_50.addWidget(self.electrumV1FromMnemonicWordsContainerQFrame)


        self.verticalLayout_48.addWidget(self.electrumV1FromMnemonicLanguageAndWordsContainerQFrame)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromMnemonicQStackedWidget)
        self.electrumV1FromSeedQStackedWidget = QWidget()
        self.electrumV1FromSeedQStackedWidget.setObjectName(u"electrumV1FromSeedQStackedWidget")
        self.verticalLayout_5 = QVBoxLayout(self.electrumV1FromSeedQStackedWidget)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromSeedQStackedWidget)
        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromSeedAndPublicKeyTypeContainerQFrame")
        self.horizontalLayout_51 = QHBoxLayout(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)
        self.horizontalLayout_51.setSpacing(15)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedContainerQFrame = QFrame(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromSeedContainerQFrame.setObjectName(u"electrumV1FromSeedContainerQFrame")
        self.verticalLayout_50 = QVBoxLayout(self.electrumV1FromSeedContainerQFrame)
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedLabelContainerQFrame = QFrame(self.electrumV1FromSeedContainerQFrame)
        self.electrumV1FromSeedLabelContainerQFrame.setObjectName(u"electrumV1FromSeedLabelContainerQFrame")
        self.SeedLabelHLayout_4 = QHBoxLayout(self.electrumV1FromSeedLabelContainerQFrame)
        self.SeedLabelHLayout_4.setSpacing(15)
        self.SeedLabelHLayout_4.setObjectName(u"SeedLabelHLayout_4")
        self.SeedLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedQLabel = QLabel(self.electrumV1FromSeedLabelContainerQFrame)
        self.electrumV1FromSeedQLabel.setObjectName(u"electrumV1FromSeedQLabel")

        self.SeedLabelHLayout_4.addWidget(self.electrumV1FromSeedQLabel)

        self.electrumV1FromSeedLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout_4.addItem(self.electrumV1FromSeedLabelContainerQFrameHSpacer)


        self.verticalLayout_50.addWidget(self.electrumV1FromSeedLabelContainerQFrame)

        self.electrumV1FromSeedQLineEdit = QLineEdit(self.electrumV1FromSeedContainerQFrame)
        self.electrumV1FromSeedQLineEdit.setObjectName(u"electrumV1FromSeedQLineEdit")

        self.verticalLayout_50.addWidget(self.electrumV1FromSeedQLineEdit)


        self.horizontalLayout_51.addWidget(self.electrumV1FromSeedContainerQFrame)

        self.electrumV1FromSeedsPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromSeedsPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromSeedsPublicKeyTypeContainerQFrame")
        self.electrumV1FromSeedsPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_12 = QVBoxLayout(self.electrumV1FromSeedsPublicKeyTypeContainerQFrame)
        self.ClientVLayout_12.setSpacing(5)
        self.ClientVLayout_12.setObjectName(u"ClientVLayout_12")
        self.ClientVLayout_12.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromSeedsPublicKeyTypeContainerQFrame)
        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromSeedPublicKeyTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_16 = QHBoxLayout(self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_16.setSpacing(15)
        self.MStrengthLabelHLayout_16.setObjectName(u"MStrengthLabelHLayout_16")
        self.MStrengthLabelHLayout_16.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedPublicKeyTypeQLabel = QLabel(self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromSeedPublicKeyTypeQLabel.setObjectName(u"electrumV1FromSeedPublicKeyTypeQLabel")

        self.MStrengthLabelHLayout_16.addWidget(self.electrumV1FromSeedPublicKeyTypeQLabel)

        self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_16.addItem(self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_12.addWidget(self.electrumV1FromSeedPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromClientQComboBox = QComboBox(self.electrumV1FromSeedsPublicKeyTypeContainerQFrame)
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.setObjectName(u"electrumV1FromClientQComboBox")

        self.ClientVLayout_12.addWidget(self.electrumV1FromClientQComboBox)


        self.horizontalLayout_51.addWidget(self.electrumV1FromSeedsPublicKeyTypeContainerQFrame)


        self.verticalLayout_5.addWidget(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)

        self.electrumV1FromSeedQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.electrumV1FromSeedQStackedWidgetVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromSeedQStackedWidget)
        self.electrumV1FromWIFQStackedWidget = QWidget()
        self.electrumV1FromWIFQStackedWidget.setObjectName(u"electrumV1FromWIFQStackedWidget")
        self.verticalLayout_53 = QVBoxLayout(self.electrumV1FromWIFQStackedWidget)
        self.verticalLayout_53.setSpacing(15)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFContainerQFrame = QFrame(self.electrumV1FromWIFQStackedWidget)
        self.electrumV1FromWIFContainerQFrame.setObjectName(u"electrumV1FromWIFContainerQFrame")
        self.electrumV1FromWIFContainerQFrame.setMinimumSize(QSize(400, 0))
        self.WIFVLayout_4 = QVBoxLayout(self.electrumV1FromWIFContainerQFrame)
        self.WIFVLayout_4.setSpacing(5)
        self.WIFVLayout_4.setObjectName(u"WIFVLayout_4")
        self.WIFVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFLabelContainerQFrame = QFrame(self.electrumV1FromWIFContainerQFrame)
        self.electrumV1FromWIFLabelContainerQFrame.setObjectName(u"electrumV1FromWIFLabelContainerQFrame")
        self.WIFLabelHLayout_4 = QHBoxLayout(self.electrumV1FromWIFLabelContainerQFrame)
        self.WIFLabelHLayout_4.setSpacing(15)
        self.WIFLabelHLayout_4.setObjectName(u"WIFLabelHLayout_4")
        self.WIFLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFQLabel = QLabel(self.electrumV1FromWIFLabelContainerQFrame)
        self.electrumV1FromWIFQLabel.setObjectName(u"electrumV1FromWIFQLabel")

        self.WIFLabelHLayout_4.addWidget(self.electrumV1FromWIFQLabel)

        self.electrumV1FromWIFLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WIFLabelHLayout_4.addItem(self.electrumV1FromWIFLabelContainerQFrameHSpacer)


        self.WIFVLayout_4.addWidget(self.electrumV1FromWIFLabelContainerQFrame)

        self.electrumV1FromWIFQLineEdit = QLineEdit(self.electrumV1FromWIFContainerQFrame)
        self.electrumV1FromWIFQLineEdit.setObjectName(u"electrumV1FromWIFQLineEdit")

        self.WIFVLayout_4.addWidget(self.electrumV1FromWIFQLineEdit)


        self.verticalLayout_53.addWidget(self.electrumV1FromWIFContainerQFrame)

        self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromWIFQStackedWidget)
        self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame")
        self.horizontalLayout_52 = QHBoxLayout(self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame)
        self.horizontalLayout_52.setSpacing(15)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromWIFPublicKeyTypeContainerQFrame")
        self.electrumV1FromWIFPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.verticalLayout_81 = QVBoxLayout(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)
        self.verticalLayout_81.setSpacing(5)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromWIFPublicKeyTypeLabelContainerQFrame")
        self.horizontalLayout_77 = QHBoxLayout(self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame)
        self.horizontalLayout_77.setSpacing(15)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFPublicKeyTypeQLabel = QLabel(self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeQLabel.setObjectName(u"electrumV1FromWIFPublicKeyTypeQLabel")

        self.horizontalLayout_77.addWidget(self.electrumV1FromWIFPublicKeyTypeQLabel)

        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_77.addItem(self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_81.addWidget(self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromWIFPublicKeyTypeQComboBox = QComboBox(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromWIFPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromWIFPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromWIFPublicKeyTypeQComboBox")

        self.verticalLayout_81.addWidget(self.electrumV1FromWIFPublicKeyTypeQComboBox)


        self.horizontalLayout_52.addWidget(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)

        self.electrumV1FromWIFBIP38PassphraseContainerQFrame = QFrame(self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseContainerQFrame.setObjectName(u"electrumV1FromWIFBIP38PassphraseContainerQFrame")
        self.verticalLayout_54 = QVBoxLayout(self.electrumV1FromWIFBIP38PassphraseContainerQFrame)
        self.verticalLayout_54.setSpacing(5)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame = QFrame(self.electrumV1FromWIFBIP38PassphraseContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame.setObjectName(u"electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame")
        self.EPassphraseLabelHLayout_8 = QHBoxLayout(self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame)
        self.EPassphraseLabelHLayout_8.setSpacing(15)
        self.EPassphraseLabelHLayout_8.setObjectName(u"EPassphraseLabelHLayout_8")
        self.EPassphraseLabelHLayout_8.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFBIP38PassphraseQCheckBox = QCheckBox(self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseQCheckBox.setObjectName(u"electrumV1FromWIFBIP38PassphraseQCheckBox")

        self.EPassphraseLabelHLayout_8.addWidget(self.electrumV1FromWIFBIP38PassphraseQCheckBox)

        self.electrumV1FromWIFBIP38PassphraseContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_8.addItem(self.electrumV1FromWIFBIP38PassphraseContainerQFrameHSpacer)


        self.verticalLayout_54.addWidget(self.electrumV1FromWIFBIP38PassphraseCheckBoxContainerQFrame)

        self.electrumV1FromWIFBIP38PassphraseQLineEdit = QLineEdit(self.electrumV1FromWIFBIP38PassphraseContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseQLineEdit.setObjectName(u"electrumV1FromWIFBIP38PassphraseQLineEdit")

        self.verticalLayout_54.addWidget(self.electrumV1FromWIFBIP38PassphraseQLineEdit)


        self.horizontalLayout_52.addWidget(self.electrumV1FromWIFBIP38PassphraseContainerQFrame)


        self.verticalLayout_53.addWidget(self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame)

        self.electrumV1FromWIFQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.electrumV1FromWIFQStackedWidgetVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromWIFQStackedWidget)
        self.electrumV1FromPrivateKeyQStackedWidget = QWidget()
        self.electrumV1FromPrivateKeyQStackedWidget.setObjectName(u"electrumV1FromPrivateKeyQStackedWidget")
        self.verticalLayout_55 = QVBoxLayout(self.electrumV1FromPrivateKeyQStackedWidget)
        self.verticalLayout_55.setSpacing(15)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromPrivateKeyQStackedWidget)
        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame")
        self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.horizontalLayout_72.setSpacing(15)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyContainerQFrame = QFrame(self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromPrivateKeyContainerQFrame.setObjectName(u"electrumV1FromPrivateKeyContainerQFrame")
        self.PrivateKeyVLayout_4 = QVBoxLayout(self.electrumV1FromPrivateKeyContainerQFrame)
        self.PrivateKeyVLayout_4.setSpacing(5)
        self.PrivateKeyVLayout_4.setObjectName(u"PrivateKeyVLayout_4")
        self.PrivateKeyVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyLabelContainerQFrame = QFrame(self.electrumV1FromPrivateKeyContainerQFrame)
        self.electrumV1FromPrivateKeyLabelContainerQFrame.setObjectName(u"electrumV1FromPrivateKeyLabelContainerQFrame")
        self.PrivateKeyLabelHLayout_4 = QHBoxLayout(self.electrumV1FromPrivateKeyLabelContainerQFrame)
        self.PrivateKeyLabelHLayout_4.setSpacing(15)
        self.PrivateKeyLabelHLayout_4.setObjectName(u"PrivateKeyLabelHLayout_4")
        self.PrivateKeyLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyQLabel = QLabel(self.electrumV1FromPrivateKeyLabelContainerQFrame)
        self.electrumV1FromPrivateKeyQLabel.setObjectName(u"electrumV1FromPrivateKeyQLabel")

        self.PrivateKeyLabelHLayout_4.addWidget(self.electrumV1FromPrivateKeyQLabel)

        self.electrumV1FromPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_4.addItem(self.electrumV1FromPrivateKeyLabelContainerQFrameHSpacer)


        self.PrivateKeyVLayout_4.addWidget(self.electrumV1FromPrivateKeyLabelContainerQFrame)

        self.electrumV1FromPrivateKeyQLineEdit = QLineEdit(self.electrumV1FromPrivateKeyContainerQFrame)
        self.electrumV1FromPrivateKeyQLineEdit.setObjectName(u"electrumV1FromPrivateKeyQLineEdit")

        self.PrivateKeyVLayout_4.addWidget(self.electrumV1FromPrivateKeyQLineEdit)


        self.horizontalLayout_72.addWidget(self.electrumV1FromPrivateKeyContainerQFrame)

        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame")
        self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.verticalLayout_91 = QVBoxLayout(self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame)
        self.verticalLayout_91.setSpacing(5)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame")
        self.horizontalLayout_80 = QHBoxLayout(self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame)
        self.horizontalLayout_80.setSpacing(15)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyPublicKeyTypeQLabel = QLabel(self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromPrivateKeyPublicKeyTypeQLabel.setObjectName(u"electrumV1FromPrivateKeyPublicKeyTypeQLabel")

        self.horizontalLayout_80.addWidget(self.electrumV1FromPrivateKeyPublicKeyTypeQLabel)

        self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_91.addWidget(self.electrumV1FromPrivateKeyPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox = QComboBox(self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromPrivateKeyPublicKeyTypeQComboBox")

        self.verticalLayout_91.addWidget(self.electrumV1FromPrivateKeyPublicKeyTypeQComboBox)


        self.horizontalLayout_72.addWidget(self.electrumV1FromPrivateKeyPublicKeyTypeContainerQFrame)


        self.verticalLayout_55.addWidget(self.electrumV1FromPrivateKeyAndPublicKeyTypeContainerQFrame)

        self.electrumV1FromPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.electrumV1FromPrivateKeyQStackedWidgetVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromPrivateKeyQStackedWidget)
        self.electrumV1FromPublicKeyQStackedWidget = QWidget()
        self.electrumV1FromPublicKeyQStackedWidget.setObjectName(u"electrumV1FromPublicKeyQStackedWidget")
        self.verticalLayout_56 = QVBoxLayout(self.electrumV1FromPublicKeyQStackedWidget)
        self.verticalLayout_56.setSpacing(15)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromPublicKeyQStackedWidget)
        self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame")
        self.horizontalLayout_78 = QHBoxLayout(self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.horizontalLayout_78.setSpacing(15)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyContainerQFrame = QFrame(self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyContainerQFrame.setObjectName(u"electrumV1FromPublicKeyContainerQFrame")
        self.PublicKeyVLayout_4 = QVBoxLayout(self.electrumV1FromPublicKeyContainerQFrame)
        self.PublicKeyVLayout_4.setSpacing(5)
        self.PublicKeyVLayout_4.setObjectName(u"PublicKeyVLayout_4")
        self.PublicKeyVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyLabelContainerQFrame = QFrame(self.electrumV1FromPublicKeyContainerQFrame)
        self.electrumV1FromPublicKeyLabelContainerQFrame.setObjectName(u"electrumV1FromPublicKeyLabelContainerQFrame")
        self.PublicKeyLabelHLayout_4 = QHBoxLayout(self.electrumV1FromPublicKeyLabelContainerQFrame)
        self.PublicKeyLabelHLayout_4.setSpacing(15)
        self.PublicKeyLabelHLayout_4.setObjectName(u"PublicKeyLabelHLayout_4")
        self.PublicKeyLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyQLabel = QLabel(self.electrumV1FromPublicKeyLabelContainerQFrame)
        self.electrumV1FromPublicKeyQLabel.setObjectName(u"electrumV1FromPublicKeyQLabel")

        self.PublicKeyLabelHLayout_4.addWidget(self.electrumV1FromPublicKeyQLabel)

        self.electrumV1FromPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PublicKeyLabelHLayout_4.addItem(self.electrumV1FromPublicKeyLabelContainerQFrameHSpacer)


        self.PublicKeyVLayout_4.addWidget(self.electrumV1FromPublicKeyLabelContainerQFrame)

        self.electrumV1FromPublicKeyQLineEdit = QLineEdit(self.electrumV1FromPublicKeyContainerQFrame)
        self.electrumV1FromPublicKeyQLineEdit.setObjectName(u"electrumV1FromPublicKeyQLineEdit")

        self.PublicKeyVLayout_4.addWidget(self.electrumV1FromPublicKeyQLineEdit)


        self.horizontalLayout_78.addWidget(self.electrumV1FromPublicKeyContainerQFrame)

        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeContainerQFrame")
        self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.verticalLayout_83 = QVBoxLayout(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)
        self.verticalLayout_83.setSpacing(5)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame")
        self.horizontalLayout_79 = QHBoxLayout(self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.horizontalLayout_79.setSpacing(15)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyPublicKeyTypeQLabel = QLabel(self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeQLabel.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeQLabel")

        self.horizontalLayout_79.addWidget(self.electrumV1FromPublicKeyPublicKeyTypeQLabel)

        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_79.addItem(self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_83.addWidget(self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame)

        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox = QComboBox(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeQComboBox")

        self.verticalLayout_83.addWidget(self.electrumV1FromPublicKeyPublicKeyTypeQComboBox)


        self.horizontalLayout_78.addWidget(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)


        self.verticalLayout_56.addWidget(self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame)

        self.electrumV1FromPublicKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.electrumV1FromPublicKeyQStackedWidgetVSpacer)

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
        self.verticalLayout_58 = QVBoxLayout(self.electrumV2FromEntropyQStackedWidget)
        self.verticalLayout_58.setSpacing(15)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyContainerQFrame = QFrame(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromEntropyContainerQFrame.setObjectName(u"electrumV2FromEntropyContainerQFrame")
        self.verticalLayout_59 = QVBoxLayout(self.electrumV2FromEntropyContainerQFrame)
        self.verticalLayout_59.setSpacing(5)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyLabelContainerQFrame = QFrame(self.electrumV2FromEntropyContainerQFrame)
        self.electrumV2FromEntropyLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyLabelContainerQFrame")
        self.EntropyLabelHLayout_7 = QHBoxLayout(self.electrumV2FromEntropyLabelContainerQFrame)
        self.EntropyLabelHLayout_7.setSpacing(15)
        self.EntropyLabelHLayout_7.setObjectName(u"EntropyLabelHLayout_7")
        self.EntropyLabelHLayout_7.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyQLabel = QLabel(self.electrumV2FromEntropyLabelContainerQFrame)
        self.electrumV2FromEntropyQLabel.setObjectName(u"electrumV2FromEntropyQLabel")

        self.EntropyLabelHLayout_7.addWidget(self.electrumV2FromEntropyQLabel)

        self.electrumV2FromEntropyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_7.addItem(self.electrumV2FromEntropyLabelContainerQFrameHSpacer)


        self.verticalLayout_59.addWidget(self.electrumV2FromEntropyLabelContainerQFrame)

        self.electrumV2FromEntropyGenerateContainerQFrame = QFrame(self.electrumV2FromEntropyContainerQFrame)
        self.electrumV2FromEntropyGenerateContainerQFrame.setObjectName(u"electrumV2FromEntropyGenerateContainerQFrame")
        self.horizontalLayout_53 = QHBoxLayout(self.electrumV2FromEntropyGenerateContainerQFrame)
        self.horizontalLayout_53.setSpacing(15)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyGenerateQLineEdit = QLineEdit(self.electrumV2FromEntropyGenerateContainerQFrame)
        self.electrumV2FromEntropyGenerateQLineEdit.setObjectName(u"electrumV2FromEntropyGenerateQLineEdit")

        self.horizontalLayout_53.addWidget(self.electrumV2FromEntropyGenerateQLineEdit)


        self.verticalLayout_59.addWidget(self.electrumV2FromEntropyGenerateContainerQFrame)


        self.verticalLayout_58.addWidget(self.electrumV2FromEntropyContainerQFrame)

        self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame = QFrame(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame.setObjectName(u"electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame")
        self.horizontalLayout_54 = QHBoxLayout(self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame)
        self.horizontalLayout_54.setSpacing(15)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyModeContainerQFrame = QFrame(self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromEntropyModeContainerQFrame.setObjectName(u"electrumV2FromEntropyModeContainerQFrame")
        self.verticalLayout_74 = QVBoxLayout(self.electrumV2FromEntropyModeContainerQFrame)
        self.verticalLayout_74.setSpacing(5)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyModeLabelContainerQFrame = QFrame(self.electrumV2FromEntropyModeContainerQFrame)
        self.electrumV2FromEntropyModeLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyModeLabelContainerQFrame")
        self.horizontalLayout_92 = QHBoxLayout(self.electrumV2FromEntropyModeLabelContainerQFrame)
        self.horizontalLayout_92.setSpacing(15)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyModeQLabel = QLabel(self.electrumV2FromEntropyModeLabelContainerQFrame)
        self.electrumV2FromEntropyModeQLabel.setObjectName(u"electrumV2FromEntropyModeQLabel")

        self.horizontalLayout_92.addWidget(self.electrumV2FromEntropyModeQLabel)

        self.electrumV2FromEntropyModeLabelContainerQFrameHSpacer = QSpacerItem(16, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_92.addItem(self.electrumV2FromEntropyModeLabelContainerQFrameHSpacer)


        self.verticalLayout_74.addWidget(self.electrumV2FromEntropyModeLabelContainerQFrame)

        self.electrumV2FromEntropyModeQComboBox = QComboBox(self.electrumV2FromEntropyModeContainerQFrame)
        self.electrumV2FromEntropyModeQComboBox.setObjectName(u"electrumV2FromEntropyModeQComboBox")

        self.verticalLayout_74.addWidget(self.electrumV2FromEntropyModeQComboBox)


        self.horizontalLayout_54.addWidget(self.electrumV2FromEntropyModeContainerQFrame)

        self.electrumV2FromEntropyPublicKeyTypeContainerQFrame = QFrame(self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromEntropyPublicKeyTypeContainerQFrame.setObjectName(u"electrumV2FromEntropyPublicKeyTypeContainerQFrame")
        self.electrumV2FromEntropyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_13 = QVBoxLayout(self.electrumV2FromEntropyPublicKeyTypeContainerQFrame)
        self.ClientVLayout_13.setSpacing(5)
        self.ClientVLayout_13.setObjectName(u"ClientVLayout_13")
        self.ClientVLayout_13.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV2FromEntropyPublicKeyTypeContainerQFrame)
        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_17 = QHBoxLayout(self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_17.setSpacing(15)
        self.MStrengthLabelHLayout_17.setObjectName(u"MStrengthLabelHLayout_17")
        self.MStrengthLabelHLayout_17.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyPublicKeyTypeQLabel = QLabel(self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame)
        self.electrumV2FromEntropyPublicKeyTypeQLabel.setObjectName(u"electrumV2FromEntropyPublicKeyTypeQLabel")

        self.MStrengthLabelHLayout_17.addWidget(self.electrumV2FromEntropyPublicKeyTypeQLabel)

        self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_17.addItem(self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_13.addWidget(self.electrumV2FromEntropyPublicKeyTypeLabelContainerQFrame)

        self.electrumV2FromEntropyPublicKeyTypeQComboBox = QComboBox(self.electrumV2FromEntropyPublicKeyTypeContainerQFrame)
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setObjectName(u"electrumV2FromEntropyPublicKeyTypeQComboBox")

        self.ClientVLayout_13.addWidget(self.electrumV2FromEntropyPublicKeyTypeQComboBox)


        self.horizontalLayout_54.addWidget(self.electrumV2FromEntropyPublicKeyTypeContainerQFrame)

        self.electrumV2FromEntropyPassphraseContainerQFrame = QFrame(self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromEntropyPassphraseContainerQFrame.setObjectName(u"electrumV2FromEntropyPassphraseContainerQFrame")
        self.EPassphraseVLayout_9 = QVBoxLayout(self.electrumV2FromEntropyPassphraseContainerQFrame)
        self.EPassphraseVLayout_9.setSpacing(5)
        self.EPassphraseVLayout_9.setObjectName(u"EPassphraseVLayout_9")
        self.EPassphraseVLayout_9.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyPassphraseLabelContainerQFrame = QFrame(self.electrumV2FromEntropyPassphraseContainerQFrame)
        self.electrumV2FromEntropyPassphraseLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyPassphraseLabelContainerQFrame")
        self.EPassphraseLabelHLayout_9 = QHBoxLayout(self.electrumV2FromEntropyPassphraseLabelContainerQFrame)
        self.EPassphraseLabelHLayout_9.setSpacing(15)
        self.EPassphraseLabelHLayout_9.setObjectName(u"EPassphraseLabelHLayout_9")
        self.EPassphraseLabelHLayout_9.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyPassphraseQLabel = QLabel(self.electrumV2FromEntropyPassphraseLabelContainerQFrame)
        self.electrumV2FromEntropyPassphraseQLabel.setObjectName(u"electrumV2FromEntropyPassphraseQLabel")

        self.EPassphraseLabelHLayout_9.addWidget(self.electrumV2FromEntropyPassphraseQLabel)

        self.electrumV2FromEntropyPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_9.addItem(self.electrumV2FromEntropyPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout_9.addWidget(self.electrumV2FromEntropyPassphraseLabelContainerQFrame)

        self.electrumV2FromEntropyPassphraseGenerateContainerQFrame = QFrame(self.electrumV2FromEntropyPassphraseContainerQFrame)
        self.electrumV2FromEntropyPassphraseGenerateContainerQFrame.setObjectName(u"electrumV2FromEntropyPassphraseGenerateContainerQFrame")
        self.horizontalLayout_55 = QHBoxLayout(self.electrumV2FromEntropyPassphraseGenerateContainerQFrame)
        self.horizontalLayout_55.setSpacing(15)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyPassphraseGenerateQLineEdit = QLineEdit(self.electrumV2FromEntropyPassphraseGenerateContainerQFrame)
        self.electrumV2FromEntropyPassphraseGenerateQLineEdit.setObjectName(u"electrumV2FromEntropyPassphraseGenerateQLineEdit")

        self.horizontalLayout_55.addWidget(self.electrumV2FromEntropyPassphraseGenerateQLineEdit)


        self.EPassphraseVLayout_9.addWidget(self.electrumV2FromEntropyPassphraseGenerateContainerQFrame)


        self.horizontalLayout_54.addWidget(self.electrumV2FromEntropyPassphraseContainerQFrame)


        self.verticalLayout_58.addWidget(self.electrumV2FromEntropyModePublicKeyTypeAndPassphraseContainerQFrame)

        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame = QFrame(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame.setObjectName(u"electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame")
        self.horizontalLayout_56 = QHBoxLayout(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)
        self.horizontalLayout_56.setSpacing(15)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyLanguageContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)
        self.electrumV2FromEntropyLanguageContainerQFrame.setObjectName(u"electrumV2FromEntropyLanguageContainerQFrame")
        self.ELanguageVLayout_5 = QVBoxLayout(self.electrumV2FromEntropyLanguageContainerQFrame)
        self.ELanguageVLayout_5.setSpacing(5)
        self.ELanguageVLayout_5.setObjectName(u"ELanguageVLayout_5")
        self.ELanguageVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyLanguageLabelContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageContainerQFrame)
        self.electrumV2FromEntropyLanguageLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyLanguageLabelContainerQFrame")
        self.ELanguageLabelHLayout_5 = QHBoxLayout(self.electrumV2FromEntropyLanguageLabelContainerQFrame)
        self.ELanguageLabelHLayout_5.setSpacing(15)
        self.ELanguageLabelHLayout_5.setObjectName(u"ELanguageLabelHLayout_5")
        self.ELanguageLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyLanguageQLabel = QLabel(self.electrumV2FromEntropyLanguageLabelContainerQFrame)
        self.electrumV2FromEntropyLanguageQLabel.setObjectName(u"electrumV2FromEntropyLanguageQLabel")

        self.ELanguageLabelHLayout_5.addWidget(self.electrumV2FromEntropyLanguageQLabel)


        self.ELanguageVLayout_5.addWidget(self.electrumV2FromEntropyLanguageLabelContainerQFrame)

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

        self.ELanguageVLayout_5.addWidget(self.electrumV2FromEntropyLanguageQComboBox)


        self.horizontalLayout_56.addWidget(self.electrumV2FromEntropyLanguageContainerQFrame)

        self.electrumV2FromEntropyWordsContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)
        self.electrumV2FromEntropyWordsContainerQFrame.setObjectName(u"electrumV2FromEntropyWordsContainerQFrame")
        self.EStrengthVLayout_5 = QVBoxLayout(self.electrumV2FromEntropyWordsContainerQFrame)
        self.EStrengthVLayout_5.setSpacing(5)
        self.EStrengthVLayout_5.setObjectName(u"EStrengthVLayout_5")
        self.EStrengthVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyWordsLabelContainerQFrame = QFrame(self.electrumV2FromEntropyWordsContainerQFrame)
        self.electrumV2FromEntropyWordsLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyWordsLabelContainerQFrame")
        self.EStrengthLabelHLayout_5 = QHBoxLayout(self.electrumV2FromEntropyWordsLabelContainerQFrame)
        self.EStrengthLabelHLayout_5.setSpacing(15)
        self.EStrengthLabelHLayout_5.setObjectName(u"EStrengthLabelHLayout_5")
        self.EStrengthLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyWordsQLabel = QLabel(self.electrumV2FromEntropyWordsLabelContainerQFrame)
        self.electrumV2FromEntropyWordsQLabel.setObjectName(u"electrumV2FromEntropyWordsQLabel")

        self.EStrengthLabelHLayout_5.addWidget(self.electrumV2FromEntropyWordsQLabel)


        self.EStrengthVLayout_5.addWidget(self.electrumV2FromEntropyWordsLabelContainerQFrame)

        self.electrumV2FromEntropyWordsQComboBox = QComboBox(self.electrumV2FromEntropyWordsContainerQFrame)
        self.electrumV2FromEntropyWordsQComboBox.addItem("")
        self.electrumV2FromEntropyWordsQComboBox.addItem("")
        self.electrumV2FromEntropyWordsQComboBox.addItem("")
        self.electrumV2FromEntropyWordsQComboBox.addItem("")
        self.electrumV2FromEntropyWordsQComboBox.addItem("")
        self.electrumV2FromEntropyWordsQComboBox.setObjectName(u"electrumV2FromEntropyWordsQComboBox")

        self.EStrengthVLayout_5.addWidget(self.electrumV2FromEntropyWordsQComboBox)


        self.horizontalLayout_56.addWidget(self.electrumV2FromEntropyWordsContainerQFrame)

        self.electrumV2FromEntropyMnemonicTypeContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)
        self.electrumV2FromEntropyMnemonicTypeContainerQFrame.setObjectName(u"electrumV2FromEntropyMnemonicTypeContainerQFrame")
        self.verticalLayout_75 = QVBoxLayout(self.electrumV2FromEntropyMnemonicTypeContainerQFrame)
        self.verticalLayout_75.setSpacing(5)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyMnemonicTypeQLabel = QLabel(self.electrumV2FromEntropyMnemonicTypeContainerQFrame)
        self.electrumV2FromEntropyMnemonicTypeQLabel.setObjectName(u"electrumV2FromEntropyMnemonicTypeQLabel")

        self.verticalLayout_75.addWidget(self.electrumV2FromEntropyMnemonicTypeQLabel)

        self.electrumV2FromEntropyMnemonicTypeQComboBox = QComboBox(self.electrumV2FromEntropyMnemonicTypeContainerQFrame)
        self.electrumV2FromEntropyMnemonicTypeQComboBox.setObjectName(u"electrumV2FromEntropyMnemonicTypeQComboBox")

        self.verticalLayout_75.addWidget(self.electrumV2FromEntropyMnemonicTypeQComboBox)


        self.horizontalLayout_56.addWidget(self.electrumV2FromEntropyMnemonicTypeContainerQFrame)


        self.verticalLayout_58.addWidget(self.electrumV2FromEntropyLanguageMnemonicTypeAndWordsContainerQFrame)

        self.electrumV2QStackedWidget.addWidget(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromMnemonicQStackedWidget = QWidget()
        self.electrumV2FromMnemonicQStackedWidget.setObjectName(u"electrumV2FromMnemonicQStackedWidget")
        self.verticalLayout_60 = QVBoxLayout(self.electrumV2FromMnemonicQStackedWidget)
        self.verticalLayout_60.setSpacing(15)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame = QFrame(self.electrumV2FromMnemonicQStackedWidget)
        self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame.setObjectName(u"electrumV2FromMnemonicAndMnemonicTypeContainerQFrame")
        self.horizontalLayout_57 = QHBoxLayout(self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame)
        self.horizontalLayout_57.setSpacing(15)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicContainerQFrame = QFrame(self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame)
        self.electrumV2FromMnemonicContainerQFrame.setObjectName(u"electrumV2FromMnemonicContainerQFrame")
        self.MnemonicVLayout_5 = QVBoxLayout(self.electrumV2FromMnemonicContainerQFrame)
        self.MnemonicVLayout_5.setSpacing(5)
        self.MnemonicVLayout_5.setObjectName(u"MnemonicVLayout_5")
        self.MnemonicVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicContainerQFrame)
        self.electrumV2FromMnemonicLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicLabelContainerQFrame")
        self.MnemonicLabelHLayout_5 = QHBoxLayout(self.electrumV2FromMnemonicLabelContainerQFrame)
        self.MnemonicLabelHLayout_5.setSpacing(15)
        self.MnemonicLabelHLayout_5.setObjectName(u"MnemonicLabelHLayout_5")
        self.MnemonicLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicQLabel = QLabel(self.electrumV2FromMnemonicLabelContainerQFrame)
        self.electrumV2FromMnemonicQLabel.setObjectName(u"electrumV2FromMnemonicQLabel")

        self.MnemonicLabelHLayout_5.addWidget(self.electrumV2FromMnemonicQLabel)

        self.electrumV2FromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout_5.addItem(self.electrumV2FromMnemonicLabelContainerQFrameHSpacer)


        self.MnemonicVLayout_5.addWidget(self.electrumV2FromMnemonicLabelContainerQFrame)

        self.electrumV2FromMnemonicGenerateContainerQFrame = QFrame(self.electrumV2FromMnemonicContainerQFrame)
        self.electrumV2FromMnemonicGenerateContainerQFrame.setObjectName(u"electrumV2FromMnemonicGenerateContainerQFrame")
        self.horizontalLayout_93 = QHBoxLayout(self.electrumV2FromMnemonicGenerateContainerQFrame)
        self.horizontalLayout_93.setSpacing(15)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicGenerateQLineEdit = QLineEdit(self.electrumV2FromMnemonicGenerateContainerQFrame)
        self.electrumV2FromMnemonicGenerateQLineEdit.setObjectName(u"electrumV2FromMnemonicGenerateQLineEdit")

        self.horizontalLayout_93.addWidget(self.electrumV2FromMnemonicGenerateQLineEdit)


        self.MnemonicVLayout_5.addWidget(self.electrumV2FromMnemonicGenerateContainerQFrame)


        self.horizontalLayout_57.addWidget(self.electrumV2FromMnemonicContainerQFrame)

        self.electrumV2FromMnemonicMnemonicTypeContainerQFrame = QFrame(self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame)
        self.electrumV2FromMnemonicMnemonicTypeContainerQFrame.setObjectName(u"electrumV2FromMnemonicMnemonicTypeContainerQFrame")
        self.verticalLayout_71 = QVBoxLayout(self.electrumV2FromMnemonicMnemonicTypeContainerQFrame)
        self.verticalLayout_71.setSpacing(5)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicMnemonicTypeContainerQFrame)
        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame")
        self.horizontalLayout_95 = QHBoxLayout(self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame)
        self.horizontalLayout_95.setSpacing(15)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicMnemonicTypeQLabel = QLabel(self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame)
        self.electrumV2FromMnemonicMnemonicTypeQLabel.setObjectName(u"electrumV2FromMnemonicMnemonicTypeQLabel")

        self.horizontalLayout_95.addWidget(self.electrumV2FromMnemonicMnemonicTypeQLabel)

        self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHSpacer = QSpacerItem(49, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_95.addItem(self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_71.addWidget(self.electrumV2FromMnemonicMnemonicTypeLabelContainerQFrame)

        self.electrumV2FromMnemonicMnemonicTypeQComboBox = QComboBox(self.electrumV2FromMnemonicMnemonicTypeContainerQFrame)
        self.electrumV2FromMnemonicMnemonicTypeQComboBox.setObjectName(u"electrumV2FromMnemonicMnemonicTypeQComboBox")

        self.verticalLayout_71.addWidget(self.electrumV2FromMnemonicMnemonicTypeQComboBox)


        self.horizontalLayout_57.addWidget(self.electrumV2FromMnemonicMnemonicTypeContainerQFrame)


        self.verticalLayout_60.addWidget(self.electrumV2FromMnemonicAndMnemonicTypeContainerQFrame)

        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame = QFrame(self.electrumV2FromMnemonicQStackedWidget)
        self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame.setObjectName(u"electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame")
        self.horizontalLayout_58 = QHBoxLayout(self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame)
        self.horizontalLayout_58.setSpacing(15)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicModeContainerQFrame = QFrame(self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromMnemonicModeContainerQFrame.setObjectName(u"electrumV2FromMnemonicModeContainerQFrame")
        self.verticalLayout_72 = QVBoxLayout(self.electrumV2FromMnemonicModeContainerQFrame)
        self.verticalLayout_72.setSpacing(5)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicModeLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicModeContainerQFrame)
        self.electrumV2FromMnemonicModeLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicModeLabelContainerQFrame")
        self.horizontalLayout_94 = QHBoxLayout(self.electrumV2FromMnemonicModeLabelContainerQFrame)
        self.horizontalLayout_94.setSpacing(15)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicModeQLabel = QLabel(self.electrumV2FromMnemonicModeLabelContainerQFrame)
        self.electrumV2FromMnemonicModeQLabel.setObjectName(u"electrumV2FromMnemonicModeQLabel")

        self.horizontalLayout_94.addWidget(self.electrumV2FromMnemonicModeQLabel)

        self.electrumV2FromMnemonicModeLabelContainerQFrameHSpacer = QSpacerItem(49, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_94.addItem(self.electrumV2FromMnemonicModeLabelContainerQFrameHSpacer)


        self.verticalLayout_72.addWidget(self.electrumV2FromMnemonicModeLabelContainerQFrame)

        self.electrumV2FromMnemonicModeQComboBox = QComboBox(self.electrumV2FromMnemonicModeContainerQFrame)
        self.electrumV2FromMnemonicModeQComboBox.setObjectName(u"electrumV2FromMnemonicModeQComboBox")

        self.verticalLayout_72.addWidget(self.electrumV2FromMnemonicModeQComboBox)


        self.horizontalLayout_58.addWidget(self.electrumV2FromMnemonicModeContainerQFrame)

        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame = QFrame(self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame.setObjectName(u"electrumV2FromMnemonicPublicKeyTypeContainerQFrame")
        self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_14 = QVBoxLayout(self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame)
        self.ClientVLayout_14.setSpacing(5)
        self.ClientVLayout_14.setObjectName(u"ClientVLayout_14")
        self.ClientVLayout_14.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame)
        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_18 = QHBoxLayout(self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_18.setSpacing(15)
        self.MStrengthLabelHLayout_18.setObjectName(u"MStrengthLabelHLayout_18")
        self.MStrengthLabelHLayout_18.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicPublicKeyTypeQLabel = QLabel(self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.electrumV2FromMnemonicPublicKeyTypeQLabel.setObjectName(u"electrumV2FromMnemonicPublicKeyTypeQLabel")

        self.MStrengthLabelHLayout_18.addWidget(self.electrumV2FromMnemonicPublicKeyTypeQLabel)

        self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_18.addItem(self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_14.addWidget(self.electrumV2FromMnemonicPublicKeyTypeLabelContainerQFrame)

        self.electrumV2FromMnemonicPublicKeyTypeQComboBox = QComboBox(self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame)
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setObjectName(u"electrumV2FromMnemonicPublicKeyTypeQComboBox")

        self.ClientVLayout_14.addWidget(self.electrumV2FromMnemonicPublicKeyTypeQComboBox)


        self.horizontalLayout_58.addWidget(self.electrumV2FromMnemonicPublicKeyTypeContainerQFrame)

        self.electrumV2FromMnemonicPassphraseContainerQFrame = QFrame(self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame)
        self.electrumV2FromMnemonicPassphraseContainerQFrame.setObjectName(u"electrumV2FromMnemonicPassphraseContainerQFrame")
        self.EPassphraseVLayout_10 = QVBoxLayout(self.electrumV2FromMnemonicPassphraseContainerQFrame)
        self.EPassphraseVLayout_10.setSpacing(5)
        self.EPassphraseVLayout_10.setObjectName(u"EPassphraseVLayout_10")
        self.EPassphraseVLayout_10.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicPassphraseLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicPassphraseContainerQFrame)
        self.electrumV2FromMnemonicPassphraseLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicPassphraseLabelContainerQFrame")
        self.MPassphraseLabelHLayout_5 = QHBoxLayout(self.electrumV2FromMnemonicPassphraseLabelContainerQFrame)
        self.MPassphraseLabelHLayout_5.setSpacing(15)
        self.MPassphraseLabelHLayout_5.setObjectName(u"MPassphraseLabelHLayout_5")
        self.MPassphraseLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicPassphraseQLabel = QLabel(self.electrumV2FromMnemonicPassphraseLabelContainerQFrame)
        self.electrumV2FromMnemonicPassphraseQLabel.setObjectName(u"electrumV2FromMnemonicPassphraseQLabel")

        self.MPassphraseLabelHLayout_5.addWidget(self.electrumV2FromMnemonicPassphraseQLabel)

        self.electrumV2FromMnemonicPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout_5.addItem(self.electrumV2FromMnemonicPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout_10.addWidget(self.electrumV2FromMnemonicPassphraseLabelContainerQFrame)

        self.electrumV2FromMnemonicPassphraseGenerateContainerQFrame = QFrame(self.electrumV2FromMnemonicPassphraseContainerQFrame)
        self.electrumV2FromMnemonicPassphraseGenerateContainerQFrame.setObjectName(u"electrumV2FromMnemonicPassphraseGenerateContainerQFrame")
        self.horizontalLayout_59 = QHBoxLayout(self.electrumV2FromMnemonicPassphraseGenerateContainerQFrame)
        self.horizontalLayout_59.setSpacing(15)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicPassphraseGenerateQLineEdit = QLineEdit(self.electrumV2FromMnemonicPassphraseGenerateContainerQFrame)
        self.electrumV2FromMnemonicPassphraseGenerateQLineEdit.setObjectName(u"electrumV2FromMnemonicPassphraseGenerateQLineEdit")

        self.horizontalLayout_59.addWidget(self.electrumV2FromMnemonicPassphraseGenerateQLineEdit)


        self.EPassphraseVLayout_10.addWidget(self.electrumV2FromMnemonicPassphraseGenerateContainerQFrame)


        self.horizontalLayout_58.addWidget(self.electrumV2FromMnemonicPassphraseContainerQFrame)


        self.verticalLayout_60.addWidget(self.electrumV2FromMnemonicModePublicKeyTypeAndPassphraseContainerQFrame)

        self.electrumV2FromMnemonicQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_60.addItem(self.electrumV2FromMnemonicQStackedWidgetVSpacer)

        self.electrumV2QStackedWidget.addWidget(self.electrumV2FromMnemonicQStackedWidget)
        self.electrumV2FromSeedQStackedWidget = QWidget()
        self.electrumV2FromSeedQStackedWidget.setObjectName(u"electrumV2FromSeedQStackedWidget")
        self.verticalLayout_61 = QVBoxLayout(self.electrumV2FromSeedQStackedWidget)
        self.verticalLayout_61.setSpacing(15)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedContainerQFrame = QFrame(self.electrumV2FromSeedQStackedWidget)
        self.electrumV2FromSeedContainerQFrame.setObjectName(u"electrumV2FromSeedContainerQFrame")
        self.electrumV2FromSeedContainerQFrame.setMinimumSize(QSize(400, 0))
        self.SeedVLayout_5 = QVBoxLayout(self.electrumV2FromSeedContainerQFrame)
        self.SeedVLayout_5.setSpacing(5)
        self.SeedVLayout_5.setObjectName(u"SeedVLayout_5")
        self.SeedVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame = QFrame(self.electrumV2FromSeedContainerQFrame)
        self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame")
        self.horizontalLayout_61 = QHBoxLayout(self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame)
        self.horizontalLayout_61.setSpacing(15)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedsContainerQFrame = QFrame(self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedsContainerQFrame.setObjectName(u"electrumV2FromSeedsContainerQFrame")
        self.verticalLayout_62 = QVBoxLayout(self.electrumV2FromSeedsContainerQFrame)
        self.verticalLayout_62.setSpacing(5)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedsLabelContainerQFrame = QFrame(self.electrumV2FromSeedsContainerQFrame)
        self.electrumV2FromSeedsLabelContainerQFrame.setObjectName(u"electrumV2FromSeedsLabelContainerQFrame")
        self.SeedLabelHLayout_5 = QHBoxLayout(self.electrumV2FromSeedsLabelContainerQFrame)
        self.SeedLabelHLayout_5.setSpacing(15)
        self.SeedLabelHLayout_5.setObjectName(u"SeedLabelHLayout_5")
        self.SeedLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedsQLabel = QLabel(self.electrumV2FromSeedsLabelContainerQFrame)
        self.electrumV2FromSeedsQLabel.setObjectName(u"electrumV2FromSeedsQLabel")

        self.SeedLabelHLayout_5.addWidget(self.electrumV2FromSeedsQLabel)

        self.electrumV2FromSeedsLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout_5.addItem(self.electrumV2FromSeedsLabelContainerQFrameHSpacer)


        self.verticalLayout_62.addWidget(self.electrumV2FromSeedsLabelContainerQFrame)

        self.electrumV2FromSeedsQLineEdit = QLineEdit(self.electrumV2FromSeedsContainerQFrame)
        self.electrumV2FromSeedsQLineEdit.setObjectName(u"electrumV2FromSeedsQLineEdit")

        self.verticalLayout_62.addWidget(self.electrumV2FromSeedsQLineEdit)


        self.horizontalLayout_61.addWidget(self.electrumV2FromSeedsContainerQFrame)

        self.electrumV2FromSeedModeContainerQFrame = QFrame(self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedModeContainerQFrame.setObjectName(u"electrumV2FromSeedModeContainerQFrame")
        self.verticalLayout_73 = QVBoxLayout(self.electrumV2FromSeedModeContainerQFrame)
        self.verticalLayout_73.setSpacing(5)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedModeQLabel = QLabel(self.electrumV2FromSeedModeContainerQFrame)
        self.electrumV2FromSeedModeQLabel.setObjectName(u"electrumV2FromSeedModeQLabel")

        self.verticalLayout_73.addWidget(self.electrumV2FromSeedModeQLabel)

        self.electrumV2FromSeedModeQComboBox = QComboBox(self.electrumV2FromSeedModeContainerQFrame)
        self.electrumV2FromSeedModeQComboBox.setObjectName(u"electrumV2FromSeedModeQComboBox")

        self.verticalLayout_73.addWidget(self.electrumV2FromSeedModeQComboBox)


        self.horizontalLayout_61.addWidget(self.electrumV2FromSeedModeContainerQFrame)

        self.electrumV2FromSeedPublicKeyTypeContainerQFrame = QFrame(self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedPublicKeyTypeContainerQFrame.setObjectName(u"electrumV2FromSeedPublicKeyTypeContainerQFrame")
        self.electrumV2FromSeedPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_15 = QVBoxLayout(self.electrumV2FromSeedPublicKeyTypeContainerQFrame)
        self.ClientVLayout_15.setSpacing(5)
        self.ClientVLayout_15.setObjectName(u"ClientVLayout_15")
        self.ClientVLayout_15.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV2FromSeedPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV2FromSeedPublicKeyTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_20 = QHBoxLayout(self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_20.setSpacing(15)
        self.MStrengthLabelHLayout_20.setObjectName(u"MStrengthLabelHLayout_20")
        self.MStrengthLabelHLayout_20.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromSeedPublicKeyTypeQLabel = QLabel(self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrame)
        self.electrumV2FromSeedPublicKeyTypeQLabel.setObjectName(u"electrumV2FromSeedPublicKeyTypeQLabel")

        self.MStrengthLabelHLayout_20.addWidget(self.electrumV2FromSeedPublicKeyTypeQLabel)

        self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_20.addItem(self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_15.addWidget(self.electrumV2FromSeedPublicKeyTypeLabelContainerQFrame)

        self.electrumV2FromSeedPublicKeyTypeQComboBox = QComboBox(self.electrumV2FromSeedPublicKeyTypeContainerQFrame)
        self.electrumV2FromSeedPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromSeedPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromSeedPublicKeyTypeQComboBox.setObjectName(u"electrumV2FromSeedPublicKeyTypeQComboBox")

        self.ClientVLayout_15.addWidget(self.electrumV2FromSeedPublicKeyTypeQComboBox)


        self.horizontalLayout_61.addWidget(self.electrumV2FromSeedPublicKeyTypeContainerQFrame)


        self.SeedVLayout_5.addWidget(self.electrumV2FromSeedModeAndPublicKeyTypeContainerQFrame)

        self.electrumV2FromSeedContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout_5.addItem(self.electrumV2FromSeedContainerQFrameVSpacer)


        self.verticalLayout_61.addWidget(self.electrumV2FromSeedContainerQFrame)

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
        self.verticalLayout_4 = QVBoxLayout(self.moneroFromEntropyQStackedWidget)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyContainerQFrame = QFrame(self.moneroFromEntropyQStackedWidget)
        self.moneroFromEntropyContainerQFrame.setObjectName(u"moneroFromEntropyContainerQFrame")
        self.verticalLayout_8 = QVBoxLayout(self.moneroFromEntropyContainerQFrame)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyLabelContainerQFrame = QFrame(self.moneroFromEntropyContainerQFrame)
        self.moneroFromEntropyLabelContainerQFrame.setObjectName(u"moneroFromEntropyLabelContainerQFrame")
        self.EntropyLabelHLayout_2 = QHBoxLayout(self.moneroFromEntropyLabelContainerQFrame)
        self.EntropyLabelHLayout_2.setSpacing(15)
        self.EntropyLabelHLayout_2.setObjectName(u"EntropyLabelHLayout_2")
        self.EntropyLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyQLabel = QLabel(self.moneroFromEntropyLabelContainerQFrame)
        self.moneroFromEntropyQLabel.setObjectName(u"moneroFromEntropyQLabel")

        self.EntropyLabelHLayout_2.addWidget(self.moneroFromEntropyQLabel)

        self.moneroFromEntropyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_2.addItem(self.moneroFromEntropyLabelContainerQFrameHSpacer)


        self.verticalLayout_8.addWidget(self.moneroFromEntropyLabelContainerQFrame)

        self.moneroFromEntropyLineEditContainerQFrame = QFrame(self.moneroFromEntropyContainerQFrame)
        self.moneroFromEntropyLineEditContainerQFrame.setObjectName(u"moneroFromEntropyLineEditContainerQFrame")
        self.horizontalLayout_13 = QHBoxLayout(self.moneroFromEntropyLineEditContainerQFrame)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyQLineEdit = QLineEdit(self.moneroFromEntropyLineEditContainerQFrame)
        self.moneroFromEntropyQLineEdit.setObjectName(u"moneroFromEntropyQLineEdit")

        self.horizontalLayout_13.addWidget(self.moneroFromEntropyQLineEdit)


        self.verticalLayout_8.addWidget(self.moneroFromEntropyLineEditContainerQFrame)


        self.verticalLayout_4.addWidget(self.moneroFromEntropyContainerQFrame)

        self.moneroFromEntropyPassphrasePaymentIDContainerQFrame = QFrame(self.moneroFromEntropyQStackedWidget)
        self.moneroFromEntropyPassphrasePaymentIDContainerQFrame.setObjectName(u"moneroFromEntropyPassphrasePaymentIDContainerQFrame")
        self.horizontalLayout_9 = QHBoxLayout(self.moneroFromEntropyPassphrasePaymentIDContainerQFrame)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyPassphraseContainerQFrame = QFrame(self.moneroFromEntropyPassphrasePaymentIDContainerQFrame)
        self.moneroFromEntropyPassphraseContainerQFrame.setObjectName(u"moneroFromEntropyPassphraseContainerQFrame")
        self.EPassphraseVLayout = QVBoxLayout(self.moneroFromEntropyPassphraseContainerQFrame)
        self.EPassphraseVLayout.setSpacing(5)
        self.EPassphraseVLayout.setObjectName(u"EPassphraseVLayout")
        self.EPassphraseVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyPassphraseLabelContainerQFrame = QFrame(self.moneroFromEntropyPassphraseContainerQFrame)
        self.moneroFromEntropyPassphraseLabelContainerQFrame.setObjectName(u"moneroFromEntropyPassphraseLabelContainerQFrame")
        self.EPassphraseLabelHLayout = QHBoxLayout(self.moneroFromEntropyPassphraseLabelContainerQFrame)
        self.EPassphraseLabelHLayout.setSpacing(15)
        self.EPassphraseLabelHLayout.setObjectName(u"EPassphraseLabelHLayout")
        self.EPassphraseLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyPassphraseQLabel = QLabel(self.moneroFromEntropyPassphraseLabelContainerQFrame)
        self.moneroFromEntropyPassphraseQLabel.setObjectName(u"moneroFromEntropyPassphraseQLabel")

        self.EPassphraseLabelHLayout.addWidget(self.moneroFromEntropyPassphraseQLabel)

        self.moneroFromEntropyPassphraseLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout.addItem(self.moneroFromEntropyPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout.addWidget(self.moneroFromEntropyPassphraseLabelContainerQFrame)

        self.moneroFromEntropyPassphraseLineEditContainerQFrame = QFrame(self.moneroFromEntropyPassphraseContainerQFrame)
        self.moneroFromEntropyPassphraseLineEditContainerQFrame.setObjectName(u"moneroFromEntropyPassphraseLineEditContainerQFrame")
        self.horizontalLayout_15 = QHBoxLayout(self.moneroFromEntropyPassphraseLineEditContainerQFrame)
        self.horizontalLayout_15.setSpacing(15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyPassphraseQLineEdit = QLineEdit(self.moneroFromEntropyPassphraseLineEditContainerQFrame)
        self.moneroFromEntropyPassphraseQLineEdit.setObjectName(u"moneroFromEntropyPassphraseQLineEdit")

        self.horizontalLayout_15.addWidget(self.moneroFromEntropyPassphraseQLineEdit)


        self.EPassphraseVLayout.addWidget(self.moneroFromEntropyPassphraseLineEditContainerQFrame)


        self.horizontalLayout_9.addWidget(self.moneroFromEntropyPassphraseContainerQFrame)

        self.moneroFromEntropyPaymentIDContainerQFrame = QFrame(self.moneroFromEntropyPassphrasePaymentIDContainerQFrame)
        self.moneroFromEntropyPaymentIDContainerQFrame.setObjectName(u"moneroFromEntropyPaymentIDContainerQFrame")
        self.verticalLayout_84 = QVBoxLayout(self.moneroFromEntropyPaymentIDContainerQFrame)
        self.verticalLayout_84.setSpacing(5)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyPaymentIDLabelContainerQFrame = QFrame(self.moneroFromEntropyPaymentIDContainerQFrame)
        self.moneroFromEntropyPaymentIDLabelContainerQFrame.setObjectName(u"moneroFromEntropyPaymentIDLabelContainerQFrame")
        self.horizontalLayout_81 = QHBoxLayout(self.moneroFromEntropyPaymentIDLabelContainerQFrame)
        self.horizontalLayout_81.setSpacing(15)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyPaymentIDQLabel = QLabel(self.moneroFromEntropyPaymentIDLabelContainerQFrame)
        self.moneroFromEntropyPaymentIDQLabel.setObjectName(u"moneroFromEntropyPaymentIDQLabel")

        self.horizontalLayout_81.addWidget(self.moneroFromEntropyPaymentIDQLabel)

        self.moneroFromEntropyPaymentIDLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.moneroFromEntropyPaymentIDLabelContainerQFrameHSpacer)


        self.verticalLayout_84.addWidget(self.moneroFromEntropyPaymentIDLabelContainerQFrame)

        self.moneroFromEntropyPaymentIDQLineEdit = QLineEdit(self.moneroFromEntropyPaymentIDContainerQFrame)
        self.moneroFromEntropyPaymentIDQLineEdit.setObjectName(u"moneroFromEntropyPaymentIDQLineEdit")

        self.verticalLayout_84.addWidget(self.moneroFromEntropyPaymentIDQLineEdit)


        self.horizontalLayout_9.addWidget(self.moneroFromEntropyPaymentIDContainerQFrame)


        self.verticalLayout_4.addWidget(self.moneroFromEntropyPassphrasePaymentIDContainerQFrame)

        self.moneroFromEntropyLanguageWordsContainerQFrame = QFrame(self.moneroFromEntropyQStackedWidget)
        self.moneroFromEntropyLanguageWordsContainerQFrame.setObjectName(u"moneroFromEntropyLanguageWordsContainerQFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.moneroFromEntropyLanguageWordsContainerQFrame)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyLanguageContainerQFrame = QFrame(self.moneroFromEntropyLanguageWordsContainerQFrame)
        self.moneroFromEntropyLanguageContainerQFrame.setObjectName(u"moneroFromEntropyLanguageContainerQFrame")
        self.ELanguageVLayout = QVBoxLayout(self.moneroFromEntropyLanguageContainerQFrame)
        self.ELanguageVLayout.setSpacing(5)
        self.ELanguageVLayout.setObjectName(u"ELanguageVLayout")
        self.ELanguageVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyLanguageLabelContainerQFrame = QFrame(self.moneroFromEntropyLanguageContainerQFrame)
        self.moneroFromEntropyLanguageLabelContainerQFrame.setObjectName(u"moneroFromEntropyLanguageLabelContainerQFrame")
        self.ELanguageLabelHLayout = QHBoxLayout(self.moneroFromEntropyLanguageLabelContainerQFrame)
        self.ELanguageLabelHLayout.setSpacing(15)
        self.ELanguageLabelHLayout.setObjectName(u"ELanguageLabelHLayout")
        self.ELanguageLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyLanguageQLabel = QLabel(self.moneroFromEntropyLanguageLabelContainerQFrame)
        self.moneroFromEntropyLanguageQLabel.setObjectName(u"moneroFromEntropyLanguageQLabel")

        self.ELanguageLabelHLayout.addWidget(self.moneroFromEntropyLanguageQLabel)

        self.moneroFromEntropyLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout.addItem(self.moneroFromEntropyLanguageLabelContainerQFrameHSpacer)


        self.ELanguageVLayout.addWidget(self.moneroFromEntropyLanguageLabelContainerQFrame)

        self.ELanguageQComboBox = QComboBox(self.moneroFromEntropyLanguageContainerQFrame)
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


        self.horizontalLayout_7.addWidget(self.moneroFromEntropyLanguageContainerQFrame)

        self.moneroFromEntropyWordsContainerQFrame = QFrame(self.moneroFromEntropyLanguageWordsContainerQFrame)
        self.moneroFromEntropyWordsContainerQFrame.setObjectName(u"moneroFromEntropyWordsContainerQFrame")
        self.EStrengthVLayout = QVBoxLayout(self.moneroFromEntropyWordsContainerQFrame)
        self.EStrengthVLayout.setSpacing(5)
        self.EStrengthVLayout.setObjectName(u"EStrengthVLayout")
        self.EStrengthVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyWordsLabelContainerQFrame = QFrame(self.moneroFromEntropyWordsContainerQFrame)
        self.moneroFromEntropyWordsLabelContainerQFrame.setObjectName(u"moneroFromEntropyWordsLabelContainerQFrame")
        self.EStrengthLabelHLayout = QHBoxLayout(self.moneroFromEntropyWordsLabelContainerQFrame)
        self.EStrengthLabelHLayout.setSpacing(15)
        self.EStrengthLabelHLayout.setObjectName(u"EStrengthLabelHLayout")
        self.EStrengthLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromEntropyWordsQLabel = QLabel(self.moneroFromEntropyWordsLabelContainerQFrame)
        self.moneroFromEntropyWordsQLabel.setObjectName(u"moneroFromEntropyWordsQLabel")

        self.EStrengthLabelHLayout.addWidget(self.moneroFromEntropyWordsQLabel)

        self.moneroFromEntropyWordsLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout.addItem(self.moneroFromEntropyWordsLabelContainerQFrameHSpacer)


        self.EStrengthVLayout.addWidget(self.moneroFromEntropyWordsLabelContainerQFrame)

        self.moneroFromEntropyWordsQComboBox = QComboBox(self.moneroFromEntropyWordsContainerQFrame)
        self.moneroFromEntropyWordsQComboBox.addItem("")
        self.moneroFromEntropyWordsQComboBox.addItem("")
        self.moneroFromEntropyWordsQComboBox.addItem("")
        self.moneroFromEntropyWordsQComboBox.addItem("")
        self.moneroFromEntropyWordsQComboBox.addItem("")
        self.moneroFromEntropyWordsQComboBox.setObjectName(u"moneroFromEntropyWordsQComboBox")

        self.EStrengthVLayout.addWidget(self.moneroFromEntropyWordsQComboBox)


        self.horizontalLayout_7.addWidget(self.moneroFromEntropyWordsContainerQFrame)


        self.verticalLayout_4.addWidget(self.moneroFromEntropyLanguageWordsContainerQFrame)

        self.moneroQStackedWidget.addWidget(self.moneroFromEntropyQStackedWidget)
        self.moneroFromMnemonicQStackedWidget = QWidget()
        self.moneroFromMnemonicQStackedWidget.setObjectName(u"moneroFromMnemonicQStackedWidget")
        self.verticalLayout_7 = QVBoxLayout(self.moneroFromMnemonicQStackedWidget)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicContainerQFrame = QFrame(self.moneroFromMnemonicQStackedWidget)
        self.moneroFromMnemonicContainerQFrame.setObjectName(u"moneroFromMnemonicContainerQFrame")
        self.MnemonicVLayout = QVBoxLayout(self.moneroFromMnemonicContainerQFrame)
        self.MnemonicVLayout.setSpacing(5)
        self.MnemonicVLayout.setObjectName(u"MnemonicVLayout")
        self.MnemonicVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicLabelContainerQFrame = QFrame(self.moneroFromMnemonicContainerQFrame)
        self.moneroFromMnemonicLabelContainerQFrame.setObjectName(u"moneroFromMnemonicLabelContainerQFrame")
        self.MnemonicLabelHLayout = QHBoxLayout(self.moneroFromMnemonicLabelContainerQFrame)
        self.MnemonicLabelHLayout.setSpacing(15)
        self.MnemonicLabelHLayout.setObjectName(u"MnemonicLabelHLayout")
        self.MnemonicLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicQLabel = QLabel(self.moneroFromMnemonicLabelContainerQFrame)
        self.moneroFromMnemonicQLabel.setObjectName(u"moneroFromMnemonicQLabel")

        self.MnemonicLabelHLayout.addWidget(self.moneroFromMnemonicQLabel)

        self.moneroFromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout.addItem(self.moneroFromMnemonicLabelContainerQFrameHSpacer)


        self.MnemonicVLayout.addWidget(self.moneroFromMnemonicLabelContainerQFrame)

        self.moneroFromMnemonicLineEditContainerQFrame = QFrame(self.moneroFromMnemonicContainerQFrame)
        self.moneroFromMnemonicLineEditContainerQFrame.setObjectName(u"moneroFromMnemonicLineEditContainerQFrame")
        self.horizontalLayout_10 = QHBoxLayout(self.moneroFromMnemonicLineEditContainerQFrame)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicQLineEdit = QLineEdit(self.moneroFromMnemonicLineEditContainerQFrame)
        self.moneroFromMnemonicQLineEdit.setObjectName(u"moneroFromMnemonicQLineEdit")

        self.horizontalLayout_10.addWidget(self.moneroFromMnemonicQLineEdit)


        self.MnemonicVLayout.addWidget(self.moneroFromMnemonicLineEditContainerQFrame)


        self.verticalLayout_7.addWidget(self.moneroFromMnemonicContainerQFrame)

        self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame = QFrame(self.moneroFromMnemonicQStackedWidget)
        self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame.setObjectName(u"moneroFromMnemonicPaymentIDPassphraseContainerQFrame")
        self.horizontalLayout_12 = QHBoxLayout(self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicPaymentIDContainerQFrame = QFrame(self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame)
        self.moneroFromMnemonicPaymentIDContainerQFrame.setObjectName(u"moneroFromMnemonicPaymentIDContainerQFrame")
        self.moneroFromMnemonicPaymentIDContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_2 = QVBoxLayout(self.moneroFromMnemonicPaymentIDContainerQFrame)
        self.ClientVLayout_2.setSpacing(5)
        self.ClientVLayout_2.setObjectName(u"ClientVLayout_2")
        self.ClientVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicPaymentIDLabelContainerQFrame = QFrame(self.moneroFromMnemonicPaymentIDContainerQFrame)
        self.moneroFromMnemonicPaymentIDLabelContainerQFrame.setObjectName(u"moneroFromMnemonicPaymentIDLabelContainerQFrame")
        self.MStrengthLabelHLayout_4 = QHBoxLayout(self.moneroFromMnemonicPaymentIDLabelContainerQFrame)
        self.MStrengthLabelHLayout_4.setSpacing(15)
        self.MStrengthLabelHLayout_4.setObjectName(u"MStrengthLabelHLayout_4")
        self.MStrengthLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicPaymentIDQLabel = QLabel(self.moneroFromMnemonicPaymentIDLabelContainerQFrame)
        self.moneroFromMnemonicPaymentIDQLabel.setObjectName(u"moneroFromMnemonicPaymentIDQLabel")

        self.MStrengthLabelHLayout_4.addWidget(self.moneroFromMnemonicPaymentIDQLabel)

        self.moneroFromMnemonicPaymentIDLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_4.addItem(self.moneroFromMnemonicPaymentIDLabelContainerQFrameHSpacer)


        self.ClientVLayout_2.addWidget(self.moneroFromMnemonicPaymentIDLabelContainerQFrame)

        self.moneroFromMnemonicPaymentIDQLineEdit = QLineEdit(self.moneroFromMnemonicPaymentIDContainerQFrame)
        self.moneroFromMnemonicPaymentIDQLineEdit.setObjectName(u"moneroFromMnemonicPaymentIDQLineEdit")

        self.ClientVLayout_2.addWidget(self.moneroFromMnemonicPaymentIDQLineEdit)


        self.horizontalLayout_12.addWidget(self.moneroFromMnemonicPaymentIDContainerQFrame)

        self.moneroFromMnemonicPassphraseContainerQFrame = QFrame(self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame)
        self.moneroFromMnemonicPassphraseContainerQFrame.setObjectName(u"moneroFromMnemonicPassphraseContainerQFrame")
        self.EPassphraseVLayout_2 = QVBoxLayout(self.moneroFromMnemonicPassphraseContainerQFrame)
        self.EPassphraseVLayout_2.setSpacing(5)
        self.EPassphraseVLayout_2.setObjectName(u"EPassphraseVLayout_2")
        self.EPassphraseVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicPassphraseLabelContainerQFrame = QFrame(self.moneroFromMnemonicPassphraseContainerQFrame)
        self.moneroFromMnemonicPassphraseLabelContainerQFrame.setObjectName(u"moneroFromMnemonicPassphraseLabelContainerQFrame")
        self.MPassphraseLabelHLayout = QHBoxLayout(self.moneroFromMnemonicPassphraseLabelContainerQFrame)
        self.MPassphraseLabelHLayout.setSpacing(15)
        self.MPassphraseLabelHLayout.setObjectName(u"MPassphraseLabelHLayout")
        self.MPassphraseLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicPassphraseQLabel = QLabel(self.moneroFromMnemonicPassphraseLabelContainerQFrame)
        self.moneroFromMnemonicPassphraseQLabel.setObjectName(u"moneroFromMnemonicPassphraseQLabel")

        self.MPassphraseLabelHLayout.addWidget(self.moneroFromMnemonicPassphraseQLabel)

        self.moneroFromMnemonicPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout.addItem(self.moneroFromMnemonicPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout_2.addWidget(self.moneroFromMnemonicPassphraseLabelContainerQFrame)

        self.moneroFromMnemonicPassphraseLineEditContainerQFrame = QFrame(self.moneroFromMnemonicPassphraseContainerQFrame)
        self.moneroFromMnemonicPassphraseLineEditContainerQFrame.setObjectName(u"moneroFromMnemonicPassphraseLineEditContainerQFrame")
        self.horizontalLayout_16 = QHBoxLayout(self.moneroFromMnemonicPassphraseLineEditContainerQFrame)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.moneroFromMnemonicPassphraseQLineEdit = QLineEdit(self.moneroFromMnemonicPassphraseLineEditContainerQFrame)
        self.moneroFromMnemonicPassphraseQLineEdit.setObjectName(u"moneroFromMnemonicPassphraseQLineEdit")

        self.horizontalLayout_16.addWidget(self.moneroFromMnemonicPassphraseQLineEdit)


        self.EPassphraseVLayout_2.addWidget(self.moneroFromMnemonicPassphraseLineEditContainerQFrame)


        self.horizontalLayout_12.addWidget(self.moneroFromMnemonicPassphraseContainerQFrame)


        self.verticalLayout_7.addWidget(self.moneroFromMnemonicPaymentIDPassphraseContainerQFrame)

        self.moneroFromMnemonicQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.moneroFromMnemonicQStackedWidgetVSpacer)

        self.moneroQStackedWidget.addWidget(self.moneroFromMnemonicQStackedWidget)
        self.moneroFromSeedQStackedWidget = QWidget()
        self.moneroFromSeedQStackedWidget.setObjectName(u"moneroFromSeedQStackedWidget")
        self.verticalLayout_9 = QVBoxLayout(self.moneroFromSeedQStackedWidget)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedSpacerContainerQFrame = QFrame(self.moneroFromSeedQStackedWidget)
        self.moneroFromSeedSpacerContainerQFrame.setObjectName(u"moneroFromSeedSpacerContainerQFrame")
        self.moneroFromSeedSpacerContainerQFrame.setMinimumSize(QSize(400, 0))
        self.SeedVLayout = QVBoxLayout(self.moneroFromSeedSpacerContainerQFrame)
        self.SeedVLayout.setSpacing(5)
        self.SeedVLayout.setObjectName(u"SeedVLayout")
        self.SeedVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedAndPaymentIDContainerQFrame = QFrame(self.moneroFromSeedSpacerContainerQFrame)
        self.moneroFromSeedAndPaymentIDContainerQFrame.setObjectName(u"moneroFromSeedAndPaymentIDContainerQFrame")
        self.horizontalLayout_17 = QHBoxLayout(self.moneroFromSeedAndPaymentIDContainerQFrame)
        self.horizontalLayout_17.setSpacing(15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedContainerQFrame = QFrame(self.moneroFromSeedAndPaymentIDContainerQFrame)
        self.moneroFromSeedContainerQFrame.setObjectName(u"moneroFromSeedContainerQFrame")
        self.verticalLayout_16 = QVBoxLayout(self.moneroFromSeedContainerQFrame)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedLabelContainerQFrame = QFrame(self.moneroFromSeedContainerQFrame)
        self.moneroFromSeedLabelContainerQFrame.setObjectName(u"moneroFromSeedLabelContainerQFrame")
        self.SeedLabelHLayout = QHBoxLayout(self.moneroFromSeedLabelContainerQFrame)
        self.SeedLabelHLayout.setSpacing(15)
        self.SeedLabelHLayout.setObjectName(u"SeedLabelHLayout")
        self.SeedLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedQLabel = QLabel(self.moneroFromSeedLabelContainerQFrame)
        self.moneroFromSeedQLabel.setObjectName(u"moneroFromSeedQLabel")

        self.SeedLabelHLayout.addWidget(self.moneroFromSeedQLabel)

        self.moneroFromSeedLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout.addItem(self.moneroFromSeedLabelContainerQFrameHSpacer)


        self.verticalLayout_16.addWidget(self.moneroFromSeedLabelContainerQFrame)

        self.moneroFromSeedQLineEdit = QLineEdit(self.moneroFromSeedContainerQFrame)
        self.moneroFromSeedQLineEdit.setObjectName(u"moneroFromSeedQLineEdit")

        self.verticalLayout_16.addWidget(self.moneroFromSeedQLineEdit)


        self.horizontalLayout_17.addWidget(self.moneroFromSeedContainerQFrame)

        self.moneroFromSeedPaymentIDContainerQFrame = QFrame(self.moneroFromSeedAndPaymentIDContainerQFrame)
        self.moneroFromSeedPaymentIDContainerQFrame.setObjectName(u"moneroFromSeedPaymentIDContainerQFrame")
        self.moneroFromSeedPaymentIDContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_3 = QVBoxLayout(self.moneroFromSeedPaymentIDContainerQFrame)
        self.ClientVLayout_3.setSpacing(5)
        self.ClientVLayout_3.setObjectName(u"ClientVLayout_3")
        self.ClientVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedPaymentIDLabelContainerQFrame = QFrame(self.moneroFromSeedPaymentIDContainerQFrame)
        self.moneroFromSeedPaymentIDLabelContainerQFrame.setObjectName(u"moneroFromSeedPaymentIDLabelContainerQFrame")
        self.MStrengthLabelHLayout_5 = QHBoxLayout(self.moneroFromSeedPaymentIDLabelContainerQFrame)
        self.MStrengthLabelHLayout_5.setSpacing(15)
        self.MStrengthLabelHLayout_5.setObjectName(u"MStrengthLabelHLayout_5")
        self.MStrengthLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSeedPaymentIDQLabel = QLabel(self.moneroFromSeedPaymentIDLabelContainerQFrame)
        self.moneroFromSeedPaymentIDQLabel.setObjectName(u"moneroFromSeedPaymentIDQLabel")

        self.MStrengthLabelHLayout_5.addWidget(self.moneroFromSeedPaymentIDQLabel)

        self.moneroFromSeedPaymentIDLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_5.addItem(self.moneroFromSeedPaymentIDLabelContainerQFrameHSpacer)


        self.ClientVLayout_3.addWidget(self.moneroFromSeedPaymentIDLabelContainerQFrame)

        self.moneroFromSeedPaymentIDQLineEdit = QLineEdit(self.moneroFromSeedPaymentIDContainerQFrame)
        self.moneroFromSeedPaymentIDQLineEdit.setObjectName(u"moneroFromSeedPaymentIDQLineEdit")

        self.ClientVLayout_3.addWidget(self.moneroFromSeedPaymentIDQLineEdit)


        self.horizontalLayout_17.addWidget(self.moneroFromSeedPaymentIDContainerQFrame)


        self.SeedVLayout.addWidget(self.moneroFromSeedAndPaymentIDContainerQFrame)

        self.moneroFromSeedSpacerContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout.addItem(self.moneroFromSeedSpacerContainerQFrameVSpacer)


        self.verticalLayout_9.addWidget(self.moneroFromSeedSpacerContainerQFrame)

        self.moneroQStackedWidget.addWidget(self.moneroFromSeedQStackedWidget)
        self.moneroFromSpendPrivateKeyQStackedWidget = QWidget()
        self.moneroFromSpendPrivateKeyQStackedWidget.setObjectName(u"moneroFromSpendPrivateKeyQStackedWidget")
        self.verticalLayout_10 = QVBoxLayout(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSpendPrivateKeyContainerQFrame = QFrame(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.moneroFromSpendPrivateKeyContainerQFrame.setObjectName(u"moneroFromSpendPrivateKeyContainerQFrame")
        self.XPrivateKeyVLayout = QVBoxLayout(self.moneroFromSpendPrivateKeyContainerQFrame)
        self.XPrivateKeyVLayout.setSpacing(5)
        self.XPrivateKeyVLayout.setObjectName(u"XPrivateKeyVLayout")
        self.XPrivateKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSpendPrivateKeyLabelContainerQFrame = QFrame(self.moneroFromSpendPrivateKeyContainerQFrame)
        self.moneroFromSpendPrivateKeyLabelContainerQFrame.setObjectName(u"moneroFromSpendPrivateKeyLabelContainerQFrame")
        self.XPrivateKeyLabelHLayout = QHBoxLayout(self.moneroFromSpendPrivateKeyLabelContainerQFrame)
        self.XPrivateKeyLabelHLayout.setSpacing(15)
        self.XPrivateKeyLabelHLayout.setObjectName(u"XPrivateKeyLabelHLayout")
        self.XPrivateKeyLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSpendPrivateKeyQLabel = QLabel(self.moneroFromSpendPrivateKeyLabelContainerQFrame)
        self.moneroFromSpendPrivateKeyQLabel.setObjectName(u"moneroFromSpendPrivateKeyQLabel")

        self.XPrivateKeyLabelHLayout.addWidget(self.moneroFromSpendPrivateKeyQLabel)

        self.moneroFromSpendPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPrivateKeyLabelHLayout.addItem(self.moneroFromSpendPrivateKeyLabelContainerQFrameHSpacer)


        self.XPrivateKeyVLayout.addWidget(self.moneroFromSpendPrivateKeyLabelContainerQFrame)

        self.moneroFromSpendPrivateKeyQLineEdit = QLineEdit(self.moneroFromSpendPrivateKeyContainerQFrame)
        self.moneroFromSpendPrivateKeyQLineEdit.setObjectName(u"moneroFromSpendPrivateKeyQLineEdit")

        self.XPrivateKeyVLayout.addWidget(self.moneroFromSpendPrivateKeyQLineEdit)


        self.verticalLayout_10.addWidget(self.moneroFromSpendPrivateKeyContainerQFrame)

        self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame = QFrame(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame.setObjectName(u"moneroFromSpendPrivateKeyPaymentIDContainerQFrame")
        self.verticalLayout_85 = QVBoxLayout(self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame)
        self.verticalLayout_85.setSpacing(5)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.moneroFromSpendPrivateKeyPaymentIDQLabel = QLabel(self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame)
        self.moneroFromSpendPrivateKeyPaymentIDQLabel.setObjectName(u"moneroFromSpendPrivateKeyPaymentIDQLabel")

        self.verticalLayout_85.addWidget(self.moneroFromSpendPrivateKeyPaymentIDQLabel)

        self.moneroFromSpendPrivateKeyPaymentIDQLineEdit = QLineEdit(self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame)
        self.moneroFromSpendPrivateKeyPaymentIDQLineEdit.setObjectName(u"moneroFromSpendPrivateKeyPaymentIDQLineEdit")

        self.verticalLayout_85.addWidget(self.moneroFromSpendPrivateKeyPaymentIDQLineEdit)


        self.verticalLayout_10.addWidget(self.moneroFromSpendPrivateKeyPaymentIDContainerQFrame)

        self.moneroFromSpendPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.moneroFromSpendPrivateKeyQStackedWidgetVSpacer)

        self.moneroQStackedWidget.addWidget(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.moneroFromPrivateKeyQStackedWidget = QWidget()
        self.moneroFromPrivateKeyQStackedWidget.setObjectName(u"moneroFromPrivateKeyQStackedWidget")
        self.verticalLayout_11 = QVBoxLayout(self.moneroFromPrivateKeyQStackedWidget)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.moneroFromPrivateKeyContainerQFrame = QFrame(self.moneroFromPrivateKeyQStackedWidget)
        self.moneroFromPrivateKeyContainerQFrame.setObjectName(u"moneroFromPrivateKeyContainerQFrame")
        self.XPublicKeyVLayout = QVBoxLayout(self.moneroFromPrivateKeyContainerQFrame)
        self.XPublicKeyVLayout.setSpacing(5)
        self.XPublicKeyVLayout.setObjectName(u"XPublicKeyVLayout")
        self.XPublicKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromPrivateKeyLabelContainerQFrame = QFrame(self.moneroFromPrivateKeyContainerQFrame)
        self.moneroFromPrivateKeyLabelContainerQFrame.setObjectName(u"moneroFromPrivateKeyLabelContainerQFrame")
        self.XPublicKeyLabelHLayout = QHBoxLayout(self.moneroFromPrivateKeyLabelContainerQFrame)
        self.XPublicKeyLabelHLayout.setSpacing(15)
        self.XPublicKeyLabelHLayout.setObjectName(u"XPublicKeyLabelHLayout")
        self.XPublicKeyLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromPrivateKeyQLabel = QLabel(self.moneroFromPrivateKeyLabelContainerQFrame)
        self.moneroFromPrivateKeyQLabel.setObjectName(u"moneroFromPrivateKeyQLabel")

        self.XPublicKeyLabelHLayout.addWidget(self.moneroFromPrivateKeyQLabel)

        self.moneroFromPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPublicKeyLabelHLayout.addItem(self.moneroFromPrivateKeyLabelContainerQFrameHSpacer)


        self.XPublicKeyVLayout.addWidget(self.moneroFromPrivateKeyLabelContainerQFrame)

        self.moneroFromPrivateKeyQLineEdit = QLineEdit(self.moneroFromPrivateKeyContainerQFrame)
        self.moneroFromPrivateKeyQLineEdit.setObjectName(u"moneroFromPrivateKeyQLineEdit")

        self.XPublicKeyVLayout.addWidget(self.moneroFromPrivateKeyQLineEdit)


        self.verticalLayout_11.addWidget(self.moneroFromPrivateKeyContainerQFrame)

        self.moneroFromPrivateKeyPaymentIDContainerQFrame = QFrame(self.moneroFromPrivateKeyQStackedWidget)
        self.moneroFromPrivateKeyPaymentIDContainerQFrame.setObjectName(u"moneroFromPrivateKeyPaymentIDContainerQFrame")
        self.verticalLayout_86 = QVBoxLayout(self.moneroFromPrivateKeyPaymentIDContainerQFrame)
        self.verticalLayout_86.setSpacing(5)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.moneroFromPrivateKeyPaymentIDQLabel = QLabel(self.moneroFromPrivateKeyPaymentIDContainerQFrame)
        self.moneroFromPrivateKeyPaymentIDQLabel.setObjectName(u"moneroFromPrivateKeyPaymentIDQLabel")

        self.verticalLayout_86.addWidget(self.moneroFromPrivateKeyPaymentIDQLabel)

        self.moneroFromPrivateKeyPaymentIDQLineEdit = QLineEdit(self.moneroFromPrivateKeyPaymentIDContainerQFrame)
        self.moneroFromPrivateKeyPaymentIDQLineEdit.setObjectName(u"moneroFromPrivateKeyPaymentIDQLineEdit")

        self.verticalLayout_86.addWidget(self.moneroFromPrivateKeyPaymentIDQLineEdit)


        self.verticalLayout_11.addWidget(self.moneroFromPrivateKeyPaymentIDContainerQFrame)

        self.moneroFromPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.moneroFromPrivateKeyQStackedWidgetVSpacer)

        self.moneroQStackedWidget.addWidget(self.moneroFromPrivateKeyQStackedWidget)
        self.moneroFromWatchOnlyQStackedWidget = QWidget()
        self.moneroFromWatchOnlyQStackedWidget.setObjectName(u"moneroFromWatchOnlyQStackedWidget")
        self.verticalLayout_13 = QVBoxLayout(self.moneroFromWatchOnlyQStackedWidget)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame = QFrame(self.moneroFromWatchOnlyQStackedWidget)
        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame.setObjectName(u"moneroFromWatchOnlyViewPrivateKeyContainerQFrame")
        self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout = QVBoxLayout(self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame)
        self.PrivateKeyVLayout.setSpacing(5)
        self.PrivateKeyVLayout.setObjectName(u"PrivateKeyVLayout")
        self.PrivateKeyVLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame = QFrame(self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame)
        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame.setObjectName(u"moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame")
        self.PrivateKeyLabelHLayout = QHBoxLayout(self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame)
        self.PrivateKeyLabelHLayout.setSpacing(15)
        self.PrivateKeyLabelHLayout.setObjectName(u"PrivateKeyLabelHLayout")
        self.PrivateKeyLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlyViewPrivateKeyQLabel = QLabel(self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame)
        self.moneroFromWatchOnlyViewPrivateKeyQLabel.setObjectName(u"moneroFromWatchOnlyViewPrivateKeyQLabel")

        self.PrivateKeyLabelHLayout.addWidget(self.moneroFromWatchOnlyViewPrivateKeyQLabel)

        self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout.addItem(self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrameHSpacer)


        self.PrivateKeyVLayout.addWidget(self.moneroFromWatchOnlyViewPrivateKeyLabelContainerQFrame)

        self.moneroFromWatchOnlyViewPrivateKeyQLIneEdit = QLineEdit(self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame)
        self.moneroFromWatchOnlyViewPrivateKeyQLIneEdit.setObjectName(u"moneroFromWatchOnlyViewPrivateKeyQLIneEdit")

        self.PrivateKeyVLayout.addWidget(self.moneroFromWatchOnlyViewPrivateKeyQLIneEdit)


        self.verticalLayout_13.addWidget(self.moneroFromWatchOnlyViewPrivateKeyContainerQFrame)

        self.moneroFromWatchOnlySpendPublicKeyContainerQFrame = QFrame(self.moneroFromWatchOnlyQStackedWidget)
        self.moneroFromWatchOnlySpendPublicKeyContainerQFrame.setObjectName(u"moneroFromWatchOnlySpendPublicKeyContainerQFrame")
        self.moneroFromWatchOnlySpendPublicKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_5 = QVBoxLayout(self.moneroFromWatchOnlySpendPublicKeyContainerQFrame)
        self.PrivateKeyVLayout_5.setSpacing(5)
        self.PrivateKeyVLayout_5.setObjectName(u"PrivateKeyVLayout_5")
        self.PrivateKeyVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame = QFrame(self.moneroFromWatchOnlySpendPublicKeyContainerQFrame)
        self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame.setObjectName(u"moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame")
        self.PrivateKeyLabelHLayout_5 = QHBoxLayout(self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame)
        self.PrivateKeyLabelHLayout_5.setSpacing(15)
        self.PrivateKeyLabelHLayout_5.setObjectName(u"PrivateKeyLabelHLayout_5")
        self.PrivateKeyLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlySpendPublicKeyQLabel = QLabel(self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame)
        self.moneroFromWatchOnlySpendPublicKeyQLabel.setObjectName(u"moneroFromWatchOnlySpendPublicKeyQLabel")

        self.PrivateKeyLabelHLayout_5.addWidget(self.moneroFromWatchOnlySpendPublicKeyQLabel)

        self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_5.addItem(self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrameHSpacer)


        self.PrivateKeyVLayout_5.addWidget(self.moneroFromWatchOnlySpendPublicKeyLabelContainerQFrame)

        self.moneroFromWatchOnlySpendPublicKeyQLineEdit = QLineEdit(self.moneroFromWatchOnlySpendPublicKeyContainerQFrame)
        self.moneroFromWatchOnlySpendPublicKeyQLineEdit.setObjectName(u"moneroFromWatchOnlySpendPublicKeyQLineEdit")

        self.PrivateKeyVLayout_5.addWidget(self.moneroFromWatchOnlySpendPublicKeyQLineEdit)


        self.verticalLayout_13.addWidget(self.moneroFromWatchOnlySpendPublicKeyContainerQFrame)

        self.moneroFromWatchOnlyPaymentIDContainerQFrame = QFrame(self.moneroFromWatchOnlyQStackedWidget)
        self.moneroFromWatchOnlyPaymentIDContainerQFrame.setObjectName(u"moneroFromWatchOnlyPaymentIDContainerQFrame")
        self.verticalLayout_87 = QVBoxLayout(self.moneroFromWatchOnlyPaymentIDContainerQFrame)
        self.verticalLayout_87.setSpacing(5)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.moneroFromWatchOnlyPaymentIDQLabel = QLabel(self.moneroFromWatchOnlyPaymentIDContainerQFrame)
        self.moneroFromWatchOnlyPaymentIDQLabel.setObjectName(u"moneroFromWatchOnlyPaymentIDQLabel")

        self.verticalLayout_87.addWidget(self.moneroFromWatchOnlyPaymentIDQLabel)

        self.moneroFromWatchOnlyPaymentIDQLineEdit = QLineEdit(self.moneroFromWatchOnlyPaymentIDContainerQFrame)
        self.moneroFromWatchOnlyPaymentIDQLineEdit.setObjectName(u"moneroFromWatchOnlyPaymentIDQLineEdit")

        self.verticalLayout_87.addWidget(self.moneroFromWatchOnlyPaymentIDQLineEdit)


        self.verticalLayout_13.addWidget(self.moneroFromWatchOnlyPaymentIDContainerQFrame)

        self.moneroQStackedWidget.addWidget(self.moneroFromWatchOnlyQStackedWidget)

        self.moneroPageQWidgetVLayout.addWidget(self.moneroQStackedWidget)

        self.hdQStackedWidget.addWidget(self.moneroPageQWidget)

        self.verticalLayout_2.addWidget(self.hdQStackedWidget)


        self.verticalLayout_3.addWidget(self.dumpsStackQGroupBox)

        self.dumpsDerivationContainerQFrame = QFrame(self.dumpsPageQStackedWidget)
        self.dumpsDerivationContainerQFrame.setObjectName(u"dumpsDerivationContainerQFrame")
        self.dumpsDerivationContainerQFrameVLayout = QVBoxLayout(self.dumpsDerivationContainerQFrame)
        self.dumpsDerivationContainerQFrameVLayout.setSpacing(15)
        self.dumpsDerivationContainerQFrameVLayout.setObjectName(u"dumpsDerivationContainerQFrameVLayout")
        self.dumpsDerivationContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.DerivationQGroupBox = QGroupBox(self.dumpsDerivationContainerQFrame)
        self.DerivationQGroupBox.setObjectName(u"DerivationQGroupBox")
        self.DerivationVLayout = QVBoxLayout(self.DerivationQGroupBox)
        self.DerivationVLayout.setSpacing(5)
        self.DerivationVLayout.setObjectName(u"DerivationVLayout")
        self.DerivationVLayout.setContentsMargins(10, 15, 10, 10)
        self.DerivationsQTabWidget = QTabWidget(self.DerivationQGroupBox)
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
        self.BIP32HLayout.setContentsMargins(0, 5, 0, 0)
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
        self.BIP44HLayout.setContentsMargins(0, 5, 0, 0)
        self.BIP44PurposeQFrame = QFrame(self.BIP44QWidget)
        self.BIP44PurposeQFrame.setObjectName(u"BIP44PurposeQFrame")
        self.BIP44PurposeVLayout = QVBoxLayout(self.BIP44PurposeQFrame)
        self.BIP44PurposeVLayout.setSpacing(5)
        self.BIP44PurposeVLayout.setObjectName(u"BIP44PurposeVLayout")
        self.BIP44PurposeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP44PurposeLabelQFrame = QFrame(self.BIP44PurposeQFrame)
        self.BIP44PurposeLabelQFrame.setObjectName(u"BIP44PurposeLabelQFrame")
        self.BIP44PurposeLabelHLayout = QHBoxLayout(self.BIP44PurposeLabelQFrame)
        self.BIP44PurposeLabelHLayout.setSpacing(15)
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
        self.BIP44CoinTypeLabelHLayout.setSpacing(15)
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
        self.BIP44AccountLabelHLayout.setSpacing(15)
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
        self.BIP44ChangeLabelHLayout.setSpacing(15)
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
        self.BIP44AddressLabelHLayout.setSpacing(15)
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
        self.BIP49HLayout.setContentsMargins(0, 5, 0, 0)
        self.BIP49PurposeQFrame = QFrame(self.BIP49QWidget)
        self.BIP49PurposeQFrame.setObjectName(u"BIP49PurposeQFrame")
        self.BIP49PurposeVLayout = QVBoxLayout(self.BIP49PurposeQFrame)
        self.BIP49PurposeVLayout.setSpacing(5)
        self.BIP49PurposeVLayout.setObjectName(u"BIP49PurposeVLayout")
        self.BIP49PurposeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP49PurposeLabelQFrame = QFrame(self.BIP49PurposeQFrame)
        self.BIP49PurposeLabelQFrame.setObjectName(u"BIP49PurposeLabelQFrame")
        self.BIP49PurposeLabelHLayout = QHBoxLayout(self.BIP49PurposeLabelQFrame)
        self.BIP49PurposeLabelHLayout.setSpacing(15)
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
        self.BIP49CoinTypeLabelHLayout.setSpacing(15)
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
        self.BIP49AccountLabelHLayout.setSpacing(15)
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
        self.BIP49ChangeLabelHLayout.setSpacing(15)
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
        self.BIP49AddressLabelHLayout.setSpacing(15)
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
        self.BIP84HLayout.setContentsMargins(0, 5, 0, 0)
        self.BIP84PurposeQFrame = QFrame(self.BIP84QWidget)
        self.BIP84PurposeQFrame.setObjectName(u"BIP84PurposeQFrame")
        self.BIP84PurposeVLayout = QVBoxLayout(self.BIP84PurposeQFrame)
        self.BIP84PurposeVLayout.setSpacing(5)
        self.BIP84PurposeVLayout.setObjectName(u"BIP84PurposeVLayout")
        self.BIP84PurposeVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP84PurposeLabelQFrame = QFrame(self.BIP84PurposeQFrame)
        self.BIP84PurposeLabelQFrame.setObjectName(u"BIP84PurposeLabelQFrame")
        self.BIP84PurposeLabelHLayout = QHBoxLayout(self.BIP84PurposeLabelQFrame)
        self.BIP84PurposeLabelHLayout.setSpacing(15)
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
        self.BIP84CoinTypeLabelHLayout.setSpacing(15)
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
        self.BIP84AccountLabelHLayout.setSpacing(15)
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
        self.BIP84ChangeLabelHLayout.setSpacing(15)
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
        self.BIP84AddressLabelHLayout.setSpacing(15)
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
        self.horizontalLayout_19.setContentsMargins(0, 5, 0, 0)
        self.BIP86PurposeQFrame = QFrame(self.BIP86QWidget)
        self.BIP86PurposeQFrame.setObjectName(u"BIP86PurposeQFrame")
        self.BIP84PurposeVLayout_2 = QVBoxLayout(self.BIP86PurposeQFrame)
        self.BIP84PurposeVLayout_2.setSpacing(5)
        self.BIP84PurposeVLayout_2.setObjectName(u"BIP84PurposeVLayout_2")
        self.BIP84PurposeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIP86PurposeLabelQFrame = QFrame(self.BIP86PurposeQFrame)
        self.BIP86PurposeLabelQFrame.setObjectName(u"BIP86PurposeLabelQFrame")
        self.BIP84PurposeLabelHLayout_2 = QHBoxLayout(self.BIP86PurposeLabelQFrame)
        self.BIP84PurposeLabelHLayout_2.setSpacing(15)
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
        self.BIP84CoinTypeLabelHLayout_2.setSpacing(15)
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
        self.BIP84AccountLabelHLayout_2.setSpacing(15)
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
        self.BIP84ChangeLabelHLayout_2.setSpacing(15)
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
        self.BIP84AddressLabelHLayout_2.setSpacing(15)
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
        self.BIP141HLayout.setContentsMargins(0, 5, 0, 0)
        self.BIP141PathQFrame = QFrame(self.BIP141QWidget)
        self.BIP141PathQFrame.setObjectName(u"BIP141PathQFrame")
        self.BIP141PathVLayout = QVBoxLayout(self.BIP141PathQFrame)
        self.BIP141PathVLayout.setSpacing(5)
        self.BIP141PathVLayout.setObjectName(u"BIP141PathVLayout")
        self.BIP141PathVLayout.setContentsMargins(0, 0, 0, 0)
        self.BIP141PathLabelQFrame = QFrame(self.BIP141PathQFrame)
        self.BIP141PathLabelQFrame.setObjectName(u"BIP141PathLabelQFrame")
        self.BIP141PathLabelHLayout = QHBoxLayout(self.BIP141PathLabelQFrame)
        self.BIP141PathLabelHLayout.setSpacing(15)
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
        self.BIP141ScriptSemanticsLabelHLayout.setSpacing(15)
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
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.CIP1852PurposeQFrame = QFrame(self.CIP1852QWidget)
        self.CIP1852PurposeQFrame.setObjectName(u"CIP1852PurposeQFrame")
        self.BIP44PurposeVLayout_2 = QVBoxLayout(self.CIP1852PurposeQFrame)
        self.BIP44PurposeVLayout_2.setSpacing(5)
        self.BIP44PurposeVLayout_2.setObjectName(u"BIP44PurposeVLayout_2")
        self.BIP44PurposeVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CIP1852PurposeLabelQFrame = QFrame(self.CIP1852PurposeQFrame)
        self.CIP1852PurposeLabelQFrame.setObjectName(u"CIP1852PurposeLabelQFrame")
        self.BIP44PurposeLabelHLayout_2 = QHBoxLayout(self.CIP1852PurposeLabelQFrame)
        self.BIP44PurposeLabelHLayout_2.setSpacing(15)
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
        self.BIP44CoinTypeLabelHLayout_2.setSpacing(15)
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
        self.BIP44AccountLabelHLayout_2.setSpacing(15)
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
        self.BIP44ChangeLabelHLayout_2.setSpacing(15)
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
        self.BIP44AddressLabelHLayout_2.setSpacing(15)
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
        self.ElectrumQWidget = QWidget()
        self.ElectrumQWidget.setObjectName(u"ElectrumQWidget")
        self.ElectrumQWidgetHLayout = QHBoxLayout(self.ElectrumQWidget)
        self.ElectrumQWidgetHLayout.setSpacing(15)
        self.ElectrumQWidgetHLayout.setObjectName(u"ElectrumQWidgetHLayout")
        self.ElectrumQWidgetHLayout.setContentsMargins(0, 5, 0, 0)
        self.ElectrumChangeQFrame = QFrame(self.ElectrumQWidget)
        self.ElectrumChangeQFrame.setObjectName(u"ElectrumChangeQFrame")
        self.BIP44AccountVLayout_3 = QVBoxLayout(self.ElectrumChangeQFrame)
        self.BIP44AccountVLayout_3.setSpacing(5)
        self.BIP44AccountVLayout_3.setObjectName(u"BIP44AccountVLayout_3")
        self.BIP44AccountVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ElectrumChangeLabelQFrame = QFrame(self.ElectrumChangeQFrame)
        self.ElectrumChangeLabelQFrame.setObjectName(u"ElectrumChangeLabelQFrame")
        self.BIP44AccountLabelHLayout_3 = QHBoxLayout(self.ElectrumChangeLabelQFrame)
        self.BIP44AccountLabelHLayout_3.setSpacing(15)
        self.BIP44AccountLabelHLayout_3.setObjectName(u"BIP44AccountLabelHLayout_3")
        self.BIP44AccountLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ElectrumChangeQLabel = QLabel(self.ElectrumChangeLabelQFrame)
        self.ElectrumChangeQLabel.setObjectName(u"ElectrumChangeQLabel")

        self.BIP44AccountLabelHLayout_3.addWidget(self.ElectrumChangeQLabel)

        self.ElectrumChangeLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AccountLabelHLayout_3.addItem(self.ElectrumChangeLabelHSpacer)


        self.BIP44AccountVLayout_3.addWidget(self.ElectrumChangeLabelQFrame)

        self.ElectrumChangeQLineEdit = QLineEdit(self.ElectrumChangeQFrame)
        self.ElectrumChangeQLineEdit.setObjectName(u"ElectrumChangeQLineEdit")

        self.BIP44AccountVLayout_3.addWidget(self.ElectrumChangeQLineEdit)


        self.ElectrumQWidgetHLayout.addWidget(self.ElectrumChangeQFrame)

        self.ElectrumAddressQFrame = QFrame(self.ElectrumQWidget)
        self.ElectrumAddressQFrame.setObjectName(u"ElectrumAddressQFrame")
        self.BIP44AccountVLayout_4 = QVBoxLayout(self.ElectrumAddressQFrame)
        self.BIP44AccountVLayout_4.setSpacing(5)
        self.BIP44AccountVLayout_4.setObjectName(u"BIP44AccountVLayout_4")
        self.BIP44AccountVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ElectrumAddressLabelQFrame = QFrame(self.ElectrumAddressQFrame)
        self.ElectrumAddressLabelQFrame.setObjectName(u"ElectrumAddressLabelQFrame")
        self.BIP44AccountLabelHLayout_4 = QHBoxLayout(self.ElectrumAddressLabelQFrame)
        self.BIP44AccountLabelHLayout_4.setSpacing(15)
        self.BIP44AccountLabelHLayout_4.setObjectName(u"BIP44AccountLabelHLayout_4")
        self.BIP44AccountLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ElectrumAddressQLabel = QLabel(self.ElectrumAddressLabelQFrame)
        self.ElectrumAddressQLabel.setObjectName(u"ElectrumAddressQLabel")

        self.BIP44AccountLabelHLayout_4.addWidget(self.ElectrumAddressQLabel)

        self.ElectrumAddressLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AccountLabelHLayout_4.addItem(self.ElectrumAddressLabelHSpacer)


        self.BIP44AccountVLayout_4.addWidget(self.ElectrumAddressLabelQFrame)

        self.ElectrumAddressQLineEdit = QLineEdit(self.ElectrumAddressQFrame)
        self.ElectrumAddressQLineEdit.setObjectName(u"ElectrumAddressQLineEdit")

        self.BIP44AccountVLayout_4.addWidget(self.ElectrumAddressQLineEdit)


        self.ElectrumQWidgetHLayout.addWidget(self.ElectrumAddressQFrame)

        self.DerivationsQTabWidget.addTab(self.ElectrumQWidget, "")
        self.MoneroQWidget = QWidget()
        self.MoneroQWidget.setObjectName(u"MoneroQWidget")
        self.MoneroQWidgetHLayout = QHBoxLayout(self.MoneroQWidget)
        self.MoneroQWidgetHLayout.setSpacing(15)
        self.MoneroQWidgetHLayout.setObjectName(u"MoneroQWidgetHLayout")
        self.MoneroQWidgetHLayout.setContentsMargins(0, 5, 0, 0)
        self.MoneroMinorQFrame = QFrame(self.MoneroQWidget)
        self.MoneroMinorQFrame.setObjectName(u"MoneroMinorQFrame")
        self.BIP44AccountVLayout_5 = QVBoxLayout(self.MoneroMinorQFrame)
        self.BIP44AccountVLayout_5.setSpacing(5)
        self.BIP44AccountVLayout_5.setObjectName(u"BIP44AccountVLayout_5")
        self.BIP44AccountVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MoneroMinorLabelQFrame = QFrame(self.MoneroMinorQFrame)
        self.MoneroMinorLabelQFrame.setObjectName(u"MoneroMinorLabelQFrame")
        self.BIP44AccountLabelHLayout_5 = QHBoxLayout(self.MoneroMinorLabelQFrame)
        self.BIP44AccountLabelHLayout_5.setSpacing(15)
        self.BIP44AccountLabelHLayout_5.setObjectName(u"BIP44AccountLabelHLayout_5")
        self.BIP44AccountLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MoneroMinorQLabel = QLabel(self.MoneroMinorLabelQFrame)
        self.MoneroMinorQLabel.setObjectName(u"MoneroMinorQLabel")

        self.BIP44AccountLabelHLayout_5.addWidget(self.MoneroMinorQLabel)

        self.MoneroMinorLabelLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AccountLabelHLayout_5.addItem(self.MoneroMinorLabelLabelHSpacer)


        self.BIP44AccountVLayout_5.addWidget(self.MoneroMinorLabelQFrame)

        self.MoneroMinorQLineEdit = QLineEdit(self.MoneroMinorQFrame)
        self.MoneroMinorQLineEdit.setObjectName(u"MoneroMinorQLineEdit")

        self.BIP44AccountVLayout_5.addWidget(self.MoneroMinorQLineEdit)


        self.MoneroQWidgetHLayout.addWidget(self.MoneroMinorQFrame)

        self.MoneroMajorQFrame = QFrame(self.MoneroQWidget)
        self.MoneroMajorQFrame.setObjectName(u"MoneroMajorQFrame")
        self.BIP44AccountVLayout_6 = QVBoxLayout(self.MoneroMajorQFrame)
        self.BIP44AccountVLayout_6.setSpacing(5)
        self.BIP44AccountVLayout_6.setObjectName(u"BIP44AccountVLayout_6")
        self.BIP44AccountVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.MoneroMajorLabelQFrame = QFrame(self.MoneroMajorQFrame)
        self.MoneroMajorLabelQFrame.setObjectName(u"MoneroMajorLabelQFrame")
        self.BIP44AccountLabelHLayout_6 = QHBoxLayout(self.MoneroMajorLabelQFrame)
        self.BIP44AccountLabelHLayout_6.setSpacing(15)
        self.BIP44AccountLabelHLayout_6.setObjectName(u"BIP44AccountLabelHLayout_6")
        self.BIP44AccountLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.MoneroMajorQLabel = QLabel(self.MoneroMajorLabelQFrame)
        self.MoneroMajorQLabel.setObjectName(u"MoneroMajorQLabel")

        self.BIP44AccountLabelHLayout_6.addWidget(self.MoneroMajorQLabel)

        self.MoneroMajorLabelHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BIP44AccountLabelHLayout_6.addItem(self.MoneroMajorLabelHSpacer)


        self.BIP44AccountVLayout_6.addWidget(self.MoneroMajorLabelQFrame)

        self.MoneroMajorQLineEdit = QLineEdit(self.MoneroMajorQFrame)
        self.MoneroMajorQLineEdit.setObjectName(u"MoneroMajorQLineEdit")

        self.BIP44AccountVLayout_6.addWidget(self.MoneroMajorQLineEdit)


        self.MoneroQWidgetHLayout.addWidget(self.MoneroMajorQFrame)

        self.DerivationsQTabWidget.addTab(self.MoneroQWidget, "")

        self.DerivationVLayout.addWidget(self.DerivationsQTabWidget)


        self.dumpsDerivationContainerQFrameVLayout.addWidget(self.DerivationQGroupBox)


        self.verticalLayout_3.addWidget(self.dumpsDerivationContainerQFrame)

        self.dumpsFormatKeysContainerQGroupBox = QGroupBox(self.dumpsPageQStackedWidget)
        self.dumpsFormatKeysContainerQGroupBox.setObjectName(u"dumpsFormatKeysContainerQGroupBox")
        self.dumpsFormatKeysContainerQFrameHLayout = QHBoxLayout(self.dumpsFormatKeysContainerQGroupBox)
        self.dumpsFormatKeysContainerQFrameHLayout.setSpacing(15)
        self.dumpsFormatKeysContainerQFrameHLayout.setObjectName(u"dumpsFormatKeysContainerQFrameHLayout")
        self.dumpsFormatKeysContainerQFrameHLayout.setContentsMargins(10, 10, 10, 10)
        self.dumpsFormatContainerQFrame = QFrame(self.dumpsFormatKeysContainerQGroupBox)
        self.dumpsFormatContainerQFrame.setObjectName(u"dumpsFormatContainerQFrame")
        self.CryptocurrencyAndFormatHLayout = QHBoxLayout(self.dumpsFormatContainerQFrame)
        self.CryptocurrencyAndFormatHLayout.setSpacing(15)
        self.CryptocurrencyAndFormatHLayout.setObjectName(u"CryptocurrencyAndFormatHLayout")
        self.CryptocurrencyAndFormatHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsformatQFrame = QFrame(self.dumpsFormatContainerQFrame)
        self.dumpsformatQFrame.setObjectName(u"dumpsformatQFrame")
        self.dumpsformatQFrame.setMaximumSize(QSize(100, 16777215))
        self.FormatVLayout = QVBoxLayout(self.dumpsformatQFrame)
        self.FormatVLayout.setSpacing(5)
        self.FormatVLayout.setObjectName(u"FormatVLayout")
        self.FormatVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsFormatLabelContainerQFrame = QFrame(self.dumpsformatQFrame)
        self.dumpsFormatLabelContainerQFrame.setObjectName(u"dumpsFormatLabelContainerQFrame")
        self.FormatLabelHLayout = QHBoxLayout(self.dumpsFormatLabelContainerQFrame)
        self.FormatLabelHLayout.setSpacing(15)
        self.FormatLabelHLayout.setObjectName(u"FormatLabelHLayout")
        self.FormatLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsFormatQLabel = QLabel(self.dumpsFormatLabelContainerQFrame)
        self.dumpsFormatQLabel.setObjectName(u"dumpsFormatQLabel")

        self.FormatLabelHLayout.addWidget(self.dumpsFormatQLabel)

        self.dumpsFormatLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.FormatLabelHLayout.addItem(self.dumpsFormatLabelContainerQFrameHSpacer)


        self.FormatVLayout.addWidget(self.dumpsFormatLabelContainerQFrame)

        self.dumpsormatQComboBox = QComboBox(self.dumpsformatQFrame)
        self.dumpsormatQComboBox.addItem("")
        self.dumpsormatQComboBox.addItem("")
        self.dumpsormatQComboBox.setObjectName(u"dumpsormatQComboBox")

        self.FormatVLayout.addWidget(self.dumpsormatQComboBox)


        self.CryptocurrencyAndFormatHLayout.addWidget(self.dumpsformatQFrame)


        self.dumpsFormatKeysContainerQFrameHLayout.addWidget(self.dumpsFormatContainerQFrame)

        self.dumpsExcludeOrIncludeQFrame = QFrame(self.dumpsFormatKeysContainerQGroupBox)
        self.dumpsExcludeOrIncludeQFrame.setObjectName(u"dumpsExcludeOrIncludeQFrame")
        self.dumpsExcludeOrIncludeQFrame.setMinimumSize(QSize(288, 0))
        self.KeysVLayout = QVBoxLayout(self.dumpsExcludeOrIncludeQFrame)
        self.KeysVLayout.setSpacing(5)
        self.KeysVLayout.setObjectName(u"KeysVLayout")
        self.KeysVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsExcludeOrIncludeLabelContainerQFrame = QFrame(self.dumpsExcludeOrIncludeQFrame)
        self.dumpsExcludeOrIncludeLabelContainerQFrame.setObjectName(u"dumpsExcludeOrIncludeLabelContainerQFrame")
        self.horizontalLayout_21 = QHBoxLayout(self.dumpsExcludeOrIncludeLabelContainerQFrame)
        self.horizontalLayout_21.setSpacing(15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.dumpsExcludeOrIncludeQLabel = QLabel(self.dumpsExcludeOrIncludeLabelContainerQFrame)
        self.dumpsExcludeOrIncludeQLabel.setObjectName(u"dumpsExcludeOrIncludeQLabel")

        self.horizontalLayout_21.addWidget(self.dumpsExcludeOrIncludeQLabel)

        self.dumpsExcludeOrIncludeLabelContainerQFrameHSpacer = QSpacerItem(524, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.dumpsExcludeOrIncludeLabelContainerQFrameHSpacer)


        self.KeysVLayout.addWidget(self.dumpsExcludeOrIncludeLabelContainerQFrame)

        self.dumpsExcludeOrIncludeLabelQFrame = QFrame(self.dumpsExcludeOrIncludeQFrame)
        self.dumpsExcludeOrIncludeLabelQFrame.setObjectName(u"dumpsExcludeOrIncludeLabelQFrame")
        self.verticalLayout_18 = QVBoxLayout(self.dumpsExcludeOrIncludeLabelQFrame)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.dumpsExcludeOrIncludeLineEditContainerQFrame = QFrame(self.dumpsExcludeOrIncludeLabelQFrame)
        self.dumpsExcludeOrIncludeLineEditContainerQFrame.setObjectName(u"dumpsExcludeOrIncludeLineEditContainerQFrame")
        self.horizontalLayout_20 = QHBoxLayout(self.dumpsExcludeOrIncludeLineEditContainerQFrame)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.dumpsExcludeOrIncludeQLineEdit = QLineEdit(self.dumpsExcludeOrIncludeLineEditContainerQFrame)
        self.dumpsExcludeOrIncludeQLineEdit.setObjectName(u"dumpsExcludeOrIncludeQLineEdit")

        self.horizontalLayout_20.addWidget(self.dumpsExcludeOrIncludeQLineEdit)


        self.verticalLayout_18.addWidget(self.dumpsExcludeOrIncludeLineEditContainerQFrame)


        self.KeysVLayout.addWidget(self.dumpsExcludeOrIncludeLabelQFrame)


        self.dumpsFormatKeysContainerQFrameHLayout.addWidget(self.dumpsExcludeOrIncludeQFrame)

        self.dumpsGenerateQPushButton = QPushButton(self.dumpsFormatKeysContainerQGroupBox)
        self.dumpsGenerateQPushButton.setObjectName(u"dumpsGenerateQPushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dumpsGenerateQPushButton.sizePolicy().hasHeightForWidth())
        self.dumpsGenerateQPushButton.setSizePolicy(sizePolicy3)
        self.dumpsGenerateQPushButton.setStyleSheet(u"")

        self.dumpsFormatKeysContainerQFrameHLayout.addWidget(self.dumpsGenerateQPushButton, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.dumpsFormatKeysContainerQGroupBox)

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
        self.outputQFrameVLayout.setContentsMargins(0, 0, 0, 15)
        self.outputFrameTopContainerQFrame = QFrame(self.outputQFrame)
        self.outputFrameTopContainerQFrame.setObjectName(u"outputFrameTopContainerQFrame")
        sizePolicy1.setHeightForWidth(self.outputFrameTopContainerQFrame.sizePolicy().hasHeightForWidth())
        self.outputFrameTopContainerQFrame.setSizePolicy(sizePolicy1)
        self.outputFrameTopContainerQFrameHLayout = QHBoxLayout(self.outputFrameTopContainerQFrame)
        self.outputFrameTopContainerQFrameHLayout.setSpacing(15)
        self.outputFrameTopContainerQFrameHLayout.setObjectName(u"outputFrameTopContainerQFrameHLayout")
        self.outputFrameTopContainerQFrameHLayout.setContentsMargins(15, 15, 15, 15)
        self.outputFrameTopContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.outputFrameTopContainerQFrameHLayout.addItem(self.outputFrameTopContainerQFrameHSpacer)

        self.expandTerminalQFrame = QFrame(self.outputFrameTopContainerQFrame)
        self.expandTerminalQFrame.setObjectName(u"expandTerminalQFrame")
        self.expandTerminalQFrame.setMinimumSize(QSize(25, 25))
        self.expandTerminalQFrame.setMaximumSize(QSize(25, 25))
        self.expandTerminalQFrame.setFrameShape(QFrame.StyledPanel)
        self.expandTerminalQFrame.setFrameShadow(QFrame.Raised)
        self.expandTerminalQFrameVLayout = QVBoxLayout(self.expandTerminalQFrame)
        self.expandTerminalQFrameVLayout.setSpacing(0)
        self.expandTerminalQFrameVLayout.setObjectName(u"expandTerminalQFrameVLayout")
        self.expandTerminalQFrameVLayout.setContentsMargins(0, 0, 0, 0)

        self.outputFrameTopContainerQFrameHLayout.addWidget(self.expandTerminalQFrame)


        self.outputQFrameVLayout.addWidget(self.outputFrameTopContainerQFrame)

        self.outputTerminalQFrame = QFrame(self.outputQFrame)
        self.outputTerminalQFrame.setObjectName(u"outputTerminalQFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.outputTerminalQFrame.sizePolicy().hasHeightForWidth())
        self.outputTerminalQFrame.setSizePolicy(sizePolicy4)
        self.outputTerminalQFrameVLayout = QVBoxLayout(self.outputTerminalQFrame)
        self.outputTerminalQFrameVLayout.setSpacing(0)
        self.outputTerminalQFrameVLayout.setObjectName(u"outputTerminalQFrameVLayout")
        self.outputTerminalQFrameVLayout.setContentsMargins(0, 0, 0, 15)
        self.outputTerminalQTextEdit = QTextEdit(self.outputTerminalQFrame)
        self.outputTerminalQTextEdit.setObjectName(u"outputTerminalQTextEdit")
        self.outputTerminalQTextEdit.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.outputTerminalQTextEdit.sizePolicy().hasHeightForWidth())
        self.outputTerminalQTextEdit.setSizePolicy(sizePolicy5)
        self.outputTerminalQTextEdit.setFrameShape(QFrame.NoFrame)
        self.outputTerminalQTextEdit.setFrameShadow(QFrame.Plain)
        self.outputTerminalQTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.outputTerminalQTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.outputTerminalQTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.outputTerminalQTextEdit.setReadOnly(True)

        self.outputTerminalQFrameVLayout.addWidget(self.outputTerminalQTextEdit)


        self.outputQFrameVLayout.addWidget(self.outputTerminalQFrame)

        self.outputTerminalQLineEdit = QLineEdit(self.outputQFrame)
        self.outputTerminalQLineEdit.setObjectName(u"outputTerminalQLineEdit")

        self.outputQFrameVLayout.addWidget(self.outputTerminalQLineEdit)


        self.centralwidgetHLayout.addWidget(self.outputQFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.hdwalletQStackedWidget.setCurrentIndex(0)
        self.hdQStackedWidget.setCurrentIndex(0)
        self.BIPQStackedWidget.setCurrentIndex(0)
        self.cardanoQStackedWidget.setCurrentIndex(4)
        self.electrumV1QStackedWidget.setCurrentIndex(2)
        self.electrumV2QStackedWidget.setCurrentIndex(2)
        self.moneroQStackedWidget.setCurrentIndex(0)
        self.DerivationsQTabWidget.setCurrentIndex(8)


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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Seed", None))
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
        self.dumpsCryptocurrencyQLabel.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.dumpsCryptocurrencyQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Bitcoin", None))
        self.dumpsCryptocurrencyQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Qtum", None))

        self.dumpsCryptocurrencyQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.dumpsNetworkQLabel.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.dumpsNetworkQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Mainnet", None))
        self.dumpsNetworkQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Testnet", None))

        self.dumpsNetworkQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.dumpsStackQGroupBox.setTitle("")
        self.BIPFromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.BIPFromEntropyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromEntropyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.BIPFromEntropyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.BIPFromEntropyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.BIPFromEntropyPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.BIPFromEntropyPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.BIPFromEntropyLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.BIPFromEntropyLanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.BIPFromEntropyLanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.BIPFromEntropyLanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.BIPFromEntropyLanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.BIPFromEntropyLanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.BIPFromEntropyLanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.BIPFromEntropyLanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.BIPFromEntropyLanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.BIPFromEntropyWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.BIPFromEntropyWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.BIPFromEntropyWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.BIPFromEntropyWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.BIPFromEntropyWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.BIPFromEntropyWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.BIPFromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.BIPFromMnemonicPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromMnemonicPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.BIPFromMnemonicPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.BIPFromMnemonicPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.BIPFromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.BIPFromMnemonicPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.BIPFromSeedsQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.BIPFromSeedPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromSeedPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.BIPFromSeedPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.BIPFromSeedPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.BIPFromXPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.BIPFromXPrivateKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromXPrivateKeyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.BIPFromXPrivateKeyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.BIPFromXPrivateKeyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.BIPFromXPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.BIPFromXPublicKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromXPublicKeyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.BIPFromXPublicKeyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.BIPFromXPublicKeyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.BIPFromWIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.BIPFromWIFPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromWIFPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.BIPFromWIFPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.BIPFromWIFPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.BIPFromWIFBIP38PassphraseQCheckBox.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.BIPFromPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.BIPFromPrivateKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromPrivateKeyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.BIPFromPrivateKeyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.BIPFromPrivateKeyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.BIPFromPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.BIPFromPublicKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromPublicKeyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.BIPFromPublicKeyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Uncompressed", None))

        self.BIPFromPublicKeyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.cardanoFromEntropyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromEntropyCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromEntropyPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.cardanoFromEntropyPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
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
        self.cardanoFromEntropyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromEntropyAddressTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromEntropyWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.cardanoFromEntropyWordsQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.cardanoFromMnemonicCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromMnemonicCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.cardanoFromMnemonicPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.cardanoFromMnemonicLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.cardanoFromMnemonicLanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.cardanoFromMnemonicLanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.cardanoFromMnemonicLanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.cardanoFromMnemonicLanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.cardanoFromMnemonicLanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.cardanoFromMnemonicLanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.cardanoFromMnemonicLanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.cardanoFromMnemonicLanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.cardanoFromMnemonicLanguageQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromMnemonicAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromMnemonicAddressTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromMnemonicWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.cardanoFromMnemonicWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.cardanoFromMnemonicWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.cardanoFromMnemonicWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.cardanoFromMnemonicWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.cardanoFromMnemonicWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.cardanoFromMnemonicWordsQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromSeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.cardanoFromSeedCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromSeedCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
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
        self.cardanoFromSeedPassphraseGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.cardanoFromXPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.cardanoFromXPrivateKeyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromXPrivateKeyCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromXPrivateKeyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.cardanoFromXPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.cardanoFromXPublicKeyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
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
        self.electrumV1FromEntropyPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.electrumV1FromEntropyPassphraseGenerateQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
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
        self.electrumV1FromEntropyWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.electrumV1FromEntropyWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.electrumV1FromEntropyWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.electrumV1FromEntropyWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.electrumV1FromEntropyWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.electrumV1FromEntropyWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.electrumV1FromEntropyWordsQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV1FromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.electrumV1FromMnemonicPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV1FromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.electrumV1FromMnemonicPassphraseGenerateQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
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
        self.electrumV1FromMnemonicWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.electrumV1FromMnemonicWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))

        self.electrumV1FromMnemonicWordsQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
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
        self.electrumV2FromEntropyModeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.electrumV2FromEntropyModeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromEntropyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Uncompressed", None))
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Compressed", None))

        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromEntropyPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.electrumV2FromEntropyPassphraseGenerateQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
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
        self.electrumV2FromEntropyWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.electrumV2FromEntropyWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.electrumV2FromEntropyWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.electrumV2FromEntropyWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.electrumV2FromEntropyWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.electrumV2FromEntropyWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.electrumV2FromEntropyWordsQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.electrumV2FromEntropyMnemonicTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic Type", None))
        self.electrumV2FromEntropyMnemonicTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
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
        self.moneroFromEntropyPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.moneroFromEntropyPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.moneroFromEntropyPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.moneroFromEntropyLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.ELanguageQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.ELanguageQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.ELanguageQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.ELanguageQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.ELanguageQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.ELanguageQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.ELanguageQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.ELanguageQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.ELanguageQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.moneroFromEntropyWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.moneroFromEntropyWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.moneroFromEntropyWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.moneroFromEntropyWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.moneroFromEntropyWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.moneroFromEntropyWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.moneroFromEntropyWordsQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.moneroFromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.moneroFromMnemonicPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.moneroFromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.moneroFromMnemonicPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.moneroFromSeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.moneroFromSeedPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.moneroFromSpendPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Spend Private Key", None))
        self.moneroFromSpendPrivateKeyPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.moneroFromPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.moneroFromPrivateKeyPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.moneroFromWatchOnlyViewPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"View Private key", None))
        self.moneroFromWatchOnlySpendPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Spend Public Key", None))
        self.moneroFromWatchOnlyPaymentIDQLabel.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.DerivationQGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Derivation", None))
        self.CustomPathQLabel.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.CustomPathQLineEdit.setText("")
        self.CustomPathQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"m/0'/0", None))
        self.CustomClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.CustomClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Custom", None))
        self.CustomClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Bitcoin Core", None))
        self.CustomClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"blockchain.info", None))
        self.CustomClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"MultiBit HD", None))
        self.CustomClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Coinomi, Ledger", None))

        self.CustomClientQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
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

        self.BIP44ChangeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
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

        self.BIP49ChangeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
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

        self.BIP84ChangeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
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

        self.BIP86ChangeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
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

        self.BIP141ScriptSemanticsQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
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

        self.CIP1852ChangeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.CIP1852AddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.CIP1852AddressQLineEdit.setText("")
        self.CIP1852AddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.CIP1852QWidget), QCoreApplication.translate("MainWindow", u"CIP1852", None))
        self.ElectrumChangeQLabel.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.ElectrumChangeQLineEdit.setText("")
        self.ElectrumChangeQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ElectrumAddressQLabel.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.ElectrumAddressQLineEdit.setText("")
        self.ElectrumAddressQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.ElectrumQWidget), QCoreApplication.translate("MainWindow", u"Electrum", None))
        self.MoneroMinorQLabel.setText(QCoreApplication.translate("MainWindow", u"Mirnor", None))
        self.MoneroMinorQLineEdit.setText("")
        self.MoneroMinorQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1", None))
        self.MoneroMajorQLabel.setText(QCoreApplication.translate("MainWindow", u"Major", None))
        self.MoneroMajorQLineEdit.setText("")
        self.MoneroMajorQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.DerivationsQTabWidget.setTabText(self.DerivationsQTabWidget.indexOf(self.MoneroQWidget), QCoreApplication.translate("MainWindow", u"Monero", None))
        self.dumpsFormatQLabel.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.dumpsormatQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"JSON", None))
        self.dumpsormatQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CSV", None))

        self.dumpsormatQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.dumpsExcludeOrIncludeQLabel.setText(QCoreApplication.translate("MainWindow", u"Exclude / Include", None))
        self.dumpsGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

