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
    for line in result[:10]:
        print(line.get('sha'), end=": ")
        print(line.get('commit').get('author').get('name'))
