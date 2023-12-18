while 1:
    b, h, c = map(str, input().split())
    print(int(b) * int(h))

    if c == "C" or c == "c":
        break