#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """Return Pascals Triangle upto n"""
    pas = []
    if n <= 0:
        return pas
    pas = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(len(pas[i - 1]) - 1):
            cnt = pas[i - 1]
            tmp.append(pas[i - 1][j] + pas[i - 1][j + 1])
        tmp.append(1)
        pas.append(tmp)
    return pas
