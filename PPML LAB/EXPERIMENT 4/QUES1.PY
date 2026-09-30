numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

largest = max(numbers)
smallest = min(numbers)

second_largest = None
second_smallest = None

for n in numbers:
    if n != largest:
        if second_largest is None or n > second_largest:
            second_largest = n

    if n != smallest:
        if second_smallest is None or n < second_smallest:
            second_smallest = n

print("Second largest:", second_largest)
print("Second smallest:", second_smallest)