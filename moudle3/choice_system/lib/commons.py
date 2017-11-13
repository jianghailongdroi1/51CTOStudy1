#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/23

import uuid,hashlib,time

def create_uuid():
    return str(uuid.uuid1())

def create_md5():
    m=hashlib.md5()
    m.update(bytes(str(time.time()),encoding="utf-8"))
    return m.hexdigest()

if __name__ == "__main__":
    print(create_uuid())
    print(create_md5())
    # print("1")




