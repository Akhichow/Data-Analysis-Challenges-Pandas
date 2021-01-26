for i in range(1, 101):
    count = 0
    for number in range(2, i):
        if i % number == 0:
            count += 1

    if (count == 0) and (i > 1):
        print(i, end=" ")