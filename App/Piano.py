from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from static.stylesheet import stylesheetclass
from PyQt5.QtGui import QPixmap, QBrush, QPalette, QTransform
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QImage, QBrush, QPixmap
import os
from PyQt5.QtCore import QDir
from PyQt5.QtMultimedia import QSound


class ButtonFactory:
    def __init__(self, app):
        self.app = app

    def create_button(self, note, x_pos, y_pos, width, height, style, sound_path):
        button = QtWidgets.QPushButton(note, self.app)
        button.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        button.setStyleSheet(style)
        button.clicked.connect(lambda _, fname=sound_path: self.play_sound(fname))
        return button

    def play_sound(self, fname):
        sound_path = QDir.currentPath() +'/sounds/' + fname
        if os.path.exists(sound_path):
            QSound.play(sound_path)
        else:
            print(f"File {sound_path} not found")
        self.app.show()


class Piano_app(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Piano App")
        self.setFixedSize(1200, 500)
        img = QImage("static/pexel.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(img))
        self.setPalette(palette)

        button_factory = ButtonFactory(self)

        white_keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B','C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2','C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3']
        white_keys_buttons = []
        x_pos = 75
        for i in range(len(white_keys)):
            button = button_factory.create_button(white_keys[i], x_pos, 100, 40, 300, stylesheetclass.stylesWhite(self), f"{white_keys[i]}.wav")
            white_keys_buttons.append(button)
            x_pos += 50

        black_keys_csharp_and_dsharp = {'C#': 100, 'D#': 150, 'C#2': 450, 'D#2': 500, 'C#3': 800, 'D#3': 850}
        cd_buttons = {}
        for note, x_pos in black_keys_csharp_and_dsharp.items():
            button = button_factory.create_button(note, x_pos, 100, 40, 150, stylesheetclass.stylesBlack(self), f"{note}.wav")
            cd_buttons[note]=button

        black_keys_fsharp_gsharp_asharp = {'F#': 250, 'G#': 300, 'A#': 350, 'F#2': 600, 'G#2': 650, 'A#2': 700, 'F#3': 950, 'G#3': 1000, 'A#3': 1050}
        sharp_buttons = {}
        for note, x_pos in black_keys_fsharp_gsharp_asharp .items():
            button = button_factory.create_button(note, x_pos, 100, 40, 150, stylesheetclass.stylesBlack(self), f"{note}.wav")
            sharp_buttons[note]=button
