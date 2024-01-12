#!/usr/bin/python3
"""
    Error code #0
"""
import urllib.request, urllib.error
import sys
if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as url:
            print(url.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
