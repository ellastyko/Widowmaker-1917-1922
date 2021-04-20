from config import *
# # # game modules # # #
from app.lobby import Lobby
from app.menu import Menu
from app.settings import Settings
from app.online import Online


class Window(QMainWindow):

    pages = {}

    def __init__(self):
        super().__init__()
        self.__initUI()
        

    def __initUI(self):
        self.setWindowIcon(QIcon('./assets/images/icon.png'))
        self.setStyleSheet(open('./assets/css/main.css').read())
        self.setGeometry(300, 100, 800, 600)


        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.__page(Menu(), "menu")
        self.__page(Lobby(), "lobby")
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
        print(event.type)    

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


