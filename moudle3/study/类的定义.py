#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/19

class Dog(object):
    def __init__(self,name):#构造函数
        self.name=name
    def sayhi(self):#类的方法
        print("hello,i am a dog %s." %(self.name))

d=Dog("alex")
d.sayhi()

