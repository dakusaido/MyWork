import sys
import sqlite3
from typing import Any

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from qt_material import apply_stylesheet

path = 'dbase.db'


def dbase_show(pat: str) -> list[Any]:
    conn = sqlite3.connect(pat)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS user(log TEXT, password TEXT)""")
    cursor.execute("""SELECT * FROM user""")

    return cursor.fetchall()


def save_log_pas(pat: str, login: str, password, key=None):
    if login.isdigit():
        raise ValueError

    conn = sqlite3.connect(pat)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user(log TEXT, password TEXT)""")

    cursor.execute("""SELECT * FROM user""")
    all_ = cursor.fetchall()
    if login in (x[0] for x in all_) and key is None:
        return False

    if key is None:
        cursor.execute("""INSERT INTO user VALUES(?, ?)""", (login, password))
        conn.commit()
        return True
    elif (key is not None) and ((login, password) in all_):
        return True


class ListPersons(QWidget):

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.list_widget = QListWidget()
        self.list_widget.move(0, 20)
        self.list_widget.resize(600, 380)

        for x in dbase_show(path):
            self.list_widget.insertItem(0, f'{x}')

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.list_widget)


class SavePerson(QWidget):

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.setFixedSize(300, 200)

        self.label = QLabel('<center>Супер сохранялка паролей:)</center>')
        self.label.setFont(QFont('Arial', 10))
        self.nameLineEdit = QLineEdit()
        self.passwordLineEdit = QLineEdit()
        self.label_name = QLabel('<center>Name<center>')
        self.label_password = QLabel('<center>Password</center>')
        self.save_button = QPushButton('Save!')

        self.HBox1 = QHBoxLayout()
        self.HBox1.addWidget(self.label_name)
        self.HBox1.addWidget(self.nameLineEdit)

        self.HBox2 = QHBoxLayout()
        self.HBox2.addWidget(self.label_password)
        self.HBox2.addWidget(self.passwordLineEdit)

        self.MainVbox = QVBoxLayout(self)
        self.MainVbox.addWidget(self.label)
        self.MainVbox.addLayout(self.HBox1)
        self.MainVbox.addLayout(self.HBox2)
        self.MainVbox.addWidget(self.save_button)

        self.save_button.clicked.connect(self.on_clicked_save_button)

    def on_clicked_save_button(self):
        value1 = self.nameLineEdit.text()
        value2 = self.passwordLineEdit.text()
        try:
            if save_log_pas(path, value1, value2):
                self.label.setText('<center>Saved!</center>')
            else:
                self.label.setText('<center>This login is already in use</center>')
        except ValueError:
            self.label.setText('<center>Error!</center>')


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.setFixedSize(512, 258)
        self.list_person = None
        self.SavePerson_ = SavePerson()

        self.label = QLabel('<center>Тут должно было что-то быть, но я поленился это делать</center>')
        self.list_persons_button = QPushButton('Users')
        self.save_person_in_db = QPushButton('Save User')

        self.HBox = QHBoxLayout()
        self.HBox.addWidget(self.list_persons_button)
        self.HBox.addWidget(self.save_person_in_db)

        self.mainVbox = QVBoxLayout()
        self.mainVbox.addWidget(self.label)
        self.mainVbox.addLayout(self.HBox)

        self.MainMainVbox = QVBoxLayout(self)
        self.MainMainVbox.addLayout(self.mainVbox)

        self.list_persons_button.clicked.connect(self.show_list_persons)
        self.save_person_in_db.clicked.connect(self.save_person)

    def show_list_persons(self):
        self.list_person = ListPersons()
        self.list_person.show()

    def save_person(self):
        self.SavePerson_.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='light_purple.xml')
    window.show()
    app.exec()
