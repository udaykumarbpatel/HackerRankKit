def sum_is_zero(arr):
    if len(arr) < 2:
        return None

    if len(arr) == 2:
        if arr[0] + arr[1] == 0:
            return True
        else:
            return False

    res = set()
    for i in arr:
        if i in res:
            return True
        else:
            res.add(0 - i)

    return False


print sum_is_zero([1, 3, 4, 5, 6, 7, 4, 5, 6, 6, 7, 7])
