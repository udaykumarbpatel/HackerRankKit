def longest_prefix(arr):
    if len(arr) == 1:  # rule out trivial case
        return arr[0]

    prefix = arr[0]

    for s in arr[1:]:
        while s[:len(prefix)] != prefix and len(prefix):
            prefix = prefix[:len(prefix)-1]
        if not prefix:
            break

    print prefix


arr = ["flower", "flow", "flight", "uday"]
longest_prefix(arr)
