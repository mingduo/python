#!/usr/bin/env python
# -*- coding: utf-8 -*-
tuple1=('a',1,3)
tuple2='a,a,b',
list1=['a','b',1]


def type():
    print type(tuple2)



def isin():
    isIn = 'a' in tuple2
    print isIn


def mathAdd():
    print  tuple1 + tuple2
    print  tuple2 * 5


def totuple():
    tuple3 = tuple(list1)
    print tuple3


def max():
    print max(tuple1)

#不可变元祖
def curd():
    print tuple1.count('a')
    print  tuple1.index('a')


def foreach():
    for x in tuple1[0:]:
        print x

#参数解析
def tupleparse():
    a, b, c = tuple1
    print a



