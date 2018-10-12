from collections import defaultdict

input_list = [(1, 2), (1, 4), (1, 6), (6, 9), (9, 11), (2, 5), (12, 13), (12, 18), (2, 13)]


def find_1_0_parent(input_list):
    if len(input_list) == 0:
        return None

    nodes = set()
    data = defaultdict(list)

    for x, y in input_list:
        data[y].append(x)
        nodes.add(x)
        nodes.add(y)

    for i in data:
        print i, data[i]

    for n in nodes:
        if len(data[n]) < 2:
            print n


find_1_0_parent(input_list)
