n = int(input("Enter a number: "))

factorial = 1

if n < 0:
    print("Factorial is not possible")
else:
    for i in range(1, n + 1):
        factorial = factorial * i

    print("Factorial:", factorial)