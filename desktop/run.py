import os
import subprocess
import string
import json
from random import choice

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
    CustomDerivation,BIP44Derivation, BIP49Derivation, BIP84Derivation,
    BIP86Derivation, CHANGES
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

class DetachedWindow(QWidget):
    def __init__(self, p):
        super().__init__()
        self.main_window = p

    def closeEvent(self, event):
        self.main_window.toggle_expand_terminal.setChecked(False)
        self.main_window.toggle_expand()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.detached_window = None

        QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), "ui/font/HD Wallet-Regular.ttf"))

        # Setup UI Stuff
        self.setWindowTitle("Hierarchical Deterministic Wallet")

        self.load_stylesheet(os.path.join(os.path.dirname(__file__), "ui/css/dark-style.css"))

        self.toggle_expand_terminal = SvgButton(
            parent_widget=self.ui.expandAndCollapseTerminalQFrame,
            icon_path=os.path.join(os.path.dirname(__file__),"ui/images/icon_maximize.svg"),
            alt_icon_path=os.path.join(os.path.dirname(__file__),"ui/images/icon_minimize.svg"),
            icon_width=17,
            icon_height=17
        )
        self.toggle_expand_terminal.setCheckable(True)
        self.toggle_expand_terminal.toggled.connect(self.toggle_expand)
        self.ui.outputTerminalQLineEdit.returnPressed.connect(self.process_command)

        self.ui.generateQPushButton.clicked.connect(lambda: self.change_page("hdwalletQStackedWidget", "generatePageQStackedWidget"))
        self.ui.dumpQPushButton.clicked.connect(lambda: self.change_page("hdwalletQStackedWidget", "dumpsPageQStackedWidget"))

        self.ui.generateEntropyClientContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.generateSeedMnemonicContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.generateLengthContainerQFrame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        self._setup_generate_stack()
        self._setup_dump_stack()

    def _setup_dump_stack(self):
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

        self.hd_allowed_derivation = {
            'BIP32': ["Custom", "BIP44", "BIP49", "BIP84", "BIP86", "BIP141", "CIP1852"],
            'BIP44': ["BIP44"],
            'BIP49': ["BIP49"],
            'BIP84': ["BIP84"],
            'BIP86': ["BIP86"],
            'BIP141': ["BIP141"],
            'Cardano': ["Custom", "CIP1852"],
            'Electrum-V1': ["Electrum"],
            'Electrum-V2': ["Electrum"],
            'Monero': ["Monero"] 
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

        self.ui.dumpsHdQComboBox.currentIndexChanged.connect(self._dump_hd_changed)
        self.ui.dumpsFromQComboBox.currentIndexChanged.connect(self._dump_from_changed)

        self.ui.dumpsCryptocurrencyQComboBox.clear()
        self.ui.dumpsCryptocurrencyQComboBox.addItems(CRYPTOCURRENCIES.names())
        self.ui.dumpsCryptocurrencyQComboBox.currentIndexChanged.connect(self._dumps_crypto_change)
        self.ui.dumpsCryptocurrencyQComboBox.setCurrentText("Bitcoin")

        self.ui.bipFromEntropyLanguageQComboBox.clear()
        self.ui.bipFromEntropyLanguageQComboBox.addItems([i.title() for i in BIP39Mnemonic.languages])
        self.ui.bipFromEntropyLanguageQComboBox.setCurrentText("English")

        self.ui.dumpsGenerateQPushButton.clicked.connect(self._dumps)

    def _dumps(self):
        try:
            self.__dumps()
        except Exception as e:
            self.println(f"ERROR: {e}")

    def __dumps(self):
        current_hd = self.ui.dumpsHdQComboBox.currentText()
        dump_from = self.ui.dumpsFromQComboBox.currentText()
        network = self.ui.dumpsNetworkQComboBox.currentText()
        exclude_set = set([p.strip() for p in self.ui.dumpsExcludeOrIncludeQLineEdit.text().split(",")])

        crypto = self.ui.dumpsCryptocurrencyQComboBox.currentText()

        hd_kwargs = {
            "cryptocurrency": CRYPTOCURRENCIES.cryptocurrency(crypto),
            "hd": HDS.hd(current_hd),
            "network": network.lower()
        }

        #TODO: implement all hd
        if current_hd in ('BIP32', 'BIP44', 'BIP49', 'BIP84', 'BIP86', 'BIP141'):
            hd = self._dump_bips(current_hd, dump_from, hd_kwargs)

        derivation = self.__dumps_get_derivation(CRYPTOCURRENCIES.cryptocurrency(crypto))
        hdwallet = hd.from_derivation(derivation=derivation)

        self.println(json.dumps(hdwallet.dumps(exclude=exclude_set), indent=4, ensure_ascii=False))


    def __dumps_get_derivation(self, crypto):
        tab = self.ui.derivationsQTabWidget
        current_tab = tab.tabText(tab.currentIndex())

        #TODO: implement all derivation
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
            pass
        elif current_tab == "CIP1852":
            pass
        elif current_tab == "Electrum":
            pass
        elif current_tab == "Monero":
            pass


    def _dump_bips(self, hd, dump_from, hd_kwargs):
        #TODO: dump from all available methods
        if dump_from == "Entropy":
            hd_kwargs["language"] = self.ui.bipFromEntropyLanguageQComboBox.currentText().lower()
            hd_kwargs["passphrase"] = self.ui.bipFromEntropyPassphraseQLineEdit.text()
            hd_kwargs["public_key_type"] = self.ui.bipFromEntropyPublicKeyTypeQComboBox.currentText().lower()
            return HDWallet(**hd_kwargs).from_entropy(
                BIP39Entropy(
                    entropy = self.ui.bipFromEntropyGenerateQLineEdit.text()
                )
            )

    def _dumps_crypto_change(self):
        crypto = self.ui.dumpsCryptocurrencyQComboBox.currentText()

        self.ui.dumpsHdQComboBox.clear()
        self.ui.dumpsHdQComboBox.addItems(CRYPTOCURRENCIES.cryptocurrency(crypto).HDS.get_hds())
        self.ui.dumpsHdQComboBox.setCurrentIndex(0)

        nets = [i.title() for i in CRYPTOCURRENCIES.cryptocurrency(crypto).NETWORKS.get_networks()]
        self.ui.dumpsNetworkQComboBox.clear()
        self.ui.dumpsNetworkQComboBox.addItems(nets)
        self.ui.dumpsNetworkQComboBox.setCurrentText("Mainnet")

    def _dump_hd_changed(self):
        current_hd = self.ui.dumpsHdQComboBox.currentText()

        if current_hd == "":
            return None

        current_hd_widget  = self.stack_hd_widgets[current_hd]
        self.change_page("hdQStackedWidget", current_hd_widget)

        keys = [key for key in self.stack_from_widgets[current_hd_widget] if key != "StackWidget"]
        self.ui.dumpsFromQComboBox.clear()
        self.ui.dumpsFromQComboBox.addItems(sorted(keys))
        self.ui.dumpsFromQComboBox.setCurrentIndex(0)

        ls_indx = 0
        for index in range(self.ui.derivationsQTabWidget.count() - 1, -1, -1):
            if self.ui.derivationsQTabWidget.tabText(index) in self.hd_allowed_derivation[current_hd]:
                self.ui.derivationsQTabWidget.setTabEnabled(index, True)
                ls_indx = index
            else:
                self.ui.derivationsQTabWidget.setTabEnabled(index, False)
        self.ui.derivationsQTabWidget.setCurrentIndex(ls_indx)

    def _dump_from_changed(self):
        dump_from = self.ui.dumpsFromQComboBox.currentText()
        if dump_from == '':
            return None

        current_hd = self.ui.dumpsHdQComboBox.currentText()

        current_hd_widget  = self.stack_hd_widgets[current_hd]
        current_from_stack = self.stack_from_widgets[current_hd_widget]["StackWidget"]
        current_from_widget = self.stack_from_widgets[current_hd_widget][dump_from]

        self.change_page(current_from_stack, current_from_widget)

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
        self.ui.generatePassphraseCharacterQCheckBox.setChecked(True)

        self.ui.generateSeedCardanoTypeQComboBox.addItems(Cardano.TYPES.get_cardano_types())
        self.ui.generateSeedMnemonicTypeQComboBox.addItems(ElectrumV2Mnemonic.mnemonic_types.keys())
        self.ui.generateMnemonicTypeQComboBox.addItems(ElectrumV2Mnemonic.mnemonic_types.keys())

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
        self.ui.generateMnemonicLanguageQComboBox.addItems([i.title() for i in MNEMONICS.mnemonic(mnemonic_client).languages])

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
            kwargs["mnemonic_type"] =  self.ui.generateMnemonicTypeQComboBox.currentText()

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
        cardano_type = self.ui.generateSeedCardanoTypeQComboBox.currentText() 
        if cardano_type == 'byron-ledger' or cardano_type == 'shelley-ledger':
            self.ui.generateSeedPassphraseGenerateQLineEdit.setEnabled(True)
        else:
            self.ui.generateSeedPassphraseGenerateQLineEdit.setText(None)
            self.ui.generateSeedPassphraseGenerateContainerQFrame.setEnabled(False)

    def _generate_seed(self):
        seed_client = self.ui.generateSeedClientQComboBox.currentText()
        mnemonic_type = self.ui.generateSeedMnemonicTypeQComboBox.currentText()
        cardano_type = self.ui.generateSeedCardanoTypeQComboBox.currentText()
        mnemonic = self.ui.generateSeedMnemonicQLineEdit.text()
        passphrase = self.ui.generateSeedPassphraseGenerateQLineEdit.text()
        output = None

        try:
            if len(mnemonic) == 0:
                raise Exception("mnemonic is required to generate seed!")
            elif CardanoSeed.name() == seed_client:
                seed = CardanoSeed.from_mnemonic(mnemonic=mnemonic, cardano_type=cardano_type, passphrase=passphrase)
            elif ElectrumV2Seed.name() == seed_client:
                seed = ElectrumV2Seed.from_mnemonic(mnemonic=mnemonic, mnemonic_type=mnemonic_type, passphrase=passphrase)
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

    def change_page(self, stacked_name: str, widget_name : str) -> None:
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
        result = subprocess.run(
                    f'hdwallet {self.ui.outputTerminalQLineEdit.text()}',
                    shell=True, 
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )

        output = result.stderr if result.stderr else result.stdout
        self.ui.outputTerminalQLineEdit.setText(None)
        self.println(output.decode())

    def println(self, s):
        #just for now

        if isinstance(s, dict):
            newtext = json.dumps(s, indent=4)  
        else:
            newtext = str(s)
       
        self.ui.outputTerminalQTextEdit.append(f"{newtext}\n\n")

    def toggle_expand(self):
        if self.toggle_expand_terminal.isChecked():
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)     
            self.showNormal()

            self.layout().removeWidget(self.ui.outputQFrame)
            self.detached_window = DetachedWindow(self)
            self.detached_window.setWindowTitle("Hierarchical Deterministic Wallet - Output")
            self.detached_window.resize(self.ui.outputQFrame.width(), self.ui.outputQFrame.height())

            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self.ui.outputQFrame)

            self.detached_window.setLayout(layout)
            self.detached_window.show()
            self.detached_window.setStyleSheet(self.styleSheet())
            self.setMinimumWidth(0)

            if not self.isMaximized():
                self.resize(self.width() - self.ui.outputQFrame.width(), self.height())

        else:
            if self.detached_window:
                self.detached_window.close()
                self.detached_window = None

            self.ui.centralwidget.layout().addWidget(self.ui.outputQFrame)

            self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
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
            0, 0, self.ui.noLayoutQWidget.width(), self.ui.outputWidgetTopContainerQWidget.height()
        ))
        self.ui.outputTerminalQWidget.setGeometry(QRect(
            0, 0, self.ui.noLayoutQWidget.width(), self.ui.noLayoutQWidget.height()
        ))
        self.ui.outputWidgetTopContainerQWidget.raise_()
        self.ui.outputTerminalQWidget.lower()

    def resizeEvent(self, event) -> None:
        self.update_terminal_ui()

    def show(self):
        super(MyMainWindow, self).show()
        self.update_terminal_ui()


if __name__ == "__main__":
    app = QApplication([])

    main_window = MyMainWindow()
    main_window.show()

    app.exec()
