#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/26

import socket
import os,json
import optparse
class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option('-s','--server',dest ='server',help='ftp server ip_addr')
        parser.add_option('-P','--port',type="int",dest ='port',help='ftp server port ')
        parser.add_option('-p','--password',dest ='password',help='password ')
        parser.add_option('-u','--username',dest ='username',help='username')
        self.options ,self.args = parser.parse_args()
        self.verify_args()
        self.make_connection()

    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.host,self.options.port))



    def verify_args(self):
        """校验参数合法性"""
        # print(options)
        # print(args)
        # print(type(options))    #<class 'optparse.Values'>不是字典
        if self.options.username and self.options.password:
            """用户名和密码都为空"""
            pass
        else:
            if self.options.username is None or self.options.password is None:
                raise Exception('\033[33;1m用户名和密码必须同时输入\033[0m')

        if self.options.server and self.options.port:
            print(self.options)
            if self.options.port > 0 and self.options.port < 65535:
                return True
            else:
                raise Exception("host port must in 0-65535")

    def authenticate(self):
        """用户认证"""
        retry_count=0
        while retry_count <3:
            username = input("username:").strip()
            username = input("username:").strip()
            self.get_auth_result(self,username,password)

    def get_auth_result(self,username,password):
        data = {'action':'auth',
                'username':username,
                'password':password}
        self.sock.send(json.dumps(data).encode())
        self.get_response()

    def get_response(self):
        """得到服务器端回复"""
        data = self.sock.recv(1024)
        data = json.loads(data)
        print("response:",data)



    def interactive(self):
        if self.authenticate():
            print("auth sucess")
# print('1')
a=FTPClient()