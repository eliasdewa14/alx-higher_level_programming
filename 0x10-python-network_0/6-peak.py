#!/usr/bin/python3
"""This function finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    length = len(list_of_integers)
    if list_of_integers == []:
        return None
    while True:
        if length == 1:
            return list_of_integers[0]
        elif length == 2:
            return max(list_of_integers)
        half = int(length // 2)
        maximum = list_of_integers[half]
        if maximum > list_of_integers[half - 1]:
            return maximum
        elif maximum < list_of_integers[half - 1]:
            return find_peak(list_of_integers[:half])
        else:
            return find_peak(list_of_integers[half + 1:])
