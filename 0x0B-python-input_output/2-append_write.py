#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)

Returns the number of characters added
"""


def append_write(filename="", text=""):
    """appending text on a file

    Arg:
        text: the text to write to the file
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
