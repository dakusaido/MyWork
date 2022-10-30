import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QRadioButton


class InstructionManual(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # Widgets
        self.instruction = '1. Triangle\n' \
                           '   "a" is the side of the triangle base\n' \
                           '   "h" is the height of the triangle\n' \
                           '   "P" is the Perimeter\n' \
                           '# The perimeter is not read if the triangle does not exist (incorrect triangle aspect ' \
                           'ratio)\n\n' \
                           '2. Rectangle\n' \
                           '   "a" is the first side of the rectangle\n' \
                           '   "b" is the second side of the rectangle\n\n' \
                           '3. Square\n' \
                           '   To count everything, you only need one side of the square\n'

        self.label = QLabel(self.instruction)

        # VBox
        self.MainVBox = QVBoxLayout(self)
        self.MainVBox.addWidget(self.label)


class MainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setFixedSize(512, 256)
        self.InstructionManual = InstructionManual()

        # Widgets
        self.label = QLabel('<center>Triangle</center>')  # Name of the figure

        self.label1 = QLabel('a = ')  # LineEdit1
        self.label2 = QLabel('h = ')  # LineEdit2
        self.label_P = QLabel('P = ')  # LineEdit3_(1, 2, 3)
        self.label_ot_S = QLabel('Square = ')  # Output Square
        self.label_ot_P = QLabel('Perimeter = ')  # Output Perimeter

        self.lineEdit1 = QLineEdit()  # label1
        self.lineEdit2 = QLineEdit()  # label2
        self.lineEdit3_1 = QLineEdit()  # label_P
        self.lineEdit3_2 = QLineEdit()  # label_P
        self.lineEdit3_3 = QLineEdit()  # label_P

        # Buttons
        self.button_triangle = QPushButton('Triangle')
        self.button_rectangle = QPushButton('Rectangle')
        self.button_square = QPushButton('Square')
        self.button = QPushButton('Click!')
        self.RadioButton = QRadioButton('Instruction manual')

        # Setup
        self.label.setFixedSize(90, 32)
        self.button_triangle.setFixedSize(90, 32)
        self.button_rectangle.setFixedSize(90, 32)
        self.button_square.setFixedSize(90, 32)

        # VBox - buttons(Triangle, Rectangle, Square)
        self.vbox_buttons = QVBoxLayout()
        self.vbox_buttons.addWidget(self.button_triangle)
        self.vbox_buttons.addWidget(self.button_rectangle)
        self.vbox_buttons.addWidget(self.button_square)

        # Main work
        self.vbox_work = QVBoxLayout()  # Main VBox

        # Label HBox
        self.HBox_label = QHBoxLayout()
        self.HBox_label.addStretch(0)
        self.HBox_label.addWidget(self.label)

        # Label(1, 2, P) and lineEdit(1, 2, 3_1, 3_2, 3_3)
        self.HBox_lineEdit1 = QHBoxLayout()
        self.HBox_lineEdit1.addWidget(self.label1)
        self.HBox_lineEdit1.addWidget(self.lineEdit1)

        self.HBox_lineEdit2 = QHBoxLayout()
        self.HBox_lineEdit2.addWidget(self.label2)
        self.HBox_lineEdit2.addWidget(self.lineEdit2)

        self.HBox_lineEdit3_123 = QHBoxLayout()
        self.HBox_lineEdit3_123.addWidget(self.label_P)
        self.HBox_lineEdit3_123.addWidget(self.lineEdit3_1)
        self.HBox_lineEdit3_123.addWidget(self.lineEdit3_2)
        self.HBox_lineEdit3_123.addWidget(self.lineEdit3_3)

        self.vbox_work.addLayout(self.HBox_label)
        self.vbox_work.addLayout(self.HBox_lineEdit1)
        self.vbox_work.addLayout(self.HBox_lineEdit2)
        self.vbox_work.addLayout(self.HBox_lineEdit3_123)

        # Main HBox
        self.main_HBox = QHBoxLayout()
        self.main_HBox.addLayout(self.vbox_buttons)
        self.main_HBox.addLayout(self.vbox_work)

        # Output VBox
        self.vbox_label_ot = QVBoxLayout()
        self.vbox_label_ot.addWidget(self.label_ot_S)
        self.vbox_label_ot.addWidget(self.label_ot_P)

        # Output and button HBox
        self.HBox_once_button = QHBoxLayout()
        self.HBox_once_button.addLayout(self.vbox_label_ot)
        self.HBox_once_button.addWidget(self.button)

        # Main VBox
        self.main_vbox = QVBoxLayout(self)
        self.main_vbox.addLayout(self.main_HBox)
        self.main_vbox.addLayout(self.HBox_once_button)
        self.main_vbox.addWidget(self.RadioButton)

        # buttons connect
        self.button_triangle.clicked.connect(self.on_clicked_triangle)
        self.button_rectangle.clicked.connect(self.on_clicked_rectangle)
        self.button_square.clicked.connect(self.on_clicked_square)
        self.button.clicked.connect(self.on_clicked_button)
        self.RadioButton.clicked.connect(self.on_clicked_radiobutton)

    def on_clicked_radiobutton(self):
        if self.RadioButton.isChecked():
            self.InstructionManual.show()
        elif not self.RadioButton.isChecked():
            self.InstructionManual.close()

    def on_clicked_triangle(self):
        self.label.setText('<center>Triangle</center>')
        self.label2.setText('h = ')
        self.lineEdit2.setDisabled(False)
        self.lineEdit3_3.setDisabled(False)
        self.lineEdit3_2.setDisabled(False)
        self.label_P.setText('P = ')
        self.on_clicked_button()

    def on_clicked_rectangle(self):
        self.label.setText('<center>Rectangle</center>')
        self.label2.setText('b = ')
        self.label_P.setText('2(a + b)')
        self.lineEdit3_3.setText('')
        self.lineEdit2.setDisabled(False)
        self.lineEdit3_3.setDisabled(True)
        self.lineEdit3_2.setDisabled(False)
        self.on_clicked_button()

    def on_clicked_square(self):
        self.label.setText('<center>Square</center>')
        self.label2.setText('b = ')
        self.label_P.setText('4 * a')
        self.lineEdit3_3.setText('')
        self.lineEdit3_2.setText('')
        self.lineEdit2.setDisabled(True)
        self.lineEdit3_2.setDisabled(True)
        self.lineEdit3_3.setDisabled(True)
        self.on_clicked_button()

    def on_clicked_button(self):
        name = self.label.text()

        n1 = self.lineEdit1.text()
        n2 = self.lineEdit2.text()
        n3 = self.lineEdit3_1.text()
        n4 = self.lineEdit3_2.text()
        n5 = self.lineEdit3_3.text()

        if name == '<center>Triangle</center>':
            try:
                self.label_ot_S.setText(f'Square = {(int(n1) * int(n2)) / 2}')
            except:
                self.label_ot_S.setText(f'Square = None')
            try:
                lst = sorted([int(n3), int(n4), int(n5)])
                if (lst[0] + lst[1]) < lst[-1]:
                    raise
                self.label_ot_P.setText(f'Perimeter = {int(n3) + int(n4) + int(n5)}')
            except:
                self.label_ot_P.setText(f'Perimeter = None')
        elif name == '<center>Square</center>':
            try:
                self.label_ot_S.setText(f'Square = {int(n1) ** 2}')
            except:
                self.label_ot_S.setText(f'Square = None')
            try:
                self.label_ot_P.setText(f'Perimeter = {4 * int(n3)}')
            except:
                self.label_ot_P.setText('Perimeter = None')
        elif name == '<center>Rectangle</center>':
            try:
                self.label_ot_S.setText(f'Square = {int(n1) * int(n2)}')
            except:
                self.label_ot_S.setText(f'Square = None')
            try:
                self.label_ot_P.setText(f'Perimeter = {2 * (int(n3) + int(n4))}')
            except:
                self.label_ot_P.setText(f'Perimeter = None')

    def do_func(self, param, func) -> None:
        eval(param)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
