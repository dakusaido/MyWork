# from PyQt6 import QtCore, QtWidgets
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# settings = QtCore.QSettings('Python', '3')
# v1 = 123
# v2 = 'Python'
# v3 = QtCore.QSize(640, 480)
# print(v1, v2, v3, sep=' | ')
# print('Сохраняем настройки')
# settings.setValue('Ключ 1/Значение 1', v1)
# settings.setValue('Значение 1', v1)
# settings.setValue('Значение 2', v2)
# settings.setValue('Значение 3', v3)
# settings.sync()
# print('Считываем настройки')
# lv1 = settings.value('Значение 1')
# lv2 = settings.value('Значение 2')
# lv3 = settings.value('Значение 3')
# print(lv1, lv2, lv3, sep=' | ')
# # settings.clear()
# if settings.contains('Значение 1'):
#     print('Значение 1 есть в хранилище')
# else:
#     print('Значения 1 нет в хранилище')
# settings.clear()
#
# settings.beginGroup('Ключ 1')
# settings.beginGroup('Ключ 2/Ключ 1')
# settings.endGroup

from PyQt6 import QtCore, QtWidgets
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle('Использование ключей')
        self.settings = QtCore.QSettings('Python', 'Использование ключей')
        vbox = QtWidgets.QVBoxLayout()
        self.textLine = QtWidgets.QLineEdit(parent=self)
        vbox.addWidget(self.textLine)
        btnSave = QtWidgets.QPushButton('&Сохранить')
        vbox.addWidget(btnSave)
        self.setLayout(vbox)
        btnSave.clicked.connect(self.saveText)
        if self.settings.contains('Окно/Местоположение'):
            self.setGeometry(self.settings.value('Окно/Местоположение'))
        else:
            self.resize(200, 50)
        if self.settings.contains('Данные/Текст'):
            self.textLine.setText(self.settings.value('Данные/Текст'))

    def closeEvent(self, event):
        self.settings.beginGroup('Окно')
        self.settings.setValue('Местоположение', self.geometry())
        self.settings.endGroup()

    def saveText(self):
        self.settings.beginGroup('Данные')
        self.settings.setValue('Текст', self.textLine.text())
        self.settings.endGroup()


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())

# from PyQt6 import QtCore, QtWidgets
# import sys
# app = QtWidgets.QApplication(sys.argv)
# settings = QtCore.QSettings('Пример', '1')
# l = ['Python', 'JavaScript', 'C#', 'PHP']
# # print(l)
# print('Сохраняем список')
# settings.beginWriteArray('Список')
# for i, el in enumerate(l):
#     settings.setArrayIndex(i)
#     settings.setValue('Элемент', el)
# settings.endArray()
# settings.sync()
# print('Считываем список')
# l1 = []
# lSize = settings.beginReadArray('Список')
# for i in range(lSize):
#     settings.setArrayIndex(i)
#     l1.append(settings.value('Элемент'))
# settings.endArray()
# print(settings.status())
# print(settings.isWritable())
# print(l1)
# settings.clear()