#!/usr/bin/python3
def roman_to_int(roman_string):
    ans = 0
    i = 0
    while (i < len(roman_string)):
        str1 = value(roman_string[i])
        if (i + 1 < len(roman_string)):
            str2 = value(roman_string[i + 1])
            if (str1 >= str2):
                ans = ans + str1
                i = i + 1
            else:
                ans = ans + str2 - str1
                i = i + 2
        else:
            ans = ans + str1
            i = i + 1
    return ans

def value(rom):
    if (rom == 'I'):
        return 1
    if (rom == 'V'):
        return 5
    if (rom == 'X'):
        return 10
    if (rom == 'L'):
        return 50
    if (rom == 'C'):
        return 100
    if (rom == 'D'):
        return 500
    if (rom == 'M'):
        return 1000
    return -1
