def remove_duplicate_sorted(arr):
    p1 = 0
    p2 = 1

    while p1 < len(arr) and p2 < len(arr):
        if arr[p1] == arr[p2]:
            pass
        else:
            arr[p1 + 1] = arr[p2]
            p1 += 1
        p2 += 1

    return p1 + 1


print remove_duplicate_sorted([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
