import sys

from random import randint
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QVBoxLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.win = SecondWindow()
        self.setCentralWidget(self.win)


class SecondWindow(QWidget):

    def __init__(self):
        super(SecondWindow, self).__init__()

        self.label = QLabel('<center>label</center>')
        self.button = QPushButton('label')
        self.coin = 0

        self.button.clicked.connect(self.clicked_button)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)

    def clicked_button(self):
        n1 = randint(1, 100)
        n2 = randint(1, n1 + 100)
        self.coin += 1
        self.label.setText(f'<center>{n1} + {n2} = {n1 + n2} | Clicked {self.coin}x</center>')
        self.button.setText(f'Clicked {self.coin}x')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(256, 128)
    window.show()
    app.exec()
