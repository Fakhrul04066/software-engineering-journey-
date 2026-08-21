import numpy as np

# 1D ARRAY SORTING
x = np.array([3, 4, 1, 5, 7])

# Sort the array in ascending order
y = np.sort(x)

print("Original 1D array:-", x)
print("Ascending order:-", y)

# Reverse the sorted array to get descending order
print("Descending order:-", y[::-1])


# 2D ARRAY SORTING
a = np.array([
    [30, 10, 20],
    [60, 50, 40],
    [90, 70, 80]
])

print("\nOriginal 2D array:")
print(a)

# axis=1 means sorting column values inside each row
row_sorted = np.sort(a, axis=1)

print("\nEach row sorted in ascending order:")
print(row_sorted)


# Sort each row in descending order
# [::, ::-1] reverses the columns of every row
print("\nEach row sorted in descending order:")
print(row_sorted[:, ::-1])


# Sort each column in ascending order
# axis=0 means sorting values vertically in each column
column_sorted = np.sort(a, axis=0)

print("\nEach column sorted in ascending order:")
print(column_sorted)


# Sort each column in descending order
# [::-1, :] reverses the rows
print("\nEach column sorted in descending order:")
print(column_sorted[::-1, :])


# Sort all elements of the 2D array
# axis=None converts the array into a 1D sorted array
all_sorted = np.sort(a, axis=None)

print("\nAll elements sorted in ascending order:")
print(all_sorted)

# Reverse the array for descending order
print("\nAll elements sorted in descending order:")
print(all_sorted[::-1])