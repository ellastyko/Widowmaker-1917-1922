from config import *
# # # game modules # # #
from app.lobby import Lobby # Online game
from app.menu import Menu # Start page
from app.settings import Settings # Settings page
from app.online import Online # Connection to server
from app.campaign import Campaign # Campaign page
from app.audio import Audio

class Window(QMainWindow):

    pages = {}

    def __init__(self):
        
        super().__init__()
        self.config = Config() # Include settings
        self.width = self.config.settings['screen']['width']
        self.height = self.config.settings['screen']['height']

        self.audio = Audio()

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
        self.setGeometry(0, 0, self.width, self.height)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Pages
        self.__page(Menu(), "menu")
        self.__page(Lobby(), "lobby")
        self.__page(Campaign(), "campaign")
        self.__page(Settings(), "settings")
        
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
        pass
        # print(event.type)    
    
    def keyPressEvent(self, event):
        # print(event.key())

        # print(QKeyEvent.isAutoRepeat(event))
        pressed = QKeyEvent.isAutoRepeat(event)
        if event.key() == 71 and not pressed:
            KEYS['F'] = True
            voice_thread = Thread(target=self.audio.record)
            voice_thread.start()

    def keyReleaseEvent(self, event):
        released = QKeyEvent.isAutoRepeat(event)
        if event.key() == 71 and released == False:
            KEYS['F'] = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


