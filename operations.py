import numpy as np


def multiplication(matrix1, matrix2):
    result_of_multiplication = np.dot(matrix1, matrix2)
    return result_of_multiplication


def addition(matrix1, matrix2):
    result_of_addition = np.add(matrix1, matrix2)
    return result_of_addition


def transpose(matrix):
    result_of_transpose = np.transpose(matrix)
    return result_of_transpose