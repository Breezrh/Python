set1 = set()
dict = {}
for i in range(100):
    a = int(input("1、查看生词列表" + "\n" +
                  "2、背单词" + "\n" +
                  "3、添加新单词" + "\n" +
                  "4、删除单词" + "\n" +
                  "5、清空生词表" + "\n" +
                  "6、退出生词本" + "\n"))
    if a == 1:
        if len(set1) == 0:
            print("生词本内容为空")
        else:
            print(f'所有生词如下{set1}' + "\n")
    elif a == 2:
        if len(set1) == 0:
            print("生词本为空")
        else:
            ran = set1.pop()
            set1.add(ran)
            while True:
                word = input(f'请输入{ran}的翻译')
                if word == dict[ran]:
                    print('答对了')
                    break
                else:
                    print('再想想')
    elif a == 3:
        new_word = input("请输入新单词")
        new_word_mean = input("请输入对应的翻译")
        set1.add(new_word)
        dict.update({new_word: new_word_mean})
        print(dict)
    elif a == 4:
        word = input("请输入要删除的生词")
        if word in set1:
            set1.remove(word)
            dict.pop(word)
            print("删除成功")
        else:
            print("删除的生词不存在")
    elif a == 5:
        if len(set1) == 0:
            print("生词本内容为空")
        else:
            set1.clear()
            dict.clear()
            print("生词本清空成功")
    elif a == 6:
        break
    else:
        print("请输入正确的编号")
