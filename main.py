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
    driver =Chrome_Config(Chrome_path) #In this function, you can config your chrome driver

    print('------------------------------------------------------------------------')
    #--------------------------------------------------------------------------------
    #parameters
    Keyword_Path = 'keyword.csv'
    Stop_num=10000 #this is the number of the items you want to crawl
    kw_start_point=0 #this parameter decides the start keyword of the crawler.its default value is 0
    save_path = 'data'#this is the path where you want to save the crawled data
    start_date= '2021-01-01' #this parameter decides the start date of the crawler.its default value is 2021-01-01
    end_date= '2020-01-01' #this parameter decides the end date of the crawler.its default value is 2020-01-01
    #----------------------------------------------------------------------------------
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    Twitter_Crawler(driver,Keyword_Path,Stop_num,kw_start_point,save_path,start_date,end_date)
    print('------------------------------------------------------------------------')
    driver.close()