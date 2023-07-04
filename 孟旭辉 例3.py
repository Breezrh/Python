shengao = float(input("请输入身高（m）"))
tizhong = float(input("请输入体重（kg）"))
BMI = tizhong / (shengao * shengao)
print("您的BMI值是", BMI)
if BMI < 18.5:
    print("您的体重过轻")
elif 18.5 <= BMI < 23.9:
    print("您的体重正常")
elif 23.9 <= BMI <= 27:
    print("您的体重过重")
elif 27 < BMI <= 32:
    print("您的体重过于肥胖")
else:
    print("您的体重令人惊叹")
