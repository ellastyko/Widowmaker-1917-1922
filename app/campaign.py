from config import *
from PyQt5.QtWidgets import  QLabel, QPushButton,  QWidget, QVBoxLayout,  QHBoxLayout

from PyQt5 import QtCore

fraction = ['Советы', 'УНР', 'Алашская автономия', 'Войско Донское', 'Финляндия', 'Комуч']

class Campaign(PageWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Campaign")
        self.UIComponents()

    def UIComponents(self):
        # QWidget
        widget = QWidget(self)
        self.setCentralWidget(widget)
        # Main Layout
        layout = QVBoxLayout(widget)
        # layout.setSpacing(0)

        # Child layouts
        header = QHBoxLayout()
        header.setGeometry(QtCore.QRect(0, 0, 800, 50))
        # header.setAlignment(QtCore.Qt.AlignCenter)
        main = QHBoxLayout()
        # main.setSpacing(0)
        fractions = QVBoxLayout()
        # main.setGeometry(QtCore.QRect(0, 100, 800, 200))
        fractions.setAlignment(QtCore.Qt.AlignRight)
        footer = QHBoxLayout()
        # footer.setGeometry(QtCore.QRect(20, 20, 741, 531))

        # Adding child layouts
        layout.addLayout(header)
        layout.addLayout(main)   
        layout.addLayout(footer)

        # Header
        # ab = QLabel()
        # ab.setObjectName('map')
        # # mb.setFixedSize(650, 300)
 
        # header.addWidget(ab, 0)
        early = QPushButton('1918')
        middle = QPushButton('1919')
        late = QPushButton('1919')

        early.setFixedSize(80, 40)
        middle.setFixedSize(80, 40)
        late.setFixedSize(80, 40)
 
        header.addWidget(early, 0)
        header.addWidget(middle, 1)
        header.addWidget(late, 1)


        # Main
        mb = QLabel()
        mb.setObjectName('map')
        mb.setMinimumSize(QtCore.QSize(500, 400))
        # mb.setFixedSize(650, 300)
 
        main.addWidget(mb, 0)
        main.addLayout(fractions)
        for i in range(len(fraction)):
            fraction[i] = QPushButton(fraction[i])
            fraction[i].setFixedSize(180, 35)
            fractions.addWidget(fraction[i], 0)


        # Footer
        back = QPushButton('Back')
        play = QPushButton('Play')

        back.setFixedSize(150, 40)
        play.setFixedSize(150, 40)
 
        footer.addWidget(back, 0)
        footer.addWidget(play, 1)

        back.clicked.connect(self.handler("menu"))

    def handler(self, button):

        def handleButton():
            if button == "lobby":
                self.goto("lobby")
            elif button == "campaign":
                self.goto("campaign")
            elif button == "settings":
                self.goto("settings")
            elif button == "menu":
                self.goto("menu")
            elif button == "exit":
                exit(1)
        return handleButton