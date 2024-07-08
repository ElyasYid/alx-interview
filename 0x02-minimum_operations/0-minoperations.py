#!/usr/bin/python3
""" Minimum Operations"""


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    next = 'H'
    jok = 'H'
    fd = 0
    while (len(jok) < n):
        if n % len(jok) == 0:
            fd += 2
            next = jok
            jok += jok
        else:
            fd += 1
            jok += next
    if len(jok) != n:
        return 0
    return fd
