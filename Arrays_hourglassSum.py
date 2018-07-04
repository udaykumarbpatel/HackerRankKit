# Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0


import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_list = []
    max = -sys.maxint
    for i in xrange(len(arr)-2):
        for j in xrange(len(arr[0])-2):
            sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                  arr[i + 2][j + 2]
            if sum > max:
                max = sum
                max_list = [arr[i][j], arr[i][j + 1], arr[i][j + 2], arr[i + 1][j + 1], arr[i + 2][j],
                            arr[i + 2][j + 1], arr[i + 2][j + 2]]
    return max_list


if __name__ == '__main__':

    arr = []
    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    print result
