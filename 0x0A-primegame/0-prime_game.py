#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    mw = 0
    bw = 0

    for n in nums:
        r_set = list(range(1, n + 1))
        p_set = primes_in_range(1, n)

        if not p_set:
            bw += 1
            continue

        isMariaTurn = True

        while True:
            if not p_set:
                if isMariaTurn:
                    bw += 1
                else:
                    mw += 1
                break

            sp = p_set.pop(0)
            r_set.remove(sp)

            r_set = [x for x in r_set if x % sp != 0]

            isMariaTurn = not isMariaTurn

    if mw > bw:
        return "Winner: Maria"

    if mw < bw:
        return "Winner: Ben"

    return None


def is_prime(n):
    """Returns True if n is prime, else returns False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returns list of prime numbers between start and end (inclusive)."""
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes
