#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/2

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest,time,xlrd
login_data_file=r"C:\test\login.xlsx"
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        print(type(data))
        return data
    except Exception as e:
        print(str(e))

def excel_table_byindex(file = login_data_file,colnameindex = 0,by_index = 0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    # data.
    nrows = table.nrows#行数
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
                list.append(app)
    return list

def login():
    listdata = excel_table_byindex()
    if (len(listdata) <= 0):
        assert 0,"excel数据异常"
    for i in range(len(listdata)):
        username = str(int(listdata[1]["passname"]))
        password = str(listdata[1]["password"])
        driver =webdriver.Firefox()
        driver.get("https://workyun.com")
        #点击登录功能
        driver.find_element_by_xpath(".//*[@id='home']/div/div[2]/header/nav/div[3]/ul/li[1]/a").click()
        driver.implicitly_wait(10)
        print(username)
        driver.find_element_by_xpath(".//*[@id='passname']").send_keys(username)
        driver.find_element_by_xpath(".//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath(".//*[@id='content']/div/div[6]/input").click()
        time.sleep(2)
        try:
            element = driver.find_element_by_xpath(".//*[@id='ee-header']/div[1]/div/ul[2]/li/a/img")
        except NoSuchElementException:
            assert 0,"fail login"

        driver.close()

if __name__ == '__main__':
    login()





