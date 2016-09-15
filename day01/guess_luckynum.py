# coding:utf8
lucky_num = 19
#需要给出默认数值
input_num = 0
#统计次数
guess_count = 0

# while input_num != lucky_num  and guess_count < 3:
for i in range(3):

    input_num = int(input("Input the guess num:"))

    # if input_num == lucky_num:
    #     print("bingo!")
    #     break
    if input_num > lucky_num:
        print("the real number is smaller...")
    else:
        print("the real number is bigger...")
    guess_count += 1
    print('选择次数',guess_count)


if input_num != lucky_num:
    print("the real number is false")
else:
    print("bingo!")

