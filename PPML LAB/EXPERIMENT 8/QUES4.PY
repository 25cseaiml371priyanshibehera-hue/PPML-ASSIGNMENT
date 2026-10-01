import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60]])
print("Original Array:")
print(arr)

print("\nStatistical Operations:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

print("\nSum of each column:", np.sum(arr, axis=0))
print("Sum of each row:", np.sum(arr, axis=1))

b = np.array([1, 2, 3])

print("\nArray for Broadcasting:")
print(b)

result = arr + b

print("Result after Broadcasting:")
print(result)
