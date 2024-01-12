#!/usr/bin/python3
"""
   Error code #1 
"""
import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])

    if r.ok == True:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))