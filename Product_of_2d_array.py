a = [[1, 2, 3], [4, 5, 6]]
b = [[1, 2, 3], [4, 5, 6], [2, 3, 4]]


def product_of_array(a, b):
    if len(a[0]) != len(b):
        return "Not Possible"

    c = [[0] * (len(b[0])) for i in range(len(a))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    print c


product_of_array(a, b)
