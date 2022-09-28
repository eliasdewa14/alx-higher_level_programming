#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    my_new_list = my_list.copy()
    return (list(map(lambda item: item * number, my_new_list)))
