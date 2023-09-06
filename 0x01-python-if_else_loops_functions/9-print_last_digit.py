#!/usr/bin/python3
def print_last_digit(number):
    number *= -1
    if number > 0:
        print(number % 10)
