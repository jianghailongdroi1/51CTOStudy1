#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/19

import logging

from logging import handlers

#create logger
logger = logging.getLogger("TEST")

log_file="fileSize.log"

#create file handler and set level to error
fh = handlers.RotatingFileHandler(filename=log_file,maxBytes=10,backupCount=3,encoding="utf-8")
fh.setLevel(logging.ERROR)

#设置不同格式
fh_formatter=logging.Formatter("%(asctime)s %(filename)s:%(lineno)d - %(levelname)s %(message)s")
# ch_formatter=logging.Formatter("%(asctime)s %(filename)s:%(lineno)d %(moudle)s %(funcname)s- %(levelname)s %(message)s")
fh.setFormatter(fh_formatter)
# ch.setFormatter(ch_formatter)

#添加hander
logger.addHandler(fh)
# logger.addHandler(ch)

logger.warning("warning..........")
logger.error("error.......")
