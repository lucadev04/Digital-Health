from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6.uic import loadUi  # Import loadUi from PyQt6.uic

import psutil
import datetime
import sys

class mainscreen(QtWidgets.QWidget):  # Inherit from QWidget
    def __init__(self, parent=None):
        super().__init__(parent)  # Call the base class constructor
        self = loadUi("/home/luca/Luca/Privat/Python/digitalhealth/GUI/mainscreen.ui", self)  # Load UI file


        # Connect the timer to the update function
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.uptime)
        self.timer.start(1000)


    def uptime(self):
        now_time = datetime.datetime.today()
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        up_time = now_time - boot_time
        up_time_2 = str(up_time).split('.')[0]
        up_time_h = up_time_2.split(':')[0]
        up_time_min = up_time_2.split(':')[1]
        up_time_sec = up_time_2.split(':')[2]
        self.lblusetime.setText(up_time_h + ":" + up_time_min + ":" + up_time_sec)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mainscreen()
    w.show()
    sys.exit(app.exec())

