#!/usr/bin/python3
for num in range(0, 100):
    if (num < 10):
        zero = 0
        print(f"{zero}{num},", end =" ")
    else:
        print(f"{num}", end = "")
        if num != 99:
            print(", ", end = "")
        else:
            print("")