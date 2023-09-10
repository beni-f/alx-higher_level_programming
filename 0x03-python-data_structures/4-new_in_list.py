#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list[:]
    if idx < len(temp) and idx >= 0:
        temp[idx] = element
    return temp
