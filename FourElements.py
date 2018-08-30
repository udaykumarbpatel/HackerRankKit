# 1
# 6
# 1 5 1 0 6 0
# 7

class Aux_Item(object):
    first = 0
    second = 0
    sum = 0

    def __init__(self, first, second, sum):
        self.first = first
        self.second = second
        self.sum = sum


def make_item(first, second, sum):
    item = Aux_Item(first, second, sum)
    return item


def aux_print(aux):
    for item in aux:
        print item.first, item.second, item.sum

def sum_of_four(arr, n, X):
    aux = []
    for i in range(0, n, 1):
        for j in range(i, n, 1):
            if i != j:
                aux.append(make_item(i, j, arr[i] + arr[j]))

    aux_print(aux)

    for i in range(0, len(aux), 1):
        f_start = aux[i].first
        s_start = aux[i].second
        u_start = aux[i].sum

        diff = X - aux[i].sum
        if diff in aux



    pass


T = int(raw_input())

for i in xrange(T):
    n = int(raw_input())
    a = map(int, raw_input().rstrip().split())
    X = int(raw_input())
    sum_of_four(a, n, X)
