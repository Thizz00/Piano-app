import unittest
from PyQt5.QtWidgets import QApplication
from piano1 import Gui_App

class TestGuiApp(unittest.TestCase):

    def test_init_ui(self):
        app = QApplication([])
        gui_app = Gui_App()
        self.assertEqual(gui_app.windowTitle(), "Piano App")
        self.assertEqual(gui_app.width(), 1200)
        self.assertEqual(gui_app.height(), 500)

    def test_play_sound(self):
        app = QApplication([])
        gui_app = Gui_App()
        self.assertEqual(gui_app.play_sound("C.wav"))
        # assert that the sound was played
        # TODO: find a way to test QSound.play() method

if __name__ == '__main__':
    unittest.main()