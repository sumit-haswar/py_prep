from typing import List, Optional


def find_least_greater_than(arr: List[int], elem: int) -> Optional[int]:
    left = 0
    right = len(arr) - 1
    candidate = None
    while left <= right:
        mid_idx = get_mid(left, right)
        mid_elem = arr[mid_idx]
        if mid_elem < elem: # discard left sub-array and look right
            left = mid_idx + 1
        elif mid_elem > elem:   # discard right sub-array and look left
            candidate = mid_elem
            right = mid_idx - 1
        else: # mid_elem == elem, keep looking right
            right = mid_idx - 1

    return candidate


def get_mid(left: int, right: int) -> int:
    return left + (right - left) // 2 # floors the division



if __name__ == "__main__":

    res = find_least_greater_than([0, 12, 17, 23, 67, 90, 99], 100)
    print(res)