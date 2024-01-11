#!/usr/bin/python3
"""
    What's my status? #0
"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as url:
    url_read = url.read()
    req = "Body response:$\n\t- type: {}$\n\t- content: {}$\n\t- utf8 content: {}$"
    print(req.format(type(url_read), url_read, url_read.decode('utf-8')))
