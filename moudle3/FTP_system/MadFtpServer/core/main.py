#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/26
import optparse,socketserver
from conf import settings
from core.ftp_server import FTPHandler

class ArgvHandler(object):
    def __init__(self):
        self.parser = optparse.OptionParser()

        (options,args) = self.parser.parse_args()
        self.verify_args(options,args)

    def verify_args(self,options,args):
        """校验并调用相应的功能"""
        if hasattr(self,args[0]):
            func = getattr(self,args[0])
            func()
        else:
            self.parser.print_help()

    def start(self):
        print("start".center(60,'-'))
        server = socketserver.ThreadingTCPServer((settings.Host,settings.PORT),FTPHandler)
        server.serve_forever()


