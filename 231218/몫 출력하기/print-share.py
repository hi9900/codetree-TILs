cnt = 0
while 1:
    n = int(input())
    if n % 2:
        continue
    print(n//2)
    cnt += 1
    if cnt == 3:
        break