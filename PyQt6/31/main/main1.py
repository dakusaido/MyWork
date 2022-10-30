import os
import sys
import zipfile

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from qt_material import apply_stylesheet


class ErrorWindow(QMainWindow):

    def __init__(self, error_type):
        QMainWindow.__init__(self, parent=None)
        self.name = error_type

        self.setFixedSize(479, 128)
        self.label = QLabel('')
        self.setCentralWidget(self.label)

        if self.name == 'RusError':
            self.russia_words()
        elif self.name == 'ZipError':
            self.zip_error()

    def russia_words(self):
        self.label.setText('<center>Ошибка! Файлы в названиях которых есть кириллица не принимается!</center>')

    def zip_error(self):
        self.label.setText('<center>Не архивированный файл не может быть разархивирован!<center>')


def not_russia(text, alphabet=None):
    if alphabet is None:
        alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return not alphabet.isdisjoint(text.lower())


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)

        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon('res/icon.png'))

        self.menu = QMenuBar()
        self.file_menu = self.menuBar().addMenu('&File')
        self.zip_file_action = QAction(QIcon('res/zip.png'), 'Zip', self)
        self.unzip_file_action = QAction(QIcon('res/unzip.png'), 'Unzip', self)
        self.exit_app = QAction(QIcon('res/exit.png'), 'Exit', self)

        self.zip_file_action.triggered.connect(self.zip_file)
        self.unzip_file_action.triggered.connect(self.unzip_file)

        self.selection_menu = self.menuBar().addMenu('&Selection')
        self.help_menu = self.menuBar().addMenu('&Help')
        self.about = QAction('About', self)
        self.help = QAction('Help', self)

        self.file_menu.addActions([self.zip_file_action, self.unzip_file_action, self.exit_app])
        self.help_menu.addActions([self.about, self.help])

        self.list_widget = QListWidget(self)
        self.list_widget.move(0, 20)
        self.list_widget.resize(600, 380)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.menu)
        self.vbox.addWidget(self.list_widget)
        self.setLayout(self.vbox)

        self.widget = QWidget()
        self.widget.setLayout(self.vbox)
        self.setCentralWidget(self.widget)

        # self.list_widget.setStyleSheet('background-color: white')
        # self.setStyleSheet('background-color: lightgray')

        self.exit_app.triggered.connect(self.close)
        self.list_widget.doubleClicked.connect(self.item_clicked)

        self.update_list()

    def update_list(self):
        self.list_widget.insertItem(0, '..')

        for i, item in enumerate(os.listdir()):
            self.list_widget.insertItem(i + 1, item)

    def item_clicked(self):
        path = os.path.abspath(os.getcwd())
        item = self.list_widget.currentItem()
        if item.text() == '..':
            os.chdir('..')
        elif os.path.isdir(item.text()):
            os.chdir(f'{path}/{item.text()}')
        else:
            if not not_russia(item.text()):
                os.system(item.text())
            else:
                self.errorWindow = ErrorWindow('RusError')
                self.errorWindow.show()

        self.list_widget.clear()
        self.update_list()

    def zip_file(self):
        file = self.list_widget.currentItem().text()
        file_name = file.split('.')
        with zipfile.ZipFile(f'{file_name[0]}.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
            zf.write(file)
        self.list_widget.clear()
        self.update_list()

    def unzip_file(self):
        file = self.list_widget.currentItem().text()
        try:
            archive = zipfile.ZipFile(file, 'r')
            archive.extractall('.')
            archive.close()
        except:
            self.errorWindow = ErrorWindow('ZipError')
            self.errorWindow.show()

        self.list_widget.clear()
        self.update_list()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Explorer")
    apply_stylesheet(app, theme='dark_purple.xml')
    window = MainWindow()
    window.show()
    app.exec()
