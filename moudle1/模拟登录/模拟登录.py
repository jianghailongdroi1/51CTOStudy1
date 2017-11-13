#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/24
'''
模拟登陆：
1. 用户输入帐号密码进行登陆
2. 用户信息保存在文件内
3. 用户密码输入错误三次后锁定用户
'''
#读取用户信息并存入字典
f1=open('userinfo','r')
userinfo=f1.read()
# print(userinfo)
f1.close()
user_dic={}
userlist=userinfo.split("#")
# print(userlist)
for item in userlist:
    item_list=item.split(":")
    user_dic[item_list[0]]=item_list[-1]
# print(user_dic)

#读取被锁定用户信息
def getLockedList():
    f2=open('locked','r')
    lockedList=f2.read()
    # print(lockedList)
    locked_list=lockedList.split('#')
    # print(locked_list)
    f2.close()
    return locked_list

#添加被锁定用户名
def addLockedUsername(name):
    f3=open("locked",'a+')
    f3.write('#'+name)
    f3.close()

username=input("please input your username>>")
lockedList=getLockedList()
# print(lockedList)
count=0
while True:
    if username in user_dic:
        #判断是否被锁定
        if username in lockedList:
          print("your account has been locked")
          break
        else:
             password=input('please input your password>>')
             if user_dic[username]==password:
                 print("welcome!")
                 break
             else:
                 count +=1
                 if count>=3:
                     print("Input wrong password three times,your account is locked!")
                     addLockedUsername(username)
                     break
    else:
        print("worry username!please try again!")
        break








