#coding:utf8
import time
import os

print(time.localtime(os.path.getatime('E:\\a.txt')))