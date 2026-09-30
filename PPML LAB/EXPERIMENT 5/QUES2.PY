data = {
    "Apple": 25,
    "Banana": 40,
    "Mango": 60,
    "Orange": 30
}

maximum_key = max(data, key=data.get)

print("Dictionary:", data)
print("Key with maximum value:", maximum_key)
print("Maximum value:", data[maximum_key])