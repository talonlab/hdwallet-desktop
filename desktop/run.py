import os
import subprocess
import string
import json
import functools

from collections import OrderedDict
from random import choice
from typing import *

from PySide6.QtWidgets import (
    QPushButton, QLineEdit, QLayout, QWidget, QApplication, QMainWindow, QFileDialog, QTextEdit, QPlainTextEdit
)
from PySide6.QtCore import QSize, QThreadPool, QEvent
from PySide6.QtGui import QGuiApplication
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QPushButton, QVBoxLayout, QHBoxLayout, QFrame,
    QStackedWidget, QSizePolicy
)
from PySide6.QtCore import QFile, Qt, QRect, QObject, QRegularExpression
from PySide6.QtGui import (
    QIntValidator, QFont, QFontDatabase, QSyntaxHighlighter,
    QTextCharFormat, QColor, QTextCursor
)
import string

from hdwallet import HDWallet
from hdwallet.hds import HDS

from hdwallet.entropies import (
    AlgorandEntropy, ALGORAND_ENTROPY_STRENGTHS,
    BIP39Entropy, BIP39_ENTROPY_STRENGTHS,
    ElectrumV1Entropy, ELECTRUM_V1_ENTROPY_STRENGTHS,
    ElectrumV2Entropy, ELECTRUM_V2_ENTROPY_STRENGTHS,
    MoneroEntropy, MONERO_ENTROPY_STRENGTHS,
    ENTROPIES
)

from hdwallet.mnemonics import (
    AlgorandMnemonic, ALGORAND_MNEMONIC_WORDS, ALGORAND_MNEMONIC_LANGUAGES,
    BIP39Mnemonic, BIP39_MNEMONIC_WORDS, BIP39_MNEMONIC_LANGUAGES,
    ElectrumV1Mnemonic, ELECTRUM_V1_MNEMONIC_WORDS, ELECTRUM_V1_MNEMONIC_LANGUAGES,
    ElectrumV2Mnemonic, ELECTRUM_V2_MNEMONIC_WORDS, ELECTRUM_V2_MNEMONIC_LANGUAGES, ELECTRUM_V2_MNEMONIC_TYPES,
    MoneroMnemonic, MONERO_MNEMONIC_WORDS, MONERO_MNEMONIC_LANGUAGES,
    MNEMONICS
)

from hdwallet.derivations import (
    IDerivation, DERIVATIONS,
    CustomDerivation, BIP44Derivation, BIP49Derivation, BIP84Derivation,
    BIP86Derivation, ElectrumDerivation, CIP1852Derivation, MoneroDerivation,
    CHANGES
)
7
from hdwallet.const import (
    ELECTRUM_V2_MODES
)

from hdwallet.cryptocurrencies import Cardano, CRYPTOCURRENCIES

from hdwallet.seeds import (
    AlgorandSeed,
    BIP39Seed,
    CardanoSeed,
    ElectrumV1Seed,
    ElectrumV2Seed,
    MoneroSeed,
    SEEDS
)

from ui.ui_hdwallet import Ui_MainWindow
from widget.SvgButton import SvgButton
from file_saver import FileSaver
from worker import Worker, WorkerSignals
from validator import Validator
from donation import Donation

def clear_layout(layout: QLayout, delete: bool = True) -> None:
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None and delete:
                widget.deleteLater()
            else:
                clear_layout(item.layout())


def put_svg(layout: QLayout, path: str, width: int, height: int) -> QSvgWidget:
    clear_layout(layout)
    svg = QSvgWidget(path)
    svg.setMinimumSize(QSize(width, height))
    svg.setMaximumSize(QSize(width, height))
    svg.setStyleSheet("background: transparent")
    layout.addWidget(svg)
    return svg

def clear_text_area(text_edit):
    text_edit.clear()

class DetachedWindow(QWidget):
    def __init__(self, p):
        super().__init__()
        self.main_window = p

    def closeEvent(self, event):
        self.main_window.toggle_expand_terminal.setChecked(False)
        self.main_window.toggle_expand()
        self.update_terminal_ui()

    def changeEvent(self, event):
        super().changeEvent(event)
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self.update_terminal_ui()
            elif self.windowState() == Qt.WindowNoState:
                self.update_terminal_ui()

    def update_terminal_ui(self):
        try:
            noLayoutQWidget: QWidget = self.layout().itemAt(0).widget().findChild(QWidget, "noLayoutQWidget")
            outputWidgetTopContainerQWidget: QWidget = self.layout().itemAt(0).widget().findChild(QWidget,
                                                                                                  "outputWidgetTopContainerQWidget")
            outputTerminalQWidget: QWidget = self.layout().itemAt(0).widget().findChild(QWidget, "outputTerminalQWidget")
            outputWidgetTopContainerQFrame: QFrame = self.layout().itemAt(0).widget().findChild(QFrame,
                                                                                                "outputWidgetTopContainerQFrame")
            outputTerminalQPlainTextEdit: QPlainTextEdit = self.layout().itemAt(0).widget().findChild(QPlainTextEdit,
                                                                                                "outputTerminalQPlainTextEdit")
            outputWidgetTopContainerQWidget.setGeometry(QRect(
                (
                    noLayoutQWidget.width() - (
                        outputWidgetTopContainerQFrame.width() + (
                            20 if outputTerminalQPlainTextEdit.verticalScrollBar().maximum() > 0 else 10
                        )
                    )
                ), 0,
                outputWidgetTopContainerQFrame.width(), outputWidgetTopContainerQWidget.height()
            ))
            outputTerminalQWidget.setGeometry(QRect(
                0, 0, noLayoutQWidget.width(), noLayoutQWidget.height()
            ))
            outputWidgetTopContainerQWidget.raise_()
            outputTerminalQWidget.lower()
        except AttributeError:
            pass

    def resizeEvent(self, event) -> None:
        self.update_terminal_ui()

    def show(self):
        super(DetachedWindow, self).show()
        self.update_terminal_ui()

    def center_window(self):
        # Get the screen resolution from the application
        screen = self.screen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
        self.update_terminal_ui()

class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []

    def add_highlighting_rule(self, pattern, char_format):
        self.highlighting_rules.append((QRegularExpression(pattern), char_format))

    def highlightBlock(self, text):
        for pattern, char_format in self.highlighting_rules:
            matcher = pattern.globalMatch(text)
            while matcher.hasNext():
                match = matcher.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), char_format)

class LogHighlighter(Highlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Punctuation highlighting
        punctuation_format = QTextCharFormat()
        punctuation_format.setForeground(QColor(255, 255, 255))
        self.add_highlighting_rule(r'[^\w\s]', punctuation_format)

        # Digit highlighting
        digit_format = QTextCharFormat()
        digit_format.setForeground(QColor(0, 120, 215))
        self.add_highlighting_rule(r'\b\d+\b', digit_format)

        # Character highlighting
        character_format = QTextCharFormat()
        character_format.setForeground(QColor(6, 240, 111))
        self.add_highlighting_rule(r'\b[a-zA-Z]+\b', character_format)

        # Values within single or double quotes
        quoted_value_format = QTextCharFormat()
        quoted_value_format.setForeground(QColor(6, 240, 111))
        self.add_highlighting_rule(r'["\'].*?["\']', quoted_value_format)

        # Highlight lines starting with "ERROR:"
        error_format = QTextCharFormat()
        error_format.setForeground(QColor(255, 96, 96))
        self.add_highlighting_rule(r'^ERROR:.*$', error_format)

class CoreApp(QMainWindow):
    def changeEvent(self, event):
        super().changeEvent(event)
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self.update_terminal_ui()
            elif self.windowState() == Qt.WindowNoState:
                self.update_terminal_ui()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.detached_window = None

        QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), "ui/font/HD Wallet-Regular.ttf"))

        # Setup UI Stuff
        self.setWindowTitle("Hierarchical Deterministic Wallet")

        self.load_stylesheet(os.path.join(os.path.dirname(__file__), "ui/css/dark-style.css"))

        put_svg(self.ui.hdwalletLogoHLayout, os.path.join(os.path.dirname(__file__), "ui/images/11.svg"), 132.04, 45)

        self.toggle_expand_terminal = SvgButton(
            parent_widget=self.ui.expandAndCollapseTerminalQFrame,
            icon_path=os.path.join(os.path.dirname(__file__), "ui/images/all_Icons/expand-white-thin.svg"),
            alt_icon_path=os.path.join(os.path.dirname(__file__), "ui/images/all_Icons/collapse-white-thin.svg"),
            icon_width=20,
            icon_height=20
        )
        self.toggle_expand_terminal.setCheckable(True)
        self.toggle_expand_terminal.toggled.connect(self.toggle_expand)
        self.ui.outputTerminalQLineEdit.returnPressed.connect(self.process_command)
        self.ui.outputTerminalQPushButton.clicked.connect(self.process_command)
        self.ui.outputTerminalQPlainTextEdit.textChanged.connect(self.update_terminal_ui)

        self.ui.generateQPushButton.clicked.connect(
            lambda: self.change_page("hdwalletQStackedWidget", "generatePageQStackedWidget"),
        )
        self.ui.dumpQPushButton.clicked.connect(
            lambda: self.change_page("hdwalletQStackedWidget", "dumpsPageQStackedWidget"))

        self.ui.generateEntropyClientContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.generateSeedMnemonicContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.generateLengthContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        LogHighlighter(self.ui.outputTerminalQPlainTextEdit.document())

        self.ui.dumpsSaveAndGenerateQPushButton.clicked.connect(
            lambda: self._dumps(save=True)
        )

        self.ui.clearTerminalQPushButton.clicked.connect(lambda: clear_text_area(self.ui.outputTerminalQPlainTextEdit))

        self.ui.generateQPushButton.clicked.connect(
            functools.partial(self.generate_dump_tab_changed, "generatePageQStackedWidget", self.ui.generateQPushButton)
        )

        self.ui.dumpQPushButton.clicked.connect(
            functools.partial(self.generate_dump_tab_changed, "dumpsPageQStackedWidget", self.ui.dumpQPushButton)
        )

        self.ui.dumpQPushButton.click()
        vali= [
            self.ui.bip44AccountQLineEdit,
            self.ui.bip44AddressQLineEdit,
            self.ui.bip49AccountQLineEdit,
            self.ui.bip49AddressQLineEdit,
            self.ui.bip84AccountQLineEdit,
            self.ui.bip84AddressQLineEdit,
            self.ui.bip86AccountQLineEdit,
            self.ui.bip86AddressQLineEdit,
            self.ui.cip1852AccountQLineEdit,
            self.ui.cip1852AddressQLineEdit,
            self.ui.electrumChangeQLineEdit,
            self.ui.electrumAddressQLineEdit,
            self.ui.moneroMinorQLineEdit,
            self.ui.moneroMajorQLineEdit
        ]
        Validator.validate_input(vali)

        self.ui.donationHDWalletQPushButton.clicked.connect(lambda: Donation.show_donation(self.window()))

        self._setup_generate_stack()
        self._setup_dump_stack()

    def _setup_dump_stack(self):

        self.script_semantics = ["P2WPKH", "P2WPKH_IN_P2SH", "P2WSH", "P2WSH_IN_P2SH"]

        self.stack_hd_widgets = {
            'BIP32': "bipsPageQWidget",
            'BIP44': "bipsPageQWidget",
            'BIP49': "bipsPageQWidget",
            'BIP84': "bipsPageQWidget",
            'BIP86': "bipsPageQWidget",
            'BIP141': "bipsPageQWidget",
            'Cardano': "cardanoPageQWidget",
            'Electrum-V1': "electrumV1PageQWidget",
            'Electrum-V2': "electrumV2PageQWidget",
            'Monero': "moneroPageQWidget"
        }

        self.hd_drivable_methods = {
            'BIP32': ["Entropy", "Mnemonic", "Seed", "XPrivate key", "XPublic key"],
            'BIP44': ["Entropy", "Mnemonic", "Seed", "XPrivate key", "XPublic key"],
            'BIP49': ["Entropy", "Mnemonic", "Seed", "XPrivate key", "XPublic key"],
            'BIP84': ["Entropy", "Mnemonic", "Seed", "XPrivate key", "XPublic key"],
            'BIP86': ["Entropy", "Mnemonic", "Seed", "XPrivate key", "XPublic key"],
            'BIP141': ["Entropy", "Mnemonic", "Seed", "XPrivate key", "XPublic key"],
            'Electrum-V1': ["Entropy", "Mnemonic", "Private key", "Public key", "Seed", "WIF"],
            'Electrum-V2': ["Entropy", "Mnemonic", "Seed"],
            'Cardano': ["Entropy", "Mnemonic", "Seed", "XPrivate key", "XPublic key"],
            'Monero': ["Entropy", "Mnemonic", "Private key", "Seed", "Spend private key", "Watch only"]
        }

        self.hd_allowed_derivation = {
            'BIP32': ["Custom", "BIP44", "BIP49", "BIP84", "BIP86", "BIP141", "CIP1852"],
            'BIP32XPUB': ["Custom", "BIP141"],
            'BIP44': ["BIP44"],
            'BIP49': ["BIP49"],
            'BIP84': ["BIP84"],
            'BIP86': ["BIP86"],
            'BIP141': ["BIP141"],
            'Cardano': ["Custom", "BIP44", "CIP1852"],
            'CardanoXPUB': ["Custom"],
            'Electrum-V1': ["Electrum"],
            'Electrum-V2': ["Electrum"],
            'Monero': ["Monero"]
        }

        self.derivation_tab = OrderedDict()

        self.derivation_tab["Custom"] = {
            "button": self.ui.customTabQPushButton,
            "widget": "customQStackedWidgetPage",
        }

        self.derivation_tab["BIP44"] = {
            "button": self.ui.bip44TabQPushButton,
            "widget": "bip44QStackedWidgetPage",
        }

        self.derivation_tab["BIP49"] = {
            "button": self.ui.bip49TabQPushButton,
            "widget": "bip49QStackedWidgetPage",
        }

        self.derivation_tab["BIP84"] = {
            "button": self.ui.bip84TabQPushButton,
            "widget": "bip84QStackedWidgetPage",
        }

        self.derivation_tab["BIP86"] = {
            "button": self.ui.bip86TabQPushButton,
            "widget": "bip86QStackedWidgetPage",
        }

        self.derivation_tab["BIP141"] = {
            "button": self.ui.bip141TabQPushButton,
            "widget": "bip141QStackedWidgetPage",
        }

        self.derivation_tab["CIP1852"] = {
            "button": self.ui.cip1852TabQPushButton,
            "widget": "cip1852QStackedWidgetPage",
        }

        self.derivation_tab["Electrum"] = {
            "button": self.ui.electrumTabQPushButton,
            "widget": "electrumQStackedWidgetPage",
        }

        self.derivation_tab["Monero"] = {
            "button": self.ui.moneroTabQPushButton,
            "widget": "moneroQStackedWidgetPage",
        }

        self.stack_from_widgets = {
            "bipsPageQWidget": {
                "StackWidget": "bipQStackedWidget",
                "Entropy": "bipFromEntropyQStackedWidget",
                "Mnemonic": "bipFromMnemonicQStackedWidget",
                "Private key": "bipFromPrivateKeyQStackedWidget",
                "Public key": "bipFromPublicKeyQStackedWidget",
                "Seed": "bipFromSeedQStackedWidget",
                "WIF": "bipFromWIFQStackedWidget",
                "XPrivate key": "bipFromXPrivateKeyQStackedWidget",
                "XPublic key": "bipFromXPublicKeyQStackedWidget"
            },
            "cardanoPageQWidget": {
                "StackWidget": "cardanoQStackedWidget",
                "Entropy": "cardanoFromEntropyQStackedWidget",
                "Mnemonic": "cardanoFromMnemonicQStackedWidget",
                "Private key": "cardanoFromPrivateKeyQStackedWidget",
                "Public key": "cardanoFromPublicKeyQStackedWidget",
                "Seed": "cardanoFromSeedQStackedWidget",
                "XPrivate key": "cardanoFromXPrivateKeyQStackedWidget",
                "XPublic key": "cardanoFromXPublicKeyQStackedWidget"
            },
            "electrumV1PageQWidget": {
                "StackWidget": "electrumV1QStackedWidget",
                "Entropy": "electrumV1FromEntropyQStackedWidget",
                "Mnemonic": "electrumV1FromMnemonicQStackedWidget",
                "Private key": "electrumV1FromPrivateKeyQStackedWidget",
                "Public key": "electrumV1FromPublicKeyQStackedWidget",
                "Seed": "electrumV1FromSeedQStackedWidget",
                "WIF": "electrumV1FromWIFQStackedWidget",
            },
            "electrumV2PageQWidget": {
                "StackWidget": "electrumV2QStackedWidget",
                "Entropy": "electrumV2FromEntropyQStackedWidget",
                "Mnemonic": "electrumV2FromMnemonicQStackedWidget",
                "Seed": "electrumV2FromSeedQStackedWidget",
            },
            "moneroPageQWidget": {
                "StackWidget": "moneroQStackedWidget",
                "Entropy": "moneroFromEntropyQStackedWidget",
                "Mnemonic": "moneroFromMnemonicQStackedWidget",
                "Private key": "moneroFromPrivateKeyQStackedWidget",
                "Seed": "moneroFromSeedQStackedWidget",
                "Spend private key": "moneroFromSpendPrivateKeyQStackedWidget",
                "Watch only": "moneroFromWatchOnlyQStackedWidget",
            }
        }

        for name, data in self.derivation_tab.items():
            data["button"].clicked.connect(
                functools.partial(self.derivation_tab_changed, data["widget"], data["button"]))

        self.ui.dumpsExcludeOrIncludeQLabel.setText("Exclude")
        self.ui.dumpsFormatQComboBox.currentIndexChanged.connect(self._dump_format_changed)

        self.ui.dumpsHdQComboBox.currentIndexChanged.connect(self._dump_hd_changed)
        self.ui.dumpsFromQComboBox.currentIndexChanged.connect(self._dump_from_changed)

        self.ui.dumpsCryptocurrencyQComboBox.clear()
        self.ui.dumpsCryptocurrencyQComboBox.addItems(CRYPTOCURRENCIES.names())
        self.ui.dumpsCryptocurrencyQComboBox.currentIndexChanged.connect(self._dumps_crypto_change)
        self.ui.dumpsCryptocurrencyQComboBox.setCurrentText("Bitcoin")

        self.ui.bipFromEntropyLanguageQComboBox.clear()
        self.ui.bipFromEntropyLanguageQComboBox.addItems([i.title() for i in BIP39Mnemonic.languages])
        self.ui.bipFromEntropyLanguageQComboBox.setCurrentText("English")

        self.ui.bipFromEntropyLanguageQComboBox.clear()
        self.ui.bipFromEntropyLanguageQComboBox.addItems([i.title() for i in BIP39Mnemonic.languages])
        self.ui.bipFromEntropyLanguageQComboBox.setCurrentText("English")

        self.ui.cardanoFromEntropyLanguageQComboBox.clear()
        self.ui.cardanoFromEntropyLanguageQComboBox.addItems([i.title() for i in BIP39Mnemonic.languages])
        self.ui.cardanoFromEntropyLanguageQComboBox.setCurrentText("English")

        self.ui.electrumV2FromEntropyLanguageQComboBox.clear()
        self.ui.electrumV2FromEntropyLanguageQComboBox.addItems([i.title() for i in ElectrumV2Mnemonic.languages])
        self.ui.electrumV2FromEntropyLanguageQComboBox.setCurrentText("English")

        self.ui.moneroFromEntropyLanguageQComboBox.clear()
        self.ui.moneroFromEntropyLanguageQComboBox.addItems([i.title() for i in MoneroMnemonic.languages])
        self.ui.moneroFromEntropyLanguageQComboBox.setCurrentText("English")

        self.ui.electrumV2FromEntropyMnemonicTypeQComboBox.addItems(
            [i.title() for i in ElectrumV2Mnemonic.mnemonic_types.keys()])
        self.ui.electrumV2FromEntropyModeQComboBox.addItems([i.title() for i in ELECTRUM_V2_MODES.get_modes()])
        self.ui.electrumV2FromEntropyMnemonicTypeQComboBox.setCurrentIndex(0)
        self.ui.electrumV2FromEntropyModeQComboBox.setCurrentIndex(0)

        self.ui.electrumV2FromMnemonicMnemonicTypeQComboBox.addItems(
            [i.title() for i in ElectrumV2Mnemonic.mnemonic_types.keys()])
        self.ui.electrumV2FromMnemonicModeQComboBox.addItems([i.title() for i in ELECTRUM_V2_MODES.get_modes()])
        self.ui.electrumV2FromMnemonicMnemonicTypeQComboBox.setCurrentIndex(0)
        self.ui.electrumV2FromMnemonicModeQComboBox.setCurrentIndex(0)

        self.ui.electrumV2FromSeedModeQComboBox.addItems([i.title() for i in ELECTRUM_V2_MODES.get_modes()])
        self.ui.electrumV2FromSeedModeQComboBox.setCurrentIndex(0)

        cardano_and_address_type = [
            (
                self.ui.cardanoFromEntropyCardanoTypeQComboBox,
                self.ui.cardanoFromEntropyAddressTypeQComboBox,
                self.ui.cardanoFromEntropyStakingQLineEdit
            ),
            (
                self.ui.cardanoFromMnemonicCardanoTypeQComboBox,
                self.ui.cardanoFromMnemonicAddressTypeQComboBox,
                self.ui.cardanoFromMnemonicStakingQLineEdit
            ),
            (
                self.ui.cardanoFromPrivateKeyCardanoTypeQComboBox,
                self.ui.cardanoFromPrivateKeyAddressTypeQComboBox,
                self.ui.cardanoFromPrivateKeyStakingQLineEdit
            ),
            (
                self.ui.cardanoFromPublicKeyCardanoTypeQComboBox,
                self.ui.cardanoFromPublicKeyAddressTypeQComboBox,
                self.ui.cardanoFromPublicKeyStakingQLineEdit
            ),
            (
                self.ui.cardanoFromSeedCardanoTypeQComboBox,
                self.ui.cardanoFromSeedAddressTypeQComboBox,
                self.ui.cardanoFromSeedStakingQLineEdit
            ),
            (
                self.ui.cardanoFromXPrivateKeyCardanoTypeQComboBox,
                self.ui.cardanoFromXPrivateKeyAddressTypeQComboBox,
                self.ui.cardanoFromXPrivateKeyStakingQLineEdit
            ),
            (
                self.ui.cardanoFromXPublicKeyCardanoTypeQComboBox,
                self.ui.cardanoFromXPublicKeyAddressTypeQComboBox,
                self.ui.cardanoFromXPublicKeyStakingQLineEdit
            ),
        ]

        cardano_list = [i.title() for i in Cardano.TYPES.get_cardano_types()]
        c_address_list = ["Payment", "Staking"]

        for pair in cardano_and_address_type:
            pair[0].clear()
            pair[1].clear()
            pair[0].addItems(cardano_list)
            pair[1].addItems(c_address_list)
            pair[0].currentIndexChanged.connect(functools.partial(self.__pair_ca_address_type, pair[1], pair[0]))
            pair[1].currentIndexChanged.connect(functools.partial(self.__pair_addr_staking, pair[1], pair[2]))
            pair[2].setEnabled(False)
            pair[0].setCurrentIndex(0)

        self.ui.dumpsGenerateQPushButton.clicked.connect(self._dumps)

    def __pair_ca_address_type(self, c_addr, c_list, idx):
        if c_list.currentText().lower().startswith("shelley"):
            c_addr.setEnabled(True)
            c_addr.setCurrentIndex(0)
        else:
            c_addr.setCurrentIndex(-1)
            c_addr.setEnabled(False)

    def __pair_addr_staking(self, c_addr, staking, idx):
        if c_addr.currentText() == "Payment":
            staking.setEnabled(True)
        else:
            staking.setText(None)
            staking.setEnabled(False)

    def _dumps(self, save=False):
        save_filepath = None
        if save:
            save_filepath = FileSaver.save_file(self.ui.dumpsFormatQComboBox.currentText())
            if save_filepath == '': return None

        def _error(e): 
            self.println(f"ERROR: {e}")
        
        def _enable_generate(): 
            self.ui.dumpsGenerateQPushButton.setEnabled(True)

        self.ui.dumpsGenerateQPushButton.setEnabled(False)

        mysignals = WorkerSignals()
        job = Worker(self.__dumps, signal=mysignals, save_filepath=save_filepath)
        job.signals = mysignals

        job.signals.interval_output.connect(self.println)

        job.signals.interval_error.connect(_error)
        job.signals.interval_finished.connect(self.println)
        job.signals.interval_error.connect(_enable_generate)
        job.signals.interval_finished.connect(_enable_generate)

        QThreadPool.globalInstance().start(job)

    def __dumps(self, signal, save_filepath):
        current_hd = self.ui.dumpsHdQComboBox.currentText()
        dump_from = self.ui.dumpsFromQComboBox.currentText()
        network = self.ui.dumpsNetworkQComboBox.currentText()
        exclude_set = set([p.strip() for p in self.ui.dumpsExcludeOrIncludeQLineEdit.text().split(",")])

        if save_filepath != None:
            saved_file = open(save_filepath, 'w')

        crypto = self.ui.dumpsCryptocurrencyQComboBox.currentText()

        hd_kwargs = {
            "cryptocurrency": CRYPTOCURRENCIES.cryptocurrency(crypto),
            "hd": HDS.hd(current_hd),
            "network": network.lower()
        }

        if current_hd in ('BIP32', 'BIP44', 'BIP49', 'BIP84', 'BIP86', 'BIP141'):
            if current_hd == 'BIP141':
                semantic_indx = self.ui.bip141ScriptSemanticsQComboBox.currentIndex()
                hd_kwargs["semantic"] = self.script_semantics[semantic_indx]
            hd = self._dump_bips(dump_from, hd_kwargs)
        elif current_hd == 'Cardano':
            hd = self._dump_cardano(dump_from, hd_kwargs)
        elif current_hd == 'Electrum-V1':
            hd = self._dump_ev1(dump_from, hd_kwargs)
        elif current_hd == 'Electrum-V2':
            hd = self._dump_ev2(dump_from, hd_kwargs)
        elif current_hd == 'Monero':
            hd = self._dump_monero(dump_from, hd_kwargs)

        derivation = None
        if self.ui.derivationQGroupBox.isEnabled():
            derivation = self.__dumps_get_derivation(CRYPTOCURRENCIES.cryptocurrency(crypto))

        if self.ui.dumpsFormatQComboBox.currentText() == "CSV":
            def drive(*args) -> List[str]:
                def drive_helper(derivations, current_derivation: List[Tuple[int, bool]] = []) -> List[str]:
                    if not derivations:

                        derivation_name: str = derivation.name()
                        if derivation_name in [
                            "BIP44", "BIP49", "BIP84", "BIP86"
                        ]:
                            _derivation: IDerivation = DERIVATIONS.derivation(
                                name=derivation_name
                            ).__call__(
                                coin_type=current_derivation[1][0],
                                account=current_derivation[2][0],
                                change=current_derivation[3][0],
                                address=current_derivation[4][0]
                            )
                        elif derivation_name == "CIP1852":
                            _derivation: IDerivation = DERIVATIONS.derivation(
                                name=derivation_name
                            ).__call__(
                                coin_type=current_derivation[1][0],
                                account=current_derivation[2][0],
                                role=current_derivation[3][0],
                                address=current_derivation[4][0]
                            )
                        elif derivation_name == 'Electrum':
                            _derivation: IDerivation = DERIVATIONS.derivation(
                                name=derivation_name
                            ).__call__(
                                change=current_derivation[0][0],
                                address=current_derivation[1][0]
                            )
                        elif derivation_name == "Monero":
                            _derivation: IDerivation = DERIVATIONS.derivation(
                                name=derivation_name
                            ).__call__(
                                minor=current_derivation[0][0],
                                major=current_derivation[1][0]
                            )
                        else:
                            _derivation: IDerivation = DERIVATIONS.derivation(
                                name=derivation_name
                            ).__call__(
                                path="m/" + "/".join(
                                    [str(item[0]) + "'" if item[1] else str(item[0]) for item in current_derivation]
                                )
                            )

                        csv_data: List[str] = []
                        hd.update_derivation(
                            derivation=_derivation
                        )
                        dump: dict = hd.dump(exclude={"root"})
                        for key in [keys.split(":") for keys in self.ui.dumpsExcludeOrIncludeQLineEdit.text().split(",")]:
                            if len(key) == 2:
                                csv_data.append(dump[key[0]][key[1]])
                            else:
                                csv_data.append(dump[key[0]])
                        csv_out = ", ".join(csv_data)
                        signal.interval_output.emit(csv_out)
                        if save_filepath != None:
                            saved_file.write(f"{csv_out}\n")
                        return [_derivation.path()]

                    path: List[str] = []
                    if len(derivations[0]) == 3:
                        for value in range(derivations[0][0], derivations[0][1] + 1):
                            path += drive_helper(
                                derivations[1:], current_derivation + [(value, derivations[0][2])]
                            )
                    else:
                        path += drive_helper(
                            derivations[1:], current_derivation + [derivations[0]]
                        )
                    return path

                return drive_helper(args)

            if derivation is None:
                return None

            drive(*derivation.derivations())
            if save_filepath != None:
                saved_file.close()

        else:
            if derivation != None:
                hd = hd.from_derivation(derivation=derivation)
                result = json.dumps(hd.dumps(exclude=exclude_set), indent=4, ensure_ascii=False)
            else:
                result = json.dumps(hd.dump(exclude=exclude_set), indent=4, ensure_ascii=False)

            if save_filepath != None:
                saved_file.write(result)
                saved_file.close()
            return result


    def __selected_dervation_name(self):
        current_widget = self.ui.derivationsQStackedWidget.currentWidget().objectName()
        for name, data in self.derivation_tab.items():
            if data["widget"] == current_widget:
                return name
        return None

    def __dumps_get_derivation(self, crypto):
        current_tab = self.__selected_dervation_name()

        if current_tab == "Custom":
            return CustomDerivation(
                path=self.ui.customPathQLineEdit.text()
            )
        elif current_tab == "BIP44":
            return BIP44Derivation(
                coin_type=crypto.COIN_TYPE,
                account=self.ui.bip44AccountQLineEdit.text(),
                change=f"{self.ui.bip44ChangeQComboBox.currentText().lower()}-chain",
                address=self.ui.bip44AddressQLineEdit.text()
            )
        elif current_tab == "BIP49":
            return BIP49Derivation(
                coin_type=crypto.COIN_TYPE,
                account=self.ui.bip49AccountQLineEdit.text(),
                change=f"{self.ui.bip49ChangeQComboBox.currentText().lower()}-chain",
                address=self.ui.bip49AddressQLineEdit.text()
            )
        elif current_tab == "BIP84":
            return BIP84Derivation(
                coin_type=crypto.COIN_TYPE,
                account=self.ui.bip84AccountQLineEdit.text(),
                change=f"{self.ui.bip84ChangeQComboBox.currentText().lower()}-chain",
                address=self.ui.bip84AddressQLineEdit.text()
            )
        elif current_tab == "BIP86":
            return BIP86Derivation(
                coin_type=crypto.COIN_TYPE,
                account=self.ui.bip86AccountQLineEdit.text(),
                change=f"{self.ui.bip86ChangeQComboBox.currentText().lower()}-chain",
                address=self.ui.bip86AddressQLineEdit.text()
            )
        elif current_tab == "BIP141":
            return CustomDerivation(
                path=self.ui.bip141PathQLineEdit.text()
            )

        elif current_tab == "CIP1852":
            role = self.ui.cip1852ChangeQComboBox.currentText().lower()
            postfix = "key" if role == "staking" else "chain"
            return CIP1852Derivation(
                coin_type=crypto.COIN_TYPE,
                account=self.ui.cip1852AccountQLineEdit.text(),
                role=f"{role}-{postfix}",
                address=self.ui.cip1852AddressQLineEdit.text()
            )

        elif current_tab == "Electrum":
            return ElectrumDerivation(
                change=self.ui.electrumChangeQLineEdit.text(),
                address=self.ui.electrumAddressQLineEdit.text(),
            )

        elif current_tab == "Monero":
            return MoneroDerivation(
                minor=self.ui.moneroMinorQLineEdit.text(),
                major=self.ui.moneroMajorQLineEdit.text()
            )

    def _dump_bips(self, dump_from, hd_kwargs):
        if dump_from == "Entropy":
            hd_kwargs["language"] = self.ui.bipFromEntropyLanguageQComboBox.currentText().lower()
            hd_kwargs["passphrase"] = self.ui.bipFromEntropyPassphraseQLineEdit.text()
            hd_kwargs["public_key_type"] = self.ui.bipFromEntropyPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_entropy(
                BIP39Entropy(
                    entropy=self.ui.bipFromEntropyGenerateQLineEdit.text()
                )
            )
        elif dump_from == "Mnemonic":
            hd_kwargs["passphrase"] = self.ui.bipFromMnemonicPassphraseQLineEdit.text()
            hd_kwargs["public_key_type"] = self.ui.bipFromMnemonicPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_mnemonic(
                BIP39Mnemonic(
                    mnemonic=self.ui.bipFromMnemonicQLineEdit.text()
                )
            )
        elif dump_from == "Private key":
            hd_kwargs["public_key_type"] = self.ui.bipFromMnemonicPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_private_key(
                private_key=self.ui.bipFromPrivateKeyQLineEdit.text()
            )
        elif dump_from == "Public key":
            hd_kwargs["public_key_type"] = self.ui.bipFromPublicKeyPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_public_key(
                public_key=self.ui.bipFromPublicKeyQLineEdit.text()
            )
        elif dump_from == "Seed":
            hd_kwargs["public_key_type"] = self.ui.bipFromSeedPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_seed(
                BIP39Seed(
                    seed=self.ui.bipFromSeedsQLineEdit.text()
                )
            )
        elif dump_from == "WIF":
            hd_kwargs["public_key_type"] = self.ui.bipFromWIFPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_wif(
                wif=self.ui.bipFromWIFQLineEdit.text()
            )
        elif dump_from == "XPrivate key":
            hd_kwargs["public_key_type"] = self.ui.bipFromXPrivateKeyPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_xprivate_key(
                xprivate_key=self.ui.bipFromXPrivateKeyQLineEdit.text(),
                strict=self.ui.bipFromXPrivateKeyStrictQCheckBox.isChecked()
            )
        elif dump_from == "XPublic key":
            hd_kwargs["public_key_type"] = self.ui.bipFromXPublicKeyPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_xpublic_key(
                xpublic_key=self.ui.bipFromXPublicKeyQLineEdit.text(),
                strict=self.ui.bipFromXPublicKeyStrictQCheckBox.isChecked()
            )

    def _dump_cardano(self, dump_from, hd_kwargs):
        if dump_from == "Entropy":
            hd_kwargs["language"] = self.ui.cardanoFromEntropyLanguageQComboBox.currentText().lower()
            hd_kwargs["passphrase"] = self.ui.cardanoFromEntropyPassphraseQLineEdit.text()
            hd_kwargs["cardano_type"] = self.ui.cardanoFromEntropyCardanoTypeQComboBox.currentText().lower()
            hd_kwargs["address_type"] = self.ui.cardanoFromEntropyAddressTypeQComboBox.currentText().lower()
            hd_kwargs["staking_public_key"] = self.ui.cardanoFromEntropyStakingQLineEdit.text()
            return HDWallet(**hd_kwargs).from_entropy(
                BIP39Entropy(
                    entropy=self.ui.cardanoFromEntropyGenerateQLineEdit.text()
                )
            )
        elif dump_from == "Mnemonic":
            hd_kwargs["passphrase"] = self.ui.cardanoFromMnemonicPassphraseQLineEdit.text()
            hd_kwargs["cardano_type"] = self.ui.cardanoFromMnemonicCardanoTypeQComboBox.currentText().lower()
            hd_kwargs["address_type"] = self.ui.cardanoFromMnemonicAddressTypeQComboBox.currentText().lower()
            hd_kwargs["staking_public_key"] = self.ui.cardanoFromMnemonicStakingQLineEdit.text()
            return HDWallet(**hd_kwargs).from_mnemonic(
                BIP39Mnemonic(
                    mnemonic=self.ui.cardanoFromMnemonicGenerateQLineEdit.text()
                )
            )
        elif dump_from == "Private key":
            hd_kwargs["cardano_type"] = self.ui.cardanoFromPrivateKeyCardanoTypeQComboBox.currentText().lower()
            hd_kwargs["address_type"] = self.ui.cardanoFromPrivateKeyAddressTypeQComboBox.currentText().lower()
            hd_kwargs["staking_public_key"] = self.ui.cardanoFromPrivateKeyStakingQLineEdit.text()
            return HDWallet(**hd_kwargs).from_private_key(
                private_key=self.ui.cardanoFromPrivateKeyQLineEdit.text()
            )
        elif dump_from == "Public key":
            hd_kwargs["cardano_type"] = self.ui.cardanoFromPublicKeyCardanoTypeQComboBox.currentText().lower()
            hd_kwargs["address_type"] = self.ui.cardanoFromPublicKeyAddressTypeQComboBox.currentText().lower()
            hd_kwargs["staking_public_key"] = self.ui.cardanoFromPublicKeyStakingQLineEdit.text()
            return HDWallet(**hd_kwargs).from_public_key(
                public_key=self.ui.cardanoFromPublicKeyQLineEdit.text()
            )
        elif dump_from == "Seed":
            hd_kwargs["passphrase"] = self.ui.cardanoFromSeedPassphraseQLineEdit.text()
            hd_kwargs["cardano_type"] = self.ui.cardanoFromSeedCardanoTypeQComboBox.currentText().lower()
            hd_kwargs["address_type"] = self.ui.cardanoFromSeedAddressTypeQComboBox.currentText().lower()
            hd_kwargs["staking_public_key"] = self.ui.cardanoFromSeedStakingQLineEdit.text()
            return HDWallet(**hd_kwargs).from_seed(
                CardanoSeed(
                    seed=self.ui.cardanoFromSeedQLineEdit.text()
                )
            )
        elif dump_from == "XPrivate key":
            hd_kwargs["cardano_type"] = self.ui.cardanoFromXPrivateKeyCardanoTypeQComboBox.currentText().lower()
            hd_kwargs["address_type"] = self.ui.cardanoFromXPrivateKeyAddressTypeQComboBox.currentText().lower()
            hd_kwargs["staking_public_key"] = self.ui.cardanoFromXPrivateKeyStakingQLineEdit.text()
            return HDWallet(**hd_kwargs).from_xprivate_key(
                xprivate_key=self.ui.cardanoFromXPrivateKeyQLineEdit.text(),
                strict=self.ui.cardanoFromXPrivateKeyStrictQCheckBox.isChecked()
            )
        elif dump_from == "XPublic key":
            hd_kwargs["cardano_type"] = self.ui.cardanoFromXPublicKeyCardanoTypeQComboBox.currentText().lower()
            hd_kwargs["address_type"] = self.ui.cardanoFromXPublicKeyAddressTypeQComboBox.currentText().lower()
            hd_kwargs["staking_public_key"] = self.ui.cardanoFromXPublicKeyStakingQLineEdit.text()
            return HDWallet(**hd_kwargs).from_xpublic_key(
                xpublic_key=self.ui.cardanoFromXPublicKeyQLineEdit.text(),
                strict=self.ui.cardanoFromXPublicKeyStrictQCheckBox.isChecked()
            )

    def _dump_ev1(self, dump_from, hd_kwargs):
        if dump_from == "Entropy":
            hd_kwargs["language"] = self.ui.electrumV1FromEntropyLanguageQComboBox.currentText().lower()
            hd_kwargs["passphrase"] = self.ui.electrumV1FromEntropyPassphraseGenerateQLineEdit.text()
            hd_kwargs["public_key_type"] = self.ui.electrumV1FromEntropyPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_entropy(
                ElectrumV1Entropy(
                    entropy=self.ui.electrumV1FromEntropyQLineEdit.text()
                )
            )
        elif dump_from == "Mnemonic":
            hd_kwargs["passphrase"] = self.ui.electrumV1FromMnemonicPassphraseGenerateQLineEdit.text()
            hd_kwargs["public_key_type"] = self.ui.electrumV1FromMnemonicPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_mnemonic(
                ElectrumV1Mnemonic(
                    mnemonic=self.ui.electrumV1FromMnemonicGenerateQLineEdit.text()
                )
            )

        elif dump_from == "Private key":
            hd_kwargs["public_key_type"] = self.ui.electrumV1FromPrivateKeyPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_private_key(
                private_key=self.ui.electrumV1FromPrivateKeyQLineEdit.text()
            )
        elif dump_from == "Public key":
            hd_kwargs["public_key_type"] = self.ui.electrumV1FromPublicKeyPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_public_key(
                public_key=self.ui.electrumV1FromPublicKeyQLineEdit.text()
            )
        elif dump_from == "Seed":
            hd_kwargs["public_key_type"] = self.ui.electrumV1FromSeedPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_seed(
                ElectrumV1Seed(
                    seed=self.ui.electrumV1FromSeedQLineEdit.text()
                )
            )
        elif dump_from == "WIF":
            hd_kwargs["public_key_type"] = self.ui.electrumV1FromWIFPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_wif(
                wif=self.ui.electrumV1FromWIFQLineEdit.text()
            )

    def _dump_ev2(self, dump_from, hd_kwargs):
        if dump_from == "Entropy":
            hd_kwargs["mode"] = self.ui.electrumV2FromEntropyModeQComboBox.currentText().lower()
            hd_kwargs["mnemonic_type"] = self.ui.electrumV2FromEntropyMnemonicTypeQComboBox.currentText().lower()
            hd_kwargs["language"] = self.ui.electrumV2FromEntropyLanguageQComboBox.currentText().lower()
            hd_kwargs["passphrase"] = self.ui.electrumV2FromEntropyGenerateQLineEdit.text()
            hd_kwargs["public_key_type"] = self.ui.electrumV2FromEntropyPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_entropy(
                ElectrumV2Entropy(
                    entropy=self.ui.electrumV2FromEntropyGenerateQLineEdit.text()
                )
            )

        elif dump_from == "Mnemonic":
            mnemonic_type = self.ui.electrumV2FromMnemonicMnemonicTypeQComboBox.currentText().lower()
            hd_kwargs["mode"] = self.ui.electrumV2FromMnemonicModeQComboBox.currentText().lower()
            hd_kwargs["mnemonic_type"] = mnemonic_type
            hd_kwargs["passphrase"] = self.ui.electrumV2FromMnemonicPassphraseGenerateQLineEdit.text()
            hd_kwargs["public_key_type"] = self.ui.electrumV2FromMnemonicPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_mnemonic(
                ElectrumV2Mnemonic(
                    mnemonic=self.ui.electrumV2FromMnemonicGenerateQLineEdit.text(),
                    mnemonic_type=mnemonic_type
                )
            )

        elif dump_from == "Seed":
            hd_kwargs["mode"] = self.ui.electrumV2FromSeedModeQComboBox.currentText().lower()
            hd_kwargs["public_key_type"] = self.ui.electrumV2FromSeedPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_seed(
                ElectrumV2Seed(
                    seed=self.ui.electrumV2FromSeedsQLineEdit.text()
                )
            )

    def _dump_monero(self, dump_from, hd_kwargs):
        if dump_from == "Entropy":
            hd_kwargs["language"] = self.ui.moneroFromEntropyLanguageQComboBox.currentText().lower()
            hd_kwargs["payment_id"] = self.ui.moneroFromEntropyPaymentIDQLineEdit.text().lower()
            return HDWallet(**hd_kwargs).from_entropy(
                MoneroEntropy(
                    entropy=self.ui.moneroFromEntropyQLineEdit.text()
                )
            )

        elif dump_from == "Mnemonic":
            hd_kwargs["payment_id"] = self.ui.moneroFromMnemonicPaymentIDQLineEdit.text().lower()
            return HDWallet(**hd_kwargs).from_mnemonic(
                MoneroMnemonic(
                    mnemonic=self.ui.moneroFromMnemonicQLineEdit.text()
                )
            )

        elif dump_from == "Private key":
            hd_kwargs["payment_id"] = self.ui.moneroFromMnemonicPaymentIDQLineEdit.text().lower()
            return HDWallet(**hd_kwargs).from_private_key(
                private_key=self.ui.moneroFromPrivateKeyQLineEdit.text().lower()
            )

        elif dump_from == "Seed":
            hd_kwargs["payment_id"] = self.ui.moneroFromSeedPaymentIDQLineEdit.text().lower()
            return HDWallet(**hd_kwargs).from_seed(
                MoneroSeed(
                    seed=self.ui.moneroFromSeedQLineEdit.text()
                )
            )

        elif dump_from == "Spend private key":
            hd_kwargs["payment_id"] = self.ui.moneroFromSpendPrivateKeyPaymentIDQLineEdit.text().lower()
            return HDWallet(**hd_kwargs).from_spend_private_key(
                spend_private_key=self.ui.moneroFromSpendPrivateKeyQLineEdit.text().lower()
            )

        elif dump_from == "Watch only":
            hd_kwargs["payment_id"] = self.ui.moneroFromWatchOnlyPaymentIDQLineEdit.text().lower()
            return HDWallet(**hd_kwargs).from_watch_only(
                view_private_key=self.ui.moneroFromWatchOnlyViewPrivateKeyQLIneEdit.text(),
                spend_public_key=self.ui.moneroFromWatchOnlySpendPublicKeyQLineEdit.text()
            )

    def _dumps_crypto_change(self):
        crypto = self.ui.dumpsCryptocurrencyQComboBox.currentText()
        crypto_obj = CRYPTOCURRENCIES.cryptocurrency(crypto)

        self.ui.dumpsHdQComboBox.clear()
        self.ui.dumpsHdQComboBox.addItems(crypto_obj.HDS.get_hds())
        self.ui.dumpsHdQComboBox.setCurrentIndex(0)

        nets = [i.title() for i in crypto_obj.NETWORKS.get_networks()]
        self.ui.dumpsNetworkQComboBox.clear()
        self.ui.dumpsNetworkQComboBox.addItems(nets)
        self.ui.dumpsNetworkQComboBox.setCurrentText("Mainnet")

        coin_typs_derviation = [
            self.ui.bip44CoinTypeQLineEdit,
            self.ui.bip49CoinTypeQLineEdit,
            self.ui.bip84CoinTypeQLineEdit,
            self.ui.bip86CoinTypeQLineEdit,
            self.ui.cip1852CoinTypeQLineEdit
        ]

        for c in coin_typs_derviation: c.setText(str(crypto_obj.COIN_TYPE))

    def _dump_format_changed(self):
        f = self.ui.dumpsFormatQComboBox.currentText()
        
        if f == "CSV":
            self.ui.dumpsExcludeOrIncludeQLabel.setText("Include")
            self.__default_csv_include()
        else:
            self.ui.dumpsExcludeOrIncludeQLabel.setText("Exclude")
            self.ui.dumpsExcludeOrIncludeQLineEdit.setText(None)


    def __default_csv_include(self):
        hd = self.ui.dumpsHdQComboBox.currentText()

        if hd == "BIP32":
            _include: str = "at:path,addresses:p2pkh,public_key,wif"
        elif hd in [
            "BIP44", "BIP49", "BIP84", "BIP86"
        ]:
            _include: str = "at:path,address,public_key,wif"
        elif hd == "BIP141":
            _include: str = f"at:path,addresses:p2wpkh,public_key,wif"
        elif hd == "Cardano":
            _include: str = "at:path,address,public_key,private_key"
        elif hd in [
            "Electrum-V1", "Electrum-V2"
        ]:
            _include: str = "at:change,at:address,address,public_key,wif"
        elif hd == "Monero":
            _include: str = "at:minor,at:major,sub_address"
        else:
            _include = None

        self.ui.dumpsExcludeOrIncludeQLineEdit.setText(_include)


    def _dump_hd_changed(self):
        current_hd = self.ui.dumpsHdQComboBox.currentText()

        if current_hd == "":
            return None

        current_hd_widget = self.stack_hd_widgets[current_hd]
        self.change_page("hdQStackedWidget", current_hd_widget)

        keys = []

        for key in self.stack_from_widgets[current_hd_widget]:
            if key == "StackWidget":
                continue
            if current_hd in {"BIP44", "BIP49", "BIP84", "BIP86"} and key == "XPublic key":
                continue

            keys.append(key)

        self.ui.dumpsFromQComboBox.clear()
        self.ui.dumpsFromQComboBox.addItems(sorted(keys))
        self.ui.dumpsFromQComboBox.setCurrentIndex(0)

        if self.ui.dumpsFormatQComboBox.currentText() == "CSV":
            self.__default_csv_include()

    def __filter_derivation_tab(self, k):
        first_name = None
        for name, data in self.derivation_tab.items():
            if name in self.hd_allowed_derivation[k]:
                data["button"].setEnabled(True)
                if not first_name:
                    first_name = name
            else:
                data["button"].setEnabled(False)
        self.derivation_tab[first_name]["button"].click()

    def _dump_from_changed(self):
        dump_from = self.ui.dumpsFromQComboBox.currentText()
        if dump_from == '':
            return None

        current_hd = self.ui.dumpsHdQComboBox.currentText()

        current_hd_widget = self.stack_hd_widgets[current_hd]
        current_from_stack = self.stack_from_widgets[current_hd_widget]["StackWidget"]
        current_from_widget = self.stack_from_widgets[current_hd_widget][dump_from]

        self.change_page(current_from_stack, current_from_widget)

        is_drived = dump_from in self.hd_drivable_methods[current_hd]
        self.ui.derivationQGroupBox.setEnabled(is_drived)

        if is_drived:
            key = current_hd
            if dump_from == "XPublic key":
                if current_hd == "BIP32":
                    key = 'BIP32XPUB'
                elif current_hd == "Cardano":
                    key = 'CardanoXPUB'
            self.__filter_derivation_tab(key)

    def _setup_generate_stack(self):
        self.ui.generateEntropyClientQComboBox.addItems(ENTROPIES.names())
        self.ui.generateEntropyClientQComboBox.currentIndexChanged.connect(self._generate_entropy_change)
        self.ui.generateEntropyClientQComboBox.setCurrentText(BIP39Entropy.name())
        self.ui.generateEntropyClientAndStrengthQPushButton.clicked.connect(self._generate_entropy)

        self.ui.generateMnemonicClientQComboBox.addItems(MNEMONICS.names())
        self.ui.generateMnemonicClientQComboBox.currentIndexChanged.connect(self._generate_mnemonic_change)
        self.ui.generateMnemonicClientQComboBox.setCurrentText(BIP39Mnemonic.name())
        self.ui.generateMnemonicClientWordsAndLanguageQPushButton.clicked.connect(self._generate_mnemonic)

        self.ui.generateMnemonicWordsQRadioButton.toggled.connect(self._generate_mnemonic_word_toggle)
        self.ui.generateMnemonicEntropyQRadioButton.toggled.connect(self._generate_mnemonic_entropy_toggle)
        self.ui.generateMnemonicWordsQRadioButton.setChecked(True)

        self.ui.generateSeedClientQComboBox.addItems(SEEDS.names())
        self.ui.generateSeedClientQComboBox.currentIndexChanged.connect(self._generate_seed_change)
        self.ui.generateSeedClientQComboBox.setCurrentText(BIP39Mnemonic.name())
        self.ui.generateSeedCardanoTypeQComboBox.currentIndexChanged.connect(self._cardano_type_changed)
        self.ui.generateSeedPassphraseGenerateQPushButton.clicked.connect(self._generate_seed)

        self.ui.generateLengthQLineEdit.setText("12")
        self.ui.generateLengthQLineEdit.setValidator(QIntValidator(1, 1000))

        self.ui.generatePassphraseUpperCaseQCheckBox.setChecked(True)
        self.ui.generatePassphraseLowerCaseQCheckBox.setChecked(True)
        self.ui.generatePassphraseNumberQCheckBox.setChecked(True)
        self.ui.generatePassphraseCharacterQCheckBox.setChecked(False)

        self.ui.generateSeedCardanoTypeQComboBox.addItems([i.title() for i in Cardano.TYPES.get_cardano_types()])
        self.ui.generateSeedMnemonicTypeQComboBox.addItems(
            [i.title() for i in ElectrumV2Mnemonic.mnemonic_types.keys()])
        self.ui.generateMnemonicTypeQComboBox.addItems([i.title() for i in ElectrumV2Mnemonic.mnemonic_types.keys()])

        self.ui.generatePassphraseQPushButton.clicked.connect(self._generate_passphrase)

    def _generate_entropy_change(self):
        entropy_client = self.ui.generateEntropyClientQComboBox.currentText()
        self.ui.generateEntropyStrengthQComboBox.clear()
        self.ui.generateEntropyStrengthQComboBox.addItems(
            map(
                str, ENTROPIES.entropy(entropy_client).strengths
            )
        )
        self.ui.generateEntropyStrengthQComboBox.setCurrentIndex(0)

    def _generate_entropy(self):
        entropy_client = self.ui.generateEntropyClientQComboBox.currentText()
        strength = int(self.ui.generateEntropyStrengthQComboBox.currentText())
        gen_entropy = ENTROPIES.entropy(entropy_client).generate(strength=strength)

        output = {
            "name": entropy_client,
            "entropy": gen_entropy,
            "strength": strength
        }

        self.println(output)

    def _generate_mnemonic_change(self):
        mnemonic_client = self.ui.generateMnemonicClientQComboBox.currentText()
        self.ui.generateMnemonicWordsQComboBox.clear()
        self.ui.generateMnemonicLanguageQComboBox.clear()

        self.ui.generateMnemonicWordsQComboBox.addItems(
            map(
                str, MNEMONICS.mnemonic(mnemonic_client).words_list
            )
        )
        self.ui.generateMnemonicLanguageQComboBox.addItems(
            [i.title() for i in MNEMONICS.mnemonic(mnemonic_client).languages])

        self.ui.generateMnemonicWordsQComboBox.setCurrentIndex(0)
        self.ui.generateMnemonicLanguageQComboBox.setCurrentText('English')

        if ElectrumV2Seed.name() == mnemonic_client:
            self.ui.generateMnemonicTypeQComboBox.setEnabled(True)
            self.ui.generateMnemonicTypeQComboBox.setCurrentIndex(0)
        else:
            self.ui.generateMnemonicTypeQComboBox.setEnabled(False)
            self.ui.generateMnemonicTypeQComboBox.setCurrentIndex(-1)

    def _generate_mnemonic_word_toggle(self):
        if self.ui.generateMnemonicWordsQRadioButton.isChecked():
            self.ui.generateMnemonicWordsQComboBox.setEnabled(True)
            self.ui.generateMnemonicWordsQComboBox.setCurrentIndex(0)
            self.ui.generateSeedMnemonicEntropyQLineEdit.setText(None)
            self.ui.generateSeedMnemonicEntropyQLineEdit.setEnabled(False)

    def _generate_mnemonic_entropy_toggle(self):
        if self.ui.generateMnemonicEntropyQRadioButton.isChecked():
            self.ui.generateMnemonicWordsQComboBox.setEnabled(False)
            self.ui.generateMnemonicWordsQComboBox.setCurrentIndex(-1)
            self.ui.generateSeedMnemonicEntropyQLineEdit.setEnabled(True)

    def _generate_mnemonic(self):
        mnemonic_client = self.ui.generateMnemonicClientQComboBox.currentText()
        word = self.ui.generateMnemonicWordsQComboBox.currentText()
        entropy = self.ui.generateSeedMnemonicEntropyQLineEdit.text()
        lang = self.ui.generateMnemonicLanguageQComboBox.currentText().lower()

        kwargs = {
            "language": lang
        }

        if ElectrumV2Seed.name() == mnemonic_client:
            kwargs["mnemonic_type"] = self.ui.generateMnemonicTypeQComboBox.currentText().lower()

        if self.ui.generateMnemonicWordsQRadioButton.isChecked():
            kwargs["words"] = int(word)
            gen_mnemonic = MNEMONICS.mnemonic(mnemonic_client).from_words(**kwargs)
        else:
            kwargs["entropy"] = entropy
            gen_mnemonic = MNEMONICS.mnemonic(mnemonic_client).from_entropy(**kwargs)

        output = {
            "name": mnemonic_client,
            "mnemonic": gen_mnemonic
        }

        output.update(kwargs)

        self.println(output)

    def _generate_seed_change(self):
        seed_client = self.ui.generateSeedClientQComboBox.currentText()

        self.ui.generateSeedCardanoTypeQComboBox.setCurrentIndex(-1)
        self.ui.generateSeedMnemonicTypeQComboBox.setCurrentIndex(-1)

        self.ui.generateSeedMnemonicTypeContainerQFrame.setEnabled(False)
        self.ui.generateSeedCardanoTypeContainerQFrame.setEnabled(False)

        self.ui.generateSeedPassphraseGenerateQLineEdit.setText(None)
        self.ui.generateSeedPassphraseGenerateContainerQFrame.setEnabled(False)

        if CardanoSeed.name() == seed_client:
            self.ui.generateSeedCardanoTypeContainerQFrame.setEnabled(True)
            self.ui.generateSeedCardanoTypeQComboBox.setCurrentIndex(0)
        elif ElectrumV2Seed.name() == seed_client:
            self.ui.generateSeedMnemonicTypeContainerQFrame.setEnabled(True)
            self.ui.generateSeedMnemonicTypeQComboBox.setCurrentIndex(0)

        if seed_client in (BIP39Seed.name(), ElectrumV2Seed.name()):
            self.ui.generateSeedPassphraseGenerateContainerQFrame.setEnabled(True)

    def _cardano_type_changed(self):
        cardano_type = self.ui.generateSeedCardanoTypeQComboBox.currentText().lower()
        if cardano_type == 'byron-ledger' or cardano_type == 'shelley-ledger':
            self.ui.generateSeedPassphraseGenerateContainerQFrame.setEnabled(True)
        else:
            self.ui.generateSeedPassphraseGenerateQLineEdit.setText(None)
            self.ui.generateSeedPassphraseGenerateContainerQFrame.setEnabled(False)

    def _generate_seed(self):
        seed_client = self.ui.generateSeedClientQComboBox.currentText()
        mnemonic_type = self.ui.generateSeedMnemonicTypeQComboBox.currentText().lower()
        cardano_type = self.ui.generateSeedCardanoTypeQComboBox.currentText().lower()
        mnemonic = self.ui.generateSeedMnemonicQLineEdit.text()
        passphrase = self.ui.generateSeedPassphraseGenerateQLineEdit.text()
        output = None

        try:
            if len(mnemonic) == 0:
                raise Exception("mnemonic is required to generate seed!")
            elif CardanoSeed.name() == seed_client:
                seed = CardanoSeed.from_mnemonic(mnemonic=mnemonic, cardano_type=cardano_type, passphrase=passphrase)
            elif ElectrumV2Seed.name() == seed_client:
                seed = ElectrumV2Seed.from_mnemonic(mnemonic=mnemonic, mnemonic_type=mnemonic_type,
                                                    passphrase=passphrase)
            elif BIP39Seed.name() == seed_client:
                seed = SEEDS.seed(seed_client).from_mnemonic(mnemonic=mnemonic, passphrase=passphrase)
            else:
                seed = SEEDS.seed(seed_client).from_mnemonic(mnemonic=mnemonic)
        except Exception as e:
            output = f"ERROR: {e}"
        else:
            output = {
                "name": seed_client,
                "seed": seed
            }

        self.println(output)

    def _generate_passphrase(self):

        if len(self.ui.generateLengthQLineEdit.text()) == 0:
            self.println("ERROR: passpharse length is required")
            return None

        length = int(self.ui.generateLengthQLineEdit.text())
        upper = self.ui.generatePassphraseUpperCaseQCheckBox.isChecked()
        lower = self.ui.generatePassphraseLowerCaseQCheckBox.isChecked()
        digit = self.ui.generatePassphraseNumberQCheckBox.isChecked()
        special = self.ui.generatePassphraseCharacterQCheckBox.isChecked()

        characters = string.ascii_lowercase if lower else ''
        characters += string.ascii_uppercase if upper else ''
        characters += string.digits if digit else ''
        characters += string.punctuation if special else ''

        output = None
        if not any([upper, lower, special, digit]):
            output = "ERROR: At least one of upper, lower, special, or digit must be selected"
        else:
            pp = "".join(choice(characters) for _ in range(length))

            output = {
                "passphrase": pp,
                "length": length
            }

        self.println(output)

    def change_page(self, stacked_name: str, widget_name: str) -> None:
        qStackedWidget: Optional[QStackedWidget] = self.findChild(QStackedWidget, stacked_name)

        if qStackedWidget is None:
            print(f"QStackWidget not found: {stacked_name}")
            return None

        qWidget: Optional[QWidget] = qStackedWidget.findChild(QWidget, widget_name)

        if qStackedWidget and qWidget:
            qStackedWidget.setCurrentWidget(qWidget)
        else:
            print(f"ERROR changing page: '{stacked_name}' '{widget_name}'")

    def process_command(self):
        cmd = self.ui.outputTerminalQLineEdit.text()
        def process():
            f_cmd = cmd if cmd.startswith('hdwallet ') else f"hdwallet {cmd}"

            self.ui.outputTerminalQLineEdit.setText(None)
            result = subprocess.run(
                f_cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            output = result.stderr if result.stderr else result.stdout
            return output.decode()

        if cmd.lower() == 'clear':
            self.ui.outputTerminalQPlainTextEdit.setPlainText(None)
            self.ui.outputTerminalQLineEdit.setText(None)
        else:
            job = Worker(process)
            job.signals.interval_finished.connect(self.println)
            QThreadPool.globalInstance().start(job)

    def println(self, s):
        # just for now

        if isinstance(s, dict):
            newtext = json.dumps(s, indent=4, ensure_ascii=False)
        elif s == None:
            return None
        else:
            newtext = str(s)

        self.ui.outputTerminalQPlainTextEdit.appendPlainText(f"{newtext}")

    def toggle_expand(self):
        if self.toggle_expand_terminal.isChecked():
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
            self.setMaximumSize(
                self.ui.hdWalletContainerQFrame.width(), self.ui.hdwalletMainQFrame.height()
                # Set maximum size of main window
            )
            self.showNormal()

            self.layout().removeWidget(self.ui.outputQFrame)
            self.detached_window = DetachedWindow(self)
            self.detached_window.setWindowTitle("Terminal")
            self.detached_window.resize(self.ui.outputQFrame.width(), self.ui.outputQFrame.height())
            self.detached_window.setMinimumHeight(self.minimumHeight())

            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self.ui.outputQFrame)

            self.detached_window.setLayout(layout)
            self.detached_window.show()
            self.detached_window.setStyleSheet(self.styleSheet())
            self.setMinimumWidth(0)
            self.detached_window.center_window()
            # self.center_window()

            if not self.isMaximized():
                self.resize(self.width() - self.ui.outputQFrame.width(), self.height())

        else:
            if self.detached_window:
                self.detached_window.close()
                self.detached_window = None

            self.ui.centralwidget.layout().addWidget(self.ui.outputQFrame)

            self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
            self.setMaximumSize(
                16777215, 16777215  # Removes maximum size of main window
            )
            self.ui.outputQFrame.setGeometry(QRect(
                0, 0, 600, self.ui.outputQFrame.height()  # Fix from detached into attached
            ))
            self.show()

    def load_stylesheet(self, path):
        style_file = QFile(path)
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stylesheet = str(style_file.readAll(), encoding='utf-8')
            self.setStyleSheet(stylesheet)

    def closeEvent(self, event):
        if self.detached_window:
            self.detached_window.close()
        super().closeEvent(event)

    def update_terminal_ui(self):

        self.ui.outputWidgetTopContainerQWidget.setGeometry(QRect(
            (
                self.ui.noLayoutQWidget.width() - (
                    self.ui.outputWidgetTopContainerQFrame.width() + (
                        20 if self.ui.outputTerminalQPlainTextEdit.verticalScrollBar().maximum() > 0 else 10
                    )
                )
            ), 0,
            self.ui.outputWidgetTopContainerQFrame.width(), self.ui.outputWidgetTopContainerQWidget.height()
        ))
        self.ui.outputTerminalQWidget.setGeometry(QRect(
            0, 0, self.ui.noLayoutQWidget.width(), self.ui.noLayoutQWidget.height()
        ))
        self.ui.outputWidgetTopContainerQWidget.raise_()
        self.ui.outputTerminalQWidget.lower()

    def resizeEvent(self, event) -> None:
        self.update_terminal_ui()

    def center_window(self):
        # Get the screen resolution from the application
        screen = self.screen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
        self.update_terminal_ui()

    def show(self):
        super(CoreApp, self).show()
        self.update_terminal_ui()
        self.update_terminal_ui()

    def update_style(self, widget: QWidget):
        widget.setStyleSheet(widget.styleSheet())

    def widget_changed(self, stacked_name: str, page_name: str, button: QWidget, qWidget: QWidget) -> None:
        for btn in qWidget.findChildren(QWidget):
            btn.setProperty("Active", "")
            self.update_style(btn)

        button.setProperty("Active", "true")
        self.update_style(button)
        self.change_page(stacked_name, page_name)

    def derivation_tab_changed(self, page_name: str, qPushButton: QPushButton) -> None:
        widget = self.ui.derivationTabButtonsContainerQFrame
        self.widget_changed("derivationsQStackedWidget", page_name, qPushButton, widget)

    def generate_dump_tab_changed(self, page_name: str, qPushButton: QPushButton) -> None:
        widget = self.ui.generateAndDumpTabContainerQFrame
        self.widget_changed("hdwalletQStackedWidget", page_name, qPushButton, widget)


if __name__ == "__main__":
    app = QApplication([])

    main_window = CoreApp()
    main_window.show()

    app.exec()
