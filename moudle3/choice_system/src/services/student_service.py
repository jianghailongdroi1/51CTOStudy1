#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/23
from src.services import admin_service
from src.moudles import Student

def register():
    """
    学生注册
    """
    # while True:
    print("学生注册".center(60,'-'))
    return admin_service.create_student()


"""
        try:
            name = input("输入学生姓名：").strip()
            age = input("输入学生年龄：").strip()
            sex = input("输入学生性别：").strip()
            qq = input("输入学生QQ：").strip()
            classes_list = Classes.get_all_obj_list()
            for k, obj in enumerate(classes_list):
                print(k, obj.name, obj)
            cid = int(input("输入班级：").strip())
            classes_obj = classes_list[cid]
            score = None
            student_list = [(obj.name, obj.age, obj.sex, obj.classes_nid) for obj in Student.get_all_obj_list()]
            for (name, age, sex, classes_obj.nid) in student_list:
                raise Exception(
                    "\033[43;1m学生[%s] 年龄[%s]  性别[%s]   班级[%s]  已存在，不能重复创建" % (name, age, sex, classes_obj.name))
            obj = Student(name, age, sex, classes_obj.nid, score)
            obj.save()
            status = True
            error = ""
            data = "\033[45;1m学生[%s] 年龄[%s]  性别[%s]   班级[%s] 创建成功" % (
            obj.name, obj.age, obj.sex, obj.classes_nid.get_obj_by_uuid().name)
        except Exception as e:
            status = False
            error = str(e)
            data = ""
        return {'status': status, 'error': error, 'data': data}
"""
def score():
    """
    学生查看个人成绩
    """
    name = input("请输入学生姓名：").strip()
    for obj in Student.get_all_obj_list():
        if obj.name== name:
            # print('ert')
            ret ='\033[33;1m学生[%s] 成绩[%s]\033[0m' \
              % (obj.name, obj.score.score_dict)
            print(ret)
            return ret
    raise Exception('\033[35;1m查成绩出错\033[0m')



def main():
    msg ="""
    '1':'注册'
    '2':'查看分数'
    """
    choice_dict={
        '1':register,
        '2':score
    }
    while True:
        print(msg)
        choice = input("请输入选项：").strip()
        if choice not in choice_dict:
            print("\033[33;1m输入有误\033[1m")
            continue
        else:
            ret = choice_dict[choice]()
        if ret:
            print('操作成功')
            return
        else:
            print('操作异常，请重新操作')
if __name__ == '__main__':
    main()

# def login():
#     pass
