from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor, QBrush, QPen
from PyQt6.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Цвета')
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(QColor.green, 8, Qt.BrushStyle.NoBrush))
        painter.drawEllipse(40, 40, 400, 400)



def main():
    app = QApplication([])
    ex = Example()
    app.exec()


if __name__ == '__main__':
    main()
