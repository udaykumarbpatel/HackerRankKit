def remove_element_array(arr, dele):
    if len(arr) == 0:
        return 0

    start, end = 0, len(arr) -1

    while start <= end:
        if arr[start] == dele:
            arr[start], arr[end], end = arr[end], arr[start], end-1
        else:
            start += 1

    return start


remove_element_array([0,1,2,2,3,0,4,2,2,4,6,2,1,3,2,2,6,3,2,6,8,3,1,2,2,5,7,9,2], 2)