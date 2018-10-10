def sum_of_three_num(arr):
    n = len(arr)
    found = False
    arr.sort()
    res = []
    for i in range(0, n - 1):
        l = i + 1
        r = n - 1
        x = arr[i]
        while l < r:
            if x + arr[l] + arr[r] == 0:
                res.append([x, arr[l], arr[r]])
                l += 1
                r -= 1
                found = True
            elif x + arr[l] + arr[r] < 0:
                l += 1
            else:
                r -= 1

    if found:
        return res
    else:
        return []


#     arr.sort()
#
#     for z in range(len(arr)):
#         res = sum_of_two_num(arr, 0, z)
#         if res:
#             return res
#
#     return None
#
#
# def sum_of_two_num(arr, k, z=None):
#     l = 0
#     r = len(arr) - 1
#     res = []
#     k = k - arr[z] if arr[z] else k
#     found = False
#     while l < r:
#         if l == z:
#             l += 1
#         if r == z:
#             r -= 1
#         if arr[l] + arr[r] == k:
#             found = True
#             res.append((arr[l], arr[r], arr[z]))
#             l += 1
#         elif arr[l] + arr[r] < k:
#             l += 1
#         else:
#             r -= 1
#
#     if found:
#         return res
#     else:
#         return None


print sum_of_three_num([0, -1, 2, -3, 1])
print sum_of_three_num([-1, 0, 1, 2, -1, -4])
