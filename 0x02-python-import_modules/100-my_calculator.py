#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    dic_operator = {"+": add, "-": sub, "*": mul, "/": div}

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op not in list(dic_operator.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, dic_operator[op](a, b)))
