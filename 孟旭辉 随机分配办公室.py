import random

ban_gong_shi = [[], [], []]
jiao_shi = ['孙浩', '李二', '张三', '李四', '王五', '赵六', '刘航', '董欣']
for i in range(len(jiao_shi)):
    ban_gong_shi[random.randint(0, 2)].append(jiao_shi[i])
print(ban_gong_shi[:])
