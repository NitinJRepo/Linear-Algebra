import numpy as np
from scipy import sparse

# Create a matrix
matrix = np.array([[1, 2],
[1, 2],
[1, 2]])

print("matrix: ", matrix)

# Create a sparse matrix
matrix = np.array([[0, 0],
[0, 1],
[3, 0]])

# Create compressed sparse row (CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix)

print("compressed sparse row (CSR) matrix: \n", matrix_sparse)

# Create larger matrix
matrix_large = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
						[3, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Create compressed sparse row (CSR) matrix
matrix_large_sparse = sparse.csr_matrix(matrix_large)
# View original sparse matrix
print("original sparse matrix: \n", matrix_sparse)

# View larger sparse matrix
print("large sparse matrix: \n", matrix_large_sparse)
