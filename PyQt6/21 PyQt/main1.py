from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget
from sys import argv


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('PyQt6')

        self.label = QLabel('<center>Hello, how are you?</center>')

        self.good_button = QPushButton('Good!')
        self.bad_button = QPushButton('Bad...')

        self.good_button.clicked.connect(self.good_func)
        self.bad_button.clicked.connect(self.bad_func)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.good_button)
        self.vbox.addWidget(self.bad_button)

    def good_func(self):
        self.label.setText("<center>That's great!</center>")

    def bad_func(self):
        self.label.setText('<center>Smile! Dude!</center>')


if __name__ == '__main__':
    app = QApplication(argv)
    window = Window()
    window.resize(256, 128)
    window.show()
    app.exec()
