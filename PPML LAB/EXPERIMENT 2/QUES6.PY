number = int(input("Enter a 3 digit number: "))

print("Prime factors:")

factor = 2

while number > 1:
    if number % factor == 0:
        print(factor, end=" ")
        number = number // factor
    else:
        factor += 1