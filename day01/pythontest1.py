b = 'I love FishC.com'
b = list(b)
print(b)

c = (1,12,3,123,12,3,32,4,5,4,56)
d = [13,3,41,2,3,5,3,5,53]
print(list(c))
print(len(c))
print(len(list(c)))
print(sorted(d))
print(sorted(c))
print(reversed(d))
print(reversed(c))
print(list(enumerate(c)))
print(list(enumerate(d)))
print(list(zip(c,d)))

def MyFirstFunction(name):
    '函数定义过程中的name叫形参'
    print('--------',MyFirstFunction.__doc__)
print(MyFirstFunction('小甲鱼'))
print(print.__doc__)
