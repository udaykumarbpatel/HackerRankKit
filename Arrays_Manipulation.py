# Input
# a b k
# 1 5 3
# 4 8 7
# 6 9 1
#
# Output
# idx	 1 2 3  4  5 6 7 8 9 10
# 	    [0,0,0, 0, 0,0,0,0,0, 0]
# 	    [3,3,3, 3, 3,0,0,0,0, 0]
# 	    [3,3,3,10,10,7,7,7,0, 0]
# 	    [3,3,3,10,10,8,8,8,1, 0]



#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for q in queries:
        for i in range(q[0], q[1]):
            arr[i] = arr[i] + q[2]
        arr[q[1]] = arr[q[1]] + q[2]
    print max(arr)



if __name__ == '__main__':
    nm = raw_input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))
    result = arrayManipulation(n, queries)
