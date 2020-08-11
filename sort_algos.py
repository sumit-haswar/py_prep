"""
# popular sorting algorithms
"""
from heap import Heap

#  --- comparison sorts ---
# bubble sort
def bubble_sort(list):
    return list


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
    pass


# quick sort
def quick_sort(list):
    pass


# merge sort
def merge_sort(list):
    pass


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


def main():
    input = [5, 2, 15, 1, 90]
    selection_sort(input)
    print(input)


if __name__ == '__main__':
    main()
