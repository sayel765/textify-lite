# Main order : 4
# Show the OCR result in an editable window

import sys
import subprocess
from .utils import is_wayland, is_x11
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit

EDITOR_STYLE = """
QWidget {
    background-color: #333333;
    color: #dddddd;
    font-size: 13pt;
}
QTextEdit {
    background-color: #262626;
    color: #eeeeee;
    font-size: 13pt;
    border: 1px solid #555555;
}
"""

def send_to_system_clipboard(text: str):
    """Push text permanently to the system clipboard via wl-copy or xclip."""
    if not text.strip():
        return

    if is_wayland():
            subprocess.run(["wl-copy"], input=text.encode("utf-8"))
    elif is_x11():
            subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode("utf-8"))
    else:
        print("[WARN] Unknown display server protocol")


class EditorWindow(QWidget):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Textify - Extract Text")
        self.resize(600, 400)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(text)
        layout.addWidget(self.text_edit)

        self.setLayout(layout)
        self.setStyleSheet(EDITOR_STYLE)

        # whenever Qt changes clipboard, mirror it
        clipboard = QApplication.clipboard()
        clipboard.dataChanged.connect(self.on_copy)

    def on_copy(self):
        # Every time something is copied inside the editor, forward it permanently.
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        if text:  # if something was copied
            send_to_system_clipboard(text)


def open_editor(text):
    app = QApplication(sys.argv)
    editor = EditorWindow(text)
    editor.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    print("--------------- editor.py ---------------------")
    open_editor("This is a text. Change however u want.")
    print("-----------------------------------------------")
