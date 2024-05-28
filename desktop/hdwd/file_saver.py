import os

from PySide6.QtWidgets import QFileDialog


class FileSaver:

    @staticmethod
    def save_file(format):
        options = QFileDialog.Options()
        options |= QFileDialog.DontConfirmOverwrite
        if format == 'JSON':
            save_as = 'JSON Files (*.json)'
        elif format == 'CSV':
            save_as = 'CSV Files (*.csv)'
        home_dir = os.path.expanduser("~")

        filename, _ = QFileDialog.getSaveFileName(None,'Save File',
                                                  os.path.join(home_dir, 'hdwallet'),
                                                  save_as,
                                                  options=options)
        return filename