#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    i = 0
    while (i < len(roman_string)):
        str1 = value[roman_string[i]]
        if (i + 1 < len(roman_string)):
            str2 = value[roman_string[i + 1]]
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
