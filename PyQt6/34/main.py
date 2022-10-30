import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 650, 500)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        self.draw_something(painter)
        painter.end()

    def draw_something(self, a0):
        from random import randint, choice

        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']

        pen = QPen()
        pen.setWidth(3)
        a0.setPen(pen)

        for i in range(10000):
            pen.setColor(QColor(choice(colors)))
            a0.setPen(pen)
            a0.drawPoint(
                200 + randint(-100, 100),
                150 + randint(-100, 100)
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
