A, B, C, D = 0, 0, 0, 0

for _ in range(3):
    a, b = input().split()

    if a == 'Y' and int(b) >= 37:
        A += 1
    elif a == 'N' and int(b) >= 37:
        B += 1
    elif a == 'Y':
        C += 1
    else:
        D += 1

if A >= 2:
    print('E')
else:
    print('N')