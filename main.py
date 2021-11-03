from config import *
# # # game modules # # #
from app.lobby import Lobby # Online game
from app.menu import Menu # Start page
from app.settings import Settings # Settings page
from app.client import Client # Connection to server
from app.campaign import Campaign # Campaign page
from app.audio import Audio
from app.sounds import Sounds

class Window(QMainWindow):

    pages = {}

    def __init__(self):
        
        super().__init__()
        
        
        self.menu = Menu()
        self.settings = Settings()
        self.lobby = Lobby()
        self.campaign = Campaign()

        # Поключаем звук меню и эффектов
        self.sounds = Sounds()          

        self.__initUI()
        
        

    def __initUI(self):

        self.setWindowTitle('Widowmaker 1917-1922')
        # Style
        self.setWindowIcon(QIcon('./assets/images/icon.png'))
        self.setStyleSheet(open('./assets/css/main.css').read())
        self.setObjectName('main')
        # Background
        img = QImage("./assets/images/sturm.jpg")
        sImage = img.scaled(QtCore.QSize(1000, 650))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        # Size
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1600, 900)
        # self.setGeometry(0, 0, self.width, self.height)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # PAGES
        self.__page(self.menu, "menu")
        self.__page(self.lobby, "lobby")
        self.__page(self.campaign, "campaign")
        self.__page(self.settings, "settings")
        
        self.goto("menu")


    def __page(self, widget, name):
        self.pages[name] = widget
        self.stacked_widget.addWidget(widget)
        widget.gotoSignal.connect(self.goto)


    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.pages:
            widget = self.pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


    def resizeEvent(self, event):
        print(event.type())    
    

    def keyPressEvent(self, event):
        # print(event.key())
        pressed = QKeyEvent.isAutoRepeat(event)
        if event.key() == 71 and not pressed:
            KEYS['F'] = True
            voice_thread = Thread(target=self.menu.client.audio.record)
            voice_thread.start()


    def keyReleaseEvent(self, event):
        released = QKeyEvent.isAutoRepeat(event)
        if event.key() == 71 and released == False:
            KEYS['F'] = False

   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.showFullScreen()
    sys.exit(app.exec_())


