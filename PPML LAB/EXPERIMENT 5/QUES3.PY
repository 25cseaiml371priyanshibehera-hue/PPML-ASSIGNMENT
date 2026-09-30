data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

result = {}
values = []

for key, value in data.items():
    if value not in values:
        values.append(value)
        result[key] = value

print("Original dictionary:", data)
print("After removing duplicate values:", result)

