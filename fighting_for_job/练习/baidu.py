#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.support import expected_conditions as EC
import unittest,time,re
import HTMLTestRunner

class Baidu(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.baidu.com/"
        self.verificationError = []
        self.accept_next_alert = True

    def test_baidu_search(self):
        """百度搜索"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath(".//*[@id='kw']").send_keys("selenium")
        time.sleep(2)
        # driver.close()
    def test_baidu_set(self):
        driver = self.driver
        url = self.base_url+"item/Fate%2FGrand Order/15091274?fr=aladdin&fromid=20599700&fromtitle=fgo"
        driver.get(url)
        time.sleep(2)
        # driver.close()

    def get_all_url(self):
        driver = self.driver
        driver.page_source

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationError)

if __name__ == '__main__':
    unittest.main()



