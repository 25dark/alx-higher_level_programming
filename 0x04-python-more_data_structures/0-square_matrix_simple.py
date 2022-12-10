#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    squared_matrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    # Iterate over the rows and columns of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Compute the square of the value of the input matrix
            squared_matrix[i][j] = matrix[i][j] ** 2

    # Return the new matrix
    return squared_matrix
