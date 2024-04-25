# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hdwallethOYWwz.ui'
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
        MainWindow.resize(1000, 558)
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

        self.donationHDWalletQPushButton = QPushButton(self.frame_22)
        self.donationHDWalletQPushButton.setObjectName(u"donationHDWalletQPushButton")

        self.horizontalLayout_6.addWidget(self.donationHDWalletQPushButton)

        self.helpHDWalletQPushButton = QPushButton(self.frame_22)
        self.helpHDWalletQPushButton.setObjectName(u"helpHDWalletQPushButton")

        self.horizontalLayout_6.addWidget(self.helpHDWalletQPushButton)


        self.verticalLayout.addWidget(self.frame_22)

        self.tabWidget = QTabWidget(self.hdWalletContainerQFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.generateHDWalletTabQWidget = QWidget()
        self.generateHDWalletTabQWidget.setObjectName(u"generateHDWalletTabQWidget")
        self.verticalLayout_14 = QVBoxLayout(self.generateHDWalletTabQWidget)
        self.verticalLayout_14.setSpacing(15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(15, 15, 15, 15)
        self.frame_14 = QFrame(self.generateHDWalletTabQWidget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setLineWidth(0)
        self.verticalLayout_15 = QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setSpacing(15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_14)
        self.frame_25.setObjectName(u"frame_25")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_25)
        self.frame_31.setObjectName(u"frame_31")
        self.verticalLayout_51 = QVBoxLayout(self.frame_31)
        self.verticalLayout_51.setSpacing(5)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_31)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_51.addWidget(self.label_22)

        self.comboBox = QComboBox(self.frame_31)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_51.addWidget(self.comboBox)


        self.horizontalLayout_14.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_25)
        self.frame_32.setObjectName(u"frame_32")
        self.verticalLayout_52 = QVBoxLayout(self.frame_32)
        self.verticalLayout_52.setSpacing(5)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_32)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_52.addWidget(self.label_23)

        self.comboBox_2 = QComboBox(self.frame_32)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_52.addWidget(self.comboBox_2)


        self.horizontalLayout_14.addWidget(self.frame_32)

        self.pushButton = QPushButton(self.frame_25)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_14.addWidget(self.pushButton, 0, Qt.AlignBottom)


        self.verticalLayout_15.addWidget(self.frame_25)


        self.verticalLayout_14.addWidget(self.frame_14)

        self.frame_26 = QFrame(self.generateHDWalletTabQWidget)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setLineWidth(0)
        self.verticalLayout_68 = QVBoxLayout(self.frame_26)
        self.verticalLayout_68.setSpacing(5)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_26)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setLineWidth(0)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_73.setSpacing(5)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_42)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_73.addWidget(self.label_28)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_9)


        self.verticalLayout_68.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_26)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_43)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(self.frame_43)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_11.addWidget(self.pushButton_2)


        self.verticalLayout_68.addWidget(self.frame_43)


        self.verticalLayout_14.addWidget(self.frame_26)

        self.frame_17 = QFrame(self.generateHDWalletTabQWidget)
        self.frame_17.setObjectName(u"frame_17")
        self.verticalLayout_41 = QVBoxLayout(self.frame_17)
        self.verticalLayout_41.setSpacing(15)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_17)
        self.frame_27.setObjectName(u"frame_27")
        self.horizontalLayout_60 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_60.setSpacing(15)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_27)
        self.frame_34.setObjectName(u"frame_34")
        self.verticalLayout_64 = QVBoxLayout(self.frame_34)
        self.verticalLayout_64.setSpacing(5)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_34)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_64.addWidget(self.label_24)

        self.comboBox_3 = QComboBox(self.frame_34)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_64.addWidget(self.comboBox_3)


        self.horizontalLayout_60.addWidget(self.frame_34)

        self.frame_36 = QFrame(self.frame_27)
        self.frame_36.setObjectName(u"frame_36")
        self.verticalLayout_66 = QVBoxLayout(self.frame_36)
        self.verticalLayout_66.setSpacing(5)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(-1, 0, 0, 0)
        self.label_26 = QLabel(self.frame_36)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_66.addWidget(self.label_26)

        self.comboBox_5 = QComboBox(self.frame_36)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_66.addWidget(self.comboBox_5)


        self.horizontalLayout_60.addWidget(self.frame_36)

        self.frame_35 = QFrame(self.frame_27)
        self.frame_35.setObjectName(u"frame_35")
        self.verticalLayout_65 = QVBoxLayout(self.frame_35)
        self.verticalLayout_65.setSpacing(5)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_35)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_65.addWidget(self.label_25)

        self.comboBox_4 = QComboBox(self.frame_35)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_65.addWidget(self.comboBox_4)


        self.horizontalLayout_60.addWidget(self.frame_35)

        self.pushButton_3 = QPushButton(self.frame_27)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_60.addWidget(self.pushButton_3, 0, Qt.AlignBottom)


        self.verticalLayout_41.addWidget(self.frame_27)

        self.frame_44 = QFrame(self.frame_17)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_44)
        self.verticalLayout_70.setSpacing(5)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.horizontalLayout_74 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_74.setSpacing(5)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_45)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_74.addWidget(self.label_30)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_74.addItem(self.horizontalSpacer_10)


        self.verticalLayout_70.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_75.setSpacing(15)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_5 = QLineEdit(self.frame_46)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)

        self.horizontalLayout_75.addWidget(self.lineEdit_5)

        self.pushButton_9 = QPushButton(self.frame_46)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_75.addWidget(self.pushButton_9)


        self.verticalLayout_70.addWidget(self.frame_46)


        self.verticalLayout_41.addWidget(self.frame_44)


        self.verticalLayout_14.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.generateHDWalletTabQWidget)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setLineWidth(0)
        self.verticalLayout_42 = QVBoxLayout(self.frame_18)
        self.verticalLayout_42.setSpacing(15)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_18)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setEnabled(False)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_68.setSpacing(15)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(184, 16777215))
        self.frame_33.setLineWidth(0)
        self.verticalLayout_63 = QVBoxLayout(self.frame_33)
        self.verticalLayout_63.setSpacing(5)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_33)
        self.frame_39.setObjectName(u"frame_39")
        self.horizontalLayout_70 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_70.setSpacing(5)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_39)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_70.addWidget(self.label_27)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_7)


        self.verticalLayout_63.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_33)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_71.setSpacing(5)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.frame_40)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_71.addWidget(self.lineEdit_4)

        self.pushButton_8 = QPushButton(self.frame_40)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_71.addWidget(self.pushButton_8)


        self.verticalLayout_63.addWidget(self.frame_40)


        self.horizontalLayout_68.addWidget(self.frame_33)

        self.frame_29 = QFrame(self.frame_30)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setLineWidth(0)
        self.verticalLayout_67 = QVBoxLayout(self.frame_29)
        self.verticalLayout_67.setSpacing(5)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_29)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_67.setSpacing(5)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_37)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_67.addWidget(self.label_18)

        self.horizontalSpacer_6 = QSpacerItem(155, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_6)


        self.verticalLayout_67.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_29)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_69.setSpacing(15)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.frame_38)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_69.addWidget(self.lineEdit_3)

        self.pushButton_7 = QPushButton(self.frame_38)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_69.addWidget(self.pushButton_7)


        self.verticalLayout_67.addWidget(self.frame_38)


        self.horizontalLayout_68.addWidget(self.frame_29)


        self.verticalLayout_42.addWidget(self.frame_30)


        self.verticalLayout_14.addWidget(self.frame_18)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_10)

        self.tabWidget.addTab(self.generateHDWalletTabQWidget, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_12 = QVBoxLayout(self.tab)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(525, 0))
        self.frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
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

        self.cardanoFromEntropyClientContainerQFrame_2 = QFrame(self.frame_3)
        self.cardanoFromEntropyClientContainerQFrame_2.setObjectName(u"cardanoFromEntropyClientContainerQFrame_2")
        self.cardanoFromEntropyClientContainerQFrame_2.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_25 = QVBoxLayout(self.cardanoFromEntropyClientContainerQFrame_2)
        self.ClientVLayout_25.setSpacing(5)
        self.ClientVLayout_25.setObjectName(u"ClientVLayout_25")
        self.ClientVLayout_25.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyClientLabelContainerQFrame_2 = QFrame(self.cardanoFromEntropyClientContainerQFrame_2)
        self.cardanoFromEntropyClientLabelContainerQFrame_2.setObjectName(u"cardanoFromEntropyClientLabelContainerQFrame_2")
        self.MStrengthLabelHLayout_30 = QHBoxLayout(self.cardanoFromEntropyClientLabelContainerQFrame_2)
        self.MStrengthLabelHLayout_30.setSpacing(15)
        self.MStrengthLabelHLayout_30.setObjectName(u"MStrengthLabelHLayout_30")
        self.MStrengthLabelHLayout_30.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyClientQLabel_2 = QLabel(self.cardanoFromEntropyClientLabelContainerQFrame_2)
        self.cardanoFromEntropyClientQLabel_2.setObjectName(u"cardanoFromEntropyClientQLabel_2")

        self.MStrengthLabelHLayout_30.addWidget(self.cardanoFromEntropyClientQLabel_2)

        self.cardanoFromEntropyClientLabelContainerQFrameHSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_30.addItem(self.cardanoFromEntropyClientLabelContainerQFrameHSpacer_2)


        self.ClientVLayout_25.addWidget(self.cardanoFromEntropyClientLabelContainerQFrame_2)

        self.cardanoFromEntropyClientQComboBox_2 = QComboBox(self.cardanoFromEntropyClientContainerQFrame_2)
        self.cardanoFromEntropyClientQComboBox_2.addItem("")
        self.cardanoFromEntropyClientQComboBox_2.addItem("")
        self.cardanoFromEntropyClientQComboBox_2.addItem("")
        self.cardanoFromEntropyClientQComboBox_2.addItem("")
        self.cardanoFromEntropyClientQComboBox_2.addItem("")
        self.cardanoFromEntropyClientQComboBox_2.addItem("")
        self.cardanoFromEntropyClientQComboBox_2.setObjectName(u"cardanoFromEntropyClientQComboBox_2")

        self.ClientVLayout_25.addWidget(self.cardanoFromEntropyClientQComboBox_2)


        self.horizontalLayout_2.addWidget(self.cardanoFromEntropyClientContainerQFrame_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.hdQStackedWidget = QStackedWidget(self.frame)
        self.hdQStackedWidget.setObjectName(u"hdQStackedWidget")
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

        self.BIPFromEntropyClientAndPassphraseQFrame = QFrame(self.BIPFromEntropyQStackedWidget)
        self.BIPFromEntropyClientAndPassphraseQFrame.setObjectName(u"BIPFromEntropyClientAndPassphraseQFrame")
        self.horizontalLayout_24 = QHBoxLayout(self.BIPFromEntropyClientAndPassphraseQFrame)
        self.horizontalLayout_24.setSpacing(15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyClientContainerQFrame = QFrame(self.BIPFromEntropyClientAndPassphraseQFrame)
        self.BIPFromEntropyClientContainerQFrame.setObjectName(u"BIPFromEntropyClientContainerQFrame")
        self.BIPFromEntropyClientContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_4 = QVBoxLayout(self.BIPFromEntropyClientContainerQFrame)
        self.ClientVLayout_4.setSpacing(5)
        self.ClientVLayout_4.setObjectName(u"ClientVLayout_4")
        self.ClientVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyClientLabelContainerQFrame = QFrame(self.BIPFromEntropyClientContainerQFrame)
        self.BIPFromEntropyClientLabelContainerQFrame.setObjectName(u"BIPFromEntropyClientLabelContainerQFrame")
        self.MStrengthLabelHLayout_6 = QHBoxLayout(self.BIPFromEntropyClientLabelContainerQFrame)
        self.MStrengthLabelHLayout_6.setSpacing(15)
        self.MStrengthLabelHLayout_6.setObjectName(u"MStrengthLabelHLayout_6")
        self.MStrengthLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyClientQLabel = QLabel(self.BIPFromEntropyClientLabelContainerQFrame)
        self.BIPFromEntropyClientQLabel.setObjectName(u"BIPFromEntropyClientQLabel")

        self.MStrengthLabelHLayout_6.addWidget(self.BIPFromEntropyClientQLabel)

        self.BIPFromEntropyClientLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_6.addItem(self.BIPFromEntropyClientLabelContainerQFrameHSpacer)


        self.ClientVLayout_4.addWidget(self.BIPFromEntropyClientLabelContainerQFrame)

        self.BIPFromEntropyClientQComboBox = QComboBox(self.BIPFromEntropyClientContainerQFrame)
        self.BIPFromEntropyClientQComboBox.addItem("")
        self.BIPFromEntropyClientQComboBox.addItem("")
        self.BIPFromEntropyClientQComboBox.addItem("")
        self.BIPFromEntropyClientQComboBox.addItem("")
        self.BIPFromEntropyClientQComboBox.addItem("")
        self.BIPFromEntropyClientQComboBox.addItem("")
        self.BIPFromEntropyClientQComboBox.setObjectName(u"BIPFromEntropyClientQComboBox")

        self.ClientVLayout_4.addWidget(self.BIPFromEntropyClientQComboBox)


        self.horizontalLayout_24.addWidget(self.BIPFromEntropyClientContainerQFrame)

        self.BIPFromEntropyPassphraseContainerQFrame = QFrame(self.BIPFromEntropyClientAndPassphraseQFrame)
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


        self.verticalLayout_22.addWidget(self.BIPFromEntropyClientAndPassphraseQFrame)

        self.BIPFromEntropyLanguageAndWordsQFrame = QFrame(self.BIPFromEntropyQStackedWidget)
        self.BIPFromEntropyLanguageAndWordsQFrame.setObjectName(u"BIPFromEntropyLanguageAndWordsQFrame")
        self.horizontalLayout_26 = QHBoxLayout(self.BIPFromEntropyLanguageAndWordsQFrame)
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.BIPFromEntropyLanguageContainerQFrame = QFrame(self.BIPFromEntropyLanguageAndWordsQFrame)
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

        self.BIPFromEntropyWordsContainerQFrame = QFrame(self.BIPFromEntropyLanguageAndWordsQFrame)
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


        self.verticalLayout_22.addWidget(self.BIPFromEntropyLanguageAndWordsQFrame)

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

        self.BIPFromMnemonicClientAndPassphraseQFrame = QFrame(self.BIPFromMnemonicQStackedWidget)
        self.BIPFromMnemonicClientAndPassphraseQFrame.setObjectName(u"BIPFromMnemonicClientAndPassphraseQFrame")
        self.horizontalLayout_28 = QHBoxLayout(self.BIPFromMnemonicClientAndPassphraseQFrame)
        self.horizontalLayout_28.setSpacing(15)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicClientContainerQFrame = QFrame(self.BIPFromMnemonicClientAndPassphraseQFrame)
        self.BIPFromMnemonicClientContainerQFrame.setObjectName(u"BIPFromMnemonicClientContainerQFrame")
        self.BIPFromMnemonicClientContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_5 = QVBoxLayout(self.BIPFromMnemonicClientContainerQFrame)
        self.ClientVLayout_5.setSpacing(5)
        self.ClientVLayout_5.setObjectName(u"ClientVLayout_5")
        self.ClientVLayout_5.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicClientLabelContainerQFrame = QFrame(self.BIPFromMnemonicClientContainerQFrame)
        self.BIPFromMnemonicClientLabelContainerQFrame.setObjectName(u"BIPFromMnemonicClientLabelContainerQFrame")
        self.MStrengthLabelHLayout_7 = QHBoxLayout(self.BIPFromMnemonicClientLabelContainerQFrame)
        self.MStrengthLabelHLayout_7.setSpacing(15)
        self.MStrengthLabelHLayout_7.setObjectName(u"MStrengthLabelHLayout_7")
        self.MStrengthLabelHLayout_7.setContentsMargins(0, 0, 0, 0)
        self.BIPFromMnemonicClientQLabel = QLabel(self.BIPFromMnemonicClientLabelContainerQFrame)
        self.BIPFromMnemonicClientQLabel.setObjectName(u"BIPFromMnemonicClientQLabel")

        self.MStrengthLabelHLayout_7.addWidget(self.BIPFromMnemonicClientQLabel)

        self.BIPFromMnemonicClientLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_7.addItem(self.BIPFromMnemonicClientLabelContainerQFrameHSpacer)


        self.ClientVLayout_5.addWidget(self.BIPFromMnemonicClientLabelContainerQFrame)

        self.BIPFromMnemonicClientQComboBox = QComboBox(self.BIPFromMnemonicClientContainerQFrame)
        self.BIPFromMnemonicClientQComboBox.addItem("")
        self.BIPFromMnemonicClientQComboBox.addItem("")
        self.BIPFromMnemonicClientQComboBox.addItem("")
        self.BIPFromMnemonicClientQComboBox.addItem("")
        self.BIPFromMnemonicClientQComboBox.addItem("")
        self.BIPFromMnemonicClientQComboBox.addItem("")
        self.BIPFromMnemonicClientQComboBox.setObjectName(u"BIPFromMnemonicClientQComboBox")

        self.ClientVLayout_5.addWidget(self.BIPFromMnemonicClientQComboBox)


        self.horizontalLayout_28.addWidget(self.BIPFromMnemonicClientContainerQFrame)

        self.BIPFromMnemonicPassphraseContainerQFrame = QFrame(self.BIPFromMnemonicClientAndPassphraseQFrame)
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


        self.verticalLayout_24.addWidget(self.BIPFromMnemonicClientAndPassphraseQFrame)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_5)

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
        self.BIPFromSeedAndClientContainerQFrame = QFrame(self.BIPFromSeedContainerQFrame)
        self.BIPFromSeedAndClientContainerQFrame.setObjectName(u"BIPFromSeedAndClientContainerQFrame")
        self.horizontalLayout_31 = QHBoxLayout(self.BIPFromSeedAndClientContainerQFrame)
        self.horizontalLayout_31.setSpacing(15)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.BIPFromSeedsContainerQFrame = QFrame(self.BIPFromSeedAndClientContainerQFrame)
        self.BIPFromSeedsContainerQFrame.setObjectName(u"BIPFromSeedsContainerQFrame")
        self.BIPFromSeedsContainerQFrame.setFrameShape(QFrame.StyledPanel)
        self.BIPFromSeedsContainerQFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.BIPFromSeedsContainerQFrame)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.SeedLabelQFrame_2 = QFrame(self.BIPFromSeedsContainerQFrame)
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

        self.SeedQLineEdit_2 = QLineEdit(self.BIPFromSeedsContainerQFrame)
        self.SeedQLineEdit_2.setObjectName(u"SeedQLineEdit_2")

        self.verticalLayout_26.addWidget(self.SeedQLineEdit_2)


        self.horizontalLayout_31.addWidget(self.BIPFromSeedsContainerQFrame)

        self.BIPFromSeedClientContainerQFrame = QFrame(self.BIPFromSeedAndClientContainerQFrame)
        self.BIPFromSeedClientContainerQFrame.setObjectName(u"BIPFromSeedClientContainerQFrame")
        self.BIPFromSeedClientContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_6 = QVBoxLayout(self.BIPFromSeedClientContainerQFrame)
        self.ClientVLayout_6.setSpacing(5)
        self.ClientVLayout_6.setObjectName(u"ClientVLayout_6")
        self.ClientVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_6 = QFrame(self.BIPFromSeedClientContainerQFrame)
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

        self.ClientQComboBox_6 = QComboBox(self.BIPFromSeedClientContainerQFrame)
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.addItem("")
        self.ClientQComboBox_6.setObjectName(u"ClientQComboBox_6")

        self.ClientVLayout_6.addWidget(self.ClientQComboBox_6)


        self.horizontalLayout_31.addWidget(self.BIPFromSeedClientContainerQFrame)


        self.SeedVLayout_2.addWidget(self.BIPFromSeedAndClientContainerQFrame)

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
        self.frame_53 = QFrame(self.BIPFromXPrivateKeyQStackedWidget)
        self.frame_53.setObjectName(u"frame_53")
        self.horizontalLayout_90 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_90.setSpacing(15)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyContainerQFrame_3 = QFrame(self.frame_53)
        self.BIPFromPrivateKeyContainerQFrame_3.setObjectName(u"BIPFromPrivateKeyContainerQFrame_3")
        self.BIPFromPrivateKeyContainerQFrame_3.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_7 = QVBoxLayout(self.BIPFromPrivateKeyContainerQFrame_3)
        self.PrivateKeyVLayout_7.setSpacing(5)
        self.PrivateKeyVLayout_7.setObjectName(u"PrivateKeyVLayout_7")
        self.PrivateKeyVLayout_7.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyLabelContainerQFrame_3 = QFrame(self.BIPFromPrivateKeyContainerQFrame_3)
        self.BIPFromPrivateKeyLabelContainerQFrame_3.setObjectName(u"BIPFromPrivateKeyLabelContainerQFrame_3")
        self.PrivateKeyLabelHLayout_7 = QHBoxLayout(self.BIPFromPrivateKeyLabelContainerQFrame_3)
        self.PrivateKeyLabelHLayout_7.setSpacing(15)
        self.PrivateKeyLabelHLayout_7.setObjectName(u"PrivateKeyLabelHLayout_7")
        self.PrivateKeyLabelHLayout_7.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyQLabel_3 = QLabel(self.BIPFromPrivateKeyLabelContainerQFrame_3)
        self.BIPFromPrivateKeyQLabel_3.setObjectName(u"BIPFromPrivateKeyQLabel_3")

        self.PrivateKeyLabelHLayout_7.addWidget(self.BIPFromPrivateKeyQLabel_3)

        self.BIPFromPrivateKeyLabelContainerQFrameHSpacer_3 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_7.addItem(self.BIPFromPrivateKeyLabelContainerQFrameHSpacer_3)


        self.PrivateKeyVLayout_7.addWidget(self.BIPFromPrivateKeyLabelContainerQFrame_3)

        self.BIPFromPrivateKeyQLineEdit_3 = QLineEdit(self.BIPFromPrivateKeyContainerQFrame_3)
        self.BIPFromPrivateKeyQLineEdit_3.setObjectName(u"BIPFromPrivateKeyQLineEdit_3")

        self.PrivateKeyVLayout_7.addWidget(self.BIPFromPrivateKeyQLineEdit_3)


        self.horizontalLayout_90.addWidget(self.BIPFromPrivateKeyContainerQFrame_3)

        self.frame_82 = QFrame(self.frame_53)
        self.frame_82.setObjectName(u"frame_82")
        self.verticalLayout_92 = QVBoxLayout(self.frame_82)
        self.verticalLayout_92.setSpacing(5)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_91.setSpacing(15)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_83)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_91.addWidget(self.label_42)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_20)


        self.verticalLayout_92.addWidget(self.frame_83)

        self.comboBox_23 = QComboBox(self.frame_82)
        self.comboBox_23.setObjectName(u"comboBox_23")

        self.verticalLayout_92.addWidget(self.comboBox_23)


        self.horizontalLayout_90.addWidget(self.frame_82)


        self.verticalLayout_27.addWidget(self.frame_53)

        self.BIPFromXPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.BIPFromXPrivateKeyQStackedWidgetVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromXPrivateKeyQStackedWidget)
        self.BIPFromXPublicKeyQStackedWidget = QWidget()
        self.BIPFromXPublicKeyQStackedWidget.setObjectName(u"BIPFromXPublicKeyQStackedWidget")
        self.verticalLayout_28 = QVBoxLayout(self.BIPFromXPublicKeyQStackedWidget)
        self.verticalLayout_28.setSpacing(15)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.BIPFromXPublicKeyQStackedWidget)
        self.frame_51.setObjectName(u"frame_51")
        self.horizontalLayout_82 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_82.setSpacing(15)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.BIPFromXPublicKeyContainerQFrame = QFrame(self.frame_51)
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

        self.frame_73 = QFrame(self.frame_51)
        self.frame_73.setObjectName(u"frame_73")
        self.verticalLayout_77 = QVBoxLayout(self.frame_73)
        self.verticalLayout_77.setSpacing(5)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_83.setSpacing(15)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_74)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_83.addWidget(self.label_31)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_16)


        self.verticalLayout_77.addWidget(self.frame_74)

        self.comboBox_12 = QComboBox(self.frame_73)
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.verticalLayout_77.addWidget(self.comboBox_12)


        self.horizontalLayout_82.addWidget(self.frame_73)


        self.verticalLayout_28.addWidget(self.frame_51)

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

        self.frame_50 = QFrame(self.BIPFromWIFQStackedWidget)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_32.setSpacing(15)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.BIPFromWIFBIP38PassphraseContainerQFrame = QFrame(self.frame_50)
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

        self.frame_75 = QFrame(self.frame_50)
        self.frame_75.setObjectName(u"frame_75")
        self.verticalLayout_76 = QVBoxLayout(self.frame_75)
        self.verticalLayout_76.setSpacing(5)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.frame_76 = QFrame(self.frame_75)
        self.frame_76.setObjectName(u"frame_76")
        self.horizontalLayout_84 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_84.setSpacing(15)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_76)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_84.addWidget(self.label_29)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_17)


        self.verticalLayout_76.addWidget(self.frame_76)

        self.comboBox_11 = QComboBox(self.frame_75)
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.verticalLayout_76.addWidget(self.comboBox_11)


        self.horizontalLayout_32.addWidget(self.frame_75)


        self.verticalLayout_29.addWidget(self.frame_50)

        self.BIPFromWIFQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.BIPFromWIFQStackedWidgetVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromWIFQStackedWidget)
        self.BIPFromPrivateKeyQStackedWidget = QWidget()
        self.BIPFromPrivateKeyQStackedWidget.setObjectName(u"BIPFromPrivateKeyQStackedWidget")
        self.verticalLayout_31 = QVBoxLayout(self.BIPFromPrivateKeyQStackedWidget)
        self.verticalLayout_31.setSpacing(15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.BIPFromPrivateKeyQStackedWidget)
        self.frame_54.setObjectName(u"frame_54")
        self.horizontalLayout_86 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_86.setSpacing(15)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyContainerQFrame = QFrame(self.frame_54)
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

        self.frame_77 = QFrame(self.frame_54)
        self.frame_77.setObjectName(u"frame_77")
        self.verticalLayout_80 = QVBoxLayout(self.frame_77)
        self.verticalLayout_80.setSpacing(5)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.frame_78 = QFrame(self.frame_77)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_87.setSpacing(15)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_78)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_87.addWidget(self.label_34)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer_18)


        self.verticalLayout_80.addWidget(self.frame_78)

        self.comboBox_15 = QComboBox(self.frame_77)
        self.comboBox_15.setObjectName(u"comboBox_15")

        self.verticalLayout_80.addWidget(self.comboBox_15)


        self.horizontalLayout_86.addWidget(self.frame_77)


        self.verticalLayout_31.addWidget(self.frame_54)

        self.BIPFromPrivateKeyContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.BIPFromPrivateKeyContainerQFrameVSpacer)

        self.BIPQStackedWidget.addWidget(self.BIPFromPrivateKeyQStackedWidget)
        self.BIPFromPublicKeyQStackedWidget = QWidget()
        self.BIPFromPublicKeyQStackedWidget.setObjectName(u"BIPFromPublicKeyQStackedWidget")
        self.verticalLayout_32 = QVBoxLayout(self.BIPFromPublicKeyQStackedWidget)
        self.verticalLayout_32.setSpacing(15)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_79 = QFrame(self.BIPFromPublicKeyQStackedWidget)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_88.setSpacing(15)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyContainerQFrame_2 = QFrame(self.frame_79)
        self.BIPFromPrivateKeyContainerQFrame_2.setObjectName(u"BIPFromPrivateKeyContainerQFrame_2")
        self.BIPFromPrivateKeyContainerQFrame_2.setMinimumSize(QSize(400, 0))
        self.PrivateKeyVLayout_6 = QVBoxLayout(self.BIPFromPrivateKeyContainerQFrame_2)
        self.PrivateKeyVLayout_6.setSpacing(5)
        self.PrivateKeyVLayout_6.setObjectName(u"PrivateKeyVLayout_6")
        self.PrivateKeyVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyLabelContainerQFrame_2 = QFrame(self.BIPFromPrivateKeyContainerQFrame_2)
        self.BIPFromPrivateKeyLabelContainerQFrame_2.setObjectName(u"BIPFromPrivateKeyLabelContainerQFrame_2")
        self.PrivateKeyLabelHLayout_6 = QHBoxLayout(self.BIPFromPrivateKeyLabelContainerQFrame_2)
        self.PrivateKeyLabelHLayout_6.setSpacing(15)
        self.PrivateKeyLabelHLayout_6.setObjectName(u"PrivateKeyLabelHLayout_6")
        self.PrivateKeyLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.BIPFromPrivateKeyQLabel_2 = QLabel(self.BIPFromPrivateKeyLabelContainerQFrame_2)
        self.BIPFromPrivateKeyQLabel_2.setObjectName(u"BIPFromPrivateKeyQLabel_2")

        self.PrivateKeyLabelHLayout_6.addWidget(self.BIPFromPrivateKeyQLabel_2)

        self.BIPFromPrivateKeyLabelContainerQFrameHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.PrivateKeyLabelHLayout_6.addItem(self.BIPFromPrivateKeyLabelContainerQFrameHSpacer_2)


        self.PrivateKeyVLayout_6.addWidget(self.BIPFromPrivateKeyLabelContainerQFrame_2)

        self.BIPFromPrivateKeyQLineEdit_2 = QLineEdit(self.BIPFromPrivateKeyContainerQFrame_2)
        self.BIPFromPrivateKeyQLineEdit_2.setObjectName(u"BIPFromPrivateKeyQLineEdit_2")

        self.PrivateKeyVLayout_6.addWidget(self.BIPFromPrivateKeyQLineEdit_2)


        self.horizontalLayout_88.addWidget(self.BIPFromPrivateKeyContainerQFrame_2)

        self.frame_80 = QFrame(self.frame_79)
        self.frame_80.setObjectName(u"frame_80")
        self.verticalLayout_82 = QVBoxLayout(self.frame_80)
        self.verticalLayout_82.setSpacing(5)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.frame_81 = QFrame(self.frame_80)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_89.setSpacing(15)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_81)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_89.addWidget(self.label_41)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_89.addItem(self.horizontalSpacer_19)


        self.verticalLayout_82.addWidget(self.frame_81)

        self.comboBox_22 = QComboBox(self.frame_80)
        self.comboBox_22.setObjectName(u"comboBox_22")

        self.verticalLayout_82.addWidget(self.comboBox_22)


        self.horizontalLayout_88.addWidget(self.frame_80)


        self.verticalLayout_32.addWidget(self.frame_79)

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

        self.cardanoFromEntropyClientAndPassphraseContainerQFrame = QFrame(self.cardanoFromEntropyQStackedWidget)
        self.cardanoFromEntropyClientAndPassphraseContainerQFrame.setObjectName(u"cardanoFromEntropyClientAndPassphraseContainerQFrame")
        self.horizontalLayout_34 = QHBoxLayout(self.cardanoFromEntropyClientAndPassphraseContainerQFrame)
        self.horizontalLayout_34.setSpacing(15)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyClientContainerQFrame = QFrame(self.cardanoFromEntropyClientAndPassphraseContainerQFrame)
        self.cardanoFromEntropyClientContainerQFrame.setObjectName(u"cardanoFromEntropyClientContainerQFrame")
        self.cardanoFromEntropyClientContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_7 = QVBoxLayout(self.cardanoFromEntropyClientContainerQFrame)
        self.ClientVLayout_7.setSpacing(5)
        self.ClientVLayout_7.setObjectName(u"ClientVLayout_7")
        self.ClientVLayout_7.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyClientLabelContainerQFrame = QFrame(self.cardanoFromEntropyClientContainerQFrame)
        self.cardanoFromEntropyClientLabelContainerQFrame.setObjectName(u"cardanoFromEntropyClientLabelContainerQFrame")
        self.MStrengthLabelHLayout_9 = QHBoxLayout(self.cardanoFromEntropyClientLabelContainerQFrame)
        self.MStrengthLabelHLayout_9.setSpacing(15)
        self.MStrengthLabelHLayout_9.setObjectName(u"MStrengthLabelHLayout_9")
        self.MStrengthLabelHLayout_9.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyClientQLabel = QLabel(self.cardanoFromEntropyClientLabelContainerQFrame)
        self.cardanoFromEntropyClientQLabel.setObjectName(u"cardanoFromEntropyClientQLabel")

        self.MStrengthLabelHLayout_9.addWidget(self.cardanoFromEntropyClientQLabel)

        self.cardanoFromEntropyClientLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_9.addItem(self.cardanoFromEntropyClientLabelContainerQFrameHSpacer)


        self.ClientVLayout_7.addWidget(self.cardanoFromEntropyClientLabelContainerQFrame)

        self.cardanoFromEntropyClientQComboBox = QComboBox(self.cardanoFromEntropyClientContainerQFrame)
        self.cardanoFromEntropyClientQComboBox.addItem("")
        self.cardanoFromEntropyClientQComboBox.addItem("")
        self.cardanoFromEntropyClientQComboBox.addItem("")
        self.cardanoFromEntropyClientQComboBox.addItem("")
        self.cardanoFromEntropyClientQComboBox.addItem("")
        self.cardanoFromEntropyClientQComboBox.addItem("")
        self.cardanoFromEntropyClientQComboBox.setObjectName(u"cardanoFromEntropyClientQComboBox")

        self.ClientVLayout_7.addWidget(self.cardanoFromEntropyClientQComboBox)


        self.horizontalLayout_34.addWidget(self.cardanoFromEntropyClientContainerQFrame)

        self.cardanoFromEntropyPassphraseContainerQFrame = QFrame(self.cardanoFromEntropyClientAndPassphraseContainerQFrame)
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


        self.verticalLayout_34.addWidget(self.cardanoFromEntropyClientAndPassphraseContainerQFrame)

        self.cardanoFromEntropyLanguageAndWordsContainerQFrame = QFrame(self.cardanoFromEntropyQStackedWidget)
        self.cardanoFromEntropyLanguageAndWordsContainerQFrame.setObjectName(u"cardanoFromEntropyLanguageAndWordsContainerQFrame")
        self.horizontalLayout_36 = QHBoxLayout(self.cardanoFromEntropyLanguageAndWordsContainerQFrame)
        self.horizontalLayout_36.setSpacing(15)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyLanguageContainerQFrame = QFrame(self.cardanoFromEntropyLanguageAndWordsContainerQFrame)
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

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout_3.addItem(self.horizontalSpacer_24)


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

        self.frame_63 = QFrame(self.cardanoFromEntropyLanguageAndWordsContainerQFrame)
        self.frame_63.setObjectName(u"frame_63")
        self.verticalLayout_89 = QVBoxLayout(self.frame_63)
        self.verticalLayout_89.setSpacing(5)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_87 = QFrame(self.frame_63)
        self.frame_87.setObjectName(u"frame_87")
        self.horizontalLayout_96 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_96.setSpacing(15)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_87)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_96.addWidget(self.label_39)

        self.horizontalSpacer_25 = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_25)


        self.verticalLayout_89.addWidget(self.frame_87)

        self.comboBox_20 = QComboBox(self.frame_63)
        self.comboBox_20.setObjectName(u"comboBox_20")

        self.verticalLayout_89.addWidget(self.comboBox_20)


        self.horizontalLayout_36.addWidget(self.frame_63)

        self.cardanoFromEntropyWordsContainerQFrame = QFrame(self.cardanoFromEntropyLanguageAndWordsContainerQFrame)
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

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout_3.addItem(self.horizontalSpacer_26)


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


        self.verticalLayout_34.addWidget(self.cardanoFromEntropyLanguageAndWordsContainerQFrame)

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
        self.cardanoFromMnemonicClientContainerQFrame = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame)
        self.cardanoFromMnemonicClientContainerQFrame.setObjectName(u"cardanoFromMnemonicClientContainerQFrame")
        self.cardanoFromMnemonicClientContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_8 = QVBoxLayout(self.cardanoFromMnemonicClientContainerQFrame)
        self.ClientVLayout_8.setSpacing(5)
        self.ClientVLayout_8.setObjectName(u"ClientVLayout_8")
        self.ClientVLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_8 = QFrame(self.cardanoFromMnemonicClientContainerQFrame)
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

        self.ClientQComboBox_8 = QComboBox(self.cardanoFromMnemonicClientContainerQFrame)
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.addItem("")
        self.ClientQComboBox_8.setObjectName(u"ClientQComboBox_8")

        self.ClientVLayout_8.addWidget(self.ClientQComboBox_8)


        self.horizontalLayout_38.addWidget(self.cardanoFromMnemonicClientContainerQFrame)

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

        self.cardanoFromEntropyLanguageAndWordsContainerQFrame_2 = QFrame(self.cardanoFromMnemonicQStackedWidget)
        self.cardanoFromEntropyLanguageAndWordsContainerQFrame_2.setObjectName(u"cardanoFromEntropyLanguageAndWordsContainerQFrame_2")
        self.horizontalLayout_40 = QHBoxLayout(self.cardanoFromEntropyLanguageAndWordsContainerQFrame_2)
        self.horizontalLayout_40.setSpacing(15)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyLanguageContainerQFrame_2 = QFrame(self.cardanoFromEntropyLanguageAndWordsContainerQFrame_2)
        self.cardanoFromEntropyLanguageContainerQFrame_2.setObjectName(u"cardanoFromEntropyLanguageContainerQFrame_2")
        self.ELanguageVLayout_6 = QVBoxLayout(self.cardanoFromEntropyLanguageContainerQFrame_2)
        self.ELanguageVLayout_6.setSpacing(5)
        self.ELanguageVLayout_6.setObjectName(u"ELanguageVLayout_6")
        self.ELanguageVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyLanguageLabelContainerQFrame_2 = QFrame(self.cardanoFromEntropyLanguageContainerQFrame_2)
        self.cardanoFromEntropyLanguageLabelContainerQFrame_2.setObjectName(u"cardanoFromEntropyLanguageLabelContainerQFrame_2")
        self.ELanguageLabelHLayout_6 = QHBoxLayout(self.cardanoFromEntropyLanguageLabelContainerQFrame_2)
        self.ELanguageLabelHLayout_6.setSpacing(15)
        self.ELanguageLabelHLayout_6.setObjectName(u"ELanguageLabelHLayout_6")
        self.ELanguageLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyLanguageQLabel_2 = QLabel(self.cardanoFromEntropyLanguageLabelContainerQFrame_2)
        self.cardanoFromEntropyLanguageQLabel_2.setObjectName(u"cardanoFromEntropyLanguageQLabel_2")

        self.ELanguageLabelHLayout_6.addWidget(self.cardanoFromEntropyLanguageQLabel_2)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ELanguageLabelHLayout_6.addItem(self.horizontalSpacer_27)


        self.ELanguageVLayout_6.addWidget(self.cardanoFromEntropyLanguageLabelContainerQFrame_2)

        self.cardanoFromEntropyLanguageQComboBox_2 = QComboBox(self.cardanoFromEntropyLanguageContainerQFrame_2)
        self.cardanoFromEntropyLanguageQComboBox_2.addItem("")
        self.cardanoFromEntropyLanguageQComboBox_2.addItem("")
        self.cardanoFromEntropyLanguageQComboBox_2.addItem("")
        self.cardanoFromEntropyLanguageQComboBox_2.addItem("")
        self.cardanoFromEntropyLanguageQComboBox_2.addItem("")
        self.cardanoFromEntropyLanguageQComboBox_2.addItem("")
        self.cardanoFromEntropyLanguageQComboBox_2.addItem("")
        self.cardanoFromEntropyLanguageQComboBox_2.addItem("")
        self.cardanoFromEntropyLanguageQComboBox_2.setObjectName(u"cardanoFromEntropyLanguageQComboBox_2")

        self.ELanguageVLayout_6.addWidget(self.cardanoFromEntropyLanguageQComboBox_2)


        self.horizontalLayout_40.addWidget(self.cardanoFromEntropyLanguageContainerQFrame_2)

        self.frame_88 = QFrame(self.cardanoFromEntropyLanguageAndWordsContainerQFrame_2)
        self.frame_88.setObjectName(u"frame_88")
        self.verticalLayout_93 = QVBoxLayout(self.frame_88)
        self.verticalLayout_93.setSpacing(5)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_89 = QFrame(self.frame_88)
        self.frame_89.setObjectName(u"frame_89")
        self.horizontalLayout_97 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_97.setSpacing(15)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_89)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_97.addWidget(self.label_43)

        self.horizontalSpacer_28 = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_28)


        self.verticalLayout_93.addWidget(self.frame_89)

        self.comboBox_24 = QComboBox(self.frame_88)
        self.comboBox_24.setObjectName(u"comboBox_24")

        self.verticalLayout_93.addWidget(self.comboBox_24)


        self.horizontalLayout_40.addWidget(self.frame_88)

        self.cardanoFromEntropyWordsContainerQFrame_2 = QFrame(self.cardanoFromEntropyLanguageAndWordsContainerQFrame_2)
        self.cardanoFromEntropyWordsContainerQFrame_2.setObjectName(u"cardanoFromEntropyWordsContainerQFrame_2")
        self.EStrengthVLayout_6 = QVBoxLayout(self.cardanoFromEntropyWordsContainerQFrame_2)
        self.EStrengthVLayout_6.setSpacing(5)
        self.EStrengthVLayout_6.setObjectName(u"EStrengthVLayout_6")
        self.EStrengthVLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyWordsLabelContainerQFrame_2 = QFrame(self.cardanoFromEntropyWordsContainerQFrame_2)
        self.cardanoFromEntropyWordsLabelContainerQFrame_2.setObjectName(u"cardanoFromEntropyWordsLabelContainerQFrame_2")
        self.EStrengthLabelHLayout_6 = QHBoxLayout(self.cardanoFromEntropyWordsLabelContainerQFrame_2)
        self.EStrengthLabelHLayout_6.setSpacing(15)
        self.EStrengthLabelHLayout_6.setObjectName(u"EStrengthLabelHLayout_6")
        self.EStrengthLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromEntropyWordsQLabel_2 = QLabel(self.cardanoFromEntropyWordsLabelContainerQFrame_2)
        self.cardanoFromEntropyWordsQLabel_2.setObjectName(u"cardanoFromEntropyWordsQLabel_2")

        self.EStrengthLabelHLayout_6.addWidget(self.cardanoFromEntropyWordsQLabel_2)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.EStrengthLabelHLayout_6.addItem(self.horizontalSpacer_29)


        self.EStrengthVLayout_6.addWidget(self.cardanoFromEntropyWordsLabelContainerQFrame_2)

        self.cardanoFromEntropyWordsQComboBox_2 = QComboBox(self.cardanoFromEntropyWordsContainerQFrame_2)
        self.cardanoFromEntropyWordsQComboBox_2.addItem("")
        self.cardanoFromEntropyWordsQComboBox_2.addItem("")
        self.cardanoFromEntropyWordsQComboBox_2.addItem("")
        self.cardanoFromEntropyWordsQComboBox_2.addItem("")
        self.cardanoFromEntropyWordsQComboBox_2.addItem("")
        self.cardanoFromEntropyWordsQComboBox_2.setObjectName(u"cardanoFromEntropyWordsQComboBox_2")

        self.EStrengthVLayout_6.addWidget(self.cardanoFromEntropyWordsQComboBox_2)


        self.horizontalLayout_40.addWidget(self.cardanoFromEntropyWordsContainerQFrame_2)


        self.verticalLayout_36.addWidget(self.cardanoFromEntropyLanguageAndWordsContainerQFrame_2)

        self.cardanoQStackedWidget.addWidget(self.cardanoFromMnemonicQStackedWidget)
        self.cardanoFromSeedQStackedWidget = QWidget()
        self.cardanoFromSeedQStackedWidget.setObjectName(u"cardanoFromSeedQStackedWidget")
        self.verticalLayout_37 = QVBoxLayout(self.cardanoFromSeedQStackedWidget)
        self.verticalLayout_37.setSpacing(15)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedClientContainerQFrame = QFrame(self.cardanoFromSeedQStackedWidget)
        self.cardanoFromSeedClientContainerQFrame.setObjectName(u"cardanoFromSeedClientContainerQFrame")
        self.cardanoFromSeedClientContainerQFrame.setMinimumSize(QSize(400, 0))
        self.SeedVLayout_3 = QVBoxLayout(self.cardanoFromSeedClientContainerQFrame)
        self.SeedVLayout_3.setSpacing(5)
        self.SeedVLayout_3.setObjectName(u"SeedVLayout_3")
        self.SeedVLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedAndClientContainerQFrame = QFrame(self.cardanoFromSeedClientContainerQFrame)
        self.cardanoFromSeedAndClientContainerQFrame.setObjectName(u"cardanoFromSeedAndClientContainerQFrame")
        self.horizontalLayout_41 = QHBoxLayout(self.cardanoFromSeedAndClientContainerQFrame)
        self.horizontalLayout_41.setSpacing(15)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromSeedContainerQFrame = QFrame(self.cardanoFromSeedAndClientContainerQFrame)
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


        self.horizontalLayout_41.addWidget(self.cardanoFromSeedContainerQFrame)


        self.SeedVLayout_3.addWidget(self.cardanoFromSeedAndClientContainerQFrame)

        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_2 = QFrame(self.cardanoFromSeedClientContainerQFrame)
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_2.setObjectName(u"cardanoFromMnemonicClientAndPassphraseContainerQFrame_2")
        self.horizontalLayout_42 = QHBoxLayout(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_2)
        self.horizontalLayout_42.setSpacing(15)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicClientContainerQFrame_2 = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_2)
        self.cardanoFromMnemonicClientContainerQFrame_2.setObjectName(u"cardanoFromMnemonicClientContainerQFrame_2")
        self.cardanoFromMnemonicClientContainerQFrame_2.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_16 = QVBoxLayout(self.cardanoFromMnemonicClientContainerQFrame_2)
        self.ClientVLayout_16.setSpacing(5)
        self.ClientVLayout_16.setObjectName(u"ClientVLayout_16")
        self.ClientVLayout_16.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_9 = QFrame(self.cardanoFromMnemonicClientContainerQFrame_2)
        self.ClientLabelQFrame_9.setObjectName(u"ClientLabelQFrame_9")
        self.MStrengthLabelHLayout_21 = QHBoxLayout(self.ClientLabelQFrame_9)
        self.MStrengthLabelHLayout_21.setSpacing(15)
        self.MStrengthLabelHLayout_21.setObjectName(u"MStrengthLabelHLayout_21")
        self.MStrengthLabelHLayout_21.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_9 = QLabel(self.ClientLabelQFrame_9)
        self.ClientQLabel_9.setObjectName(u"ClientQLabel_9")

        self.MStrengthLabelHLayout_21.addWidget(self.ClientQLabel_9)

        self.ClientLabelHSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_21.addItem(self.ClientLabelHSpacer_9)


        self.ClientVLayout_16.addWidget(self.ClientLabelQFrame_9)

        self.ClientQComboBox_9 = QComboBox(self.cardanoFromMnemonicClientContainerQFrame_2)
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.addItem("")
        self.ClientQComboBox_9.setObjectName(u"ClientQComboBox_9")

        self.ClientVLayout_16.addWidget(self.ClientQComboBox_9)


        self.horizontalLayout_42.addWidget(self.cardanoFromMnemonicClientContainerQFrame_2)

        self.cardanoFromClientContainerQFrame = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_2)
        self.cardanoFromClientContainerQFrame.setObjectName(u"cardanoFromClientContainerQFrame")
        self.cardanoFromClientContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_9 = QVBoxLayout(self.cardanoFromClientContainerQFrame)
        self.ClientVLayout_9.setSpacing(5)
        self.ClientVLayout_9.setObjectName(u"ClientVLayout_9")
        self.ClientVLayout_9.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromClientLabelContainerQFrame = QFrame(self.cardanoFromClientContainerQFrame)
        self.cardanoFromClientLabelContainerQFrame.setObjectName(u"cardanoFromClientLabelContainerQFrame")
        self.MStrengthLabelHLayout_12 = QHBoxLayout(self.cardanoFromClientLabelContainerQFrame)
        self.MStrengthLabelHLayout_12.setSpacing(15)
        self.MStrengthLabelHLayout_12.setObjectName(u"MStrengthLabelHLayout_12")
        self.MStrengthLabelHLayout_12.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromClientQLabel = QLabel(self.cardanoFromClientLabelContainerQFrame)
        self.cardanoFromClientQLabel.setObjectName(u"cardanoFromClientQLabel")

        self.MStrengthLabelHLayout_12.addWidget(self.cardanoFromClientQLabel)

        self.cardanoFromClientLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_12.addItem(self.cardanoFromClientLabelContainerQFrameHSpacer)


        self.ClientVLayout_9.addWidget(self.cardanoFromClientLabelContainerQFrame)

        self.cardanoFromClientQComboBox = QComboBox(self.cardanoFromClientContainerQFrame)
        self.cardanoFromClientQComboBox.addItem("")
        self.cardanoFromClientQComboBox.addItem("")
        self.cardanoFromClientQComboBox.addItem("")
        self.cardanoFromClientQComboBox.addItem("")
        self.cardanoFromClientQComboBox.addItem("")
        self.cardanoFromClientQComboBox.addItem("")
        self.cardanoFromClientQComboBox.setObjectName(u"cardanoFromClientQComboBox")

        self.ClientVLayout_9.addWidget(self.cardanoFromClientQComboBox)


        self.horizontalLayout_42.addWidget(self.cardanoFromClientContainerQFrame)

        self.cardanoFromMnemonicPassphraseContainerQFrame_2 = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_2)
        self.cardanoFromMnemonicPassphraseContainerQFrame_2.setObjectName(u"cardanoFromMnemonicPassphraseContainerQFrame_2")
        self.EPassphraseVLayout_11 = QVBoxLayout(self.cardanoFromMnemonicPassphraseContainerQFrame_2)
        self.EPassphraseVLayout_11.setSpacing(5)
        self.EPassphraseVLayout_11.setObjectName(u"EPassphraseVLayout_11")
        self.EPassphraseVLayout_11.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicPassphraseLabelContainerQFrame_2 = QFrame(self.cardanoFromMnemonicPassphraseContainerQFrame_2)
        self.cardanoFromMnemonicPassphraseLabelContainerQFrame_2.setObjectName(u"cardanoFromMnemonicPassphraseLabelContainerQFrame_2")
        self.MPassphraseLabelHLayout_6 = QHBoxLayout(self.cardanoFromMnemonicPassphraseLabelContainerQFrame_2)
        self.MPassphraseLabelHLayout_6.setSpacing(15)
        self.MPassphraseLabelHLayout_6.setObjectName(u"MPassphraseLabelHLayout_6")
        self.MPassphraseLabelHLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicPassphraseQLabel_2 = QLabel(self.cardanoFromMnemonicPassphraseLabelContainerQFrame_2)
        self.cardanoFromMnemonicPassphraseQLabel_2.setObjectName(u"cardanoFromMnemonicPassphraseQLabel_2")

        self.MPassphraseLabelHLayout_6.addWidget(self.cardanoFromMnemonicPassphraseQLabel_2)

        self.cardanoFromMnemonicPassphraseLabelContainerQFrameHSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MPassphraseLabelHLayout_6.addItem(self.cardanoFromMnemonicPassphraseLabelContainerQFrameHSpacer_2)


        self.EPassphraseVLayout_11.addWidget(self.cardanoFromMnemonicPassphraseLabelContainerQFrame_2)

        self.cardanoFromMnemonicPassphraseGenerateContainerQFrame_2 = QFrame(self.cardanoFromMnemonicPassphraseContainerQFrame_2)
        self.cardanoFromMnemonicPassphraseGenerateContainerQFrame_2.setObjectName(u"cardanoFromMnemonicPassphraseGenerateContainerQFrame_2")
        self.horizontalLayout_62 = QHBoxLayout(self.cardanoFromMnemonicPassphraseGenerateContainerQFrame_2)
        self.horizontalLayout_62.setSpacing(15)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicPassphraseQLineEdit_2 = QLineEdit(self.cardanoFromMnemonicPassphraseGenerateContainerQFrame_2)
        self.cardanoFromMnemonicPassphraseQLineEdit_2.setObjectName(u"cardanoFromMnemonicPassphraseQLineEdit_2")

        self.horizontalLayout_62.addWidget(self.cardanoFromMnemonicPassphraseQLineEdit_2)

        self.cardanoFromMnemonicPassphraseGenerateQPushButton_2 = QPushButton(self.cardanoFromMnemonicPassphraseGenerateContainerQFrame_2)
        self.cardanoFromMnemonicPassphraseGenerateQPushButton_2.setObjectName(u"cardanoFromMnemonicPassphraseGenerateQPushButton_2")

        self.horizontalLayout_62.addWidget(self.cardanoFromMnemonicPassphraseGenerateQPushButton_2)


        self.EPassphraseVLayout_11.addWidget(self.cardanoFromMnemonicPassphraseGenerateContainerQFrame_2)


        self.horizontalLayout_42.addWidget(self.cardanoFromMnemonicPassphraseContainerQFrame_2)


        self.SeedVLayout_3.addWidget(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_2)

        self.cardanoFromSeedClientContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout_3.addItem(self.cardanoFromSeedClientContainerQFrameVSpacer)


        self.verticalLayout_37.addWidget(self.cardanoFromSeedClientContainerQFrame)

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

        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_5 = QFrame(self.cardanoFromXPrivateKeyQStackedWidget)
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_5.setObjectName(u"cardanoFromMnemonicClientAndPassphraseContainerQFrame_5")
        self.horizontalLayout_63 = QHBoxLayout(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_5)
        self.horizontalLayout_63.setSpacing(15)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicClientContainerQFrame_5 = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_5)
        self.cardanoFromMnemonicClientContainerQFrame_5.setObjectName(u"cardanoFromMnemonicClientContainerQFrame_5")
        self.cardanoFromMnemonicClientContainerQFrame_5.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_19 = QVBoxLayout(self.cardanoFromMnemonicClientContainerQFrame_5)
        self.ClientVLayout_19.setSpacing(5)
        self.ClientVLayout_19.setObjectName(u"ClientVLayout_19")
        self.ClientVLayout_19.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_12 = QFrame(self.cardanoFromMnemonicClientContainerQFrame_5)
        self.ClientLabelQFrame_12.setObjectName(u"ClientLabelQFrame_12")
        self.MStrengthLabelHLayout_24 = QHBoxLayout(self.ClientLabelQFrame_12)
        self.MStrengthLabelHLayout_24.setSpacing(15)
        self.MStrengthLabelHLayout_24.setObjectName(u"MStrengthLabelHLayout_24")
        self.MStrengthLabelHLayout_24.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_12 = QLabel(self.ClientLabelQFrame_12)
        self.ClientQLabel_12.setObjectName(u"ClientQLabel_12")

        self.MStrengthLabelHLayout_24.addWidget(self.ClientQLabel_12)

        self.ClientLabelHSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_24.addItem(self.ClientLabelHSpacer_12)


        self.ClientVLayout_19.addWidget(self.ClientLabelQFrame_12)

        self.ClientQComboBox_12 = QComboBox(self.cardanoFromMnemonicClientContainerQFrame_5)
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.addItem("")
        self.ClientQComboBox_12.setObjectName(u"ClientQComboBox_12")

        self.ClientVLayout_19.addWidget(self.ClientQComboBox_12)


        self.horizontalLayout_63.addWidget(self.cardanoFromMnemonicClientContainerQFrame_5)

        self.cardanoFromClientContainerQFrame_4 = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_5)
        self.cardanoFromClientContainerQFrame_4.setObjectName(u"cardanoFromClientContainerQFrame_4")
        self.cardanoFromClientContainerQFrame_4.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_17 = QVBoxLayout(self.cardanoFromClientContainerQFrame_4)
        self.ClientVLayout_17.setSpacing(5)
        self.ClientVLayout_17.setObjectName(u"ClientVLayout_17")
        self.ClientVLayout_17.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromClientLabelContainerQFrame_4 = QFrame(self.cardanoFromClientContainerQFrame_4)
        self.cardanoFromClientLabelContainerQFrame_4.setObjectName(u"cardanoFromClientLabelContainerQFrame_4")
        self.MStrengthLabelHLayout_22 = QHBoxLayout(self.cardanoFromClientLabelContainerQFrame_4)
        self.MStrengthLabelHLayout_22.setSpacing(15)
        self.MStrengthLabelHLayout_22.setObjectName(u"MStrengthLabelHLayout_22")
        self.MStrengthLabelHLayout_22.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromClientQLabel_4 = QLabel(self.cardanoFromClientLabelContainerQFrame_4)
        self.cardanoFromClientQLabel_4.setObjectName(u"cardanoFromClientQLabel_4")

        self.MStrengthLabelHLayout_22.addWidget(self.cardanoFromClientQLabel_4)

        self.cardanoFromClientLabelContainerQFrameHSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_22.addItem(self.cardanoFromClientLabelContainerQFrameHSpacer_4)


        self.ClientVLayout_17.addWidget(self.cardanoFromClientLabelContainerQFrame_4)

        self.cardanoFromClientQComboBox_4 = QComboBox(self.cardanoFromClientContainerQFrame_4)
        self.cardanoFromClientQComboBox_4.addItem("")
        self.cardanoFromClientQComboBox_4.addItem("")
        self.cardanoFromClientQComboBox_4.addItem("")
        self.cardanoFromClientQComboBox_4.addItem("")
        self.cardanoFromClientQComboBox_4.addItem("")
        self.cardanoFromClientQComboBox_4.addItem("")
        self.cardanoFromClientQComboBox_4.setObjectName(u"cardanoFromClientQComboBox_4")

        self.ClientVLayout_17.addWidget(self.cardanoFromClientQComboBox_4)


        self.horizontalLayout_63.addWidget(self.cardanoFromClientContainerQFrame_4)


        self.verticalLayout_39.addWidget(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_5)

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

        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_4 = QFrame(self.cardanoFromXPublicKeyQStackedWidget)
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_4.setObjectName(u"cardanoFromMnemonicClientAndPassphraseContainerQFrame_4")
        self.horizontalLayout_64 = QHBoxLayout(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_4)
        self.horizontalLayout_64.setSpacing(15)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicClientContainerQFrame_4 = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_4)
        self.cardanoFromMnemonicClientContainerQFrame_4.setObjectName(u"cardanoFromMnemonicClientContainerQFrame_4")
        self.cardanoFromMnemonicClientContainerQFrame_4.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_18 = QVBoxLayout(self.cardanoFromMnemonicClientContainerQFrame_4)
        self.ClientVLayout_18.setSpacing(5)
        self.ClientVLayout_18.setObjectName(u"ClientVLayout_18")
        self.ClientVLayout_18.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_11 = QFrame(self.cardanoFromMnemonicClientContainerQFrame_4)
        self.ClientLabelQFrame_11.setObjectName(u"ClientLabelQFrame_11")
        self.MStrengthLabelHLayout_23 = QHBoxLayout(self.ClientLabelQFrame_11)
        self.MStrengthLabelHLayout_23.setSpacing(15)
        self.MStrengthLabelHLayout_23.setObjectName(u"MStrengthLabelHLayout_23")
        self.MStrengthLabelHLayout_23.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_11 = QLabel(self.ClientLabelQFrame_11)
        self.ClientQLabel_11.setObjectName(u"ClientQLabel_11")

        self.MStrengthLabelHLayout_23.addWidget(self.ClientQLabel_11)

        self.ClientLabelHSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_23.addItem(self.ClientLabelHSpacer_11)


        self.ClientVLayout_18.addWidget(self.ClientLabelQFrame_11)

        self.ClientQComboBox_11 = QComboBox(self.cardanoFromMnemonicClientContainerQFrame_4)
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.addItem("")
        self.ClientQComboBox_11.setObjectName(u"ClientQComboBox_11")

        self.ClientVLayout_18.addWidget(self.ClientQComboBox_11)


        self.horizontalLayout_64.addWidget(self.cardanoFromMnemonicClientContainerQFrame_4)

        self.cardanoFromClientContainerQFrame_3 = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_4)
        self.cardanoFromClientContainerQFrame_3.setObjectName(u"cardanoFromClientContainerQFrame_3")
        self.cardanoFromClientContainerQFrame_3.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_20 = QVBoxLayout(self.cardanoFromClientContainerQFrame_3)
        self.ClientVLayout_20.setSpacing(5)
        self.ClientVLayout_20.setObjectName(u"ClientVLayout_20")
        self.ClientVLayout_20.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromClientLabelContainerQFrame_3 = QFrame(self.cardanoFromClientContainerQFrame_3)
        self.cardanoFromClientLabelContainerQFrame_3.setObjectName(u"cardanoFromClientLabelContainerQFrame_3")
        self.MStrengthLabelHLayout_25 = QHBoxLayout(self.cardanoFromClientLabelContainerQFrame_3)
        self.MStrengthLabelHLayout_25.setSpacing(15)
        self.MStrengthLabelHLayout_25.setObjectName(u"MStrengthLabelHLayout_25")
        self.MStrengthLabelHLayout_25.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromClientQLabel_3 = QLabel(self.cardanoFromClientLabelContainerQFrame_3)
        self.cardanoFromClientQLabel_3.setObjectName(u"cardanoFromClientQLabel_3")

        self.MStrengthLabelHLayout_25.addWidget(self.cardanoFromClientQLabel_3)

        self.cardanoFromClientLabelContainerQFrameHSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_25.addItem(self.cardanoFromClientLabelContainerQFrameHSpacer_3)


        self.ClientVLayout_20.addWidget(self.cardanoFromClientLabelContainerQFrame_3)

        self.cardanoFromClientQComboBox_3 = QComboBox(self.cardanoFromClientContainerQFrame_3)
        self.cardanoFromClientQComboBox_3.addItem("")
        self.cardanoFromClientQComboBox_3.addItem("")
        self.cardanoFromClientQComboBox_3.addItem("")
        self.cardanoFromClientQComboBox_3.addItem("")
        self.cardanoFromClientQComboBox_3.addItem("")
        self.cardanoFromClientQComboBox_3.addItem("")
        self.cardanoFromClientQComboBox_3.setObjectName(u"cardanoFromClientQComboBox_3")

        self.ClientVLayout_20.addWidget(self.cardanoFromClientQComboBox_3)


        self.horizontalLayout_64.addWidget(self.cardanoFromClientContainerQFrame_3)


        self.verticalLayout_40.addWidget(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_4)

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

        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_3 = QFrame(self.cardanoFromPrivateKeyQStackedWidget)
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_3.setObjectName(u"cardanoFromMnemonicClientAndPassphraseContainerQFrame_3")
        self.horizontalLayout_65 = QHBoxLayout(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_3)
        self.horizontalLayout_65.setSpacing(15)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicClientContainerQFrame_3 = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_3)
        self.cardanoFromMnemonicClientContainerQFrame_3.setObjectName(u"cardanoFromMnemonicClientContainerQFrame_3")
        self.cardanoFromMnemonicClientContainerQFrame_3.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_21 = QVBoxLayout(self.cardanoFromMnemonicClientContainerQFrame_3)
        self.ClientVLayout_21.setSpacing(5)
        self.ClientVLayout_21.setObjectName(u"ClientVLayout_21")
        self.ClientVLayout_21.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_10 = QFrame(self.cardanoFromMnemonicClientContainerQFrame_3)
        self.ClientLabelQFrame_10.setObjectName(u"ClientLabelQFrame_10")
        self.MStrengthLabelHLayout_26 = QHBoxLayout(self.ClientLabelQFrame_10)
        self.MStrengthLabelHLayout_26.setSpacing(15)
        self.MStrengthLabelHLayout_26.setObjectName(u"MStrengthLabelHLayout_26")
        self.MStrengthLabelHLayout_26.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_10 = QLabel(self.ClientLabelQFrame_10)
        self.ClientQLabel_10.setObjectName(u"ClientQLabel_10")

        self.MStrengthLabelHLayout_26.addWidget(self.ClientQLabel_10)

        self.ClientLabelHSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_26.addItem(self.ClientLabelHSpacer_10)


        self.ClientVLayout_21.addWidget(self.ClientLabelQFrame_10)

        self.ClientQComboBox_10 = QComboBox(self.cardanoFromMnemonicClientContainerQFrame_3)
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.addItem("")
        self.ClientQComboBox_10.setObjectName(u"ClientQComboBox_10")

        self.ClientVLayout_21.addWidget(self.ClientQComboBox_10)


        self.horizontalLayout_65.addWidget(self.cardanoFromMnemonicClientContainerQFrame_3)

        self.cardanoFromClientContainerQFrame_2 = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_3)
        self.cardanoFromClientContainerQFrame_2.setObjectName(u"cardanoFromClientContainerQFrame_2")
        self.cardanoFromClientContainerQFrame_2.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_22 = QVBoxLayout(self.cardanoFromClientContainerQFrame_2)
        self.ClientVLayout_22.setSpacing(5)
        self.ClientVLayout_22.setObjectName(u"ClientVLayout_22")
        self.ClientVLayout_22.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromClientLabelContainerQFrame_2 = QFrame(self.cardanoFromClientContainerQFrame_2)
        self.cardanoFromClientLabelContainerQFrame_2.setObjectName(u"cardanoFromClientLabelContainerQFrame_2")
        self.MStrengthLabelHLayout_27 = QHBoxLayout(self.cardanoFromClientLabelContainerQFrame_2)
        self.MStrengthLabelHLayout_27.setSpacing(15)
        self.MStrengthLabelHLayout_27.setObjectName(u"MStrengthLabelHLayout_27")
        self.MStrengthLabelHLayout_27.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromClientQLabel_2 = QLabel(self.cardanoFromClientLabelContainerQFrame_2)
        self.cardanoFromClientQLabel_2.setObjectName(u"cardanoFromClientQLabel_2")

        self.MStrengthLabelHLayout_27.addWidget(self.cardanoFromClientQLabel_2)

        self.cardanoFromClientLabelContainerQFrameHSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_27.addItem(self.cardanoFromClientLabelContainerQFrameHSpacer_2)


        self.ClientVLayout_22.addWidget(self.cardanoFromClientLabelContainerQFrame_2)

        self.cardanoFromClientQComboBox_2 = QComboBox(self.cardanoFromClientContainerQFrame_2)
        self.cardanoFromClientQComboBox_2.addItem("")
        self.cardanoFromClientQComboBox_2.addItem("")
        self.cardanoFromClientQComboBox_2.addItem("")
        self.cardanoFromClientQComboBox_2.addItem("")
        self.cardanoFromClientQComboBox_2.addItem("")
        self.cardanoFromClientQComboBox_2.addItem("")
        self.cardanoFromClientQComboBox_2.setObjectName(u"cardanoFromClientQComboBox_2")

        self.ClientVLayout_22.addWidget(self.cardanoFromClientQComboBox_2)


        self.horizontalLayout_65.addWidget(self.cardanoFromClientContainerQFrame_2)


        self.verticalLayout_43.addWidget(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_3)

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

        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_6 = QFrame(self.cardanoFromPublicKeyQStackedWidget)
        self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_6.setObjectName(u"cardanoFromMnemonicClientAndPassphraseContainerQFrame_6")
        self.horizontalLayout_66 = QHBoxLayout(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_6)
        self.horizontalLayout_66.setSpacing(15)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromMnemonicClientContainerQFrame_6 = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_6)
        self.cardanoFromMnemonicClientContainerQFrame_6.setObjectName(u"cardanoFromMnemonicClientContainerQFrame_6")
        self.cardanoFromMnemonicClientContainerQFrame_6.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_23 = QVBoxLayout(self.cardanoFromMnemonicClientContainerQFrame_6)
        self.ClientVLayout_23.setSpacing(5)
        self.ClientVLayout_23.setObjectName(u"ClientVLayout_23")
        self.ClientVLayout_23.setContentsMargins(0, 0, 0, 0)
        self.ClientLabelQFrame_13 = QFrame(self.cardanoFromMnemonicClientContainerQFrame_6)
        self.ClientLabelQFrame_13.setObjectName(u"ClientLabelQFrame_13")
        self.MStrengthLabelHLayout_28 = QHBoxLayout(self.ClientLabelQFrame_13)
        self.MStrengthLabelHLayout_28.setSpacing(15)
        self.MStrengthLabelHLayout_28.setObjectName(u"MStrengthLabelHLayout_28")
        self.MStrengthLabelHLayout_28.setContentsMargins(0, 0, 0, 0)
        self.ClientQLabel_13 = QLabel(self.ClientLabelQFrame_13)
        self.ClientQLabel_13.setObjectName(u"ClientQLabel_13")

        self.MStrengthLabelHLayout_28.addWidget(self.ClientQLabel_13)

        self.ClientLabelHSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_28.addItem(self.ClientLabelHSpacer_13)


        self.ClientVLayout_23.addWidget(self.ClientLabelQFrame_13)

        self.ClientQComboBox_13 = QComboBox(self.cardanoFromMnemonicClientContainerQFrame_6)
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.addItem("")
        self.ClientQComboBox_13.setObjectName(u"ClientQComboBox_13")

        self.ClientVLayout_23.addWidget(self.ClientQComboBox_13)


        self.horizontalLayout_66.addWidget(self.cardanoFromMnemonicClientContainerQFrame_6)

        self.cardanoFromClientContainerQFrame_5 = QFrame(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_6)
        self.cardanoFromClientContainerQFrame_5.setObjectName(u"cardanoFromClientContainerQFrame_5")
        self.cardanoFromClientContainerQFrame_5.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_24 = QVBoxLayout(self.cardanoFromClientContainerQFrame_5)
        self.ClientVLayout_24.setSpacing(5)
        self.ClientVLayout_24.setObjectName(u"ClientVLayout_24")
        self.ClientVLayout_24.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromClientLabelContainerQFrame_5 = QFrame(self.cardanoFromClientContainerQFrame_5)
        self.cardanoFromClientLabelContainerQFrame_5.setObjectName(u"cardanoFromClientLabelContainerQFrame_5")
        self.MStrengthLabelHLayout_29 = QHBoxLayout(self.cardanoFromClientLabelContainerQFrame_5)
        self.MStrengthLabelHLayout_29.setSpacing(15)
        self.MStrengthLabelHLayout_29.setObjectName(u"MStrengthLabelHLayout_29")
        self.MStrengthLabelHLayout_29.setContentsMargins(0, 0, 0, 0)
        self.cardanoFromClientQLabel_5 = QLabel(self.cardanoFromClientLabelContainerQFrame_5)
        self.cardanoFromClientQLabel_5.setObjectName(u"cardanoFromClientQLabel_5")

        self.MStrengthLabelHLayout_29.addWidget(self.cardanoFromClientQLabel_5)

        self.cardanoFromClientLabelContainerQFrameHSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_29.addItem(self.cardanoFromClientLabelContainerQFrameHSpacer_5)


        self.ClientVLayout_24.addWidget(self.cardanoFromClientLabelContainerQFrame_5)

        self.cardanoFromClientQComboBox_5 = QComboBox(self.cardanoFromClientContainerQFrame_5)
        self.cardanoFromClientQComboBox_5.addItem("")
        self.cardanoFromClientQComboBox_5.addItem("")
        self.cardanoFromClientQComboBox_5.addItem("")
        self.cardanoFromClientQComboBox_5.addItem("")
        self.cardanoFromClientQComboBox_5.addItem("")
        self.cardanoFromClientQComboBox_5.addItem("")
        self.cardanoFromClientQComboBox_5.setObjectName(u"cardanoFromClientQComboBox_5")

        self.ClientVLayout_24.addWidget(self.cardanoFromClientQComboBox_5)


        self.horizontalLayout_66.addWidget(self.cardanoFromClientContainerQFrame_5)


        self.verticalLayout_44.addWidget(self.cardanoFromMnemonicClientAndPassphraseContainerQFrame_6)

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

        self.electrumV1FromEntropyClientAndPassphraseContainerQFrame = QFrame(self.electrumV1FromEntropyQStackedWidget)
        self.electrumV1FromEntropyClientAndPassphraseContainerQFrame.setObjectName(u"electrumV1FromEntropyClientAndPassphraseContainerQFrame")
        self.horizontalLayout_44 = QHBoxLayout(self.electrumV1FromEntropyClientAndPassphraseContainerQFrame)
        self.horizontalLayout_44.setSpacing(15)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyClientContainerQFrame = QFrame(self.electrumV1FromEntropyClientAndPassphraseContainerQFrame)
        self.electrumV1FromEntropyClientContainerQFrame.setObjectName(u"electrumV1FromEntropyClientContainerQFrame")
        self.electrumV1FromEntropyClientContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_10 = QVBoxLayout(self.electrumV1FromEntropyClientContainerQFrame)
        self.ClientVLayout_10.setSpacing(5)
        self.ClientVLayout_10.setObjectName(u"ClientVLayout_10")
        self.ClientVLayout_10.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyClientLabelContainerQFrame = QFrame(self.electrumV1FromEntropyClientContainerQFrame)
        self.electrumV1FromEntropyClientLabelContainerQFrame.setObjectName(u"electrumV1FromEntropyClientLabelContainerQFrame")
        self.MStrengthLabelHLayout_13 = QHBoxLayout(self.electrumV1FromEntropyClientLabelContainerQFrame)
        self.MStrengthLabelHLayout_13.setSpacing(15)
        self.MStrengthLabelHLayout_13.setObjectName(u"MStrengthLabelHLayout_13")
        self.MStrengthLabelHLayout_13.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromEntropyClientQLabel = QLabel(self.electrumV1FromEntropyClientLabelContainerQFrame)
        self.electrumV1FromEntropyClientQLabel.setObjectName(u"electrumV1FromEntropyClientQLabel")

        self.MStrengthLabelHLayout_13.addWidget(self.electrumV1FromEntropyClientQLabel)

        self.electrumV1FromEntropyClientLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_13.addItem(self.electrumV1FromEntropyClientLabelContainerQFrameHSpacer)


        self.ClientVLayout_10.addWidget(self.electrumV1FromEntropyClientLabelContainerQFrame)

        self.electrumV1FromEntropyClientQComboBox = QComboBox(self.electrumV1FromEntropyClientContainerQFrame)
        self.electrumV1FromEntropyClientQComboBox.addItem("")
        self.electrumV1FromEntropyClientQComboBox.addItem("")
        self.electrumV1FromEntropyClientQComboBox.addItem("")
        self.electrumV1FromEntropyClientQComboBox.addItem("")
        self.electrumV1FromEntropyClientQComboBox.addItem("")
        self.electrumV1FromEntropyClientQComboBox.addItem("")
        self.electrumV1FromEntropyClientQComboBox.setObjectName(u"electrumV1FromEntropyClientQComboBox")

        self.ClientVLayout_10.addWidget(self.electrumV1FromEntropyClientQComboBox)


        self.horizontalLayout_44.addWidget(self.electrumV1FromEntropyClientContainerQFrame)

        self.electrumV1FromEntropyPassphraseContainerQFrame = QFrame(self.electrumV1FromEntropyClientAndPassphraseContainerQFrame)
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


        self.verticalLayout_46.addWidget(self.electrumV1FromEntropyClientAndPassphraseContainerQFrame)

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

        self.electrumV1FromMnemonicClientAndPassphraseContainerQFrame = QFrame(self.electrumV1FromMnemonicQStackedWidget)
        self.electrumV1FromMnemonicClientAndPassphraseContainerQFrame.setObjectName(u"electrumV1FromMnemonicClientAndPassphraseContainerQFrame")
        self.horizontalLayout_48 = QHBoxLayout(self.electrumV1FromMnemonicClientAndPassphraseContainerQFrame)
        self.horizontalLayout_48.setSpacing(15)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicClientContainerQFrame = QFrame(self.electrumV1FromMnemonicClientAndPassphraseContainerQFrame)
        self.electrumV1FromMnemonicClientContainerQFrame.setObjectName(u"electrumV1FromMnemonicClientContainerQFrame")
        self.electrumV1FromMnemonicClientContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_11 = QVBoxLayout(self.electrumV1FromMnemonicClientContainerQFrame)
        self.ClientVLayout_11.setSpacing(5)
        self.ClientVLayout_11.setObjectName(u"ClientVLayout_11")
        self.ClientVLayout_11.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicClientLabelContainerQFrame = QFrame(self.electrumV1FromMnemonicClientContainerQFrame)
        self.electrumV1FromMnemonicClientLabelContainerQFrame.setObjectName(u"electrumV1FromMnemonicClientLabelContainerQFrame")
        self.MStrengthLabelHLayout_14 = QHBoxLayout(self.electrumV1FromMnemonicClientLabelContainerQFrame)
        self.MStrengthLabelHLayout_14.setSpacing(15)
        self.MStrengthLabelHLayout_14.setObjectName(u"MStrengthLabelHLayout_14")
        self.MStrengthLabelHLayout_14.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromMnemonicClientQLabel = QLabel(self.electrumV1FromMnemonicClientLabelContainerQFrame)
        self.electrumV1FromMnemonicClientQLabel.setObjectName(u"electrumV1FromMnemonicClientQLabel")

        self.MStrengthLabelHLayout_14.addWidget(self.electrumV1FromMnemonicClientQLabel)

        self.electrumV1FromMnemonicClientLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_14.addItem(self.electrumV1FromMnemonicClientLabelContainerQFrameHSpacer)


        self.ClientVLayout_11.addWidget(self.electrumV1FromMnemonicClientLabelContainerQFrame)

        self.electrumV1FromMnemonicClientQComboBox = QComboBox(self.electrumV1FromMnemonicClientContainerQFrame)
        self.electrumV1FromMnemonicClientQComboBox.addItem("")
        self.electrumV1FromMnemonicClientQComboBox.addItem("")
        self.electrumV1FromMnemonicClientQComboBox.addItem("")
        self.electrumV1FromMnemonicClientQComboBox.addItem("")
        self.electrumV1FromMnemonicClientQComboBox.addItem("")
        self.electrumV1FromMnemonicClientQComboBox.addItem("")
        self.electrumV1FromMnemonicClientQComboBox.setObjectName(u"electrumV1FromMnemonicClientQComboBox")

        self.ClientVLayout_11.addWidget(self.electrumV1FromMnemonicClientQComboBox)


        self.horizontalLayout_48.addWidget(self.electrumV1FromMnemonicClientContainerQFrame)

        self.electrumV1FromMnemonicPassphraseContainerQFrame = QFrame(self.electrumV1FromMnemonicClientAndPassphraseContainerQFrame)
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


        self.verticalLayout_48.addWidget(self.electrumV1FromMnemonicClientAndPassphraseContainerQFrame)

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
        self.electrumV1FromSeedClientContainerQFrame = QFrame(self.electrumV1FromSeedQStackedWidget)
        self.electrumV1FromSeedClientContainerQFrame.setObjectName(u"electrumV1FromSeedClientContainerQFrame")
        self.electrumV1FromSeedClientContainerQFrame.setMinimumSize(QSize(400, 0))
        self.SeedVLayout_4 = QVBoxLayout(self.electrumV1FromSeedClientContainerQFrame)
        self.SeedVLayout_4.setSpacing(5)
        self.SeedVLayout_4.setObjectName(u"SeedVLayout_4")
        self.SeedVLayout_4.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedAndClientContainerQFrame = QFrame(self.electrumV1FromSeedClientContainerQFrame)
        self.electrumV1FromSeedAndClientContainerQFrame.setObjectName(u"electrumV1FromSeedAndClientContainerQFrame")
        self.horizontalLayout_51 = QHBoxLayout(self.electrumV1FromSeedAndClientContainerQFrame)
        self.horizontalLayout_51.setSpacing(15)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromSeedContainerQFrame = QFrame(self.electrumV1FromSeedAndClientContainerQFrame)
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

        self.electrumV1FromClientContainerQFrame = QFrame(self.electrumV1FromSeedAndClientContainerQFrame)
        self.electrumV1FromClientContainerQFrame.setObjectName(u"electrumV1FromClientContainerQFrame")
        self.electrumV1FromClientContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_12 = QVBoxLayout(self.electrumV1FromClientContainerQFrame)
        self.ClientVLayout_12.setSpacing(5)
        self.ClientVLayout_12.setObjectName(u"ClientVLayout_12")
        self.ClientVLayout_12.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromClientLabelContainerQFrame = QFrame(self.electrumV1FromClientContainerQFrame)
        self.electrumV1FromClientLabelContainerQFrame.setObjectName(u"electrumV1FromClientLabelContainerQFrame")
        self.MStrengthLabelHLayout_16 = QHBoxLayout(self.electrumV1FromClientLabelContainerQFrame)
        self.MStrengthLabelHLayout_16.setSpacing(15)
        self.MStrengthLabelHLayout_16.setObjectName(u"MStrengthLabelHLayout_16")
        self.MStrengthLabelHLayout_16.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromClientQLabel = QLabel(self.electrumV1FromClientLabelContainerQFrame)
        self.electrumV1FromClientQLabel.setObjectName(u"electrumV1FromClientQLabel")

        self.MStrengthLabelHLayout_16.addWidget(self.electrumV1FromClientQLabel)

        self.electrumV1FromClientLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_16.addItem(self.electrumV1FromClientLabelContainerQFrameHSpacer)


        self.ClientVLayout_12.addWidget(self.electrumV1FromClientLabelContainerQFrame)

        self.electrumV1FromClientQComboBox = QComboBox(self.electrumV1FromClientContainerQFrame)
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.addItem("")
        self.electrumV1FromClientQComboBox.setObjectName(u"electrumV1FromClientQComboBox")

        self.ClientVLayout_12.addWidget(self.electrumV1FromClientQComboBox)


        self.horizontalLayout_51.addWidget(self.electrumV1FromClientContainerQFrame)


        self.SeedVLayout_4.addWidget(self.electrumV1FromSeedAndClientContainerQFrame)

        self.electrumV1FromSeedClientContainerQFrameVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout_4.addItem(self.electrumV1FromSeedClientContainerQFrameVSpacer)


        self.verticalLayout_49.addWidget(self.electrumV1FromSeedClientContainerQFrame)

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

        self.frame_55 = QFrame(self.electrumV1FromWIFQStackedWidget)
        self.frame_55.setObjectName(u"frame_55")
        self.horizontalLayout_52 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_52.setSpacing(15)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromWIFBIP38PassphraseContainerQFrame = QFrame(self.frame_55)
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

        self.frame_66 = QFrame(self.frame_55)
        self.frame_66.setObjectName(u"frame_66")
        self.verticalLayout_81 = QVBoxLayout(self.frame_66)
        self.verticalLayout_81.setSpacing(5)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.frame_66)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_77.setSpacing(15)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_67)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_77.addWidget(self.label_35)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_12)


        self.verticalLayout_81.addWidget(self.frame_67)

        self.comboBox_16 = QComboBox(self.frame_66)
        self.comboBox_16.setObjectName(u"comboBox_16")

        self.verticalLayout_81.addWidget(self.comboBox_16)


        self.horizontalLayout_52.addWidget(self.frame_66)


        self.verticalLayout_53.addWidget(self.frame_55)

        self.electrumV1FromWIFQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.electrumV1FromWIFQStackedWidgetVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromWIFQStackedWidget)
        self.electrumV1FromPrivateKeyQStackedWidget = QWidget()
        self.electrumV1FromPrivateKeyQStackedWidget.setObjectName(u"electrumV1FromPrivateKeyQStackedWidget")
        self.verticalLayout_55 = QVBoxLayout(self.electrumV1FromPrivateKeyQStackedWidget)
        self.verticalLayout_55.setSpacing(15)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.electrumV1FromPrivateKeyQStackedWidget)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_72.setSpacing(15)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPrivateKeyContainerQFrame = QFrame(self.frame_56)
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

        self.frame_64 = QFrame(self.frame_56)
        self.frame_64.setObjectName(u"frame_64")
        self.verticalLayout_91 = QVBoxLayout(self.frame_64)
        self.verticalLayout_91.setSpacing(5)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.frame_71 = QFrame(self.frame_64)
        self.frame_71.setObjectName(u"frame_71")
        self.horizontalLayout_80 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_80.setSpacing(15)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_71)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_80.addWidget(self.label_40)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_14)


        self.verticalLayout_91.addWidget(self.frame_71)

        self.comboBox_21 = QComboBox(self.frame_64)
        self.comboBox_21.setObjectName(u"comboBox_21")

        self.verticalLayout_91.addWidget(self.comboBox_21)


        self.horizontalLayout_72.addWidget(self.frame_64)


        self.verticalLayout_55.addWidget(self.frame_56)

        self.electrumV1FromPrivateKeyQStackedWidgetVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.electrumV1FromPrivateKeyQStackedWidgetVSpacer)

        self.electrumV1QStackedWidget.addWidget(self.electrumV1FromPrivateKeyQStackedWidget)
        self.electrumV1FromPublicKeyQStackedWidget = QWidget()
        self.electrumV1FromPublicKeyQStackedWidget.setObjectName(u"electrumV1FromPublicKeyQStackedWidget")
        self.verticalLayout_56 = QVBoxLayout(self.electrumV1FromPublicKeyQStackedWidget)
        self.verticalLayout_56.setSpacing(15)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.electrumV1FromPublicKeyQStackedWidget)
        self.frame_57.setObjectName(u"frame_57")
        self.horizontalLayout_78 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_78.setSpacing(15)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.electrumV1FromPublicKeyContainerQFrame = QFrame(self.frame_57)
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

        self.frame_68 = QFrame(self.frame_57)
        self.frame_68.setObjectName(u"frame_68")
        self.verticalLayout_83 = QVBoxLayout(self.frame_68)
        self.verticalLayout_83.setSpacing(5)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.frame_68)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_79.setSpacing(15)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_69)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_79.addWidget(self.label_37)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_13)


        self.verticalLayout_83.addWidget(self.frame_69)

        self.comboBox_18 = QComboBox(self.frame_68)
        self.comboBox_18.setObjectName(u"comboBox_18")

        self.verticalLayout_83.addWidget(self.comboBox_18)


        self.horizontalLayout_78.addWidget(self.frame_68)


        self.verticalLayout_56.addWidget(self.frame_57)

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

        self.electrumV2FromEntropyClientAndPassphraseContainerQFrame = QFrame(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromEntropyClientAndPassphraseContainerQFrame.setObjectName(u"electrumV2FromEntropyClientAndPassphraseContainerQFrame")
        self.horizontalLayout_54 = QHBoxLayout(self.electrumV2FromEntropyClientAndPassphraseContainerQFrame)
        self.horizontalLayout_54.setSpacing(15)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.electrumV2FromEntropyClientAndPassphraseContainerQFrame)
        self.frame_48.setObjectName(u"frame_48")
        self.verticalLayout_74 = QVBoxLayout(self.frame_48)
        self.verticalLayout_74.setSpacing(5)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_48)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_92.setSpacing(15)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_52)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_92.addWidget(self.label_14)

        self.horizontalSpacer_21 = QSpacerItem(16, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_21)


        self.verticalLayout_74.addWidget(self.frame_52)

        self.comboBox_9 = QComboBox(self.frame_48)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.verticalLayout_74.addWidget(self.comboBox_9)


        self.horizontalLayout_54.addWidget(self.frame_48)

        self.electrumV2FromEntropyClientContainerQFrame = QFrame(self.electrumV2FromEntropyClientAndPassphraseContainerQFrame)
        self.electrumV2FromEntropyClientContainerQFrame.setObjectName(u"electrumV2FromEntropyClientContainerQFrame")
        self.electrumV2FromEntropyClientContainerQFrame.setMinimumSize(QSize(150, 0))
        self.ClientVLayout_13 = QVBoxLayout(self.electrumV2FromEntropyClientContainerQFrame)
        self.ClientVLayout_13.setSpacing(5)
        self.ClientVLayout_13.setObjectName(u"ClientVLayout_13")
        self.ClientVLayout_13.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyClientLabelContainerQFrame = QFrame(self.electrumV2FromEntropyClientContainerQFrame)
        self.electrumV2FromEntropyClientLabelContainerQFrame.setObjectName(u"electrumV2FromEntropyClientLabelContainerQFrame")
        self.MStrengthLabelHLayout_17 = QHBoxLayout(self.electrumV2FromEntropyClientLabelContainerQFrame)
        self.MStrengthLabelHLayout_17.setSpacing(15)
        self.MStrengthLabelHLayout_17.setObjectName(u"MStrengthLabelHLayout_17")
        self.MStrengthLabelHLayout_17.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyClientQLabel = QLabel(self.electrumV2FromEntropyClientLabelContainerQFrame)
        self.electrumV2FromEntropyClientQLabel.setObjectName(u"electrumV2FromEntropyClientQLabel")

        self.MStrengthLabelHLayout_17.addWidget(self.electrumV2FromEntropyClientQLabel)

        self.electrumV2FromEntropyClientLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_17.addItem(self.electrumV2FromEntropyClientLabelContainerQFrameHSpacer)


        self.ClientVLayout_13.addWidget(self.electrumV2FromEntropyClientLabelContainerQFrame)

        self.electrumV2FromEntropyClientQComboBox = QComboBox(self.electrumV2FromEntropyClientContainerQFrame)
        self.electrumV2FromEntropyClientQComboBox.addItem("")
        self.electrumV2FromEntropyClientQComboBox.addItem("")
        self.electrumV2FromEntropyClientQComboBox.addItem("")
        self.electrumV2FromEntropyClientQComboBox.addItem("")
        self.electrumV2FromEntropyClientQComboBox.addItem("")
        self.electrumV2FromEntropyClientQComboBox.addItem("")
        self.electrumV2FromEntropyClientQComboBox.setObjectName(u"electrumV2FromEntropyClientQComboBox")

        self.ClientVLayout_13.addWidget(self.electrumV2FromEntropyClientQComboBox)


        self.horizontalLayout_54.addWidget(self.electrumV2FromEntropyClientContainerQFrame)

        self.electrumV2FromEntropyPassphraseContainerQFrame = QFrame(self.electrumV2FromEntropyClientAndPassphraseContainerQFrame)
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


        self.verticalLayout_58.addWidget(self.electrumV2FromEntropyClientAndPassphraseContainerQFrame)

        self.electrumV2FromEntropyLanguageAndWordsContainerQFrame = QFrame(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromEntropyLanguageAndWordsContainerQFrame.setObjectName(u"electrumV2FromEntropyLanguageAndWordsContainerQFrame")
        self.horizontalLayout_56 = QHBoxLayout(self.electrumV2FromEntropyLanguageAndWordsContainerQFrame)
        self.horizontalLayout_56.setSpacing(15)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromEntropyLanguageContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageAndWordsContainerQFrame)
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

        self.electrumV2FromEntropyWordsContainerQFrame = QFrame(self.electrumV2FromEntropyLanguageAndWordsContainerQFrame)
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

        self.frame_49 = QFrame(self.electrumV2FromEntropyLanguageAndWordsContainerQFrame)
        self.frame_49.setObjectName(u"frame_49")
        self.verticalLayout_75 = QVBoxLayout(self.frame_49)
        self.verticalLayout_75.setSpacing(5)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_49)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_75.addWidget(self.label_21)

        self.comboBox_10 = QComboBox(self.frame_49)
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.verticalLayout_75.addWidget(self.comboBox_10)


        self.horizontalLayout_56.addWidget(self.frame_49)


        self.verticalLayout_58.addWidget(self.electrumV2FromEntropyLanguageAndWordsContainerQFrame)

        self.electrumV2QStackedWidget.addWidget(self.electrumV2FromEntropyQStackedWidget)
        self.electrumV2FromMnemonicQStackedWidget = QWidget()
        self.electrumV2FromMnemonicQStackedWidget.setObjectName(u"electrumV2FromMnemonicQStackedWidget")
        self.verticalLayout_60 = QVBoxLayout(self.electrumV2FromMnemonicQStackedWidget)
        self.verticalLayout_60.setSpacing(15)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.electrumV2FromMnemonicQStackedWidget)
        self.frame_28.setObjectName(u"frame_28")
        self.horizontalLayout_57 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_57.setSpacing(15)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicContainerQFrame = QFrame(self.frame_28)
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

        self.frame_84 = QFrame(self.frame_28)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_84)
        self.verticalLayout_71.setSpacing(5)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.frame_84)
        self.frame_86.setObjectName(u"frame_86")
        self.horizontalLayout_95 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_95.setSpacing(15)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_86)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_95.addWidget(self.label_13)

        self.horizontalSpacer_22 = QSpacerItem(49, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_22)


        self.verticalLayout_71.addWidget(self.frame_86)

        self.comboBox_6 = QComboBox(self.frame_84)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.verticalLayout_71.addWidget(self.comboBox_6)


        self.horizontalLayout_57.addWidget(self.frame_84)


        self.verticalLayout_60.addWidget(self.frame_28)

        self.electrumV2FromMnemonicClientAndPassphraseContainerQFrame = QFrame(self.electrumV2FromMnemonicQStackedWidget)
        self.electrumV2FromMnemonicClientAndPassphraseContainerQFrame.setObjectName(u"electrumV2FromMnemonicClientAndPassphraseContainerQFrame")
        self.horizontalLayout_58 = QHBoxLayout(self.electrumV2FromMnemonicClientAndPassphraseContainerQFrame)
        self.horizontalLayout_58.setSpacing(15)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.electrumV2FromMnemonicClientAndPassphraseContainerQFrame)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_41)
        self.verticalLayout_72.setSpacing(5)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_41)
        self.frame_85.setObjectName(u"frame_85")
        self.horizontalLayout_94 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_94.setSpacing(15)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_85)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_94.addWidget(self.label_32)

        self.horizontalSpacer_23 = QSpacerItem(49, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_23)


        self.verticalLayout_72.addWidget(self.frame_85)

        self.comboBox_7 = QComboBox(self.frame_41)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.verticalLayout_72.addWidget(self.comboBox_7)


        self.horizontalLayout_58.addWidget(self.frame_41)

        self.electrumV2FromMnemonicClientContainerQFrame = QFrame(self.electrumV2FromMnemonicClientAndPassphraseContainerQFrame)
        self.electrumV2FromMnemonicClientContainerQFrame.setObjectName(u"electrumV2FromMnemonicClientContainerQFrame")
        self.ClientVLayout_14 = QVBoxLayout(self.electrumV2FromMnemonicClientContainerQFrame)
        self.ClientVLayout_14.setSpacing(5)
        self.ClientVLayout_14.setObjectName(u"ClientVLayout_14")
        self.ClientVLayout_14.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicClientLabelContainerQFrame = QFrame(self.electrumV2FromMnemonicClientContainerQFrame)
        self.electrumV2FromMnemonicClientLabelContainerQFrame.setObjectName(u"electrumV2FromMnemonicClientLabelContainerQFrame")
        self.MStrengthLabelHLayout_18 = QHBoxLayout(self.electrumV2FromMnemonicClientLabelContainerQFrame)
        self.MStrengthLabelHLayout_18.setSpacing(15)
        self.MStrengthLabelHLayout_18.setObjectName(u"MStrengthLabelHLayout_18")
        self.MStrengthLabelHLayout_18.setContentsMargins(0, 0, 0, 0)
        self.electrumV2FromMnemonicClientQLabel = QLabel(self.electrumV2FromMnemonicClientLabelContainerQFrame)
        self.electrumV2FromMnemonicClientQLabel.setObjectName(u"electrumV2FromMnemonicClientQLabel")

        self.MStrengthLabelHLayout_18.addWidget(self.electrumV2FromMnemonicClientQLabel)

        self.electrumV2FromMnemonicClientLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MStrengthLabelHLayout_18.addItem(self.electrumV2FromMnemonicClientLabelContainerQFrameHSpacer)


        self.ClientVLayout_14.addWidget(self.electrumV2FromMnemonicClientLabelContainerQFrame)

        self.electrumV2FromMnemonicClientQComboBox = QComboBox(self.electrumV2FromMnemonicClientContainerQFrame)
        self.electrumV2FromMnemonicClientQComboBox.addItem("")
        self.electrumV2FromMnemonicClientQComboBox.addItem("")
        self.electrumV2FromMnemonicClientQComboBox.addItem("")
        self.electrumV2FromMnemonicClientQComboBox.addItem("")
        self.electrumV2FromMnemonicClientQComboBox.addItem("")
        self.electrumV2FromMnemonicClientQComboBox.addItem("")
        self.electrumV2FromMnemonicClientQComboBox.setObjectName(u"electrumV2FromMnemonicClientQComboBox")

        self.ClientVLayout_14.addWidget(self.electrumV2FromMnemonicClientQComboBox)


        self.horizontalLayout_58.addWidget(self.electrumV2FromMnemonicClientContainerQFrame)

        self.electrumV2FromMnemonicPassphraseContainerQFrame = QFrame(self.electrumV2FromMnemonicClientAndPassphraseContainerQFrame)
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


        self.verticalLayout_60.addWidget(self.electrumV2FromMnemonicClientAndPassphraseContainerQFrame)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_7)

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
        self.electrumV2FromSeedClientContainerQFrame = QFrame(self.electrumV2FromSeedContainerQFrame)
        self.electrumV2FromSeedClientContainerQFrame.setObjectName(u"electrumV2FromSeedClientContainerQFrame")
        self.horizontalLayout_61 = QHBoxLayout(self.electrumV2FromSeedClientContainerQFrame)
        self.horizontalLayout_61.setSpacing(15)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.electrumV2FromSeedClientContainerQFrame)
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

        self.frame_47 = QFrame(self.electrumV2FromSeedClientContainerQFrame)
        self.frame_47.setObjectName(u"frame_47")
        self.verticalLayout_73 = QVBoxLayout(self.frame_47)
        self.verticalLayout_73.setSpacing(5)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_47)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_73.addWidget(self.label_20)

        self.comboBox_8 = QComboBox(self.frame_47)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.verticalLayout_73.addWidget(self.comboBox_8)


        self.horizontalLayout_61.addWidget(self.frame_47)

        self.ClientQFrame_15 = QFrame(self.electrumV2FromSeedClientContainerQFrame)
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


        self.SeedVLayout_5.addWidget(self.electrumV2FromSeedClientContainerQFrame)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SeedVLayout_5.addItem(self.verticalSpacer_27)


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

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
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


        self.verticalLayout_12.addWidget(self.frame)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.horizontalLayout.addWidget(self.hdWalletContainerQFrame)

        self.outputQFrame = QFrame(self.centralwidget)
        self.outputQFrame.setObjectName(u"outputQFrame")
        self.outputQFrame.setMinimumSize(QSize(400, 0))
        self.verticalLayout_2 = QVBoxLayout(self.outputQFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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

        self.tabWidget.setCurrentIndex(1)
        self.hdQStackedWidget.setCurrentIndex(0)
        self.BIPQStackedWidget.setCurrentIndex(0)
        self.cardanoQStackedWidget.setCurrentIndex(5)
        self.electrumV1QStackedWidget.setCurrentIndex(5)
        self.electrumV2QStackedWidget.setCurrentIndex(2)
        self.moneroQStackedWidget.setCurrentIndex(2)
        self.DerivationsQTabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.donationHDWalletQPushButton.setText(QCoreApplication.translate("MainWindow", u"Donation", None))
        self.helpHDWalletQPushButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Client", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Strength", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.comboBox_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Client", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.comboBox_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Words", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.comboBox_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Language", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generateHDWalletTabQWidget), QCoreApplication.translate("MainWindow", u"Generate", None))
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

        self.cardanoFromEntropyClientQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.cardanoFromEntropyClientQComboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromEntropyClientQComboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromEntropyClientQComboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromEntropyClientQComboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromEntropyClientQComboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromEntropyClientQComboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.BIPFromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.BIPFromEntropyClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromEntropyClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.BIPFromEntropyClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.BIPFromEntropyClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.BIPFromEntropyClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.BIPFromEntropyClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.BIPFromEntropyClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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
        self.BIPFromMnemonicClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromMnemonicClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.BIPFromMnemonicClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.BIPFromMnemonicClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.BIPFromMnemonicClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.BIPFromMnemonicClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.BIPFromMnemonicClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.BIPFromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.BIPFromMnemonicPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.SeedQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.ClientQLabel_6.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.ClientQComboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.BIPFromPrivateKeyQLabel_3.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromXPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromWIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.BIPFromWIFBIP38PassphraseQCheckBox.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.BIPFromWIFBIP38PassphraseGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.BIPFromPrivateKeyQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.cardanoFromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.cardanoFromEntropyClientQLabel.setText(QCoreApplication.translate("MainWindow", u"cardano Type", None))
        self.cardanoFromEntropyClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromEntropyClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromEntropyClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromEntropyClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromEntropyClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromEntropyClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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

        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromEntropyWordsQLabel.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.cardanoFromEntropyWordsQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.cardanoFromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.ClientQLabel_8.setText(QCoreApplication.translate("MainWindow", u"cardano type", None))
        self.ClientQComboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_8.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_8.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_8.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.cardanoFromMnemonicPassphraseQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.cardanoFromEntropyLanguageQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.cardanoFromEntropyLanguageQComboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese Simplified", None))
        self.cardanoFromEntropyLanguageQComboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese Traditional", None))
        self.cardanoFromEntropyLanguageQComboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.cardanoFromEntropyLanguageQComboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.cardanoFromEntropyLanguageQComboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Italian", None))
        self.cardanoFromEntropyLanguageQComboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.cardanoFromEntropyLanguageQComboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.cardanoFromEntropyLanguageQComboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromEntropyWordsQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Words", None))
        self.cardanoFromEntropyWordsQComboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Words", None))
        self.cardanoFromEntropyWordsQComboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"15 Words", None))
        self.cardanoFromEntropyWordsQComboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"18 Words", None))
        self.cardanoFromEntropyWordsQComboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"21 Words", None))
        self.cardanoFromEntropyWordsQComboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"24 Words", None))

        self.cardanoFromSeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.ClientQLabel_9.setText(QCoreApplication.translate("MainWindow", u"cardano type", None))
        self.ClientQComboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_9.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_9.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_9.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromMnemonicPassphraseQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.cardanoFromMnemonicPassphraseQLineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.cardanoFromMnemonicPassphraseGenerateQPushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.cardanoFromXPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPrivate Key", None))
        self.ClientQLabel_12.setText(QCoreApplication.translate("MainWindow", u"Cardano Type", None))
        self.ClientQComboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_12.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_12.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_12.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromClientQLabel_4.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromClientQComboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromClientQComboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromClientQComboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromClientQComboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromClientQComboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromClientQComboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromXPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"XPublic Key", None))
        self.ClientQLabel_11.setText(QCoreApplication.translate("MainWindow", u"cardano type", None))
        self.ClientQComboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_11.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_11.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_11.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_11.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromClientQLabel_3.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromClientQComboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromClientQComboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromClientQComboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromClientQComboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromClientQComboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromClientQComboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromPrivateKeyContainerQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.ClientQLabel_10.setText(QCoreApplication.translate("MainWindow", u"cardano type", None))
        self.ClientQComboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_10.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_10.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_10.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_10.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromClientQLabel_2.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromClientQComboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromClientQComboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromClientQComboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromClientQComboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromClientQComboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromClientQComboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.ClientQLabel_13.setText(QCoreApplication.translate("MainWindow", u"cardano type", None))
        self.ClientQComboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_13.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_13.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_13.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_13.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.cardanoFromClientQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Address Type", None))
        self.cardanoFromClientQComboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.cardanoFromClientQComboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.cardanoFromClientQComboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.cardanoFromClientQComboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.cardanoFromClientQComboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.cardanoFromClientQComboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.electrumV1FromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.electrumV1FromEntropyClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromEntropyClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV1FromEntropyClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV1FromEntropyClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV1FromEntropyClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV1FromEntropyClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV1FromEntropyClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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
        self.electrumV1FromMnemonicClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromMnemonicClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV1FromMnemonicClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV1FromMnemonicClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV1FromMnemonicClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV1FromMnemonicClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV1FromMnemonicClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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
        self.electrumV1FromClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV1FromClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV1FromClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV1FromClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV1FromClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV1FromClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.electrumV1FromWIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Wallet Important Format", None))
        self.electrumV1FromWIFBIP38PassphraseQCheckBox.setText(QCoreApplication.translate("MainWindow", u"BIP38 Passphrase", None))
        self.electrumV1FromWIFBIP38PassphraseQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV1FromPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromEntropyQLabel.setText(QCoreApplication.translate("MainWindow", u"Entropy", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.electrumV2FromEntropyClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromEntropyClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV2FromEntropyClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV2FromEntropyClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV2FromEntropyClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV2FromEntropyClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV2FromEntropyClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Mnemonic Type", None))
        self.electrumV2FromMnemonicQLabel.setText(QCoreApplication.translate("MainWindow", u"Mnemonic", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Mnemonic Type", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.comboBox_7.setPlaceholderText("")
        self.electrumV2FromMnemonicClientQLabel.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.electrumV2FromMnemonicClientQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.electrumV2FromMnemonicClientQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.electrumV2FromMnemonicClientQComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.electrumV2FromMnemonicClientQComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.electrumV2FromMnemonicClientQComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.electrumV2FromMnemonicClientQComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

        self.electrumV2FromMnemonicPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.electrumV2FromMnemonicPassphraseGenerateQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Optional)", None))
        self.SeedQLabel_5.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.ClientQLabel_15.setText(QCoreApplication.translate("MainWindow", u"Public Key Type", None))
        self.ClientQComboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"Algorand", None))
        self.ClientQComboBox_15.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP39", None))
        self.ClientQComboBox_15.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardano", None))
        self.ClientQComboBox_15.setItemText(3, QCoreApplication.translate("MainWindow", u"Electrum V1", None))
        self.ClientQComboBox_15.setItemText(4, QCoreApplication.translate("MainWindow", u"Electrum V2", None))
        self.ClientQComboBox_15.setItemText(5, QCoreApplication.translate("MainWindow", u"Monero", None))

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
        self.XPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None))
        self.XPublicKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Spend Private Key", None))
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
        self.FormatLabelQLabel.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.FormatQComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"JSON", None))
        self.FormatQComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CSV", None))

        self.KeysQLabel.setText(QCoreApplication.translate("MainWindow", u"Keys", None))
        self.GenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Dumps", None))
    # retranslateUi

