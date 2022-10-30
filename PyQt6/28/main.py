import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.pixmap = QPixmap('img0.png')

        self.button1 = QPushButton('(-∞; -4] v {-0.25; 0; 0.25} v [4; +∞)')
        self.button2 = QPushButton('(-∞; 0) v (0, +∞) v {4}')
        self.button3 = QPushButton('{3; 4; 175/3}')

        self.label = QLabel('')
        self.label_ot = QLabel('')
        self.label.setPixmap(self.pixmap)

        self.vbox1 = QVBoxLayout()
        self.vbox1.addWidget(self.button1)
        self.vbox1.addWidget(self.button2)
        self.vbox1.addWidget(self.button3)

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox1)
        self.hbox.addWidget(self.label_ot)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)
        self.vbox.addLayout(self.hbox)

        self.button1.clicked.connect(self.on_clicked1)
        self.button2.clicked.connect(self.on_clicked2)
        self.button3.clicked.connect(self.on_clicked2)

    def on_clicked1(self):
        self.label_ot.setText("<center>Is the right answer!</center>")

    def on_clicked2(self):
        self.label_ot.setText('<center>Wrong!</center>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
