import random
result = random.randint(1,10)
print("=============欢迎来到小开工作室=============")
while(True):
    temp = input("猜数字小游戏：")
    guess = int(temp)

    if guess == result:
        print("恭喜你猜对了！")
        break
    else:
        if guess > result:
            print("你猜的值大了,请重新输入")
        else:
            print("你猜的值小了,请重新输入")


