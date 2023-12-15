n = int(input())

sum_a = 0
for i in range(1, n):
    if n % i == 0:
        sum_a += i

    if sum_a > n:
        break
    
if sum_a == n:
    print("P")
else:
    print("N")