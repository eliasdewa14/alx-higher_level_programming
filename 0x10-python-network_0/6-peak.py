#!/usr/bin/python3
"""This function finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    length_list = len(list_of_integers)
    if length_list == 0:
        return None
    if length_list == 1:
        return list_of_integers[0]
    elif length_list == 2:
        return max(list_of_integers)
    half = int(length_list // 2)
    maximum_of_list = list_of_integers[half]
    if maximum_of_list > list_of_integers[half - 1]:
        return maximum_of_list
    elif maximum_of_list < list_of_integers[half - 1]:
        return find_peak(list_of_integers[:half])
    else:
        return find_peak(list_of_integers[half + 1:])
