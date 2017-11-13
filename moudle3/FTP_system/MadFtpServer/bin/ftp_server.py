#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/26

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
sys.path.append(BASE_DIR)
from core import main
from core import ftp_server
if __name__ == '__main__':
    main.ArgvHandler(sys.argv)

