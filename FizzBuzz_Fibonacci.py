def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    res = [0] * n
    res[0] = 1
    res[1] = 1

    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2]
        fizz_buzz(res[i])
    print res


def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print n, "FizzBuzz"
    elif n % 3 == 0:
        print n, "Fizz"
    elif n % 5 == 0:
        print n, "Buzz"
    else:
        print n


fibonacci(17)
