import json
import csv


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
