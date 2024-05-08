import json
import csv

from PySide6.QtWidgets import QFileDialog


class FileSaver:

    @staticmethod
    def save_as_json(filename, text):
        with open(filename, 'w') as file:
            data = {'text': text}
            json.dump(data, file, indent=4)

    @staticmethod
    def save_as_csv(filename, text):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            lines = text.split('\n')
            for line in lines:
                writer.writerow([line])

    @staticmethod
    def save_file(textedit, combobox):
        options = QFileDialog.Options()
        options |= QFileDialog.DontConfirmOverwrite
        save_as = combobox.currentText()
        if save_as == 'JSON':
            save_as = 'JSON Files (*.json)'
        elif save_as == 'CSV':
            save_as = 'CSV Files (*.csv)'

        filename, _ = QFileDialog.getSaveFileName(None, 'Save File', '',
                                                  save_as,
                                                  options=options)
        if filename:
            text = textedit.toPlainText()
            selected_format = combobox.currentText()

            if selected_format == 'JSON':
                if not filename.endswith('.json'):
                    filename += '.json'
                FileSaver.save_as_json(filename, text)
            elif selected_format == 'CSV':
                if not filename.endswith('.csv'):
                    filename += '.csv'
                FileSaver.save_as_csv(filename, text)

