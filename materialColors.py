# -*- coding: utf-8 -*-
# Material Color Tool
# Source : - https://material.io/guidelines/style/color.html#color-color-palette
# Script By: Ruchit Bhatt
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import sys

class materialColorsUI(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 820)
        MainWindow.setMinimumSize(QtCore.QSize(282, 820))
        MainWindow.setMaximumSize(QtCore.QSize(282, 820))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.redColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.redColorBtn.setStyleSheet("background-color: #f44336;\n"
"border-style: solid;\n"
"border-color: #f44336;\n"
"border-width: 5px;\n"
"border-radius: 10px;\n")
        self.redColorBtn.setText("")
        self.redColorBtn.setFlat(False)
        self.redColorBtn.setObjectName("redColorBtn")
        self.verticalLayout_2.addWidget(self.redColorBtn)
        self.pinkColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pinkColorBtn.setStyleSheet("background-color: #E91E63;\n"
"border-style: solid;\n"
"border-color: #E91E63;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.pinkColorBtn.setText("")
        self.pinkColorBtn.setFlat(False)
        self.pinkColorBtn.setObjectName("pinkColorBtn")
        self.verticalLayout_2.addWidget(self.pinkColorBtn)
        self.purpleColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.purpleColorBtn.setStyleSheet("background-color: #9C27B0;\n"
"border-style: solid;\n"
"border-color: #9C27B0;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.purpleColorBtn.setText("")
        self.purpleColorBtn.setFlat(False)
        self.purpleColorBtn.setObjectName("purpleColorBtn")
        self.verticalLayout_2.addWidget(self.purpleColorBtn)
        self.deepPurpleColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deepPurpleColorBtn.setStyleSheet("background-color: #673AB7;\n"
"border-style: solid;\n"
"border-color: #673AB7;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.deepPurpleColorBtn.setText("")
        self.deepPurpleColorBtn.setFlat(False)
        self.deepPurpleColorBtn.setObjectName("deepPurpleColorBtn")
        self.verticalLayout_2.addWidget(self.deepPurpleColorBtn)
        self.indigoColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.indigoColorBtn.setStyleSheet("background-color: #3F51B5;\n"
"border-style: solid;\n"
"border-color: #3F51B5;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.indigoColorBtn.setText("")
        self.indigoColorBtn.setFlat(False)
        self.indigoColorBtn.setObjectName("indigoColorBtn")
        self.verticalLayout_2.addWidget(self.indigoColorBtn)
        self.blueColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.blueColorBtn.setStyleSheet("background-color: #2196F3;\n"
"border-style: solid;\n"
"border-color: #2196F3;\n"
"border-width: 5px;\n"
"border-radius: 10px;")
        self.blueColorBtn.setText("")
        self.blueColorBtn.setFlat(False)
        self.blueColorBtn.setObjectName("blueColorBtn")
        self.verticalLayout_2.addWidget(self.blueColorBtn)
        self.lightBlueColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.lightBlueColorBtn.setStyleSheet("background-color: #03A9F4;\n"
"border-style: solid;\n"
"border-color: #03A9F4;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.lightBlueColorBtn.setText("")
        self.lightBlueColorBtn.setFlat(False)
        self.lightBlueColorBtn.setObjectName("lightBlueColorBtn")
        self.verticalLayout_2.addWidget(self.lightBlueColorBtn)
        self.cyanColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cyanColorBtn.setStyleSheet("background-color: #00BCD4;\n"
"border-style: solid;\n"
"border-color: #00BCD4;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.cyanColorBtn.setText("")
        self.cyanColorBtn.setFlat(False)
        self.cyanColorBtn.setObjectName("cyanColorBtn")
        self.verticalLayout_2.addWidget(self.cyanColorBtn)
        self.tealColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.tealColorBtn.setStyleSheet("background-color: #009688;\n"
"border-style: solid;\n"
"border-color: #009688;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.tealColorBtn.setText("")
        self.tealColorBtn.setFlat(False)
        self.tealColorBtn.setObjectName("tealColorBtn")
        self.verticalLayout_2.addWidget(self.tealColorBtn)
        self.greenColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.greenColorBtn.setStyleSheet("background-color: #4CAF50;\n"
"border-style: solid;\n"
"border-color: #4CAF50;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.greenColorBtn.setText("")
        self.greenColorBtn.setFlat(False)
        self.greenColorBtn.setObjectName("greenColorBtn")
        self.verticalLayout_2.addWidget(self.greenColorBtn)
        self.lightGreenColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.lightGreenColorBtn.setStyleSheet("background-color: #8BC34A;\n"
"border-style: solid;\n"
"border-color: #8BC34A;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.lightGreenColorBtn.setText("")
        self.lightGreenColorBtn.setFlat(False)
        self.lightGreenColorBtn.setObjectName("lightGreenColorBtn")
        self.verticalLayout_2.addWidget(self.lightGreenColorBtn)
        self.limeColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.limeColorBtn.setStyleSheet("background-color: #CDDC39;\n"
"border-style: solid;\n"
"border-color: #CDDC39;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.limeColorBtn.setText("")
        self.limeColorBtn.setFlat(False)
        self.limeColorBtn.setObjectName("limeColorBtn")
        self.verticalLayout_2.addWidget(self.limeColorBtn)
        self.yellowColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.yellowColorBtn.setStyleSheet("background-color: #FFEB3B;\n"
"border-style: solid;\n"
"border-color: #FFEB3B;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.yellowColorBtn.setText("")
        self.yellowColorBtn.setFlat(False)
        self.yellowColorBtn.setObjectName("yellowColorBtn")
        self.verticalLayout_2.addWidget(self.yellowColorBtn)
        self.amberColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.amberColorBtn.setStyleSheet("background-color: #FFC107;\n"
"border-style: solid;\n"
"border-color: #FFC107;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.amberColorBtn.setText("")
        self.amberColorBtn.setFlat(False)
        self.amberColorBtn.setObjectName("amberColorBtn")
        self.verticalLayout_2.addWidget(self.amberColorBtn)
        self.orangeColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.orangeColorBtn.setStyleSheet("background-color: #FF9800;\n"
"border-style: solid;\n"
"border-color: #FF9800;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.orangeColorBtn.setText("")
        self.orangeColorBtn.setFlat(False)
        self.orangeColorBtn.setObjectName("orangeColorBtn")
        self.verticalLayout_2.addWidget(self.orangeColorBtn)
        self.deepOrangeColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deepOrangeColorBtn.setStyleSheet("background-color: #FF5722;\n"
"border-style: solid;\n"
"border-color: #FF5722;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.deepOrangeColorBtn.setText("")
        self.deepOrangeColorBtn.setFlat(False)
        self.deepOrangeColorBtn.setObjectName("deepOrangeColorBtn")
        self.verticalLayout_2.addWidget(self.deepOrangeColorBtn)
        self.brownColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.brownColorBtn.setStyleSheet("background-color: #795548;\n"
"border-style: solid;\n"
"border-color: #795548;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.brownColorBtn.setText("")
        self.brownColorBtn.setFlat(False)
        self.brownColorBtn.setObjectName("brownColorBtn")
        self.verticalLayout_2.addWidget(self.brownColorBtn)
        self.greyColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.greyColorBtn.setStyleSheet("background-color: #9E9E9E;\n"
"border-style: solid;\n"
"border-color: #9E9E9E;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.greyColorBtn.setText("")
        self.greyColorBtn.setFlat(False)
        self.greyColorBtn.setObjectName("greyColorBtn")
        self.verticalLayout_2.addWidget(self.greyColorBtn)
        self.blueGreyColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.blueGreyColorBtn.setStyleSheet("background-color: #607D8B;\n"
"border-style: solid;\n"
"border-color: #607D8B;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.blueGreyColorBtn.setText("")
        self.blueGreyColorBtn.setFlat(False)
        self.blueGreyColorBtn.setObjectName("blueGreyColorBtn")
        self.verticalLayout_2.addWidget(self.blueGreyColorBtn)
        self.blackColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.blackColorBtn.setStyleSheet("background-color: #000000;\n"
"border-style: solid;\n"
"border-color: #000000;\n"
"border-width: 5px;\n"
"border-radius: 10px")
        self.blackColorBtn.setText("")
        self.blackColorBtn.setFlat(False)
        self.blackColorBtn.setObjectName("blackColorBtn")
        self.verticalLayout_2.addWidget(self.blackColorBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.stackedWidget.setObjectName("stackedWidget")
        self.redPage = QtWidgets.QWidget()
        self.redPage.setObjectName("redPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.redPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.redBtn = QtWidgets.QPushButton(self.redPage)
        self.redBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.redBtn.setFont(font)
        self.redBtn.setStyleSheet("background-color: #F44336;\n"
"border-style: solid;\n"
"color:#ffffff;")
        self.redBtn.setObjectName("redBtn")
        self.verticalLayout_3.addWidget(self.redBtn)
        self.red50Btn = QtWidgets.QPushButton(self.redPage)
        self.red50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.red50Btn.setFont(font)
        self.red50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.red50Btn.setStyleSheet("background-color: #FFEBEE;\n"
"border-style: solid;\n"
"Text-align:right")
        self.red50Btn.setObjectName("red50Btn")
        self.verticalLayout_3.addWidget(self.red50Btn)
        self.red100Btn = QtWidgets.QPushButton(self.redPage)
        self.red100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.red100Btn.setFont(font)
        self.red100Btn.setStyleSheet("background-color: #FFCDD2;\n"
"border-style: solid;\n"
"Text-align:right")
        self.red100Btn.setObjectName("red100Btn")
        self.verticalLayout_3.addWidget(self.red100Btn)
        self.red200Btn = QtWidgets.QPushButton(self.redPage)
        self.red200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.red200Btn.setFont(font)
        self.red200Btn.setStyleSheet("background-color: #EF9A9A;\n"
"border-style: solid;\n"
"Text-align:right")
        self.red200Btn.setObjectName("red200Btn")
        self.verticalLayout_3.addWidget(self.red200Btn)
        self.red300Btn = QtWidgets.QPushButton(self.redPage)
        self.red300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.red300Btn.setFont(font)
        self.red300Btn.setStyleSheet("background-color: #E57373;\n"
"border-style: solid;\n"
"Text-align:right")
        self.red300Btn.setObjectName("red300Btn")
        self.verticalLayout_3.addWidget(self.red300Btn)
        self.red400Btn = QtWidgets.QPushButton(self.redPage)
        self.red400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.red400Btn.setFont(font)
        self.red400Btn.setStyleSheet("background-color: #EF5350;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.red400Btn.setObjectName("red400Btn")
        self.verticalLayout_3.addWidget(self.red400Btn)
        self.red500Btn = QtWidgets.QPushButton(self.redPage)
        self.red500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.red500Btn.setFont(font)
        self.red500Btn.setStyleSheet("background-color: #F44336;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.red500Btn.setObjectName("red500Btn")
        self.verticalLayout_3.addWidget(self.red500Btn)
        self.red600Btn = QtWidgets.QPushButton(self.redPage)
        self.red600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.red600Btn.setFont(font)
        self.red600Btn.setStyleSheet("background-color: #E53935;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.red600Btn.setObjectName("red600Btn")
        self.verticalLayout_3.addWidget(self.red600Btn)
        self.red700Btn = QtWidgets.QPushButton(self.redPage)
        self.red700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.red700Btn.setFont(font)
        self.red700Btn.setStyleSheet("background-color: #D32F2F;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.red700Btn.setObjectName("red700Btn")
        self.verticalLayout_3.addWidget(self.red700Btn)
        self.red800Btn = QtWidgets.QPushButton(self.redPage)
        self.red800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.red800Btn.setFont(font)
        self.red800Btn.setStyleSheet("background-color: #C62828;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.red800Btn.setObjectName("red800Btn")
        self.verticalLayout_3.addWidget(self.red800Btn)
        self.red900Btn = QtWidgets.QPushButton(self.redPage)
        self.red900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.red900Btn.setFont(font)
        self.red900Btn.setStyleSheet("background-color: #B71C1C;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.red900Btn.setObjectName("red900Btn")
        self.verticalLayout_3.addWidget(self.red900Btn)
        self.redA100Btn = QtWidgets.QPushButton(self.redPage)
        self.redA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.redA100Btn.setFont(font)
        self.redA100Btn.setStyleSheet("background-color: #FF8A80;\n"
"border-style: solid;\n"
"Text-align:right")
        self.redA100Btn.setObjectName("redA100Btn")
        self.verticalLayout_3.addWidget(self.redA100Btn)
        self.redA200Btn = QtWidgets.QPushButton(self.redPage)
        self.redA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.redA200Btn.setFont(font)
        self.redA200Btn.setStyleSheet("background-color: #FF5252;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.redA200Btn.setObjectName("redA200Btn")
        self.verticalLayout_3.addWidget(self.redA200Btn)
        self.redA400Btn = QtWidgets.QPushButton(self.redPage)
        self.redA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.redA400Btn.setFont(font)
        self.redA400Btn.setStyleSheet("background-color: #FF1744;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.redA400Btn.setObjectName("redA400Btn")
        self.verticalLayout_3.addWidget(self.redA400Btn)
        self.redA700Btn = QtWidgets.QPushButton(self.redPage)
        self.redA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.redA700Btn.setFont(font)
        self.redA700Btn.setStyleSheet("background-color: #D50000;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.redA700Btn.setObjectName("redA700Btn")
        self.verticalLayout_3.addWidget(self.redA700Btn)
        self.stackedWidget.addWidget(self.redPage)
        self.pinkPage = QtWidgets.QWidget()
        self.pinkPage.setObjectName("pinkPage")
        self.pink100Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pink100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.pink100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pink100Btn.setFont(font)
        self.pink100Btn.setStyleSheet("background-color: #F8BBD0;\n"
"border-style: solid;\n"
"Text-align:right")
        self.pink100Btn.setObjectName("pink100Btn")
        self.pinkA200Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pinkA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.pinkA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pinkA200Btn.setFont(font)
        self.pinkA200Btn.setStyleSheet("background-color: #FF4081;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.pinkA200Btn.setObjectName("pinkA200Btn")
        self.pinkA400Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pinkA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.pinkA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pinkA400Btn.setFont(font)
        self.pinkA400Btn.setStyleSheet("background-color: #F50057;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.pinkA400Btn.setObjectName("pinkA400Btn")
        self.pink50Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pink50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.pink50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.pink50Btn.setFont(font)
        self.pink50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pink50Btn.setStyleSheet("background-color: #FCE4EC;\n"
"border-style: solid;\n"
"Text-align:right")
        self.pink50Btn.setObjectName("pink50Btn")
        self.pinkA100Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pinkA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.pinkA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pinkA100Btn.setFont(font)
        self.pinkA100Btn.setStyleSheet("background-color: #FF80AB;\n"
"border-style: solid;\n"
"Text-align:right")
        self.pinkA100Btn.setObjectName("pinkA100Btn")
        self.pink900Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pink900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.pink900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pink900Btn.setFont(font)
        self.pink900Btn.setStyleSheet("background-color: #880E4F;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.pink900Btn.setObjectName("pink900Btn")
        self.pink400Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pink400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.pink400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pink400Btn.setFont(font)
        self.pink400Btn.setStyleSheet("background-color: #EC407A;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.pink400Btn.setObjectName("pink400Btn")
        self.pink700Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pink700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.pink700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pink700Btn.setFont(font)
        self.pink700Btn.setStyleSheet("background-color: #C2185B;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.pink700Btn.setObjectName("pink700Btn")
        self.pinkA700Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pinkA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.pinkA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pinkA700Btn.setFont(font)
        self.pinkA700Btn.setStyleSheet("background-color: #C51162;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.pinkA700Btn.setObjectName("pinkA700Btn")
        self.pink200Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pink200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.pink200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pink200Btn.setFont(font)
        self.pink200Btn.setStyleSheet("background-color: #F48FB1;\n"
"border-style: solid;\n"
"Text-align:right")
        self.pink200Btn.setObjectName("pink200Btn")
        self.pink800Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pink800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.pink800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pink800Btn.setFont(font)
        self.pink800Btn.setStyleSheet("background-color: #AD1457;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.pink800Btn.setObjectName("pink800Btn")
        self.pink300Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pink300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.pink300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pink300Btn.setFont(font)
        self.pink300Btn.setStyleSheet("background-color: #F06292;\n"
"border-style: solid;\n"
"Text-align:right")
        self.pink300Btn.setObjectName("pink300Btn")
        self.pinkBtn = QtWidgets.QPushButton(self.pinkPage)
        self.pinkBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.pinkBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pinkBtn.setFont(font)
        self.pinkBtn.setStyleSheet("background-color: #E91E63;\n"
"border-style: solid;\n"
"color:#ffffff;")
        self.pinkBtn.setObjectName("pinkBtn")
        self.pink500Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pink500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.pink500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pink500Btn.setFont(font)
        self.pink500Btn.setStyleSheet("background-color: #E91E63;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.pink500Btn.setObjectName("pink500Btn")
        self.pink600Btn = QtWidgets.QPushButton(self.pinkPage)
        self.pink600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.pink600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pink600Btn.setFont(font)
        self.pink600Btn.setStyleSheet("background-color: #D81B60;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.pink600Btn.setObjectName("pink600Btn")
        self.stackedWidget.addWidget(self.pinkPage)
        self.purplePage = QtWidgets.QWidget()
        self.purplePage.setObjectName("purplePage")
        self.purple800Btn = QtWidgets.QPushButton(self.purplePage)
        self.purple800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.purple800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purple800Btn.setFont(font)
        self.purple800Btn.setStyleSheet("background-color: #6A1B9A;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.purple800Btn.setObjectName("purple800Btn")
        self.purple50Btn = QtWidgets.QPushButton(self.purplePage)
        self.purple50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.purple50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.purple50Btn.setFont(font)
        self.purple50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.purple50Btn.setStyleSheet("background-color: #F3E5F5;\n"
"border-style: solid;\n"
"Text-align:right")
        self.purple50Btn.setObjectName("purple50Btn")
        self.purple600Btn = QtWidgets.QPushButton(self.purplePage)
        self.purple600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.purple600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purple600Btn.setFont(font)
        self.purple600Btn.setStyleSheet("background-color: #8E24AA;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.purple600Btn.setObjectName("purple600Btn")
        self.purpleA400Btn = QtWidgets.QPushButton(self.purplePage)
        self.purpleA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.purpleA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purpleA400Btn.setFont(font)
        self.purpleA400Btn.setStyleSheet("background-color: #D500F9;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.purpleA400Btn.setObjectName("purpleA400Btn")
        self.purple400Btn = QtWidgets.QPushButton(self.purplePage)
        self.purple400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.purple400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purple400Btn.setFont(font)
        self.purple400Btn.setStyleSheet("background-color: #AB47BC;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.purple400Btn.setObjectName("purple400Btn")
        self.purple500Btn = QtWidgets.QPushButton(self.purplePage)
        self.purple500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.purple500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purple500Btn.setFont(font)
        self.purple500Btn.setStyleSheet("background-color: #9C27B0;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.purple500Btn.setObjectName("purple500Btn")
        self.purpleBtn = QtWidgets.QPushButton(self.purplePage)
        self.purpleBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.purpleBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.purpleBtn.setFont(font)
        self.purpleBtn.setStyleSheet("background-color: #9C27B0;\n"
"border-style: solid;\n"
"color:#ffffff;")
        self.purpleBtn.setObjectName("purpleBtn")
        self.purple100Btn = QtWidgets.QPushButton(self.purplePage)
        self.purple100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.purple100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purple100Btn.setFont(font)
        self.purple100Btn.setStyleSheet("background-color: #E1BEE7;\n"
"border-style: solid;\n"
"Text-align:right")
        self.purple100Btn.setObjectName("purple100Btn")
        self.purple300Btn = QtWidgets.QPushButton(self.purplePage)
        self.purple300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.purple300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purple300Btn.setFont(font)
        self.purple300Btn.setStyleSheet("background-color: #BA68C8;\n"
"border-style: solid;\n"
"Text-align:right")
        self.purple300Btn.setObjectName("purple300Btn")
        self.purple700Btn = QtWidgets.QPushButton(self.purplePage)
        self.purple700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.purple700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purple700Btn.setFont(font)
        self.purple700Btn.setStyleSheet("background-color: #7B1FA2;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.purple700Btn.setObjectName("purple700Btn")
        self.purpleA200Btn = QtWidgets.QPushButton(self.purplePage)
        self.purpleA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.purpleA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purpleA200Btn.setFont(font)
        self.purpleA200Btn.setStyleSheet("background-color: #E040FB;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.purpleA200Btn.setObjectName("purpleA200Btn")
        self.purple200Btn = QtWidgets.QPushButton(self.purplePage)
        self.purple200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.purple200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purple200Btn.setFont(font)
        self.purple200Btn.setStyleSheet("background-color: #CE93D8;\n"
"border-style: solid;\n"
"Text-align:right")
        self.purple200Btn.setObjectName("purple200Btn")
        self.purple900Btn = QtWidgets.QPushButton(self.purplePage)
        self.purple900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.purple900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purple900Btn.setFont(font)
        self.purple900Btn.setStyleSheet("background-color: #4A148C;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.purple900Btn.setObjectName("purple900Btn")
        self.purpleA100Btn = QtWidgets.QPushButton(self.purplePage)
        self.purpleA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.purpleA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purpleA100Btn.setFont(font)
        self.purpleA100Btn.setStyleSheet("background-color: #EA80FC;\n"
"border-style: solid;\n"
"Text-align:right")
        self.purpleA100Btn.setObjectName("purpleA100Btn")
        self.purpleA700Btn = QtWidgets.QPushButton(self.purplePage)
        self.purpleA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.purpleA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.purpleA700Btn.setFont(font)
        self.purpleA700Btn.setStyleSheet("background-color: #AA00FF;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.purpleA700Btn.setObjectName("purpleA700Btn")
        self.stackedWidget.addWidget(self.purplePage)
        self.deepPurplePage = QtWidgets.QWidget()
        self.deepPurplePage.setObjectName("deepPurplePage")
        self.deepPurpleA400Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurpleA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.deepPurpleA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurpleA400Btn.setFont(font)
        self.deepPurpleA400Btn.setStyleSheet("background-color: #651FFF;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepPurpleA400Btn.setObjectName("deepPurpleA400Btn")
        self.deepPurple900Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurple900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.deepPurple900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurple900Btn.setFont(font)
        self.deepPurple900Btn.setStyleSheet("background-color: #311B92;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepPurple900Btn.setObjectName("deepPurple900Btn")
        self.deepPurple50Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurple50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.deepPurple50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.deepPurple50Btn.setFont(font)
        self.deepPurple50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deepPurple50Btn.setStyleSheet("background-color: #EDE7F6;\n"
"border-style: solid;\n"
"Text-align:right")
        self.deepPurple50Btn.setObjectName("deepPurple50Btn")
        self.deepPurple800Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurple800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.deepPurple800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurple800Btn.setFont(font)
        self.deepPurple800Btn.setStyleSheet("background-color: #4527A0;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepPurple800Btn.setObjectName("deepPurple800Btn")
        self.deepPurple300Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurple300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.deepPurple300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurple300Btn.setFont(font)
        self.deepPurple300Btn.setStyleSheet("background-color: #9575CD;\n"
"border-style: solid;\n"
"Text-align:right")
        self.deepPurple300Btn.setObjectName("deepPurple300Btn")
        self.deepPurpleBtn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurpleBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.deepPurpleBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.deepPurpleBtn.setFont(font)
        self.deepPurpleBtn.setStyleSheet("background-color: #673AB7;\n"
"border-style: solid;\n"
"color:#ffffff;")
        self.deepPurpleBtn.setObjectName("deepPurpleBtn")
        self.deepPurpleA100Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurpleA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.deepPurpleA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurpleA100Btn.setFont(font)
        self.deepPurpleA100Btn.setStyleSheet("background-color: #B388FF;\n"
"border-style: solid;\n"
"Text-align:right")
        self.deepPurpleA100Btn.setObjectName("deepPurpleA100Btn")
        self.deepPurpleA700Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurpleA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.deepPurpleA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurpleA700Btn.setFont(font)
        self.deepPurpleA700Btn.setStyleSheet("background-color: #6200EA;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepPurpleA700Btn.setObjectName("deepPurpleA700Btn")
        self.deepPurple700Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurple700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.deepPurple700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurple700Btn.setFont(font)
        self.deepPurple700Btn.setStyleSheet("background-color: #512DA8;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepPurple700Btn.setObjectName("deepPurple700Btn")
        self.deepPurple500Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurple500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.deepPurple500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurple500Btn.setFont(font)
        self.deepPurple500Btn.setStyleSheet("background-color: #673AB7;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepPurple500Btn.setObjectName("deepPurple500Btn")
        self.deepPurple600Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurple600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.deepPurple600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurple600Btn.setFont(font)
        self.deepPurple600Btn.setStyleSheet("background-color: #5E35B1;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepPurple600Btn.setObjectName("deepPurple600Btn")
        self.deepPurple100Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurple100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.deepPurple100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurple100Btn.setFont(font)
        self.deepPurple100Btn.setStyleSheet("background-color: #D1C4E9;\n"
"border-style: solid;\n"
"Text-align:right")
        self.deepPurple100Btn.setObjectName("deepPurple100Btn")
        self.deepPurple200Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurple200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.deepPurple200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurple200Btn.setFont(font)
        self.deepPurple200Btn.setStyleSheet("background-color: #B39DDB;\n"
"border-style: solid;\n"
"Text-align:right")
        self.deepPurple200Btn.setObjectName("deepPurple200Btn")
        self.deepPurple400Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurple400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.deepPurple400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurple400Btn.setFont(font)
        self.deepPurple400Btn.setStyleSheet("background-color: #7E57C2;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepPurple400Btn.setObjectName("deepPurple400Btn")
        self.deepPurpleA200Btn = QtWidgets.QPushButton(self.deepPurplePage)
        self.deepPurpleA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.deepPurpleA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepPurpleA200Btn.setFont(font)
        self.deepPurpleA200Btn.setStyleSheet("background-color: #7C4DFF;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepPurpleA200Btn.setObjectName("deepPurpleA200Btn")
        self.stackedWidget.addWidget(self.deepPurplePage)
        self.indigoPage = QtWidgets.QWidget()
        self.indigoPage.setObjectName("indigoPage")
        self.indigo800Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigo800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.indigo800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigo800Btn.setFont(font)
        self.indigo800Btn.setStyleSheet("background-color: #283593;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.indigo800Btn.setObjectName("indigo800Btn")
        self.indigoA400Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigoA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.indigoA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigoA400Btn.setFont(font)
        self.indigoA400Btn.setStyleSheet("background-color: #3D5AFE;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.indigoA400Btn.setObjectName("indigoA400Btn")
        self.indigo500Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigo500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.indigo500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigo500Btn.setFont(font)
        self.indigo500Btn.setStyleSheet("background-color: #3F51B5;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.indigo500Btn.setObjectName("indigo500Btn")
        self.indigoA700Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigoA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.indigoA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigoA700Btn.setFont(font)
        self.indigoA700Btn.setStyleSheet("background-color: #304FFE;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.indigoA700Btn.setObjectName("indigoA700Btn")
        self.indigo700Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigo700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.indigo700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigo700Btn.setFont(font)
        self.indigo700Btn.setStyleSheet("background-color: #303F9F;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.indigo700Btn.setObjectName("indigo700Btn")
        self.indigo900Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigo900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.indigo900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigo900Btn.setFont(font)
        self.indigo900Btn.setStyleSheet("background-color: #1A237E;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.indigo900Btn.setObjectName("indigo900Btn")
        self.indigo600Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigo600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.indigo600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigo600Btn.setFont(font)
        self.indigo600Btn.setStyleSheet("background-color: #3949AB;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.indigo600Btn.setObjectName("indigo600Btn")
        self.indigoA200Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigoA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.indigoA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigoA200Btn.setFont(font)
        self.indigoA200Btn.setStyleSheet("background-color: #536DFE;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.indigoA200Btn.setObjectName("indigoA200Btn")
        self.indigoA100Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigoA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.indigoA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigoA100Btn.setFont(font)
        self.indigoA100Btn.setStyleSheet("background-color: #8C9EFF;\n"
"border-style: solid;\n"
"Text-align:right")
        self.indigoA100Btn.setObjectName("indigoA100Btn")
        self.indigo300Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigo300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.indigo300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigo300Btn.setFont(font)
        self.indigo300Btn.setStyleSheet("background-color: #7986CB;\n"
"border-style: solid;\n"
"Text-align:right")
        self.indigo300Btn.setObjectName("indigo300Btn")
        self.indigo400Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigo400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.indigo400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigo400Btn.setFont(font)
        self.indigo400Btn.setStyleSheet("background-color: #5C6BC0;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.indigo400Btn.setObjectName("indigo400Btn")
        self.indigo50Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigo50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.indigo50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.indigo50Btn.setFont(font)
        self.indigo50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.indigo50Btn.setStyleSheet("background-color: #E8EAF6;\n"
"border-style: solid;\n"
"Text-align:right")
        self.indigo50Btn.setObjectName("indigo50Btn")
        self.indigoBtn = QtWidgets.QPushButton(self.indigoPage)
        self.indigoBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.indigoBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.indigoBtn.setFont(font)
        self.indigoBtn.setStyleSheet("background-color: #3F51B5;\n"
"border-style: solid;\n"
"color:#ffffff;")
        self.indigoBtn.setObjectName("indigoBtn")
        self.indigo100Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigo100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.indigo100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigo100Btn.setFont(font)
        self.indigo100Btn.setStyleSheet("background-color: #C5CAE9;\n"
"border-style: solid;\n"
"Text-align:right")
        self.indigo100Btn.setObjectName("indigo100Btn")
        self.indigo200Btn = QtWidgets.QPushButton(self.indigoPage)
        self.indigo200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.indigo200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.indigo200Btn.setFont(font)
        self.indigo200Btn.setStyleSheet("background-color: #9FA8DA;\n"
"border-style: solid;\n"
"Text-align:right")
        self.indigo200Btn.setObjectName("indigo200Btn")
        self.stackedWidget.addWidget(self.indigoPage)
        self.bluePage = QtWidgets.QWidget()
        self.bluePage.setObjectName("bluePage")
        self.blue400Btn = QtWidgets.QPushButton(self.bluePage)
        self.blue400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.blue400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blue400Btn.setFont(font)
        self.blue400Btn.setStyleSheet("background-color: #42A5F5;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.blue400Btn.setObjectName("blue400Btn")
        self.blueA100Btn = QtWidgets.QPushButton(self.bluePage)
        self.blueA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.blueA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueA100Btn.setFont(font)
        self.blueA100Btn.setStyleSheet("background-color: #82B1FF;\n"
"border-style: solid;\n"
"Text-align:right")
        self.blueA100Btn.setObjectName("blueA100Btn")
        self.blue100Btn = QtWidgets.QPushButton(self.bluePage)
        self.blue100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.blue100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blue100Btn.setFont(font)
        self.blue100Btn.setStyleSheet("background-color: #BBDEFB;\n"
"border-style: solid;\n"
"Text-align:right")
        self.blue100Btn.setObjectName("blue100Btn")
        self.blue200Btn = QtWidgets.QPushButton(self.bluePage)
        self.blue200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.blue200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blue200Btn.setFont(font)
        self.blue200Btn.setStyleSheet("background-color: #90CAF9;\n"
"border-style: solid;\n"
"Text-align:right")
        self.blue200Btn.setObjectName("blue200Btn")
        self.blueA700Btn = QtWidgets.QPushButton(self.bluePage)
        self.blueA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.blueA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueA700Btn.setFont(font)
        self.blueA700Btn.setStyleSheet("background-color: #2962FF;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blueA700Btn.setObjectName("blueA700Btn")
        self.blue500Btn = QtWidgets.QPushButton(self.bluePage)
        self.blue500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.blue500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blue500Btn.setFont(font)
        self.blue500Btn.setStyleSheet("background-color: #2196F3;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.blue500Btn.setObjectName("blue500Btn")
        self.blue700Btn = QtWidgets.QPushButton(self.bluePage)
        self.blue700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.blue700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blue700Btn.setFont(font)
        self.blue700Btn.setStyleSheet("background-color: #1976D2;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blue700Btn.setObjectName("blue700Btn")
        self.blue300Btn = QtWidgets.QPushButton(self.bluePage)
        self.blue300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.blue300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blue300Btn.setFont(font)
        self.blue300Btn.setStyleSheet("background-color: #64B5F6;\n"
"border-style: solid;\n"
"Text-align:right")
        self.blue300Btn.setObjectName("blue300Btn")
        self.blue600Btn = QtWidgets.QPushButton(self.bluePage)
        self.blue600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.blue600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blue600Btn.setFont(font)
        self.blue600Btn.setStyleSheet("background-color: #1E88E5;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blue600Btn.setObjectName("blue600Btn")
        self.blue50Btn = QtWidgets.QPushButton(self.bluePage)
        self.blue50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.blue50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.blue50Btn.setFont(font)
        self.blue50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blue50Btn.setStyleSheet("background-color: #E3F2FD;\n"
"border-style: solid;\n"
"Text-align:right")
        self.blue50Btn.setObjectName("blue50Btn")
        self.blueA200Btn = QtWidgets.QPushButton(self.bluePage)
        self.blueA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.blueA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueA200Btn.setFont(font)
        self.blueA200Btn.setStyleSheet("background-color: #448AFF;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blueA200Btn.setObjectName("blueA200Btn")
        self.blueA400Btn = QtWidgets.QPushButton(self.bluePage)
        self.blueA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.blueA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueA400Btn.setFont(font)
        self.blueA400Btn.setStyleSheet("background-color: #2979FF;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blueA400Btn.setObjectName("blueA400Btn")
        self.blue900Btn = QtWidgets.QPushButton(self.bluePage)
        self.blue900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.blue900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blue900Btn.setFont(font)
        self.blue900Btn.setStyleSheet("background-color: #0D47A1;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blue900Btn.setObjectName("blue900Btn")
        self.blue800Btn = QtWidgets.QPushButton(self.bluePage)
        self.blue800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.blue800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blue800Btn.setFont(font)
        self.blue800Btn.setStyleSheet("background-color: #1565C0;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blue800Btn.setObjectName("blue800Btn")
        self.blueBtn = QtWidgets.QPushButton(self.bluePage)
        self.blueBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.blueBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.blueBtn.setFont(font)
        self.blueBtn.setStyleSheet("background-color: #2196F3;\n"
"border-style: solid;\n"
"")
        self.blueBtn.setObjectName("blueBtn")
        self.stackedWidget.addWidget(self.bluePage)
        self.lightBluePage = QtWidgets.QWidget()
        self.lightBluePage.setObjectName("lightBluePage")
        self.lightBlueA700Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlueA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.lightBlueA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlueA700Btn.setFont(font)
        self.lightBlueA700Btn.setStyleSheet("background-color: #0091EA;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.lightBlueA700Btn.setObjectName("lightBlueA700Btn")
        self.lightBlue50Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlue50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.lightBlue50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.lightBlue50Btn.setFont(font)
        self.lightBlue50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lightBlue50Btn.setStyleSheet("background-color: #E1F5FE;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lightBlue50Btn.setObjectName("lightBlue50Btn")
        self.lightBlue200Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlue200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.lightBlue200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlue200Btn.setFont(font)
        self.lightBlue200Btn.setStyleSheet("background-color: #81D4FA;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lightBlue200Btn.setObjectName("lightBlue200Btn")
        self.lightBlue800Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlue800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.lightBlue800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlue800Btn.setFont(font)
        self.lightBlue800Btn.setStyleSheet("background-color: #0277BD;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.lightBlue800Btn.setObjectName("lightBlue800Btn")
        self.lightBlue100Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlue100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.lightBlue100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlue100Btn.setFont(font)
        self.lightBlue100Btn.setStyleSheet("background-color: #B3E5FC;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lightBlue100Btn.setObjectName("lightBlue100Btn")
        self.lightBlueBtn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlueBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.lightBlueBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lightBlueBtn.setFont(font)
        self.lightBlueBtn.setStyleSheet("background-color: #03A9F4;\n"
"border-style: solid;")
        self.lightBlueBtn.setObjectName("lightBlueBtn")
        self.lightBlueA100Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlueA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.lightBlueA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlueA100Btn.setFont(font)
        self.lightBlueA100Btn.setStyleSheet("background-color: #80D8FF;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lightBlueA100Btn.setObjectName("lightBlueA100Btn")
        self.lightBlue700Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlue700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.lightBlue700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlue700Btn.setFont(font)
        self.lightBlue700Btn.setStyleSheet("background-color: #0288D1;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.lightBlue700Btn.setObjectName("lightBlue700Btn")
        self.lightBlue300Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlue300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.lightBlue300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlue300Btn.setFont(font)
        self.lightBlue300Btn.setStyleSheet("background-color: #4FC3F7;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lightBlue300Btn.setObjectName("lightBlue300Btn")
        self.lightBlue500Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlue500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.lightBlue500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlue500Btn.setFont(font)
        self.lightBlue500Btn.setStyleSheet("background-color: #03A9F4;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightBlue500Btn.setObjectName("lightBlue500Btn")
        self.lightBlueA400Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlueA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.lightBlueA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlueA400Btn.setFont(font)
        self.lightBlueA400Btn.setStyleSheet("background-color: #00B0FF;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightBlueA400Btn.setObjectName("lightBlueA400Btn")
        self.lightBlue400Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlue400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.lightBlue400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlue400Btn.setFont(font)
        self.lightBlue400Btn.setStyleSheet("background-color: #29B6F6;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightBlue400Btn.setObjectName("lightBlue400Btn")
        self.lightBlue900Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlue900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.lightBlue900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlue900Btn.setFont(font)
        self.lightBlue900Btn.setStyleSheet("background-color: #01579B;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.lightBlue900Btn.setObjectName("lightBlue900Btn")
        self.lightBlue600Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlue600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.lightBlue600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlue600Btn.setFont(font)
        self.lightBlue600Btn.setStyleSheet("background-color: #039BE5;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightBlue600Btn.setObjectName("lightBlue600Btn")
        self.lightBlueA200Btn = QtWidgets.QPushButton(self.lightBluePage)
        self.lightBlueA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.lightBlueA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightBlueA200Btn.setFont(font)
        self.lightBlueA200Btn.setStyleSheet("background-color: #40C4FF;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightBlueA200Btn.setObjectName("lightBlueA200Btn")
        self.stackedWidget.addWidget(self.lightBluePage)
        self.cyanPage = QtWidgets.QWidget()
        self.cyanPage.setObjectName("cyanPage")
        self.cyanBtn = QtWidgets.QPushButton(self.cyanPage)
        self.cyanBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.cyanBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cyanBtn.setFont(font)
        self.cyanBtn.setStyleSheet("background-color: #00BCD4;\n"
"border-style: solid;")
        self.cyanBtn.setObjectName("cyanBtn")
        self.cyanA400Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyanA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.cyanA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyanA400Btn.setFont(font)
        self.cyanA400Btn.setStyleSheet("background-color: #00E5FF;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.cyanA400Btn.setObjectName("cyanA400Btn")
        self.cyan800Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyan800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.cyan800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyan800Btn.setFont(font)
        self.cyan800Btn.setStyleSheet("background-color: #00838F;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.cyan800Btn.setObjectName("cyan800Btn")
        self.cyan300Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyan300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.cyan300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyan300Btn.setFont(font)
        self.cyan300Btn.setStyleSheet("background-color: #4DD0E1;\n"
"border-style: solid;\n"
"Text-align:right")
        self.cyan300Btn.setObjectName("cyan300Btn")
        self.cyan700Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyan700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.cyan700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyan700Btn.setFont(font)
        self.cyan700Btn.setStyleSheet("background-color: #0097A7;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.cyan700Btn.setObjectName("cyan700Btn")
        self.cyan400Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyan400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.cyan400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyan400Btn.setFont(font)
        self.cyan400Btn.setStyleSheet("background-color: #26C6DA;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.cyan400Btn.setObjectName("cyan400Btn")
        self.cyan900Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyan900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.cyan900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyan900Btn.setFont(font)
        self.cyan900Btn.setStyleSheet("background-color: #006064;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.cyan900Btn.setObjectName("cyan900Btn")
        self.cyan200Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyan200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.cyan200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyan200Btn.setFont(font)
        self.cyan200Btn.setStyleSheet("background-color: #80DEEA;\n"
"border-style: solid;\n"
"Text-align:right")
        self.cyan200Btn.setObjectName("cyan200Btn")
        self.cyanA200Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyanA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.cyanA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyanA200Btn.setFont(font)
        self.cyanA200Btn.setStyleSheet("background-color: #18FFFF;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.cyanA200Btn.setObjectName("cyanA200Btn")
        self.cyan50Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyan50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.cyan50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.cyan50Btn.setFont(font)
        self.cyan50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cyan50Btn.setStyleSheet("background-color: #E0F7FA;\n"
"border-style: solid;\n"
"Text-align:right")
        self.cyan50Btn.setObjectName("cyan50Btn")
        self.cyan500Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyan500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.cyan500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyan500Btn.setFont(font)
        self.cyan500Btn.setStyleSheet("background-color: #00BCD4;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.cyan500Btn.setObjectName("cyan500Btn")
        self.cyanA700Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyanA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.cyanA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyanA700Btn.setFont(font)
        self.cyanA700Btn.setStyleSheet("background-color: #00B8D4;\n"
"border-style: solid;\n"
"Text-align:right")
        self.cyanA700Btn.setObjectName("cyanA700Btn")
        self.cyan600Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyan600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.cyan600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyan600Btn.setFont(font)
        self.cyan600Btn.setStyleSheet("background-color: #00ACC1;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.cyan600Btn.setObjectName("cyan600Btn")
        self.cyan100Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyan100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.cyan100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyan100Btn.setFont(font)
        self.cyan100Btn.setStyleSheet("background-color: #B2EBF2;\n"
"border-style: solid;\n"
"Text-align:right")
        self.cyan100Btn.setObjectName("cyan100Btn")
        self.cyanA100Btn = QtWidgets.QPushButton(self.cyanPage)
        self.cyanA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.cyanA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cyanA100Btn.setFont(font)
        self.cyanA100Btn.setStyleSheet("background-color: #84FFFF;\n"
"border-style: solid;\n"
"Text-align:right")
        self.cyanA100Btn.setObjectName("cyanA100Btn")
        self.stackedWidget.addWidget(self.cyanPage)
        self.tealPage = QtWidgets.QWidget()
        self.tealPage.setObjectName("tealPage")
        self.tealBtn = QtWidgets.QPushButton(self.tealPage)
        self.tealBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.tealBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tealBtn.setFont(font)
        self.tealBtn.setStyleSheet("background-color: #009688;\n"
"border-style: solid;\n"
"color:#ffffff")
        self.tealBtn.setObjectName("tealBtn")
        self.tealA400Btn = QtWidgets.QPushButton(self.tealPage)
        self.tealA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.tealA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tealA400Btn.setFont(font)
        self.tealA400Btn.setStyleSheet("background-color: #1DE9B6;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.tealA400Btn.setObjectName("tealA400Btn")
        self.teal800Btn = QtWidgets.QPushButton(self.tealPage)
        self.teal800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.teal800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teal800Btn.setFont(font)
        self.teal800Btn.setStyleSheet("background-color: #00695C;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.teal800Btn.setObjectName("teal800Btn")
        self.teal300Btn = QtWidgets.QPushButton(self.tealPage)
        self.teal300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.teal300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teal300Btn.setFont(font)
        self.teal300Btn.setStyleSheet("background-color: #4DB6AC;\n"
"border-style: solid;\n"
"Text-align:right")
        self.teal300Btn.setObjectName("teal300Btn")
        self.teal700Btn = QtWidgets.QPushButton(self.tealPage)
        self.teal700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.teal700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teal700Btn.setFont(font)
        self.teal700Btn.setStyleSheet("background-color: #00796B;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.teal700Btn.setObjectName("teal700Btn")
        self.teal400Btn = QtWidgets.QPushButton(self.tealPage)
        self.teal400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.teal400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teal400Btn.setFont(font)
        self.teal400Btn.setStyleSheet("background-color: #26A69A;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.teal400Btn.setObjectName("teal400Btn")
        self.teal900Btn = QtWidgets.QPushButton(self.tealPage)
        self.teal900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.teal900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teal900Btn.setFont(font)
        self.teal900Btn.setStyleSheet("background-color: #004D40;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.teal900Btn.setObjectName("teal900Btn")
        self.teal200Btn = QtWidgets.QPushButton(self.tealPage)
        self.teal200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.teal200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teal200Btn.setFont(font)
        self.teal200Btn.setStyleSheet("background-color: #80CBC4;\n"
"border-style: solid;\n"
"Text-align:right")
        self.teal200Btn.setObjectName("teal200Btn")
        self.tealA200Btn = QtWidgets.QPushButton(self.tealPage)
        self.tealA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.tealA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tealA200Btn.setFont(font)
        self.tealA200Btn.setStyleSheet("background-color: #64FFDA;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.tealA200Btn.setObjectName("tealA200Btn")
        self.teal50Btn = QtWidgets.QPushButton(self.tealPage)
        self.teal50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.teal50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.teal50Btn.setFont(font)
        self.teal50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.teal50Btn.setStyleSheet("background-color: #E0F2F1;\n"
"border-style: solid;\n"
"Text-align:right")
        self.teal50Btn.setObjectName("teal50Btn")
        self.teal500Btn = QtWidgets.QPushButton(self.tealPage)
        self.teal500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.teal500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teal500Btn.setFont(font)
        self.teal500Btn.setStyleSheet("background-color: #009688;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff")
        self.teal500Btn.setObjectName("teal500Btn")
        self.tealA700Btn = QtWidgets.QPushButton(self.tealPage)
        self.tealA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.tealA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tealA700Btn.setFont(font)
        self.tealA700Btn.setStyleSheet("background-color: #00BFA5;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.tealA700Btn.setObjectName("tealA700Btn")
        self.teal600Btn = QtWidgets.QPushButton(self.tealPage)
        self.teal600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.teal600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teal600Btn.setFont(font)
        self.teal600Btn.setStyleSheet("background-color: #00897B;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff")
        self.teal600Btn.setObjectName("teal600Btn")
        self.teal100Btn = QtWidgets.QPushButton(self.tealPage)
        self.teal100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.teal100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teal100Btn.setFont(font)
        self.teal100Btn.setStyleSheet("background-color: #B2DFDB;\n"
"border-style: solid;\n"
"Text-align:right")
        self.teal100Btn.setObjectName("teal100Btn")
        self.tealA100Btn = QtWidgets.QPushButton(self.tealPage)
        self.tealA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.tealA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tealA100Btn.setFont(font)
        self.tealA100Btn.setStyleSheet("background-color: #A7FFEB;\n"
"border-style: solid;\n"
"Text-align:right")
        self.tealA100Btn.setObjectName("tealA100Btn")
        self.stackedWidget.addWidget(self.tealPage)
        self.greenPage = QtWidgets.QWidget()
        self.greenPage.setObjectName("greenPage")
        self.greenBtn = QtWidgets.QPushButton(self.greenPage)
        self.greenBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.greenBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.greenBtn.setFont(font)
        self.greenBtn.setStyleSheet("background-color: #4CAF50;\n"
"border-style: solid;")
        self.greenBtn.setObjectName("greenBtn")
        self.greenA400Btn = QtWidgets.QPushButton(self.greenPage)
        self.greenA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.greenA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.greenA400Btn.setFont(font)
        self.greenA400Btn.setStyleSheet("background-color: #00E676;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.greenA400Btn.setObjectName("greenA400Btn")
        self.green800Btn = QtWidgets.QPushButton(self.greenPage)
        self.green800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.green800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.green800Btn.setFont(font)
        self.green800Btn.setStyleSheet("background-color: #2E7D32;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.green800Btn.setObjectName("green800Btn")
        self.green300Btn = QtWidgets.QPushButton(self.greenPage)
        self.green300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.green300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.green300Btn.setFont(font)
        self.green300Btn.setStyleSheet("background-color: #81C784;\n"
"border-style: solid;\n"
"Text-align:right")
        self.green300Btn.setObjectName("green300Btn")
        self.green700Btn = QtWidgets.QPushButton(self.greenPage)
        self.green700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.green700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.green700Btn.setFont(font)
        self.green700Btn.setStyleSheet("background-color: #388E3C;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.green700Btn.setObjectName("green700Btn")
        self.green400Btn = QtWidgets.QPushButton(self.greenPage)
        self.green400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.green400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.green400Btn.setFont(font)
        self.green400Btn.setStyleSheet("background-color: #66BB6A;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.green400Btn.setObjectName("green400Btn")
        self.green900Btn = QtWidgets.QPushButton(self.greenPage)
        self.green900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.green900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.green900Btn.setFont(font)
        self.green900Btn.setStyleSheet("background-color: #1B5E20;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.green900Btn.setObjectName("green900Btn")
        self.green200Btn = QtWidgets.QPushButton(self.greenPage)
        self.green200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.green200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.green200Btn.setFont(font)
        self.green200Btn.setStyleSheet("background-color: #A5D6A7;\n"
"border-style: solid;\n"
"Text-align:right")
        self.green200Btn.setObjectName("green200Btn")
        self.greenA200Btn = QtWidgets.QPushButton(self.greenPage)
        self.greenA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.greenA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.greenA200Btn.setFont(font)
        self.greenA200Btn.setStyleSheet("background-color: #69F0AE;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.greenA200Btn.setObjectName("greenA200Btn")
        self.green50Btn = QtWidgets.QPushButton(self.greenPage)
        self.green50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.green50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.green50Btn.setFont(font)
        self.green50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.green50Btn.setStyleSheet("background-color: #E8F5E9;\n"
"border-style: solid;\n"
"Text-align:right")
        self.green50Btn.setObjectName("green50Btn")
        self.green500Btn = QtWidgets.QPushButton(self.greenPage)
        self.green500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.green500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.green500Btn.setFont(font)
        self.green500Btn.setStyleSheet("background-color: #4CAF50;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.green500Btn.setObjectName("green500Btn")
        self.greenA700Btn = QtWidgets.QPushButton(self.greenPage)
        self.greenA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.greenA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.greenA700Btn.setFont(font)
        self.greenA700Btn.setStyleSheet("background-color: #00C853;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.greenA700Btn.setObjectName("greenA700Btn")
        self.green600Btn = QtWidgets.QPushButton(self.greenPage)
        self.green600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.green600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.green600Btn.setFont(font)
        self.green600Btn.setStyleSheet("background-color:#43A047;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.green600Btn.setObjectName("green600Btn")
        self.green100Btn = QtWidgets.QPushButton(self.greenPage)
        self.green100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.green100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.green100Btn.setFont(font)
        self.green100Btn.setStyleSheet("background-color: #C8E6C9;\n"
"border-style: solid;\n"
"Text-align:right")
        self.green100Btn.setObjectName("green100Btn")
        self.greenA100Btn = QtWidgets.QPushButton(self.greenPage)
        self.greenA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.greenA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.greenA100Btn.setFont(font)
        self.greenA100Btn.setStyleSheet("background-color: #B9F6CA;\n"
"border-style: solid;\n"
"Text-align:right")
        self.greenA100Btn.setObjectName("greenA100Btn")
        self.stackedWidget.addWidget(self.greenPage)
        self.lightGreenPage = QtWidgets.QWidget()
        self.lightGreenPage.setObjectName("lightGreenPage")
        self.lightGreenBtn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreenBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.lightGreenBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lightGreenBtn.setFont(font)
        self.lightGreenBtn.setStyleSheet("background-color: #8BC34A;\n"
"border-style: solid;")
        self.lightGreenBtn.setObjectName("lightGreenBtn")
        self.lightGreenA400Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreenA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.lightGreenA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreenA400Btn.setFont(font)
        self.lightGreenA400Btn.setStyleSheet("background-color: #76FF03;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightGreenA400Btn.setObjectName("lightGreenA400Btn")
        self.lightGreen800Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreen800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.lightGreen800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreen800Btn.setFont(font)
        self.lightGreen800Btn.setStyleSheet("background-color: #558B2F;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.lightGreen800Btn.setObjectName("lightGreen800Btn")
        self.lightGreen300Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreen300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.lightGreen300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreen300Btn.setFont(font)
        self.lightGreen300Btn.setStyleSheet("background-color: #AED581;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lightGreen300Btn.setObjectName("lightGreen300Btn")
        self.lightGreen700Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreen700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.lightGreen700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreen700Btn.setFont(font)
        self.lightGreen700Btn.setStyleSheet("background-color: #689F38;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightGreen700Btn.setObjectName("lightGreen700Btn")
        self.lightGreen400Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreen400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.lightGreen400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreen400Btn.setFont(font)
        self.lightGreen400Btn.setStyleSheet("background-color: #9CCC65;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightGreen400Btn.setObjectName("lightGreen400Btn")
        self.lightGreen900Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreen900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.lightGreen900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreen900Btn.setFont(font)
        self.lightGreen900Btn.setStyleSheet("background-color: #33691E;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.lightGreen900Btn.setObjectName("lightGreen900Btn")
        self.lightGreen200Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreen200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.lightGreen200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreen200Btn.setFont(font)
        self.lightGreen200Btn.setStyleSheet("background-color: #C5E1A5;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lightGreen200Btn.setObjectName("lightGreen200Btn")
        self.lightGreenA200Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreenA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.lightGreenA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreenA200Btn.setFont(font)
        self.lightGreenA200Btn.setStyleSheet("background-color: #B2FF59;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightGreenA200Btn.setObjectName("lightGreenA200Btn")
        self.lightGreen50Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreen50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.lightGreen50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.lightGreen50Btn.setFont(font)
        self.lightGreen50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lightGreen50Btn.setStyleSheet("background-color: #F1F8E9;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lightGreen50Btn.setObjectName("lightGreen50Btn")
        self.lightGreen500Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreen500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.lightGreen500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreen500Btn.setFont(font)
        self.lightGreen500Btn.setStyleSheet("background-color: #8BC34A;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightGreen500Btn.setObjectName("lightGreen500Btn")
        self.lightGreenA700Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreenA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.lightGreenA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreenA700Btn.setFont(font)
        self.lightGreenA700Btn.setStyleSheet("background-color: #64DD17;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightGreenA700Btn.setObjectName("lightGreenA700Btn")
        self.lightGreen600Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreen600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.lightGreen600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreen600Btn.setFont(font)
        self.lightGreen600Btn.setStyleSheet("background-color: #7CB342;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lightGreen600Btn.setObjectName("lightGreen600Btn")
        self.lightGreen100Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreen100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.lightGreen100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreen100Btn.setFont(font)
        self.lightGreen100Btn.setStyleSheet("background-color: #DCEDC8;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lightGreen100Btn.setObjectName("lightGreen100Btn")
        self.lightGreenA100Btn = QtWidgets.QPushButton(self.lightGreenPage)
        self.lightGreenA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.lightGreenA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lightGreenA100Btn.setFont(font)
        self.lightGreenA100Btn.setStyleSheet("background-color: #CCFF90;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lightGreenA100Btn.setObjectName("lightGreenA100Btn")
        self.stackedWidget.addWidget(self.lightGreenPage)
        self.limePage = QtWidgets.QWidget()
        self.limePage.setObjectName("limePage")
        self.limeBtn = QtWidgets.QPushButton(self.limePage)
        self.limeBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.limeBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.limeBtn.setFont(font)
        self.limeBtn.setStyleSheet("background-color: #CDDC39;\n"
"border-style: solid;")
        self.limeBtn.setObjectName("limeBtn")
        self.limeA400Btn = QtWidgets.QPushButton(self.limePage)
        self.limeA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.limeA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.limeA400Btn.setFont(font)
        self.limeA400Btn.setStyleSheet("background-color: #C6FF00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.limeA400Btn.setObjectName("limeA400Btn")
        self.lime800Btn = QtWidgets.QPushButton(self.limePage)
        self.lime800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.lime800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lime800Btn.setFont(font)
        self.lime800Btn.setStyleSheet("background-color: #9E9D24;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lime800Btn.setObjectName("lime800Btn")
        self.lime300Btn = QtWidgets.QPushButton(self.limePage)
        self.lime300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.lime300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lime300Btn.setFont(font)
        self.lime300Btn.setStyleSheet("background-color: #DCE775;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lime300Btn.setObjectName("lime300Btn")
        self.lime700Btn = QtWidgets.QPushButton(self.limePage)
        self.lime700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.lime700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lime700Btn.setFont(font)
        self.lime700Btn.setStyleSheet("background-color: #AFB42B;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lime700Btn.setObjectName("lime700Btn")
        self.lime400Btn = QtWidgets.QPushButton(self.limePage)
        self.lime400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.lime400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lime400Btn.setFont(font)
        self.lime400Btn.setStyleSheet("background-color: #D4E157;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lime400Btn.setObjectName("lime400Btn")
        self.lime900Btn = QtWidgets.QPushButton(self.limePage)
        self.lime900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.lime900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lime900Btn.setFont(font)
        self.lime900Btn.setStyleSheet("background-color: #827717;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.lime900Btn.setObjectName("lime900Btn")
        self.lime200Btn = QtWidgets.QPushButton(self.limePage)
        self.lime200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.lime200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lime200Btn.setFont(font)
        self.lime200Btn.setStyleSheet("background-color: #E6EE9C;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lime200Btn.setObjectName("lime200Btn")
        self.limeA200Btn = QtWidgets.QPushButton(self.limePage)
        self.limeA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.limeA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.limeA200Btn.setFont(font)
        self.limeA200Btn.setStyleSheet("background-color: #EEFF41;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.limeA200Btn.setObjectName("limeA200Btn")
        self.lime50Btn = QtWidgets.QPushButton(self.limePage)
        self.lime50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.lime50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.lime50Btn.setFont(font)
        self.lime50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lime50Btn.setStyleSheet("background-color: #F9FBE7;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lime50Btn.setObjectName("lime50Btn")
        self.lime500Btn = QtWidgets.QPushButton(self.limePage)
        self.lime500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.lime500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lime500Btn.setFont(font)
        self.lime500Btn.setStyleSheet("background-color: #CDDC39;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lime500Btn.setObjectName("lime500Btn")
        self.limeA700Btn = QtWidgets.QPushButton(self.limePage)
        self.limeA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.limeA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.limeA700Btn.setFont(font)
        self.limeA700Btn.setStyleSheet("background-color: #AEEA00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.limeA700Btn.setObjectName("limeA700Btn")
        self.lime600Btn = QtWidgets.QPushButton(self.limePage)
        self.lime600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.lime600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lime600Btn.setFont(font)
        self.lime600Btn.setStyleSheet("background-color: #C0CA33;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.lime600Btn.setObjectName("lime600Btn")
        self.lime100Btn = QtWidgets.QPushButton(self.limePage)
        self.lime100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.lime100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lime100Btn.setFont(font)
        self.lime100Btn.setStyleSheet("background-color: #F0F4C3;\n"
"border-style: solid;\n"
"Text-align:right")
        self.lime100Btn.setObjectName("lime100Btn")
        self.limeA100Btn = QtWidgets.QPushButton(self.limePage)
        self.limeA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.limeA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.limeA100Btn.setFont(font)
        self.limeA100Btn.setStyleSheet("background-color: #F4FF81;\n"
"border-style: solid;\n"
"Text-align:right")
        self.limeA100Btn.setObjectName("limeA100Btn")
        self.stackedWidget.addWidget(self.limePage)
        self.yellowPage = QtWidgets.QWidget()
        self.yellowPage.setObjectName("yellowPage")
        self.yellowBtn = QtWidgets.QPushButton(self.yellowPage)
        self.yellowBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.yellowBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yellowBtn.setFont(font)
        self.yellowBtn.setStyleSheet("background-color: #FFEB3B;\n"
"border-style: solid;")
        self.yellowBtn.setObjectName("yellowBtn")
        self.yellowA400Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellowA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.yellowA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellowA400Btn.setFont(font)
        self.yellowA400Btn.setStyleSheet("background-color: #FFEA00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.yellowA400Btn.setObjectName("yellowA400Btn")
        self.yellow800Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellow800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.yellow800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellow800Btn.setFont(font)
        self.yellow800Btn.setStyleSheet("background-color: #F9A825;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.yellow800Btn.setObjectName("yellow800Btn")
        self.yellow300Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellow300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.yellow300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellow300Btn.setFont(font)
        self.yellow300Btn.setStyleSheet("background-color: #FFF176;\n"
"border-style: solid;\n"
"Text-align:right")
        self.yellow300Btn.setObjectName("yellow300Btn")
        self.yellow700Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellow700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.yellow700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellow700Btn.setFont(font)
        self.yellow700Btn.setStyleSheet("background-color: #FBC02D;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.yellow700Btn.setObjectName("yellow700Btn")
        self.yellow400Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellow400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.yellow400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellow400Btn.setFont(font)
        self.yellow400Btn.setStyleSheet("background-color: #FFEE58;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.yellow400Btn.setObjectName("yellow400Btn")
        self.yellow900Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellow900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.yellow900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellow900Btn.setFont(font)
        self.yellow900Btn.setStyleSheet("background-color: #F57F17;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.yellow900Btn.setObjectName("yellow900Btn")
        self.yellow200Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellow200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.yellow200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellow200Btn.setFont(font)
        self.yellow200Btn.setStyleSheet("background-color: #FFF59D;\n"
"border-style: solid;\n"
"Text-align:right")
        self.yellow200Btn.setObjectName("yellow200Btn")
        self.yellowA200Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellowA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.yellowA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellowA200Btn.setFont(font)
        self.yellowA200Btn.setStyleSheet("background-color: #FFFF00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.yellowA200Btn.setObjectName("yellowA200Btn")
        self.yellow50Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellow50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.yellow50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.yellow50Btn.setFont(font)
        self.yellow50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.yellow50Btn.setStyleSheet("background-color: #FFFDE7;\n"
"border-style: solid;\n"
"Text-align:right")
        self.yellow50Btn.setObjectName("yellow50Btn")
        self.yellow500Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellow500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.yellow500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellow500Btn.setFont(font)
        self.yellow500Btn.setStyleSheet("background-color: #FFEB3B;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.yellow500Btn.setObjectName("yellow500Btn")
        self.yellowA700Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellowA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.yellowA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellowA700Btn.setFont(font)
        self.yellowA700Btn.setStyleSheet("background-color: #FFD600;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.yellowA700Btn.setObjectName("yellowA700Btn")
        self.yellow600Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellow600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.yellow600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellow600Btn.setFont(font)
        self.yellow600Btn.setStyleSheet("background-color: #FDD835;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.yellow600Btn.setObjectName("yellow600Btn")
        self.yellow100Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellow100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.yellow100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellow100Btn.setFont(font)
        self.yellow100Btn.setStyleSheet("background-color: #FFF9C4;\n"
"border-style: solid;\n"
"Text-align:right")
        self.yellow100Btn.setObjectName("yellow100Btn")
        self.yellowA100Btn = QtWidgets.QPushButton(self.yellowPage)
        self.yellowA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.yellowA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yellowA100Btn.setFont(font)
        self.yellowA100Btn.setStyleSheet("background-color: #FFFF8D;\n"
"border-style: solid;\n"
"Text-align:right")
        self.yellowA100Btn.setObjectName("yellowA100Btn")
        self.stackedWidget.addWidget(self.yellowPage)
        self.amberPage = QtWidgets.QWidget()
        self.amberPage.setObjectName("amberPage")
        self.amberBtn = QtWidgets.QPushButton(self.amberPage)
        self.amberBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.amberBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.amberBtn.setFont(font)
        self.amberBtn.setStyleSheet("background-color: #FFC107;\n"
"border-style: solid;")
        self.amberBtn.setObjectName("amberBtn")
        self.amberA400Btn = QtWidgets.QPushButton(self.amberPage)
        self.amberA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.amberA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amberA400Btn.setFont(font)
        self.amberA400Btn.setStyleSheet("background-color: #FFC400;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.amberA400Btn.setObjectName("amberA400Btn")
        self.amber800Btn = QtWidgets.QPushButton(self.amberPage)
        self.amber800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.amber800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amber800Btn.setFont(font)
        self.amber800Btn.setStyleSheet("background-color: #FF8F00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.amber800Btn.setObjectName("amber800Btn")
        self.amber300Btn = QtWidgets.QPushButton(self.amberPage)
        self.amber300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.amber300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amber300Btn.setFont(font)
        self.amber300Btn.setStyleSheet("background-color: #FFD54F;\n"
"border-style: solid;\n"
"Text-align:right")
        self.amber300Btn.setObjectName("amber300Btn")
        self.amber700Btn = QtWidgets.QPushButton(self.amberPage)
        self.amber700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.amber700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amber700Btn.setFont(font)
        self.amber700Btn.setStyleSheet("background-color: #FFA000;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.amber700Btn.setObjectName("amber700Btn")
        self.amber400Btn = QtWidgets.QPushButton(self.amberPage)
        self.amber400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.amber400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amber400Btn.setFont(font)
        self.amber400Btn.setStyleSheet("background-color: #FFCA28;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.amber400Btn.setObjectName("amber400Btn")
        self.amber900Btn = QtWidgets.QPushButton(self.amberPage)
        self.amber900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.amber900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amber900Btn.setFont(font)
        self.amber900Btn.setStyleSheet("background-color: #FF6F00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.amber900Btn.setObjectName("amber900Btn")
        self.amber200Btn = QtWidgets.QPushButton(self.amberPage)
        self.amber200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.amber200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amber200Btn.setFont(font)
        self.amber200Btn.setStyleSheet("background-color: #FFE082;\n"
"border-style: solid;\n"
"Text-align:right")
        self.amber200Btn.setObjectName("amber200Btn")
        self.amberA200Btn = QtWidgets.QPushButton(self.amberPage)
        self.amberA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.amberA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amberA200Btn.setFont(font)
        self.amberA200Btn.setStyleSheet("background-color: #FFD740;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.amberA200Btn.setObjectName("amberA200Btn")
        self.amber50Btn = QtWidgets.QPushButton(self.amberPage)
        self.amber50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.amber50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.amber50Btn.setFont(font)
        self.amber50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.amber50Btn.setStyleSheet("background-color: #FFF8E1;\n"
"border-style: solid;\n"
"Text-align:right")
        self.amber50Btn.setObjectName("amber50Btn")
        self.amber500Btn = QtWidgets.QPushButton(self.amberPage)
        self.amber500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.amber500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amber500Btn.setFont(font)
        self.amber500Btn.setStyleSheet("background-color: #FFC107;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.amber500Btn.setObjectName("amber500Btn")
        self.amberA700Btn = QtWidgets.QPushButton(self.amberPage)
        self.amberA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.amberA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amberA700Btn.setFont(font)
        self.amberA700Btn.setStyleSheet("background-color: #FFAB00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.amberA700Btn.setObjectName("amberA700Btn")
        self.amber600Btn = QtWidgets.QPushButton(self.amberPage)
        self.amber600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.amber600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amber600Btn.setFont(font)
        self.amber600Btn.setStyleSheet("background-color: #FFB300;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.amber600Btn.setObjectName("amber600Btn")
        self.amber100Btn = QtWidgets.QPushButton(self.amberPage)
        self.amber100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.amber100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amber100Btn.setFont(font)
        self.amber100Btn.setStyleSheet("background-color: #FFECB3;\n"
"border-style: solid;\n"
"Text-align:right")
        self.amber100Btn.setObjectName("amber100Btn")
        self.amberA100Btn = QtWidgets.QPushButton(self.amberPage)
        self.amberA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.amberA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amberA100Btn.setFont(font)
        self.amberA100Btn.setStyleSheet("background-color: #FFE57F;\n"
"border-style: solid;\n"
"Text-align:right")
        self.amberA100Btn.setObjectName("amberA100Btn")
        self.stackedWidget.addWidget(self.amberPage)
        self.orangePage = QtWidgets.QWidget()
        self.orangePage.setObjectName("orangePage")
        self.orangeBtn = QtWidgets.QPushButton(self.orangePage)
        self.orangeBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.orangeBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.orangeBtn.setFont(font)
        self.orangeBtn.setStyleSheet("background-color: #FF9800;\n"
"border-style: solid;")
        self.orangeBtn.setObjectName("orangeBtn")
        self.orangeA400Btn = QtWidgets.QPushButton(self.orangePage)
        self.orangeA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.orangeA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orangeA400Btn.setFont(font)
        self.orangeA400Btn.setStyleSheet("background-color: #FF9100;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.orangeA400Btn.setObjectName("orangeA400Btn")
        self.orange800Btn = QtWidgets.QPushButton(self.orangePage)
        self.orange800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.orange800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orange800Btn.setFont(font)
        self.orange800Btn.setStyleSheet("background-color: #EF6C00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.orange800Btn.setObjectName("orange800Btn")
        self.orange300Btn = QtWidgets.QPushButton(self.orangePage)
        self.orange300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.orange300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orange300Btn.setFont(font)
        self.orange300Btn.setStyleSheet("background-color: #FFB74D;\n"
"border-style: solid;\n"
"Text-align:right")
        self.orange300Btn.setObjectName("orange300Btn")
        self.orange700Btn = QtWidgets.QPushButton(self.orangePage)
        self.orange700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.orange700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orange700Btn.setFont(font)
        self.orange700Btn.setStyleSheet("background-color: #F57C00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.orange700Btn.setObjectName("orange700Btn")
        self.orange400Btn = QtWidgets.QPushButton(self.orangePage)
        self.orange400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.orange400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orange400Btn.setFont(font)
        self.orange400Btn.setStyleSheet("background-color: #FFA726;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.orange400Btn.setObjectName("orange400Btn")
        self.orange900Btn = QtWidgets.QPushButton(self.orangePage)
        self.orange900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.orange900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orange900Btn.setFont(font)
        self.orange900Btn.setStyleSheet("background-color: #E65100;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.orange900Btn.setObjectName("orange900Btn")
        self.orange200Btn = QtWidgets.QPushButton(self.orangePage)
        self.orange200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.orange200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orange200Btn.setFont(font)
        self.orange200Btn.setStyleSheet("background-color: #FFCC80;\n"
"border-style: solid;\n"
"Text-align:right")
        self.orange200Btn.setObjectName("orange200Btn")
        self.orangeA200Btn = QtWidgets.QPushButton(self.orangePage)
        self.orangeA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.orangeA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orangeA200Btn.setFont(font)
        self.orangeA200Btn.setStyleSheet("background-color: #FFAB40;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.orangeA200Btn.setObjectName("orangeA200Btn")
        self.orange50Btn = QtWidgets.QPushButton(self.orangePage)
        self.orange50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.orange50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.orange50Btn.setFont(font)
        self.orange50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.orange50Btn.setStyleSheet("background-color: #FFF3E0;\n"
"border-style: solid;\n"
"Text-align:right")
        self.orange50Btn.setObjectName("orange50Btn")
        self.orange500Btn = QtWidgets.QPushButton(self.orangePage)
        self.orange500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.orange500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orange500Btn.setFont(font)
        self.orange500Btn.setStyleSheet("background-color: #FF9800;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.orange500Btn.setObjectName("orange500Btn")
        self.orangeA700Btn = QtWidgets.QPushButton(self.orangePage)
        self.orangeA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.orangeA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orangeA700Btn.setFont(font)
        self.orangeA700Btn.setStyleSheet("background-color: #FF6D00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.orangeA700Btn.setObjectName("orangeA700Btn")
        self.orange600Btn = QtWidgets.QPushButton(self.orangePage)
        self.orange600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.orange600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orange600Btn.setFont(font)
        self.orange600Btn.setStyleSheet("background-color: #FB8C00;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.orange600Btn.setObjectName("orange600Btn")
        self.orange100Btn = QtWidgets.QPushButton(self.orangePage)
        self.orange100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.orange100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orange100Btn.setFont(font)
        self.orange100Btn.setStyleSheet("background-color: #FFE0B2;\n"
"border-style: solid;\n"
"Text-align:right")
        self.orange100Btn.setObjectName("orange100Btn")
        self.orangeA100Btn = QtWidgets.QPushButton(self.orangePage)
        self.orangeA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.orangeA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.orangeA100Btn.setFont(font)
        self.orangeA100Btn.setStyleSheet("background-color: #FFD180;\n"
"border-style: solid;\n"
"Text-align:right")
        self.orangeA100Btn.setObjectName("orangeA100Btn")
        self.stackedWidget.addWidget(self.orangePage)
        self.deepOrangePage = QtWidgets.QWidget()
        self.deepOrangePage.setObjectName("deepOrangePage")
        self.deepOrangeBtn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrangeBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.deepOrangeBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.deepOrangeBtn.setFont(font)
        self.deepOrangeBtn.setStyleSheet("background-color: #FF5722;\n"
"border-style: solid;")
        self.deepOrangeBtn.setObjectName("deepOrangeBtn")
        self.deepOrangeA400Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrangeA400Btn.setGeometry(QtCore.QRect(0, 700, 202, 50))
        self.deepOrangeA400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrangeA400Btn.setFont(font)
        self.deepOrangeA400Btn.setStyleSheet("background-color: #FF3D00;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepOrangeA400Btn.setObjectName("deepOrangeA400Btn")
        self.deepOrange800Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrange800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.deepOrange800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrange800Btn.setFont(font)
        self.deepOrange800Btn.setStyleSheet("background-color: #D84315;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepOrange800Btn.setObjectName("deepOrange800Btn")
        self.deepOrange300Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrange300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.deepOrange300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrange300Btn.setFont(font)
        self.deepOrange300Btn.setStyleSheet("background-color: #FF8A65;\n"
"border-style: solid;\n"
"Text-align:right")
        self.deepOrange300Btn.setObjectName("deepOrange300Btn")
        self.deepOrange700Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrange700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.deepOrange700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrange700Btn.setFont(font)
        self.deepOrange700Btn.setStyleSheet("background-color: #E64A19;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepOrange700Btn.setObjectName("deepOrange700Btn")
        self.deepOrange400Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrange400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.deepOrange400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrange400Btn.setFont(font)
        self.deepOrange400Btn.setStyleSheet("background-color: #FF7043;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.deepOrange400Btn.setObjectName("deepOrange400Btn")
        self.deepOrange900Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrange900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.deepOrange900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrange900Btn.setFont(font)
        self.deepOrange900Btn.setStyleSheet("background-color: #BF360C;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepOrange900Btn.setObjectName("deepOrange900Btn")
        self.deepOrange200Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrange200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.deepOrange200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrange200Btn.setFont(font)
        self.deepOrange200Btn.setStyleSheet("background-color: #FFAB91;\n"
"border-style: solid;\n"
"Text-align:right")
        self.deepOrange200Btn.setObjectName("deepOrange200Btn")
        self.deepOrangeA200Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrangeA200Btn.setGeometry(QtCore.QRect(0, 650, 202, 50))
        self.deepOrangeA200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrangeA200Btn.setFont(font)
        self.deepOrangeA200Btn.setStyleSheet("background-color: #FF6E40;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.deepOrangeA200Btn.setObjectName("deepOrangeA200Btn")
        self.deepOrange50Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrange50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.deepOrange50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.deepOrange50Btn.setFont(font)
        self.deepOrange50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deepOrange50Btn.setStyleSheet("background-color: #FBE9E7;\n"
"border-style: solid;\n"
"Text-align:right")
        self.deepOrange50Btn.setObjectName("deepOrange50Btn")
        self.deepOrange500Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrange500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.deepOrange500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrange500Btn.setFont(font)
        self.deepOrange500Btn.setStyleSheet("background-color: #FF5722;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.deepOrange500Btn.setObjectName("deepOrange500Btn")
        self.deepOrangeA700Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrangeA700Btn.setGeometry(QtCore.QRect(0, 750, 202, 50))
        self.deepOrangeA700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrangeA700Btn.setFont(font)
        self.deepOrangeA700Btn.setStyleSheet("background-color: #DD2C00;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepOrangeA700Btn.setObjectName("deepOrangeA700Btn")
        self.deepOrange600Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrange600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.deepOrange600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrange600Btn.setFont(font)
        self.deepOrange600Btn.setStyleSheet("background-color: #F4511E;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.deepOrange600Btn.setObjectName("deepOrange600Btn")
        self.deepOrange100Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrange100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.deepOrange100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrange100Btn.setFont(font)
        self.deepOrange100Btn.setStyleSheet("background-color: #FFCCBC;\n"
"border-style: solid;\n"
"Text-align:right")
        self.deepOrange100Btn.setObjectName("deepOrange100Btn")
        self.deepOrangeA100Btn = QtWidgets.QPushButton(self.deepOrangePage)
        self.deepOrangeA100Btn.setGeometry(QtCore.QRect(0, 600, 202, 50))
        self.deepOrangeA100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deepOrangeA100Btn.setFont(font)
        self.deepOrangeA100Btn.setStyleSheet("background-color: #FF9E80;\n"
"border-style: solid;\n"
"Text-align:right")
        self.deepOrangeA100Btn.setObjectName("deepOrangeA100Btn")
        self.stackedWidget.addWidget(self.deepOrangePage)
        self.brownPage = QtWidgets.QWidget()
        self.brownPage.setObjectName("brownPage")
        self.brownBtn = QtWidgets.QPushButton(self.brownPage)
        self.brownBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.brownBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.brownBtn.setFont(font)
        self.brownBtn.setStyleSheet("background-color: #795548;\n"
"border-style: solid;;\n"
"color:#ffffff;")
        self.brownBtn.setObjectName("brownBtn")
        self.brown800Btn = QtWidgets.QPushButton(self.brownPage)
        self.brown800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.brown800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.brown800Btn.setFont(font)
        self.brown800Btn.setStyleSheet("background-color: #4E342E;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.brown800Btn.setObjectName("brown800Btn")
        self.brown300Btn = QtWidgets.QPushButton(self.brownPage)
        self.brown300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.brown300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.brown300Btn.setFont(font)
        self.brown300Btn.setStyleSheet("background-color: #A1887F;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.brown300Btn.setObjectName("brown300Btn")
        self.brown700Btn = QtWidgets.QPushButton(self.brownPage)
        self.brown700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.brown700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.brown700Btn.setFont(font)
        self.brown700Btn.setStyleSheet("background-color: #5D4037;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.brown700Btn.setObjectName("brown700Btn")
        self.brown400Btn = QtWidgets.QPushButton(self.brownPage)
        self.brown400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.brown400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.brown400Btn.setFont(font)
        self.brown400Btn.setStyleSheet("background-color: #8D6E63;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.brown400Btn.setObjectName("brown400Btn")
        self.brown900Btn = QtWidgets.QPushButton(self.brownPage)
        self.brown900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.brown900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.brown900Btn.setFont(font)
        self.brown900Btn.setStyleSheet("background-color: #3E2723;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.brown900Btn.setObjectName("brown900Btn")
        self.brown200Btn = QtWidgets.QPushButton(self.brownPage)
        self.brown200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.brown200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.brown200Btn.setFont(font)
        self.brown200Btn.setStyleSheet("background-color: #BCAAA4;\n"
"border-style: solid;\n"
"Text-align:right")
        self.brown200Btn.setObjectName("brown200Btn")
        self.brown50Btn = QtWidgets.QPushButton(self.brownPage)
        self.brown50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.brown50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.brown50Btn.setFont(font)
        self.brown50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.brown50Btn.setStyleSheet("background-color: #EFEBE9;\n"
"border-style: solid;\n"
"Text-align:right")
        self.brown50Btn.setObjectName("brown50Btn")
        self.brown500Btn = QtWidgets.QPushButton(self.brownPage)
        self.brown500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.brown500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.brown500Btn.setFont(font)
        self.brown500Btn.setStyleSheet("background-color: #795548;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.brown500Btn.setObjectName("brown500Btn")
        self.brown600Btn = QtWidgets.QPushButton(self.brownPage)
        self.brown600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.brown600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.brown600Btn.setFont(font)
        self.brown600Btn.setStyleSheet("background-color: #6D4C41;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.brown600Btn.setObjectName("brown600Btn")
        self.brown100Btn = QtWidgets.QPushButton(self.brownPage)
        self.brown100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.brown100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.brown100Btn.setFont(font)
        self.brown100Btn.setStyleSheet("background-color: #D7CCC8;\n"
"border-style: solid;\n"
"Text-align:right")
        self.brown100Btn.setObjectName("brown100Btn")
        self.stackedWidget.addWidget(self.brownPage)
        self.greyPage = QtWidgets.QWidget()
        self.greyPage.setObjectName("greyPage")
        self.grey700Btn = QtWidgets.QPushButton(self.greyPage)
        self.grey700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.grey700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.grey700Btn.setFont(font)
        self.grey700Btn.setStyleSheet("background-color: #616161;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.grey700Btn.setObjectName("grey700Btn")
        self.grey200Btn = QtWidgets.QPushButton(self.greyPage)
        self.grey200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.grey200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.grey200Btn.setFont(font)
        self.grey200Btn.setStyleSheet("background-color: #EEEEEE;\n"
"border-style: solid;\n"
"Text-align:right")
        self.grey200Btn.setObjectName("grey200Btn")
        self.grey500Btn = QtWidgets.QPushButton(self.greyPage)
        self.grey500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.grey500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.grey500Btn.setFont(font)
        self.grey500Btn.setStyleSheet("background-color: #9E9E9E;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.grey500Btn.setObjectName("grey500Btn")
        self.grey900Btn = QtWidgets.QPushButton(self.greyPage)
        self.grey900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.grey900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.grey900Btn.setFont(font)
        self.grey900Btn.setStyleSheet("background-color: #212121;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.grey900Btn.setObjectName("grey900Btn")
        self.greyBtn = QtWidgets.QPushButton(self.greyPage)
        self.greyBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.greyBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.greyBtn.setFont(font)
        self.greyBtn.setStyleSheet("background-color: #9E9E9E;\n"
"border-style: solid;")
        self.greyBtn.setObjectName("greyBtn")
        self.grey400Btn = QtWidgets.QPushButton(self.greyPage)
        self.grey400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.grey400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.grey400Btn.setFont(font)
        self.grey400Btn.setStyleSheet("background-color: #BDBDBD;\n"
"border-style: solid;\n"
"Text-align:right;")
        self.grey400Btn.setObjectName("grey400Btn")
        self.grey100Btn = QtWidgets.QPushButton(self.greyPage)
        self.grey100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.grey100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.grey100Btn.setFont(font)
        self.grey100Btn.setStyleSheet("background-color: #F5F5F5;\n"
"border-style: solid;\n"
"Text-align:right")
        self.grey100Btn.setObjectName("grey100Btn")
        self.grey300Btn = QtWidgets.QPushButton(self.greyPage)
        self.grey300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.grey300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.grey300Btn.setFont(font)
        self.grey300Btn.setStyleSheet("background-color: #E0E0E0;\n"
"border-style: solid;\n"
"Text-align:right")
        self.grey300Btn.setObjectName("grey300Btn")
        self.grey800Btn = QtWidgets.QPushButton(self.greyPage)
        self.grey800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.grey800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.grey800Btn.setFont(font)
        self.grey800Btn.setStyleSheet("background-color: #424242;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.grey800Btn.setObjectName("grey800Btn")
        self.grey600Btn = QtWidgets.QPushButton(self.greyPage)
        self.grey600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.grey600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.grey600Btn.setFont(font)
        self.grey600Btn.setStyleSheet("background-color: #757575;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.grey600Btn.setObjectName("grey600Btn")
        self.grey50Btn = QtWidgets.QPushButton(self.greyPage)
        self.grey50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.grey50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.grey50Btn.setFont(font)
        self.grey50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grey50Btn.setStyleSheet("background-color: #FAFAFA;\n"
"border-style: solid;\n"
"Text-align:right")
        self.grey50Btn.setObjectName("grey50Btn")
        self.stackedWidget.addWidget(self.greyPage)
        self.blueGreyPage = QtWidgets.QWidget()
        self.blueGreyPage.setObjectName("blueGreyPage")
        self.blueGrey700Btn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGrey700Btn.setGeometry(QtCore.QRect(0, 450, 202, 50))
        self.blueGrey700Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueGrey700Btn.setFont(font)
        self.blueGrey700Btn.setStyleSheet("background-color: #455A64;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blueGrey700Btn.setObjectName("blueGrey700Btn")
        self.blueGrey200Btn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGrey200Btn.setGeometry(QtCore.QRect(0, 200, 202, 50))
        self.blueGrey200Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueGrey200Btn.setFont(font)
        self.blueGrey200Btn.setStyleSheet("background-color: #B0BEC5;\n"
"border-style: solid;\n"
"Text-align:right")
        self.blueGrey200Btn.setObjectName("blueGrey200Btn")
        self.blueGrey500Btn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGrey500Btn.setGeometry(QtCore.QRect(0, 350, 202, 50))
        self.blueGrey500Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueGrey500Btn.setFont(font)
        self.blueGrey500Btn.setStyleSheet("background-color: #607D8B;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blueGrey500Btn.setObjectName("blueGrey500Btn")
        self.blueGrey900Btn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGrey900Btn.setGeometry(QtCore.QRect(0, 550, 202, 50))
        self.blueGrey900Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueGrey900Btn.setFont(font)
        self.blueGrey900Btn.setStyleSheet("background-color: #263238;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blueGrey900Btn.setObjectName("blueGrey900Btn")
        self.blueGreyBtn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGreyBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.blueGreyBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.blueGreyBtn.setFont(font)
        self.blueGreyBtn.setStyleSheet("background-color: #607D8B;\n"
"border-style: solid;\n"
"color:#ffffff;")
        self.blueGreyBtn.setObjectName("blueGreyBtn")
        self.blueGrey400Btn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGrey400Btn.setGeometry(QtCore.QRect(0, 300, 202, 50))
        self.blueGrey400Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueGrey400Btn.setFont(font)
        self.blueGrey400Btn.setStyleSheet("background-color: #78909C;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blueGrey400Btn.setObjectName("blueGrey400Btn")
        self.blueGrey100Btn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGrey100Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.blueGrey100Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueGrey100Btn.setFont(font)
        self.blueGrey100Btn.setStyleSheet("background-color: #CFD8DC;\n"
"border-style: solid;\n"
"Text-align:right")
        self.blueGrey100Btn.setObjectName("blueGrey100Btn")
        self.blueGrey300Btn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGrey300Btn.setGeometry(QtCore.QRect(0, 250, 202, 50))
        self.blueGrey300Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueGrey300Btn.setFont(font)
        self.blueGrey300Btn.setStyleSheet("background-color: #90A4AE;\n"
"border-style: solid;\n"
"Text-align:right")
        self.blueGrey300Btn.setObjectName("blueGrey300Btn")
        self.blueGrey800Btn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGrey800Btn.setGeometry(QtCore.QRect(0, 500, 202, 50))
        self.blueGrey800Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueGrey800Btn.setFont(font)
        self.blueGrey800Btn.setStyleSheet("background-color: #37474F;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blueGrey800Btn.setObjectName("blueGrey800Btn")
        self.blueGrey600Btn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGrey600Btn.setGeometry(QtCore.QRect(0, 400, 202, 50))
        self.blueGrey600Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blueGrey600Btn.setFont(font)
        self.blueGrey600Btn.setStyleSheet("background-color: #546E7A;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.blueGrey600Btn.setObjectName("blueGrey600Btn")
        self.blueGrey50Btn = QtWidgets.QPushButton(self.blueGreyPage)
        self.blueGrey50Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.blueGrey50Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.blueGrey50Btn.setFont(font)
        self.blueGrey50Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blueGrey50Btn.setStyleSheet("background-color: #ECEFF1;\n"
"border-style: solid;\n"
"Text-align:right")
        self.blueGrey50Btn.setObjectName("blueGrey50Btn")
        self.stackedWidget.addWidget(self.blueGreyPage)
        self.blackPage = QtWidgets.QWidget()
        self.blackPage.setObjectName("blackPage")
        self.black0Btn = QtWidgets.QPushButton(self.blackPage)
        self.black0Btn.setGeometry(QtCore.QRect(0, 150, 202, 50))
        self.black0Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.black0Btn.setFont(font)
        self.black0Btn.setStyleSheet("background-color: #000000;\n"
"border-style: solid;\n"
"Text-align:right;\n"
"color:#ffffff;")
        self.black0Btn.setObjectName("black0Btn")
        self.blackBtn = QtWidgets.QPushButton(self.blackPage)
        self.blackBtn.setGeometry(QtCore.QRect(0, 0, 202, 100))
        self.blackBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.blackBtn.setFont(font)
        self.blackBtn.setStyleSheet("background-color: #000000;\n"
"border-style: solid;\n"
"color:#ffffff;")
        self.blackBtn.setObjectName("blackBtn")
        self.black1Btn = QtWidgets.QPushButton(self.blackPage)
        self.black1Btn.setGeometry(QtCore.QRect(0, 100, 202, 50))
        self.black1Btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.black1Btn.setFont(font)
        self.black1Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.black1Btn.setStyleSheet("background-color: #FFFFFF;\n"
"border-style: solid;\n"
"Text-align:right")
        self.black1Btn.setObjectName("black1Btn")
        self.stackedWidget.addWidget(self.blackPage)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Material Colors", None, -1))
        self.redColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Red</span></p></body></html>", None, -1))
        self.pinkColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Pink</span></p></body></html>", None, -1))
        self.purpleColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Purple</span></p></body></html>", None, -1))
        self.deepPurpleColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Deep Purple</span></p></body></html>", None, -1))
        self.indigoColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Indigo</span></p></body></html>", None, -1))
        self.blueColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Blue</span></p></body></html>", None, -1))
        self.lightBlueColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Light Blue</span></p></body></html>", None, -1))
        self.cyanColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Cyan</span></p></body></html>", None, -1))
        self.tealColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Teal</span></p></body></html>", None, -1))
        self.greenColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Green</span></p></body></html>", None, -1))
        self.lightGreenColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Light Green</span></p></body></html>", None, -1))
        self.limeColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Lime</span></p></body></html>", None, -1))
        self.yellowColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Yellow</span></p></body></html>", None, -1))
        self.amberColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Amber</span></p></body></html>", None, -1))
        self.orangeColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Orange</span></p></body></html>", None, -1))
        self.deepOrangeColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Deep Orange</span></p></body></html>", None, -1))
        self.brownColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Brown</span></p></body></html>", None, -1))
        self.greyColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Grey</span></p></body></html>", None, -1))
        self.blueGreyColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Blue Grey</span></p></body></html>", None, -1))
        self.blackColorBtn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Black</span></p></body></html>", None, -1))
        self.redBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Red", None, -1))
        self.red50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.red100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.red200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.red300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.red400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.red500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.red600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.red700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.red800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.red900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.redA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.redA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.redA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.redA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.pink100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.pinkA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.pinkA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.pink50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.pinkA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.pink900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.pink400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.pink700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.pinkA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.pink200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.pink800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.pink300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.pinkBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Pink", None, -1))
        self.pink500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.pink600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.purple800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.purple50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.purple600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.purpleA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.purple400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.purple500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.purpleBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Purple", None, -1))
        self.purple100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.purple300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.purple700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.purpleA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.purple200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.purple900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.purpleA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.purpleA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.deepPurpleA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.deepPurple900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.deepPurple50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.deepPurple800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.deepPurple300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.deepPurpleBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Deep Purple", None, -1))
        self.deepPurpleA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.deepPurpleA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.deepPurple700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.deepPurple500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.deepPurple600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.deepPurple100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.deepPurple200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.deepPurple400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.deepPurpleA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.indigo800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.indigoA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.indigo500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.indigoA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.indigo700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.indigo900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.indigo600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.indigoA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.indigoA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.indigo300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.indigo400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.indigo50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.indigoBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Indigo", None, -1))
        self.indigo100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.indigo200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.blue400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.blueA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.blue100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.blue200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.blueA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.blue500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.blue700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.blue300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.blue600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.blue50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.blueA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.blueA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.blue900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.blue800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.blueBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Blue", None, -1))
        self.lightBlueA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.lightBlue50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.lightBlue200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.lightBlue800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.lightBlue100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.lightBlueBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Light Blue", None, -1))
        self.lightBlueA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.lightBlue700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.lightBlue300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.lightBlue500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.lightBlueA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.lightBlue400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.lightBlue900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.lightBlue600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.lightBlueA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.cyanBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Cyan", None, -1))
        self.cyanA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.cyan800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.cyan300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.cyan700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.cyan400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.cyan900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.cyan200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.cyanA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.cyan50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.cyan500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.cyanA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.cyan600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.cyan100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.cyanA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.tealBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Teal", None, -1))
        self.tealA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.teal800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.teal300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.teal700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.teal400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.teal900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.teal200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.tealA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.teal50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.teal500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.tealA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.teal600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.teal100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.tealA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.greenBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Green", None, -1))
        self.greenA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.green800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.green300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.green700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.green400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.green900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.green200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.greenA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.green50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.green500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.greenA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.green600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.green100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.greenA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.lightGreenBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Light Green", None, -1))
        self.lightGreenA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.lightGreen800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.lightGreen300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.lightGreen700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.lightGreen400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.lightGreen900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.lightGreen200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.lightGreenA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.lightGreen50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.lightGreen500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.lightGreenA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.lightGreen600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.lightGreen100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.lightGreenA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.limeBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Lime", None, -1))
        self.limeA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.lime800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.lime300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.lime700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.lime400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.lime900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.lime200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.limeA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.lime50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.lime500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.limeA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.lime600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.lime100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.limeA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.yellowBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Yellow", None, -1))
        self.yellowA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.yellow800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.yellow300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.yellow700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.yellow400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.yellow900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.yellow200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.yellowA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.yellow50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.yellow500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.yellowA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.yellow600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.yellow100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.yellowA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.amberBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Amber", None, -1))
        self.amberA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.amber800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.amber300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.amber700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.amber400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.amber900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.amber200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.amberA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.amber50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.amber500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.amberA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.amber600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.amber100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.amberA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.orangeBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Orange", None, -1))
        self.orangeA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.orange800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.orange300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.orange700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.orange400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.orange900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.orange200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.orangeA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.orange50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.orange500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.orangeA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.orange600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.orange100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.orangeA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.deepOrangeBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Deep Orange", None, -1))
        self.deepOrangeA400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A400  ", None, -1))
        self.deepOrange800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.deepOrange300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.deepOrange700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.deepOrange400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.deepOrange900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.deepOrange200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.deepOrangeA200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A200  ", None, -1))
        self.deepOrange50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.deepOrange500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.deepOrangeA700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A700  ", None, -1))
        self.deepOrange600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.deepOrange100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.deepOrangeA100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "A100  ", None, -1))
        self.brownBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Brown", None, -1))
        self.brown800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.brown300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.brown700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.brown400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.brown900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.brown200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.brown50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.brown500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.brown600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.brown100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.grey700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.grey200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.grey500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.grey900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.greyBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Grey", None, -1))
        self.grey400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.grey100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.grey300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.grey800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.grey600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.grey50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.blueGrey700Btn.setText(QtWidgets.QApplication.translate("MainWindow", "700  ", None, -1))
        self.blueGrey200Btn.setText(QtWidgets.QApplication.translate("MainWindow", "200  ", None, -1))
        self.blueGrey500Btn.setText(QtWidgets.QApplication.translate("MainWindow", "500  ", None, -1))
        self.blueGrey900Btn.setText(QtWidgets.QApplication.translate("MainWindow", "900  ", None, -1))
        self.blueGreyBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Blue Grey", None, -1))
        self.blueGrey400Btn.setText(QtWidgets.QApplication.translate("MainWindow", "400  ", None, -1))
        self.blueGrey100Btn.setText(QtWidgets.QApplication.translate("MainWindow", "100  ", None, -1))
        self.blueGrey300Btn.setText(QtWidgets.QApplication.translate("MainWindow", "300  ", None, -1))
        self.blueGrey800Btn.setText(QtWidgets.QApplication.translate("MainWindow", "800  ", None, -1))
        self.blueGrey600Btn.setText(QtWidgets.QApplication.translate("MainWindow", "600  ", None, -1))
        self.blueGrey50Btn.setText(QtWidgets.QApplication.translate("MainWindow", "50  ", None, -1))
        self.black0Btn.setText(QtWidgets.QApplication.translate("MainWindow", "0  ", None, -1))
        self.blackBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Black", None, -1))
        self.black1Btn.setText(QtWidgets.QApplication.translate("MainWindow", "1  ", None, -1))
        self.redColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(0))
        self.pinkColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(1))
        self.purpleColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(2))
        self.deepPurpleColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(3))
        self.indigoColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(4))
        self.blueColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(5))
        self.lightBlueColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(6))
        self.cyanColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(7))
        self.tealColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(8))
        self.greenColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(9))
        self.lightGreenColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(10))
        self.limeColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(11))
        self.yellowColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(12))
        self.amberColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(13))
        self.orangeColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(14))
        self.deepOrangeColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(15))
        self.brownColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(16))
        self.greyColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(17))
        self.blueGreyColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(18))
        self.blackColorBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(19))
        self.red50Btn.clicked.connect(self.getColorFn)

        buttonList = []

        for index in range(self.stackedWidget.count()):
            currentChildList = self.stackedWidget.widget(index).children()
            for i in currentChildList:
                if isinstance(i, QtWidgets.QPushButton):
                    buttonList.append(i)
        for j in buttonList:
            j.clicked.connect(self.getColorFn)
            #j.clicked.connect(lambda:self.getColorFn(buttonName=j))
            #j.clicked.connect(self.getColorFn(j.objectName()))

    def getColorFn(self):
        button = self.sender()
        if isinstance(button, QtWidgets.QPushButton):
            #print(button.palette().color(QtGui.QPalette.Background).name())
            clipBoarVar = QtWidgets.QApplication.clipboard()
            clipBoarVar.clear(mode=clipBoarVar.Clipboard)
            clipBoarVar.setText(str(button.palette().color(QtGui.QPalette.Background).name()), mode=clipBoarVar.Clipboard)
            #QtWidgets.QMessageBox.information(QtWidgets.QWidget(), "Clipboard", str(button.palette().color(QtGui.QPalette.Background).name())+'is now copied to your clipboard')


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    screenshot = materialColorsUI()
    screenshot.show()
sys.exit(app.exec_())