list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D", "E"]

result = []

for i in range(5):
    result.append(list1[i])
    result.append(list2[i])

print("Combined list:", result)