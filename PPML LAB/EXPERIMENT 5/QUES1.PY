dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

dict3 = {}

dict3.update(dict1)
dict3.update(dict2)

print("First dictionary:", dict1)
print("Second dictionary:", dict2)
print("Merged dictionary:", dict3)