import qstylizer.parser

class stylesheetclass(object):
    def stylesWhite(self):
        css = qstylizer.parser.parse(
        """
            QPushButton {background-color: rgb(255, 255, 255);
            border-radius: 20px;}
            QPushButton:hover {background-color: #193349;}
            QPushButton:pressed{ background-color: #6b4b62;}
        """)
        return css.toString()
    def stylesBlack(self):
        css = qstylizer.parser.parse(
        """
            QPushButton{background-color: rgb(0, 0, 0);
            border-radius: 10px;
            color: white;}
            QPushButton:hover{background-color: #193349;}
            QPushButton:pressed {background-color: #6b4b62;}
        """)
        return css.toString()
