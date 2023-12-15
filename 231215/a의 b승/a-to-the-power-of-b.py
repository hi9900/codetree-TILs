a, b = map(int, input().split())

# a를 b번 곱한다.
prod = 1
for _ in range(b):
    prod *= a

print(prod)
# print(a ** b)