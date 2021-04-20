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
        self.searchButton = QPushButton("", self)
        self.searchButton.clicked.connect(self.make_handleButton("searchButton"))

    def make_handleButton(self, button):
        def handleButton():
            if button == "searchButton":
                self.goto("settings")
        return handleButton