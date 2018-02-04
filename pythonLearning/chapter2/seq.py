#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __title__ = ''索引
# __author__ = 'SEELE'
# __mtime__ = '2018/2/4'
x = "123456789"
t=["323",123]
print t

#   2.2.1 ---------------第一个为0 从0开始 最后一个为-1 -2 -3 类似redis list
print x[0] + x[-1] + x[len(x) - 1]

# --------------2.2 .2分片 类似substring
def slice():
    print "分片"
    print x[0:3]
    print x[-3:-1]
    print x[1:]
    print x[:4]
    print x[:]
    # step 代表不步长，跳跃长度
    print x[::2]


# --------------分片 类似substring
slice()

#   2.2.1 输出每月的天
def printDay():
    end = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st'];
    print end[0]
    print end

# str day int(day)->int
    day = raw_input("day(0-31): ");
    print day + end[int(day) - 1];


printDay()

# 2.2.3序列相加
#相同类型可以相加
x1=[1,2,3]+[4]
print  x1

#2.2.4 乘法
x3=[]
