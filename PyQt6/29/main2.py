import sys

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont

from random import randint


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.setWindowTitle("[Big or Small] Game")

        self.setFixedSize(512, 256)
        self.bs_label = '0'
        self.point = 5
        self.random_number = randint(1, 100)

        self.point_label = QLabel(f'{self.point} xp')
        self.main_label = QLabel(f'{self.bs_label}')
        self.main_label.setFont(QFont('Arial', 28))

        self.HBox_point_label = QHBoxLayout()
        self.HBox_point_label.addStretch(0)
        self.HBox_point_label.addWidget(self.point_label)

        self.HBox_main_label = QHBoxLayout()
        self.HBox_main_label.addStretch(0)
        self.HBox_main_label.addWidget(self.main_label)

        self.MainVBox = QVBoxLayout(self)
        self.MainVBox.addLayout(self.HBox_point_label)
        self.MainVBox.addLayout(self.HBox_main_label)

        self.grid_numbers()
        self.clicked_button()

    def grid_numbers(self):

        self.grid = QGridLayout()
        self.button_0 = QPushButton('0')
        self.button_1 = QPushButton('1')
        self.button_2 = QPushButton('2')
        self.button_3 = QPushButton('3')
        self.button_4 = QPushButton('4')
        self.button_5 = QPushButton('5')
        self.button_6 = QPushButton('6')
        self.button_7 = QPushButton('7')
        self.button_8 = QPushButton('8')
        self.button_9 = QPushButton('9')
        self.button_ = QPushButton('Click!')
        self.button_clear = QPushButton('C')

        self.names = [self.button_7, self.button_8, self.button_9,
                      self.button_4, self.button_5, self.button_6,
                      self.button_1, self.button_2, self.button_3,
                      self.button_clear, self.button_0, self.button_]

        for name, position in zip(self.names, [(i, j) for i in range(4) for j in range(3)]):
            if name == '':
                self.grid.addWidget(QLabel(), *position)
                continue
            self.grid.addWidget(name, *position)
        self.MainVBox.addLayout(self.grid)

    def clicked_button(self):
        for name in self.names:
            if name != '' and name != self.button_ and name != self.button_clear:
                name.pressed.connect(lambda x=name: self.in_main_label(x))
            elif name == self.button_:
                name.pressed.connect(lambda x=name: self.main_work(int(self.bs_label)))
        self.button_clear.clicked.connect(self.clicked_clear)

    def clicked_clear(self):
        self.bs_label = self.main_label.text()[:-1]
        self.main_label.setText(f'{self.bs_label}')

    def in_main_label(self, a):
        self.bs_label += a.text()
        self.main_label.setText(f'{int(self.bs_label)}')

    def main_work(self, num):
        if num > self.random_number:
            self.main_label.setText('Smaller')
        elif num < self.random_number:
            self.main_label.setText('Bigger')
        elif num == self.random_number:
            self.main_label.setText('Congratulations!')
            self.random_number = randint(1, 100)
            self.point = 5
            self.point_label.setText(str(self.point))
            self.bs_label = '0'
            self.point_label.setText(str(self.point))
            return
        self.point -= 1
        if self.point <= 0:
            self.main_label.setText(f'You Lose! Win number is {self.random_number}')
            self.point = 5
            self.bs_label = '0'
            self.point_label.setText(str(self.point))
            self.random_number = randint(1, 100)
            return
        self.bs_label = '0'
        self.point_label.setText(str(self.point))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
