"""
PyHasher - Generates a SHA-256 Hash from the selected file.
Steve Hageman, 10Sept24
Freeware
"""
import sys
from pathlib import Path
from hashlib import sha256
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QGridLayout,QLineEdit,QPushButton, QLabel


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyHasher')
        self.setGeometry(100, 100, 800, 100)

        layout = QGridLayout()
        self.setLayout(layout)

        # file selection
        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.process_hash)
        self.filename_edit = QLineEdit()
        self.sha_edit = QLineEdit()

        layout.addWidget(QLabel('Select file to generate SHA-256 Hash from:'), 0, 0)
        layout.addWidget(file_browse, 0, 1)

        # File display
        layout.addWidget(QLabel('File Selected:'), 2, 0)
        layout.addWidget(self.filename_edit, 2, 1, 1, 2)

        # Hash display
        layout.addWidget(QLabel('SHA-256 Hash:'), 3, 0)
        layout.addWidget(self.sha_edit, 3, 1, 1, 2)

        self.show()

    def process_hash(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            "",
            "Files (*.*)"
        )

        if filename:
            path = Path(filename)

            # Update File box
            self.filename_edit.setText(str(path))

            # Read file to memory
            with open(str(path)) as f:
                contents = f.read()

                # Generate Hash & Update Hash box
                hash = sha256(contents.encode('utf-8')).hexdigest()
                self.sha_edit.setText(hash)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

# ----- Fini -----
