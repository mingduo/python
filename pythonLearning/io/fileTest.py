#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.178linux.com/97342

def write():
    f = open('fileTest', 'a')

    try:
        f.write("hhhh")
    finally:
        f.flush()
        f.close()

#不需要try catch
def withopen ():
    f = open('fileTest', 'a')
    with f:
        f.write('123')


def read():
    global f, txt
    f = open('fileTest')
    for txt in f:
        print txt
    f.close()


def readlines():
    global f, txt
    f = open('fileTest')
    print f.name
    print f.readlines()
    for txt in f.readlines():
        print txt

readlines()

