#!/usr/bin/env python
# -*- coding: utf-8 -*-
#re模块为高级字符串处理提供了正则表达式工具。
# 对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
#http://www.runoob.com/python3/python3-stdlib.html

#http://www.178linux.com/97337
import re

print re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
#匹配替换
print re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')