#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/23
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
sys.path.append(BASE_DIR)
from src import identifier
import pickle,os,time
from conf import settings
class BaseModel:
    def save(self):
        file_path= os.path.join(self.db_path,str(self.nid))
        f = open(file_path,"wb")
        pickle.dump(self,f)
        f.close()

    @classmethod
    def get_all_obj_list(cls):
        # print('in the get_all_obj_list()')
        ret = []
        for filename in os.listdir(cls.db_path):
            if filename:
                file_path = os.path.join(cls.db_path, filename)
                f = open(file_path, 'rb')
                ret.append(pickle.load(f))
                f.close()
        return ret

class Admin(BaseModel):
    db_path = settings.ADMIN_DB
    def __init__(self,username,password):
        self.nid = identifier.AdminNid(self.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')

    @staticmethod
    def login():
        try:
            name = input("请输入用户名：").strip()
            pas = input("请输入密码：").strip()
            for obj in Admin.get_all_obj_list():
                if obj.username == name and obj.password == pas:
                    status =True
                    error =''
                    data = '\033[35;1m登陆成功\033[0m'
                    break
            else:
                raise Exception("\033[33;1m用户名或密码错误\033[0m")
        except Exception as e:
            status =False
            error = str(e)
            data =''
        return {'status':status,'error':error,'data':data}

class School(BaseModel):
    db_path = settings.SCHOOL_DB
    def __init__(self,name,addr):
        self.nid = identifier.SchoolNid(self.db_path)
        self.name = name
        self.addr = addr
        self.__income = 0
        self.create_time = time.strftime('%Y-%m-%d %X')

    def __str__(self):
        return self.name

class Teacher(BaseModel):
    db_path = settings.TEACHER_DB
    def __init__(self,name,level):
        # print('db')
        self.nid = identifier.TeacherNid(self.db_path)
        # print('name')
        self.name = name
        # print('level')
        self.level = level
        # print('account')
        self.__account = 0
        # print('time')
        self.create_time = time.strftime('%Y-%m-%d %X')

class Course(BaseModel):
    db_path = settings.COURSE_DB
    def __init__(self,name,price,period,school_nid):
        self.nid = identifier.CourseNid(self.db_path)
        self.name = name
        self.price = price
        self.period = period
        self.school_nid = school_nid

class Course_to_teacher(BaseModel):
    db_path = settings.COURSE_TO_TEACHER_DB
    def __init__(self,course_nid,teacher_nid):
        self.nid = identifier.Course_to_teacherNid(self.db_path)
        self.course_nid = course_nid
        self.teacher_nid = teacher_nid

    def get_course_to_teacher_list(self):
        ret = self.get_all_obj_list()
        # if ret:

        res = [(obj.course_nid.get_obj_by_uuid(),obj.teacher_nid.get_obj_by_uuid()) \
               for obj in ret]
        return res

class Classes(BaseModel):
    db_path = settings.CLASSES_DB
    def __init__(self,name,tuition,school_nid,course_to_teacher_list):
        self.nid = identifier.ClassesNid(self.db_path)
        self.name = name
        self.tuition = tuition
        self.school_nid = school_nid
        self.course_to_teacher_list = course_to_teacher_list

class Score:
    def __init__(self,nid):
        self.nid=nid  #nid指学生的id
        self.score_dict={}

    def set(self,course_to_teacher_nid,number):
        self.score_dict[course_to_teacher_nid]=number

    def get(self,course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid)

class Student(BaseModel):
    db_path = settings.STUDENT_DB
    def __init__(self,name,age,sex,qq,classes_nid):
        self.nid = identifier.ClassesNid(self.db_path)
        self.name = name
        self.age = age
        self.sex = sex
        self.qq = qq
        self.classes_nid = classes_nid
        self.score = Score(self.nid)


    # pass


