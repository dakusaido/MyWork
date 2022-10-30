from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QLabel, QWidget
from PyQt6 import QtCore
from sys import argv


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setFixedSize(256, 128)

        self.label = QLabel('<center>Click on the button!</center>')
        self.button = QPushButton('Click!')
        self.time = QtCore.QTimer()
        self.TIME_FIVE = 5

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)

        self.time.timeout.connect(self.on_timeout)
        self.button.clicked.connect(self.on_clicked)

    def on_timeout(self):
        if self.TIME_FIVE >= 0:
            self.label.setText(f'<center>{self.TIME_FIVE}</center>')
            self.TIME_FIVE -= 1
        else:
            self.label.setText('<center>Time is over!</center>')
            self.time.stop()
            self.button.setEnabled(False)

    def on_clicked(self):
        self.time.start(1000)


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()
