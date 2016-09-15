# f = open("new.txt","r")
# print(f.read())
# f.close()


f = open("new.txt","r")
# 往里面输入
for line in f:
    if "1" in line:
        print("this is the hello say hello")
    else:
        print(line)
f.close()