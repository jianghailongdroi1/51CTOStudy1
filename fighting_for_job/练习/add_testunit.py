#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/3

import unittest,time

import baidu
import HTMLTestRunner
#实例化一个测试套件
testunit = unittest.TestSuite()
#将用例加到测试套件中
testunit.addTest(unittest.makeSuite(baidu.Baidu))
#报告地址

# report_filename = r"C:\test"+ "\" + time.asctime(time.localtime(time.time()) + '.html'
now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))
report_filename = r"C:\test\%s.html" %(now)

# report_filename = r"C:\test\%s.html" %(time.time())
with open(report_filename,"wb") as rf:
    runner = HTMLTestRunner.HTMLTestRunner(stream=rf,title="测试报告",description="用例执行情况")
    runner.run(testunit)


