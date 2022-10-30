import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QTabWidget


class MainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.lineEdit = QLineEdit()
        self.button = QPushButton('click!')

        self.tab = QTabWidget()
        self.tab.addTab(self.lineEdit, 'lineEdit')
        self.tab.addTab(self.button, 'button')

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.tab)

        self.button.clicked.connect(self.on_clicked_button)

    def on_clicked_button(self):
        self.lineEdit.setText('Hello!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()