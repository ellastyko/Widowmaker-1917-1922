from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, \
                            QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsItem, QLabel, QPushButton, \
                            QDesktopWidget, QFrame, QFileDialog, QPlainTextEdit, QGridLayout, QWidget, \
                            QStackedWidget, QVBoxLayout, QOpenGLWidget

from PyQt5.QtGui import QPixmap, QTransform, QBrush, QColor, QPen, QCursor, QIcon, QImage, QPalette, QDrag, QKeyEvent
from PyQt5 import QtCore

import sys
import random
import os
import json
import numpy as np
from threading import Thread, main_thread
import pyaudio
import wave
import socket

_BASEDIR_ = os.path.dirname(__file__)
sys.path.append(_BASEDIR_)

KEYS = {
    'F': False,
    'W': False
}

class PageWindow(QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)




