#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.178linux.com/97342
#http://www.runoob.com/python3/python3-os-file-methods.html
import os,sys

print  os.getcwd()
print os.name,sys.platform
print sys.path
#返回内容列表
print  os.listdir(os.getcwd())
for file in os.listdir(os.getcwd()):
    if file.find("Test")>0:
        os.chmod(file,777)
    print os.stat(file)
os.system("java")