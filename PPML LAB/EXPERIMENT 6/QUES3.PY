matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")

for row in matrix:
    print(row)

transpose = []

for j in range(3):
    row = []

    for i in range(3):
        row.append(matrix[i][j])

    transpose.append(row)

print("Transpose:")

for row in transpose:
    print(row)