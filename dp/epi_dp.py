from typing import List


def fibonacci_dp(n: int) -> int:
    def _fibonacci_dp(number):
        if number in cache:
            return cache[number]
        cache[number] = _fibonacci_dp(number - 1) + _fibonacci_dp(number - 2)
        return cache[number]

    cache = {0: 0, 1: 1}
    _fibonacci_dp(n)
    return cache[n]


def fibonacci_iter(n: int) -> int:
    fibo_minus_1, fibo_minus_2 = 0, 1
    for number in range(1, n + 1):
        f = fibo_minus_1 + fibo_minus_2
        fibo_minus_2, fibo_minus_1 = fibo_minus_1, f

    return fibo_minus_1


def find_maximum_subarray_brute_force(array: List[int]) -> (int, List[int]):
    """O(n^2) time complexity"""
    # calculate S
    S = []
    for idx in range(len(array)):
        sum = 0
        for curr in range(0, idx + 1):
            sum = sum + array[curr]

        S.append(sum)
    #
    maximum = 0
    max_sub_array = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if i == 0:
                sum_i_j = S[j]
            else:
                sum_i_j = S[j] - S[i - 1]

            if sum_i_j > maximum:
                max_sub_array = [i, j]
                maximum = sum_i_j

    return maximum, max_sub_array


def find_maximum_subarray(array: List[int]) -> int:
    """builds max subarray from left to right, using dp approach
    """
    sum = []
    maximum = 0
    for i in range(len(array)):
        if i == 0:
            sum.append(array[i])
            maximum = array[i]
            continue
        curr_max = max(array[i], sum[i - 1] + array[i])
        sum.append(curr_max)
        maximum = max(curr_max, maximum)

    return maximum


#   16.2 Levenshtein distance
def levenshtein_distance(a: str, b: str) -> int:
    pass
    # def _levenshtein_distance(a_idx, b_idx):
    #     pass
    #
    # matrix = [[-1] * len(b) for _ in a]
    # _levenshtein_distance(len(a) - 1, len(b) - 1)
