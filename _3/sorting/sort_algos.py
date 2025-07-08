from typing import List
import heapq


class MyHeap:
    def __init__(self):
        pass

    def _get_left(self, idx):
        return None

    def _get_right(self, idx):
        return None



# heap sort
def heap_sort(arr: List[int]):
    heapq.heapify(arr)
    while arr:
        print(heapq.heappop(arr))

# merge sort
def merge_sort(arr: List[int]):
    pass

# quick sort
def quick_sort(arr: List[int]):
    pass


if __name__ == "__main__":
    # print("hello")
    heap_sort([6,9,4,1,2,90,123,4])