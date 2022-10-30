import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class MyThread(QtCore.QThread):
    signal_thread = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

        self.isrun = False
        self.count = 0

    def run(self):
        self.isrun = True
        while self.isrun:
            if self.count <= 9:
                self.count += 1
                self.signal_thread.emit(f'Connection... {self.count * 10}%')
                self.sleep(1)
            else:
                self.count = 0
                break


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        # labels
        self.label = QLabel('<center>Hello!</center>')

        # buttons
        self.start_button = QPushButton('Start!')
        self.stop_button = QPushButton('Stop!')

        # boxes
        self.vbox = QVBoxLayout(self)

        # Sets in box
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.start_button)
        self.vbox.addWidget(self.stop_button)

        # class MyThread
        self.my_thread = MyThread()

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop_thread)
        self.my_thread.finished.connect(self.on_finished)
        self.my_thread.signal_thread.connect(self.on_change)

    def start(self):
        if not self.my_thread.isRunning():
            self.start_button.setDisabled(True)
            self.stop_button.setDisabled(False)
            self.my_thread.start()

    def stop_thread(self):
        if self.my_thread.isRunning():
            self.my_thread.isrun = False
            self.stop_button.setDisabled(True)

    def on_finished(self):
        self.label.setText('<center>The connection was suspended!</center>')
        self.start_button.setDisabled(False)

    def on_change(self, s):
        self.label.setText(s)

    def closeEvent(self, event):
        self.hide()
        self.my_thread.isrun = False
        self.my_thread.wait(5000)
        event.accept()


if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(256, 128)
    window.show()
    app.exec()
