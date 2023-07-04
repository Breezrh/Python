def jia(x, y):
    add = x + y
    return add


def jian(x, y):
    sub = x - y
    return sub


def cheng(x, y):
    ride = x * y
    return ride


def chu(x, y):
    div = x / y
    return div


num1 = int(input("请输入第一个数字"))
a = int(input("请选择运算符号：" + "\n" + "1、+" + '\n' +
              "2、-" + "\n" +
              "3、x" + "\n" +
              "4、/" + '\n'))
num2 = int(input("请输入第二个数字"))
if a == 1:
    print(f'结果为{jia(num1, num2)}')
elif a == 2:
    print(f'结果为{jian(num1, num2)}')
elif a == 3:
    print(f'结果为{cheng(num1, num2)}')
elif a == 4:
    if num1 != 0:
        print(f'结果为{chu(num1, num2)}')
    else:
        print('0不能当被除数')
