#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/18

import random
checkcode=""

# for i in range(4):
#     current=random.randint(0,9)
#     checkcode+=str(current)
# print(checkcode)
for i in range(4):
    current=random.randrange(0,9)
    if current ==i:
        tmp=chr(random.randint(65,90))
    else:
        tmp=random.randint(0,9)
    checkcode+=str(tmp)
print(checkcode)
#     print(current)


