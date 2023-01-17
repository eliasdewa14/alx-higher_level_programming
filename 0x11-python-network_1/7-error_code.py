#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response
"""

from sys import argv
import requests


if __name__ == '__main__':
    req = requests.get(argv[1])
    print('Error code: {}'.format(
        req.status_code)) if req.status_code >= 400 else print(req.text)
