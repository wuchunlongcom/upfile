#-*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.test import TestCase
#
import os
print(os.system('[ "x$(find ./ -name admin.py)" == "x" ]')) #256   文件存在
print(os.system('[ "x$(find ./ -name admin.py1)" == "x" ]')) #0    文件不存在
print(os.system('[ false ]'))  #0
print(os.system('[ "x$(find ./ -name static)" == "x" ]')) #256     目录存在
print(os.system('[ "x$(find ./ -name static1)" == "x" ]')) #0      文件不存在
print(os.system('[ "x$(diff forms.py forms2.py)" != "x" ] ')) #256 forms1.py 与 forms2.py相同
print(os.system('[ "x$(diff forms1.py forms2.py)" != "x" ] ')) #0  forms1.py 与 forms2.py不同




