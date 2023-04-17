import sys
from PyQt5.QtWidgets import QApplication
from App.Piano import Piano_app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Piano_app()
    ex.show()
    sys.exit(app.exec_())