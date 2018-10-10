# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

def one_plus(digits):
    if len(digits) == 0:
        return 0

    last = len(digits) - 1
    carry = 0
    while True:
        if digits[last] != 9:
            digits[last] += 1
            break
        else:
            digits[last] = 0
            if last == 0:
                digits.insert(0, 1)
                break;
        last -= 1
    return digits


print one_plus([1, 2, 3])
print one_plus([4, 3, 2, 1])
print one_plus([1, 2, 9])
print one_plus([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])
