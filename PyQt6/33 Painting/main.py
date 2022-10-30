from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = 'Лутц\nИзучаем Python'
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Отрисовка текста')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 255))
        qp.setFont(QFont('Decorative', 20))
        qp.drawText(event.rect(), Qt.AlignmentFlag.AlignCenter, self.text)


def main():
    app = QApplication([])
    ex = Example()
    app.exec()


if __name__ == '__main__':
    main()
