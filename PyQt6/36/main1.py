from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Медиа плеер')
        self.setGeometry(100, 100, 100, 100)
        self._setup_ui()

    def _setup_ui(self):
        self.central_widget = QWidget(self)
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        self.user_action = -1
        self.play_button = QPushButton()
        self.player = MediaPlayer()
        self.play_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        self.pause_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
        self.play_button.setIcon(self.play_icon)
        self.play_button.clicked.connect(self.play_pause_button_clicked)
        self.select_button = QPushButton('Select Music')
        self.select_button.clicked.connect(self._on_open_file)

        self.url_text = QLineEdit()
        self.ok_button = QPushButton()
        self.ok_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DialogYesButton)
        self.ok_button.setIcon(self.ok_icon)
        self.ok_button.clicked.connect(self.change_url)

        self.volume = QDial()
        self.volume.setMaximum(100)
        self.volume.setMinimum(0)
        self.volume.setValue(int(self.player.current_volume * 100))

        self.volume.valueChanged.connect(self.sliderMoved)
        self.central_widget_layout.addWidget(self.url_text)
        self.central_widget_layout.addWidget(self.select_button)
        self.central_widget_layout.addWidget(self.ok_button)
        self.central_widget_layout.addWidget(self.play_button)
        self.central_widget_layout.addWidget(self.volume)

    def sliderMoved(self):
        self.player.current_volume = self.volume.value() / 100
        self.player.audio_output.setVolume(self.player.current_volume)

    def change_url(self):
        url = self.url_text.text()
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
        file_name = QFileDialog.getOpenFileName(self, '', None, 'Song (*.mp3)')[0].split('/')[-1]
        self.player.setSource(QUrl.fromLocalFile(file_name))
        self.player.play()


class MediaPlayer(QMediaPlayer):
    def __init__(self, parent=None):
        QMediaPlayer.__init__(self, parent)
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
