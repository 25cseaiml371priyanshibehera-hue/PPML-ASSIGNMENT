numbers = [10, -5, 0, 20, -10, 0, 5]

positive = len(list(filter(lambda x: x > 0, numbers)))
negative = len(list(filter(lambda x: x < 0, numbers)))
zero = len(list(filter(lambda x: x == 0, numbers)))

total = len(numbers)

print("Positive ratio:", positive / total)
print("Negative ratio:", negative / total)
print("Zero ratio:", zero / total)