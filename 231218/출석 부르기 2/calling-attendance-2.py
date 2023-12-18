data = ["John", "Tom", "Paul", "Sam"]
while 1:
    n = int(input())
    if n < 5:
        print(data[n-1])
    else:
        print("Vacancy")
        break