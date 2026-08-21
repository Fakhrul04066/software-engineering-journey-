import numpy as np

# One-dimensional array
a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Element of 2 to 4 index:- ", a1[2:5])

print("Element of 1 to 5 skipping 1 each time:- ", a1[1:5:2])

print("Reverse:- ", a1[-1:-5:-1])

print("First to last and skip 1:- ", a1[::2])


# Two-dimensional array
a2 = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("\nTwo Dimensional Array:")
print(a2)

# First row
print("First row:- ", a2[0])

# Second row
print("Second row:- ", a2[1])

# Element from row 1, column 2
print("Element at row 1, column 2:- ", a2[1, 2])

# First two rows
print("First two rows:-")
print(a2[0:2])

# First two columns
print("First two columns:-")
print(a2[:, 0:2])

# Elements from row 0 to 1 and column 1 to 2
print("Selected rows and columns:-")
print(a2[0:2, 1:3])

# Skip one column
print("Skip one column:-")
print(a2[:, ::2])

# Reverse rows
print("Reverse rows:-")
print(a2[::-1])

# Reverse columns
print("Reverse columns:-")
print(a2[:, ::-1])