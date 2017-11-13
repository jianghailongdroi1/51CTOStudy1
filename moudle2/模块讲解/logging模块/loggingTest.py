#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/19

import logging

logging.basicConfig(filename="app.log",
                    level=logging.DEBUG,
                    format="%(asctime)s %(process)d %(filename)s:%(lineno)d %(moudle)s %(funcname)s- %(levelname)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p")
logging.info("test info")
logging.debug("test debug")
logging.error("test error")
logging.warning("test warning")
logging.critical("test critical")
