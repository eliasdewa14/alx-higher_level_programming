#!/usr/bin/python3

def multiple_returns(sentence):
    res = []
    res.append(len(sentence))
    res.append(sentence[0])
    return (tuple(res))
