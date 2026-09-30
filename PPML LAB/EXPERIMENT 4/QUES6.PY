def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not possible")
else:
    print("Factorial:", factorial(number))