user = {}

while True:
    a = int(input("请输入功能序号：" + "\n" +
                  "1、添加联系人" + "\n" +
                  "2、查看通讯录" + "\n" +
                  "3、删除联系人" + "\n" +
                  "4、修改联系人" + "\n" +
                  "5、查找联系人" + "\n" +
                  "6、退出" + "\n" + "\n"))

    if a == 1:
        add_name = input("请输入联系人的姓名：")
        user.update({add_name: {'num': "", 'mail': "", 'site': ""}})
        add_num = input("请输入联系人的手机号码：")
        new_name = user[add_name]
        new_name['num'] = add_num
        add_mail = input("请输入联系人的邮箱：")
        new_name['mail'] = add_mail
        add_site = input("请输入联系人的地址:")
        new_name['site'] = add_site
        user[add_name] = new_name
        print("\n")

    elif a == 2:
        if len(user) == 0:
            print("通讯录无信息")
        else:
            for i in user.items():
                print(i)

    elif a == 3:
        if len(user) == 0:
            print("通讯录无信息")
        else:
            delete = input("请输入要删除的联系人的姓名：")
        if delete in user:
            del user[delete]
            print("删除成功")
        else:
            print("该联系人不在通讯录中")

    elif a == 4:
        old_name = input("请输入要修改的联系人的名字：")
        new_user = user
        new_name = input("请输入新的姓名:")
        new_user[new_name] = {'num': "", 'mail': "", 'site': ""}
        new_num = input("请输入新的手机号：")
        new_user[new_name]['num'] = new_num
        new_mail = input("请输入新的邮箱：")
        new_user[new_name]['mail'] = new_mail
        new_site = input("请输入新的地址")
        new_user[new_name]['site'] = new_site
        del user[old_name]
        print("修改成功！")
        for i in user.items():
            print(i)

    elif a == 5:
        select_name = input("请输入要查找的联系人姓名：")
        value = user.get(select_name)
        if value:
            print(select_name, user[select_name])
        else:
            print("该联系人不在通讯录中")

    elif a == 6:
        break
    else:
        print("请输入正确的功能序号！" + '\n')
