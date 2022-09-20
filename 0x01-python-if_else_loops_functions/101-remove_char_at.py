#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i in str:
        if 0 <= n <= len(str):
            if i == str[n]:
                continue
            else:
                new_str += i
        else:
            new_str += i
    return new_str
