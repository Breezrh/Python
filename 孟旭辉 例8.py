zhanghu = "12345"
mima = "123"
i = 0
while i < 3:
    userzhanghu = int(input("请输入账户"))
    usermima = int(input("请输入密码"))
    i += 1
    if i != 3:
        if str(userzhanghu) != zhanghu or str(usermima) != mima:
            print("用户名或密码错误", "您还有", 3 - i, "次机会")
        else:
            print("登录成功")
            break
    else:
        print("输入错误次数过多，请稍后再试")
