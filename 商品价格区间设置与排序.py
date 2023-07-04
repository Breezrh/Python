min = int(input("请输入最小价格"))
max = int(input("请输入最大价格"))
test = []
jiage = [399, 4369, 539, 288, 109, 749, 235, 190, 99, 1000]
for i in range(len(jiage)):
    if jiage[i] > min and jiage[i] < max:
        test.append(jiage[i])
        jiage[i] = min
paixu = int(input("1、价格降序排序" + "\n" + "2、价格升序排序"))
if paixu == 1:
    test.sort(reverse=True)
    print(test[:])
else:
    test.sort(reverse=False)
    print(test[:])
