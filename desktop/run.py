#!/usr/bin/env python3
import sys

from PySide6.QtWidgets import QApplication
from hdwd.main import MainApplication

def main():
    qApplication: QApplication = QApplication(sys.argv)
    main_application: MainApplication = MainApplication()
    main_application.app.show()
    sys.exit(qApplication.exec())

if __name__ == '__main__':
    main()