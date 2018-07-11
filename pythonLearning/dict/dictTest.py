#!/usr/bin/env python
# -*- coding: utf-8 -*-
#参考http://www.178linux.com/95428
#参考http://www.runoob.com/python/python-dictionary.html


#init
dict1 = {'a': 1, 'b': 2, 'b': '3'}
dict2=dict(a=1,b=4)


def get():
    if dict1.has_key('a1'):
        print dict1['a1']
    else:
        print "default:"+str(dict1['a'])

    isget = dict1.get('a1')
    print  isget == None


def update():
    print dict1
    dict1.update(b='xx')
    print  dict1


def remove():
    print  dict1.pop('b', 'default')
    print dict1.pop('b', 'default')


def fromkeys():
    d = dict.fromkeys(range(5))
    print d
    d = dict.fromkeys(range(5), 0)
    print d


def foreach():
    for k in dict1:
        print k
    for k in dict1.keys():
        print k
    for k in dict1.values():
        print k

    # 返回的是二元元组
    for k in dict1.items():
        print k
    # 使用封装和解构
    for k, j in dict1.items():
        print k, j
    for k, j in dict1.iteritems():
        print k, j


