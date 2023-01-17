#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

from sys import argv
from requests.auth import HTTPBasicAuth
import requests


if __name__ == '__main__':
    user = 'https://api.github.com/user'
    author = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get(user, auth=author)
    print(req.json().get('id'))
