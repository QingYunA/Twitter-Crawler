from functions import *
# from selenium.webdriver.chrome.options import Options  # => 引入Chrome的配置
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Gui_Crawler
import os


def Chrome_Config(Chrome_path):
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument("--headless")  # => 为Chrome配置无头模式
    # options.add_argument("--headless")
    s=Service(executable_path=Chrome_path)
    driver = webdriver.Chrome(service=s, options=options)
    return driver






if __name__ == '__main__':

    Chrome_path = "F:\Code//2022\chromedriver_win32\chromedriver.exe"  # Enter your chrome driver path here
    driver = Chrome_Config(Chrome_path)  # In this function, you can config your chrome driver
    print('------------------------------------------------------------------------')
    # --------------------------------------------------------------------------------
    # parameters
    Keyword_Path = 'keyword.csv'
    Stop_num = 10  # this is the number of the items you want to crawl
    kw_start_point = 0  # this parameter decides the start keyword of the crawler.its default value is 0
    save_path = 'data'  # this is the path where you want to save the crawled data
    start_date = '2022-05-09'  # this parameter decides the start date of the crawler.its default value is 2021-01-01
    end_date = '2020-01-01'  # this parameter decides the end date of the crawler.its default value is 2020-01-01
    limit_language = 'all'  # this parameter decides the language of the crawler.its default value is en
    # ----------------------------------------------------------------------------------
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Gui_Crawler.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda :Twitter_Crawler(driver, Keyword_Path, Stop_num, kw_start_point, save_path, start_date, end_date, limit_language))
    MainWindow.show()
    print('------------------------------------------------------------------------')
    driver.close()

    sys.exit(app.exec_())
    # Twitter_Crawler(driver, Keyword_Path, Stop_num, kw_start_point, save_path, start_date, end_date, limit_language)