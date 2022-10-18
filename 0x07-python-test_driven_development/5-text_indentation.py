#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: text to indent
    Return:
        a text with two lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    space = 1
    for i in text:
        if space == 1:
            if i == ' ':
                continue
            else:
                space = 0
        if space == 0:
            if i not in [".", "?", ":"]:
                print(i, end="")
            else:
                print(i)
                print()
                space = 1
