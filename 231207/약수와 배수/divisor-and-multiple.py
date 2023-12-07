n = int(input())
data = list(map(int, input().split()))
k = int(input())

a, b = 0, 0
for d in data:
    # k의 약수
    if k % d == 0:
        a += d
    # k의 배수
    if d % k == 0:
        b += d
    
print(a, b, sep="\n")