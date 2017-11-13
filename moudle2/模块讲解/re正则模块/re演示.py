#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/20
import re
# a = 'hello word diao zha tian'
# ret = re.match('h\w+',a)
# print(ret.group()) #获取匹配到的所有结果
# print(ret.groups()) # 获取模型中匹配到的分组情况
# print(ret.groupdict())# 获取模型中匹配到的分组结果
# ############output##############
# # hello
# # ()
# # {}
# ret = re.match('(?P<n>h)(?P<n1>\w+)',a)
# print(ret)
# print(ret.group()) #获取匹配到的所有结果
# print(ret.groups()) # 获取模型中匹配到的分组情况
# print(ret.groupdict())# 获取模型中匹配到的分组结果
def f1(ex):
    return eval(ex)  # 测试用 真实中要自己编写四则运算


a = '1*2+(5/6)+(12*23)/15+1'
while True:
    ret = re.split('\(([^()]+)\)', a)
    print(ret)
    if len(ret) == 3:
        a, b, c = re.split('\(([^()]+)\)', a, 1)
        rec = f1(b)
        a = a + str(rec) + c
    else:
        red = f1(a)
        print(red)
        break