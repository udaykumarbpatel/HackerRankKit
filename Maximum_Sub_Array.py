import sys


def max_sub_array(nums):
    max_sum = -sys.maxint
    max_ending_here = 0

    for i in nums:
        max_ending_here += i
        if max_sum < max_ending_here:
            max_sum = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0

    print max_sum


max_sub_array([-2, -3, -4, -11, -2, -31, -5, -4])
max_sub_array([-2, -3, 4, -1, -2, 1, 5, -3])


