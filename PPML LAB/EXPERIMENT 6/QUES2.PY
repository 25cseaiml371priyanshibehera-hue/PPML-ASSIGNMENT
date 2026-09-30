matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")

for row in matrix:
    print(row)

print("Row sums:")

for row in matrix:
    print(sum(row))

print("Column sums:")

for j in range(3):
    total = 0

    for i in range(3):
        total = total + matrix[i][j]

    print(total)