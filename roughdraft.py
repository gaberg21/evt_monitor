# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roughdraft.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 871, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.gridLayout.setSpacing(40)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.flowLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.flowLabel.setFont(font)
        self.flowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.flowLabel.setObjectName("flowLabel")
        self.verticalLayout_2.addWidget(self.flowLabel)
        self.flowNum = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.flowNum.setSmallDecimalPoint(False)
        self.flowNum.setDigitCount(7)
        self.flowNum.setMode(QtWidgets.QLCDNumber.Dec)
        self.flowNum.setProperty("value", 0.0)
        self.flowNum.setProperty("intValue", 0)
        self.flowNum.setObjectName("flowNum")
        self.verticalLayout_2.addWidget(self.flowNum)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.totVolLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.totVolLabel.setFont(font)
        self.totVolLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totVolLabel.setObjectName("totVolLabel")
        self.verticalLayout_3.addWidget(self.totVolLabel)
        self.totVolNum = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.totVolNum.setDigitCount(7)
        self.totVolNum.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.totVolNum.setObjectName("totVolNum")
        self.verticalLayout_3.addWidget(self.totVolNum)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.amperageLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.amperageLabel.setFont(font)
        self.amperageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.amperageLabel.setObjectName("amperageLabel")
        self.verticalLayout_4.addWidget(self.amperageLabel)
        self.amperageNum = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.amperageNum.setDigitCount(7)
        self.amperageNum.setObjectName("amperageNum")
        self.verticalLayout_4.addWidget(self.amperageNum)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.voltageLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.voltageLabel.setFont(font)
        self.voltageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.voltageLabel.setObjectName("voltageLabel")
        self.verticalLayout_11.addWidget(self.voltageLabel)
        self.voltageNum = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.voltageNum.setDigitCount(7)
        self.voltageNum.setObjectName("voltageNum")
        self.verticalLayout_11.addWidget(self.voltageNum)
        self.gridLayout.addLayout(self.verticalLayout_11, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mphLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mphLabel.setFont(font)
        self.mphLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mphLabel.setObjectName("mphLabel")
        self.verticalLayout.addWidget(self.mphLabel)
        self.mphNum = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.mphNum.setDigitCount(7)
        self.mphNum.setObjectName("mphNum")
        self.verticalLayout.addWidget(self.mphNum)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.distanceLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.distanceLabel.setFont(font)
        self.distanceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.distanceLabel.setObjectName("distanceLabel")
        self.verticalLayout_10.addWidget(self.distanceLabel)
        self.distanceNum = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.distanceNum.setDigitCount(7)
        self.distanceNum.setObjectName("distanceNum")
        self.verticalLayout_10.addWidget(self.distanceNum)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.gridLayout.addLayout(self.verticalLayout_9, 0, 2, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 440, 871, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeDisplay = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.timeDisplay.setFont(font)
        self.timeDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.timeDisplay.setObjectName("timeDisplay")
        self.horizontalLayout.addWidget(self.timeDisplay)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_3.addWidget(self.startButton)
        self.pauseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pauseButton.setFont(font)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_3.addWidget(self.pauseButton)
        self.resetButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_3.addWidget(self.resetButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.flowLabel.setText(_translate("MainWindow", "Flow Rate"))
        self.totVolLabel.setText(_translate("MainWindow", "Total Volume"))
        self.amperageLabel.setText(_translate("MainWindow", "Amperage"))
        self.voltageLabel.setText(_translate("MainWindow", "Voltage"))
        self.mphLabel.setText(_translate("MainWindow", "MPH"))
        self.distanceLabel.setText(_translate("MainWindow", "Miles"))
        self.timeDisplay.setText(_translate("MainWindow", "00:00"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
