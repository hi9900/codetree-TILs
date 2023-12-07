g = int(input())
a = int(input())

gender = 'M' if g == 0 else 'W'

if gender == 'M':
    ans = 'M' if a >= 19 else 'B'
if gender == 'W':
    ans = 'W' if a >= 19 else 'G'

print(ans)