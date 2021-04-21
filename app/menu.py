from config import *
from config import PageWindow


class Menu(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):       
        self.setWindowTitle("Menu")
        self.UiComponents()

    def UiComponents(self):
        # QWidget
        widget = QWidget(self)
        self.setCentralWidget(widget)
        # Layout
        layout = QVBoxLayout(widget)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        # layout.setSpacing(100)
        # Buttons
        lobby = QPushButton('Online')
        campaign = QPushButton('Campaign')
        settings = QPushButton('Settings')
        out = QPushButton('Exit')

        lobby.setFixedSize(200, 50)
        campaign.setFixedSize(200, 50)
        settings.setFixedSize(200, 50)
        out.setFixedSize(200, 50)

        layout.addWidget(lobby, 0)   
        layout.addWidget(campaign, 1)
        layout.addWidget(settings, 2)     
        layout.addWidget(out, 3)

        lobby.clicked.connect(self.handler("lobby"))
        campaign.clicked.connect(self.handler("campaign"))
        settings.clicked.connect(self.handler("settings"))
        out.clicked.connect(self.handler("exit"))

    def handler(self, button):

        def handleButton():
            if button == "lobby":
                self.goto("lobby")
            elif button == "campaign":
                self.goto("campaign")
            elif button == "settings":
                self.goto("settings")
            elif button == "exit":
                exit(1)
        return handleButton