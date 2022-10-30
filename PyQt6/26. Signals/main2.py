import sys

from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout


class MyLineEdit(QLineEdit):
    def __init__(self, id, parent=None):
        QLineEdit.__init__(self, parent)
        self.id = id

    def focusInEvent(self, a0):
        QLineEdit.focusInEvent(self, a0)

    def focusOutEvent(self, a0):
        QLineEdit.focusOutEvent(self, a0)


class MainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setFixedSize(256, 128)

        self.button = QPushButton('Click!')
        self.line1 = MyLineEdit(1)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.button)

        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        print(self.line1.text())
        self.line1.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
