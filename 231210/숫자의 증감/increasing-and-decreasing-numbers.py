c, n = input().split()
n = int(n)
if c == 'A':
    print(*list(range(1, n+1)))
else:
    print(*list(range(n, 0, -1)))