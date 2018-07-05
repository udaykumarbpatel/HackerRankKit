# 8
# 1 2 5 3 7 8 6 4
# 1 2 3 4 5 6 7 8
# 1 2 3 5 4 6 7 8
# 1 2 5 3 4 6 7 8
# 1 2 5 3 4 7 6 8
# 1 2 5 3 7 4 6 8
# 1 2 5 3 7 6 4 8
# 1 2 5 3 7 6 8 4
# 1 2 5 3 7 8 6 4
# 1 2 3 4 5 6 7 8

# !/bin/python

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    length = len(q)
    count = 0
    flag = 0
    for i in range(length - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print "Too chaotic"
            flag = 1
            break
        for j in range(max(0, q[i] - 2), i):
            if (q[j] > q[i]):
                count = count + 1
    if flag != 1:
        print count


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())
        q = map(int, raw_input().rstrip().split())
        minimumBribes(q)
