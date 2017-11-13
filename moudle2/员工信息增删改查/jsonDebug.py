#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/20

import json,sys,re
# reload(sys)
# sys.setdefaultencoding("utf-8")
d={"1":{"name":"Mark","age":'32','phone':'13651054608',"dept":"IT","enroll_data":"2014-04-02"},"2":{"name":"alex","age":'22','phone':'13651054609',"dept":"运维","enroll_data":"2013-04-01"}}
# # d_final=d.
# with open("information.txt","a",encoding="utf-8") as f:
#     json.dump(d,f)
# # print(help(re.compile))
# with open("information.txt","r",encoding="utf-8") as f:
#     json.loads(f.read())


# Json存储
def store(data):
    with open('information.txt', 'w') as json_file:
        json_file.write(json.dumps(data))
#
#
# Json加载
def load():
    with open('information.txt') as json_file:
        data = json.load(json_file)
        return data

def get_final_result(show_item,show_list):
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
if __name__=="__main__":
    # store(d)
    # # print(load())
    # a=get_final_result(["name","age"],{'1': {'name': 'Mark', 'age': '22', 'phone': '13651054608', 'dept': 'IT', 'enroll_data': '2013-04-01'}})
    # print(a)
    a='like'
    print(a  in [">", "=", "like"])

# for item in d:
#     print(type(item))
# def load():
#     with open('information.txt') as json_file:
#         data = json.load(json_file)
#         return data
# initial_data=load()
# print(initial_data)
