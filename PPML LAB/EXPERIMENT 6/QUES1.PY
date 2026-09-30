numbers = [1, 3, 5, 1, 3, 2, 5, 4, 2, 1]

groups = []

for number in numbers:
    if number not in [group[0] for group in groups]:
        group = []

        for n in numbers:
            if n == number:
                group.append(n)

        groups.append(group)

print("Original list:", numbers)
print("Grouped matrix:")

for row in groups:
    print(row)