n = int(input())

for i in range(1, n+1):
    # 온전수가 아님
    if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9):
        continue
    print(i, end=" ")