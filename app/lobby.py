from config import *
from config import PageWindow


class Lobby(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lobby")
        self.UiComponents()

    def UiComponents(self):
        self.searchButton = QPushButton("", self)
        self.searchButton.clicked.connect(self.make_handleButton("searchButton"))

    def make_handleButton(self, button):
        def handleButton():
            if button == "searchButton":
                self.goto("menu")
        return handleButton