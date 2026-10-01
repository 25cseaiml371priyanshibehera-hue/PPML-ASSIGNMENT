import numpy as np
ones_array = np.ones((2, 3))
zeros_array = np.zeros((2, 3))
empty_array = np.empty((2, 3))
print("Ones:")
print(ones_array)
print("Zeros:")
print(zeros_array)
print("Empty:")
print(empty_array)
arr = np.array([[1, 2, 3],[4, 5, 6]])
print("\nArray Properties:")
print("Shape of array:", arr.shape)
print("Number of dimensions:", arr.ndim)
print("Size of array:", arr.size)
print("Data type:", arr.dtype)
print("Item size:", arr.itemsize)

reshaped = arr.reshape(3, 2)

print("\nReshaped array:")
print(reshaped)

arr1 = np.array([1, 2, 3])

copy_arr1 = arr1.copy()
view_arr1 = arr1.view()

print("\nOriginal:", arr1)
print("Copy:", copy_arr1)
print("View:", view_arr1)

arr2 = np.array([1, 2])
arr3 = np.array([3, 4])

concatenated = np.concatenate((arr2, arr3))

print("\nConcatenated array:", concatenated)

arr4 = np.array([5, 2, 9, 1])

print("Sorted array:", np.sort(arr4))
