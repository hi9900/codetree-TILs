n = int(input())
cnt = 0
while 1:
    if n >= 1000:
        print(cnt)
        break
    
    if n % 2:
        n = n * 2 + 2
    else:
        n = n * 3 + 1

    cnt += 1