T = {'h': 'Thursday', 'u': 'Tuesday'}
S = {'a': 'Saturday', 'u': 'Sunday'}
dict = {'t': T, 's': S, 'w': "Wednesday", 'm': 'Monday', 'f': 'Friday'}
a = input("请输入要查询的单词首字母").lower().strip()
if a in {'t', 's', 'f', 'm', 'w'}:
    if dict[a] == T or dict[a] == S:
        b = input("请输入第二个字符").lower().strip()
        if b in {'u', 'h', 'a'}:
            print(dict[a][b])
        else:
            print("请输入正确的字母")
    else:
        print("请输入正确的字母")
