#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/23
import getpass
from src.moudles import Admin

def initialize():
    try:
        user = input("输入初始化用户名：").strip()
        pwd = input("输入初始化密码：").strip()
        #pwd = getpass.getpass("输入初始化密码：").strip()
        obj = Admin(user,pwd)
        # print('123344')
        obj.save()
        # print('12')
        return True
    except Exception as e:
        print(str(e))

def main():
    show="""
    1.初始化管理员账户
    """
    choice_dict = {
        '1':initialize
    }
    while True:
        print(show)
        choice = input("请输入操作选项：").strip()

        if choice not in choice_dict:
            print('\033[43;1m选项错误，请重新输入！！！\033[0m')
        else:
            ret = choice_dict[choice]()
        if ret:
            print('操作成功')
            return
        else:
            print('操作异常，请重新操作')

if __name__ == '__main__':
    main()

