#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 参考http://www.runoob.com/python/python-lists.html
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = ['math']


# 合并
def mathAdd():
    list3 = list1 + list2 + ['a']
    list4 = list2 * 3
    print list3, list4


def contain():
    isIn = 'chemistry' in list1
    print isIn
    isIn = 'chemistry' not in list1
    print isIn


# 列表解析
def listparse():
    a, b, c, d = list1
    print a


def crud():
    list2.append("b")
    print list2
    # count 统计某个元素在列表中出现的次数
    print list2.count('math2')
    del list2[1]
    print list2
    list2.extend(['152', 12])
    print list2
    list2.insert(1, 'x')
    print list2
    list2.remove('x')
    print list2
    i = list2.index('math')
    print i
    if ("math2" in list2):
        print list2.index('math2')
    else:
        print "not in "


def foreach():
    for x in list1[0:-1]:
        print x

print 'xrange'
for x in xrange(10, 20):
    print x

print 'range'
for x in range(10, 20):
    print x