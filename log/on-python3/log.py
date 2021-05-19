#!/usr/bin/env python
# -*- coding:utf8 -*-


import logging
import logging.handlers

# logging初始化工作

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt = '%Y-%m-%d  %H:%M:%S %a',  #注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                    filename="haolog.log")

# log级别：FATAL、ERROR、WARN、INFO、DEBUG。后面的打印得多
logging.error("error log abc")
logging.info("info log efg")
