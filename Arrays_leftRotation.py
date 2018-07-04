#!/bin/python

#5 4
#1 2 3 4 5


# Complete the rotLeft function below.
def rotLeft(a, d):
    d = d%len(a)
    output = []
    for i in range(d, len(a),1):
        output.append(a[i])
    for i in range(0, d, 1):
        output.append(a[i])

    return output


if __name__ == '__main__':
    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)
    print result