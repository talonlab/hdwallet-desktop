import subprocess
from random import choice
import string

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QPushButton, QVBoxLayout, QHBoxLayout, QFrame,
    QStackedWidget
)
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QIntValidator

import string


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

from hdwallet.cryptocurrencies import Cardano

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

        # Setup UI Stuff
        self.setWindowTitle("Hierarchical Deterministic Wallet")

        self.load_stylesheet("ui/css/dark-style.css")

        self.toggle_expand_terminal = SvgButton(
            parent_widget=self.ui.expandTerminalQFrame,
            icon_path="ui/images/icon_maximize.svg",
            alt_icon_path="ui/images/icon_minimize.svg",
            icon_width=17,
            icon_height=17
        )
        self.toggle_expand_terminal.setCheckable(True)
        self.toggle_expand_terminal.toggled.connect(self.toggle_expand)
        self.ui.outputTerminalQLineEdit.returnPressed.connect(self.process_command)

        self.ui.generateQPushButton.clicked.connect(lambda: self.change_page("hdwalletQStackedWidget", "generatePageQStackedWidget"))
        self.ui.dumpQPushButton.clicked.connect(lambda: self.change_page("hdwalletQStackedWidget", "dumpsPageQStackedWidget"))

        self._setup_generate_stack()

    def _setup_generate_stack(self):
        self.ui.generateEntropyClientQComboBox.addItems(ENTROPIES.names())
        self.ui.generateEntropyClientQComboBox.currentIndexChanged.connect(self._generate_entropy_change)
        self.ui.generateEntropyClientQComboBox.setCurrentText(BIP39Entropy.name())
        self.ui.generateEntropyClientAndStrengthQPushButton.clicked.connect(self._generate_entropy)

        self.ui.generateMnemonicClientQComboBox.addItems(MNEMONICS.names())
        self.ui.generateMnemonicClientQComboBox.currentIndexChanged.connect(self._generate_mnemonic_change)
        self.ui.generateMnemonicClientQComboBox.setCurrentText(BIP39Mnemonic.name())
        self.ui.generateMnemonicClientWordsAndLanguageQPushButton.clicked.connect(self._generate_mnemonic)

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
        self.println(gen_entropy)


    def _generate_mnemonic_change(self):
        mnemonic_client = self.ui.generateMnemonicClientQComboBox.currentText()
        self.ui.generateMnemonicWordsQComboBox.clear()
        self.ui.generateMnemonicLanguageQComboBox.clear()

        self.ui.generateMnemonicWordsQComboBox.addItems(
            map(
                str, MNEMONICS.mnemonic(mnemonic_client).words_list
            )
        )
        self.ui.generateMnemonicLanguageQComboBox.addItems(MNEMONICS.mnemonic(mnemonic_client).languages)

        self.ui.generateMnemonicWordsQComboBox.setCurrentIndex(0)
        self.ui.generateMnemonicLanguageQComboBox.setCurrentText('english')


    def _generate_mnemonic(self):
        mnemonic_client = self.ui.generateMnemonicClientQComboBox.currentText()
        word = self.ui.generateMnemonicWordsQComboBox.currentText()
        lang = self.ui.generateMnemonicLanguageQComboBox.currentText()
        gen_mnemonic = MNEMONICS.mnemonic(mnemonic_client).from_words(
                            words=int(word),
                            language=lang
                        )

        self.println(gen_mnemonic)

    def _generate_seed_change(self):
        seed_client = self.ui.generateSeedClientQComboBox.currentText()

        self.ui.generateSeedMnemonicTypeQComboBox.clear()
        self.ui.generateSeedCardanoTypeQComboBox.clear()

        self.ui.generateSeedMnemonicTypeContainerQFrame.setEnabled(False)
        self.ui.generateSeedCardanoTypeContainerQFrame.setEnabled(False)

        self.ui.generateSeedPassphraseGenerateQLineEdit.setText(None)
        self.ui.generateSeedPassphraseGenerateContainerQFrame.setEnabled(False)

        if CardanoSeed.name() == seed_client:
            self.ui.generateSeedCardanoTypeContainerQFrame.setEnabled(True)
            self.ui.generateSeedCardanoTypeQComboBox.addItems(Cardano.TYPES.get_cardano_types())
            self.ui.generateSeedCardanoTypeQComboBox.setCurrentIndex(0)
        elif ElectrumV2Seed.name() == seed_client:
            self.ui.generateSeedMnemonicTypeContainerQFrame.setEnabled(True)
            self.ui.generateSeedMnemonicTypeQComboBox.addItems(ElectrumV2Mnemonic.mnemonic_types.keys())
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
        passphrase = None if passphrase == '' else passphrase

        output = None

        try:
            if len(mnemonic) == 0:
                output = "Error: mnemonic is required to generate seed!"
            elif CardanoSeed.name() == seed_client:
                output = CardanoSeed.from_mnemonic(mnemonic=mnemonic, cardano_type=cardano_type, passphrase=passphrase)
            elif ElectrumV2Seed.name() == seed_client:
                output = ElectrumV2Seed.from_mnemonic(mnemonic=mnemonic, mnemonic_type=mnemonic_type, passphrase=passphrase)
            elif BIP39Seed.name() == seed_client:
                output = SEEDS.seed(seed_client).from_mnemonic(mnemonic=mnemonic, passphrase=passphrase)
            else:
                output = SEEDS.seed(seed_client).from_mnemonic(mnemonic=mnemonic)
        except Exception as e:
            output = str(e)

        self.println(output)

    def _generate_passphrase(self):

        if len(self.ui.generateLengthQLineEdit.text()) == 0:
            self.println("Error: passpharse length is required")
            return None

        length = int(self.ui.generateLengthQLineEdit.text())
        upper = self.ui.generatePassphraseUpperCaseQCheckBox.isChecked()
        lower = self.ui.generatePassphraseLowerCaseQCheckBox.isChecked()
        special = self.ui.generatePassphraseNumberQCheckBox.isChecked()
        digit = self.ui.generatePassphraseCharacterQCheckBox.isChecked()


        characters = string.ascii_lowercase if lower else ''
        characters += string.ascii_uppercase if upper else ''
        characters += string.digits if digit else ''
        characters += string.punctuation if special else ''

        if not any([upper, lower, special, digit]):
            self.println("Error: At least one of upper, lower, special, or digit must be selected")
        else:
            pp = "".join(choice(characters) for _ in range(length))
            self.println(pp)

    def change_page(self, stacked_name: str, widget_name : str) -> None:
        qStackedWidget: Optional[QStackedWidget] = self.findChild(QStackedWidget, stacked_name)

        if qStackedWidget is None:
            print(f"QStackWidget not found: {stacked_name}")
            return None

        qWidget: Optional[QWidget] = qStackedWidget.findChild(QWidget, widget_name)

        if qStackedWidget and qWidget: 
            qStackedWidget.setCurrentWidget(qWidget)
        else:
            print(f"Error changing page: '{stacked_name}' '{widget_name}'")


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
        oldtext = self.ui.outputTerminalQTextEdit.toPlainText()
        self.ui.outputTerminalQTextEdit.setText(oldtext + "\n\n" + str(s))        

    def toggle_expand(self):
        if self.toggle_expand_terminal.isChecked():
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)     
            self.showNormal()

            self.layout().removeWidget(self.ui.outputQFrame)
            self.detached_window = DetachedWindow(self)
            self.detached_window.setWindowTitle("Hierarchical Deterministic Wallet - Output")
            self.detached_window.resize(self.ui.outputQFrame.width(), self.ui.outputQFrame.height())

            layout = QVBoxLayout()
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

if __name__ == "__main__":
    app = QApplication([])

    main_window = MyMainWindow()
    main_window.show()

    app.exec()
