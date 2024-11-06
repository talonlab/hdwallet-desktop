#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from cx_Freeze import setup, Executable
from hdwallet import info

import platform

app_name  = "HDWallet"

if platform.system() == "Windows":
    icon_path = "desktop/ui/images/icon/icon.ico"
else:
    icon_path = "desktop/ui/images/svg/HDW-Logo.svg"

msi_shortcut_table = [
    (
        "DesktopShortcut",             # Shortcut
        "DesktopFolder",               # Directory_
        app_name,                      # Name that will be show on the link
        "TARGETDIR",                   # Component_
        f"[TARGETDIR]{app_name}.exe",  # Target exe to exexute
        None,                          # Arguments
        None,                          # Description
        None,                          # Hotkey
        None,                          # Icon
        None,                          # IconIndex
        None,                          # ShowCmd
        'TARGETDIR'                    # WkDir
    )
]

msi_directory_table = [
    ("ProgramMenuFolder", "TARGETDIR", "."),
    ("HDWalletMenu", "ProgramMenuFolder", "HDWAL~1|HDWallet")
]

msi_data = {
    "Shortcut": msi_shortcut_table,
    "Directory": msi_directory_table
}

bdist_msi_opt = {
    "add_to_path": False,
    "data": msi_data,
    "initial_target_dir": f"[ProgramFiles64Folder]\\{app_name}",
    "install_icon": icon_path,
    "upgrade_code": "{B1CFF0C5-5145-3C96-A54E-4AECA6F5774D}"
}

build_exe_opt = {
    "packages": ["_scrypt"],
    "excludes": ["tkinter"],
    "include_msvcr": True
}

executables = [
    Executable(
        "launch.py",
        base="gui",
        icon=icon_path,
        target_name=app_name,
        shortcut_name=app_name,
        shortcut_dir="HDWalletMenu",
        copyright=f"Copyright (C) 2024 {app_name}"
    )
]

setup(
    name=app_name,
    version=info.__versions__["desktop"],
    author=info.__author__,
    description="A desktop application for generating hierarchical deterministic wallets using the HDWallet library.",
    executables=executables,
    options={
        "build_exe": build_exe_opt,
        "bdist_msi": bdist_msi_opt
    }
)