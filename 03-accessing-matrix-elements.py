import numpy as np

matrix = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]])

print("Select the first two rows and all columns of a matrix:")
print(matrix[:2,:])

print("Select all rows and the second column:")
print(matrix[:,1:2])

print("select an element of third row and second column:")
print(matrix[2,1])

print("select all rows of the last column:")
print(matrix[:,-1])

print("select all the columns except last one:")
print(matrix[:,:-1])
