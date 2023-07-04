# for i in range(1, 101):
#   if i % 7 == 0 or '7' in str(i):
#       print(i, end=' ')
a = 0
for i in range(1, 101):
    if i % 7 == 0 or '7' in str(i):
        print('*', end='、')
        a += 1
    else:
        print(i, end='、')
        a += 1
    if a % 10 == 0:
        print("\t")
