from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, \
                            QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsItem, QLabel, QPushButton, \
                            QDesktopWidget, QFrame, QFileDialog, QPlainTextEdit, QGridLayout, QWidget, \
                            QStackedWidget, QVBoxLayout, QOpenGLWidget

from PyQt5.QtGui import QPixmap, QTransform, QBrush, QColor, QPen, QCursor, QIcon, QImage, QPalette, QDrag, QKeyEvent
from PyQt5 import QtCore

import sys
import os

class PageWindow(QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)



class env:

    BASEDIR =  os.path.dirname(__file__)

    def __init__(self) -> None:
        sys.path.append(self.BASEDIR)
