#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Marvin"
# Date: 2017/8/1

'''
三级菜单：
1. 运行程序输出第一级菜单
2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
3. 菜单数据保存在文件中
'''

menu={
    'A1':{
        'A2':{
            'A3':{
                'A4'
            }
        },
        'a2':{
            'a3':{
                'a4'
            }
        }
    },
    'B1':{
        'B2':{
            'B3':{
                'B4'
            }
        }
    },
    'C1':{
        'C2':{
            'C3':{
                'C4'
                }
            }
        }
}
level=[]
while True:
    for key in menu:
        print(key)
    choice=input('please input your chice>>').strip()
    #在一级菜单时，返回，退出程序
    if choice == 'b':
        if len(level)==0:
            break
        menu=level[-1]
        level.pop()
        # continue
    if len(choice) ==0 or choice not in menu:continue
    #存储菜单记录
    level.append(menu)
    menu=menu[choice]


