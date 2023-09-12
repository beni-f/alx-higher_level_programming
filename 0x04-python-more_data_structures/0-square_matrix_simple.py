#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    size = len(matrix)
    new_matrix = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            if i < len(matrix) and j < len(matrix[i]):
                new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
