import json
import csv

from PySide6.QtWidgets import QFileDialog


class FileSaver:
    @staticmethod
    def save_as_text(filename, text):
        with open(filename, 'w') as file:
            lines = text.split('\n')
            for line in lines:
                file.write(line + '\n')

    @staticmethod
    def save_as_json(filename, text):
        mnemonics = text.strip().split('}{')
        mnemonics = [m.strip() for m in mnemonics]

        json_data = '[' + ','.join(['{' + m + '}' for m in mnemonics]) + ']'

        with open(filename, 'w') as file:
            file.write(json_data)

    @staticmethod
    def save_as_csv(filename, text):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            lines = text.split('\n')
            for line in lines:
                writer.writerow([line])

    @staticmethod
    def save_file(textedit):
        options = QFileDialog.Options()
        options |= QFileDialog.DontConfirmOverwrite

        filename, _ = QFileDialog.getSaveFileName(None, 'Save File', 'hdwallet',
                                                  "Text Files (*.txt);; JSON Files (*.json);; CSV Files (*.csv)",
                                                  options=options)
        if filename:
            text = textedit.toPlainText()
            selected_format = filename

            if selected_format.endswith(".json"):
                if not filename.endswith('.json'):
                    filename += '.json'
                FileSaver.save_as_json(filename, text)
            elif selected_format.endswith(".csv"):
                if not filename.endswith('.csv'):
                    filename += '.csv'
                FileSaver.save_as_csv(filename, text)
            else:
                if not filename.endswith('.txt'):
                    filename += '.txt'
                FileSaver.save_as_text(filename, text)

