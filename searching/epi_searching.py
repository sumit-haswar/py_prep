from typing import List
from random import randint


#   11.1 search a sorted array for first occurrence of k
def find_first_occurrence(list: List[int], k: int) -> int:
    left = 0
    right = len(list) - 1
    result = -1
    while left <= right:
        mid = _get_mid(left, right)
        if list[mid] == k:
            result = mid
            right = mid - 1
        elif list[mid] > k: # look left
            right = mid - 1
        else:  # k > list[mid], look right
            left = mid + 1

    return result


#   11.2 search a sorted array for entry equal to its index
def search_entry_equal_to_its_index(list: List[int]):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = left + (right - left) // 2
        diff = list[mid] - mid
        if diff == 0:
            return mid
        elif diff > 0:  # diff is positive, look left
            right = mid - 1
        else:  # look right, diff is negative, look right
            left = mid + 1

    return -1


#   11.3 search a cyclically sorted array
def search_smallest(list: List[int]):
    left = 0
    right = len(list) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list[mid] > list[right]:  # least is in mid --> right
            left = mid + 1
        else:
            right = mid

    return left


#   11.4 compute the integer square root
def get_square_root(k: int) -> int:
    left = 1
    right = k

    while left <= right:
        mid = left + (right - left) // 2
        sqr = mid * mid
        if sqr == k:
            return mid
        elif sqr > k:
            right = mid - 1
        else:
            left = mid + 1

    return left - 1


# -- -- -- -- generalized search -- -- -- --
#   11.6 search in a 2d sorted array
def matrix_search(matrix, num):
    rows = len(matrix)
    cols = len(matrix[0])

    # start with top right
    curr_row = 0
    curr_col = cols - 1
    while curr_row < rows and curr_col < cols:
        if matrix[curr_row][curr_col] == num:
            return curr_row, curr_col
        elif matrix[curr_row][curr_col] < num:  # go down
            curr_row += 1
        else:  # go left
            curr_col -= 1

    return -1, -1


#   11.7 find min and max simultaneously
def find_min_max_stream(A: List[int]):
    if len(A) < 2:
        return A[0], A[0]

    list_min, list_max = _get_min_max(A[0], A[1])

    # move from 2 to second-last in lock-steps of 2
    for idx in range(2, len(A) - 1, 2):
        curr_min, curr_max = _get_min_max(A[idx], A[idx + 1])

        list_min = min(list_min, curr_min)
        list_max = max(list_max, curr_max)

    # if input list is odd, one comparison with last elem
    if len(A) % 2 == 1:
        list_min = min(list_min, A[-1])
        list_max = max(list_max, A[-1])

    return list_min, list_max


#   11.8 find the kth largest element
def find_kth_largest(list: List[int], k: int) -> int:
    def _get_pivot_idx(left, right, idx) -> int:
        # swap idx with right
        idx_val = list[idx]
        list[idx] = list[right]
        list[right] = idx_val

        pivot_idx = left
        while left < right:
            if list[left] < idx_val:
                left += 1
            elif list[left] > idx_val:
                # swap list[left] with list[pivot_idx]
                curr = list[left]
                list[left] = list[pivot_idx]
                list[pivot_idx] = curr
                pivot_idx += 1
                left += 1

        list[right] = list[pivot_idx]
        list[pivot_idx] = idx_val

        return pivot_idx

    def _find_kth_largest(left, right) -> int:
        idx = randint(left, right)  # right is inclusive
        pivot_idx = _get_pivot_idx(left, right, idx)
        if pivot_idx == k - 1:
            return list[pivot_idx]
        elif pivot_idx < k - 1:
            return _find_kth_largest(pivot_idx + 1, right)
        else:
            return _find_kth_largest(left, pivot_idx - 1)

    return _find_kth_largest(0, len(list) - 1)


#   11.10 find the duplicate and missing elements
def find_duplicate_missing(a: List[int]):
    # do XOR of all values in a and 0 -> n-1
    xor = 0
    for i, elem in enumerate(a):
        xor ^= xor ^ i ^ elem

    missing_or_duplicate = 0
    diff_mask = xor & ~(xor - 1)

    for i, elem in enumerate(a):
        if i & diff_mask:
            missing_or_duplicate ^= i
        if elem & diff_mask:
            missing_or_duplicate ^= elem

    if missing_or_duplicate in a:
        duplicate = missing_or_duplicate
        missing = missing_or_duplicate ^ xor
    else:
        missing = missing_or_duplicate
        duplicate = missing_or_duplicate ^ xor

    return missing, duplicate


# todo
#   (11.5) compute the real square root
#   (11.9) find the missing IP address


def _get_mid(left, right):
    return left + (right - left) // 2


def _get_min_max(a, b):
    if a < b:
        return a, b
    else:
        return b, a
