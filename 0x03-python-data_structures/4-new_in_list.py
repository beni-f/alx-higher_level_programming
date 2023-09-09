#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list
    if idx < len(temp) and idx >= 0:
        temp[idx] = element
    return temp
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)