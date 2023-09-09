#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    counter = len(my_list) - 1
    for i in my_list:
        i = my_list[counter]
        counter -= 1
        print("{}".format(i))
