a, b = map(int, input().split())

while 1:
    if a > b:
        break

    print(a, end=" ")
    
    if a % 2:
        a *= 2
    else:
        a += 3