# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hdwalletVlbjMN.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 509)
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
        self.hdWalletHeaderContainerQFrame = QFrame(self.hdWalletContainerQFrame)
        self.hdWalletHeaderContainerQFrame.setObjectName(u"hdWalletHeaderContainerQFrame")
        self.hdWalletHeaderContainerQFrame.setMinimumSize(QSize(525, 47))
        self.hdWalletHeaderContainerQFrame.setMaximumSize(QSize(16777215, 47))
        self.horizontalLayout_6 = QHBoxLayout(self.hdWalletHeaderContainerQFrame)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 15, 0)
        self.hdWalletLogoContainerQFrame = QFrame(self.hdWalletHeaderContainerQFrame)
        self.hdWalletLogoContainerQFrame.setObjectName(u"hdWalletLogoContainerQFrame")
        self.verticalLayout_20 = QVBoxLayout(self.hdWalletLogoContainerQFrame)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.hdWalletLogoContainerQFrame)

        self.hdWalletHeaderContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.hdWalletHeaderContainerQFrameHSpacer)

        self.generateQPushButton = QPushButton(self.hdWalletHeaderContainerQFrame)
        self.generateQPushButton.setObjectName(u"generateQPushButton")

        self.horizontalLayout_6.addWidget(self.generateQPushButton)

        self.dumpQPushButton = QPushButton(self.hdWalletHeaderContainerQFrame)
        self.dumpQPushButton.setObjectName(u"dumpQPushButton")

        self.horizontalLayout_6.addWidget(self.dumpQPushButton)

        self.donationHDWalletQPushButton = QPushButton(self.hdWalletHeaderContainerQFrame)
        self.donationHDWalletQPushButton.setObjectName(u"donationHDWalletQPushButton")

        self.horizontalLayout_6.addWidget(self.donationHDWalletQPushButton)

        self.helpHDWalletQPushButton = QPushButton(self.hdWalletHeaderContainerQFrame)
        self.helpHDWalletQPushButton.setObjectName(u"helpHDWalletQPushButton")

        self.horizontalLayout_6.addWidget(self.helpHDWalletQPushButton)


        self.verticalLayout.addWidget(self.hdWalletHeaderContainerQFrame)

        self.hdwalletQStackedWidget = QStackedWidget(self.hdWalletContainerQFrame)
        self.hdwalletQStackedWidget.setObjectName(u"hdwalletQStackedWidget")
        self.generatePageQStackedWidget = QWidget()
        self.generatePageQStackedWidget.setObjectName(u"generatePageQStackedWidget")
        self.verticalLayout_14 = QVBoxLayout(self.generatePageQStackedWidget)
        self.verticalLayout_14.setSpacing(15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(15, 15, 15, 15)
        self.entropyGeneratorLabelQFrame = QFrame(self.generatePageQStackedWidget)
        self.entropyGeneratorLabelQFrame.setObjectName(u"entropyGeneratorLabelQFrame")
        self.entropyGeneratorLabelQFrame.setFrameShape(QFrame.StyledPanel)
        self.entropyGeneratorLabelQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.entropyGeneratorLabelQFrame)
        self.horizontalLayout_98.setSpacing(15)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.entropyGeneratorQLabel = QLabel(self.entropyGeneratorLabelQFrame)
        self.entropyGeneratorQLabel.setObjectName(u"entropyGeneratorQLabel")
        self.entropyGeneratorQLabel.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_98.addWidget(self.entropyGeneratorQLabel)

        self.entropyGeneratorHLine = QFrame(self.entropyGeneratorLabelQFrame)
        self.entropyGeneratorHLine.setObjectName(u"entropyGeneratorHLine")
        self.entropyGeneratorHLine.setFrameShape(QFrame.HLine)
        self.entropyGeneratorHLine.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_98.addWidget(self.entropyGeneratorHLine)


        self.verticalLayout_14.addWidget(self.entropyGeneratorLabelQFrame)

        self.generateEntopyClientAndStrengthContainerQFrame = QFrame(self.generatePageQStackedWidget)
        self.generateEntopyClientAndStrengthContainerQFrame.setObjectName(u"generateEntopyClientAndStrengthContainerQFrame")
        self.generateEntopyClientAndStrengthContainerQFrame.setLineWidth(0)
        self.verticalLayout_15 = QVBoxLayout(self.generateEntopyClientAndStrengthContainerQFrame)
        self.verticalLayout_15.setSpacing(15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.generateClientAndStrengthContainerQFrame = QFrame(self.generateEntopyClientAndStrengthContainerQFrame)
        self.generateClientAndStrengthContainerQFrame.setObjectName(u"generateClientAndStrengthContainerQFrame")
        self.horizontalLayout_14 = QHBoxLayout(self.generateClientAndStrengthContainerQFrame)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.generateEntropyClientContainerQFrame = QFrame(self.generateClientAndStrengthContainerQFrame)
        self.generateEntropyClientContainerQFrame.setObjectName(u"generateEntropyClientContainerQFrame")
        self.verticalLayout_51 = QVBoxLayout(self.generateEntropyClientContainerQFrame)
        self.verticalLayout_51.setSpacing(5)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.generateEntropyClientQLabel = QLabel(self.generateEntropyClientContainerQFrame)
        self.generateEntropyClientQLabel.setObjectName(u"generateEntropyClientQLabel")

        self.verticalLayout_51.addWidget(self.generateEntropyClientQLabel)

        self.generateEntropyClientQComboBox = QComboBox(self.generateEntropyClientContainerQFrame)
        self.generateEntropyClientQComboBox.setObjectName(u"generateEntropyClientQComboBox")

        self.verticalLayout_51.addWidget(self.generateEntropyClientQComboBox)


        self.horizontalLayout_14.addWidget(self.generateEntropyClientContainerQFrame)

        self.generateEntropyStrengthContainerQFrame = QFrame(self.generateClientAndStrengthContainerQFrame)
        self.generateEntropyStrengthContainerQFrame.setObjectName(u"generateEntropyStrengthContainerQFrame")
        self.verticalLayout_52 = QVBoxLayout(self.generateEntropyStrengthContainerQFrame)
        self.verticalLayout_52.setSpacing(5)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.generateEntropyStrengthQLabel = QLabel(self.generateEntropyStrengthContainerQFrame)
        self.generateEntropyStrengthQLabel.setObjectName(u"generateEntropyStrengthQLabel")

        self.verticalLayout_52.addWidget(self.generateEntropyStrengthQLabel)

        self.generateEntropyStrengthQComboBox = QComboBox(self.generateEntropyStrengthContainerQFrame)
        self.generateEntropyStrengthQComboBox.setObjectName(u"generateEntropyStrengthQComboBox")

        self.verticalLayout_52.addWidget(self.generateEntropyStrengthQComboBox)


        self.horizontalLayout_14.addWidget(self.generateEntropyStrengthContainerQFrame)

        self.generateEntropyClientAndStrengthQPushButton = QPushButton(self.generateClientAndStrengthContainerQFrame)
        self.generateEntropyClientAndStrengthQPushButton.setObjectName(u"generateEntropyClientAndStrengthQPushButton")
        self.generateEntropyClientAndStrengthQPushButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_14.addWidget(self.generateEntropyClientAndStrengthQPushButton, 0, Qt.AlignBottom)


        self.verticalLayout_15.addWidget(self.generateClientAndStrengthContainerQFrame)


        self.verticalLayout_14.addWidget(self.generateEntopyClientAndStrengthContainerQFrame)

        self.generateEntropyContainerQFrame = QFrame(self.generatePageQStackedWidget)
        self.generateEntropyContainerQFrame.setObjectName(u"generateEntropyContainerQFrame")
        self.generateEntropyContainerQFrame.setLineWidth(0)
        self.verticalLayout_68 = QVBoxLayout(self.generateEntropyContainerQFrame)
        self.verticalLayout_68.setSpacing(5)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.generateEntropyLabelContainerQFrame = QFrame(self.generateEntropyContainerQFrame)
        self.generateEntropyLabelContainerQFrame.setObjectName(u"generateEntropyLabelContainerQFrame")
        self.generateEntropyLabelContainerQFrame.setLineWidth(0)
        self.horizontalLayout_73 = QHBoxLayout(self.generateEntropyLabelContainerQFrame)
        self.horizontalLayout_73.setSpacing(5)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.generateEntropyQLabel = QLabel(self.generateEntropyLabelContainerQFrame)
        self.generateEntropyQLabel.setObjectName(u"generateEntropyQLabel")

        self.horizontalLayout_73.addWidget(self.generateEntropyQLabel)

        self.generateEntropyLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_73.addItem(self.generateEntropyLabelContainerQFrameHSpacer)


        self.verticalLayout_68.addWidget(self.generateEntropyLabelContainerQFrame)

        self.generateEntropyLineEditContainerQFrame = QFrame(self.generateEntropyContainerQFrame)
        self.generateEntropyLineEditContainerQFrame.setObjectName(u"generateEntropyLineEditContainerQFrame")
        self.generateEntropyLineEditContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.generateEntropyLineEditContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.generateEntropyLineEditContainerQFrame)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.generateEntropyQLineEdit = QLineEdit(self.generateEntropyLineEditContainerQFrame)
        self.generateEntropyQLineEdit.setObjectName(u"generateEntropyQLineEdit")
        self.generateEntropyQLineEdit.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.generateEntropyQLineEdit)

        self.generateEntropyCopyQLineEdit = QPushButton(self.generateEntropyLineEditContainerQFrame)
        self.generateEntropyCopyQLineEdit.setObjectName(u"generateEntropyCopyQLineEdit")

        self.horizontalLayout_11.addWidget(self.generateEntropyCopyQLineEdit)


        self.verticalLayout_68.addWidget(self.generateEntropyLineEditContainerQFrame)


        self.verticalLayout_14.addWidget(self.generateEntropyContainerQFrame)

        self.mnemonicGeneratorLabelQFrame = QFrame(self.generatePageQStackedWidget)
        self.mnemonicGeneratorLabelQFrame.setObjectName(u"mnemonicGeneratorLabelQFrame")
        self.mnemonicGeneratorLabelQFrame.setFrameShape(QFrame.StyledPanel)
        self.mnemonicGeneratorLabelQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.mnemonicGeneratorLabelQFrame)
        self.horizontalLayout_41.setSpacing(15)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.mnemonicGeneratorQLabel = QLabel(self.mnemonicGeneratorLabelQFrame)
        self.mnemonicGeneratorQLabel.setObjectName(u"mnemonicGeneratorQLabel")
        self.mnemonicGeneratorQLabel.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_41.addWidget(self.mnemonicGeneratorQLabel)

        self.mnemonicGeneratorHLine = QFrame(self.mnemonicGeneratorLabelQFrame)
        self.mnemonicGeneratorHLine.setObjectName(u"mnemonicGeneratorHLine")
        self.mnemonicGeneratorHLine.setFrameShape(QFrame.HLine)
        self.mnemonicGeneratorHLine.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_41.addWidget(self.mnemonicGeneratorHLine)


        self.verticalLayout_14.addWidget(self.mnemonicGeneratorLabelQFrame)

        self.generateMnemonicClientWordsAndLanguageContainerQFrame = QFrame(self.generatePageQStackedWidget)
        self.generateMnemonicClientWordsAndLanguageContainerQFrame.setObjectName(u"generateMnemonicClientWordsAndLanguageContainerQFrame")
        self.verticalLayout_41 = QVBoxLayout(self.generateMnemonicClientWordsAndLanguageContainerQFrame)
        self.verticalLayout_41.setSpacing(15)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicClientWordsLanguageContainerQFrame = QFrame(self.generateMnemonicClientWordsAndLanguageContainerQFrame)
        self.generateMnemonicClientWordsLanguageContainerQFrame.setObjectName(u"generateMnemonicClientWordsLanguageContainerQFrame")
        self.horizontalLayout_60 = QHBoxLayout(self.generateMnemonicClientWordsLanguageContainerQFrame)
        self.horizontalLayout_60.setSpacing(15)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicClientContainerQFrame = QFrame(self.generateMnemonicClientWordsLanguageContainerQFrame)
        self.generateMnemonicClientContainerQFrame.setObjectName(u"generateMnemonicClientContainerQFrame")
        self.verticalLayout_64 = QVBoxLayout(self.generateMnemonicClientContainerQFrame)
        self.verticalLayout_64.setSpacing(5)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicClientQLabel = QLabel(self.generateMnemonicClientContainerQFrame)
        self.generateMnemonicClientQLabel.setObjectName(u"generateMnemonicClientQLabel")

        self.verticalLayout_64.addWidget(self.generateMnemonicClientQLabel)

        self.generateMnemonicClientQComboBox = QComboBox(self.generateMnemonicClientContainerQFrame)
        self.generateMnemonicClientQComboBox.setObjectName(u"generateMnemonicClientQComboBox")

        self.verticalLayout_64.addWidget(self.generateMnemonicClientQComboBox)


        self.horizontalLayout_60.addWidget(self.generateMnemonicClientContainerQFrame)

        self.generateMnemonicWordsContainerQFrame = QFrame(self.generateMnemonicClientWordsLanguageContainerQFrame)
        self.generateMnemonicWordsContainerQFrame.setObjectName(u"generateMnemonicWordsContainerQFrame")
        self.verticalLayout_66 = QVBoxLayout(self.generateMnemonicWordsContainerQFrame)
        self.verticalLayout_66.setSpacing(5)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(-1, 0, 0, 0)
        self.generateMnemonicWordsQLabel = QLabel(self.generateMnemonicWordsContainerQFrame)
        self.generateMnemonicWordsQLabel.setObjectName(u"generateMnemonicWordsQLabel")

        self.verticalLayout_66.addWidget(self.generateMnemonicWordsQLabel)

        self.generateMnemonicWordsQComboBox = QComboBox(self.generateMnemonicWordsContainerQFrame)
        self.generateMnemonicWordsQComboBox.setObjectName(u"generateMnemonicWordsQComboBox")

        self.verticalLayout_66.addWidget(self.generateMnemonicWordsQComboBox)


        self.horizontalLayout_60.addWidget(self.generateMnemonicWordsContainerQFrame)

        self.generateMnemonicLanguageContainerQFrame = QFrame(self.generateMnemonicClientWordsLanguageContainerQFrame)
        self.generateMnemonicLanguageContainerQFrame.setObjectName(u"generateMnemonicLanguageContainerQFrame")
        self.verticalLayout_65 = QVBoxLayout(self.generateMnemonicLanguageContainerQFrame)
        self.verticalLayout_65.setSpacing(5)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicLanguageQLabel = QLabel(self.generateMnemonicLanguageContainerQFrame)
        self.generateMnemonicLanguageQLabel.setObjectName(u"generateMnemonicLanguageQLabel")

        self.verticalLayout_65.addWidget(self.generateMnemonicLanguageQLabel)

        self.generateMnemonicLanguageQComboBox = QComboBox(self.generateMnemonicLanguageContainerQFrame)
        self.generateMnemonicLanguageQComboBox.setObjectName(u"generateMnemonicLanguageQComboBox")

        self.verticalLayout_65.addWidget(self.generateMnemonicLanguageQComboBox)


        self.horizontalLayout_60.addWidget(self.generateMnemonicLanguageContainerQFrame)

        self.generateMnemonicClientWordsAndLanguageQPushButton = QPushButton(self.generateMnemonicClientWordsLanguageContainerQFrame)
        self.generateMnemonicClientWordsAndLanguageQPushButton.setObjectName(u"generateMnemonicClientWordsAndLanguageQPushButton")
        self.generateMnemonicClientWordsAndLanguageQPushButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_60.addWidget(self.generateMnemonicClientWordsAndLanguageQPushButton, 0, Qt.AlignBottom)


        self.verticalLayout_41.addWidget(self.generateMnemonicClientWordsLanguageContainerQFrame)

        self.generateMnemonicContainerQFrame = QFrame(self.generateMnemonicClientWordsAndLanguageContainerQFrame)
        self.generateMnemonicContainerQFrame.setObjectName(u"generateMnemonicContainerQFrame")
        self.generateMnemonicContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.generateMnemonicContainerQFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.generateMnemonicContainerQFrame)
        self.verticalLayout_70.setSpacing(5)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicLabelContainerQFrame = QFrame(self.generateMnemonicContainerQFrame)
        self.generateMnemonicLabelContainerQFrame.setObjectName(u"generateMnemonicLabelContainerQFrame")
        self.horizontalLayout_74 = QHBoxLayout(self.generateMnemonicLabelContainerQFrame)
        self.horizontalLayout_74.setSpacing(5)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicQLabel = QLabel(self.generateMnemonicLabelContainerQFrame)
        self.generateMnemonicQLabel.setObjectName(u"generateMnemonicQLabel")

        self.horizontalLayout_74.addWidget(self.generateMnemonicQLabel)

        self.generateMnemonicLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_74.addItem(self.generateMnemonicLabelContainerQFrameHSpacer)


        self.verticalLayout_70.addWidget(self.generateMnemonicLabelContainerQFrame)

        self.generateMnemonicLineEditContainerQFrame = QFrame(self.generateMnemonicContainerQFrame)
        self.generateMnemonicLineEditContainerQFrame.setObjectName(u"generateMnemonicLineEditContainerQFrame")
        self.generateMnemonicLineEditContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.generateMnemonicLineEditContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.generateMnemonicLineEditContainerQFrame)
        self.horizontalLayout_75.setSpacing(15)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.generateMnemonicQLineEdit = QLineEdit(self.generateMnemonicLineEditContainerQFrame)
        self.generateMnemonicQLineEdit.setObjectName(u"generateMnemonicQLineEdit")
        self.generateMnemonicQLineEdit.setEnabled(False)

        self.horizontalLayout_75.addWidget(self.generateMnemonicQLineEdit)

        self.generateMnemonicCopyQPushButton = QPushButton(self.generateMnemonicLineEditContainerQFrame)
        self.generateMnemonicCopyQPushButton.setObjectName(u"generateMnemonicCopyQPushButton")

        self.horizontalLayout_75.addWidget(self.generateMnemonicCopyQPushButton)


        self.verticalLayout_70.addWidget(self.generateMnemonicLineEditContainerQFrame)


        self.verticalLayout_41.addWidget(self.generateMnemonicContainerQFrame)


        self.verticalLayout_14.addWidget(self.generateMnemonicClientWordsAndLanguageContainerQFrame)

        self.passphraseGeneratorLabelQFrame = QFrame(self.generatePageQStackedWidget)
        self.passphraseGeneratorLabelQFrame.setObjectName(u"passphraseGeneratorLabelQFrame")
        self.passphraseGeneratorLabelQFrame.setFrameShape(QFrame.StyledPanel)
        self.passphraseGeneratorLabelQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.passphraseGeneratorLabelQFrame)
        self.horizontalLayout_30.setSpacing(15)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.passphraseGeneratorQLabel = QLabel(self.passphraseGeneratorLabelQFrame)
        self.passphraseGeneratorQLabel.setObjectName(u"passphraseGeneratorQLabel")
        self.passphraseGeneratorQLabel.setMaximumSize(QSize(116, 16777215))

        self.horizontalLayout_30.addWidget(self.passphraseGeneratorQLabel)

        self.passphraseGeneratorHLine = QFrame(self.passphraseGeneratorLabelQFrame)
        self.passphraseGeneratorHLine.setObjectName(u"passphraseGeneratorHLine")
        self.passphraseGeneratorHLine.setFrameShape(QFrame.HLine)
        self.passphraseGeneratorHLine.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_30.addWidget(self.passphraseGeneratorHLine)


        self.verticalLayout_14.addWidget(self.passphraseGeneratorLabelQFrame)

        self.generateLengthAndPassphraseContainerQFrame = QFrame(self.generatePageQStackedWidget)
        self.generateLengthAndPassphraseContainerQFrame.setObjectName(u"generateLengthAndPassphraseContainerQFrame")
        self.generateLengthAndPassphraseContainerQFrame.setLineWidth(0)
        self.verticalLayout_42 = QVBoxLayout(self.generateLengthAndPassphraseContainerQFrame)
        self.verticalLayout_42.setSpacing(15)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.generateLengthAndPassphraseQFrame = QFrame(self.generateLengthAndPassphraseContainerQFrame)
        self.generateLengthAndPassphraseQFrame.setObjectName(u"generateLengthAndPassphraseQFrame")
        self.generateLengthAndPassphraseQFrame.setEnabled(False)
        self.generateLengthAndPassphraseQFrame.setFrameShape(QFrame.StyledPanel)
        self.generateLengthAndPassphraseQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.generateLengthAndPassphraseQFrame)
        self.horizontalLayout_68.setSpacing(15)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.generateLengthContainerQFrame = QFrame(self.generateLengthAndPassphraseQFrame)
        self.generateLengthContainerQFrame.setObjectName(u"generateLengthContainerQFrame")
        self.generateLengthContainerQFrame.setMaximumSize(QSize(184, 16777215))
        self.generateLengthContainerQFrame.setLineWidth(0)
        self.verticalLayout_63 = QVBoxLayout(self.generateLengthContainerQFrame)
        self.verticalLayout_63.setSpacing(5)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.generateLengthLabelContainerQFrame = QFrame(self.generateLengthContainerQFrame)
        self.generateLengthLabelContainerQFrame.setObjectName(u"generateLengthLabelContainerQFrame")
        self.horizontalLayout_70 = QHBoxLayout(self.generateLengthLabelContainerQFrame)
        self.horizontalLayout_70.setSpacing(5)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.generateLengthQLabel = QLabel(self.generateLengthLabelContainerQFrame)
        self.generateLengthQLabel.setObjectName(u"generateLengthQLabel")

        self.horizontalLayout_70.addWidget(self.generateLengthQLabel)

        self.generateLengthLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_70.addItem(self.generateLengthLabelContainerQFrameHSpacer)


        self.verticalLayout_63.addWidget(self.generateLengthLabelContainerQFrame)

        self.generateLengthLineEditContainerQFrame = QFrame(self.generateLengthContainerQFrame)
        self.generateLengthLineEditContainerQFrame.setObjectName(u"generateLengthLineEditContainerQFrame")
        self.generateLengthLineEditContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.generateLengthLineEditContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.generateLengthLineEditContainerQFrame)
        self.horizontalLayout_71.setSpacing(5)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.generateLengthQLineEdit = QLineEdit(self.generateLengthLineEditContainerQFrame)
        self.generateLengthQLineEdit.setObjectName(u"generateLengthQLineEdit")
        self.generateLengthQLineEdit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_71.addWidget(self.generateLengthQLineEdit)

        self.generatePassphraseLengthQPushButton = QPushButton(self.generateLengthLineEditContainerQFrame)
        self.generatePassphraseLengthQPushButton.setObjectName(u"generatePassphraseLengthQPushButton")
        self.generatePassphraseLengthQPushButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_71.addWidget(self.generatePassphraseLengthQPushButton)


        self.verticalLayout_63.addWidget(self.generateLengthLineEditContainerQFrame)


        self.horizontalLayout_68.addWidget(self.generateLengthContainerQFrame)

        self.generatePassphraseContainerQFrame = QFrame(self.generateLengthAndPassphraseQFrame)
        self.generatePassphraseContainerQFrame.setObjectName(u"generatePassphraseContainerQFrame")
        self.generatePassphraseContainerQFrame.setLineWidth(0)
        self.verticalLayout_67 = QVBoxLayout(self.generatePassphraseContainerQFrame)
        self.verticalLayout_67.setSpacing(5)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.generatePassphraseLabelContainerQFrame = QFrame(self.generatePassphraseContainerQFrame)
        self.generatePassphraseLabelContainerQFrame.setObjectName(u"generatePassphraseLabelContainerQFrame")
        self.generatePassphraseLabelContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.generatePassphraseLabelContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.generatePassphraseLabelContainerQFrame)
        self.horizontalLayout_67.setSpacing(5)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.generatePassphraseQLabel = QLabel(self.generatePassphraseLabelContainerQFrame)
        self.generatePassphraseQLabel.setObjectName(u"generatePassphraseQLabel")

        self.horizontalLayout_67.addWidget(self.generatePassphraseQLabel)

        self.generatePassphraseLabelContainerQFrameHSpacer = QSpacerItem(155, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_67.addItem(self.generatePassphraseLabelContainerQFrameHSpacer)


        self.verticalLayout_67.addWidget(self.generatePassphraseLabelContainerQFrame)

        self.generatePassphraseLineEditContainerQFrame = QFrame(self.generatePassphraseContainerQFrame)
        self.generatePassphraseLineEditContainerQFrame.setObjectName(u"generatePassphraseLineEditContainerQFrame")
        self.generatePassphraseLineEditContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.generatePassphraseLineEditContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.generatePassphraseLineEditContainerQFrame)
        self.horizontalLayout_69.setSpacing(15)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.generatePassphraseQLineEdit = QLineEdit(self.generatePassphraseLineEditContainerQFrame)
        self.generatePassphraseQLineEdit.setObjectName(u"generatePassphraseQLineEdit")

        self.horizontalLayout_69.addWidget(self.generatePassphraseQLineEdit)

        self.generatePassphraseCopyQPushButton = QPushButton(self.generatePassphraseLineEditContainerQFrame)
        self.generatePassphraseCopyQPushButton.setObjectName(u"generatePassphraseCopyQPushButton")

        self.horizontalLayout_69.addWidget(self.generatePassphraseCopyQPushButton)


        self.verticalLayout_67.addWidget(self.generatePassphraseLineEditContainerQFrame)


        self.horizontalLayout_68.addWidget(self.generatePassphraseContainerQFrame)


        self.verticalLayout_42.addWidget(self.generateLengthAndPassphraseQFrame)


        self.verticalLayout_14.addWidget(self.generateLengthAndPassphraseContainerQFrame)

        self.generatePageQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.generatePageQStackedWidgetVSpacer)

        self.hdwalletQStackedWidget.addWidget(self.generatePageQStackedWidget)
        self.dumpsPageQStackedWidget = QWidget()
        self.dumpsPageQStackedWidget.setObjectName(u"dumpsPageQStackedWidget")
        self.verticalLayout_12 = QVBoxLayout(self.dumpsPageQStackedWidget)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.dumpsPageEntireContainerQFrame = QFrame(self.dumpsPageQStackedWidget)
        self.dumpsPageEntireContainerQFrame.setObjectName(u"dumpsPageEntireContainerQFrame")
        self.dumpsPageEntireContainerQFrame.setMinimumSize(QSize(525, 0))
        self.dumpsPageEntireContainerQFrame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.dumpsPageEntireContainerQFrame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 5, 15, 15)
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrame = QFrame(self.dumpsPageEntireContainerQFrame)
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrame.setObjectName(u"dumpsHDFromCryptocurrencyAndNetworkContainerQFrame")
        self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrame)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dumpsHdListComboContainerQFrame = QFrame(self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrame)
        self.dumpsHdListComboContainerQFrame.setObjectName(u"dumpsHdListComboContainerQFrame")
        self.verticalLayout_5 = QVBoxLayout(self.dumpsHdListComboContainerQFrame)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.dumpsHdListLabelContainerQFrame = QFrame(self.dumpsHdListComboContainerQFrame)
        self.dumpsHdListLabelContainerQFrame.setObjectName(u"dumpsHdListLabelContainerQFrame")
        self.dumpsHdListLabelContainerQFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.dumpsHdListLabelContainerQFrame)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dumpsHdListQLabel = QLabel(self.dumpsHdListLabelContainerQFrame)
        self.dumpsHdListQLabel.setObjectName(u"dumpsHdListQLabel")

        self.horizontalLayout_3.addWidget(self.dumpsHdListQLabel)

        self.dumpsHdListLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.dumpsHdListLabelContainerQFrameHSpacer)


        self.verticalLayout_5.addWidget(self.dumpsHdListLabelContainerQFrame)

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
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dumpsHdQComboBox.sizePolicy().hasHeightForWidth())
        self.dumpsHdQComboBox.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.dumpsHdQComboBox)


        self.horizontalLayout_2.addWidget(self.dumpsHdListComboContainerQFrame)

        self.dumpsFromContainerQFrame = QFrame(self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrame)
        self.dumpsFromContainerQFrame.setObjectName(u"dumpsFromContainerQFrame")
        self.verticalLayout_6 = QVBoxLayout(self.dumpsFromContainerQFrame)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.dumpsFromLabelContainerQFrame = QFrame(self.dumpsFromContainerQFrame)
        self.dumpsFromLabelContainerQFrame.setObjectName(u"dumpsFromLabelContainerQFrame")
        self.dumpsFromLabelContainerQFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.dumpsFromLabelContainerQFrame)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dumpsFromQLabel = QLabel(self.dumpsFromLabelContainerQFrame)
        self.dumpsFromQLabel.setObjectName(u"dumpsFromQLabel")

        self.horizontalLayout_8.addWidget(self.dumpsFromQLabel)

        self.dumpsFromLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.dumpsFromLabelContainerQFrameHSpacer)


        self.verticalLayout_6.addWidget(self.dumpsFromLabelContainerQFrame)

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
        sizePolicy.setHeightForWidth(self.dumpsFromQComboBox.sizePolicy().hasHeightForWidth())
        self.dumpsFromQComboBox.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.dumpsFromQComboBox)


        self.horizontalLayout_2.addWidget(self.dumpsFromContainerQFrame)

        self.dumpsCryptocurrencyContainerQFrame = QFrame(self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrame)
        self.dumpsCryptocurrencyContainerQFrame.setObjectName(u"dumpsCryptocurrencyContainerQFrame")
        self.CryptocurrencyVLayout = QVBoxLayout(self.dumpsCryptocurrencyContainerQFrame)
        self.CryptocurrencyVLayout.setSpacing(5)
        self.CryptocurrencyVLayout.setObjectName(u"CryptocurrencyVLayout")
        self.CryptocurrencyVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsCryptocurrencyLabelContainerQFrame = QFrame(self.dumpsCryptocurrencyContainerQFrame)
        self.dumpsCryptocurrencyLabelContainerQFrame.setObjectName(u"dumpsCryptocurrencyLabelContainerQFrame")
        self.CryptocurrencyLabelHLayout = QHBoxLayout(self.dumpsCryptocurrencyLabelContainerQFrame)
        self.CryptocurrencyLabelHLayout.setSpacing(15)
        self.CryptocurrencyLabelHLayout.setObjectName(u"CryptocurrencyLabelHLayout")
        self.CryptocurrencyLabelHLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsCryptocurrencyQLabel = QLabel(self.dumpsCryptocurrencyLabelContainerQFrame)
        self.dumpsCryptocurrencyQLabel.setObjectName(u"dumpsCryptocurrencyQLabel")

        self.CryptocurrencyLabelHLayout.addWidget(self.dumpsCryptocurrencyQLabel)

        self.dumpsCryptocurrencyLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.CryptocurrencyLabelHLayout.addItem(self.dumpsCryptocurrencyLabelContainerQFrameHSpacer)


        self.CryptocurrencyVLayout.addWidget(self.dumpsCryptocurrencyLabelContainerQFrame)

        self.dumpsCryptocurrencyQComboBox = QComboBox(self.dumpsCryptocurrencyContainerQFrame)
        self.dumpsCryptocurrencyQComboBox.addItem("")
        self.dumpsCryptocurrencyQComboBox.addItem("")
        self.dumpsCryptocurrencyQComboBox.setObjectName(u"dumpsCryptocurrencyQComboBox")

        self.CryptocurrencyVLayout.addWidget(self.dumpsCryptocurrencyQComboBox)


        self.horizontalLayout_2.addWidget(self.dumpsCryptocurrencyContainerQFrame)

        self.dumpsNetworkContainerQFrame = QFrame(self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrame)
        self.dumpsNetworkContainerQFrame.setObjectName(u"dumpsNetworkContainerQFrame")
        self.dumpsNetworkContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_25 = QVBoxLayout(self.dumpsNetworkContainerQFrame)
        self.ClientVLayout_25.setSpacing(5)
        self.ClientVLayout_25.setObjectName(u"ClientVLayout_25")
        self.ClientVLayout_25.setContentsMargins(0, 0, 0, 0)
        self.dumpsNetworkLabelContainerQFrame = QFrame(self.dumpsNetworkContainerQFrame)
        self.dumpsNetworkLabelContainerQFrame.setObjectName(u"dumpsNetworkLabelContainerQFrame")
        self.MStrengthLabelHLayout_30 = QHBoxLayout(self.dumpsNetworkLabelContainerQFrame)
        self.MStrengthLabelHLayout_30.setSpacing(15)
        self.MStrengthLabelHLayout_30.setObjectName(u"MStrengthLabelHLayout_30")
        self.MStrengthLabelHLayout_30.setContentsMargins(0, 0, 0, 0)
        self.dumpsNetworkQLabel = QLabel(self.dumpsNetworkLabelContainerQFrame)
        self.dumpsNetworkQLabel.setObjectName(u"dumpsNetworkQLabel")

        self.MStrengthLabelHLayout_30.addWidget(self.dumpsNetworkQLabel)

        self.dumpsNetworkLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_30.addItem(self.dumpsNetworkLabelContainerQFrameHSpacer)


        self.ClientVLayout_25.addWidget(self.dumpsNetworkLabelContainerQFrame)

        self.dumpsNetworkQComboBox = QComboBox(self.dumpsNetworkContainerQFrame)
        self.dumpsNetworkQComboBox.addItem("")
        self.dumpsNetworkQComboBox.addItem("")
        self.dumpsNetworkQComboBox.addItem("")
        self.dumpsNetworkQComboBox.addItem("")
        self.dumpsNetworkQComboBox.addItem("")
        self.dumpsNetworkQComboBox.addItem("")
        self.dumpsNetworkQComboBox.setObjectName(u"dumpsNetworkQComboBox")

        self.ClientVLayout_25.addWidget(self.dumpsNetworkQComboBox)


        self.horizontalLayout_2.addWidget(self.dumpsNetworkContainerQFrame)


        self.verticalLayout_3.addWidget(self.dumpsHDFromCryptocurrencyAndNetworkContainerQFrame)

        self.hdQStackedWidget = QStackedWidget(self.dumpsPageEntireContainerQFrame)
        self.hdQStackedWidget.setObjectName(u"hdQStackedWidget")
        self.hdQStackedWidget.setLineWidth(0)
        self.BIPsPageQWidget = QWidget()
        self.BIPsPageQWidget.setObjectName(u"BIPsPageQWidget")
        self.verticalLayout_21 = QVBoxLayout(self.BIPsPageQWidget)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 15, 0, 0)
        self.BIPQStackedWidget = QStackedWidget(self.BIPsPageQWidget)
        self.BIPQStackedWidget.setObjectName(u"BIPQStackedWidget")
        self.BIPFromEntropyQStackedWidget = QWidget()
        self.BIPFromEntropyQStackedWidget.setObjectName(u"BIPFromEntropyQStackedWidget")
        self.verticalLayout_22 = QVBoxLayout(self.BIPFromEntropyQStackedWidget)
        self.verticalLayout_22.setSpacing(15)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyContainerQFrame = QFrame(self.BIPFromEntropyQStackedWidget)
        self.BIPFromEntropyContainerQFrame.setObjectName(u"BIPFromEntropyContainerQFrame")
        self.verticalLayout_23 = QVBoxLayout(self.BIPFromEntropyContainerQFrame)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyLabelContainerQFrame = QFrame(self.BIPFromEntropyContainerQFrame)
        self.BIPFromEntropyLabelContainerQFrame.setObjectName(u"BIPFromEntropyLabelContainerQFrame")
        self.EntropyLabelHLayout_3 = QHBoxLayout(self.BIPFromEntropyLabelContainerQFrame)
        self.EntropyLabelHLayout_3.setSpacing(15)
        self.EntropyLabelHLayout_3.setObjectName(u"EntropyLabelHLayout_3")
        self.EntropyLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyQLabel = QLabel(self.BIPFromEntropyLabelContainerQFrame)
        self.BIPFromEntropyQLabel.setObjectName(u"BIPFromEntropyQLabel")

        self.EntropyLabelHLayout_3.addWidget(self.BIPFromEntropyQLabel)

        self.BIPFromEntropyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EntropyLabelHLayout_3.addItem(self.BIPFromEntropyLabelContainerQFrameHSpacer)


        self.verticalLayout_23.addWidget(self.BIPFromEntropyLabelContainerQFrame)

        self.BIPFromEntropyEntAndGenerateContainerQFrame = QFrame(self.BIPFromEntropyContainerQFrame)
        self.BIPFromEntropyEntAndGenerateContainerQFrame.setObjectName(u"BIPFromEntropyEntAndGenerateContainerQFrame")
        self.horizontalLayout_23 = QHBoxLayout(self.BIPFromEntropyEntAndGenerateContainerQFrame)
        self.horizontalLayout_23.setSpacing(15)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyGenerateQLineEdit = QLineEdit(self.BIPFromEntropyEntAndGenerateContainerQFrame)
        self.BIPFromEntropyGenerateQLineEdit.setObjectName(u"BIPFromEntropyGenerateQLineEdit")

        self.horizontalLayout_23.addWidget(self.BIPFromEntropyGenerateQLineEdit)


        self.verticalLayout_23.addWidget(self.BIPFromEntropyEntAndGenerateContainerQFrame)


        self.verticalLayout_22.addWidget(self.BIPFromEntropyContainerQFrame)

        self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame = QFrame(self.BIPFromEntropyQStackedWidget)
        self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame.setObjectName(u"BIPFromEntropyPublicKeyAndPassphraseContainerQFrame")
        self.horizontalLayout_24 = QHBoxLayout(self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame)
        self.horizontalLayout_24.setSpacing(15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPublicKeyTypeContainerQFrame = QFrame(self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame)
        self.BIPFromEntropyPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromEntropyPublicKeyTypeContainerQFrame")
        self.BIPFromEntropyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_4 = QVBoxLayout(self.BIPFromEntropyPublicKeyTypeContainerQFrame)
        self.ClientVLayout_4.setSpacing(5)
        self.ClientVLayout_4.setObjectName(u"ClientVLayout_4")
        self.ClientVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromEntropyPublicKeyTypeContainerQFrame)
        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromEntropyPublicKeyTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_6 = QHBoxLayout(self.BIPFromEntropyPublicKeyTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_6.setSpacing(15)
        self.MStrengthLabelHLayout_6.setObjectName(u"MStrengthLabelHLayout_6")
        self.MStrengthLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPublicKeyTypeQLabel = QLabel(self.BIPFromEntropyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromEntropyPublicKeyTypeQLabel.setObjectName(u"BIPFromEntropyPublicKeyTypeQLabel")

        self.MStrengthLabelHLayout_6.addWidget(self.BIPFromEntropyPublicKeyTypeQLabel)

        self.BIPFromEntropyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_6.addItem(self.BIPFromEntropyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_4.addWidget(self.BIPFromEntropyPublicKeyTypeLabelContainerQFrame)

        self.BIPFromEntropyPublicKeyTypeQComboBox = QComboBox(self.BIPFromEntropyPublicKeyTypeContainerQFrame)
        self.BIPFromEntropyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromEntropyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromEntropyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromEntropyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromEntropyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromEntropyPublicKeyTypeQComboBox.addItem("")
        self.BIPFromEntropyPublicKeyTypeQComboBox.setObjectName(u"BIPFromEntropyPublicKeyTypeQComboBox")

        self.ClientVLayout_4.addWidget(self.BIPFromEntropyPublicKeyTypeQComboBox)


        self.horizontalLayout_24.addWidget(self.BIPFromEntropyPublicKeyTypeContainerQFrame)

        self.BIPFromEntropyPassphraseContainerQFrame = QFrame(self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame)
        self.BIPFromEntropyPassphraseContainerQFrame.setObjectName(u"BIPFromEntropyPassphraseContainerQFrame")
        self.EPassphraseVLayout_3 = QVBoxLayout(self.BIPFromEntropyPassphraseContainerQFrame)
        self.EPassphraseVLayout_3.setSpacing(5)
        self.EPassphraseVLayout_3.setObjectName(u"EPassphraseVLayout_3")
        self.EPassphraseVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPassphraseLabelContainerQFrame = QFrame(self.BIPFromEntropyPassphraseContainerQFrame)
        self.BIPFromEntropyPassphraseLabelContainerQFrame.setObjectName(u"BIPFromEntropyPassphraseLabelContainerQFrame")
        self.EPassphraseLabelHLayout_3 = QHBoxLayout(self.BIPFromEntropyPassphraseLabelContainerQFrame)
        self.EPassphraseLabelHLayout_3.setSpacing(15)
        self.EPassphraseLabelHLayout_3.setObjectName(u"EPassphraseLabelHLayout_3")
        self.EPassphraseLabelHLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPassphraseQLabel = QLabel(self.BIPFromEntropyPassphraseLabelContainerQFrame)
        self.BIPFromEntropyPassphraseQLabel.setObjectName(u"BIPFromEntropyPassphraseQLabel")

        self.EPassphraseLabelHLayout_3.addWidget(self.BIPFromEntropyPassphraseQLabel)

        self.BIPFromEntropyPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_3.addItem(self.BIPFromEntropyPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout_3.addWidget(self.BIPFromEntropyPassphraseLabelContainerQFrame)

        self.BIPFromEntropyPassphraseGenerateContainerQFrame = QFrame(self.BIPFromEntropyPassphraseContainerQFrame)
        self.BIPFromEntropyPassphraseGenerateContainerQFrame.setObjectName(u"BIPFromEntropyPassphraseGenerateContainerQFrame")
        self.horizontalLayout_25 = QHBoxLayout(self.BIPFromEntropyPassphraseGenerateContainerQFrame)
        self.horizontalLayout_25.setSpacing(15)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyPassphraseQLineEdit = QLineEdit(self.BIPFromEntropyPassphraseGenerateContainerQFrame)
        self.BIPFromEntropyPassphraseQLineEdit.setObjectName(u"BIPFromEntropyPassphraseQLineEdit")

        self.horizontalLayout_25.addWidget(self.BIPFromEntropyPassphraseQLineEdit)


        self.EPassphraseVLayout_3.addWidget(self.BIPFromEntropyPassphraseGenerateContainerQFrame)


        self.horizontalLayout_24.addWidget(self.BIPFromEntropyPassphraseContainerQFrame)


        self.verticalLayout_22.addWidget(self.BIPFromEntropyPublicKeyAndPassphraseContainerQFrame)

        self.BIPFromEntropyLanguageAndWordsContainerQFrame = QFrame(self.BIPFromEntropyQStackedWidget)
        self.BIPFromEntropyLanguageAndWordsContainerQFrame.setObjectName(u"BIPFromEntropyLanguageAndWordsContainerQFrame")
        self.horizontalLayout_26 = QHBoxLayout(self.BIPFromEntropyLanguageAndWordsContainerQFrame)
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyLanguageContainerQFrame = QFrame(self.BIPFromEntropyLanguageAndWordsContainerQFrame)
        self.BIPFromEntropyLanguageContainerQFrame.setObjectName(u"BIPFromEntropyLanguageContainerQFrame")
        self.ELanguageVLayout_2 = QVBoxLayout(self.BIPFromEntropyLanguageContainerQFrame)
        self.ELanguageVLayout_2.setSpacing(5)
        self.ELanguageVLayout_2.setObjectName(u"ELanguageVLayout_2")
        self.ELanguageVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyLanguageLabelContainerQFrame = QFrame(self.BIPFromEntropyLanguageContainerQFrame)
        self.BIPFromEntropyLanguageLabelContainerQFrame.setObjectName(u"BIPFromEntropyLanguageLabelContainerQFrame")
        self.ELanguageLabelHLayout_2 = QHBoxLayout(self.BIPFromEntropyLanguageLabelContainerQFrame)
        self.ELanguageLabelHLayout_2.setSpacing(15)
        self.ELanguageLabelHLayout_2.setObjectName(u"ELanguageLabelHLayout_2")
        self.ELanguageLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyLanguageQLabel = QLabel(self.BIPFromEntropyLanguageLabelContainerQFrame)
        self.BIPFromEntropyLanguageQLabel.setObjectName(u"BIPFromEntropyLanguageQLabel")

        self.ELanguageLabelHLayout_2.addWidget(self.BIPFromEntropyLanguageQLabel)

        self.BIPFromEntropyLanguageLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout_2.addItem(self.BIPFromEntropyLanguageLabelContainerQFrameHSpacer)


        self.ELanguageVLayout_2.addWidget(self.BIPFromEntropyLanguageLabelContainerQFrame)

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

        self.ELanguageVLayout_2.addWidget(self.BIPFromEntropyLanguageQComboBox)


        self.horizontalLayout_26.addWidget(self.BIPFromEntropyLanguageContainerQFrame)

        self.BIPFromEntropyWordsContainerQFrame = QFrame(self.BIPFromEntropyLanguageAndWordsContainerQFrame)
        self.BIPFromEntropyWordsContainerQFrame.setObjectName(u"BIPFromEntropyWordsContainerQFrame")
        self.EStrengthVLayout_2 = QVBoxLayout(self.BIPFromEntropyWordsContainerQFrame)
        self.EStrengthVLayout_2.setSpacing(5)
        self.EStrengthVLayout_2.setObjectName(u"EStrengthVLayout_2")
        self.EStrengthVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyWordsLabelContainerQFrame = QFrame(self.BIPFromEntropyWordsContainerQFrame)
        self.BIPFromEntropyWordsLabelContainerQFrame.setObjectName(u"BIPFromEntropyWordsLabelContainerQFrame")
        self.EStrengthLabelHLayout_2 = QHBoxLayout(self.BIPFromEntropyWordsLabelContainerQFrame)
        self.EStrengthLabelHLayout_2.setSpacing(15)
        self.EStrengthLabelHLayout_2.setObjectName(u"EStrengthLabelHLayout_2")
        self.EStrengthLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyWordsQLabel = QLabel(self.BIPFromEntropyWordsLabelContainerQFrame)
        self.BIPFromEntropyWordsQLabel.setObjectName(u"BIPFromEntropyWordsQLabel")

        self.EStrengthLabelHLayout_2.addWidget(self.BIPFromEntropyWordsQLabel)

        self.BIPFromEntropyWordsLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout_2.addItem(self.BIPFromEntropyWordsLabelContainerQFrameHSpacer)


        self.EStrengthVLayout_2.addWidget(self.BIPFromEntropyWordsLabelContainerQFrame)

        self.BIPFromEntropyWordsQComboBox = QComboBox(self.BIPFromEntropyWordsContainerQFrame)
        self.BIPFromEntropyWordsQComboBox.addItem("")
        self.BIPFromEntropyWordsQComboBox.addItem("")
        self.BIPFromEntropyWordsQComboBox.addItem("")
        self.BIPFromEntropyWordsQComboBox.addItem("")
        self.BIPFromEntropyWordsQComboBox.addItem("")
        self.BIPFromEntropyWordsQComboBox.setObjectName(u"BIPFromEntropyWordsQComboBox")

        self.EStrengthVLayout_2.addWidget(self.BIPFromEntropyWordsQComboBox)


        self.horizontalLayout_26.addWidget(self.BIPFromEntropyWordsContainerQFrame)


        self.verticalLayout_22.addWidget(self.BIPFromEntropyLanguageAndWordsContainerQFrame)

        self.BIPQStackedWidget.addWidget(self.BIPFromEntropyQStackedWidget)
        self.BIPFromMnemonicQStackedWidget = QWidget()
        self.BIPFromMnemonicQStackedWidget.setObjectName(u"BIPFromMnemonicQStackedWidget")
        self.verticalLayout_24 = QVBoxLayout(self.BIPFromMnemonicQStackedWidget)
        self.verticalLayout_24.setSpacing(15)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicContainerQFrame = QFrame(self.BIPFromMnemonicQStackedWidget)
        self.BIPFromMnemonicContainerQFrame.setObjectName(u"BIPFromMnemonicContainerQFrame")
        self.MnemonicVLayout_2 = QVBoxLayout(self.BIPFromMnemonicContainerQFrame)
        self.MnemonicVLayout_2.setSpacing(5)
        self.MnemonicVLayout_2.setObjectName(u"MnemonicVLayout_2")
        self.MnemonicVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicLabelContainerQFrame = QFrame(self.BIPFromMnemonicContainerQFrame)
        self.BIPFromMnemonicLabelContainerQFrame.setObjectName(u"BIPFromMnemonicLabelContainerQFrame")
        self.MnemonicLabelHLayout_2 = QHBoxLayout(self.BIPFromMnemonicLabelContainerQFrame)
        self.MnemonicLabelHLayout_2.setSpacing(15)
        self.MnemonicLabelHLayout_2.setObjectName(u"MnemonicLabelHLayout_2")
        self.MnemonicLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicQLabel = QLabel(self.BIPFromMnemonicLabelContainerQFrame)
        self.BIPFromMnemonicQLabel.setObjectName(u"BIPFromMnemonicQLabel")

        self.MnemonicLabelHLayout_2.addWidget(self.BIPFromMnemonicQLabel)

        self.BIPFromMnemonicLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MnemonicLabelHLayout_2.addItem(self.BIPFromMnemonicLabelContainerQFrameHSpacer)


        self.MnemonicVLayout_2.addWidget(self.BIPFromMnemonicLabelContainerQFrame)

        self.BIPFromMnemonicLabelGenerateContainerQFrame = QFrame(self.BIPFromMnemonicContainerQFrame)
        self.BIPFromMnemonicLabelGenerateContainerQFrame.setObjectName(u"BIPFromMnemonicLabelGenerateContainerQFrame")
        self.horizontalLayout_27 = QHBoxLayout(self.BIPFromMnemonicLabelGenerateContainerQFrame)
        self.horizontalLayout_27.setSpacing(15)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicQLineEdit = QLineEdit(self.BIPFromMnemonicLabelGenerateContainerQFrame)
        self.BIPFromMnemonicQLineEdit.setObjectName(u"BIPFromMnemonicQLineEdit")

        self.horizontalLayout_27.addWidget(self.BIPFromMnemonicQLineEdit)

        self.BIPFromMnemonicLabelGenerateContainerQFrame_2 = QFrame(self.BIPFromMnemonicLabelGenerateContainerQFrame)
        self.BIPFromMnemonicLabelGenerateContainerQFrame_2.setObjectName(u"BIPFromMnemonicLabelGenerateContainerQFrame_2")
        self.GenerateMnemonicVLayout_2 = QVBoxLayout(self.BIPFromMnemonicLabelGenerateContainerQFrame_2)
        self.GenerateMnemonicVLayout_2.setSpacing(15)
        self.GenerateMnemonicVLayout_2.setObjectName(u"GenerateMnemonicVLayout_2")
        self.GenerateMnemonicVLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_27.addWidget(self.BIPFromMnemonicLabelGenerateContainerQFrame_2)


        self.MnemonicVLayout_2.addWidget(self.BIPFromMnemonicLabelGenerateContainerQFrame)


        self.verticalLayout_24.addWidget(self.BIPFromMnemonicContainerQFrame)

        self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame = QFrame(self.BIPFromMnemonicQStackedWidget)
        self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame.setObjectName(u"BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame")
        self.horizontalLayout_28 = QHBoxLayout(self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame)
        self.horizontalLayout_28.setSpacing(15)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPublicKeyTypeContainerQFrame = QFrame(self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame)
        self.BIPFromMnemonicPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromMnemonicPublicKeyTypeContainerQFrame")
        self.BIPFromMnemonicPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_5 = QVBoxLayout(self.BIPFromMnemonicPublicKeyTypeContainerQFrame)
        self.ClientVLayout_5.setSpacing(5)
        self.ClientVLayout_5.setObjectName(u"ClientVLayout_5")
        self.ClientVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromMnemonicPublicKeyTypeContainerQFrame)
        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromMnemonicPublicKeyTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_7 = QHBoxLayout(self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_7.setSpacing(15)
        self.MStrengthLabelHLayout_7.setObjectName(u"MStrengthLabelHLayout_7")
        self.MStrengthLabelHLayout_7.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPublicKeyTypeQLabel = QLabel(self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrame)
        self.BIPFromMnemonicPublicKeyTypeQLabel.setObjectName(u"BIPFromMnemonicPublicKeyTypeQLabel")

        self.MStrengthLabelHLayout_7.addWidget(self.BIPFromMnemonicPublicKeyTypeQLabel)

        self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_7.addItem(self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_5.addWidget(self.BIPFromMnemonicPublicKeyTypeLabelContainerQFrame)

        self.BIPFromMnemonicPublicKeyTypeQComboBox = QComboBox(self.BIPFromMnemonicPublicKeyTypeContainerQFrame)
        self.BIPFromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.BIPFromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.BIPFromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.BIPFromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.BIPFromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.BIPFromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.BIPFromMnemonicPublicKeyTypeQComboBox.setObjectName(u"BIPFromMnemonicPublicKeyTypeQComboBox")

        self.ClientVLayout_5.addWidget(self.BIPFromMnemonicPublicKeyTypeQComboBox)


        self.horizontalLayout_28.addWidget(self.BIPFromMnemonicPublicKeyTypeContainerQFrame)

        self.BIPFromMnemonicPassphraseContainerQFrame = QFrame(self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame)
        self.BIPFromMnemonicPassphraseContainerQFrame.setObjectName(u"BIPFromMnemonicPassphraseContainerQFrame")
        self.EPassphraseVLayout_4 = QVBoxLayout(self.BIPFromMnemonicPassphraseContainerQFrame)
        self.EPassphraseVLayout_4.setSpacing(5)
        self.EPassphraseVLayout_4.setObjectName(u"EPassphraseVLayout_4")
        self.EPassphraseVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPassphraseLabelContainerQFrame = QFrame(self.BIPFromMnemonicPassphraseContainerQFrame)
        self.BIPFromMnemonicPassphraseLabelContainerQFrame.setObjectName(u"BIPFromMnemonicPassphraseLabelContainerQFrame")
        self.MPassphraseLabelHLayout_2 = QHBoxLayout(self.BIPFromMnemonicPassphraseLabelContainerQFrame)
        self.MPassphraseLabelHLayout_2.setSpacing(15)
        self.MPassphraseLabelHLayout_2.setObjectName(u"MPassphraseLabelHLayout_2")
        self.MPassphraseLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPassphraseQLabel = QLabel(self.BIPFromMnemonicPassphraseLabelContainerQFrame)
        self.BIPFromMnemonicPassphraseQLabel.setObjectName(u"BIPFromMnemonicPassphraseQLabel")

        self.MPassphraseLabelHLayout_2.addWidget(self.BIPFromMnemonicPassphraseQLabel)

        self.BIPFromMnemonicPassphraseLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout_2.addItem(self.BIPFromMnemonicPassphraseLabelContainerQFrameHSpacer)


        self.EPassphraseVLayout_4.addWidget(self.BIPFromMnemonicPassphraseLabelContainerQFrame)

        self.BIPFromMnemonicPassphraseGeneratelContainerQFrame = QFrame(self.BIPFromMnemonicPassphraseContainerQFrame)
        self.BIPFromMnemonicPassphraseGeneratelContainerQFrame.setObjectName(u"BIPFromMnemonicPassphraseGeneratelContainerQFrame")
        self.horizontalLayout_29 = QHBoxLayout(self.BIPFromMnemonicPassphraseGeneratelContainerQFrame)
        self.horizontalLayout_29.setSpacing(15)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicPassphraseQLineEdit = QLineEdit(self.BIPFromMnemonicPassphraseGeneratelContainerQFrame)
        self.BIPFromMnemonicPassphraseQLineEdit.setObjectName(u"BIPFromMnemonicPassphraseQLineEdit")

        self.horizontalLayout_29.addWidget(self.BIPFromMnemonicPassphraseQLineEdit)


        self.EPassphraseVLayout_4.addWidget(self.BIPFromMnemonicPassphraseGeneratelContainerQFrame)


        self.horizontalLayout_28.addWidget(self.BIPFromMnemonicPassphraseContainerQFrame)


        self.verticalLayout_24.addWidget(self.BIPFromMnemonicPublicKeyTypeAndPassphraseQFrame)

        self.BIPFromMnemonicQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.BIPFromMnemonicQStackedWidgetVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromMnemonicQStackedWidget)
        self.BIPFromSeedQStackedWidget = QWidget()
        self.BIPFromSeedQStackedWidget.setObjectName(u"BIPFromSeedQStackedWidget")
        self.verticalLayout_25 = QVBoxLayout(self.BIPFromSeedQStackedWidget)
        self.verticalLayout_25.setSpacing(15)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedContainerQFrame = QFrame(self.BIPFromSeedQStackedWidget)
        self.BIPFromSeedContainerQFrame.setObjectName(u"BIPFromSeedContainerQFrame")
        self.BIPFromSeedContainerQFrame.setMinimumSize(QSize(400, 0))
        self.SeedVLayout_2 = QVBoxLayout(self.BIPFromSeedContainerQFrame)
        self.SeedVLayout_2.setSpacing(5)
        self.SeedVLayout_2.setObjectName(u"SeedVLayout_2")
        self.SeedVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedAndPublicKeyTypeContainerQFrame = QFrame(self.BIPFromSeedContainerQFrame)
        self.BIPFromSeedAndPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromSeedAndPublicKeyTypeContainerQFrame")
        self.horizontalLayout_31 = QHBoxLayout(self.BIPFromSeedAndPublicKeyTypeContainerQFrame)
        self.horizontalLayout_31.setSpacing(15)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedsContainerQFrame = QFrame(self.BIPFromSeedAndPublicKeyTypeContainerQFrame)
        self.BIPFromSeedsContainerQFrame.setObjectName(u"BIPFromSeedsContainerQFrame")
        self.BIPFromSeedsContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.BIPFromSeedsContainerQFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.BIPFromSeedsContainerQFrame)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedsLabelContainerQFrame = QFrame(self.BIPFromSeedsContainerQFrame)
        self.BIPFromSeedsLabelContainerQFrame.setObjectName(u"BIPFromSeedsLabelContainerQFrame")
        self.SeedLabelHLayout_2 = QHBoxLayout(self.BIPFromSeedsLabelContainerQFrame)
        self.SeedLabelHLayout_2.setSpacing(15)
        self.SeedLabelHLayout_2.setObjectName(u"SeedLabelHLayout_2")
        self.SeedLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedsQLabel = QLabel(self.BIPFromSeedsLabelContainerQFrame)
        self.BIPFromSeedsQLabel.setObjectName(u"BIPFromSeedsQLabel")

        self.SeedLabelHLayout_2.addWidget(self.BIPFromSeedsQLabel)

        self.BIPFromSeedsLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SeedLabelHLayout_2.addItem(self.BIPFromSeedsLabelContainerQFrameHSpacer)


        self.verticalLayout_26.addWidget(self.BIPFromSeedsLabelContainerQFrame)

        self.BIPFromSeedsQLineEdit = QLineEdit(self.BIPFromSeedsContainerQFrame)
        self.BIPFromSeedsQLineEdit.setObjectName(u"BIPFromSeedsQLineEdit")

        self.verticalLayout_26.addWidget(self.BIPFromSeedsQLineEdit)


        self.horizontalLayout_31.addWidget(self.BIPFromSeedsContainerQFrame)

        self.BIPFromSeedPublicKeyTypeContainerQFrame = QFrame(self.BIPFromSeedAndPublicKeyTypeContainerQFrame)
        self.BIPFromSeedPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromSeedPublicKeyTypeContainerQFrame")
        self.BIPFromSeedPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_6 = QVBoxLayout(self.BIPFromSeedPublicKeyTypeContainerQFrame)
        self.ClientVLayout_6.setSpacing(5)
        self.ClientVLayout_6.setObjectName(u"ClientVLayout_6")
        self.ClientVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromSeedPublicKeyTypeContainerQFrame)
        self.BIPFromSeedPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromSeedPublicKeyTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_8 = QHBoxLayout(self.BIPFromSeedPublicKeyTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_8.setSpacing(15)
        self.MStrengthLabelHLayout_8.setObjectName(u"MStrengthLabelHLayout_8")
        self.MStrengthLabelHLayout_8.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedPublicKeyTypeQLabel = QLabel(self.BIPFromSeedPublicKeyTypeLabelContainerQFrame)
        self.BIPFromSeedPublicKeyTypeQLabel.setObjectName(u"BIPFromSeedPublicKeyTypeQLabel")

        self.MStrengthLabelHLayout_8.addWidget(self.BIPFromSeedPublicKeyTypeQLabel)

        self.BIPFromSeedPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_8.addItem(self.BIPFromSeedPublicKeyTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_6.addWidget(self.BIPFromSeedPublicKeyTypeLabelContainerQFrame)

        self.BIPFromSeedPublicKeyTypeQComboBox = QComboBox(self.BIPFromSeedPublicKeyTypeContainerQFrame)
        self.BIPFromSeedPublicKeyTypeQComboBox.addItem("")
        self.BIPFromSeedPublicKeyTypeQComboBox.addItem("")
        self.BIPFromSeedPublicKeyTypeQComboBox.addItem("")
        self.BIPFromSeedPublicKeyTypeQComboBox.addItem("")
        self.BIPFromSeedPublicKeyTypeQComboBox.addItem("")
        self.BIPFromSeedPublicKeyTypeQComboBox.addItem("")
        self.BIPFromSeedPublicKeyTypeQComboBox.setObjectName(u"BIPFromSeedPublicKeyTypeQComboBox")

        self.ClientVLayout_6.addWidget(self.BIPFromSeedPublicKeyTypeQComboBox)


        self.horizontalLayout_31.addWidget(self.BIPFromSeedPublicKeyTypeContainerQFrame)


        self.SeedVLayout_2.addWidget(self.BIPFromSeedAndPublicKeyTypeContainerQFrame)

        self.BIPFromSeedContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout_2.addItem(self.BIPFromSeedContainerQFrameVSpacer)


        self.verticalLayout_25.addWidget(self.BIPFromSeedContainerQFrame)

        self.BIPQStackedWidget.addWidget(self.BIPFromSeedQStackedWidget)
        self.BIPFromXPrivateKeyQStackedWidget = QWidget()
        self.BIPFromXPrivateKeyQStackedWidget.setObjectName(u"BIPFromXPrivateKeyQStackedWidget")
        self.verticalLayout_27 = QVBoxLayout(self.BIPFromXPrivateKeyQStackedWidget)
        self.verticalLayout_27.setSpacing(15)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame = QFrame(self.BIPFromXPrivateKeyQStackedWidget)
        self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame.setObjectName(u"BIPFromXPrivateKeyAndPublicKeyTypeQFrame")
        self.horizontalLayout_90 = QHBoxLayout(self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame)
        self.horizontalLayout_90.setSpacing(15)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyContainerQFrame = QFrame(self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame)
        self.BIPFromXPrivateKeyContainerQFrame.setObjectName(u"BIPFromXPrivateKeyContainerQFrame")
        self.BIPFromXPrivateKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_7 = QVBoxLayout(self.BIPFromXPrivateKeyContainerQFrame)
        self.PrivateKeyVLayout_7.setSpacing(5)
        self.PrivateKeyVLayout_7.setObjectName(u"PrivateKeyVLayout_7")
        self.PrivateKeyVLayout_7.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyLabelContainerQFrame = QFrame(self.BIPFromXPrivateKeyContainerQFrame)
        self.BIPFromXPrivateKeyLabelContainerQFrame.setObjectName(u"BIPFromXPrivateKeyLabelContainerQFrame")
        self.PrivateKeyLabelHLayout_7 = QHBoxLayout(self.BIPFromXPrivateKeyLabelContainerQFrame)
        self.PrivateKeyLabelHLayout_7.setSpacing(15)
        self.PrivateKeyLabelHLayout_7.setObjectName(u"PrivateKeyLabelHLayout_7")
        self.PrivateKeyLabelHLayout_7.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyQLabel = QLabel(self.BIPFromXPrivateKeyLabelContainerQFrame)
        self.BIPFromXPrivateKeyQLabel.setObjectName(u"BIPFromXPrivateKeyQLabel")

        self.PrivateKeyLabelHLayout_7.addWidget(self.BIPFromXPrivateKeyQLabel)

        self.BIPFromXPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_7.addItem(self.BIPFromXPrivateKeyLabelContainerQFrameHSpacer)


        self.PrivateKeyVLayout_7.addWidget(self.BIPFromXPrivateKeyLabelContainerQFrame)

        self.BIPFromXPrivateKeyQLineEdit = QLineEdit(self.BIPFromXPrivateKeyContainerQFrame)
        self.BIPFromXPrivateKeyQLineEdit.setObjectName(u"BIPFromXPrivateKeyQLineEdit")

        self.PrivateKeyVLayout_7.addWidget(self.BIPFromXPrivateKeyQLineEdit)


        self.horizontalLayout_90.addWidget(self.BIPFromXPrivateKeyContainerQFrame)

        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame = QFrame(self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame)
        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromXPrivateKeyPublicKeyTypeContainerQFrame")
        self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.verticalLayout_92 = QVBoxLayout(self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame)
        self.verticalLayout_92.setSpacing(5)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame)
        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame")
        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame)
        self.horizontalLayout_91.setSpacing(15)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPrivateKeyPublicKeyTypeQLabel = QLabel(self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromXPrivateKeyPublicKeyTypeQLabel.setObjectName(u"BIPFromXPrivateKeyPublicKeyTypeQLabel")

        self.horizontalLayout_91.addWidget(self.BIPFromXPrivateKeyPublicKeyTypeQLabel)

        self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_91.addItem(self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_92.addWidget(self.BIPFromXPrivateKeyPublicKeyTypeLabelContainerQFrame)

        self.BIPFromXPrivateKeyPublicKeyTypeQComboBox = QComboBox(self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame)
        self.BIPFromXPrivateKeyPublicKeyTypeQComboBox.setObjectName(u"BIPFromXPrivateKeyPublicKeyTypeQComboBox")

        self.verticalLayout_92.addWidget(self.BIPFromXPrivateKeyPublicKeyTypeQComboBox)


        self.horizontalLayout_90.addWidget(self.BIPFromXPrivateKeyPublicKeyTypeContainerQFrame)


        self.verticalLayout_27.addWidget(self.BIPFromXPrivateKeyAndPublicKeyTypeQFrame)

        self.BIPFromXPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.BIPFromXPrivateKeyQStackedWidgetVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromXPrivateKeyQStackedWidget)
        self.BIPFromXPublicKeyQStackedWidget = QWidget()
        self.BIPFromXPublicKeyQStackedWidget.setObjectName(u"BIPFromXPublicKeyQStackedWidget")
        self.verticalLayout_28 = QVBoxLayout(self.BIPFromXPublicKeyQStackedWidget)
        self.verticalLayout_28.setSpacing(15)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame = QFrame(self.BIPFromXPublicKeyQStackedWidget)
        self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame")
        self.horizontalLayout_82 = QHBoxLayout(self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.horizontalLayout_82.setSpacing(15)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyContainerQFrame = QFrame(self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromXPublicKeyContainerQFrame.setObjectName(u"BIPFromXPublicKeyContainerQFrame")
        self.XPublicKeyVLayout_2 = QVBoxLayout(self.BIPFromXPublicKeyContainerQFrame)
        self.XPublicKeyVLayout_2.setSpacing(5)
        self.XPublicKeyVLayout_2.setObjectName(u"XPublicKeyVLayout_2")
        self.XPublicKeyVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyLabelContainerQFrame = QFrame(self.BIPFromXPublicKeyContainerQFrame)
        self.BIPFromXPublicKeyLabelContainerQFrame.setObjectName(u"BIPFromXPublicKeyLabelContainerQFrame")
        self.XPublicKeyLabelHLayout_2 = QHBoxLayout(self.BIPFromXPublicKeyLabelContainerQFrame)
        self.XPublicKeyLabelHLayout_2.setSpacing(15)
        self.XPublicKeyLabelHLayout_2.setObjectName(u"XPublicKeyLabelHLayout_2")
        self.XPublicKeyLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyQLabel = QLabel(self.BIPFromXPublicKeyLabelContainerQFrame)
        self.BIPFromXPublicKeyQLabel.setObjectName(u"BIPFromXPublicKeyQLabel")

        self.XPublicKeyLabelHLayout_2.addWidget(self.BIPFromXPublicKeyQLabel)

        self.BIPFromXPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.XPublicKeyLabelHLayout_2.addItem(self.BIPFromXPublicKeyLabelContainerQFrameHSpacer)


        self.XPublicKeyVLayout_2.addWidget(self.BIPFromXPublicKeyLabelContainerQFrame)

        self.BIPFromXPublicKeyQLineEdit = QLineEdit(self.BIPFromXPublicKeyContainerQFrame)
        self.BIPFromXPublicKeyQLineEdit.setObjectName(u"BIPFromXPublicKeyQLineEdit")

        self.XPublicKeyVLayout_2.addWidget(self.BIPFromXPublicKeyQLineEdit)


        self.horizontalLayout_82.addWidget(self.BIPFromXPublicKeyContainerQFrame)

        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame = QFrame(self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromXPublicKeyPublicKeyTypeContainerQFrame")
        self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.verticalLayout_77 = QVBoxLayout(self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame)
        self.verticalLayout_77.setSpacing(5)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame)
        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame")
        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.horizontalLayout_83.setSpacing(15)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyPublicKeyTypeQLabel = QLabel(self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromXPublicKeyPublicKeyTypeQLabel.setObjectName(u"BIPFromXPublicKeyPublicKeyTypeQLabel")

        self.horizontalLayout_83.addWidget(self.BIPFromXPublicKeyPublicKeyTypeQLabel)

        self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_83.addItem(self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_77.addWidget(self.BIPFromXPublicKeyPublicKeyTypeLabelContainerQFrame)

        self.BIPFromXPublicKeyPublicKeyTypeQComboBox = QComboBox(self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame)
        self.BIPFromXPublicKeyPublicKeyTypeQComboBox.setObjectName(u"BIPFromXPublicKeyPublicKeyTypeQComboBox")

        self.verticalLayout_77.addWidget(self.BIPFromXPublicKeyPublicKeyTypeQComboBox)


        self.horizontalLayout_82.addWidget(self.BIPFromXPublicKeyPublicKeyTypeContainerQFrame)


        self.verticalLayout_28.addWidget(self.BIPFromXPublicKeyAndPublicKeyTypeContainerQFrame)

        self.BIPFromXPublicKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.BIPFromXPublicKeyQStackedWidgetVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromXPublicKeyQStackedWidget)
        self.BIPFromWIFQStackedWidget = QWidget()
        self.BIPFromWIFQStackedWidget.setObjectName(u"BIPFromWIFQStackedWidget")
        self.verticalLayout_29 = QVBoxLayout(self.BIPFromWIFQStackedWidget)
        self.verticalLayout_29.setSpacing(15)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFContainerQFrame = QFrame(self.BIPFromWIFQStackedWidget)
        self.BIPFromWIFContainerQFrame.setObjectName(u"BIPFromWIFContainerQFrame")
        self.BIPFromWIFContainerQFrame.setMinimumSize(QSize(400, 0))
        self.WIFVLayout_2 = QVBoxLayout(self.BIPFromWIFContainerQFrame)
        self.WIFVLayout_2.setSpacing(5)
        self.WIFVLayout_2.setObjectName(u"WIFVLayout_2")
        self.WIFVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFLabelContainerQFrame = QFrame(self.BIPFromWIFContainerQFrame)
        self.BIPFromWIFLabelContainerQFrame.setObjectName(u"BIPFromWIFLabelContainerQFrame")
        self.WIFLabelHLayout_2 = QHBoxLayout(self.BIPFromWIFLabelContainerQFrame)
        self.WIFLabelHLayout_2.setSpacing(15)
        self.WIFLabelHLayout_2.setObjectName(u"WIFLabelHLayout_2")
        self.WIFLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFQLabel = QLabel(self.BIPFromWIFLabelContainerQFrame)
        self.BIPFromWIFQLabel.setObjectName(u"BIPFromWIFQLabel")

        self.WIFLabelHLayout_2.addWidget(self.BIPFromWIFQLabel)

        self.BIPFromWIFLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WIFLabelHLayout_2.addItem(self.BIPFromWIFLabelContainerQFrameHSpacer)


        self.WIFVLayout_2.addWidget(self.BIPFromWIFLabelContainerQFrame)

        self.BIPFromWIFQLineEdit = QLineEdit(self.BIPFromWIFContainerQFrame)
        self.BIPFromWIFQLineEdit.setObjectName(u"BIPFromWIFQLineEdit")

        self.WIFVLayout_2.addWidget(self.BIPFromWIFQLineEdit)


        self.verticalLayout_29.addWidget(self.BIPFromWIFContainerQFrame)

        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame = QFrame(self.BIPFromWIFQStackedWidget)
        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame.setObjectName(u"BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame")
        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)
        self.horizontalLayout_32.setSpacing(15)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFPublicKeyTypeContainerQFrame = QFrame(self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)
        self.BIPFromWIFPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromWIFPublicKeyTypeContainerQFrame")
        self.BIPFromWIFPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.verticalLayout_76 = QVBoxLayout(self.BIPFromWIFPublicKeyTypeContainerQFrame)
        self.verticalLayout_76.setSpacing(5)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromWIFPublicKeyTypeContainerQFrame)
        self.BIPFromWIFPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromWIFPublicKeyTypeLabelContainerQFrame")
        self.horizontalLayout_84 = QHBoxLayout(self.BIPFromWIFPublicKeyTypeLabelContainerQFrame)
        self.horizontalLayout_84.setSpacing(15)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFPublicKeyTypeQLabel = QLabel(self.BIPFromWIFPublicKeyTypeLabelContainerQFrame)
        self.BIPFromWIFPublicKeyTypeQLabel.setObjectName(u"BIPFromWIFPublicKeyTypeQLabel")

        self.horizontalLayout_84.addWidget(self.BIPFromWIFPublicKeyTypeQLabel)

        self.BIPFromWIFPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_84.addItem(self.BIPFromWIFPublicKeyTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_76.addWidget(self.BIPFromWIFPublicKeyTypeLabelContainerQFrame)

        self.BIPFromWIFPublicKeyTypeQComboBox = QComboBox(self.BIPFromWIFPublicKeyTypeContainerQFrame)
        self.BIPFromWIFPublicKeyTypeQComboBox.setObjectName(u"BIPFromWIFPublicKeyTypeQComboBox")

        self.verticalLayout_76.addWidget(self.BIPFromWIFPublicKeyTypeQComboBox)


        self.horizontalLayout_32.addWidget(self.BIPFromWIFPublicKeyTypeContainerQFrame)

        self.BIPFromWIFBIP38PassphraseContainerQFrame = QFrame(self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)
        self.BIPFromWIFBIP38PassphraseContainerQFrame.setObjectName(u"BIPFromWIFBIP38PassphraseContainerQFrame")
        self.verticalLayout_30 = QVBoxLayout(self.BIPFromWIFBIP38PassphraseContainerQFrame)
        self.verticalLayout_30.setSpacing(5)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame = QFrame(self.BIPFromWIFBIP38PassphraseContainerQFrame)
        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame.setObjectName(u"BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame")
        self.EPassphraseLabelHLayout_4 = QHBoxLayout(self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame)
        self.EPassphraseLabelHLayout_4.setSpacing(15)
        self.EPassphraseLabelHLayout_4.setObjectName(u"EPassphraseLabelHLayout_4")
        self.EPassphraseLabelHLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFBIP38PassphraseQCheckBox = QCheckBox(self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame)
        self.BIPFromWIFBIP38PassphraseQCheckBox.setObjectName(u"BIPFromWIFBIP38PassphraseQCheckBox")

        self.EPassphraseLabelHLayout_4.addWidget(self.BIPFromWIFBIP38PassphraseQCheckBox)

        self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout_4.addItem(self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrameHSpacer)


        self.verticalLayout_30.addWidget(self.BIPFromWIFBIP38PassphraseCheckBoxContainerQFrame)

        self.BIPFromWIFBIP38PassphraseGenerateContainerQFrame = QFrame(self.BIPFromWIFBIP38PassphraseContainerQFrame)
        self.BIPFromWIFBIP38PassphraseGenerateContainerQFrame.setObjectName(u"BIPFromWIFBIP38PassphraseGenerateContainerQFrame")
        self.horizontalLayout_85 = QHBoxLayout(self.BIPFromWIFBIP38PassphraseGenerateContainerQFrame)
        self.horizontalLayout_85.setSpacing(15)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFBIP38PassphraseQLineEdit = QLineEdit(self.BIPFromWIFBIP38PassphraseGenerateContainerQFrame)
        self.BIPFromWIFBIP38PassphraseQLineEdit.setObjectName(u"BIPFromWIFBIP38PassphraseQLineEdit")

        self.horizontalLayout_85.addWidget(self.BIPFromWIFBIP38PassphraseQLineEdit)

        self.BIPFromWIFBIP38PassphraseGenerateQPushButton = QPushButton(self.BIPFromWIFBIP38PassphraseGenerateContainerQFrame)
        self.BIPFromWIFBIP38PassphraseGenerateQPushButton.setObjectName(u"BIPFromWIFBIP38PassphraseGenerateQPushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BIPFromWIFBIP38PassphraseGenerateQPushButton.sizePolicy().hasHeightForWidth())
        self.BIPFromWIFBIP38PassphraseGenerateQPushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_85.addWidget(self.BIPFromWIFBIP38PassphraseGenerateQPushButton)


        self.verticalLayout_30.addWidget(self.BIPFromWIFBIP38PassphraseGenerateContainerQFrame)


        self.horizontalLayout_32.addWidget(self.BIPFromWIFBIP38PassphraseContainerQFrame)


        self.verticalLayout_29.addWidget(self.BIPFromWIFPublicKeyAndBIP38PassphraseContainerQFrame)

        self.BIPFromWIFQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.BIPFromWIFQStackedWidgetVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromWIFQStackedWidget)
        self.BIPFromPrivateKeyQStackedWidget = QWidget()
        self.BIPFromPrivateKeyQStackedWidget.setObjectName(u"BIPFromPrivateKeyQStackedWidget")
        self.verticalLayout_31 = QVBoxLayout(self.BIPFromPrivateKeyQStackedWidget)
        self.verticalLayout_31.setSpacing(15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame = QFrame(self.BIPFromPrivateKeyQStackedWidget)
        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame")
        self.horizontalLayout_86 = QHBoxLayout(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.horizontalLayout_86.setSpacing(15)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyContainerQFrame = QFrame(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromPrivateKeyContainerQFrame.setObjectName(u"BIPFromPrivateKeyContainerQFrame")
        self.BIPFromPrivateKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_2 = QVBoxLayout(self.BIPFromPrivateKeyContainerQFrame)
        self.PrivateKeyVLayout_2.setSpacing(5)
        self.PrivateKeyVLayout_2.setObjectName(u"PrivateKeyVLayout_2")
        self.PrivateKeyVLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyLabelContainerQFrame = QFrame(self.BIPFromPrivateKeyContainerQFrame)
        self.BIPFromPrivateKeyLabelContainerQFrame.setObjectName(u"BIPFromPrivateKeyLabelContainerQFrame")
        self.PrivateKeyLabelHLayout_2 = QHBoxLayout(self.BIPFromPrivateKeyLabelContainerQFrame)
        self.PrivateKeyLabelHLayout_2.setSpacing(15)
        self.PrivateKeyLabelHLayout_2.setObjectName(u"PrivateKeyLabelHLayout_2")
        self.PrivateKeyLabelHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyQLabel = QLabel(self.BIPFromPrivateKeyLabelContainerQFrame)
        self.BIPFromPrivateKeyQLabel.setObjectName(u"BIPFromPrivateKeyQLabel")

        self.PrivateKeyLabelHLayout_2.addWidget(self.BIPFromPrivateKeyQLabel)

        self.BIPFromPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_2.addItem(self.BIPFromPrivateKeyLabelContainerQFrameHSpacer)


        self.PrivateKeyVLayout_2.addWidget(self.BIPFromPrivateKeyLabelContainerQFrame)

        self.BIPFromPrivateKeyQLineEdit = QLineEdit(self.BIPFromPrivateKeyContainerQFrame)
        self.BIPFromPrivateKeyQLineEdit.setObjectName(u"BIPFromPrivateKeyQLineEdit")

        self.PrivateKeyVLayout_2.addWidget(self.BIPFromPrivateKeyQLineEdit)


        self.horizontalLayout_86.addWidget(self.BIPFromPrivateKeyContainerQFrame)

        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame_2 = QFrame(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame_2.setObjectName(u"BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame_2")
        self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame_2.setMinimumSize(QSize(150, 0))
        self.verticalLayout_80 = QVBoxLayout(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame_2)
        self.verticalLayout_80.setSpacing(5)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyAndPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame_2)
        self.BIPFromPrivateKeyAndPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromPrivateKeyAndPublicKeyTypeLabelContainerQFrame")
        self.BIPFromPrivateKeyAndPublicKeyTypeLabelContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.BIPFromPrivateKeyAndPublicKeyTypeLabelContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.BIPFromPrivateKeyAndPublicKeyTypeLabelContainerQFrame)
        self.horizontalLayout_87.setSpacing(15)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyPublicKeyTypeQLabel = QLabel(self.BIPFromPrivateKeyAndPublicKeyTypeLabelContainerQFrame)
        self.BIPFromPrivateKeyPublicKeyTypeQLabel.setObjectName(u"BIPFromPrivateKeyPublicKeyTypeQLabel")

        self.horizontalLayout_87.addWidget(self.BIPFromPrivateKeyPublicKeyTypeQLabel)

        self.BIPFromPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_87.addItem(self.BIPFromPrivateKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_80.addWidget(self.BIPFromPrivateKeyAndPublicKeyTypeLabelContainerQFrame)

        self.BIPFromPrivateKeyPublicKeyTypeQComboBox = QComboBox(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame_2)
        self.BIPFromPrivateKeyPublicKeyTypeQComboBox.setObjectName(u"BIPFromPrivateKeyPublicKeyTypeQComboBox")

        self.verticalLayout_80.addWidget(self.BIPFromPrivateKeyPublicKeyTypeQComboBox)


        self.horizontalLayout_86.addWidget(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame_2)


        self.verticalLayout_31.addWidget(self.BIPFromPrivateKeyAndPublicKeyTypeContainerQFrame)

        self.BIPFromPrivateKeyContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.BIPFromPrivateKeyContainerQFrameVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromPrivateKeyQStackedWidget)
        self.BIPFromPublicKeyQStackedWidget = QWidget()
        self.BIPFromPublicKeyQStackedWidget.setObjectName(u"BIPFromPublicKeyQStackedWidget")
        self.verticalLayout_32 = QVBoxLayout(self.BIPFromPublicKeyQStackedWidget)
        self.verticalLayout_32.setSpacing(15)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame = QFrame(self.BIPFromPublicKeyQStackedWidget)
        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromPublicKeyAndPublicKeyTypeContainerQFrame")
        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.horizontalLayout_88.setSpacing(15)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyContainerQFrame = QFrame(self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromPublicKeyContainerQFrame.setObjectName(u"BIPFromPublicKeyContainerQFrame")
        self.BIPFromPublicKeyContainerQFrame.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_6 = QVBoxLayout(self.BIPFromPublicKeyContainerQFrame)
        self.PrivateKeyVLayout_6.setSpacing(5)
        self.PrivateKeyVLayout_6.setObjectName(u"PrivateKeyVLayout_6")
        self.PrivateKeyVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyLabelContainerQFrame = QFrame(self.BIPFromPublicKeyContainerQFrame)
        self.BIPFromPublicKeyLabelContainerQFrame.setObjectName(u"BIPFromPublicKeyLabelContainerQFrame")
        self.PrivateKeyLabelHLayout_6 = QHBoxLayout(self.BIPFromPublicKeyLabelContainerQFrame)
        self.PrivateKeyLabelHLayout_6.setSpacing(15)
        self.PrivateKeyLabelHLayout_6.setObjectName(u"PrivateKeyLabelHLayout_6")
        self.PrivateKeyLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyQLabel = QLabel(self.BIPFromPublicKeyLabelContainerQFrame)
        self.BIPFromPublicKeyQLabel.setObjectName(u"BIPFromPublicKeyQLabel")

        self.PrivateKeyLabelHLayout_6.addWidget(self.BIPFromPublicKeyQLabel)

        self.BIPFromPublicKeyLabelContainerQFrameHSpacer = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_6.addItem(self.BIPFromPublicKeyLabelContainerQFrameHSpacer)


        self.PrivateKeyVLayout_6.addWidget(self.BIPFromPublicKeyLabelContainerQFrame)

        self.BIPFromPublicKeyQLineEdit = QLineEdit(self.BIPFromPublicKeyContainerQFrame)
        self.BIPFromPublicKeyQLineEdit.setObjectName(u"BIPFromPublicKeyQLineEdit")

        self.PrivateKeyVLayout_6.addWidget(self.BIPFromPublicKeyQLineEdit)


        self.horizontalLayout_88.addWidget(self.BIPFromPublicKeyContainerQFrame)

        self.BIPFromPublicKeyPublicKeyTypeContainerQFrame = QFrame(self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame)
        self.BIPFromPublicKeyPublicKeyTypeContainerQFrame.setObjectName(u"BIPFromPublicKeyPublicKeyTypeContainerQFrame")
        self.BIPFromPublicKeyPublicKeyTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.verticalLayout_82 = QVBoxLayout(self.BIPFromPublicKeyPublicKeyTypeContainerQFrame)
        self.verticalLayout_82.setSpacing(5)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.BIPFromPublicKeyPublicKeyTypeContainerQFrame)
        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame")
        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.horizontalLayout_89.setSpacing(15)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPublicKeyPublicKeyTypeQLabel = QLabel(self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame)
        self.BIPFromPublicKeyPublicKeyTypeQLabel.setObjectName(u"BIPFromPublicKeyPublicKeyTypeQLabel")

        self.horizontalLayout_89.addWidget(self.BIPFromPublicKeyPublicKeyTypeQLabel)

        self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_89.addItem(self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrameHSpacer)


        self.verticalLayout_82.addWidget(self.BIPFromPublicKeyPublicKeyTypeLabelContainerQFrame)

        self.BIPFromPublicKeyPublicKeyTypeQComboBox = QComboBox(self.BIPFromPublicKeyPublicKeyTypeContainerQFrame)
        self.BIPFromPublicKeyPublicKeyTypeQComboBox.setObjectName(u"BIPFromPublicKeyPublicKeyTypeQComboBox")

        self.verticalLayout_82.addWidget(self.BIPFromPublicKeyPublicKeyTypeQComboBox)


        self.horizontalLayout_88.addWidget(self.BIPFromPublicKeyPublicKeyTypeContainerQFrame)


        self.verticalLayout_32.addWidget(self.BIPFromPublicKeyAndPublicKeyTypeContainerQFrame)

        self.BIPFromPublicKeyContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.BIPFromPublicKeyContainerQFrameVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromPublicKeyQStackedWidget)

        self.verticalLayout_21.addWidget(self.BIPQStackedWidget)

        self.hdQStackedWidget.addWidget(self.BIPsPageQWidget)
        self.cardanoPageQWidget = QWidget()
        self.cardanoPageQWidget.setObjectName(u"cardanoPageQWidget")
        self.verticalLayout_33 = QVBoxLayout(self.cardanoPageQWidget)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 15, 0, 0)
        self.cardanoQStackedWidget = QStackedWidget(self.cardanoPageQWidget)
        self.cardanoQStackedWidget.setObjectName(u"cardanoQStackedWidget")
        self.cardanoFromEntropyQStackedWidget = QWidget()
        self.cardanoFromEntropyQStackedWidget.setObjectName(u"cardanoFromEntropyQStackedWidget")
        self.verticalLayout_34 = QVBoxLayout(self.cardanoFromEntropyQStackedWidget)
        self.verticalLayout_34.setSpacing(15)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout_34.addWidget(self.cardanoFromEntropyContainerQFrame)

        self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame = QFrame(self.cardanoFromEntropyQStackedWidget)
        self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame.setObjectName(u"cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame")
        self.horizontalLayout_34 = QHBoxLayout(self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame)
        self.horizontalLayout_34.setSpacing(15)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyCardanoTypeContainerQFrame = QFrame(self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame)
        self.cardanoFromEntropyCardanoTypeContainerQFrame.setObjectName(u"cardanoFromEntropyCardanoTypeContainerQFrame")
        self.cardanoFromEntropyCardanoTypeContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_7 = QVBoxLayout(self.cardanoFromEntropyCardanoTypeContainerQFrame)
        self.ClientVLayout_7.setSpacing(5)
        self.ClientVLayout_7.setObjectName(u"ClientVLayout_7")
        self.ClientVLayout_7.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyCardanoTypeLabelContainerQFrame = QFrame(self.cardanoFromEntropyCardanoTypeContainerQFrame)
        self.cardanoFromEntropyCardanoTypeLabelContainerQFrame.setObjectName(u"cardanoFromEntropyCardanoTypeLabelContainerQFrame")
        self.MStrengthLabelHLayout_9 = QHBoxLayout(self.cardanoFromEntropyCardanoTypeLabelContainerQFrame)
        self.MStrengthLabelHLayout_9.setSpacing(15)
        self.MStrengthLabelHLayout_9.setObjectName(u"MStrengthLabelHLayout_9")
        self.MStrengthLabelHLayout_9.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyCardanoTypeQLabel = QLabel(self.cardanoFromEntropyCardanoTypeLabelContainerQFrame)
        self.cardanoFromEntropyCardanoTypeQLabel.setObjectName(u"cardanoFromEntropyCardanoTypeQLabel")

        self.MStrengthLabelHLayout_9.addWidget(self.cardanoFromEntropyCardanoTypeQLabel)

        self.cardanoFromEntropyCardanoTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_9.addItem(self.cardanoFromEntropyCardanoTypeLabelContainerQFrameHSpacer)


        self.ClientVLayout_7.addWidget(self.cardanoFromEntropyCardanoTypeLabelContainerQFrame)

        self.cardanoFromEntropyCardanoTypeQComboBox = QComboBox(self.cardanoFromEntropyCardanoTypeContainerQFrame)
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.addItem("")
        self.cardanoFromEntropyCardanoTypeQComboBox.setObjectName(u"cardanoFromEntropyCardanoTypeQComboBox")

        self.ClientVLayout_7.addWidget(self.cardanoFromEntropyCardanoTypeQComboBox)


        self.horizontalLayout_34.addWidget(self.cardanoFromEntropyCardanoTypeContainerQFrame)

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


        self.horizontalLayout_34.addWidget(self.cardanoFromEntropyPassphraseContainerQFrame)


        self.verticalLayout_34.addWidget(self.cardanoFromEntropyCardanoTypeAndPassphraseContainerQFrame)

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


        self.verticalLayout_34.addWidget(self.cardanoFromEntropyLanguageAddressTypeAndWordsContainerQFrame)

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
        self.cardanoFromSeedContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.cardanoFromSeedContainerQFrame.setFrameShadow(QFrame.Raised)
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

        self.verticalLayout_33.addWidget(self.cardanoQStackedWidget)

        self.hdQStackedWidget.addWidget(self.cardanoPageQWidget)
        self.electrumV1PageQWidget = QWidget()
        self.electrumV1PageQWidget.setObjectName(u"electrumV1PageQWidget")
        self.verticalLayout_45 = QVBoxLayout(self.electrumV1PageQWidget)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 15, 0, 0)
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
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.addItem("")
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
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.addItem("")
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
        self.verticalLayout_49 = QVBoxLayout(self.electrumV1FromSeedQStackedWidget)
        self.verticalLayout_49.setSpacing(15)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromSeedQStackedWidget)
        self.electrumV1FromSeedPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromSeedPublicKeyTypeContainerQFrame")
        self.electrumV1FromSeedPublicKeyTypeContainerQFrame.setMinimumSize(QSize(400, 0))
        self.SeedVLayout_4 = QVBoxLayout(self.electrumV1FromSeedPublicKeyTypeContainerQFrame)
        self.SeedVLayout_4.setSpacing(5)
        self.SeedVLayout_4.setObjectName(u"SeedVLayout_4")
        self.SeedVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromSeedPublicKeyTypeContainerQFrame)
        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromSeedAndPublicKeyTypeContainerQFrame")
        self.horizontalLayout_51 = QHBoxLayout(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)
        self.horizontalLayout_51.setSpacing(15)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedContainerQFrame = QFrame(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)
        self.electrumV1FromSeedContainerQFrame.setObjectName(u"electrumV1FromSeedContainerQFrame")
        self.electrumV1FromSeedContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.electrumV1FromSeedContainerQFrame.setFrameShadow(QFrame.Raised)
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
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.setObjectName(u"electrumV1FromClientQComboBox")

        self.ClientVLayout_12.addWidget(self.electrumV1FromClientQComboBox)


        self.horizontalLayout_51.addWidget(self.electrumV1FromSeedsPublicKeyTypeContainerQFrame)


        self.SeedVLayout_4.addWidget(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrame)

        self.electrumV1FromSeedAndPublicKeyTypeContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout_4.addItem(self.electrumV1FromSeedAndPublicKeyTypeContainerQFrameVSpacer)


        self.verticalLayout_49.addWidget(self.electrumV1FromSeedPublicKeyTypeContainerQFrame)

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

        self.electrumV1FromWIFBIP38PassphraseGenerateContainerQFrame = QFrame(self.electrumV1FromWIFBIP38PassphraseContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseGenerateContainerQFrame.setObjectName(u"electrumV1FromWIFBIP38PassphraseGenerateContainerQFrame")
        self.horizontalLayout_76 = QHBoxLayout(self.electrumV1FromWIFBIP38PassphraseGenerateContainerQFrame)
        self.horizontalLayout_76.setSpacing(15)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFBIP38PassphraseQLineEdit = QLineEdit(self.electrumV1FromWIFBIP38PassphraseGenerateContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseQLineEdit.setObjectName(u"electrumV1FromWIFBIP38PassphraseQLineEdit")

        self.horizontalLayout_76.addWidget(self.electrumV1FromWIFBIP38PassphraseQLineEdit)

        self.electrumV1FromWIFBIP38PassphraseQPushButton = QPushButton(self.electrumV1FromWIFBIP38PassphraseGenerateContainerQFrame)
        self.electrumV1FromWIFBIP38PassphraseQPushButton.setObjectName(u"electrumV1FromWIFBIP38PassphraseQPushButton")
        sizePolicy1.setHeightForWidth(self.electrumV1FromWIFBIP38PassphraseQPushButton.sizePolicy().hasHeightForWidth())
        self.electrumV1FromWIFBIP38PassphraseQPushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_76.addWidget(self.electrumV1FromWIFBIP38PassphraseQPushButton)


        self.verticalLayout_54.addWidget(self.electrumV1FromWIFBIP38PassphraseGenerateContainerQFrame)


        self.horizontalLayout_52.addWidget(self.electrumV1FromWIFBIP38PassphraseContainerQFrame)

        self.electrumV1FromWIFPublicKeyTypeContainerQFrame = QFrame(self.electrumV1FromWIFBIP38AndPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeContainerQFrame.setObjectName(u"electrumV1FromWIFPublicKeyTypeContainerQFrame")
        self.verticalLayout_81 = QVBoxLayout(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)
        self.verticalLayout_81.setSpacing(5)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromWIFPublicKeyTypeLabelContainerQFrame")
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.electrumV1FromWIFPublicKeyTypeLabelContainerQFrame.setFrameShadow(QFrame.Raised)
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
        self.electrumV1FromWIFPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromWIFPublicKeyTypeQComboBox")

        self.verticalLayout_81.addWidget(self.electrumV1FromWIFPublicKeyTypeQComboBox)


        self.horizontalLayout_52.addWidget(self.electrumV1FromWIFPublicKeyTypeContainerQFrame)


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
        self.electrumV1FromPrivateKeyContainerQFrame.setMinimumSize(QSize(400, 0))
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
        self.verticalLayout_83 = QVBoxLayout(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)
        self.verticalLayout_83.setSpacing(5)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame = QFrame(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame")
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.electrumV1FromPublicKeyPublicKeyTypeLabelContainerQFrame.setFrameShadow(QFrame.Raised)
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
        self.electrumV1FromPublicKeyPublicKeyTypeQComboBox.setObjectName(u"electrumV1FromPublicKeyPublicKeyTypeQComboBox")

        self.verticalLayout_83.addWidget(self.electrumV1FromPublicKeyPublicKeyTypeQComboBox)


        self.horizontalLayout_78.addWidget(self.electrumV1FromPublicKeyPublicKeyTypeContainerQFrame)


        self.verticalLayout_56.addWidget(self.electrumV1FromPublicKeyAndPublicKeyTypeContainerQFrame)

        self.electrumV1FromPublicKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.electrumV1FromPublicKeyQStackedWidgetVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromPublicKeyQStackedWidget)

        self.verticalLayout_45.addWidget(self.electrumV1QStackedWidget)

        self.hdQStackedWidget.addWidget(self.electrumV1PageQWidget)
        self.electrumV2PageQWidget = QWidget()
        self.electrumV2PageQWidget.setObjectName(u"electrumV2PageQWidget")
        self.verticalLayout_57 = QVBoxLayout(self.electrumV2PageQWidget)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 15, 0, 0)
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
        self.electrumV2FromEntropyModeLabelContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.electrumV2FromEntropyModeLabelContainerQFrame.setFrameShadow(QFrame.Raised)
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
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.addItem("")
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
        self.electrumV2FromMnemonicMnemonicTypeContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.electrumV2FromMnemonicMnemonicTypeContainerQFrame.setFrameShadow(QFrame.Raised)
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
        self.electrumV2FromMnemonicModeContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.electrumV2FromMnemonicModeContainerQFrame.setFrameShadow(QFrame.Raised)
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
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.addItem("")
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
        self.electrumV2FromSeedsContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.electrumV2FromSeedsContainerQFrame.setFrameShadow(QFrame.Raised)
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
        self.electrumV2FromSeedPublicKeyTypeQComboBox.addItem("")
        self.electrumV2FromSeedPublicKeyTypeQComboBox.addItem("")
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

        self.verticalLayout_57.addWidget(self.electrumV2QStackedWidget)

        self.hdQStackedWidget.addWidget(self.electrumV2PageQWidget)
        self.moneroPageQWidget = QWidget()
        self.moneroPageQWidget.setObjectName(u"moneroPageQWidget")
        self.verticalLayout_69 = QVBoxLayout(self.moneroPageQWidget)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 15, 0, 0)
        self.moneroQStackedWidget = QStackedWidget(self.moneroPageQWidget)
        self.moneroQStackedWidget.setObjectName(u"moneroQStackedWidget")
        self.moneroFromEntropyQStackedWidget = QWidget()
        self.moneroFromEntropyQStackedWidget.setObjectName(u"moneroFromEntropyQStackedWidget")
        self.verticalLayout_4 = QVBoxLayout(self.moneroFromEntropyQStackedWidget)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.moneroFromEntropyQStackedWidget)
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


        self.verticalLayout_8.addWidget(self.EGenerateQFrame)


        self.verticalLayout_4.addWidget(self.frame_16)

        self.frame_7 = QFrame(self.moneroFromEntropyQStackedWidget)
        self.frame_7.setObjectName(u"frame_7")
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
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

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EPassphraseLabelHLayout.addItem(self.horizontalSpacer_8)


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


        self.EPassphraseVLayout.addWidget(self.frame_12)


        self.horizontalLayout_9.addWidget(self.EPassphraseQFrame)

        self.frame_58 = QFrame(self.frame_7)
        self.frame_58.setObjectName(u"frame_58")
        self.verticalLayout_84 = QVBoxLayout(self.frame_58)
        self.verticalLayout_84.setSpacing(5)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.frame_72 = QFrame(self.frame_58)
        self.frame_72.setObjectName(u"frame_72")
        self.horizontalLayout_81 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_81.setSpacing(15)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_72)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_81.addWidget(self.label_38)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_15)


        self.verticalLayout_84.addWidget(self.frame_72)

        self.lineEdit_2 = QLineEdit(self.frame_58)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_84.addWidget(self.lineEdit_2)


        self.horizontalLayout_9.addWidget(self.frame_58)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.moneroFromEntropyQStackedWidget)
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

        self.moneroQStackedWidget.addWidget(self.moneroFromEntropyQStackedWidget)
        self.moneroFromMnemonicQStackedWidget = QWidget()
        self.moneroFromMnemonicQStackedWidget.setObjectName(u"moneroFromMnemonicQStackedWidget")
        self.verticalLayout_7 = QVBoxLayout(self.moneroFromMnemonicQStackedWidget)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.MnemonicQFrame = QFrame(self.moneroFromMnemonicQStackedWidget)
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

        self.horizontalLayout_10.addWidget(self.MGenerateQFrame)


        self.MnemonicVLayout.addWidget(self.frame_13)


        self.verticalLayout_7.addWidget(self.MnemonicQFrame)

        self.frame_15 = QFrame(self.moneroFromMnemonicQStackedWidget)
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

        self.lineEdit_6 = QLineEdit(self.ClientQFrame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.ClientVLayout_2.addWidget(self.lineEdit_6)


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


        self.EPassphraseVLayout_2.addWidget(self.frame_19)


        self.horizontalLayout_12.addWidget(self.MPassphraseQFrame)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.moneroQStackedWidget.addWidget(self.moneroFromMnemonicQStackedWidget)
        self.moneroFromSeedQStackedWidget = QWidget()
        self.moneroFromSeedQStackedWidget.setObjectName(u"moneroFromSeedQStackedWidget")
        self.verticalLayout_9 = QVBoxLayout(self.moneroFromSeedQStackedWidget)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.SeedQFrame = QFrame(self.moneroFromSeedQStackedWidget)
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

        self.lineEdit_7 = QLineEdit(self.ClientQFrame_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.ClientVLayout_3.addWidget(self.lineEdit_7)


        self.horizontalLayout_17.addWidget(self.ClientQFrame_3)


        self.SeedVLayout.addWidget(self.frame_20)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout.addItem(self.verticalSpacer)


        self.verticalLayout_9.addWidget(self.SeedQFrame)

        self.moneroQStackedWidget.addWidget(self.moneroFromSeedQStackedWidget)
        self.moneroFromSpendPrivateKeyQStackedWidget = QWidget()
        self.moneroFromSpendPrivateKeyQStackedWidget.setObjectName(u"moneroFromSpendPrivateKeyQStackedWidget")
        self.verticalLayout_10 = QVBoxLayout(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.XPrivateKeyQFrame = QFrame(self.moneroFromSpendPrivateKeyQStackedWidget)
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

        self.frame_59 = QFrame(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.frame_59.setObjectName(u"frame_59")
        self.verticalLayout_85 = QVBoxLayout(self.frame_59)
        self.verticalLayout_85.setSpacing(5)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_59)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_85.addWidget(self.label_15)

        self.lineEdit_8 = QLineEdit(self.frame_59)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_85.addWidget(self.lineEdit_8)


        self.verticalLayout_10.addWidget(self.frame_59)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.moneroQStackedWidget.addWidget(self.moneroFromSpendPrivateKeyQStackedWidget)
        self.moneroFromWatchOnlyQStackedWidget = QWidget()
        self.moneroFromWatchOnlyQStackedWidget.setObjectName(u"moneroFromWatchOnlyQStackedWidget")
        self.verticalLayout_11 = QVBoxLayout(self.moneroFromWatchOnlyQStackedWidget)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.XPublicKeyQFrame = QFrame(self.moneroFromWatchOnlyQStackedWidget)
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

        self.frame_60 = QFrame(self.moneroFromWatchOnlyQStackedWidget)
        self.frame_60.setObjectName(u"frame_60")
        self.verticalLayout_86 = QVBoxLayout(self.frame_60)
        self.verticalLayout_86.setSpacing(5)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_60)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_86.addWidget(self.label_19)

        self.lineEdit_9 = QLineEdit(self.frame_60)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_86.addWidget(self.lineEdit_9)


        self.verticalLayout_11.addWidget(self.frame_60)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.moneroQStackedWidget.addWidget(self.moneroFromWatchOnlyQStackedWidget)
        self.moneroFromPrivateKeyQStackedWidget = QWidget()
        self.moneroFromPrivateKeyQStackedWidget.setObjectName(u"moneroFromPrivateKeyQStackedWidget")
        self.verticalLayout_13 = QVBoxLayout(self.moneroFromPrivateKeyQStackedWidget)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQFrame = QFrame(self.moneroFromPrivateKeyQStackedWidget)
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

        self.PrivateKeyQFrame_2 = QFrame(self.moneroFromPrivateKeyQStackedWidget)
        self.PrivateKeyQFrame_2.setObjectName(u"PrivateKeyQFrame_2")
        self.PrivateKeyQFrame_2.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_5 = QVBoxLayout(self.PrivateKeyQFrame_2)
        self.PrivateKeyVLayout_5.setSpacing(5)
        self.PrivateKeyVLayout_5.setObjectName(u"PrivateKeyVLayout_5")
        self.PrivateKeyVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyLabelQFrame_2 = QFrame(self.PrivateKeyQFrame_2)
        self.PrivateKeyLabelQFrame_2.setObjectName(u"PrivateKeyLabelQFrame_2")
        self.PrivateKeyLabelHLayout_5 = QHBoxLayout(self.PrivateKeyLabelQFrame_2)
        self.PrivateKeyLabelHLayout_5.setSpacing(15)
        self.PrivateKeyLabelHLayout_5.setObjectName(u"PrivateKeyLabelHLayout_5")
        self.PrivateKeyLabelHLayout_5.setContentsMargins(0, 0, 0, 0)
        self.PrivateKeyQLabel_2 = QLabel(self.PrivateKeyLabelQFrame_2)
        self.PrivateKeyQLabel_2.setObjectName(u"PrivateKeyQLabel_2")

        self.PrivateKeyLabelHLayout_5.addWidget(self.PrivateKeyQLabel_2)

        self.PrivateKeyLabelHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_5.addItem(self.PrivateKeyLabelHSpacer_2)


        self.PrivateKeyVLayout_5.addWidget(self.PrivateKeyLabelQFrame_2)

        self.PrivateKeyQLineEdit_2 = QLineEdit(self.PrivateKeyQFrame_2)
        self.PrivateKeyQLineEdit_2.setObjectName(u"PrivateKeyQLineEdit_2")

        self.PrivateKeyVLayout_5.addWidget(self.PrivateKeyQLineEdit_2)


        self.verticalLayout_13.addWidget(self.PrivateKeyQFrame_2)

        self.frame_61 = QFrame(self.moneroFromPrivateKeyQStackedWidget)
        self.frame_61.setObjectName(u"frame_61")
        self.verticalLayout_87 = QVBoxLayout(self.frame_61)
        self.verticalLayout_87.setSpacing(5)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_61)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_87.addWidget(self.label_17)

        self.lineEdit_10 = QLineEdit(self.frame_61)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_87.addWidget(self.lineEdit_10)


        self.verticalLayout_13.addWidget(self.frame_61)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.moneroQStackedWidget.addWidget(self.moneroFromPrivateKeyQStackedWidget)

        self.verticalLayout_69.addWidget(self.moneroQStackedWidget)

        self.hdQStackedWidget.addWidget(self.moneroPageQWidget)

        self.verticalLayout_3.addWidget(self.hdQStackedWidget)

        self.dumpsDerivationContainerQFrame = QFrame(self.dumpsPageEntireContainerQFrame)
        self.dumpsDerivationContainerQFrame.setObjectName(u"dumpsDerivationContainerQFrame")
        self.verticalLayout_17 = QVBoxLayout(self.dumpsDerivationContainerQFrame)
        self.verticalLayout_17.setSpacing(15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.DerivationQFrame = QFrame(self.dumpsDerivationContainerQFrame)
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


        self.verticalLayout_3.addWidget(self.dumpsDerivationContainerQFrame)

        self.dumpsFormatKeysContainerQFrame = QFrame(self.dumpsPageEntireContainerQFrame)
        self.dumpsFormatKeysContainerQFrame.setObjectName(u"dumpsFormatKeysContainerQFrame")
        self.horizontalLayout_4 = QHBoxLayout(self.dumpsFormatKeysContainerQFrame)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.dumpsFormatContainerQFrame = QFrame(self.dumpsFormatKeysContainerQFrame)
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


        self.horizontalLayout_4.addWidget(self.dumpsFormatContainerQFrame)

        self.dumpsKeysContainerQFrame = QFrame(self.dumpsFormatKeysContainerQFrame)
        self.dumpsKeysContainerQFrame.setObjectName(u"dumpsKeysContainerQFrame")
        self.horizontalLayout_18 = QHBoxLayout(self.dumpsKeysContainerQFrame)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.dumpsKeysQFrame = QFrame(self.dumpsKeysContainerQFrame)
        self.dumpsKeysQFrame.setObjectName(u"dumpsKeysQFrame")
        self.dumpsKeysQFrame.setMinimumSize(QSize(288, 0))
        self.KeysVLayout = QVBoxLayout(self.dumpsKeysQFrame)
        self.KeysVLayout.setSpacing(5)
        self.KeysVLayout.setObjectName(u"KeysVLayout")
        self.KeysVLayout.setContentsMargins(0, 0, 0, 0)
        self.dumpsKeysLabelContainerQFrame = QFrame(self.dumpsKeysQFrame)
        self.dumpsKeysLabelContainerQFrame.setObjectName(u"dumpsKeysLabelContainerQFrame")
        self.horizontalLayout_21 = QHBoxLayout(self.dumpsKeysLabelContainerQFrame)
        self.horizontalLayout_21.setSpacing(15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.dumpsKeysQLabel = QLabel(self.dumpsKeysLabelContainerQFrame)
        self.dumpsKeysQLabel.setObjectName(u"dumpsKeysQLabel")

        self.horizontalLayout_21.addWidget(self.dumpsKeysQLabel)

        self.dumpsKeysLabelContainerQFrameHSpacer = QSpacerItem(524, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.dumpsKeysLabelContainerQFrameHSpacer)


        self.KeysVLayout.addWidget(self.dumpsKeysLabelContainerQFrame)

        self.dumpsKeysLabelQFrame = QFrame(self.dumpsKeysQFrame)
        self.dumpsKeysLabelQFrame.setObjectName(u"dumpsKeysLabelQFrame")
        self.verticalLayout_18 = QVBoxLayout(self.dumpsKeysLabelQFrame)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.dumpsKeysLineEditContainerQFrame = QFrame(self.dumpsKeysLabelQFrame)
        self.dumpsKeysLineEditContainerQFrame.setObjectName(u"dumpsKeysLineEditContainerQFrame")
        self.horizontalLayout_20 = QHBoxLayout(self.dumpsKeysLineEditContainerQFrame)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.dumpsKeysQLineEdit = QLineEdit(self.dumpsKeysLineEditContainerQFrame)
        self.dumpsKeysQLineEdit.setObjectName(u"dumpsKeysQLineEdit")

        self.horizontalLayout_20.addWidget(self.dumpsKeysQLineEdit)

        self.dumpsKeysGenerateQPushButton = QPushButton(self.dumpsKeysLineEditContainerQFrame)
        self.dumpsKeysGenerateQPushButton.setObjectName(u"dumpsKeysGenerateQPushButton")
        sizePolicy1.setHeightForWidth(self.dumpsKeysGenerateQPushButton.sizePolicy().hasHeightForWidth())
        self.dumpsKeysGenerateQPushButton.setSizePolicy(sizePolicy1)
        self.dumpsKeysGenerateQPushButton.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.dumpsKeysGenerateQPushButton)


        self.verticalLayout_18.addWidget(self.dumpsKeysLineEditContainerQFrame)


        self.KeysVLayout.addWidget(self.dumpsKeysLabelQFrame)


        self.horizontalLayout_18.addWidget(self.dumpsKeysQFrame)


        self.horizontalLayout_4.addWidget(self.dumpsKeysContainerQFrame)


        self.verticalLayout_3.addWidget(self.dumpsFormatKeysContainerQFrame)


        self.verticalLayout_12.addWidget(self.dumpsPageEntireContainerQFrame)

        self.hdwalletQStackedWidget.addWidget(self.dumpsPageQStackedWidget)

        self.verticalLayout.addWidget(self.hdwalletQStackedWidget)

        self.hdWalletContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.hdWalletContainerQFrameVSpacer)

        self.hdWalletContainerQFrameVSpacerB = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.hdWalletContainerQFrameVSpacerB)


        self.horizontalLayout.addWidget(self.hdWalletContainerQFrame)

        self.outputQFrame = QFrame(self.centralwidget)
        self.outputQFrame.setObjectName(u"outputQFrame")
        self.outputQFrame.setMinimumSize(QSize(400, 0))
        self.verticalLayout_2 = QVBoxLayout(self.outputQFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.outputFrameTopContainerQFrame = QFrame(self.outputQFrame)
        self.outputFrameTopContainerQFrame.setObjectName(u"outputFrameTopContainerQFrame")
        self.outputFrameTopContainerQFrame.setMinimumSize(QSize(0, 30))
        self.outputFrameTopContainerQFrame.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_22 = QHBoxLayout(self.outputFrameTopContainerQFrame)
        self.horizontalLayout_22.setSpacing(15)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.outputFrameTopContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.outputFrameTopContainerQFrameHSpacer)

        self.expandTerminalQFrame = QFrame(self.outputFrameTopContainerQFrame)
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


        self.verticalLayout_2.addWidget(self.outputFrameTopContainerQFrame)

        self.outputTerminalQTextEdit = QTextEdit(self.outputQFrame)
        self.outputTerminalQTextEdit.setObjectName(u"outputTerminalQTextEdit")
        self.outputTerminalQTextEdit.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.outputTerminalQTextEdit.sizePolicy().hasHeightForWidth())
        self.outputTerminalQTextEdit.setSizePolicy(sizePolicy3)
        self.outputTerminalQTextEdit.setFrameShape(QFrame.NoFrame)
        self.outputTerminalQTextEdit.setFrameShadow(QFrame.Plain)
        self.outputTerminalQTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.outputTerminalQTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.outputTerminalQTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.outputTerminalQTextEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.outputTerminalQTextEdit)

        self.outputTerminalQLineEdit = QLineEdit(self.outputQFrame)
        self.outputTerminalQLineEdit.setObjectName(u"outputTerminalQLineEdit")

        self.verticalLayout_2.addWidget(self.outputTerminalQLineEdit)


        self.horizontalLayout.addWidget(self.outputQFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.hdwalletQStackedWidget.setCurrentIndex(1)
        self.hdQStackedWidget.setCurrentIndex(2)
        self.BIPQStackedWidget.setCurrentIndex(4)
        self.cardanoQStackedWidget.setCurrentIndex(4)
        self.electrumV1QStackedWidget.setCurrentIndex(0)
        self.electrumV2QStackedWidget.setCurrentIndex(2)
        self.moneroQStackedWidget.setCurrentIndex(4)
        self.DerivationsQTabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.generateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.dumpQPushButton.setText(QCoreApplication.translate("MainWindow", u"Dumps", None))
        self.donationHDWalletQPushButton.setText(QCoreApplication.translate("MainWindow", u"Donation", None))
        self.helpHDWalletQPushButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.entropyGeneratorQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy Generator", None))
        self.generateEntropyClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.generateEntropyClientQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Client", None))
        self.generateEntropyStrengthQLabel.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.generateEntropyStrengthQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Strength", None))
        self.generateEntropyClientAndStrengthQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.generateEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.generateEntropyCopyQLineEdit.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.mnemonicGeneratorQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic Generator", None))
        self.generateMnemonicClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.generateMnemonicClientQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Client", None))
        self.generateMnemonicWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.generateMnemonicWordsQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Words", None))
        self.generateMnemonicLanguageQLabel.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.generateMnemonicLanguageQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Language", None))
        self.generateMnemonicClientWordsAndLanguageQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.generateMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.generateMnemonicCopyQPushButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.passphraseGeneratorQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase Generator", None))
        self.generateLengthQLabel.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.generatePassphraseLengthQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.generatePassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.generatePassphraseCopyQPushButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
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

        self.dumpsFromQLabel.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.dumpsFromQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.dumpsFromQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.dumpsFromQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Private key", None))
        self.dumpsFromQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Public key", None))
        self.dumpsFromQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Seed", None))
        self.dumpsFromQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"WIF", None))
        self.dumpsFromQComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.dumpsFromQComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"XPublic Key", None))

        self.dumpsCryptocurrencyQLabel.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.dumpsCryptocurrencyQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Bitcoin", None))
        self.dumpsCryptocurrencyQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Qtum", None))

        self.dumpsNetworkQLabel.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.dumpsNetworkQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.dumpsNetworkQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.dumpsNetworkQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.dumpsNetworkQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.dumpsNetworkQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.dumpsNetworkQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.BIPFromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.BIPFromEntropyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromEntropyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.BIPFromEntropyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.BIPFromEntropyPublicKeyTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.BIPFromEntropyPublicKeyTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.BIPFromEntropyPublicKeyTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.BIPFromEntropyPublicKeyTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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
        self.BIPFromMnemonicPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.BIPFromMnemonicPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.BIPFromMnemonicPublicKeyTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.BIPFromMnemonicPublicKeyTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.BIPFromMnemonicPublicKeyTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.BIPFromMnemonicPublicKeyTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.BIPFromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.BIPFromMnemonicPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.BIPFromSeedsQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.BIPFromSeedPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromSeedPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.BIPFromSeedPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.BIPFromSeedPublicKeyTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.BIPFromSeedPublicKeyTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.BIPFromSeedPublicKeyTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.BIPFromSeedPublicKeyTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.BIPFromXPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.BIPFromXPrivateKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromXPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.BIPFromXPublicKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromWIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.BIPFromWIFPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromWIFBIP38PassphraseQCheckBox.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.BIPFromWIFBIP38PassphraseGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.BIPFromPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.BIPFromPrivateKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.BIPFromPublicKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.cardanoFromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.cardanoFromEntropyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"cardano Type", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromEntropyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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

        self.cardanoFromEntropyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromEntropyWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.cardanoFromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.cardanoFromMnemonicCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"cardano type", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromMnemonicCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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

        self.cardanoFromMnemonicAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromMnemonicWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.cardanoFromMnemonicWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.cardanoFromMnemonicWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.cardanoFromMnemonicWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.cardanoFromMnemonicWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.cardanoFromMnemonicWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.cardanoFromSeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.cardanoFromSeedCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"cardano type", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromSeedCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromSeedAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromSeedAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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

        self.cardanoFromXPrivateKeyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromXPrivateKeyAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromXPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.cardanoFromXPublicKeyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"cardano type", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromXPublicKeyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromXPublicKeyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromXPublicKeyAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromPrivateKeyContainerQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.cardanoFromPrivateKeyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"cardano type", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromPrivateKeyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromPrivateKeyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromPrivateKeyAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.cardanoFromPublicKeyCardanoTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"cardano type", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromPublicKeyCardanoTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromPublicKeyAddressTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromPublicKeyAddressTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.electrumV1FromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.electrumV1FromEntropyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV1FromEntropyPublicKeyTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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

        self.electrumV1FromEntropyWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.electrumV1FromEntropyWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.electrumV1FromEntropyWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.electrumV1FromEntropyWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.electrumV1FromEntropyWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.electrumV1FromEntropyWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.electrumV1FromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.electrumV1FromMnemonicPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV1FromMnemonicPublicKeyTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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

        self.electrumV1FromMnemonicWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.electrumV1FromMnemonicWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))

        self.electrumV1FromSeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.electrumV1FromSeedPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV1FromClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV1FromClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV1FromClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV1FromClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV1FromClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.electrumV1FromWIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.electrumV1FromWIFBIP38PassphraseQCheckBox.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.electrumV1FromWIFBIP38PassphraseQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.electrumV1FromWIFPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.electrumV1FromPrivateKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.electrumV1FromPublicKeyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.electrumV2FromEntropyModeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.electrumV2FromEntropyPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV2FromEntropyPublicKeyTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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

        self.electrumV2FromEntropyWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.electrumV2FromEntropyWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.electrumV2FromEntropyWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.electrumV2FromEntropyWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.electrumV2FromEntropyWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.electrumV2FromEntropyWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.electrumV2FromEntropyMnemonicTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic Type", None))
        self.electrumV2FromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.electrumV2FromMnemonicMnemonicTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic Type", None))
        self.electrumV2FromMnemonicModeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.electrumV2FromMnemonicModeQComboBox.setPlaceholderText("")
        self.electrumV2FromMnemonicPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV2FromMnemonicPublicKeyTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.electrumV2FromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.electrumV2FromMnemonicPassphraseGenerateQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.electrumV2FromSeedsQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.electrumV2FromSeedModeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.electrumV2FromSeedPublicKeyTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromSeedPublicKeyTypeQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV2FromSeedPublicKeyTypeQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV2FromSeedPublicKeyTypeQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV2FromSeedPublicKeyTypeQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV2FromSeedPublicKeyTypeQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV2FromSeedPublicKeyTypeQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.EntropyQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.EPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.EPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
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
        self.ClientQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.MPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.MPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.SeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.ClientQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.XPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Spend Private Key", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.XPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Watch Only", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.PrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"View Private key", None))
        self.PrivateKeyQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Spend Public Key", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
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
        self.dumpsFormatQLabel.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.dumpsormatQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"JSON", None))
        self.dumpsormatQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CSV", None))

        self.dumpsKeysQLabel.setText(QCoreApplication.translate("MainWindow", u"Keys", None))
        self.dumpsKeysGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

