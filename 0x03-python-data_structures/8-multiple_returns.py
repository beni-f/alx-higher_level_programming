#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = 0
        for letter in sentence:
            length += 1
        return length, sentence[0]
    else:
        return None
