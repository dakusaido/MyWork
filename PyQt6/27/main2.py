import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QSplitter, QFrame
from PyQt6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setFixedSize(512, 256)

        self.label1 = QLabel('<center>Hello!</center>')
        self.label2 = QLabel('<center>How are you?</center>')

        self.button1 = QPushButton('First button')
        self.button2 = QPushButton('Second button')

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.button1)
        self.hbox.addWidget(self.button2)

        self.splitter = QSplitter(Qt.Orientation.Vertical)
        self.label1.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        self.label2.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        self.splitter.addWidget(self.label1)
        self.splitter.addWidget(self.label2)

        self.vbox = QVBoxLayout(self)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.splitter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
