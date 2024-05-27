import string
from random import choice


from PySide6.QtGui import QIntValidator

from hdwallet.cryptocurrencies import Cardano, CRYPTOCURRENCIES

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

from hdwallet.seeds import (
    AlgorandSeed,
    BIP39Seed,
    CardanoSeed,
    ElectrumV1Seed,
    ElectrumV2Seed,
    MoneroSeed,
    SEEDS
)

class Generate:
    def __init__(self, app):
        self.app = app
        self.ui = app.ui
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

        self.app.println(output)

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

        self.app.println(output)

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

        self.app.println(output)

    def _generate_passphrase(self):

        if len(self.ui.generateLengthQLineEdit.text()) == 0:
            self.app.println("ERROR: passpharse length is required")
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

        self.app.println(output)
