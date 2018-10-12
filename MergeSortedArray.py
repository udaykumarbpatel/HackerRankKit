# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]


def merge_sorted(nums1, m, nums2, n):
    if len(nums1) == len(nums2) == 1:
        nums1[0] = nums2[0]
        return nums1

    i = j = 0

    while i < m and j < n:
        if nums1[i] < nums2[j] and nums1[i] != 0:
            i += 1
        else:
            nums1.pop()
            nums1.insert(i, nums2[j])
            j += 1

    while j < len(nums2):
        nums1.pop()
        nums1.insert(i + 1, nums2[j])
        i += 1
        j += 1

    return nums1


print merge_sorted([0], 1, [1], 1)
print merge_sorted([1, 0], 2, [2], 1)
print merge_sorted([1, 0], 1, [2], 1)
print merge_sorted([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print merge_sorted([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3)
