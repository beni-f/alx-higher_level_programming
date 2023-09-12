#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        max_num = 0
        max = " "
        for word in a_dictionary:
            if a_dictionary[word] > max_num:
                max_num = a_dictionary[word]
                max = word
        return max
