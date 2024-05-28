from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
import re

class Validator:
    @staticmethod
    def validate_string(input_string):
        pattern = r'^\d-\d$'
        return bool(re.match(pattern, input_string))

    @staticmethod
    def validate_and_filter(input_string):
        if Validator.validate_string(input_string):
            return input_string
        else:
            return None

    @staticmethod
    def text_changed_callback(line_edit):
        def callback():
            input_text = line_edit.text()
            filtered_text = Validator.validate_and_filter(input_text)
            if filtered_text is None:
                line_edit.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9-]*")))
            else:
                line_edit.setValidator(None)

        callback()

        return callback

    @staticmethod
    def validate_input(lineedits):
        for lineedit in lineedits:
            lineedit.textChanged.connect(
                Validator.text_changed_callback(lineedit)
            )
