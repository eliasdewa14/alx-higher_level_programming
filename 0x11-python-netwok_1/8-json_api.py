#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

from sys import argv
import requests

if __name__ == '__main__':
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]
    req = requests.post('http://0.0.0:5000/search_user', data={'q': q})
    try:
        r = req.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
