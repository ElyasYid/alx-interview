#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """function to check if data is utf-8 valid"""
    nb = 0

    ka = 1 << 7
    ku = 1 << 6

    for j in data:

        mb = 1 << 7

        if nb == 0:

            while mb & j:
                nb += 1
                mb = mb >> 1

            if nb == 0:
                continue

            if nb == 1 or nb > 4:
                return False

        else:
            if not (j & ka and not (j & ku)):
                return False

        nb -= 1

    if nb == 0:
        return True

    return False
