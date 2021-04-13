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
        elif list[mid] > k:  # look left
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
        # move idx to right
        idx_val = list[idx]
        list[idx] = list[right]
        list[right] = idx_val

        pivot_idx = left
        while left < right:
            # if elem at left is less than pivot-elem, continue
            if list[left] < idx_val:
                left += 1
            elif list[left] > idx_val:
                # swap list[left] with list[pivot_idx]
                curr = list[left]
                list[left] = list[pivot_idx]
                list[pivot_idx] = curr

                pivot_idx += 1
                left += 1
        # re-swap with right
        list[right] = list[pivot_idx]
        list[pivot_idx] = idx_val

        return pivot_idx

    def _find_kth_largest(left, right) -> int:
        # get a random index
        idx = randint(left, right)  # right is inclusive

        # find if the elem at pivot_idx is the kth element
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

class Entry:
    def __init__(self, number, freq):
        self.number = number
        self.freq = freq

    def __str__(self):
        return "{}:{}".format(self.number, self.freq)


def find_top_k_frequent_elements(list: List[int], k: int) -> List[int]:
    def _partition(list: List[Entry], left, right, idx):
        # move idx to right
        idx_freq_val = list[idx].freq
        list[idx], list[right] = list[right], list[idx]

        curr = left
        while curr < right:
            if list[curr].freq > idx_freq_val:
                curr += 1
            elif list[curr].freq <= idx_freq_val:
                list[curr], list[left] = list[left], list[curr]
                left += 1
                curr += 1

        list[left], list[right] = list[right], list[left]
        return left

    def _find_top_k_frequent(list, left, right, k):

        if left == right:
            return

        rand_idx = randint(left, right)
        pivot_idx = _partition(list, left, right, rand_idx)

        if pivot_idx == k - 1:
            return
        elif pivot_idx < k - 1:
            _find_top_k_frequent(list, pivot_idx + 1, right, k)
        else:
            _find_top_k_frequent(list, left, pivot_idx - 1, k)

    # build a hash-map: element : frequency
    count_map = {}
    for n in list:
        if n not in count_map:
            count_map[n] = Entry(n, 0)
        count_map[n].freq += 1

    if len(count_map) <= k:
        return [e.number for e in count_map.values()]

    seq = [entry for entry in count_map.values()]
    _find_top_k_frequent(seq, 0, len(seq) - 1, len(seq) - k)
    return [e.number for e in seq[-k:]]


def _get_mid(left, right):
    return left + (right - left) // 2


def _get_min_max(a, b):
    if a < b:
        return a, b
    else:
        return b, a


if __name__ == "__main__":
    list = [-5, -9, 67, -10, 4, -57, 47, 13, -67, -26, -57, 63, 38, -68, 62, -45, -37, 95, 49, -91, -53, -42, -33, 80,
            78, -30, -36, 22, 9, -86, 79, -1, 44, -92, 30, -68, -94, 58, -51, -26, -38, 5, -74, 25, 71, -93, 52, -12,
            -86, 7, -86, 53, 78, -31, -5, -87, 88, -98, -39, 9, 99, 23, 96, -90, 51, -64, 35, -73, 9, 60, -78, 70, 99,
            14, 70, 71, -78, 50, 7, 46, -89, 57, -1, 87, -87, -95, 48, 49, 79, -54, 31, 28, -27, 75, 31, -76, -12, 35,
            40, -90, -60, -60, -7, 67, 73, -34, -42, -35, 61, 51, 18, 95, 16, 78, -81, -91, -30, 92, 57, -79, 5, 41, 29,
            72, -62, -47, 80, 29, 1, -21, -36, 5, 82, 4, -12, -52, -56, -47, -68, 95, 85, -87, -7, -12, 98, 75, -64,
            -93, 11, 73, -81, -9, -12, -9, 51, 17, -94, 33, -9, 57, -35, 10, -17, 87, -18, -55, -52, 30, -62, 73, 35,
            -74, -47, -63, 77, -72, -55, 5, 73, 21, 14, 7, -65, -51, -55, -49, 98, -20, -22, -68, 34, -20, 92, 55, 47,
            -20, 6, -54, -12, 3, 75, 69, 60, 15, 88, 64, 2, -27, -50, 55, 73, 46, -15, -64, 93, -47, -75, -55, -75, 21,
            -57, 91, -12, -99, -68, -56, -14, -4, -77, -94, 55, 93, -31, 68, -12, -23, 59, -56, -86, 43, 83, -93, -78,
            -11, -7, 96, -3, -87, -37, 19, -78, 67, -29, 77, -28, 91, -73, -68, -22, 18, -7, 3, 15, 77, 99, 31, -48,
            -86, -45, -82, 52, -39, 8, -88, -83, -58, -77, 5, 87, -61, 50, 32, -66, -36, 60, -53, 52, 70, -36, -1, 83,
            -56, 33, 98, -80, 28, 1, -21, -50, -60, 44, 99, 18, 83, -29, 83, -36, -55, -6, 96, -60, 61, 75, 6, -57, 2,
            82, 62, -27, 36, 60, 72, 92, 61, -65, 79, -57, -34, -23, -28, -55, 53, 36, -80, 5, -76, 64, -81, -32, -43,
            -1, 50, -16, -72, -74, 22, 88, 28, -79, -99, 85, -13, -34, -76, 85, 6, 21, -99, 10, -46, 79, 11, -70, 17,
            47, -22, -62, 0, 6, 75, -19, 57, -25, -52, -83, 90, 21, 95, 52, 68, 47, -12, 76, -9, -65, 86, 90, 16, 74,
            64, 26, 84, 64, -42, 97, -72, 53, -76, 11, 89, -62, 67, 100, 15, 53, 68, -16, 24, 11, -77, 20, 59, -95, -50,
            -20, 27, 45, 94, 13, -93, 86, 49, 12, 19, 17, -33, -52, -28, 71, 79, -19, -73, 40, -99, 83, 77, 19, -20, 98,
            86, -5, -5, 73, 18, 100, 73, -45, 33, 3, 89, 32, -53, 73, 16, -3, -26, -80, 49, -78, 67, 31, 1, -85, -44,
            -91, -68, 75, -74, 95, 23, 89, 99, -84, 54, -93, 68, 0, -41, 66, -15, -27, -23, -9, -68, 37, 45, -69, 57,
            80, 10, -64, 35, 26, 55, -67, 31, -76, 36, -99, 21]
    # [-12, -68, 73, -55, -9, 5, 75]
    print(find_top_k_frequent_elements(list, 7))
