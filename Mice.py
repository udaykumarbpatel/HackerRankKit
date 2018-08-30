def is_safe(matrix, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and matrix[x][y] != 0:
        return True

    return False
    pass


def solve_maze_util(matrix, x, y, sol):
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True

    if is_safe(matrix, x, y):
        sol[x][y] = 1

        count = int(matrix[x][y])
        print count,x,y
        for i in range(0, count, 1):
            if matrix[x + i][y] == 0:
                matrix[x + i][y] = 1
            if solve_maze_util(matrix, x + 1, y, sol):
                return True
            if matrix[x][y + i] == 0:
                matrix[x][y + i] = 1
            if solve_maze_util(matrix, x, y + 1, sol):
                return True

        sol[x][y] = 0
        return False


def print_solution(sol):
    for s in sol:
        for a in s:
            print a,
        print
    pass


def mice_to_destination(matrix):

    sol = [[0 for j in range(len(matrix))] for i in range(len(matrix))]

    if not solve_maze_util(matrix, 0, 0, sol):
        print("-1");
        # return

    print_solution(sol)
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
