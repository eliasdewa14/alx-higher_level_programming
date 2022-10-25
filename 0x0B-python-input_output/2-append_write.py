#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
Returns the number of characters added
"""


def append_write(filename="", text=""):
    """appending text on a file"""

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)

    """file reading"""
    with open(filename, encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            charCount = 0
            for word in line:
                for char in word:
                    charCount += 1
            return charCount
