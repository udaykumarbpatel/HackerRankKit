# 1
# 6
# 1 5 1 0 6 0
# 7
from collections import defaultdict


def sum_of_four(arr, n, X):
    aux = defaultdict(list)
    for i in range(0, n, 1):
        for j in range(i, n, 1):
            if i != j:
                aux[arr[i] + arr[j]].append((i, j))

    for item in aux:
        diff = X - item

        if diff == item:
            if len(aux.get(item)) > 2:
                return True

        if diff in aux:
            old = aux.get(item)
            new = aux.get(diff)
            for old_t in old:
                for new_t in new:
                    if len(tuple(set(old_t).intersection(set(new_t)))) == 0:
                        return True
    return False


T = int(raw_input())

for i in xrange(T):
    n = int(raw_input())
    a = map(int, raw_input().rstrip().split())
    X = int(raw_input())
    print sum_of_four(a, n, X)