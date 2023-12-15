a, b = map(int, input().split())

ans, cnt = 0, 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        ans += i
        cnt += 1

print(f'{ans} {ans/cnt:.1f}')