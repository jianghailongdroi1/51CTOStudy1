#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/19

import logging,time

from logging import handlers

#create logger
logger = logging.getLogger("TEST")

log_file="Timelog.log"

#create file handler and set level to error
fh = handlers.TimedRotatingFileHandler(filename=log_file,when="S",interval=5,backupCount=3,encoding="utf-8")
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
time.sleep(2)
logger.error("error.......")
logger.error("error.......")
logger.error("error.......")
