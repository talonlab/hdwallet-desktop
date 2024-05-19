from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit


class HistoryLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(HistoryLineEdit, self).__init__(parent)
        self.history = []
        self.history_index = 0

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.prev_history()
        elif event.key() == Qt.Key_Down:
            self.next_history()
        elif event.key() == Qt.Key_Return:
            self.history.append(self.text())
            self.history_index = len(self.history)

        super(HistoryLineEdit, self).keyPressEvent(event)

    def prev_history(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.setText(self.history[self.history_index])

    def next_history(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.setText(self.history[self.history_index])
        else:
            self.clear()
