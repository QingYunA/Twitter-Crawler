# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Gui_Crawler.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functions import *
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(222, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 210, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.StarDate = QtWidgets.QDateEdit(self.centralwidget)
        self.StarDate.setGeometry(QtCore.QRect(80, 61, 110, 21))
        self.StarDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 5, 9), QtCore.QTime(0, 0, 0)))
        self.StarDate.setObjectName("StarDate")
        self.EndDate = QtWidgets.QDateEdit(self.centralwidget)
        self.EndDate.setGeometry(QtCore.QRect(80, 90, 110, 22))
        self.EndDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 5, 8), QtCore.QTime(0, 0, 0)))
        self.EndDate.setObjectName("EndDate")
        self.Search_num = QtWidgets.QLineEdit(self.centralwidget)
        self.Search_num.setGeometry(QtCore.QRect(70, 124, 113, 20))
        self.Search_num.setObjectName("Search_num")
        self.check_Date = QtWidgets.QCheckBox(self.centralwidget)
        self.check_Date.setGeometry(QtCore.QRect(20, 30, 101, 21))
        self.check_Date.setObjectName("check_Date")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 41, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 124, 51, 21))
        self.label_3.setObjectName("label_3")
        self.limit_language = QtWidgets.QCheckBox(self.centralwidget)
        self.limit_language.setGeometry(QtCore.QRect(20, 10, 111, 21))
        self.limit_language.setObjectName("limit_language")
        self.start_point = QtWidgets.QLineEdit(self.centralwidget)
        self.start_point.setGeometry(QtCore.QRect(70, 174, 113, 21))
        self.start_point.setObjectName("start_point")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 171, 21))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 10, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 222, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Twitter Crawler"))
        self.pushButton.setText(_translate("MainWindow", "Start Crawler"))
        self.check_Date.setText(_translate("MainWindow", "Limit Date"))
        self.label.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "End"))
        self.label_3.setText(_translate("MainWindow", "Max num"))
        self.limit_language.setText(_translate("MainWindow", "Limit Language"))
        self.label_4.setText(_translate("MainWindow", "Start from which kw"))
        self.comboBox.setItemText(0, _translate("MainWindow", "eu"))
        self.comboBox.setItemText(1, _translate("MainWindow", "zh"))



    def Chrome_Config(self, Chrome_path):
        options = ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        # options.add_argument("--headless")  # => 为Chrome配置无头模式
        # options.add_argument("--headless")
        s = Service(executable_path=Chrome_path)
        driver = webdriver.Chrome(service=s, options=options)
        return driver

    def Ui_Twitter_Crawler(self):
        # parameters
        Keyword_Path = 'keyword.csv'
        Stop_num = 10  # this is the number of the items you want to crawl
        kw_start_point = 0  # this parameter decides the start keyword of the crawler.its default value is 0
        save_path = 'data'  # this is the path where you want to save the crawled data
        start_date = '2022-05-09'  # this parameter decides the start date of the crawler.its default value is 2021-01-01
        end_date = '2020-01-01'  # this parameter decides the end date of the crawler.its default value is 2020-01-01
        # limit_language = 'all'  # this parameter decides the language of the crawler.its default value is en
        # ----------------------------------------------------------------------------------
        start_date = self.StarDate.text()
        end_date = self.EndDate.text()
        if os.path.exists(save_path) == False:
            os.mkdir(save_path)
        if (self.limit_language.isChecked()):
            limit_language = self.comboBox.currentText()
        else:
            limit_language = 'all'
        if self.start_point.text() != '':
            kw_start_point = int(self.start_point.text())
        if self.Search_num.text() != '':
            Stop_num = int(self.Search_num.text())
        # print(start_date, end_date, limit_language, kw_start_point, Stop_num)
        Chrome_path = r"F:\Code//2022\chromedriver_win32\chromedriver.exe"  # Enter your chrome driver path here
        driver = self.Chrome_Config(Chrome_path)  # In this function, you can config your chrome driver
        Twitter_Crawler(driver, Keyword_Path, Stop_num, kw_start_point, save_path, start_date, end_date, limit_language)
        driver.close()
