from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Медиа плеер')
        self.setGeometry(200, 200, 381, 302)
        self._setup_ui()

    def _setup_ui(self):
        self.central_widget = QWidget(self)
        self.central_widget_layout = QVBoxLayout()
        self.setCentralWidget(self.central_widget)
        self.lineEdit = QLineEdit()
        self.done_button = QPushButton('Done')
        self.Hbox2 = QHBoxLayout()
        self.Hbox2.addWidget(self.lineEdit)
        self.Hbox2.addWidget(self.done_button)

        try:
            self.done_button.clicked.connect(
                lambda x: self.list_widget.addItem(
                    self.lineEdit.text().strip() if self.lineEdit.text() is not None else None))
        except:
            print('Error')

        self.add_button = QPushButton('Add Radio Station')
        self.add_button.clicked.connect(lambda x: self.mainVbox.addLayout(self.Hbox2))

        self.user_action = -1
        self.play_button = QPushButton()
        self.player = MediaPlayer()
        self.play_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        self.pause_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
        self.play_button.setIcon(self.play_icon)
        self.play_button.clicked.connect(self.play_pause_button_clicked)
        self.select_button = QPushButton('Select Music')
        self.select_button.clicked.connect(self._on_open_file)
        self.list_widget = QListWidget()
        self.list_widget.addItem('http://sv.wargaming.fm:8051/128')

        self.url_text = QLineEdit()
        self.ok_button = QPushButton()
        self.ok_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DialogYesButton)
        self.ok_button.setIcon(self.ok_icon)
        self.ok_button.clicked.connect(lambda x: self.change_url())

        self.volume = QDial()
        self.volume.setMaximum(100)
        self.volume.setMinimum(0)
        self.volume.setValue(int(self.player.current_volume * 100))

        self.volume.valueChanged.connect(self.sliderMoved)
        self.central_widget_layout.addWidget(self.url_text)
        self.central_widget_layout.addWidget(self.select_button)
        self.central_widget_layout.addWidget(self.add_button)
        self.central_widget_layout.addWidget(self.ok_button)
        self.central_widget_layout.addWidget(self.play_button)
        self.central_widget_layout.addWidget(self.volume)

        self.HBox = QHBoxLayout()
        self.HBox.addLayout(self.central_widget_layout)
        self.HBox.addWidget(self.list_widget)

        self.mainVbox = QVBoxLayout(self.central_widget)
        self.mainVbox.addLayout(self.HBox)

        self.list_widget.itemClicked.connect(lambda x: self.change_url(a=self.list_widget.currentItem().text()))

    def sliderMoved(self):
        self.player.current_volume = self.volume.value() / 100
        self.player.audio_output.setVolume(self.player.current_volume)

    def change_url(self, a=None):
        if a is None:
            url = self.url_text.text()
        else:
            url = a
        if url is not None:
            self.url_text.clear()
            self.player.stop()
            self.player.setSource(QUrl(url))
            self.player.play()
            print('Станция изменена')
        else:
            print('Вы не ввели адрес')

    def play(self):
        self.play_button.setIcon(self.pause_icon)
        self.user_action = 1
        self.player.setSource(QUrl("http://pool.anison.fm:9000/AniSonFM(320)?nocache=0.9834540412142996"))
        self.player.play()

    def pause(self):
        self.play_button.setIcon(self.play_icon)
        self.user_action = 2
        self.player.pause()

    def unpause(self):
        self.play_button.setIcon(self.pause_icon)
        self.user_action = 1
        self.player.play()

    def play_pause_button_clicked(self):
        if self.user_action <= 0:
            self.play()
        elif self.user_action == 1:
            self.pause()
        elif self.user_action == 2:
            self.unpause()

    def _on_open_file(self):
        file_name = QFileDialog.getOpenFileName(self, '', None, 'Song (*.mp3)')[0]
        print(file_name)
        self.player.setSource(QUrl(file_name))
        self.player.play()


class MediaPlayer(QMediaPlayer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.audio_output = QAudioOutput()
        self.setAudioOutput(self.audio_output)
        self.audioOutput().setVolume(0.3)
        self.current_volume = self.audio_output.volume()

    def play(self):
        super().play()
        print('Запущено')

    def pause(self):
        super().pause()
        print('Остановлено')


if __name__ == '__main__':
    app = QApplication([])
    ex = MainWindow()
    ex.show()
    app.exec()
