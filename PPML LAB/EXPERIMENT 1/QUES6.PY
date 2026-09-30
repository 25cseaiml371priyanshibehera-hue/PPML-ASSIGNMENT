meters = int(input("Enter distance in meters: "))

kilometers = meters // 1000
remaining_meters = meters % 1000

print("Kilometers:", kilometers)
print("Remaining meters:", remaining_meters)