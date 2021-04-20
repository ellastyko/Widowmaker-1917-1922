import sys, random, os
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, \
                            QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsItem, QLabel, QPushButton, \
                            QDesktopWidget, QFrame, QFileDialog, QPlainTextEdit, QGridLayout, QWidget, \
                            QStackedWidget

from PyQt5.QtGui import QPixmap, QTransform, QBrush, QColor, QPen, QCursor, QIcon, QImage, QPalette, QDrag
from PyQt5 import QtCore


_BASEDIR_ = os.path.dirname(__file__)
sys.path.append(_BASEDIR_)

class PageWindow(QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)

class Config():

    def __init__(self):
        try:
            settings = open('./app/settings/config.json')
        except Exception:
            print(f'to default settings {Exception}')
        else:
            print('Opened')
        finally:
            print(settings)
