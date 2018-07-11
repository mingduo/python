#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.runoob.com/python/python-date-time.html
import time
import calendar
import datetime
#seconds
print time.time()
#获取当前时间
print time.localtime(time.time())

#格式化日期
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

#类似 java8 time localdatetime localdate
def getYesterday():
    print  datetime.datetime.today()
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    print yesterday
    print yesterday.strftime("%Y-%m-%d %H:%M:%S")


#昨天
getYesterday()


def sleep():
    time.sleep(1)



def cal():
    print  calendar.month(2018, 7)




