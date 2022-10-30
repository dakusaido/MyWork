from PyQt6.QtWidgets import QApplication, QWidget
from sys import argv


class MainWindow(QWidget):
    def __init__(self, diction, parent=None):
        QWidget.__init__(self, parent)
        self.resize(256, 128)
        self.diction = diction

    def moveEvent(self, e):
        self.diction = {'x': e.pos().x(), 'y': e.pos().y()}
        # print(self.diction)  # If you want to see the dictionary, just remove #
        return QWidget.moveEvent(self, e)


if __name__ == '__main__':
    dic = {}

    app = QApplication(argv)
    window = MainWindow(dic)
    window.show()
    app.exec()
