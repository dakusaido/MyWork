from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton, QLabel
from PyQt6 import QtCore
from sys import argv


class PyQtSlot(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)

    @QtCore.pyqtSlot()
    def print_hello(self):
        return '<center>hello</center>'


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.label = QLabel()
        self.button = QPushButton('Click')
        self.PyQtSlot = PyQtSlot()

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)

        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.label.setText(self.PyQtSlot.print_hello())


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    window.setFixedSize(258, 128)
    window.show()
    app.exec()
