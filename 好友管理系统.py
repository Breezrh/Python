haoyou = []
for i in range(100):
    test = int(input("1、添加好友" + "\n" + "2、删除好友" + "\n" + "3、备注好友" + "\n" + "4、展示好友" + "\n" + "5、退出"))
    if test == 1:
        tianjia = input("请输入要添加的好友：")
        haoyou.append(tianjia)
        print("添加", tianjia, "为好友成功", end=" ")
    elif test == 2:
        shanchu = input("请输入删除好友的姓名：")
        haoyou.remove(shanchu)
        print("删除成功", end=" ")
    elif test == 3:
        chaxun = input("请输入要修改的好友姓名：")
        xiugai = input("请输入修改后的好友姓名：")
        index = haoyou.index(chaxun)
        haoyou[index] = xiugai
        print("备注成功", end=" ")
    elif test == 4:
        if len(haoyou) == 0:
            print("好友列表为空", end=" ")
        else:
            print(haoyou[:])
    elif test == 5:
        print("关闭好友系统")
        break
