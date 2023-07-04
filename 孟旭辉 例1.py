for i in range(1000,9999):
    qian = int(i//1000)
    bai=int(i%1000/100)
    shi=int(i%100/10)
    ge=int(i%10)
    if qian==ge and bai==shi:
        print(i)