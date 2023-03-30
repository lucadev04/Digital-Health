numbers = [1, 2, 4, 3, 6, 10, 11, 12, 111, 112, 12345678]

for n in numbers:
    test = n/2
    test2 = str(test).split('.')[1]
    if test2 == "0":
        print(n)
    else:
        continue