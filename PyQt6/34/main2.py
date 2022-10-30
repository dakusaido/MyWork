import sys

from PyQt5 import QtCore, QtGui, QtWidgets  # GUI REQUIREMENTS
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys  # RUNNING THE APP REQUIREMENTS
import cv2 as cv  # FILTER REQUIREMENTS
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QGridLayout,
                             QLabel, QPushButton, QGraphicsView)
from PyQt5.QtWidgets import QGraphicsView

fname = ''


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.btn = QPushButton('Select')
        self.btn.clicked.connect(self.open)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.btn)

    def open(self):
        global fname
        imgName, imgType = QFileDialog.getOpenFileName(self, "Open picture", "", "All Files(*)")
        image = cv.imread(imgName)
        if image is None:
            print("No picture selected")
        else:
            size = (int(self.label.width()), int(self.label.height()))  # width n height of label
            shrink = cv.resize(image, size,
                               interpolation=cv.INTER_AREA)  # Resize image to label size using Interpolation
            shrink = cv.cvtColor(shrink, cv.COLOR_BGR2RGB)  # convert Color space
            self.QtImg = QtGui.QImage(shrink.data,  # resize image in QT without distortion
                                      shrink.shape[1],  # get rows, columns data and store in tuple
                                      shrink.shape[0],
                                      shrink.shape[1] * 3,
                                      QtGui.QImage.Format_RGB888)  # Qt color spaces rgb convert
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
            fname = imgName
            print(imgName)
            one = 50
            two = 50


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
