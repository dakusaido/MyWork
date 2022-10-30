import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class MyThread(QtCore.QThread):
    signal_thread = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        for i in range(1, 7):
            self.sleep(2)
            self.signal_thread.emit(f'Connection... {20 * i}%')


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        # labels
        self.label = QLabel('<center>Hello!</center>')

        # buttons
        self.button = QPushButton('Click!')

        # boxes
        self.vbox = QVBoxLayout(self)

        # Sets in box
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)

        # class MyThread
        self.my_thread = MyThread()
        self.button.clicked.connect(self.rewriteLabel)
        self.my_thread.finished.connect(self.on_started)
        self.my_thread.signal_thread.connect(self.on_change)

    def rewriteLabel(self):
        self.button.setDisabled(True)
        self.label.setText('<center>Wait!</center>')
        self.my_thread.start()

    def on_started(self):
        self.label.setText('<center>Bye!</center>')
        self.button.setDisabled(False)

    def on_change(self, s):
        self.label.setText(s)


if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(256, 128)
    window.show()
    app.exec()
