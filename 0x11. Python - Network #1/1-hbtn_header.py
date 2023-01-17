#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header of
the response
"""
from sys import argv
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen(argv[1]) as request:
        print(request.headers.get('X-Request-Id'))
