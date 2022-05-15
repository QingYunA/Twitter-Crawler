# import BeautifulSoup
import os
from math import fabs
import time
import datetime
from xml.etree.ElementTree import Comment

import requests
from hyperlink import URL
from numpy import common_type
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions


def Twitter_Crawler(driver, Keyword_Path, Stop_num, kw_start_point=0, save_path=None, start_date=None, end_date=None,
                    limit_language='all', photo_path='./photo/'):
    '''
    core function
    :param driver: Chrome Driver
    :param Keyword_Path:the file directory of your keywords which should be csv
    :param Stop_num: the number of the items need to be collect
    :param kw_start_point:start of your keyword
    :param save_path: the file directory of your data which should be csv
    :param start_date: the start date of search
    :param end_date: the end date of search
    :return:
    '''
    df = pd.read_csv(Keyword_Path, encoding='GB18030')
    page_index = 1
    search_end = False
    for index, kw in enumerate(df['keywords']):
        if (index >= kw_start_point):
            Data_List = []
            History_data = []
            url = 'https://twitter.com/search?q=%s&src=typed_query' % kw
            driver.get(url)
            driver.implicitly_wait(10)
            try:
                old_scroll_height = 0  # 表明页面在最上端
                js1 = 'return document.body.scrollHeight'  # 获取页面高度的javascript语句
                js2 = 'window.scrollTo(0, document.body.scrollHeight)'  # 将页面下拉的Javascript语句
                while ((driver.execute_script(js1) > old_scroll_height and len(
                        Data_List) < Stop_num) and search_end == False):  # 将当前页面高度与上一次的页面高度进行对比
                    old_scroll_height = driver.execute_script(js1)  # 获取到当前页面高度
                    driver.execute_script(js2)  # 操控浏览器进行下拉
                    time.sleep(3)  # 空出加载的时间
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    divs = soup.find_all('div', {'class': 'css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu'})
                    for divIndex, div in enumerate(divs):
                        data_list = []

                        try:
                            content = div.find('div', {
                                'class': 'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0'})
                            if (content):
                                str_content = content.get_text()
                            else:
                                content = div.find('div', {
                                    'class': 'css-901oao r-18jsvk2 r-1tl8opc r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0'})
                                str_content = content.get_text()

                            # 获取名字
                            name = div.find(
                                'span', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'}).get_text()
                            # 获取用户名
                            user_name = div.find(
                                'div', {'class': 'css-1dbjc4n r-18u37iz r-1wbh5a2 r-13hce6t'}).get_text()
                            # 写入时间
                            date = div.find('time')
                            date = date['datetime']
                            date = date.split('T')[0]
                            # 校验推文发布时间是否在范围内
                            # if (date > start_date):
                            #     continue
                            # if (date < end_date):
                            #     search_end = True
                            #     print('时间超出%s，搜索结束!' % end_date)
                            # 写入转发 评论 点赞数量
                            temp = div.find_all('span', {
                                'class': 'css-901oao css-16my406 r-poiln3 r-n6v787 r-1cwl3u0 r-1k6nrdp r-1e081e0 r-qvutc0'})
                            interactionDatas = []
                            for span in temp:
                                interactionDatas.append(span.get_text())
                            try:
                                language = content.get('lang')
                            except:
                                language = 'unknown'
                            # download img
                            kw_photo_path = photo_path + kw + '/'
                            # print(kw_photo_path)
                            if (not os.path.exists(kw_photo_path)):
                                os.mkdir(kw_photo_path)
                            try:
                                img_url = div.find('img', {'alt': "图像"}).get('src')
                                r = requests.get(img_url)
                                path = os.path.join(kw_photo_path, user_name + '.jpg')
                                print(path)
                                with open(path, 'wb') as f:
                                    f.write(r.content)
                            except:
                                wushifasheng = 0
                            # 写入dataSet
                            if ((language == limit_language or limit_language == 'all') and (
                                    str_content not in History_data)):
                                data_list.append(name)  # 名字
                                data_list.append(user_name)  # 用户名
                                data_list.append(date)
                                data_list.append(str(str_content).strip().replace('\n', ''))  # 内容
                                for interactionData in interactionDatas:
                                    data_list.append(interactionData)
                                data_list.append(language)
                                History_data.append(str_content)
                            else:
                                continue
                            Data_List.append(data_list)
                        except:
                            continue
            except Exception as e:
                print(e)
            SaveToCSV(Data_List, index, df, page_index, save_path)


def SaveToCSV(Data_List, index, keyword_df, page_index, save_path):
    '''
    将数据保存到CSV文件中
    '''
    df_Sheet = pd.DataFrame(Data_List, columns=[
        'Name', 'User_name', 'Date', 'Content', 'Comments', 'Forward', 'Like', 'Language'])
    TIMEFORMAT = '%y%m%d-%H%M%S'
    now = datetime.datetime.now().strftime(TIMEFORMAT)
    kw = keyword_df['keywords'][index]
    kw = kw.split(' ')[0]
    csv_path = save_path + '/kw=%s-%s.csv' % (kw, now)
    df_Sheet.to_csv(csv_path, encoding='utf_8_sig')
    print('第 {} 个URL信息已获取完毕。'.format(page_index))
    try:
        print("共采集了%s条数据" % len(Data_List))
    except:
        print('意外')
