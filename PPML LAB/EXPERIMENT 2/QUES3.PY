number = input("Enter a number: ")

if number == number[::-1]:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")