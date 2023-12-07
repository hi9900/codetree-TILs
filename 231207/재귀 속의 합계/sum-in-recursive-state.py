a = int(input())

ans = 0
while 1:
    ans += a
    a -= 1

    if a == 0:
        break

print(ans)