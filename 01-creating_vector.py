import numpy as np

# Create a vector as a row
vector_row = np.array([1, 2, 3, 4, 5])

print("row vector: ", vector_row)

# Create a vector as a column
vector_column = np.array([[1],
[2],
[3],
[4],
[5]])

print("column vector: ", vector_column)

# Selecting elements

print("Select third element of vector:")
print(vector_column[2])

print("Select all elements of a vector:")
print(vector_row[:])

print("Select everything up to and including the third element:")
print(vector_column[:3])

print("Select everything after the third element:")
print(vector_column[3:])

print("Select the last element:")
print(vector_column[-1])

