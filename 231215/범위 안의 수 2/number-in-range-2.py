ans, cnt = 0, 0
for _ in range(10):
    n = int(input())

    if 0 <= n <= 200:
        ans += n
        cnt += 1

print(f'{ans} {ans/cnt:.1f}')