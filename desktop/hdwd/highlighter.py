from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor

class LogHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []

        # Punctuation highlighting
        punctuation_format = QTextCharFormat()
        punctuation_format.setForeground(QColor(255, 255, 255))
        self.add_highlighting_rule(r'[^\w\s]', punctuation_format)

        # Digit highlighting
        digit_format = QTextCharFormat()
        digit_format.setForeground(QColor(255, 165, 0))
        self.add_highlighting_rule(r'\b\d+\b', digit_format)

        # Character highlighting
        character_format = QTextCharFormat()
        character_format.setForeground(QColor(255, 255, 255))
        self.add_highlighting_rule(r'\b[a-zA-Z]+\b', character_format)

        # Values within single or double quotes
        quoted_value_format = QTextCharFormat()
        quoted_value_format.setForeground(QColor(131, 185, 255))
        self.add_highlighting_rule(r'["\'].*?["\']', quoted_value_format)

        # Highlight lines starting with "ERROR:"
        error_format = QTextCharFormat()
        error_format.setForeground(QColor(255, 96, 96))
        self.add_highlighting_rule(r'^ERROR:.*$', error_format)

        mslash_format = QTextCharFormat()
        mslash_format.setForeground(QColor(131, 185, 255))
        self.add_highlighting_rule(r'\bm/.*?(?=\s)', mslash_format)
        
        json_string_value_format = QTextCharFormat()
        json_string_value_format.setForeground(QColor(255, 255, 255))
        self.add_highlighting_rule(r':\s*".*?"', json_string_value_format)

    def add_highlighting_rule(self, pattern, char_format):
        self.highlighting_rules.append((QRegularExpression(pattern), char_format))

    def highlightBlock(self, text):
        for pattern, char_format in self.highlighting_rules:
            matcher = pattern.globalMatch(text)
            while matcher.hasNext():
                match = matcher.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), char_format)
