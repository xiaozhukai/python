# coding:utf8
passline = 60


def func(val):
    passline = 90
    #id属性
    print('%x'%id(val))

    if val >= passline:
        print ('pass')
    else:
        print ('failed')

    def in_func():
        print (val)

    # 返回原对象89
    in_func()
    #函数内部返回函数对象
    return in_func

# 返回最大数值
def Max(val1, val2):
    return max(val1, val2)

#接收这个参数
f = func(89)
#调用接收的这个参数
f()#in_func



# print (max(90, 100))
