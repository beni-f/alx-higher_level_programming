#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, value in enumerate(i):
            if j == len(i) - 1:
                print("{:d}".format(value))
            else:
                print("{:d}".format(value), end=" ")
