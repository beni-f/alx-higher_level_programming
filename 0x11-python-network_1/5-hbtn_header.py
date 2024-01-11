#!/usr/bin/python3
"""
    Response header value #1
"""
import sys
import requests

r = requests.get(sys.argv[1])

print(r.headers['X-Request-Id'])