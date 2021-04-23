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


def longest_increasing_subsequence():
    pass


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
                    # result.clear()
                    # result.append(partitions_str.split('|'))
                    result['partition'] = partitions_str.split('|')
                    global_min[0] = diff
                elif diff < global_min[0]:
                    # result.clear()
                    # result.append(partitions_str.split('|'))
                    result['partition'] = partitions_str.split('|')
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

    result = {}
    total_books = len(books)
    global_min = [None]
    _partition(books, '', total_books, 1)
    return global_min[0], result['partition']


def partition_dp(seq: List[int], k: int):
    # dp table for values
    n = len(seq)

    prefix_sum = []
    curr_idx = 0
    while curr_idx < n:
        val = 0
        if prefix_sum:
            val = prefix_sum[-1]

        val += seq[curr_idx]

        prefix_sum.append(val)

        curr_idx += 1

    m = [[seq[0] for _ in range(k)]]
    # init value for m
    for i in range(1, n):
        curr_row = [prefix_sum[i]]
        for j in range(1, k):
            curr_row.append(float('-inf'))
        m.append(curr_row)

    # dp table for dividers
    d = []

    print(m)

    for elems in range(1, n):
        for partitions in range(1, k):
            for x in range(0, elems):

                cost = max(m[x][partitions - 1], prefix_sum[elems] - prefix_sum[x])

                if m[elems][partitions] == float('-inf') or m[elems][partitions] > cost:
                    m[elems][partitions] = cost

    print(m)


if __name__ == "__main__":
    # books = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    books = list(range(1, 10))
    partition_dp(books, 3)
    # print(partition(books, 3))
    # partition_dp(books, 3)
    # seq = [2,4,3,5,1,7,6,9,8]
