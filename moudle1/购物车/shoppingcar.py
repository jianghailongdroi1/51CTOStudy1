#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/25
'''
购物车：
1. 商品信息- 数量、单价、名称
2. 用户信息- 帐号、密码、余额
3. 用户可充值
4. 购物历史信息
5. 允许用户多次购买，每次可购买多件
6. 余额不足时进行提醒
7. 用户退出时 ，输出档次购物信息
8. 用户下次登陆时可查看购物历史
9. 商品列表分级显示
'''
import os

#展示商品列表
def goodsList_show():
    print('''Choice the goods you want，here are the list:
    %s'''%(goodsList))

#读取被锁定用户信息
def getLockedList():
    f=open('locked','r')
    lockedList=f.read()
    # print(lockedList)
    locked_list=lockedList.split('#')
    # print(locked_list)
    f.close()
    return locked_list
#添加被锁定用户名
def addLockedUsername(name):
    f1=open("locked",'a+')
    f1.write('#'+name)
    f1.close()

#登录
def login(username):
    lockedList=getLockedList()
    # print(lockedList)
    while True:
        if username in userList:
            #判断是否被锁定
            if username in lockedList:
                print("your account has been locked")
                os._exit(0)
            else:
                password=input('please input your password>>')
                if userList[username][0]==password:
                    print("welcome!")
                    break
                else:
                    count[username] +=1
                    if count[username]>=3:
                        print("Input wrong password three times,your account is locked!")
                        addLockedUsername(username)
                        os._exit(0)
        else:
            username=input("worry username!please try again>>")
            if username not in count:
                count[username]=0
            login(username)
            count[username] +=1





#显示用户信息
def user_information_show(username):
    print("用户名为%s,余额为%s" %(username,userList[username][-1]))

#获取用户购物历史信息
def shopping_History_show(username):
    if username in shoppingHistroy:
        print("Your shoppingHistory:%s"%(shoppingHistroy[username]))
    else:
        print("您暂时还没有购物记录，快去购物吧！")

#添加到购物车
def add_to_shoppingCar(item):
    if item in shopping_Car:
        shopping_Car[item][-1] += 1
    else:
        shopping_Car[item]=[goodsList[item],1]

#获取购物车
def shoppingCar_show(username):
    print("Your shoppingCar %S"%(shopping_Car[username]))

#删除购物车内商品
def del_from_shoppingCar(goodname):
    if goodname in shopping_Car:
        del shopping_Car[goodname]
    else:
        print("购物车内不存在该商品")

#充值
def recharge(s):
    if str.isdigit(s):
        userList[username][-1] +=int(s)
        print("充值成功！")

#展示购物记录
def shoppingRecord_show():
    print("Your shoppingRecord:%s"%(shoppingRecord))

#结算
def checkOut():
    amountShouldPay=0
    if len(shopping_Car)==0:
        print("Nothing to checkOut")
    else:
        for item in shopping_Car:
            amountShouldPay+= shopping_Car[item][0]*shopping_Car[item][-1]
        if amountShouldPay <= userList[username][-1]:
            userList[username][-1] -=amountShouldPay
            print("CheckOut success!")
            for item in shopping_Car:
                for item1 in shoppingHistroy[username]:
                    if item1==item:
                        shoppingHistroy[username][item1][-1] +=shopping_Car[item][-1]
                else:
                    shoppingHistroy[username][item[0]]=shopping_Car[item]

        else:
            print('Balance is not enough,recharge fist!')
            choice=input("input 'R' to recharge>>")
            if choice=="R":
                monkey=input("how much do you want to recharge>>")
                recharge(monkey)
                user_information_show(username)
                checkOut()
                #print("1")
            else:
                print("worry input")
                os._exit(0)


#用户信息：用户名/密码/余额
userList={
    "Marvin":["q123",1000],
    "chenqifeng":["w1234",1500],
    "chenfan":["224466",2000]
}
#历史购物记录
shoppingHistroy={
    "Marvin": {"iphone":[5600,2],
               "bike":[1000,1]
               },

    "chenqifeng": {"T-shirt":[199,1]},
    "chenfan": {"chair":[1200,1]}
}
#商品列表
goodsList={
    "iphone":5600,
    "bike":1000,
    "T-shirt":199,
    "chair":1200,
    "cup":600
}
shoppingRecord={}
shopping_Car={}
myUsername=""
count={}
username=input("please input your username>>")
count[username]=0
login(username)
user_information_show(username)
shopping_History_show(username)
goodsList_show()
while(True):
    choice1=input('''
    Which goods do you want to buy?please input the goodsname
    if you want to checkout,please input "C"
    if you want to quit,please input "Q"
    ''')
    if choice1 in goodsList:
        add_to_shoppingCar(choice1)
    elif choice1 =="C":
        print("your shoppingCar:%s"%(shopping_Car))
        checkOut()
        continue
    elif choice1=="Q":
        shoppingRecord_show()
        print("goodbye!")
        os._exit(0)
    else:
        print("worry input")










