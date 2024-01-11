#!/usr/bin/python3
"""
    Response header value #0
"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as url:
    print(url.headers['X-Request-Id'])