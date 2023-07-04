import time
xinghao=50
print("="*24+"加载开始"+"="*25)
for i in range(xinghao+1):
    xinghao1="*"*i
    dian="~"*(xinghao-i)
    baifenbi=(i/xinghao)*100
    print("\r{:.0f}%[{}{}]".format(baifenbi,xinghao1,dian),end="")
    time.sleep(0.3)
print("\n"+"="*24+"加载结束"+"="*25)