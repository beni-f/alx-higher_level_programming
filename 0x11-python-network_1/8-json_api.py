#!/usr/bin/python3
"""
    Search API
"""
import requests 
import sys

if __name__ == '__main__':
    letter = ""
    if sys.argv == 2:
        letter = sys.argv[1]
    value = {'q': letter}
    url = requests.post('http://0.0.0.0:5000/search_user', data=value)

    try: 
        resp = url.json()
        if resp == {}:
            print('No result')
        else:
            print("[{}] {}".format(resp['id'], resp['name']))
    except ValueError:
        print("Not a valid JSON")


    
