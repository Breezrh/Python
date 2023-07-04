def hanoi_tower(n, A, B, C):
    if n == 1:
        print(f"移动圆盘 {n} 从 {A} 到 {C}")
        return 1
    else:
        step1 = hanoi_tower(n - 1, A, C, B)
        print(f"移动圆盘 {n} 从 {A} 到 {C}")
        step2 = 1
        step3 = hanoi_tower(n - 1, B, A, C)
        return step1 + step2 + step3


n = int(input('请输入圆盘数量'))
step = hanoi_tower(n, 'A', 'B', 'C')
print(f"总共需要移动 {step} 步")
