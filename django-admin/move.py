import os

f = open('html.htm')
a = f.tell()
print a
help(f.tell)

c = f.read(3)
b = f.tell()
print b, c
help(f.tell)

a = unicode.encode(u"慕课", 'utf-8')
print a
