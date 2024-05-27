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

class CoreApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup UI Stuff


        self._setup_generate_stack()
        self._setup_dump_stack()

