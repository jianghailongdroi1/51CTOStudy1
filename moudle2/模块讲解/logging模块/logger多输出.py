#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/19

import logging

#create logger
logger = logging.getLogger("TEST-LOG")
logger.setLevel(logging.DEBUG)

#create console handler and set level to warning
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

#create file handler and set level to error
fh = logging.FileHandler("log_file.txt",encoding="utf-8")
fh.setLevel(logging.ERROR)

#设置不同格式
fh_formatter=logging.Formatter("%(asctime)s %(filename)s:%(lineno)d - %(levelname)s %(message)s")
ch_formatter=logging.Formatter("%(asctime)s %(filename)s:%(lineno)d %(moudle)s %(funcname)s- %(levelname)s %(message)s")
fh.setFormatter(fh_formatter)
ch.setFormatter(ch_formatter)

#添加hander
logger.addHandler(fh)
logger.addHandler(ch)

logger.warning("warning..........")
logger.error("error.......")
