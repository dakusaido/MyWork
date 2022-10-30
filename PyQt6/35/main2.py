import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


def read_file(path: str) -> str:
    with open(path) as file:
        return file.read()


class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        self.bar = self.menuBar()
        file = self.bar.addMenu('File')

        file.addAction('New')

        file.triggered[QAction].connect(self.windowaction)

    def windowaction(self, q):
        sub = QMdiSubWindow()
        subwidget = QWidget()
        subvbox = QVBoxLayout()
        textEdit = QTextEdit(read_file('txa.txt'))
        subvbox.addWidget(textEdit)
        subwidget.setLayout(subvbox)
        sub.setWidget(subwidget)

        self.mdi.addSubWindow(sub)

        sub.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
