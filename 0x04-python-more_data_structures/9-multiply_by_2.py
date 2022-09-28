#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_new_dic = a_dictionary.copy()
    for i in my_new_dic.keys():
        my_new_dic[i] *= 2
    return (my_new_dic)
