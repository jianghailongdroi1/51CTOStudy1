# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
# # __author__ = "Q1mi"
# # Date: 2017/9/14
# #
# # import time
# #
# # def timer(func):
# #     def warpper()
# #
# #
# # def qst1():
# #     time.sleep(3)
# #     print("in test1")
# # qst1()
# import time
#
# def deco(func):
#     start_time=time.time()
#     func()
#     end_time=time.time()
#     print("the func run time is %s" %(end_time-start_time))
#
#
#
# def test1():
#     time.sleep(3)
#     print("in the test1")
#
# def test2():
#     time.sleep(3)
#     print("in the test2")
#
# deco(test1)
# deco(test2)
#
# # test1()
# # test2()

import time

user,passwd="Marvin","224466"

def auth(func):
    def wrapper(*args,**kwargs):
        username = input("Username:").strip()
        password = input("Password:").strip()

        if user==username and passwd ==password:
            print("\033[32:1m登录成功\033[0m")
            func(*args,**kwargs)
        else:
            exit("\033[31:1m用户名或密码错误\033[0m")
    return wrapper

def index():
    print("welcome to index page")

@auth
def home():
    print("welcome to home page")

@auth
def bbs():
    print("welcome to bbs page")

index()

home()

bbs()