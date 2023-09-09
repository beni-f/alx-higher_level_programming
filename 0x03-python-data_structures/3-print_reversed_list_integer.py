#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    counter = len(my_list) - 1
    temp = my_list
    for i in range(len(my_list)):
        temp[i] = my_list[counter]
        counter -= 1
        print("{}".format(my_list[i]))

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
