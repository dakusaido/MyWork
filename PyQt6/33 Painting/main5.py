from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 650, 500)
        self.setWindowTitle('Кисть')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, painter):
        painter.drawRoundedRect(40, 40, 100, 100, 10, 10)
        painter.drawRoundedRect(80, 80, 100, 100, 10, 50)
        painter.drawRoundedRect(120, 120, 100, 100, 50, 10)
        painter.drawRoundedRect(160, 160, 100, 100, 50, 50)

        painter.drawEllipse(300, 10, 100, 100)
        painter.drawEllipse(300, 10, 150, 200)
        painter.drawEllipse(300, 10, 200, 300)


def main():
    app = QApplication([])
    ex = Example()
    app.exec()


if __name__ == '__main__':
    main()
