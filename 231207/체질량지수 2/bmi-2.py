h, w = map(int, input().split())

ans = w * 100**2 // h**2
print(ans)
if ans >= 25:
    print('Obesity')