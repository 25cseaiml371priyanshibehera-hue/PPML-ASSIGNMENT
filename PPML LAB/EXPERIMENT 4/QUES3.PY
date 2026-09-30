numbers = []

for i in range(20):
    n = int(input("Enter number: "))
    numbers.append(n)

for i in range(20):
    if numbers[i] % 2 != 0:
        numbers[i] = numbers[i] + 5

print("Updated list:", numbers)