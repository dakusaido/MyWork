import sqlite3

from main1 import *

path = 'dbase.db'


def save_log_pas(path: str, login: str, password, key=None):
    if login.isdigit():
        raise "Login not be int"

    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS person(log TEXT, password TEXT)""")

    cursor.execute("""SELECT * FROM person""")
    all_ = cursor.fetchall()
    if login in (x[0] for x in all_) and key is None:
        return False

    if key is None:
        cursor.execute("""INSERT INTO person VALUES(?, ?)""", (login, password))
        conn.commit()
    elif (key is not None) and ((login, password) in all_):
        return True


class FirstWindow(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.coin = True

        self.setFixedSize(400, 200)
        self.reg_button = QPushButton('Registration')
        self.in_button = QPushButton('Sign in')
        self.label = QLabel('<center>Registration</center>')
        self.log_lineEdit = QLineEdit()
        self.pas_lineEdit = QLineEdit()
        self.button = QPushButton('Click!')

        self.HBox_button = QHBoxLayout()
        self.HBox_button.addWidget(self.reg_button)
        self.HBox_button.addWidget(self.in_button)

        self.main_VBox = QVBoxLayout(self)
        self.main_VBox.addLayout(self.HBox_button)
        self.main_VBox.addWidget(self.label)
        self.main_VBox.addWidget(self.log_lineEdit)
        self.main_VBox.addWidget(self.pas_lineEdit)
        self.main_VBox.addWidget(self.button)

        self.reg_button.clicked.connect(lambda x: self.clicked_reg_in_button(key='reg'))
        self.in_button.clicked.connect(lambda x: self.clicked_reg_in_button(key='in'))
        self.button.clicked.connect(lambda x: self.on_clicked_button(key=self.coin))

    def clicked_reg_in_button(self, key):
        if key == 'reg':
            self.label.setText('<center>Registration</center>')
            self.coin = True
        else:
            self.label.setText('<center>Sign in</center>')
            self.coin = False

    def on_clicked_button(self, key):
        log = self.log_lineEdit.text()
        pas = self.pas_lineEdit.text()

        if log == '' or pas == '':
            self.label.setText('<center>Error!</center>')
            return

        if key:
            try:
                if save_log_pas(path, log, pas) is False:
                    self.label.setText('<center>This login is already in use</center>')
                else:
                    self.label.setText('<center>Great!</center>')
            except:
                self.label.setText("<center>Error: Login didn't to be int</center>")
        else:
            try:
                if save_log_pas(path, log, pas, key=123):
                    self.window = MainWindow()
                    apply_stylesheet(app, theme='dark_purple.xml')
                    self.window.show()
                    self.close()
                else:
                    self.label.setText('<center>Not Correctly!</center>')
            except:
                self.label.setText("<center>Error: Login didn't to be int</center>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml')
    window = FirstWindow()
    window.show()
    app.exec()
