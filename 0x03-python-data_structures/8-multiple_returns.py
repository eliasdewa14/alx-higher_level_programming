#!/usr/bin/python3
def multiple_returns(sentence):
    res = []
    res.append(len(sentence))
    if sentence == "":
        res.append("None")
    else:
        res.append(sentence[0])
    return (tuple(res))
