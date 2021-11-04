from config import PageWindow
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout
from PyQt5 import QtCore

class Menu(PageWindow):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.UIComponents() 
        

    def UIComponents(self):
        # QWidget
        widget = QWidget(self)
        self.setCentralWidget(widget)
        # Layout
        layout = QVBoxLayout(widget)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        # layout.setSpacing(100)
        # Buttons
        campaign = QPushButton('Campaign')
        settings = QPushButton('Settings')
        out = QPushButton('Exit')

        campaign.setFixedSize(200, 50)
        settings.setFixedSize(200, 50)
        out.setFixedSize(200, 50)

        layout.addWidget(campaign, 1)
        layout.addWidget(settings, 2)     
        layout.addWidget(out, 3)

        campaign.clicked.connect(self.handler("campaign"))
        settings.clicked.connect(self.handler("settings"))
        out.clicked.connect(self.handler("exit"))

    def handler(self, button):

        def handleButton():
            if button == "campaign":
                self.goto("campaign")
            elif button == "settings":
                self.goto("settings")
            elif button == "exit":
                exit(1)
        return handleButton
    
    # @property
    # def client(self):
    #     return self.__client