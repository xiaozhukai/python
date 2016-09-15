# coding:utf8
from asyncore import read

f = open('html.htm')

iter_f = iter(f)

#文件读取内容
content = f.read()

lines = 0


#每遍历一行就让总行数+1
for line in iter_f:

    lines += 1

print(lines)
print(content)