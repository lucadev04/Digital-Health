from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from PyQt6.uic import *

import psutil
import datetime
import sys

def uptime():
    now_time = datetime.datetime.today()
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    up_time = now_time-boot_time
    up_time_2 = str(up_time).split('.')[0]
    up_time_h = up_time_2.split(':')[0]
    up_time_min = up_time_2.split(':')[1]
    up_time_sec = up_time_2.split(':')[2]
    w.lblusetime.setText(up_time_h + ":" + up_time_min + ":" + up_time_sec)

app = QApplication(sys.argv)
w = loadUi("/home/luca/Luca/Privat/Python/digitalhealth/GUI/mainscreen.ui")
timer = QTimer()
timer.timeout.connect(uptime)
timer.start(1000)

w.show()
sys.exit(app.exec())
