#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = 0
        for num in my_list:
            if num >= max:
                max = num
        return max
    else:
        return None
