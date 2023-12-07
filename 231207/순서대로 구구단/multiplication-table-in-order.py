a, b = map(int, input().split())

r = 1 if a < b else -1
e = b+1 if a < b else b-1

for i in range(1, 10):
    for j in range(a, e, r):
        print(f'{j} * {i} = {j*i}', end="  ")
    print()