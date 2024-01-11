#!/usr/bin/python3
"""
    What's my status
"""
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')

print('Body response:')
print('\t- type: {}'.format(type(r.text)))
print('\t- content: {}'.format(r.text))
