mima = input("请输入密码")
sum_ascll = 0
str_ascll = ""
for i in mima:
    a = ord(i)
    sum_ascll += a
    str_ascll += str(a)
    fanzhuan = str_ascll[::-1]
    jieguo = int(fanzhuan) + sum_ascll
print("加密后的结果为：", jieguo)
