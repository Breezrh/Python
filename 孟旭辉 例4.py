print("(1)有车票，（2）没车票")
chepiao=int(input("请输入是否有车票"))
if chepiao==1:
    changdu=int(input("请输入刀子长度"))
    if changdu<10:
        print("您已通过安检，祝您旅途愉快")
    else:
        print("行李中含有违禁物品，请原地等待工作人员处理")
else:
    print("请您购买车票后上车")