#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/18
# #相对路径
# print(__file__)
#
# #绝对路劲
# import os
# print(os.path.abspath(__file__))
# #文件夹名
# print(os.path.dirname(os.path.abspath(__file__)))
# #ATM的路径
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
#
# import sys
# sys.path.append(BASE_DIR)
# from conf import settings
# from core import main
#
#
# main.login()
"""
ATM主程序的执行文件
"""
import os,sys
dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#找到当前路径
sys.path.insert(0,dir)#添加路径
print(dir)
#将main.py里面所有代码封装成mian变量
from core import main

if __name__=="__main":
    main.run()
