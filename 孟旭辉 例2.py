lirun=int(input("请输入利润（万）"))
if lirun<=10:
    print("奖金提成为",lirun*0.1,"万元")
elif lirun<=20:
    print("奖金提成为",1+(lirun-10)*0.075,"万元")
elif lirun <= 40:
    print("奖金提成为",1.75+(lirun-20)*0.05,"万元")
elif lirun<=60:
    print("奖金提成为",2.25+(lirun-40)*0.015,"万元")
elif lirun <= 100:
    print("奖金提成为",2.40+(lirun-60)*0.01,"万元")