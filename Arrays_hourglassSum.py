# Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

import sys


def calculate_sum(arr, i, j):
    return arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
           arr[i + 2][j + 2]


# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_list = []
    max = -sys.maxint
    for i in xrange(len(arr) - 2):
        for j in xrange(len(arr[0]) - 2):
            sum = calculate_sum(arr, i, j)

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
