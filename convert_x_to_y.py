def convert_x_to_y(x, y):
    if x == y:
        return 0

    if x <= 0 and y > 0:
        return "Not Possible"

    if x > y:
        return x - y

    if y % 2 == 1:
        return 1 + convert_x_to_y(x, y + 1)
    else:
        return 1 + convert_x_to_y(x, y / 2)


def bfs(x, y):
    if x <= 0 and y > 0:
        return "Not Possible"

    que = [(x, 0)]
    visited = set()

    while len(que) > 0:
        ele, pos = que.pop(0)
        if ele * 2 == y or ele - 1 == y:
            return pos + 1
        else:
            if (ele * 2) not in visited:
                que.append((ele * 2, pos + 1))
                visited.add(ele * 2)
            if (ele - 1) not in visited:
                que.append((ele - 1, pos + 1))
                visited.add(ele - 1)


x = 2
y = 11
print convert_x_to_y(x, y)
print bfs(x, y)
