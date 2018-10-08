def sum_of_binary(a, b):
    a, b = list(a), list(b)
    res, carry = [], 0

    while a or b:
        n1 = n2 = 0
        if a:
            n1 = int(a.pop())
        if b:
            n2 = int(b.pop())

        tmp = n1 + n2 + carry
        carry = 0
        if tmp == 1 or tmp == 0:
            res.append(tmp)
        elif tmp == 2:
            res.append(0)
            carry += 1
        else:
            res.append(1)
            carry += 1
    if carry:
        res.append(carry)
    return ''.join(str(d) for d in res)[::-1]


a = "11"
b = "1"
print sum_of_binary(a, b)
