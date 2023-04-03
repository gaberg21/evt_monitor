from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer

import sys
import os
import serial
from time import strftime, gmtime

from serialtesting import XFM, CycleAnalyst
from roughdraft import Ui_MainWindow

#os.system("pyuic5 roughdraft.ui -o roughdraft.py")

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #self.xfm = XFM('COM3')
        
        #flow_timer = QTimer(self)
        #flow_timer.timeout.connect(self.flow_update)
        #flow_timer.start(333)

        #self.xfm.reset_totalizer()
        #vol_timer = QTimer(self)
        #vol_timer.timeout.connect(self.vol_update)
        #vol_timer.start(333)
        
        
        #self.ca = CycleAnalyst('COM4')

        #ca_timer = QTimer(self)
        #ca_timer.timeout.connect(self.ca_update)
        #ca_timer.start(10)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.startButton.pressed.connect(self.start)
        self.ui.pauseButton.pressed.connect(self.pause)
        self.ui.resetButton.pressed.connect(self.reset)
        
        self.count = 0
        stopwatch_timer = QTimer(self)
        stopwatch_timer.timeout.connect(self.timer_worker)
        stopwatch_timer.start(1000)
        self.running = True
        
    def flow_update(self):
        current_flow = self.xfm.read_flow()
        self.ui.flowNum.display(current_flow)

    def vol_update(self):
        current_vol = self.xfm.read_volume()
        self.ui.totVolNum.display(current_vol)
        
    def ca_update(self):
        current_values = self.ca.read_values()
        self.ui.voltageNum.display(current_values[1])
        self.ui.amperageNum.display(current_values[2])
        self.ui.mphNum.display(current_values[3])
        self.ui.distanceNum.display(current_values[4])
        
    def timer_worker(self):
        if self.running:
            self.count += 1
        text = str(strftime("%M:%S", gmtime(self.count)))
        self.ui.timeDisplay.setText(text)
                
    def start(self):
        self.running = True
        
    def pause(self):
        self.running = False
    
    def reset(self):
        self.running = False
        self.count = 0
        text = str(strftime("%M:%S", gmtime(self.count)))
        self.ui.timeDisplay.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())