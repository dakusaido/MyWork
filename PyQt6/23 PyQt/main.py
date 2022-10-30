import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QApplication, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.secondWindow = SecondWindow()
        self.setCentralWidget(self.secondWindow)


class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()

        self.label = QLabel("<center>That's simple calculator</center>")
        self.text_browser = QLineEdit()
        self.text_browser.setReadOnly(False)
        self.button = QPushButton('Click!')

        self.button.clicked.connect(self.print_que)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.text_browser)
        self.vbox.addWidget(self.button)

        self.setLayout(self.vbox)

    def print_que(self):
        try:
            self.label.setText(f'{eval(self.text_browser.text())}')
        except:
            self.label.setText('Add Correctly!!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(256, 128)
    window.show()
    app.exec()
