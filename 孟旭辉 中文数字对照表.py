daxie = ("零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖")
num = input("请输入要换算0~9的数字")
for i in range(len(num)):
    print(daxie[int(num[i])], end="")