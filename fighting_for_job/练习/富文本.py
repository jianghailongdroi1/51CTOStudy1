#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/2


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

profileDir = r"C:\Users\jianghailong.EXPOPAY\AppData\Local\Temp\rust_mozprofile.CblvQpf5ii1M"
profile = webdriver.FirefoxProfile(profileDir)
driver = webdriver.Firefox(profile)

url = "http://www.cnblogs.com/"
personal_url = url + "Macal/"
driver.get(personal_url)
driver.find_element_by_xpath(".//*[@id='blog_nav_newpost']").click()
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='Editor_Edit_txbTitle']").send_keys("biaoti")
body = "zhe shi body"
driver.switch_to.frame("Editor_Edit_EditorBody_ifr")
driver.find_element_by_xpath(".//*[@id='tinymce']/p").send_keys(Keys.TAB)
driver.find_element_by_xpath(".//*[@id='tinymce']/p").send_keys(body)

