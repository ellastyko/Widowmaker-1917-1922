from config import PageWindow
from PyQt5.QtWidgets import  QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QComboBox,  QSlider
from PyQt5 import QtCore
import os, json

DEFAULT = { 
    'graphics': {
        
        'screen': { 
            'width': 1600,
            'height': 900     
        }
    },    
    'volume': {
        'music': 50,
        'voice': 50,
        'effects': 50
    },
    'other': {
        'lang': 'ru'
    }
}


class Settings(PageWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        
        try:
            self.settings = open('./config.json', 'r+').read()
        except Exception as e:
            print(f'to default settings {e}')
            if os.path.isdir('settings') == False:
                os.mkdir('settings')
            open('./config.json', 'w+').write(json.dumps(DEFAULT))
            self.settings = open('./config.json', 'r+').read()
        finally:
            self.settings = json.loads(self.settings)

        self.UIComponents()


    def UIComponents(self):
        # QWidget
        widget = QWidget(self)
        self.setCentralWidget(widget)

        # Main Layout
        layout = QVBoxLayout(widget)
        # layout.setAlignment(QtCore.Qt.AlignCenter)
        # layout.setSpacing(1)

        # Child layouts
        settings = QHBoxLayout()

        graphics = QVBoxLayout()
        volume = QVBoxLayout()
        other = QVBoxLayout()
        # # # WIDGETS FOR GRAFICS # # #
        graphics_label = QLabel('Graphics')
        screen = QComboBox()
        # screen.changeEvent()
        screen.addItem('1920×1080')
        screen.addItem('1600×900')
        screen.addItem('1536×864')
        screen.addItem('1440×900')
        screen.addItem('1366×768')
        graphics.addWidget(graphics_label, 0)
        graphics.addWidget(screen, 0)
        # # # # # # # # # # # # # # # #
        # # # WIDGETS FOR VOLUME # # #
        volume_label = QLabel('Volume')   
        music = QSlider(QtCore.Qt.Horizontal)
        # music.
        voice = QSlider(QtCore.Qt.Horizontal)
        effects = QSlider(QtCore.Qt.Horizontal)
        all_sound = QSlider(QtCore.Qt.Horizontal)

        volume.addWidget(volume_label, 0)
        volume.addWidget(music, 0)
        volume.addWidget(voice, 0)
        volume.addWidget(effects, 0)
        volume.addWidget(all_sound, 0)


        # # # # # # # # # # # # # # # #     
        # # # WIDGETS FOR OTHER # # #
        other_label = QLabel('Other')
        lang = QComboBox()
        lang.addItem('Ru')
        lang.addItem('En')
        other.addWidget(other_label, 0)
        other.addWidget(lang, 0)
        other.addWidget(other_label, 0)
        # # # # # # # # # # # # # # # #

        settings.addLayout(graphics)
        settings.addLayout(volume)
        settings.addLayout(other)

        # # # FOOTER LAYOUT # # #
        footer = QHBoxLayout()
        
        # Buttons for footer
        back = QPushButton('Back')
        save = QPushButton('Save')


        back.setFixedSize(200, 50)
        save.setFixedSize(200, 50)

        footer.addWidget(back, 0)   
        footer.addWidget(save, 0)

        back.clicked.connect(self.handler("menu"))
        save.clicked.connect(self.handler("save"))

        # Adding child layouts to Main
        layout.addLayout(settings)
        layout.addLayout(footer)


    def handler(self, button):

        def handleButton():
            if button == "menu":
                self.goto("menu")
            elif button == "save":
                print('Save') # TODO
        return handleButton

    