from config import *
from config import PageWindow
from config import Config

class Settings(PageWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Settings")
        self.UiComponents()

    def UiComponents(self):
        self.backButton = QPushButton("Обратно", self)
        self.backButton.setGeometry(QtCore.QRect(5, 5, 100, 20))
        self.backButton.clicked.connect(self.goToMain)

    def goToMain(self):
        self.goto("lobby")