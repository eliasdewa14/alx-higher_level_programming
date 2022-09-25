#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    for i in range(len(tuple_a)):
        tuple_a += (0, 0)
        tuple_b += (0, 0)
        res.append(tuple_a[i] + tuple_b[i])
    return (tuple(res))
