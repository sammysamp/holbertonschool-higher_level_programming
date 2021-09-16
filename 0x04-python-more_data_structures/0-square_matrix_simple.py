#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = matrix.copy()
    for i in range(len(newmatrix)):
        newmatrix[i] = list(map(lambda n: n ** 2, newmatrix[i]))
    return newmatrix
