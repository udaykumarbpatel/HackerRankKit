from collections import defaultdict

input_list = [(1, 2), (1, 4), (1, 6), (6, 9), (9, 11), (2, 5), (12, 13), (12, 18), (2, 13)]


def dfs(data, key, path=[]):
    match = []
    for i in data:
        if key in data[i]:
            match.append(i)

    if len(match) == 0:
        result = list()
        result.append(path)
        return result
    else:
        temp_res = []
        for i in match:
            temp_path = []
            for j in path:
                temp_path.append(j)
            temp_path.append(i)
            local_res = dfs(data, i, temp_path)
            for i in local_res:
                temp_res.append(i)
        return temp_res


def least_common_ancestor(input_list, a, b):
    d = defaultdict(list)
    for x, y in input_list:
        d[x].append(y)

    for i in d:
        print i, d[i]

    res1 = dfs(d, a, [])
    res2 = dfs(d, b, [])

    print res1
    print res2

    for i in res1:
        for j in res2:
            if set(i).intersection(j):
                return True
    return False


print least_common_ancestor(input_list, 9, 13)
