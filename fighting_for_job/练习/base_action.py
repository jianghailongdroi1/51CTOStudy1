#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/2

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
# # driver = webdriver.IE()
# # driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# # driver.find_element_by_name("tj_trnews").click()
# driver.find_element_by_xpath(".//*[@id='form']/span[1]").send_keys("p")
#
# time.sleep(1)
# # driver.set_window_size(540,960)
# # # driver.close()
# # # driver.get_screenshot_as_file("C:\\test\selenium\b1.png")
# # time.sleep(1)
# # driver.maximize_window()
# driver.quit()
# # driver.get("http://www.hordehome.com")
# # time.sleep(2)
# # driver.back()
# # # print("3333")
# # time.sleep(2)
# # driver.forward()
# # driver.refresh()
# ActionChains(driver).context_click().perform()
driver.get("http://www.hordehome.com")
driver.implicitly_wait(10)
driver.find_element_by_xpath(".//*[@id='ember808']/header/div/div/div[2]/span/button[2]").click()
driver.find_element_by_xpath(".//*[@id='login-account-name']").send_keys("853226549@qq.com")
driver.find_element_by_xpath(".//*[@id='login-account-password']").send_keys("yunlong123")
driver.find_element_by_css_selector(".btn.btn-large.btn-primary").click()
# driver.find_element_by_xpath(".//*[@id='ember1211']/div[2]/button[1]").click()


