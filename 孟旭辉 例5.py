print("华东地区（01），华南地区（02），华北地区（03）")
diqu=input("请输入地区编号")
zhongliang=float(input("请输入重量（kg）"))
if diqu=="01":
    if zhongliang<=3:
        print("您的费用为",13,"元")
    else:
        print("您的费用为",13+((zhongliang-3)*3))
if diqu=="02":
    if zhongliang<=3:
        print("您的费用为",12,"元")
    else:
        print("您的费用为",12+((zhongliang-3)*2))
if diqu=="03":
    if zhongliang<=3:
        print("您的费用为",14,"元")
    else:
        print("您的费用为",14+((zhongliang-3)*4))
else:
    print("请输入正确的地区编号")