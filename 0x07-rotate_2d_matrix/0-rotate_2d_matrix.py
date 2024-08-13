#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    lm = len(matrix)
    for j in range(int(lm / 2)):
        k = (lm - j - 1)
        for m in range(j, k):
            y = (lm - 1 - m)
            tmp = matrix[j][m]
            matrix[j][m] = matrix[y][j]
            matrix[y][j] = matrix[k][y]
            matrix[k][y] = matrix[m][k]
            matrix[m][k] = tmp
