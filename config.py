from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, \
                            QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsItem, QLabel, QPushButton, \
                            QDesktopWidget, QFrame, QFileDialog, QPlainTextEdit, QGridLayout, QWidget, \
                            QStackedWidget, QVBoxLayout

from PyQt5.QtGui import QPixmap, QTransform, QBrush, QColor, QPen, QCursor, QIcon, QImage, QPalette, QDrag, QKeyEvent
from PyQt5 import QtCore

import sys
import random
import os
import json
import numpy as np
from threading import Thread

_BASEDIR_ = os.path.dirname(__file__)
sys.path.append(_BASEDIR_)

DEFAULT = { 
    'lang': 'en',
    'screen': { 
        'width': 1600,
        'height': 900     
    },
    'volume': {
        'music': 50,
        'voice': 50
    }
}

KEYS = {
    'F': False,
    'W': False
}

class PageWindow(QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)

class Config():

    settings = None

    def __init__(self):
        try:
            self.settings = open('./settings/config.json', 'r+').read()
        except Exception:
            print(f'to default settings {Exception}')
            if os.path.isdir('settings') == False:
                os.mkdir('settings')
            open('./settings/config.json', 'w+').write(json.dumps(DEFAULT))
            self.settings = open('./settings/config.json', 'r+').read()
        finally:
            self.settings = json.loads(self.settings)

