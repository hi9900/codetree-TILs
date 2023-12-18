ans = 1
for _ in range(5):
    n = int(input())
    if n % 3:
        ans = 0
        break

print(ans)