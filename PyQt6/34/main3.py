from PyQt5.QtWidgets import *
from PyQt5.Qt import QWidget, QPushButton, QLabel, QVBoxLayout, QPixmap, QFileDialog, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.button = QPushButton('Done')
        self.button.clicked.connect(self.on_clicked)

        self.button_open = QPushButton('Выбрать картинку')
        self.button_open.clicked.connect(self._on_open_image)

        self.button_save_as = QPushButton('Сохранить картинку')
        self.button_save_as.clicked.connect(self._on_save_as_image)

        self.label_image = QLabel()

        self.HBox = QHBoxLayout()
        self.HBox.addWidget(self.lineEdit1)
        self.HBox.addWidget(self.lineEdit2)
        self.HBox.addWidget(self.lineEdit3)
        self.HBox.addWidget(self.lineEdit4)
        self.HBox.addWidget(self.button)

        self.lineEdit3.setEnabled(False)
        self.lineEdit4.setEnabled(False)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.button_open)
        main_layout.addLayout(self.HBox)
        main_layout.addWidget(self.button_save_as)
        main_layout.addWidget(self.label_image)

    def on_clicked(self):
        try:
            s1 = [self.lineEdit1.text(),
                  self.lineEdit2.text()]

            pixmap = self.pixmap.scaled(*map(int, s1))
            self.label_image.setPixmap(pixmap)
        except:
            pass

    def _on_open_image(self):
        file_name = QFileDialog.getOpenFileName(self, "Выбор картинки", None, "Image (*.png *.jpg)")[0]
        if not file_name:
            return

        self.pixmap = QPixmap(file_name)
        self.label_image.setPixmap(self.pixmap)

    def _on_save_as_image(self):
        file_name = QFileDialog.getSaveFileName(self, "Сохранение картинки", 'img.jpg', "Image (*.png *.jpg)")[0]
        if not file_name:
            return

        self.label_image.pixmap().save(file_name)


if __name__ == '__main__':
    app = QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec()
