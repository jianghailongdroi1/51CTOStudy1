#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/7

'''
HAproxy配置文件操作
1. 根据用户输入输出对应的backend下的server信息
2. 可添加backend 和sever信息
3. 可修改backend 和sever信息
4. 可删除backend 和sever信息
5. 操作配置文件前进行备份
6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
'''

import os
def fetch(data):
    backend_data="backend %s"%(data)
    # print(backend_data)
    searched_data = []
    with open("haproxy配置文件.txt","r")as f:
        tag=False
        for line in f:
            #print(line)
            if line.strip() ==backend_data:
                #print("1")
                tag=True
                continue
            if line.startswith("frontend"):
                #print("2")
                tag=False
                break
            if tag and line:
                #print("3")
                searched_data.append(line.strip())
    # for item in searched_data:
    #         print(item)
    return searched_data

def add(data):
    backend_title="backend %s"%(data["backend"])

    record="server %s %s weight %s maxconn %s" %(data["record"]["server"],\
                                                 data["record"]["server"],\
                                                 data["record"]["weight"],\
                                                 data["record"]["maxconn"])

    record_list=fetch(data["backend"])
    # 如果要插入的backend存在
        # 1.首先设定2个标志：flag和has_write
            # flag:用于找到要添加的backend下的内容
            # has_write:用于判断fetch_list中的内容是否重新写入到了文件
        # 2.遍历源文件ha：
            # 1首先逐行读取，并同时进行判断，
                 # 1.判断backend是否已经找到，先把backend写入文件，然后找到后将flag设置为True，最后跳出本次循环
                 # 2.判断找到的backend里面的record是否为空，若为空将flag设置为False
                 # 3.对flag进行判断
                    # 1.将flag为True的record从fetch_list写入到文件中，在这里面同时要进行是否已经写入的判断，即定义has_write的作用
                    # 2.若flag为False，就直接写入新文件，即将非列表里的内容直接写入
    if record_list:
        flag=False
        has_write=False
        with open("haproxy配置文件.txt","r")as f_read,\
                open("haproxy配置文件_new.txt","w")as f_write:
            for line in f_read:
                if line.strip()==backend_title:
                    f_write.write(line)
                    flag=True
                    continue
                if flag and line.startswith("frontend"):
                    flag=False
                if flag:
                    if not has_write:
                        f_write.write("%s%s\n"%(" "*8,record))
                        f_write.write(line)
                        has_write=True
                        print("1")
                    else:
                        f_write.write(line)
                        print("2")
                        # print("1")
                    # f_write.write("\n")
                else:
                    f_write.write(line)
    #如果要插入的backend不存在
        #分2部分写入：
            # 1部分.从ha文件里面直接读取，并同时将读取的内容写入新的文件ha.new
            # 2部分.将新的backend和context信息，直接写到新的文件ha.new的文件尾部
    else:
        with open("haproxy配置文件.txt", "r")as f_read, \
                open("haproxy配置文件_new.txt", "w")as f_write:
            for line in f_read:
                f_write.write(line)
            f_write.write(backend_title+"/n")
            f_write.write(record+"/n")

    os.rename("haproxy配置文件.txt","haproxy配置文件bak.txt")
    os.rename("haproxy配置文件_new.txt", "haproxy配置文件.txt")
    os.remove("haproxy配置文件bak.txt")

def remove(data):
    backend_data = "backend %s" % (data["backend"])
    record = "server %s %s weight %s maxconn %s" % (data["record"]["server"], \
                                                    data["record"]["server"], \
                                                    data["record"]["weight"], \
                                                    data["record"]["maxconn"])
    record_list = fetch(data["backend"])

    if not record or record not in record_list:
        print("\033[33:1m无此条记录\033[0m")
        return
    else:
        record_list.insert(0,backend_data)
        record_list.remove(record)
        with open("haproxy配置文件.txt","r")as f_read,\
                open("haproxy配置文件_new.txt","w")as f_write:
            tag =False
            has_writed=False
            for r_line in f_read:
                if r_line.strip()==backend_data:
                    tag=True
                    continue
                if tag and r_line.startswith("frontend"):
                    tag=False
                if not tag:
                    f_write.write(r_line)
                else:
                    if not has_writed:
                        for new_line in record_list:
                            if new_line.startswith("backend"):
                                f_write.write(new_line+"\n")
                            else:
                                f_write.write("%s%s\n" %(" "*8,new_line))
                        has_writed=True
    os.rename("haproxy配置文件.txt","haproxy配置文件bak.txt")
    os.rename("haproxy配置文件_new.txt", "haproxy配置文件.txt")
    os.remove("haproxy配置文件bak.txt")

def fix(data):
    backend_title = "backend %s" % (data[0]["backend"])
    old= "server %s %s weight %s maxconn %s" % (data[0]["record"]["server"], \
                                                    data[0]["record"]["server"], \
                                                    data[0]["record"]["weight"], \
                                                    data[0]["record"]["maxconn"])
    new = "server %s %s weight %s maxconn %s" % (data[1]["record"]["server"], \
                                                 data[1]["record"]["server"], \
                                                 data[1]["record"]["weight"], \
                                                 data[1]["record"]["maxconn"])
    fetch_list = fetch(data[0]["backend"])
    if not fetch_list or old not in fetch_list:
        print(
            "\033[33:1m无此条记录\033[0m"
        )
    else:
        remove(data[0])
        add(data[1])



if __name__=='__main__':
    msg='''
    1：查询
    2：添加
    3：删除
    4：修改
    5：退出
    '''
    menu_dic={
        "1":fetch,
        "2":add,
        "3":remove,
        "4":fix,
        "5":exit
    }
    while True:
        print(msg)
        choice=input("操作>>:")
        if len(choice)==0 or choice not in menu_dic:continue
        if choice=="5":break

        data=input("数据>>:").strip()
        if choice !="1":
            data=eval(data)
        menu_dic[choice](data)