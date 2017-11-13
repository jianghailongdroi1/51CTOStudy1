#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/23

from lib import commons
import pickle,os

class Nid:
    def __init__(self,role,db_path):
        role_list = [
            'admin','teacher','school',"course",'course_to_teacher','classes','student'
        ]
        if role not in role_list:
            raise Exception('角色定义有误，选项为：%s' %(",".join(role_list)))
        self.uuid =commons.create_uuid()
        self.db_path = db_path
        self.role = role

    def __str__(self):
        return self.uuid

    def get_obj_by_uuid(self):

        for filename in os.listdir(self.db_path):
            if filename == self.uuid:
                file_path = os.path.join(self.db_path, self.uuid)
                with open(file_path,'rb') as f:
                    return pickle.load(f)
        return None


class AdminNid(Nid):
    def __init__(self,db_path):
        super(AdminNid,self).__init__('admin',db_path)
        # print('121')
class SchoolNid(Nid):
    def __init__(self,db_path):
        super(SchoolNid,self).__init__('school',db_path)
    # pass

class TeacherNid(Nid):
    def __init__(self,db_path):
        super(TeacherNid,self).__init__('teacher',db_path)
    # pass

class CourseNid(Nid):
    def __init__(self,db_path):
        super(CourseNid,self).__init__('course',db_path)
    # pass

class Course_to_teacherNid(Nid):
    def __init__(self,db_path):
        super(Course_to_teacherNid,self).__init__('course_to_teacher',db_path)
    # pass

class ClassesNid(Nid):
    def __init__(self,db_path):
        super(ClassesNid,self).__init__('classes',db_path)
    # pass

class StudentNid(Nid):
    def __init__(self,db_path):
        super(StudentNid,self).__init__('student',db_path)
    # pass