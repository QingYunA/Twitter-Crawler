import pandas as pd
import time
import datetime
from xml.etree.ElementTree import Comment
from hyperlink import URL
from numpy import common_type
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from selenium import webdriver
import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
from selenium.webdriver import ChromeOptions


def creatBroserDriver(path):
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--headless")  # => 为Chrome配置无头模式
    # options.add_argument("--headless")
    driver = webdriver.Chrome(path, options=options)
    return driver


# 从csv文件中读出某个元素
def readDf(path, elementName):
    df = pd.read_csv(path, encoding='UTF-8')
    return df[elementName]


def searchFunsNum(driver, userName):
    urlPath = 'https://twitter.com/search?q=%s&src=typed_query&f=user' % userName
    driver.get(urlPath)
    driver.implicitly_wait(10);
    try:
        nameElement = driver.find_element(by=By.XPATH,
                                          value="//*[contains(@class,'css-1dbjc4n r-12181gd r-1pi2tsx r-1ny4l3l r-o7ynqc r-6416eg r-13qz1uu')]")
        ActionChains(driver).move_to_element(nameElement).click().perform()
    except:
        return 'Cant find this user!'
    # driver.implicitly_wait(5);
    divs = []
    noResTimes = 0
    while (not divs):
        try:
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            divs = soup.find_all('span',
                                 {'class': 'css-901oao css-16my406 r-18jsvk2 r-poiln3 r-b88u0q r-bcqeeo r-qvutc0'})
            noResTimes += 1
            if noResTimes >= 20:
                return 'Cant find this user!'
        except:
            return 'Cant find this user!'

    funsNum = divs[1].get_text()
    if (',' in funsNum):
        temp = funsNum.split(',')
        funsNum = int(temp[0]) * 1000 + int(temp[1])
        return funsNum

    elif ('万' in funsNum):
        temp = funsNum.split('万')
        funsNum = float(temp[0]) * 10000
        return funsNum
    elif (funsNum == 'Cant find this user!'):
        return funsNum
    else:
        return funsNum


def saveToCsv(savePath, oriDfPath, insertData, columnName):
    df = pd.read_csv(oriDfPath, encoding="UTF-8")
    df.insert(loc=len(df.columns), column=columnName, value=insertData)
    df.to_csv(savePath, encoding='utf_8_sig')


def tranFunNum(csvPath, savePath):
    df = pd.read_csv(csvPath, encoding="UTF-8")
    FunsNum = df['Funs']
    procFun = []
    for i in FunsNum:
        if (',' in i):
            temp = i.split(',')
            realNum = int(temp[0]) * 1000 + int(temp[1])
            procFun.append(realNum)
            # print(realNum)
        elif ('万' in i):
            temp = temp = i.split('万')
            realNum = float(temp[0]) * 10000
            procFun.append(realNum)
        elif (i == 'Cant find this user!'):
            procFun.append('Cant find this user!')
        else:
            procFun.append(int(i))
    df.drop(columns='Funs', axis="columns", inplace=True)
    df.insert(loc=len(df.columns), column='Funs', value=procFun)
    df.to_csv(savePath, encoding='utf_8_sig')


def transDir(basePath, savebasePath):
    fileNames = os.listdir(basePath)
    for filePath in fileNames:
        csvPath = os.path.join(basePath, filePath)
        # savePath=savebasePath+'F:\Code/2022/CYQ-spider/0313-testAddFuns/afterProcess/Trans—%s'%filePath
        savePath = savebasePath + 'Trans—%s' % filePath
        print('Transfering file %s' % csvPath)
        # print(csvPath)
        tranFunNum(csvPath, savePath)
        print('File %s transfer done!' % csvPath)


if __name__ == '__main__':
    #-----------------------------------------------------
    driverPath = "F:\Code//2022\chromedriver_win32\chromedriver.exe" #Enter your chromedriver path here
    basePath = 'data/' # Enter the path of the csv file you want to process
    savaBasePath = '0313data/addFuns/' # Enter the path of the csv file you want to save
    #-----------------------------------------------------
    if (not os.path.exists(savaBasePath)):
        os.mkdir(savaBasePath)
    driver = creatBroserDriver(driverPath)
    fileNames = os.listdir(basePath)
    for filePath in fileNames:
        csvPath = os.path.join(basePath, filePath)
        if (not os.path.isdir(csvPath)):
            print('processing file %s' % filePath)
            savePath = savaBasePath + 'Done-%s' % filePath
            funsArray = []

            userNames = readDf(csvPath, elementName='User_name')
            for index, userName in enumerate(userNames):
                funsNum = searchFunsNum(driver, userName=userName)
                funsArray.append(funsNum)
                if len(funsArray) % 500 == 0:
                    print('Process %s items' % len(funsArray))

            saveToCsv(savePath=savePath, oriDfPath=csvPath, insertData=funsArray, columnName='Funs')
            print('Process have done! saved in %s' % savePath)
