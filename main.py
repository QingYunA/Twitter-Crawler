from functions import *
# from selenium.webdriver.chrome.options import Options  # => 引入Chrome的配置
from selenium.webdriver import ChromeOptions
from selenium import webdriver
import os

def Chrome_Config(Chrome_path):
    
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument("--headless")  # => 为Chrome配置无头模式
    # options.add_argument("--headless")


    driver = webdriver.Chrome(Chrome_path, options=options)
    return driver
if __name__ == '__main__':

    Chrome_path = "F:\Code//2022\chromedriver_win32\chromedriver.exe"  # Enter your chrome driver path here
    driver =Chrome_Config(Chrome_path) #into this function you can choose headless mode

    print('------------------------------------------------------------------------')
    Keyword_Path = 'keyword.csv'
    Stop_num=10000 #Collect Stop_num items information
    kw_start_point=0 #this parameter decides the start keyword of the crawler.its default value is 0
    save_path = 'data'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    Twitter_Crawler(driver,Keyword_Path,Stop_num=Stop_num)
    print('------------------------------------------------------------------------')
    driver.close()