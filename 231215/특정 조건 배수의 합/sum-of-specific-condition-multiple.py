a, b = map(int, input().split())

ans = 0
for i in range(a, b+1):
    if i % 5 == 0:
        ans += i

print(ans)