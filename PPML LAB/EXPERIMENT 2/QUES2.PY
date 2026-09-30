number = input("Enter a 5 digit number: ")

print("Digits at odd positions:")

for i in range(0, 5, 2):
    print(number[i])