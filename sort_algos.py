"""
# popular sorting algorithms
"""
from heap import Heap


# selection sort
def selection_sort(list):
    left_idx = 0

    while left_idx < len(list):
        min, min_idx = _get_min(list, left_idx, len(list))
        # swap if required
        if min_idx != left_idx:
            temp = list[min_idx]
            list[min_idx] = list[left_idx]
            list[left_idx] = temp

        left_idx += 1


# insertion sort
def insertion_sort(list):
    # i moves left to right starting with idx = 1
    size = len(list)
    for i in range(1, size):
        j = i
        # j goes right to left
        while j > 0 and list[j] < list[j - 1]:
            _swap(list, j, j - 1)
            j = j - 1


# quick sort
def quick_sort(list, left, right):
    pivot = _partition(list, left, right)

    if left < (pivot - 1):
        quick_sort(list, left, pivot - 1)

    if right > (pivot + 1):
        quick_sort(list, pivot + 1, right)


def _partition(list, left, right):
    # start with right as pivot-val
    pivot_value = list[right]

    left_idx = left - 1

    right_idx = left
    while right_idx <= right - 1:
        # if you find elem <= pivot_value increment left_idx swap with loop index and
        if list[right_idx] <= pivot_value:
            left_idx += 1
            _swap(list, left_idx, right_idx)
        right_idx += 1
    # finally exchange left_idx + 1 with right
    _swap(list, left_idx + 1, right)

    # return the correct index of pivot_val
    return left_idx + 1


def _partition_2(seq, left, right):
    pivot_idx = left + (right - left) // 2
    pivot_val = seq[pivot_idx]

    # move pivot_val to right
    seq[right], seq[pivot_idx] = seq[pivot_idx], seq[right]

    curr_right = right - 1
    curr_left = left
    while curr_left <= curr_right:
        if seq[curr_left] < pivot_val:
            curr_left += 1
        else:
            # swap, curr_right and curr_left
            seq[curr_left], seq[curr_right] = seq[curr_right], seq[curr_left]
            curr_right -= 1

    # swap seq[curr_left] with correct place of pivot_val
    seq[right], seq[curr_left] = seq[curr_left], seq[right]

    return curr_left


# merge sort
def merge_sort(list, left, right):
    if left >= right:
        return

    mid = (right + left) // 2

    merge_sort(list, left, mid)
    merge_sort(list, mid + 1, right)

    _merge(list, left, mid, right)


def _merge_2(arr, left, mid, right):
    aux = []
    left_idx = left
    right_idx = mid + 1

    while left_idx <= mid and right_idx <= right:

        if arr[left_idx] < arr[right_idx]:
            aux.append(arr[left_idx])
            left_idx += 1
        else:
            aux.append(arr[right_idx])
            right_idx += 1

    while left_idx <= mid:
        aux.append(arr[left_idx])
        left_idx += 1

    while right_idx <= right:
        aux.append(arr[right_idx])
        right_idx += 1

    # copy aux to arr
    curr = left
    for i in aux:
        arr[curr] = i
        curr += 1

def _merge(list, left, mid, right):
    left_size = mid - left + 1
    right_size = right - mid

    left_list = []
    right_list = []
    # copy list elements range left:mid mid+1:right to left and right
    for i in range(0, left_size):
        left_list.append(list[left + i])

    for j in range(0, right_size):
        right_list.append(list[mid + 1 + j])

    # left_seq = []
    # right_seq = []
    # for i in range(left, mid + 1):
    #     left_seq.append(list[i])
    #
    # for i in range(mid + 1, right + 1):
    #     right_seq.append(list[i])

    # perform merge onto list itself in lock-steps
    left_idx = 0
    right_idx = 0
    idx = left

    while left_idx < left_size and right_idx < right_size:
        if left_list[left_idx] < right_list[right_idx]:
            list[idx] = left_list[left_idx]
            idx += 1
            left_idx += 1
        elif left_list[left_idx] > right_list[right_idx]:
            list[idx] = right_list[right_idx]
            idx += 1
            right_idx += 1

    while left_idx < left_size:
        list[idx] = left_list[left_idx]
        idx += 1
        left_idx += 1

    while right_idx < right_size:
        list[idx] = right_list[right_idx]
        idx += 1
        right_idx += 1


# heap sort
def heap_sort(list):
    heap = Heap(list)
    return heap.heap_sort()


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# counting sort

# tim sort

# shell sort

# bucket sort

# radix sort

def _get_min(list, start, end):
    min = list[start]
    min_idx = start

    curr_idx = start + 1
    while curr_idx < end:
        if list[curr_idx] < min:
            min_idx = curr_idx
            min = list[curr_idx]

        curr_idx += 1

    return min, min_idx


def _swap(list, idx_a, idx_b):
    temp = list[idx_a]
    list[idx_a] = list[idx_b]
    list[idx_b] = temp
