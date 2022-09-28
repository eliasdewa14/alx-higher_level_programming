#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    total_sum = 0
    sum = 0
    for i, j in my_list:
        sum += j
        total_sum += i * j
    return total_sum / sum
