n = int(input())
ans = "N"
for i in range(2, n):
    if n % i == 0:
        ans = "C"
        break

print(ans)