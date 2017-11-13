#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/23
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)
sys.path.append(BASE_DIR)

from src.moudles import Admin
from src.moudles import School
from src.moudles import Teacher
from src.moudles import Course
from src.moudles import Classes
from src.moudles import Course_to_teacher
from src.moudles import Score
from src.moudles import Student

def create_school():
    try:
        name = input("输入学校名称：").strip()
        addr = input("输入学校地址：").strip()
        # print('33')
        school_list = [(obj.name, obj.addr) for obj in School.get_all_obj_list()]
        # school_list = [(obj.name, obj.addr) for obj in School.get_all_obj_list()]

        # print('44')
        # print(school_list)
        if (name,addr) in school_list:
            raise Exception('\033[33;1m[%s][%s]已经存在，不可重复创建\033[0m' %(name,addr))
        obj =School(name,addr)
        obj.save()
        status = True
        error = ''
        data='\033[33;1m[%s][%s]校区 创建成功\033[0m' %(obj.name,obj.addr)
    except Exception as e:
        status=False
        error = str(e)
        data = ''
    return {'status':status,'error':error,'data':data}


def show_school():
    for obj in School.get_all_obj_list():
        print('\033[35;1m学校[%s] 地址[%s] 创建日期[%s]\033[0m'.center(60,'-') \
              %(obj.name,obj.addr,obj.create_time))


def create_teacher():
    try:
        name = input("输入老师姓名：").strip()
        level = input("输入等级：").strip()
        teacher_list=[obj.name for obj in Teacher.get_all_obj_list()]
        if name in teacher_list:
            raise Exception('\033[33;1m[%s]已经存在，不可重复创建\033[0m' %(name))
        obj =Teacher(name,level)
        # print(obj.name,obj.addr)
        # print('bf save')
        obj.save()
        status=True

        # print('bf error')
        error = ''
        # print("bf data")
        data='\033[35;1m老师[%s]等级[%s] 创建成功\033[0m' %(obj.name,obj.level)
    except Exception as e:
        status=False
        error = str(e)
        data = ''
    return {'status':status,'error':error,'data':data}

def show_teacher():
    for obj in Teacher.get_all_obj_list():
        print('\033[35;1m老师[%s] 等级[%s] 创建日期[%s]\033[0m'.center(60,'-') \
              %(obj.name,obj.level,obj.create_time))


def create_course():
    try:
        print('创建课程'.center(60,'='))
        school_list = School.get_all_obj_list()
        for k,obj in enumerate(school_list):
            print(k,obj,obj.addr)
        sid = int(input('请输入学校：'))
        school_obj = school_list[sid]

        name = input("输入课程名称：").strip()
        price = input("输入课程价格：").strip()
        period = input("输入课程周期：").strip()

        course_list=[(obj.name,obj.nid.uuid) for obj in Course.get_all_obj_list()]#uuid???
        if (name,school_obj.nid.uuid) in course_list:
            raise Exception('\033[33;1m[%s]已经存在，不可重复创建\033[0m' %name)
        obj =Course(name,price,period,school_obj.nid)
        obj.save()
        status=True
        error = ''
        data='\033[33;1m课程[%s] 价格[%s] 周期[%s]创建成功\033[0m' %(obj.name,obj.price,obj.period)
    except Exception as e:
        status=False
        error = str(e)
        data = ''
    return {'status':status,'error':error,'data':data}

def show_course():
    for obj in Course.get_all_obj_list():
        print('\033[33;1m[%s] [%s]校区 [%s]课程 价格[%s] 周期[%s]\033[0m'.center(60, '-') \
              % (obj.school_nid.get_obj_by_uuid().name, obj.school_nid.get_obj_by_uuid().addr, \
                 obj.name, obj.price, obj.period))

def create_course_to_teacher():
    """
    self.course_nid = course_nid
    self.teacher_nid = teacher_nid
    :return:
    """
    try:
        #get teacher list
        teacher_list = Teacher.get_all_obj_list()
        for k,obj in enumerate(teacher_list):
            print(k,obj.name)
        tid = int(input('请输入老师：'))
        teacher_obj = teacher_list[tid]

        #get course list
        course_list = Course.get_all_obj_list()
        for k, obj in enumerate(course_list):
            print(k,obj.name)
        cid = int(input('请输入课程：'))
        course_obj = course_list[cid]
        print(course_obj.nid.get_obj_by_uuid().name)
        #course_list = [(obj.name, obj.school_nid.uuid) for obj in Course.get_all_obj_list()]  # uuid???
        course_to_teacher_list = [(obj.course_nid,obj.teacher_nid) for obj in Course_to_teacher.get_all_obj_list()]
        # print(course_to_teacher_list)
        for (course_obj.nid,teacher_obj.nid) in course_to_teacher_list:
            raise Exception('\033[33;1m[%s]  [%s]已经存在，不可重复创建\033[0m' % (obj.course_nid.get_obj_by_uuid().name, \
                                                                        obj.teacher_nid.get_obj_by_uuid().name))
        obj = Course_to_teacher(course_obj.nid,teacher_obj.nid)
        obj.save()
        status=True
        error = ''
        data = '\033[33;1m课程[%s] 老师[%s] 创建成功\033[0m' % (course_obj.name, teacher_obj.name)

    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_course_to_teacher():
    # print('1')
    for obj in Course_to_teacher.get_all_obj_list():
        """
        self.nid = identifier.Course_to_teacherNid(self.db_path)
        self.course_nid = course_nid
        self.teacher_nid = teacher_nid"""
        # print(obj.nid,obj.course_nid,obj.teacher_nid)
        print(obj.course_nid.get_obj_by_uuid().name,obj.teacher_nid.get_obj_by_uuid().name)
        # print('\033[33;1m[%s] [%s]校区 [%s]班级 学费[%s] 课程老师对应表[%s]\033[0m'.center(60, '-') \
        #       % (obj.school_nid.get_obj_by_uuid().name, obj.school_nid.get_obj_by_uuid().addr, \
        #          obj.name, obj.tuition, obj.course_to_teacher_list))

def create_classes():
    """
    self.name = name
        self.tuition = tuition
        self.school_nid = school_nid
        self.course_to_teacher_list = course_to_teacher_list
    :return:
    """
    try:
        print('创建班级'.center(60,'='))
        #获取学校信息
        school_list = School.get_all_obj_list()
        for k,obj in enumerate(school_list):
            print(k,obj,obj.addr)
        sid = int(input('请输入学校：'))
        school_obj = school_list[sid]
        #显示课程，老师
        print("课程，老师列表".center(60,'-'))

        # course_to_teacher_list=[(obj.nid,obj.course_nid.get_obj_by_uuid().name,obj.teacher_nid.get_obj_by_uuid().name) for obj in Course_to_teacher.get_all_obj_list()]
        course_to_teacher_list=Course_to_teacher.get_all_obj_list()
        for k,obj in enumerate(course_to_teacher_list):
            print(k,obj.course_nid.get_obj_by_uuid().name,obj.teacher_nid.get_obj_by_uuid().name)
        c_t_tid=int(input('请输入课程：'))
        course_to_teacher_obj=course_to_teacher_list[c_t_tid]
        # show_course_to_teacher()


        # for obj in Course_to_teacher.get_all_obj_list():
        #     course_to_teacher_nid_list = [(obj.course_nid,obj.teacher_nid)]
        #     course_to_teacher_list = [(obj.course_nid.get_obj_by_uuid().name,obj.teacher_nid.get_obj_by_uuid().name)]
        #     print(course_to_teacher_list)
        # for i in course_to_teacher_list:
        #     print(i)
        #     print('\n')

        # course_list = Course.get_all_obj_list()
        # print("课程列表".center(60,'-'))
        # for k,obj in enumerate(course_list):
        #     print(k,obj.name)
        # cid = int(input('请输入课程：'))
        # course_obj = course_list[cid]
        #
        # teacher_list = Teacher.get_all_obj_list()
        # print("老师列表".center(60,'-'))
        # for k, obj in enumerate(teacher_list):
        #     print(k, obj.name)
        # tid = int(input('请输入老师：'))
        # teacher_obj = teacher_list[tid]
        # print(course_obj.nid,teacher_obj.nid)
        # for obj in course_to_teacher_list:
        #     print(obj)
        # ret = (course_obj.nid,teacher_obj.nid) in course_to_teacher_nid_list
        # course_to_teacher_nid=None
        # if ret:
        #     for obj in Course_to_teacher.get_all_obj_list():
        #         if obj.course_nid==course_obj.nid and obj.teacher_nid==teacher_obj.nid:
        #             course_to_teacher_nid=obj.nid
        # else:
        #     # print("输入的课程/老师有误")
        #     raise Exception('\033[33;1m输入的课程/老师有误\033[0m')
        name = input("输入班级名称：").strip()
        tuition = input("输入学费：").strip()
        classes_list=[obj.name for obj in Classes.get_all_obj_list()]#uuid???
        if name in classes_list:
            raise Exception('\033[33;1m班级[%s] 学费[%s]已经存在，不可重复创建\033[0m' %(name,tuition))
        obj =Classes(name,tuition,school_obj.nid,course_to_teacher_obj.nid)
        obj.save()
        status=True
        error = ''
        data='\033[33;1m班级[%s] 学费[%s]创建成功\033[0m' %(obj.name,obj.tuition)
    except Exception as e:
        status=False
        error = str(e)
        data = ''
    return {'status':status,'error':error,'data':data}

def show_classes():
    """
        self.name = name
        self.tuition = tuition
        self.school_nid = school_nid
        self.course_to_teacher_list = course_to_teacher_list
        :return:
        """
    for obj in Classes.get_all_obj_list():
        print('\033[33;1m[%s] [%s]校区 [%s]班级 学费[%s]\033[0m'.center(60, '-') \
              % (obj.school_nid.get_obj_by_uuid().name, obj.school_nid.get_obj_by_uuid().addr, \
                 obj.name, obj.tuition))

def create_student():
    try:
        name = input("输入学生姓名：").strip()
        age = input("输入学生年龄：").strip()
        sex = input("输入学生性别：").strip()
        qq = input("输入学生QQ：").strip()
        classes_list = Classes.get_all_obj_list()
        for k,obj in enumerate(classes_list):
            print(k,obj.name)
        cid = int(input("输入班级：").strip())
        classes_obj = classes_list[cid]
        score = None
        student_list=[(obj.name,obj.age,obj.sex,obj.classes_nid) for obj in Student.get_all_obj_list()]
        # student_list=Student.get_all_obj_list()

        # for obj in student_list:
        #     print(obj)
        if (name,age,sex,classes_obj.nid) in student_list:
            # print()
            raise Exception("\033[33;1m学生[%s] 年龄[%s]  性别[%s]   班级[%s]  已存在，不能重复创建" \
                            %(name,age,sex,classes_obj.name))
        # print('bf create student')
        obj = Student(name,age,sex,classes_obj.nid,score)
        # print('bf save')
        obj.save()
        # print('af save')
        status = True
        error =""
        data = "\033[35;1m学生[%s] 年龄[%s]  性别[%s]   班级[%s] 创建成功" %(obj.name,obj.age,obj.sex,classes_obj.name)
    except Exception as e:
        status = False
        error = str(e)
        data =""
    return {'status':status,'error':error,'data':data}

def show_student():
    for obj in Student.get_all_obj_list():
        print('\033[33;1m学生[%s] 年龄[%s] 性别[%s] 成绩[%s]\033[0m'.center(60, '-') \
              # % (obj.name,obj.age,obj.sex,obj.classes_nid.get_obj_by_uuid().name, obj.score))
              % (obj.name,obj.age,obj.sex, obj.score.score_dict))

def show():
    msg = '''
            0:选项
            1:创建学校
            2:查看学校
            3:创建老师
            4:查看老师
            5:创建课程
            6:查看课程
            7:创建班级
            8:查看班级
            9:关联老师与课程
            10:创建学生
            11:查看学生
            12:退出
        '''
    print(msg)

def main():
    login()
    choice_dic = {
        '0':show,
        '1':create_school,
        '2':show_school,
        '3':create_teacher,
        '4':show_teacher,
        '5':create_course,
        '6':show_course,
        '7':create_classes,
        '8':show_classes,
        '9':create_course_to_teacher,
        '10':create_student,
        '11':show_student,
        '12':exit
    }
    show()
    # print('1')
    while True:
        choice = input("请输入选项：").strip()
        if choice not in choice_dic:continue
        ret = choice_dic[choice]()
        if ret :
            if ret['status']:
                # print('11')
                print(ret['data'].center(60,'-'))
            else:
                # print("22")
                print(ret['error'].center(60,'-'))

def login():
    while True:
        ret = Admin.login()
        if ret:
            if ret['status']:
                print(ret['data'].center(60,'-'))
                break
            # main()
            else:
                print(ret['error'].center(60,'-'))
                # continue
# show_course_to_teacher()

if __name__ == '__main__':
    main()
    # show_school()