favouritre = 'FishC'
for i in favouritre:
    print(i,end='')
print()

#得到集合中的每个值
member = ['小甲鱼',['小布丁','小乌龟'],'小旭旭']
for i in member:
    print(i)

#得到的是定义里面的所有数
print(list(range(5)))
print(list(iterable='小布丁'),'迭代器')

print(member[1][1])
print(dir(member))
print(member[1:4])

print(8 * (8,))
print(8 * (8))


str2 = 'xiao kai love'
print(str2.capitalize())
print(str2.casefold())
print(str2.center(20))
print(str2.count('z'))
print(str2.find('z'))


str3 = 'I\tlovemelllllll\tFishC.com!'
print(str3.expandtabs())

str4 = 'I love FishC.com'
print(str4)
print("{a} love {b}.{c}".format(a ="a",b = "FishC", c = "com"))

print("{{0}}".format("123"))

print('%c'%98)
print('%#o' %108)