#!/bin/python

# Complete the rotLeft function below.
def rotLeft(a, d):
    return a


if __name__ == '__main__':
    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)
    print result