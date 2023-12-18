n = int(input())
cnt = 0

while 1:
    if n == 1:
        break

    if n % 2:
        n = n * 3 + 1
    else:
        n //= 2

    cnt += 1

print(cnt)