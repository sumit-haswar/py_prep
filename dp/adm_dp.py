def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoized(n):
    def _fibonacci_memoized(n):
        if n in lookup:
            return lookup[n]

        r = _fibonacci_memoized(n - 1) + _fibonacci_memoized(n - 2)
        lookup[n] = r
        return r

    lookup = {0: 0, 1: 1}
    _fibonacci_memoized(n)
    return lookup[n]


def fibonacci_iter(n):
    curr_minus_2 = 0
    curr_minus_1 = 1
    for i in range(2, n + 1):
        curr = curr_minus_2 + curr_minus_1
        curr_minus_2 = curr_minus_1
        curr_minus_1 = curr

    return curr_minus_1


def binomial_coefficients_recur(n, k):
    def _binomial_coefficients_recur(n, k):
        if n <= 1 or k == 0 or n == k:
            return 1
        return _binomial_coefficients_recur(n - 1, k) \
               + _binomial_coefficients_recur(n - 1, k - 1)

    return _binomial_coefficients_recur(n, k)


def binomial_coefficients(n, k):
    """get n choose k using pascal's triangle"""
    matrix = []

    N = n + 1

    # create pascal's triangle with col:1 and diagonal:1
    for row in range(N):
        curr_row = [1]
        for col in range(1, row + 1):
            curr_row.append(1 if row == col else 0)
        matrix.append(curr_row)

    for row in range(2, N):
        for col in range(1, len(matrix[row]) - 1):
            matrix[row][col] = matrix[row - 1][col] + matrix[row - 1][col - 1]

    return matrix[n][k]
