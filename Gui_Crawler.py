# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Gui_Crawler.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 130, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.StarDate = QtWidgets.QDateEdit(self.centralwidget)
        self.StarDate.setGeometry(QtCore.QRect(100, 110, 110, 22))
        self.StarDate.setObjectName("StarDate")
        self.EndDate = QtWidgets.QDateEdit(self.centralwidget)
        self.EndDate.setGeometry(QtCore.QRect(100, 140, 110, 22))
        self.EndDate.setObjectName("EndDate")
        self.Num = QtWidgets.QLineEdit(self.centralwidget)
        self.Num.setGeometry(QtCore.QRect(100, 180, 113, 20))
        self.Num.setObjectName("Num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.pushButton.setText(_translate("MainWindow", "Start Crawler"))

