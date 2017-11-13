#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/26

import socketserver,json
class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            # self.request.sendall(self.data.upper())
            data = json.load(self.data)
            if data.get('action') is not None:
                if hasattr(self,data.get('action')):
                    func = getattr(self,data.get('action'))
                    func(data)
            else:
                raise Exception('\033[35;1mcmd命令输入有误\033[0m')
    def __put(self,*args,**kwargs):
        pass

    def __get(self, *args,**kwargs):
        pass

    def __ls__(self, *args,**kwargs):
        pass

    def __cd__(self, *args,**kwargs):
        pass



# if __name__ == '__main__':


