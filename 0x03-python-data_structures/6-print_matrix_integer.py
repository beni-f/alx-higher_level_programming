#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if i != 0:
            print("")
        for j in range(len(matrix)):
            print("{}".format(matrix[i][j]), end=" ")
    print("")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

    