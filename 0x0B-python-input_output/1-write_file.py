#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
Returns the number of characters written
"""


def write_file(filename="", text=""):
    """writing on file"""

    with open(filename, 'w', encoding="utf-8") as f:
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
