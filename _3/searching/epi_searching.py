from typing import List
from math import isclose
from random import randint

# 11.1 search a sorted array for first occurrence of k
def find_first_occurrence(arr: List[int], k : int) -> int:
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = _get_mid(left, right)
        if arr[mid] < k:
            left = mid + 1
        elif arr[mid] > k:
            right = mid - 1
        else: # arr[mid] == k
            result = mid
            right = mid - 1

    return result

# 11.4 compute the integer square root of a number
def calculate_sqrt(n : int) -> int:
    left = 0
    right = n
    while left <= right:
        mid = _get_mid(left, right)
        sqr = mid * mid
        if sqr == n:
            return mid
        elif sqr > n: # look between left and mid
            right = mid - 1
        else:   # sqr < n
            left = mid + 1

    return left - 1


def _get_pivot_idx(arr, left, right, random_k) -> int:
    random_val = arr[random_k]

    # swap rightmost elem with random_elem
    arr[random_k] = arr[right]
    arr[right] = random_val

    pivot_idx = left
    while left < right:
        if arr[left] < random_val:
            left += 1
        else:   # arr[left] > random_val:
            # swap with pivot_idx and inc it
            arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]
            pivot_idx += 1
            left += 1

    # finally swap pivot_idx with right
    arr[right], arr[pivot_idx] = arr[pivot_idx], arr[right]
    return pivot_idx

# 11.8 find the kth largest element(pivot)
def find_kth_largest_element(arr: List[int], k: int) -> int:

    left = 0
    right = len(arr) - 1

    while left <= right:
        random_k = randint(left, right)
        pivot_idx = _get_pivot_idx(arr, left, right, random_k)

        if pivot_idx == (k - 1):
            return arr[pivot_idx]
        elif pivot_idx > (k - 1): # look left
            right = pivot_idx - 1
        else:
            left = pivot_idx + 1

# 11.3 search a cyclically sorted array
def find_cyclic_array_head(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = _get_mid(left, right)
        mid_elem = arr[mid]
        if arr[right] > mid_elem: # look left
            right = mid
        else:
            left = mid + 1

    return left


# 11.5 compute the real square root
def calculate_real_sqrt(n: int) -> int:
    if n < 1:
        left = n
        right = 1.0
    else:
        left = 1.0
        right = n

    while not isclose(left, right):
        mid = (left + right) * 0.5
        mid_sq = mid * mid
        if mid_sq > n: # look left
            right = mid
        else:
            left = mid

    return left


# 11.6 search in a 2d sorted array
def find_element_in_matrix(matrix, elem: int) -> (int, int):
    rows = len(matrix)
    cols = len(matrix[0])

    # start with top right
    curr_row = 0
    curr_col = cols - 1
    while curr_row < rows and curr_col >= 0:
        curr_elem = matrix[curr_row][curr_col]
        if curr_elem == elem:
            return curr_row, curr_col
        elif elem < curr_elem:
            curr_col = curr_col - 1
        else:
            curr_row = curr_row + 1

    return -1, -1


# 11.7 find the min and max simultaneously
def find_min_max(input: List[int]) -> (int, int):

    if len(input) == 1:
        return input[0], input[0]

    minimum, maximum = _get_min_max(input[0], input[1])

    for idx in range(2, len(input) - 1, 2):
        print(idx)
        first_val = input[idx]
        second_val = input[idx + 1]

        # get local min-max
        curr_min, curr_max = _get_min_max(first_val, second_val)

        minimum = min(minimum, curr_min)
        maximum = max(maximum, curr_max)

    if len(input) % 2 == 1:
        # compare last value
        minimum = min(minimum, input[-1])
        maximum = max(maximum, input[-1])


    return minimum, maximum


# 11.2 search a sorted array for entry equal to its index
def find_elem_equal_to_index(input: List[int]) -> int:
    left = 0
    right = len(input) - 1
    while left <= right:
        mid = _get_mid(left, right)
        diff = input[mid] - mid
        if diff == 0:
            return mid
        elif diff < 0:
            left = mid + 1
        else: # diff > 0
            right = mid - 1

    return -1

# todo
#   11.9    find the missing IP Address
#   11.10   find the duplicate and missing elements
def find_duplicate_and_missing():
    pass

def _get_min_max(a, b):
    return (a , b) if a <= b else (b , a)

def _get_mid(left, right):
    return left + (right - left)//2

if __name__ == "__main__":
    # res = find_first_occurrence([5,9,14,25,25,25,25,36], 36)

    # res = find_min_max([24, 44, 98, 4, 9, 10, 15, 17, 18, 105, 107])
    print(calculate_real_sqrt(36))
    # matrix = [
    #     [5,9,12,15],
    #     [6,10,13,16],
    #     [7,11,14,23],
    #     [8,11.5,14.5,26]
    # ]
    #
    # print(find_element_in_matrix(matrix, 26))
    arr = [12, 2, 4, 99, 5, 15, 22, 14]
    print(arr)
    k = 5
    res = find_kth_largest_element(arr, k)
    print(f"{k}th largest:{res}")
    print(arr)