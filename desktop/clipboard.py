from PySide6.QtGui import QGuiApplication


def copy_to_clipboard(text: str) -> None:
    clipboard = QGuiApplication.clipboard()
    clipboard.setText(text)


def get_clipboard_text() -> str:
    clipboard = QGuiApplication.clipboard()
    return clipboard.text()


def clear_clipboard() -> None:
    clipboard = QGuiApplication.clipboard()
    clipboard.clear()