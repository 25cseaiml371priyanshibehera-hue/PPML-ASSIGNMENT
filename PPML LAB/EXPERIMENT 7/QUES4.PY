letters = ['a', 'B', 'c', 'A', 'b', 'C', 'a']

changed = list(map(lambda x: x.swapcase(), letters))

result = []

for letter in changed:
    if letter not in result:
        result.append(letter)

print("Original list:", letters)
print("After changing case:", changed)
print("After removing duplicates:", result)