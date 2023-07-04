#敏感词过滤
ciku="操"
hua=input("请输入一段话")
for i in ciku:
    if i in hua:
        hua=hua.replace(ciku,"*")
print(hua)