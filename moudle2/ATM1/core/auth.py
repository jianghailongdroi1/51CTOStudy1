#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/11

"""
认证模块
"""
print("BB")
import os,json,time

from core import db_handle
from conf import settings

def access_auth(account,password,log_obj):
    """
    下面的access_login调用access_auth方法，用于登陆
    :param account:用户名
    :param password:密码
    :return:如果未超期，返回字典，超期则打印相应提示
    """
    db_path=db_handle.handle(settings.DATABASE)#调用db_handle方法返回路径/db/accounts
    print(db_path)
    account_file ="%s/%s.json" %(db_path,account)#用户文件
    print(account_file)
    if os.path.isfile(account_file):#如果用户文件存在（即用户存在）
        with open(account_file,"r",encoding='utf-8') as f:#打开文件
            account_data=json.load(f)  #account_data为字典形式
            print(account_data)
            if account_data["password"] == password:
                expire_time =time.mktime(time.strptime(account_data["expire_data"],"%Y-%m-%d"))
                print(expire_time)
                print(time.strptime(account_data["expire_data"],"%Y-%m-%d"))
                if time.time() > expire_time:#如果信用卡超期
                    log_obj.error("Account [%s] had expired,Please contract the bank" % account)
                    print("\033[31;1m账号%s已过期，请联系银行" % account)
                else:   #信用卡未超期，返回用戶數據的字典
                    print("return")
                    log_obj.info("Account [%s] logging success" % account)
                    return account_data
            else:
                log_obj.error("Account or Passworddoes not correct!")
                print("\033[31;1m密码错误！\033[0m")
    else:
        #用户名不存在
        log_obj.error("Account [%s] does not exist!" % account)
        print("\033[31;1m用户不存在\033[0m")

def access_login(user_data,log_obj):
    """
    登陆
    :param user_data:
    :return:
    """
    retry=0
    while not user_data["is_authenticated"] and retry < 3:
        account=input("账号：").strip()
        password=input("密码：").strip()
        #用戶賬戶密碼正確且信用卡未超期，返回用戶數據的字典
        user_auth_data=access_auth(account,password)
        if user_auth_data:
            user_data["is_authenticated"] = True #用戶認證為True
            user_data["account_id"]=account  #用戶賬號ID為賬號名
            print("歡迎")
            return user_auth_data
        retry += 1  # 登陆和信用卡认证出错，则次数加1

    else: # 若次数超过三次，打印相关信息并退出
        print("Account [%s] try logging too many times..." % account)
        log_obj.error("Account [%s] try logging too many times..." % account)
        exit()





