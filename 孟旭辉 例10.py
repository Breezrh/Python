import random

suijishu = random.randint(1, 10)
a = 0
while a < 5:
    user = int(input("请猜数"))
    a += 1
    if a < 5:
        if user == suijishu:
            print("恭喜，猜数成功")
            break
        elif user > suijishu:
            print("很遗憾，猜大了", "还剩", 5 - a, "次机会")
        elif user < suijishu:
            print("很遗憾，猜小了", 5 - a, "次机会")
    else:
        print("猜数机会用完了")
        break
