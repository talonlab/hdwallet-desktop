#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Abenezer Lulseged Wube <itsm3abena@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from PySide6.QtWidgets import QApplication

import sys

from desktop.main import MainApplication


def main() -> None:
    qapp: QApplication = QApplication(sys.argv)
    main_application: MainApplication = MainApplication()
    main_application.app.show()
    sys.exit(qapp.exec())


if __name__ == '__main__':
    main()
