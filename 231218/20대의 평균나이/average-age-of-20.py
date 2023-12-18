sum_a, cnt_a = 0, 0

while 1:
    a = int(input())

    if a < 20 or a > 29:
        print(f'{sum_a / cnt_a:.2f}')
        break

    sum_a += a
    cnt_a += 1