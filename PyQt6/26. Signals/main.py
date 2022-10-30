import sys

from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtGui import QKeySequence
from PyQt6.QtCore import QEvent, Qt


class MyLineEdit(QLineEdit):
    def __init__(self, id, parent=None):
        QLineEdit.__init__(self, parent)
        self.id = id
        self.ID = None

    def event(self, a0):
        if a0.type() == QEvent.Type.Shortcut:
            if self.id == a0.shortcutId():
                self.setFocus(Qt.FocusReason.ShortcutFocusReason)
                return True
        return QLineEdit.event(self, a0)

    def focusInEvent(self, a0):
        QLineEdit.focusInEvent(self, a0)

    def focusOutEvent(self, a0):
        QLineEdit.focusOutEvent(self, a0)


class MainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setFixedSize(256, 128)

        self.button = QPushButton('Click!')
        self.line1 = MyLineEdit(1)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.button)

        self.button.clicked.connect(self.on_clicked)
        self.line1.id = self.line1.grabShortcut(QKeySequence('Alt+c'))

    def on_clicked(self):
        self.line1.clearFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
