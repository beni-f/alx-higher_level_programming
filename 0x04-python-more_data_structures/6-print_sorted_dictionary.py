#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for word in sorted(a_dictionary):
        print("{}: {}".format(word, a_dictionary[word]))
