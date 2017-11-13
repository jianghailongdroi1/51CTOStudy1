#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/19
import re,json
# d={"1":{"name":"alex","age":'22','phone':'13651054608',"dept":"运维","enroll_data":"2013-04-01"}}
# json.dump(d,sort_keys=True)

#Json存储
def store(data):
    with open('information.txt', 'w') as json_file:
        json_file.write(json.dumps(data))

#Json加载
def load():
    with open('information.txt') as json_file:
        data = json.load(json_file)
        return data
#判断phone是否重复
def phone_repete(info1,info2):
    for item in info1:
        info1[item]["phone"]==info2["phone"]
        return True
    return False

#将符合要求的查询结果转化为字符串
#{'1': {'name': 'Mark', 'age': '22', 'phone': '13651054608', 'dept': 'IT', 'enroll_data': '2013-04-01'}}
def get_final_result(show_item,show_list):
    if len(show_list)==0:
        return("没有符合条件的结果")
    show_final_list=[]
    show_final=""
    for item2 in show_list:
        for i in show_item:
            if i =="staff_id":
                show_final_list.append(item2)
            else:
                show_final_list.append(show_list[item2][i])
        show_final_list.append("\n")
        show_final=",".join(show_final_list)
    return show_final
#查询
def fetch(data):
    #需要展示的项，如staff_id等
    show_item=[]
    #筛选的初步结果，字典形式
    show_list={}
    all_item=["staff_id","name","age","phone","dept","enroll_date"]
    data1=data.split(" ")#['select', '*', 'from', 'staff_table', 'where', 'dept', '=', '"IT"']
    #判断是否是select语句
    if data1[0]!="select":
        return("此语句不是select语句")

    #检索查询项及校验
    if data1[1]=="*":
        show_item=all_item
    else:
        show_item=data1[1].split(",")
        for item in show_item:
            if item not in ["staff_id","name","age","phone","dept","enroll_date"]:
                return("输入的查询项%s有误" %item)

    #校验查询的表是否正确
    if re.findall(r"from (.+?) where",data)[0]!="staff_table":
        return("查询的表不存在")

    #where条件
    df=data1[-3].strip()
    if df not in all_item or data1[-2] not in [">","=","like"]:
        return("查询语句中的where条件输入有误")

    #读取Json文件中的原始数据
    initial_data=load()#{'1': {'name': 'Mark', 'age': '22', 'phone': '13651054608', 'dept': 'IT', 'enroll_date': '2013-04-01'}}
    condition=data1[-3]
    symbol=data1[-2]
    if condition=="staff_id":
        if symbol==">":
            for item in initial_data:
                if item > int(data1[-1]):
                    show_list[item] = initial_data[item]
        if symbol=="=":
            for item in initial_data:
                if item > int(data1[-1]):
                    show_list[item] = initial_data[item]
        return get_final_result(show_item,show_list)
    if condition=="age":
        if symbol==">":
            for item in initial_data:
                if int(initial_data[item]["age"])>int(data1[-1]):
                    show_list[item]=initial_data[item]
        if symbol=="=":
            for item in initial_data:
                if initial_data[item]["age"]==int(data1[-1]):
                    show_list[item]=initial_data[item]
        return get_final_result(show_item,show_list)

    if condition in ["name","phone","dept","enroll_date"]:
        if symbol=="like":
            for item in initial_data:
                r=re.findall(r"%s(.+?)" %data1[-1].strip().strip('"'),initial_data[item][condition])
                if len(r)!=0:
                    show_list[item]=initial_data[item]
        if symbol=="=":
            for item in initial_data:
                if initial_data[item][condition]==data1[-1].strip("\\\""):
                    show_list[item]=initial_data[item]
        return get_final_result(show_item,show_list)

def judge_add_sql(statements):
    #insert into staff_table values ('name','age','phone','dept','enroll_date')
    #截取输入的值
    r=re.findall(r"insert into staff_table values (.+)",statements)[0].strip("(").strip(")").replace("'",'').replace('"',"")
    r=r.split(",")
    #没有截取到内容时
    if r==None or len(r)!=5:
        return False
    else:
        return("{'name':'%s','age':'%s','phone':'%s','dept':'%s','enroll_date':'%s'}" %(r[0],r[1],r[2],r[3],r[4]))

def judge_update_sql(statements):
    #UPDATE staff_table SET dept="Market" WHERE dept = "IT"
    change= re.findall(r"UPDATE staff_table SET (.+) WHERE *",statements)
    condition = re.findall(r"UPDATE staff_table SET %s WHERE (.+)" %change[0], statements)
    change = change[0].split("=")
    condition=condition[0].split("=")
    if change[0] and change[1] and condition[0] and condition[1]:
        r=[change,condition]
        return r
    else:
        return False

def add(data):
    #检索输入语句是否正确
    judgment=judge_add_sql(data)
    if judgment==False:
        return ("输入的语句有误")
    else:
        judgment=eval(judgment)
        #判断phone是否重复
        old_file=load()
        k_max=1
        for k in old_file:
            #获取序号的最大值
            if k_max<int(k):
                k_max=int(k)
            if old_file[k]['phone']==judgment['phone']:
                return('phone已存在')
        k_new=k_max+1
        old_file[str(k_new)]=judgment
        store(old_file)
        return("添加成功")

def updata(data):
    #UPDATE staff_table SET dept="Market" WHERE dept = "IT"
    flag = False
    r=judge_update_sql(data)
    old_file=load()
    # print(old_file)
    for k in old_file:
        f = r[1][0].strip(" ")
        if old_file[k][f]==r[1][1].strip().strip("'").strip('"'):
            flag=True
            old_file[k][r[0][0]] = r[0][1].strip().strip("'").strip('"')
            store(old_file)
        if flag:
            return("修改成功")
        else:
            return("输入有误")


def delete(data):
    old_file=load()
    for k in old_file:
        if k==data:
            old_file.pop(data)
            store(old_file)
            return("删除成功")
    return("未找到对应数据")

# if __main__==__name__:
while True:
    print('''========================
                欢迎来到员工信息系统
             ------------------------
                     1、查询
                     2、添加
                     3、修改
                     4、删除
                     5、退出
    
    ''')
    choice=input("请输入功能选项:")
    # info="select name,age from staff_table where age > 22"
    if choice.isdigit():
        choice=int(choice)
        if choice in [1,2,3,4]:
            data = input("请输入语句:")
            if choice==1:
                print(fetch(data))
            if choice == 2:
                print(add(data))
            if choice == 3:
                print(updata(data))
            if choice == 4:
                print(delete(data))
            continue
        if choice==5:
            print("欢迎下次再来！")
            break
        print("输入的数字有误，请重新输入！")
    else:
        print("输入有误，请重新输入！")
