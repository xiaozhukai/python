def fun(n):
    if n < 1:
        print("你输入的有误！！")
        return -1

    if n == 1 or n == 2:
        return 1
    else:
        return fun(n -1 ) + fun(n - 2)
result = fun(32)
if result != -1:
    print("总共有%d对小兔子诞生！！！" %result)