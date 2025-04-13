from typing import List


def heap_sort(arr: List[int]):
    # 1. build max heap of the input array
    build_max_heap(arr)

    last_idx = len(arr) - 1
    # 2 from n to 1, swap and max-heapify
    while last_idx > 0:
        arr[0], arr[last_idx] = arr[last_idx], arr[0]
        last_idx -= 1
        max_heapify(arr, 0, last_idx)

    return arr

def build_max_heap(arr: List[int], last_idx: int = None):
    # for an input array, all elements from first_leaf_idx to n are leaf nodex
    if last_idx is None:
        last_idx = len(arr) - 1

    for idx in range(last_idx, -1, -1):
        max_heapify(arr, idx, last_idx)

def max_heapify(arr: List[int], idx: int, last_idx: int):
    left = get_left(idx)
    right = get_right(idx)

    if left <= last_idx and arr[left] > arr[idx]:
        largest = left
    else:
        largest = idx

    if right <= last_idx and arr[right] > arr[largest]:
        largest = right

    if largest != idx:
        # swap elements at largest and idx
        arr[idx], arr[largest] = arr[largest], arr[idx]
        max_heapify(arr, largest, last_idx)

def get_first_leaf_idx(last_idx: int) -> int:
    return (last_idx - 1)//2 + 1

def get_left(idx):
    return 2 * idx + 1

def get_right(idx):
    return 2 * idx + 2

def get_parent(idx):
    return (idx - 1) // 2

class PriorityQueue():

    def __init__(self, items: List[int] = None):
        self._pq = []
        self._size = 0
        for item in items:
            self._pq.append(item)
        build_max_heap(self._pq)
        self._size = len(self._pq)

    def peek_max(self):
        return self._pq[0]

    def pop_max(self):
        if self._size == 0:
            raise Exception("queue empty")

        curr_max = self._pq[0]
        # swap last-element with first element
        self._pq[0], self._pq[self._size - 1] = self._pq[self._size - 1], self._pq[0]
        self._size -= 1
        max_heapify(self._pq, 0, self._size - 1)

        return curr_max

    def insert(self, val: int):
        self._size += 1
        self._pq[self._size - 1] = float('-inf')
        self.inc_key(self._size - 1, val)

    def inc_key(self, idx, new_key: int):
        if self._pq[idx] > new_key:
            raise Exception("new_key value can't be lower than current")

        self._pq[idx] = new_key
        while idx >= 0 and self._pq[get_parent(idx)] < self._pq[idx]:
            # swap parent value and current value
            self._pq[get_parent(idx)], self._pq[idx] = self._pq[idx], self._pq[get_parent(idx)],
            idx = get_parent(idx)


if __name__ == "__main__":

    # res = heap_sort()
    # [2, 4, 5, 7, 8, 13, 17, 20, 25, 500, 700]
    pq = PriorityQueue([5, 13, 2, 25, 500, 7, 17, 20, 8, 4, 700])
    for i in range(12):
        print(pq.pop_max())