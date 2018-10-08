def solve_maze_util(matrix, x, y, sol):
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True

    if 0 <= x < N and 0 <= y < N and matrix[x][y] != 0:
        sol[x][y] = 1

        count = int(matrix[x][y])

        for i in range(0, count, 1):
            if solve_maze_util(matrix, x, y + i + 1, sol):
                return True
            if solve_maze_util(matrix, x + i + 1, y, sol):
                return True

        sol[x][y] = 0
    return False


def mice_to_destination(matrix):
    sol = [[0 for j in range(len(matrix))] for i in range(len(matrix))]

    if not solve_maze_util(matrix, 0, 0, sol):
        print("-1");
        return
    print
    for s in sol:
        for a in s:
            print a,
        print
    return


N = 0
T = int(raw_input())

for i in range(0, T, 1):
    N = int(raw_input())
    matrix = []
    for i in range(0, N, 1):
        lst = raw_input().split()
        matrix.append(lst)
    mice_to_destination(matrix)
