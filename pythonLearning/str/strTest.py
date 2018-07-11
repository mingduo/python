#!/usr/bin/env python
# -*- coding: utf-8 -*-
#参考http://www.178linux.com/94042
#http://www.runoob.com/python/python-strings.html
str1 = ' Hello World! '
str2 = "Python Runoob"


def mathAdd():
    print str1 + str2
    print str1 * 2


def substr():
    print str1[1:]
    for x in str1[2:-2]:
        print x


def isin():
    print '0' in str1


list1=['a','b']
print ':'.join(list1)

print str1.split(" ")
print str1.replace('H','h')
print  str1.strip()

#在指定区间[start,end)从左至右查找子串sub，找到返回索引，没有则返回-1
print  str1.find('ello')
#在指定区间[start,end)从左至右查找子串sub，找到返回索引，没有则抛出ValueError
print  str1.index('ello')

print  len(str1)

print str1.endswith("ld")
#类似 java log.info
print '{},wo{}'.format('hi','2')