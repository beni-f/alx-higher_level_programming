#!/usr/bin/python3
def pow(a, b):
    prod = 1
    for i in range(b):
        prod *= a
    return prod

print(pow (3, 10))