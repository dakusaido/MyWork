import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self, parent)
        self.settings = QSettings("MyCompany", "MyApp")
        if not self.settings.value("geometry") is None:
            self.restoreGeometry(self.settings.value("geometry"))
        if not self.settings.value("windowState") is None:
            self.restoreState(self.settings.value("windowState"))

    def closeEvent(self, event):
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        QMainWindow.closeEvent(self, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow(None)
    window.show()
    app.exec()
