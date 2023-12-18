a, b, c = map(int, input().split())
ans = "NO"
for i in range(a, b+1):
    if i % 7 == 0:
        ans = "YES"
        break

print(ans)