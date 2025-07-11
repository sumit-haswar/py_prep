from typing import List


def _swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


class MyHeap:
    def __init__(self, arr):
        self.data = arr
        self.heap_size = len(self.data)

    def _left(self, idx):
        return 2 * idx + 1

    def _right(self, idx):
        return 2 * idx + 2

    def _parent(self, idx):
        return (idx - 1) // 2

    def _swap(self, a_idx, b_idx):
        temp = self.data[a_idx]
        self.data[a_idx] = self.data[b_idx]
        self.data[b_idx] = temp

    def _max_heapify(self, idx):
        left_idx = self._left(idx)
        right_idx = self._right(idx)

        largest = idx
        if left_idx < self.heap_size and self.data[largest] < self.data[left_idx]:
            largest = left_idx

        if right_idx < self.heap_size and self.data[largest] < self.data[right_idx]:
            largest = right_idx

        if largest != idx:
            self._swap(idx, largest)
            self._max_heapify(largest)

    def _build_max_heap(self):
        mid = len(self.data) // 2
        # fun _max_heapify from mid to 0
        while mid >= 0:
            self._max_heapify(mid)
            mid -= 1

    def sort(self):
        # build max-heap
        self._build_max_heap()  # O(n) operation, max is at index 0
        pivot_idx = len(self.data) - 1
        while pivot_idx > 0:
            self._swap(0, pivot_idx)

            self.heap_size -= 1
            self._max_heapify(0)

            pivot_idx -= 1


# heap sort
def heap_sort(arr: List[int]):
    my_heap = MyHeap(arr)
    my_heap.sort()
    return my_heap.data


# merge sort
def merge_sort(arr: List[int]):
    def _merge(list_a, list_b):
        res = []
        a_idx = 0
        b_idx = 0
        while a_idx < len(list_a) and b_idx < len(list_b):
            if list_a[a_idx] < list_b[b_idx]:
                res.append(list_a[a_idx])
                a_idx += 1
            elif list_a[a_idx] > list_b[b_idx]:
                res.append(list_b[b_idx])
                b_idx += 1
            else:
                res.append(list_a[a_idx])
                a_idx += 1
                res.append(list_b[b_idx])
                b_idx += 1

        while a_idx < len(list_a):
            res.append(list_a[a_idx])
            a_idx += 1

        while b_idx < len(list_b):
            res.append(list_b[b_idx])
            b_idx += 1

        return res

    def _merge_sort(arr):
        if len(arr) == 0 or len(arr) == 1:
            return arr

        if len(arr) == 2:
            return [arr[0], arr[1]] if arr[0] < arr[1] else [arr[1], arr[0]]

        mid = len(arr) // 2

        left_part = _merge_sort(arr[0:mid])
        right_part = _merge_sort(arr[mid:])

        # combine left_part and right_part
        return _merge(left_part, right_part)

    return _merge_sort(arr)


# quick sort
def quick_sort(arr: List[int]):
    def _partition(arr, left, right, pivot_idx) -> int:
        pivot_val = arr[pivot_idx]

        # move pivot_val to right
        _swap(arr, pivot_idx, right)

        l = left
        r = right - 1
        while l <= r:
            if arr[l] < pivot_val:
                l += 1
            else:  # arr[l] > pivot_val, so should be moved to right
                _swap(arr, l, r)
                r -= 1

        _swap(arr, l, right)
        return l

    def _quick_sort(arr, left, right):
        pivot_idx = left + (right - left) // 2

        pivot = _partition(arr, left, right, pivot_idx)

        if left < pivot - 1:
            _quick_sort(arr, left, pivot - 1)

        if right > pivot + 1:
            _quick_sort(arr, pivot + 1, right)

    _quick_sort(arr, 0, len(arr) - 1)

    return arr


if __name__ == "__main__":
    # print("hello")
    print(heap_sort([6000, 6, 9, 4, 1, 2, 90, 123, 6000, 4, 800, 456, 0, 6000]))
    print(merge_sort([6000, 6, 9, 4, 1, 2, 90, 123, 6000, 4, 800, 456, 0, 6000]))
    print(quick_sort([6000, 6, 9, 4, 1, 2, 90, 123, 6000, 4, 800, 456, 0, 6000, 89]))
