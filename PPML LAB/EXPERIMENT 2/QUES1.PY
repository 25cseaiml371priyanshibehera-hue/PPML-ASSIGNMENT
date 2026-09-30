percentage = int(input("Enter percentage: "))

if percentage >= 90:
    print("Grade: O")
elif percentage >= 80:
    print("Grade: E")
elif percentage >= 70:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")