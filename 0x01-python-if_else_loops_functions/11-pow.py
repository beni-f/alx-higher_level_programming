#!/usr/bin/python3
def pow(a, b):
    prod = 1
    if b > 0:
        for i in range(b):
                prod *= a
    else:
        b *= -1
        for i in range(b):
            prod *= 1 / a
    return prod
