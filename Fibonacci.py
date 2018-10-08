def fibonacci_dp(n):
    if n <= 2:
        return 1

    seq = [0] * n
    seq[0] = seq[1] = 1

    for i in range(2, n):
        seq[i] = seq[i - 1] + seq[i - 2]

    print seq


fibonacci_dp(10)
