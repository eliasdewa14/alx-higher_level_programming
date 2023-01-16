"""This function finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    length = len(list_of_integers)
    if length == 0:
        return
    if (length == 1 or (length == 2 and list_of_integers[0] >=
                        list_of_integers[1])):
        return list_of_integers[0]
    if (length == 2 and list_of_integers[0] < list_of_integers[1]):
        return list_of_integers[1]

    half = length // 2
    maximum = list_of_integers[half]
    if maximum > list_of_integers[half - 1]:
        return maximum
    elif maximum < list_of_integers[half - 1]:
        return find_peak(list_of_integers[:half])
    else:
        return find_peak(list_of_integers[half:])
