#!/usr/bin/python3
"""a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter, and
finally displays the body of the response
"""

from sys import argv
import requests


if __name__ == '__main__':
    email = {'email': argv[2]}
    req = requests.post(argv[1], data=email)
    print(req.text)
