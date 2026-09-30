list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

result = list(map(lambda a, b, c: a + b + c, list1, list2, list3))

print("First list:", list1)
print("Second list:", list2)
print("Third list:", list3)
print("Result:", result)