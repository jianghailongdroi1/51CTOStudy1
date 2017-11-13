#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/26

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
sys.path.append(BASE_DIR)

USER_HOME = "%s/home" % BASE_DIR
LOG_HOME = "%s/log" % BASE_DIR

LOG_LEVEL = 'DEBUG'
ACCOUNT_DIR = "%s/db" % BASE_DIR

HOST = '0.0.0.0'
PORT =9999

