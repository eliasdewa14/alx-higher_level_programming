#!/usr/bin/python3
import sys

n = len(sys.argv)
sum = 0
for i in range(1, n):
     sum += int(sys.argv[i])
print("{}".format(sum))
