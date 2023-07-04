x=int(input("请输入第一短边的长度"))
y=int(input("请输入第二短边的长度"))
z=int(input("请输入第三长边的长度"))
if x+y<=z :
    print("两短边之和必须大于第三边")
else:
    q=(x+y+z)/2
    S=(q*(q-x)*(q-y)*(q-z))**0.5
    print("三角形的面积：",S)