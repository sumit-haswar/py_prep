from typing import List


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
        elif list[mid] > k:
            right = mid - 1
        else:  # k > list[mid]
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
        elif diff > 0:  # look left
            right = mid - 1
        else:  # look right
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
#   11.7 find min and max simultaneously

#   11.8 find the kth largest element
def find_kth_largest(list: List[int], k: int) -> int:
    pass


#   11.9 find the missing IP address
#   11.10 find the duplicate and missing elements

# todo
#   (11.5) compute the real square root
# def get_real_square_root():
#     pass

def _get_mid(left, right):
    return left + (right - left) // 2
