n = int(input())

sum_a, ans = 0, "N"
for i in range(1, n):
    if n % i == 0:
        sum_a += i

    if sum_a > n:
        print(ans)
        break
    
if sum_a == n:
    print("P")