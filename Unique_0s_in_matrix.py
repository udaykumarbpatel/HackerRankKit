input_matrix = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0]]


def mark_unique(input_matrix, i, j, visited):
    a, b = i, j

    while b < len(input_matrix[a]) and input_matrix[a][b] == 0:
        visited[a][b] = 1
        b += 1

    c, d = i, j

    while c < len(input_matrix) and input_matrix[c][d] == 0:
        while d < b and input_matrix[c][d] == 0:
            d += 1
        if d == b:
            for f in range(c, b):
                visited[c][f] = 1
        c += 1

    return visited


def find_unique_0_s(input_matrix):
    print input_matrix
    visited = [[0] * len(input_matrix[0]) for i in range(len(input_matrix))]
    count = 0;
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[0])):
            if input_matrix[i][j] == 0:
                if visited[i][j]:
                    pass
                else:
                    count += 1
                    visited = mark_unique(input_matrix, i, j, visited)

    print count


find_unique_0_s(input_matrix)
