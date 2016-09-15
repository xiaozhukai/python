#汉罗塔游戏
#n层数，x轴，y轴，z轴
def hanoi(n ,x , y , z):
    if n == 1:
        print(x ,'--->', z)
    else:
        hanoi(n-1 ,x ,z ,y )    #将前n-1个盘子从x移动到y上
        print(x,'--->',z)
        hanoi(n-1 ,y ,x , z)

n = int(input("请输入汉罗塔层数"))
hanoi(n , "x" , "y" , "z" )