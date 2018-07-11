#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://www.178linux.com/97342
from os import  path
import os
print
p=path.join('fileTest')
print  p
print  path.exists(p)
print  path.split(p)
newPath=os.getcwd()+'\\'+path.basename(p)

print  path.dirname(newPath)
print  path.basename(newPath)
print path.splitdrive(p)
print path.abspath('fileTest')
