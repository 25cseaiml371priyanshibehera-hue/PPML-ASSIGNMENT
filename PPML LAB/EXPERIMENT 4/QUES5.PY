def even_numbers(numbers):
    result = []

    for n in numbers:
        if n % 2 == 0:
            result.append(n)

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("Original list:", numbers)
print("Even values:", even_numbers(numbers))