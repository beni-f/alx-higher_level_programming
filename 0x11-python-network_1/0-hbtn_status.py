#!/usr/bin/python3
"""
	What's my status? #0
"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as url:
	url_read = url.read()
	print('Body response:')
	print('\t- type: {}'.format(type(url_read)))
	print('\t- content: {}'.format(url_read))
	print('\t- utf8 content: {}'.format(url_read.decode('utf-8')))