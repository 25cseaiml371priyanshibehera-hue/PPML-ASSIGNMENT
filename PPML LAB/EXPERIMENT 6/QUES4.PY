numbers = [10, 20, 30, 40, 50]

number = int(input("Enter number to search: "))

check = lambda x: x == number

found = False

for n in numbers:
    if check(n):
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")