from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import  QWidget
from static.stylesheet import stylesheetclass
from PyQt5.QtGui import QPixmap, QBrush, QPalette, QTransform
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette ,QImage, QBrush
from PyQt5.QtGui import QPixmap, QBrush, QPalette
import os
from PyQt5.QtCore import QDir
from PyQt5.QtMultimedia import QSound

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

        
        octave = ['C', 'D', 'E', 'F', 'G', 'A', 'B','C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2','C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3']
        octave_buttons = []
        x_pos = 75
        for i in range(len(octave)):
            button = QtWidgets.QPushButton(octave[i],self)
            button.setGeometry(QtCore.QRect(x_pos, 100, 40, 300))
            button.setStyleSheet(stylesheetclass.stylesWhite(self))
            button.clicked.connect(lambda _, fname=f"{octave[i]}.wav": self.play_sound(fname))
            octave_buttons.append(button)
            x_pos += 50
        
        cd = {'C#': 100, 'D#': 150, 'C#2': 450, 'D#2': 500, 'C#3': 800, 'D#3': 850}

        cd_buttons = {}
        for note, x_pos in cd.items():
            button = QtWidgets.QPushButton(note, self)
            button.setGeometry(QtCore.QRect(x_pos, 100, 40, 150))
            button.setStyleSheet(stylesheetclass.stylesBlack(self))
            button.clicked.connect(lambda _, fname=f"{note}.wav": self.play_sound(fname))
            cd_buttons[note]=button

            


        sharp_dict = {'F#': 250, 'G#': 300, 'A#': 350, 'F#2': 600, 'G#2': 650, 'A#2': 700, 'F#3': 950, 'G#3': 1000, 'A#3': 1050}
        sharp_buttons = {}
        for note, x_pos in sharp_dict.items():
            button = QtWidgets.QPushButton(note, self)
            button.setGeometry(QtCore.QRect(x_pos, 100, 40, 150))
            button.setStyleSheet(stylesheetclass.stylesBlack(self))
            button.clicked.connect(lambda _, fname=f"{note}.wav": self.play_sound(fname))
            sharp_buttons[note]=button

    def play_sound(self, fname):
        sound_path = QDir.currentPath() +'/sounds/' + fname
        if os.path.exists(sound_path):
            QSound.play(sound_path)
        else:
            print(f"File {sound_path} not found")
        self.show()  
