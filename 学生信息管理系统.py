students = {}


def add(set):
    name = input("请输入学生姓名：")
    sex = input("请输入学生性别：")
    num = input("请输入学生身份证号：")
    set[name] = {'性别': sex, '身份证号': num}


def dele(set):
    if len(set) == 0:
        print("系统目录为空")
    else:
        name = input("请输入要删除的的学生的名字")
        if name in set:
            del set[name]
        else:
            print("该学生不在管理系统中")


def mod(set):
    if len(set) != 0:
        old_name = input("请输入要修改的学生姓名")
        if old_name in set:
            new_studet = set
            new_name = input("请输入新的名字")
            new_sex = input("请输入性别：")
            new_num = input("请输入身份证号：")
            new_studet[new_name] = {'性别': new_sex, '身份证号': new_num}
            del set[old_name]

        else:
            print("该学生不在管理系统中")
    else:
        print("管理系统为空")


def find(set):
    if len(set) != 0:
        name = input("请输入要查询的学生姓名：")
        a = set.get(name)
        if a:
            print('='*40)
            print('姓名：',name, set[name])
            print('='*40)
        else:
            print('该学生不在管理系统中')
    else:
        print('系统目录为空')


while True:
    a = int(input("欢迎使用学生信息管理系统，请选择功能序号：" + '\n' +
                  '1、添加学生信息' + '\n' +
                  '2、删除学生信息' + '\n' +
                  '3、修改学生信息' + '\n' +
                  '4、查找学生信息' + '\n' +
                  '5、查看系统列表' + '\n' +
                  '6、退出程序'+'\n'))
    if a == 1:
        add(students)
    elif a == 2:
        dele(students)
    elif a == 3:
        mod(students)
    elif a == 4:
        find(students)
    elif a == 5:
        if len(students) == 0:
            print("系统目录为空")
        else:
            for i in students.items():
                print(i)
    elif a == 6:
        break
