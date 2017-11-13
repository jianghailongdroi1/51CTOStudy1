#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/24

import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
sys.path.append(BASE_DIR)

from src.services import admin_service
from src.services import teacher_service
from src.services import student_service
from src.services import initialize_service
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

def show_role():
    msg="""
    '0':初始化
    '1':管理员
    '2':老师
    '3':学生
    """
    print(msg)

def main():
    choice_dict={
        '0':initialize_service.main,
        '1':admin_service.main,
        '2':teacher_service.main,
        '3':student_service.main
    }
    show_role()
    while True:
        choice = input("请输入角色：").strip()
        if choice not in choice_dict:
            print("输入有误")
            continue
        else:
            choice_dict[choice]()
if __name__ == '__main__':
    main()
