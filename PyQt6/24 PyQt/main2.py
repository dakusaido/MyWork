from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton, QLabel
from PyQt6 import QtCore
from sys import argv


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.coin = 0
        self.label = QLabel('')
        self.button_1 = QPushButton('Click')
        self.button_2 = QPushButton('Block')
        self.button_3 = QPushButton('Active')
        self.button_4 = QPushButton('Delete')

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button_1)
        self.vbox.addWidget(self.button_2)
        self.vbox.addWidget(self.button_3)
        self.vbox.addWidget(self.button_4)

        self.button_1.clicked.connect(self.on_clicked_1)
        self.button_2.clicked.connect(self.on_clicked_2)
        self.button_3.clicked.connect(self.on_clicked_3)
        self.button_4.clicked.connect(self.on_clicked_4)

    @QtCore.pyqtSlot()
    def on_clicked_1(self):
        self.label.setText(f'<center>button_1 active</center>')

    @QtCore.pyqtSlot()
    def on_clicked_2(self):
        self.label.setText('<center>button_2 active</center>')
        self.button_1.blockSignals(True)
        self.button_2.setEnabled(False)
        self.button_3.setEnabled(True)

    @QtCore.pyqtSlot()
    def on_clicked_3(self):
        self.label.setText('<center>button_3 active</center>')
        self.button_1.blockSignals(False)
        self.button_2.setEnabled(True)
        self.button_3.setEnabled(False)

    @QtCore.pyqtSlot()
    def on_clicked_4(self):
        self.label.setText('<center>button_4 active</center>')
        self.button_1.clicked.disconnect(self.on_clicked_1)
        self.button_2.setEnabled(False)
        self.button_3.setEnabled(False)
        self.button_4.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    window.setFixedSize(256, 128)
    window.show()
    app.exec()
