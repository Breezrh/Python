# def ok(x):
#     if 2 >= x > 0:
#         return 1
#     else:
#         return ok(x - 1) + ok(x - 2)
#
#
# while True:
#     a = int(input('请输入要计算的数字'))
#     print(f'计算结果为：{ok(a)}')

memo = {1: 1, 2: 1}


def ok(x):
    if x in memo:
        return memo[x]
    else:
        memo[x] = ok(x - 1) + ok(x - 2)
        print(memo[x], '=', ok(x - 1), '+', ok(x - 2))
        return memo[x]


while True:
    a = int(input('请输入要计算的数字'))
    print(f'计算结果为：{ok(a)}')
