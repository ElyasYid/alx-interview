#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(c, t):
    """
    Returns: minimum number of coins needed for total.
        Returns 0 if total <= 0.
        Returns -1 if total cannot be met.
    """
    if not c or c is None:
        return -1
    if t <= 0:
        return 0
    chg = 0
    c = sorted(c)[::-1]
    for coin in c:
        while coin <= t:
            t -= coin
            chg += 1
        if t == 0:
            return chg
    return -1
