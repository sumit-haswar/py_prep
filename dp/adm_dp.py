from typing import List


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
    """get n choose k using simple recursion (exponential time!)"""

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
    # matrix is N rows and k + 1 columns
    for row in range(N):
        # first column values are always 1: C(n,0) == 1
        curr_row = [1]
        for col in range(1, row + 1):
            # diagonal values are also 1: C(n,n) == 1
            curr_row.append(1 if row == col else 0)
        matrix.append(curr_row)

    for row in range(2, N):
        for col in range(1, len(matrix[row]) - 1):
            matrix[row][col] = matrix[row - 1][col] + matrix[row - 1][col - 1]

    return matrix[n][k]

def get_partitions_diff(partitions_str):
    partitions = partitions_str.split('|')
    min_val = float('inf')
    max_val = float('-inf')
    for partition in partitions:
        books = partition.split(',')
        total_pages = sum([int(x) for x in books])
        min_val = min(total_pages, min_val)
        max_val = max(total_pages, max_val)

    return max_val - min_val

def partition(books: List[int], k: int):
    def _partition(books, curr_partition, total_books, curr_idx):
        # base-case
        if curr_idx == k:
            if books:
                partitions_str = curr_partition + '|' + ','.join([str(x) for x in books])
                print(partitions_str)
                diff = get_partitions_diff(partitions_str)
                if global_min[0] is None:
                    result.clear()
                    result.append(partitions_str)
                    global_min[0] = diff
                elif diff < global_min[0]:
                    result.clear()
                    result.append(partitions_str)
                    global_min[0] = min(diff, global_min[0])
            return

        for div in range(1, total_books):
            left = books[:div]
            rest = books[div:]

            _partition(rest,
                       curr_partition + '|' + ','.join([str(x) for x in left]) if curr_partition else ','.join(
                           [str(x) for x in left]),
                       total_books,
                       curr_idx + 1)

    result = []
    total_books = len(books)
    global_min = [None]
    _partition(books, '', total_books, 1)
    return global_min, result

def partition_dp(books: List[int], k: int):
    # dp table for values
    n = len(books)

    m = []

    # dp table for dividers
    d =[]

    # prefix sum array
    p = []

    cost = 0

    p.append(0)
    for i in range(1, n):
        p.append(p[i-1] + books[i])

    print(p)


if __name__ == "__main__":
    books = [float('inf'), 100, 200, 300, 400, 500, 600, 700, 800, 900]
    # books = [1,2,3,4,5,6,7,8,9]
    # books = [100, 200, 300, 400, 500]
    # print(partition(books, 3))
    partition_dp(books,3)
