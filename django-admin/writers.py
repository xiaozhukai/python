# coding:utf8
#打开这个文件
f = open('html.htm','w')

#写入到文本中
# f.write('text write')

#写入日志
for i in range(10000):
    f.write("text write" +str(i)+ '\n')

f.flush()
f.close()
print( 'ok')
