numbers = [1, 2, 3, 4, 5]

words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

result_list = list(map(lambda x: words[x], numbers))

numbers_tuple = (1, 2, 3, 4, 5)

result_tuple = tuple(map(lambda x: words[x], numbers_tuple))

print("List:", numbers)
print("Converted list:", result_list)

print("Tuple:", numbers_tuple)
print("Converted tuple:", result_tuple)