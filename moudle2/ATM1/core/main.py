#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/18

# print(__file__)
'''
额度 15000或自定义
实现购物商城，买东西加入 购物车，调用信用卡接口结账
可以提现，手续费5%
支持多账户登录
支持账户间转账
记录每月日常消费流水
提供还款接口
ATM记录操作日志
提供管理接口，包括添加账户、用户额度，冻结账户等。。。
用户认证用装饰器

主逻辑交互模块
'''

from core import auth,log,transaction,account

#用户数据信息
user_data={
    "account_id":None,       #账号ID
    'is_authenticated':False,#是否认证
    'account_data':None      #账号数据
}
#調用log文件下的log方法，返回日誌對象
access_logger = log.log("access")

def account_info(acc_data):
    """
    acc_data:包括ID，is_authenticaed,用户帐号信息
    查看用户帐户信息
    :return:
    """
    print(acc_data)


def repay(acc_data):
    """
    acc_data:包括ID，is_authenticaed,用户帐号信息
    还款
    :return:
    """
    print(acc_data)
    print("??")
    #调用account模块的load_account方法，从数据库从load出用户信息
    account_data = account.load_account(acc_data["id"])
    print(account_data)
    current_balance = """
    -------------BALANCE INFO--------------
    Credit:%s
    Balance:%s
    """ % (account_data["credit"], account_data["balance"])
    back_flag = False
    while not back_flag:
        print(current_balance)
        repay_amount = input("\033[31;1mInput repay amount(b=back):\033[0m").strip()
        #如果用户输入整型数字
        if len(repay_amount) > 0 and repay_amount.isdigit():
            #调用transaction模块的方法,参数分别是用户帐户信息，交易类型，交易金额
            new_account_data = transaction.make_transaction(account_data, "repay", repay_amount)
            if new_account_data:
                print("\033[42;1mNew Balance:%s\033[0m" % new_account_data["balance"])

        else:
            print("\033[31;1m%s is not valid amount,Only accept interger!\033[0m" % repay_amount)

        if repay_amount =="b" or repay_amount == "back":
            back_flag = True

def withdraw():
    """
    退出
    :return:
    """
    pass

def transfer():
    """
    转账
    :return:
    """
    pass

def paycheck():
    """
    转账检查
    :return:
    """
    pass

def logout():
    """
    退出登录
    :return:
    """
    pass

def interactive():
    """
    交互
    :return:
    """
    msg = (
        """
        -------------ZhangChengLiang Bank---------------
        \033[31;1m 1.  账户信息
        2.  还款
        3.  取款
        4.  转账
        5.  账单
        6.  退出
        \033[0m"""
    )
    menu_dic = {
        "1":account_info,
        "2":repay,
        "3":withdraw,
        "4":transfer,
        "5":paycheck,
        "6":logout
    }
    flag = False
    while not flag:
        print(msg)
        choice = input("<<<:").strip()
        if choice in menu_dic:
            #很重要！！省了很多代码，不用像之前一个一个判断！
            menu_dic[choice](acc_data)

        else:
            print("\033[31;1mYou choice doesn't exist!\033[0m")

def run():
    """
    当主要程序启动时调用，用于实现主要交互逻辑
    :return:
    """
    # 调用认证模块,返回用户文件json.load后的字典,传入access_logger日志对象
    access_data = auth.access_login(user_data, access_logger)
    print("AA")
    if user_data["is_authenticated"]:       #如果用户认证成功
        print("has authenticated")
        #将用户文件的字典赋给user_data["account_data"]
        user_data["account_data"] = access_data
        interactive(user_data)   #用户交互开始