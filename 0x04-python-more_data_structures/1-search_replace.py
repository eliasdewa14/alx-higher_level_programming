#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = my_list.copy()
    for i in my_new_list:
        if i == search:
            my_new_list[my_new_list.index(i)] = replace
    return my_new_list
