n = int(input("Enter N: "))

for num in range(2, n + 1):

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:

        second = num + 2

        count2 = 0

        for i in range(1, second + 1):
            if second % i == 0:
                count2 += 1

        if count2 == 2 and second <= n:
            print(num, second)