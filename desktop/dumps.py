#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import inspect
import functools
import time
import json
import os
from typing import *
from collections import OrderedDict

from PySide6.QtWidgets import (
    QPushButton, QFileDialog, QComboBox, QFrame
)
from PySide6.QtCore import QThreadPool

from bip38 import (
    cryptocurrencies, BIP38
)

from hdwallet import HDWallet
from hdwallet.hds import HDS
from hdwallet.const import ELECTRUM_V2_MODES
from hdwallet.cryptocurrencies import (
    Cardano, CRYPTOCURRENCIES
)
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

from hdwallet.derivations import (
    IDerivation, DERIVATIONS,
    CustomDerivation, BIP44Derivation, BIP49Derivation, BIP84Derivation,
    BIP86Derivation, ElectrumDerivation, CIP1852Derivation, MoneroDerivation, HDWDerivation,
    CHANGES
)

from hdwallet.const import SLIP10_SECP256K1_CONST

from hdwallet.exceptions import MnemonicError, DerivationError

from desktop.utils.worker import (
    Worker, WorkerSignals
)

from desktop.utils import set_red_border, clear_all_borders


class Dumps:

    def __init__(self, app):
        self.app = app
        self.ui = app.ui
        self._setup_dump_stack()

    def _setup_dump_stack(self):

        self.errboxes = [
            self.ui.dumpsStackQGroupBox,
            self.ui.derivationQGroupBox,
            self.ui.dumpsFormatKeysContainerQGroupBox
        ]

        self.ui.dumpsSaveAndGenerateQPushButton.clicked.connect(
            lambda: self._dumps(save=True)
        )
        self.ui.dumpsGenerateQPushButton.clicked.connect(self._dumps)

        self.script_semantics = ["P2WPKH", "P2WPKH_IN_P2SH", "P2WSH", "P2WSH_IN_P2SH"]

        self.stack_hd_widgets = {
            "BIP32": "bipsPageQWidget",
            "BIP44": "bipsPageQWidget",
            "BIP49": "bipsPageQWidget",
            "BIP84": "bipsPageQWidget",
            "BIP86": "bipsPageQWidget",
            "BIP141": "bipsPageQWidget",
            "Cardano": "cardanoPageQWidget",
            "Electrum-V1": "electrumV1PageQWidget",
            "Electrum-V2": "electrumV2PageQWidget",
            "Monero": "moneroPageQWidget"
        }

        self.hd_undrivable_methods = {
            "BIP32": ["WIF", "Private key", "Public key"],
            "BIP44": ["WIF", "Private key", "Public key"],
            "BIP49": ["WIF", "Private key", "Public key"],
            "BIP84": ["WIF", "Private key", "Public key"],
            "BIP86": ["WIF", "Private key", "Public key"],
            "BIP141": ["WIF", "Private key", "Public key"],
            "Electrum-V1": [],
            "Electrum-V2": [],
            "Cardano": ["Private key", "Public key"],
            "Monero": []
        }

        self.hd_allowed_derivation = {
            "BIP32": ["Custom", "BIP44", "BIP49", "BIP84", "BIP86", "BIP141", "CIP1852", "HDW"],
            "BIP32XPUB": ["Custom", "BIP141"],
            "BIP44": ["BIP44"],
            "BIP49": ["BIP49"],
            "BIP84": ["BIP84"],
            "BIP86": ["BIP86"],
            "BIP141": ["BIP141"],
            "Cardano": ["Custom", "BIP44", "CIP1852"],
            "CardanoXPUB": ["Custom"],
            "Electrum-V1": ["Electrum"],
            "Electrum-V2": ["Electrum"],
            "Monero": ["Monero"]
        }

        self.derivation_tab = OrderedDict()

        self.derivation_tab["Custom"] = {
            "button": self.ui.customTabQPushButton,
            "widget": "customQStackedWidgetPage"
        }

        self.derivation_tab["BIP44"] = {
            "button": self.ui.bip44TabQPushButton,
            "widget": "bip44QStackedWidgetPage"
        }

        self.derivation_tab["BIP49"] = {
            "button": self.ui.bip49TabQPushButton,
            "widget": "bip49QStackedWidgetPage"
        }

        self.derivation_tab["BIP84"] = {
            "button": self.ui.bip84TabQPushButton,
            "widget": "bip84QStackedWidgetPage"
        }

        self.derivation_tab["BIP86"] = {
            "button": self.ui.bip86TabQPushButton,
            "widget": "bip86QStackedWidgetPage"
        }

        self.derivation_tab["BIP141"] = {
            "button": self.ui.bip141TabQPushButton,
            "widget": "bip141QStackedWidgetPage"
        }

        self.derivation_tab["CIP1852"] = {
            "button": self.ui.cip1852TabQPushButton,
            "widget": "cip1852QStackedWidgetPage"
        }

        self.derivation_tab["Electrum"] = {
            "button": self.ui.electrumTabQPushButton,
            "widget": "electrumQStackedWidgetPage"
        }

        self.derivation_tab["Monero"] = {
            "button": self.ui.moneroTabQPushButton,
            "widget": "moneroQStackedWidgetPage"
        }

        self.derivation_tab["HDW"] = {
            "button": self.ui.hdwTabQPushButton,
            "widget": "hdwQStackedWidgetPage"
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

        self.bip38_cryptocurrencies = {
            name: cls for name, cls in inspect.getmembers(cryptocurrencies, inspect.isclass)
            if issubclass(cls, cryptocurrencies.ICryptocurrency)
        }

        self.custom_paths = {
            "Custom": None,
            "Bitcoin Core": "m/0'/0'",
            "blockchain.info": "m/44'/0'/0'",
            "MultiBit HD": "m/0'/0",
            "Coinomi, Ledger": "m/44'/0'/0'"
        }

        for name, data in self.derivation_tab.items():
            data["button"].clicked.connect(
                functools.partial(self.derivation_tab_changed, data["widget"], data["button"]))

        self._update_terminal_state(False, False)
        self.ui.stopTerminalQPushButton.clicked.connect(
            lambda: self._update_terminal_state(False, True)
        )

        # Algorand clients
        algorand_clients = ["Algorand", "BIP39"]
        self.algorand_client_combo_boxes = [
            (self.ui.bipFromEntropyClientQComboBox, self.ui.bipFromEntropyClientContainerQFrame),
            (self.ui.bipFromMnemonicClientQComboBox, self.ui.bipFromMnemonicClientContainerQFrame),
            (self.ui.bipFromSeedClientQComboBox, self.ui.bipFromSeedClientContainerQFrame)
        ]

        self.cardano_client_combo_boxes = [
            self.ui.cardanoFromEntropyClientQComboBox,
            self.ui.cardanoFromMnemonicClientQComboBox,
            self.ui.cardanoFromSeedClientQComboBox
        ]

        self.electrumv1_client_combo_boxes = [
            self.ui.electrumV1FromEntropyClientQComboBox,
            self.ui.electrumV1FromMnemonicClientQComboBox,
            self.ui.electrumV1FromSeedClientQComboBox
        ]

        self.electrumv2_client_combo_boxes = [
            self.ui.electrumV2FromEntropyClientQComboBox,
            self.ui.electrumV2FromMnemonicClientQComboBox,
            self.ui.electrumV2FromSeedClientQComboBox
        ]

        self.monero_client_combo_boxes = [
            self.ui.moneroFromEntropyClientQComboBox,
            self.ui.moneroFromMnemonicClientQComboBox,
            self.ui.moneroFromSeedClientQComboBox
        ]

        combo_boxes_with_clients = [
            (self.algorand_client_combo_boxes, algorand_clients),  
            (self.cardano_client_combo_boxes, ["Cardano"]),
            (self.electrumv1_client_combo_boxes, ["Electrum-V1"]),
            (self.electrumv2_client_combo_boxes, ["Electrum-V2"]),
            (self.monero_client_combo_boxes, ["Monero"])
        ]

        for combo_box_list, clients in combo_boxes_with_clients:
            for combo_box_item in combo_box_list:
                if isinstance(combo_box_item, tuple):
                    combo_box = combo_box_item[0]
                else:
                    combo_box = combo_box_item

                combo_box.addItems(clients) if len(clients) > 1 else combo_box.addItem(clients[0])
                combo_box.setCurrentIndex(0)

        self.ui.customClientQComboBox.clear()
        self.ui.customClientQComboBox.addItems(self.custom_paths.keys())
        self.ui.customClientQComboBox.currentIndexChanged.connect(self._custom_path_client_changed)
        self.ui.customClientQComboBox.setCurrentIndex(0)

        self.ui.hdwEccQLineEdit.setText(str(list(HDWDerivation.eccs.keys())))
        self.ui.hdwEccQFrame.setEnabled(False)

        self.ui.dumpsExcludeOrIncludeQLabel.setText("Exclude")
        self.ui.dumpsFormatQComboBox.currentTextChanged.connect(self._dump_format_changed)

        self.ui.dumpsHdQComboBox.currentIndexChanged.connect(self._dump_hd_changed)
        self.ui.dumpsFromQComboBox.currentIndexChanged.connect(self._dump_from_changed)

        self.ui.dumpsCryptocurrencyQComboBox.clear()
        self.ui.dumpsCryptocurrencyQComboBox.addItems(CRYPTOCURRENCIES.names())
        self.ui.dumpsCryptocurrencyQComboBox.currentIndexChanged.connect(self._dumps_crypto_change)
        self.ui.dumpsCryptocurrencyQComboBox.setCurrentText("Bitcoin")

        self.ui.bipFromEntropyLanguageQComboBox.clear()
        self.ui.bipFromEntropyLanguageQComboBox.addItems([i.title() for i in BIP39Mnemonic.languages])
        self.ui.bipFromEntropyLanguageQComboBox.setCurrentText("English")

        self.ui.cardanoFromEntropyLanguageQComboBox.clear()
        self.ui.cardanoFromEntropyLanguageQComboBox.addItems([i.title() for i in BIP39Mnemonic.languages])
        self.ui.cardanoFromEntropyLanguageQComboBox.setCurrentText("English")

        self.ui.electrumV1FromEntropyLanguageQComboBox.clear()
        self.ui.electrumV1FromEntropyLanguageQComboBox.addItems([i.title() for i in ElectrumV1Mnemonic.languages])
        self.ui.electrumV1FromEntropyLanguageQComboBox.setCurrentText("English")

        self.ui.electrumV2FromEntropyLanguageQComboBox.clear()
        self.ui.electrumV2FromEntropyLanguageQComboBox.addItems([i.title() for i in ElectrumV2Mnemonic.languages])
        self.ui.electrumV2FromEntropyLanguageQComboBox.setCurrentText("English")

        self.ui.moneroFromEntropyLanguageQComboBox.clear()
        self.ui.moneroFromEntropyLanguageQComboBox.addItems([i.title() for i in MoneroMnemonic.languages])
        self.ui.moneroFromEntropyLanguageQComboBox.setCurrentText("English")

        electrum_v2_modes = [i.title() for i in ELECTRUM_V2_MODES.get_modes()]

        self.ui.electrumV2FromEntropyMnemonicTypeQComboBox.addItems([i.title() for i in ElectrumV2Mnemonic.mnemonic_types.keys()])
        self.ui.electrumV2FromEntropyModeQComboBox.addItems(electrum_v2_modes)
        self.ui.electrumV2FromEntropyMnemonicTypeQComboBox.setCurrentIndex(0)
        self.ui.electrumV2FromEntropyModeQComboBox.setCurrentIndex(0)

        self.ui.electrumV2FromMnemonicMnemonicTypeQComboBox.addItems([i.title() for i in ElectrumV2Mnemonic.mnemonic_types.keys()])
        self.ui.electrumV2FromMnemonicModeQComboBox.addItems(electrum_v2_modes)
        self.ui.electrumV2FromMnemonicMnemonicTypeQComboBox.setCurrentIndex(0)
        self.ui.electrumV2FromMnemonicModeQComboBox.setCurrentIndex(0)

        self.ui.electrumV2FromSeedModeQComboBox.addItems(electrum_v2_modes)
        self.ui.electrumV2FromSeedModeQComboBox.setCurrentIndex(0)

        # BIPs WIF BIP38 events
        self.ui.bipFromWIFBIP38PassphraseContainerQFrame.setEnabled(False)
        self.ui.bipFromWIFBIP38PassphraseQLineEdit.setEnabled(False)
        self.ui.bipFromWIFBIP38PassphraseQCheckBox.setChecked(False)
        self.ui.bipFromWIFBIP38PassphraseQCheckBox.toggled.connect(
            lambda:
                self._bip38_toggled(
                    self.ui.bipFromWIFBIP38PassphraseQCheckBox,
                    self.ui.bipFromWIFBIP38PassphraseQLineEdit,
                    self.ui.bipFromWIFQLabel,
                    self.ui.bipFromWIFBIP38PassphraseContainerQFrame
                )
        )

        # ElectrumV2 WIF BIP38 events
        self.ui.electrumV1FromWIFBIP38PassphraseContainerQFrame.setEnabled(False)
        self.ui.electrumV1FromWIFBIP38PassphraseQLineEdit.setEnabled(False)
        self.ui.electrumV1FromWIFBIP38PassphraseQCheckBox.setChecked(False)
        self.ui.electrumV1FromWIFBIP38PassphraseQCheckBox.toggled.connect(
            lambda:
                self._bip38_toggled(
                    self.ui.electrumV1FromWIFBIP38PassphraseQCheckBox,
                    self.ui.electrumV1FromWIFBIP38PassphraseQLineEdit,
                    self.ui.electrumV1FromWIFQLabel,
                    self.ui.electrumV1FromWIFBIP38PassphraseContainerQFrame
                )
        )


        cardano_and_address_type = [
            (
                self.ui.cardanoFromEntropyCardanoTypeQComboBox,
                self.ui.cardanoFromEntropyAddressTypeQComboBox,
                self.ui.cardanoFromEntropyStakingQLineEdit,
                self.ui.cardanoFromEntropyAddressTypeContainerQFrame,
                self.ui.cardanoFromEntropyStakingContainerQFrame
            ),
            (
                self.ui.cardanoFromMnemonicCardanoTypeQComboBox,
                self.ui.cardanoFromMnemonicAddressTypeQComboBox,
                self.ui.cardanoFromMnemonicStakingQLineEdit,
                self.ui.cardanoFromMnemonicAddressTypeContainerQFrame,
                self.ui.cardanoFromMnemonicStakingContainerQFrame

            ),
            (
                self.ui.cardanoFromPrivateKeyCardanoTypeQComboBox,
                self.ui.cardanoFromPrivateKeyAddressTypeQComboBox,
                self.ui.cardanoFromPrivateKeyStakingQLineEdit,
                self.ui.cardanoFromPrivateKeyAddressTypeContainerQFrame,
                self.ui.cardanoFromPrivateKeyStakingContainerQFrame
            ),
            (
                self.ui.cardanoFromPublicKeyCardanoTypeQComboBox,
                self.ui.cardanoFromPublicKeyAddressTypeQComboBox,
                self.ui.cardanoFromPublicKeyStakingQLineEdit,
                self.ui.cardanoFromPublicKeyAddressTypeContainerQFrame,
                self.ui.cardanoFromPublicKeyStakingContainerQFrame
            ),
            (
                self.ui.cardanoFromSeedCardanoTypeQComboBox,
                self.ui.cardanoFromSeedAddressTypeQComboBox,
                self.ui.cardanoFromSeedStakingQLineEdit,
                self.ui.cardanoFromSeedAddressTypeContainerQFrame,
                self.ui.cardanoFromSeedStakingContainerQFrame
            ),
            (
                self.ui.cardanoFromXPrivateKeyCardanoTypeQComboBox,
                self.ui.cardanoFromXPrivateKeyAddressTypeQComboBox,
                self.ui.cardanoFromXPrivateKeyStakingQLineEdit,
                self.ui.cardanoFromXPrivateKeyAddressTypeContainerQFrame,
                self.ui.cardanoFromXPrivateKeyStakingContainerQFrame
            ),
            (
                self.ui.cardanoFromXPublicKeyCardanoTypeQComboBox,
                self.ui.cardanoFromXPublicKeyAddressTypeQComboBox,
                self.ui.cardanoFromXPublicKeyStakingQLineEdit,
                self.ui.cardanoFromXPublicKeyAddressTypeContainerQFrame,
                self.ui.cardanoFromXPublicKeyStakingContainerQFrame
            ),
        ]


        #list of cardano types
        cardano_list = [i.title() for i in Cardano.TYPES.get_cardano_types()]

        #Byron options removed from private and public 
        removed_list_pri =[
            self.ui.cardanoFromPrivateKeyCardanoTypeQComboBox,
            self.ui.cardanoFromPublicKeyCardanoTypeQComboBox
        ]
        cardano_list_removed = [item for item in cardano_list if not item.lower().startswith('byron')]

        #list of address
        c_address_list = ["Payment", "Staking"]

        for pair in cardano_and_address_type:
            if isinstance(pair[0], QComboBox):
                pair[0].clear()
            if isinstance(pair[1], QComboBox):
                pair[1].clear()
            if pair[0] in removed_list_pri:
                pair[0].addItems(cardano_list_removed)
                pair[0].setCurrentIndex(0)#set selected combo to Shelly-Icarus
            else:
                pair[0].addItems(cardano_list)   
                pair[0].setCurrentIndex(3)#set selected combo to Shelly-Icarus

            pair[1].addItems(c_address_list)
            pair[0].currentIndexChanged.connect(functools.partial(self.__pair_ca_address_type, pair[1], pair[0], pair[3]))
            pair[1].currentIndexChanged.connect(functools.partial(self.__pair_addr_staking, pair[1], pair[2], pair[4]))
            pair[2].setEnabled(False)
            pair[4].setEnabled(False)
            

        self.ui.cardanoFromXPublicKeyStrictQCheckBox.setChecked(True)
        self.ui.cardanoFromXPrivateKeyStrictQCheckBox.setChecked(True)
        self.ui.bipFromXPrivateKeyStrictQCheckBox.setChecked(True)
        self.ui.bipFromXPublicKeyStrictQCheckBox.setChecked(True)

    def __pair_ca_address_type(self, c_addr, c_list, cd_addr, idx):
        if c_list.currentText().lower().startswith("shelley"):
            c_addr.setEnabled(True)
            cd_addr.setEnabled(True)
            c_addr.setCurrentIndex(0)
        else:
            c_addr.setCurrentIndex(-1)
            c_addr.setEnabled(False)
            cd_addr.setEnabled(False)

    def __pair_addr_staking(self, c_addr, staking, cd_addr,idx):
        if c_addr.currentText() == "Payment":
            staking.setEnabled(True)
            cd_addr.setEnabled(True)
        else:
            staking.setText(None)
            staking.setEnabled(False)
            cd_addr.setEnabled(False)

    def _file_locator(self, format):
        options = QFileDialog.Options()
        options |= QFileDialog.DontConfirmOverwrite
        if format == 'JSON':  save_as = 'JSON Files (*.json)'
        elif format == 'CSV': save_as = 'CSV Files (*.csv)'
        home_dir = os.path.expanduser("~")
        filename, _ = QFileDialog.getSaveFileName(
            None,
            'Save File',
            os.path.join(home_dir, 'hdwallet'),
            save_as,
            options=options
        )

        return filename

    def _dumps(self, save=False):
        save_filepath = None
        clear_all_borders(self.errboxes)
        if save:
            save_filepath = self._file_locator(self.ui.dumpsFormatQComboBox.currentText())
            if save_filepath == '': return None

        def _error(e):
            self.app.println(f"ERROR: {e}")
            if isinstance(e, DerivationError):  
                set_red_border(self.ui.derivationQGroupBox)
            elif isinstance(e, ExportFormatError):  
                set_red_border(self.ui.dumpsFormatKeysContainerQGroupBox)
            else:
                set_red_border(self.ui.dumpsStackQGroupBox)
        
        def _task_ended(): 
            self.ui.dumpsGenerateQPushButton.setEnabled(True)
            self._update_terminal_state(False, False)

        self.ui.dumpsGenerateQPushButton.setEnabled(False)

        mysignals = WorkerSignals()
        job = Worker(self.__dumps, signal=mysignals, save_filepath=save_filepath)
        job.signals = mysignals

        job.signals.interval_output.connect(self.app.println)

        job.signals.interval_error.connect(_error)
        job.signals.interval_finished.connect(self.app.println)
        job.signals.interval_error.connect(_task_ended)
        job.signals.interval_finished.connect(_task_ended)

        self._update_terminal_state(True, False)

        QThreadPool.globalInstance().start(job)

    def __dumps(self, signal, save_filepath):
        current_hd = self.ui.dumpsHdQComboBox.currentText()
        dump_from = self.ui.dumpsFromQComboBox.currentText()
        network = self.ui.dumpsNetworkQComboBox.currentText()
        dformat = self.ui.dumpsFormatQComboBox.currentText()
        exclude_include = [p.strip() for p in self.ui.dumpsExcludeOrIncludeQLineEdit.text().split(",")]

        saved_file = None
        if save_filepath != None:
            saved_file = open(save_filepath, 'w')
            signal.interval_finished.connect(saved_file.close)

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
                    elif derivation_name == "HDW":
                        _derivation: IDerivation = DERIVATIONS.derivation(
                            name=derivation_name
                        ).__call__(
                            account=current_derivation[0][0],
                            ecc=current_derivation[1][0],
                            address=current_derivation[2][0]
                        )
                    else:
                        _derivation: IDerivation = DERIVATIONS.derivation(
                            name=derivation_name
                        ).__call__(
                            path="m/" + "/".join(
                                [str(item[0]) + "'" if item[1] else str(item[0]) for item in current_derivation]
                            )
                        )


                    hd.update_derivation(
                        derivation=_derivation
                    )


                    csv_data: List[str] = []

                    if dformat == "CSV":
                        dump = hd.dump(exclude={"root"})

                        try:
                            for key in [keys.split(":") for keys in exclude_include]:
                                if len(key) == 2:
                                    csv_data.append(dump[key[0]][key[1]])
                                else:
                                    csv_data.append(dump[key[0]])
                            out = ", ".join(map(str, csv_data))

                        except Exception as e:
                            raise ExportFormatError(e)

                    else:
                        dump = hd.dump(exclude={'root', *exclude_include})
                        out = json.dumps(dump, indent=4, ensure_ascii=False)

                    signal.interval_output.emit(out)
                    
                    if hd_kwargs["cryptocurrency"].ECC.NAME != "SLIP10-Secp256k1" and SLIP10_SECP256K1_CONST.USE == "coincurve":
                        time.sleep(0.03)
                    
                    if saved_file != None:
                        saved_file.write(f"{out}\n")
                    return [_derivation.path()]

                path: List[str] = []
                if len(derivations[0]) == 3:
                    for value in range(derivations[0][0], derivations[0][1] + 1):
                        if self.terminal_cancelled:
                           break
                        path += drive_helper(
                            derivations[1:], current_derivation + [(value, derivations[0][2])]
                        )
                else:
                    path += drive_helper(
                        derivations[1:], current_derivation + [derivations[0]]
                    )
                return path

            return drive_helper(args)

        if dformat == "CSV":
            if derivation is None:
                return None
            drive(*derivation.derivations())

        else:
            if derivation != None:                
                if "root" not in exclude_include:
                    root = json.dumps(hd.dump(exclude={"derivation", *exclude_include}), indent=4, ensure_ascii=False)
                    
                    signal.interval_output.emit(root)

                    if saved_file != None:
                        saved_file.write(f"{root}\n")

                drive(*derivation.derivations())
            else:
                result = json.dumps(hd.dump(exclude=set(exclude_include)), indent=4, ensure_ascii=False)

                if saved_file != None:
                    saved_file.write(result)
                return result

        return None


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

        elif current_tab == "HDW":
            return HDWDerivation(
                account=self.ui.hdwAccountQLineEdit.text(),
                ecc=self.ui.hdwEccQComboBox.currentText(),
                address=self.ui.hdwAddressQLineEdit.text()
            )

    def _dump_bips(self, dump_from, hd_kwargs):
        if dump_from == "Entropy":
            hd_kwargs["language"] = self.ui.bipFromEntropyLanguageQComboBox.currentText().lower()
            hd_kwargs["passphrase"] = self.ui.bipFromEntropyPassphraseQLineEdit.text()
            hd_kwargs["public_key_type"] = self.ui.bipFromEntropyPublicKeyTypeQComboBox.currentText().lower()
            
            entropy_class = ENTROPIES.entropy(self.ui.bipFromEntropyClientQComboBox.currentText())
            
            return HDWallet(**hd_kwargs).from_entropy(
                entropy_class(
                    entropy=self.ui.bipFromEntropyGenerateQLineEdit.text()
                )
            )
        elif dump_from == "Mnemonic":
            hd_kwargs["passphrase"] = self.ui.bipFromMnemonicPassphraseQLineEdit.text()
            hd_kwargs["public_key_type"] = self.ui.bipFromMnemonicPublicKeyTypeQComboBox.currentText().lower()

            mnemonic_class = MNEMONICS.mnemonic(self.ui.bipFromMnemonicClientQComboBox.currentText())

            return HDWallet(**hd_kwargs).from_mnemonic(
                mnemonic_class(
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

            seed_class = SEEDS.seed(self.ui.bipFromSeedClientQComboBox.currentText())

            return HDWallet(**hd_kwargs).from_seed(
                BIP39Seed(
                    seed=self.ui.bipFromSeedsQLineEdit.text()
                )
            )
        elif dump_from == "WIF":
            hd_kwargs["public_key_type"] = self.ui.bipFromWIFPublicKeyTypeQComboBox.currentText().lower()
            wif = self.ui.bipFromWIFQLineEdit.text()

            if self.ui.bipFromWIFBIP38PassphraseQCheckBox.isChecked():
                crypto_name = hd_kwargs["cryptocurrency"].NAME
                passphrase = self.ui.bipFromWIFBIP38PassphraseQLineEdit.text()

                bip38: BIP38 = BIP38(
                  cryptocurrency=self.bip38_cryptocurrencies[crypto_name] , network=hd_kwargs["network"]
                )
                wif = bip38.decrypt(encrypted_wif=wif, passphrase=passphrase)

            return HDWallet(**hd_kwargs).from_wif(
                wif=wif
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
            wif = self.ui.electrumV1FromWIFQLineEdit.text()

            if self.ui.electrumV1FromWIFBIP38PassphraseQCheckBox.isChecked():
                crypto_name = hd_kwargs["cryptocurrency"].NAME
                passphrase = self.ui.electrumV1FromWIFBIP38PassphraseQLineEdit.text()

                bip38: BIP38 = BIP38(
                  cryptocurrency=self.bip38_cryptocurrencies[crypto_name] , network=hd_kwargs["network"]
                )
                wif = bip38.decrypt(encrypted_wif=wif, passphrase=passphrase)


            return HDWallet(**hd_kwargs).from_wif(
                wif=wif
            )

    def _dump_ev2(self, dump_from, hd_kwargs):
        if dump_from == "Entropy":
            hd_kwargs["mode"] = self.ui.electrumV2FromEntropyModeQComboBox.currentText().lower()
            hd_kwargs["mnemonic_type"] = self.ui.electrumV2FromEntropyMnemonicTypeQComboBox.currentText().lower()
            hd_kwargs["language"] = self.ui.electrumV2FromEntropyLanguageQComboBox.currentText().lower()
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
        if crypto == '':
            return None

        crypto_obj = CRYPTOCURRENCIES.cryptocurrency(crypto)

        self.ui.dumpsHdQComboBox.clear()
        self.ui.dumpsHdQComboBox.addItems(crypto_obj.HDS.get_hds())
        self.ui.dumpsHdQComboBox.setCurrentText(crypto_obj.DEFAULT_HD)

        nets = [i.title() for i in crypto_obj.NETWORKS.get_networks()]
        self.ui.dumpsNetworkQComboBox.clear()
        self.ui.dumpsNetworkQComboBox.addItems(nets)
        self.ui.dumpsNetworkQComboBox.setCurrentText("Mainnet")
        self.ui.hdwEccQLineEdit.setText(crypto_obj.ECC.NAME)


        coin_typs_derviation = [
            self.ui.bip44CoinTypeQLineEdit,
            self.ui.bip49CoinTypeQLineEdit,
            self.ui.bip84CoinTypeQLineEdit,
            self.ui.bip86CoinTypeQLineEdit,
            self.ui.cip1852CoinTypeQLineEdit
        ]

        is_bip38_supported = crypto_obj.NAME in self.bip38_cryptocurrencies

        self.ui.bipFromWIFBIP38PassphraseQCheckBox.setChecked(False)
        self.ui.bipFromWIFBIP38PassphraseQCheckBox.setEnabled(is_bip38_supported)
        self.ui.electrumV1FromWIFBIP38PassphraseQCheckBox.setChecked(False)
        self.ui.electrumV1FromWIFBIP38PassphraseQCheckBox.setEnabled(is_bip38_supported)
        
        for c in coin_typs_derviation: c.setText(str(crypto_obj.COIN_TYPE))

        if crypto == "Algorand":
            for combo_box, container in self.algorand_client_combo_boxes:
                combo_box.setCurrentText("Algorand")
                container.setEnabled(True) 
        else:
            for combo_box, container in self.algorand_client_combo_boxes:
                combo_box.setCurrentText("BIP39")
                container.setEnabled(False) 

    def _dump_format_changed(self, export_format):
        if export_format == "CSV":
            self.ui.dumpsExcludeOrIncludeQLabel.setText("Include")
            self.__default_csv_include()
        else:
            self.ui.dumpsExcludeOrIncludeQLabel.setText("Exclude")
            self.ui.dumpsExcludeOrIncludeQLineEdit.setText("root")


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
        self.app.change_page("hdQStackedWidget", current_hd_widget)

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
        else:
            self.ui.dumpsExcludeOrIncludeQLineEdit.setText("root")
 

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
        clear_all_borders(self.errboxes)
        dump_from = self.ui.dumpsFromQComboBox.currentText()
        if dump_from == '':
            return None

        current_hd = self.ui.dumpsHdQComboBox.currentText()

        current_hd_widget = self.stack_hd_widgets[current_hd]
        current_from_stack = self.stack_from_widgets[current_hd_widget]["StackWidget"]
        current_from_widget = self.stack_from_widgets[current_hd_widget][dump_from]

        self.app.change_page(current_from_stack, current_from_widget)

        is_drived = dump_from not in self.hd_undrivable_methods[current_hd]
        self.ui.derivationQGroupBox.setEnabled(is_drived)

        if is_drived:
            key = current_hd
            if dump_from == "XPublic key":
                if current_hd == "BIP32":
                    key = 'BIP32XPUB'
                elif current_hd == "Cardano":
                    key = 'CardanoXPUB'
            self.__filter_derivation_tab(key)

    def derivation_tab_changed(self, page_name: str, qPushButton: QPushButton) -> None:
        widget = self.ui.derivationTabButtonsContainerQFrame
        self.app.tab_changed("derivationsQStackedWidget", page_name, qPushButton, widget)

    def _custom_path_client_changed(self):
        path = self.custom_paths[self.ui.customClientQComboBox.currentText()]
        
        if path != None:
            self.ui.customPathQLineEdit.setText(path)

        self.ui.customPathQFrame.setEnabled(path == None)

    def _bip38_toggled(self, chkbox, passphrase, lable, passphrase_frame):
        chkbox_state = chkbox.isChecked()
        passphrase.setText(None)
        passphrase.setEnabled(chkbox_state)
        passphrase_frame.setEnabled(chkbox_state)

        if chkbox_state:
            lable.setText("Encrypted Wallet Important Format")
        else:
            lable.setText("Wallet Important Format")

    def _update_terminal_state(self, stop_btn_enable, terminal_cancelled):
        self.ui.stopTerminalQPushButton.setEnabled(stop_btn_enable)
        self.terminal_cancelled = terminal_cancelled

class ExportFormatError(Exception):
    pass