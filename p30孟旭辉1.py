a=int(input("请输入一个三位数"))
ge=a%10
shi=a//10%10
bai=a//100
if ge**3+shi**3+bai**3==a:
    print(a,"是水仙花数")
else:
    print(a,"不是水仙花数")