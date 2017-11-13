#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/26

import re
def md(date_list,symbol):
    '''
    :param date_list: 匹配到的表达式
    :param symbol: 符号
    :return: 乘数计算得到的值
    '''
    a = date_list.index(symbol)  #取到符号
    # print(a)
    if symbol == '*' and date_list[a + 1] != '-': #如果是乘号并且索引的下一个位置不是负号计算
        k = float(date_list[a - 1]) * float(date_list[a + 1])
    elif symbol == '/' and date_list[a + 1] != '-':  #如果是除号并且索引的下一个位置不是负号计算
        k = float(date_list[a - 1]) / float(date_list[a + 1])
    elif symbol == '*' and date_list[a + 1] == '-': #如果是乘号并且索引的下一个位置是负号计算
        k = -(float(date_list[a - 1]) * float(date_list[a + 2]))
    elif symbol == '/' and date_list[a + 1] == '-': #如果是除号并且索引的下一个位置是负号计算
        k = -(float(date_list[a - 1]) / float(date_list[a + 2]))
    del date_list[a - 1], date_list[a - 1], date_list[a - 1] #删除列表里参与计算的索引位置
    date_list.insert(a - 1, str(k))  #把新的值插入到列表中
    return date_list

#处理混乱的四则，按照先算乘除后加减的原则
def fun(s):
    '''
    :param s: 去除括号后的表达式
    :return: 表达式的返回值
    '''
    list_str = re.findall('([\d\.]+|/|-|\+|\*)',s) #匹配表达式
    # print(list_str)
    sum=0
    while True:
        #先算*/后算+-
        if '*' in list_str and '/' not in list_str:  #判断*在表达式内,/不在
            md(list_str, '*')
        elif '*' not in list_str and '/' in list_str: #判断*不在表达式内,/在
            md(list_str, '/')                   #调用md函数处理除号
        elif '*' in list_str and '/' in list_str: #判断*在表达式内,/也在
            a = list_str.index('*')
            b = list_str.index('/')
            if a < b:
                md(list_str, '*')
            else:
                md(list_str, '/')
        else:
            if list_str[0]=='-':   #判断首个数字是否是负号
                list_str[0]=list_str[0]+list_str[1]
                del list_str[1]
            sum += float(list_str[0])
            #3+1-4+7
            for i in range(1, len(list_str), 2):    #1,3,5,7,9
                if list_str[i] == '+' and list_str[i + 1] != '-':
                    sum += float(list_str[i + 1])
                elif list_str[i] == '+' and list_str[i + 1] == '-':
                    sum -= float(list_str[i + 2])
                elif list_str[i] == '-' and list_str[i + 1] == '-':
                    sum += float(list_str[i + 2])
                elif list_str[i] == '-' and list_str[i + 1] != '-':
                    sum -= float(list_str[i + 1])
            break
    return sum

a=input("请输入算式：")#a='1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#循环去除括号
while True:
    ret = re.split('\(([^()]+)\)', a , 1)
    # print(ret)
    if len(ret) == 3:
        a,b,c = re.split('\(([^()]+)\)', a, 1)
        rec = fun(b)
        a = a + str(rec) + c
    else:
        red = fun(a)
        print(red)
        break
