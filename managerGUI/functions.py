from PyQt5 import *
from PyQt5.QtCore import *
from FirstVersion import *
import sys


def maximise_window(ui):
    if ui.isMaximized():
        ui.showNormal()
    else:
        ui.showMaximized()
