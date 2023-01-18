#!/usr/bin/python3
"""a Python script that takes 2 arguments in order to solve challenge
"""

from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[1], argv[2])
    req = requests.get(url)
    result = req.json()
    for line in range(10):
        print('{}: {}'.format(
            result[line].get('sha'),
            result[line].get('commit').get('author').get('name')))
