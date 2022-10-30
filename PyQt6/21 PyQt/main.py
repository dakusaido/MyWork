from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Title
        self.setWindowTitle('Calc')

        # Label
        self.num = '5 + 5'
        self.label = QLabel(self.num)

        # Buttons
        self.button = QPushButton('click')
        self.button.clicked.connect(self.click)

        self.button_exit = QPushButton('Exit...')
        self.button_exit.clicked.connect(exit)

        # Block
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.button_exit)

    def click(self):
        self.label.setText(f'{self.num} = {eval(self.num)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(256, 128)
    window.show()
    app.exec()
