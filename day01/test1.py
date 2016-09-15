def discounts(price,rate):
    final_price = price * rate
    return final_price

old_price = float(input("请输入价格:"))
rate = float(input("请输入折扣价:"))
new_price = discounts(old_price,rate)
print("折后价格",new_price)