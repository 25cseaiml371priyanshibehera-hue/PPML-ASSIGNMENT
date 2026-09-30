text = input("Enter a string: ")

words = text.split()

print("Even length words:")

for word in words:
    if len(word) % 2 == 0:
        print(word)