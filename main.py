from functions import *
# from selenium.webdriver.chrome.options import Options  # => 引入Chrome的配置
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Gui_Crawler
import os









if __name__ == '__main__':


    print('------------------------------------------------------------------------')
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Gui_Crawler.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda :ui.Ui_Twitter_Crawler())
    MainWindow.show()
    print('------------------------------------------------------------------------')
    sys.exit(app.exec_())
    # Twitter_Crawler(driver, Keyword_Path, Stop_num, kw_start_point, save_path, start_date, end_date, limit_language)