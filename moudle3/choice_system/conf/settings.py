#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/23

import os

#选课系统变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
ADMIN_DB = os.path.join(BASE_DIR,"db","admin")
SCHOOL_DB = os.path.join(BASE_DIR,"db","school")
TEACHER_DB = os.path.join(BASE_DIR,"db","teacher")
COURSE_DB = os.path.join(BASE_DIR,"db","course")
COURSE_TO_TEACHER_DB = os.path.join(BASE_DIR,"db","course_to_teacher")
CLASSES_DB = os.path.join(BASE_DIR,"db","classes")
STUDENT_DB = os.path.join(BASE_DIR,"db","student")




# STUDENTS_DATABASE = {
#     "db_tool":"file_storage",   #文件存储，这里可拓展成数据库形式的
#     "name":"students",          #db下的文件名
#     "path":"%s/db/accounts" % BASE_DIR
# }
# TEACHERS_DATABASE = {
#     "db_tool":"file_storage",   #文件存储，这里可拓展成数据库形式的
#     "name":"teachers",          #db下的文件名
#     "path":"%s/db/accounts" % BASE_DIR
# }