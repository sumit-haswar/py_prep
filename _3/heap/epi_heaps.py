import heapq
from typing import Iterator, List
from math import sqrt


# get top-k longest strings of an iterator
def top_k(k: int, stream: Iterator[str]):
    # iterate through first k strings
    heap = []
    for i in range(k):
        elem = next(stream, None)
        if elem is None:
            break
        heap.append((len(elem), elem))
    heapq.heapify(heap)
    for next_str in stream:
        curr_len = len(next_str)
        if curr_len > heap[0][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, (curr_len, next_str))

    return heap


# 10.1 merge sorted files
def merge_sorted_files(file_iterators: List[Iterator[int]]):
    min_heap = []
    # iterate through the list and add to min_heap
    for idx, file_iterator in enumerate(file_iterators):
        min_heap.append((next(file_iterator), idx))

    heapq.heapify(min_heap)
    res = []
    while min_heap:
        curr = heapq.heappop(min_heap)
        res.append(curr[0])  # add value to result
        file_idx = curr[1]
        next_elem = next(file_iterators[file_idx], None)
        if next_elem is None:
            continue

        heapq.heappush(min_heap, (next_elem, file_idx))

    return res


class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def dist(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def __lt__(self, other):
        return sqrt(self.x * self.x + self.y * self.y) < sqrt(other.x * other.x + other.y * other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


# 10.4 compute the k closest stars
def find_k_closest_stars(k: int, stars_iterator: Iterator[Star]):
    max_heap = []
    for curr in range(k):
        curr_star = next(stars_iterator)
        max_heap.append((curr_star.dist * -1, curr_star))

    heapq.heapify(max_heap)

    for star in stars_iterator:
        # peek farthest star
        farthest_star = max_heap[0][1]
        if star < farthest_star:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (star.dist * -1, star))

    return [str(x[1]) for x in max_heap]


# 10.3 sort an almost sorted array
def sort_almost_sorted_array(arr: Iterator[int], k: int):
    res = []
    min_heap = []
    for i in range(k + 1):
        min_heap.append(next(arr))
    heapq.heapify(min_heap)

    while min_heap:
        least = heapq.heappop(min_heap)
        res.append(least)
        num = next(arr, None)
        if num is None:
            continue
        heapq.heappush(min_heap, num)

    return res


# 10.5 compute the median of online data
def find_stream_median(arr: Iterator[int]) -> List[int]:
    max_heap = []
    min_heap = []
    res = []

    for elem in arr:
        heapq.heappush(max_heap, -1 * elem)

        heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))

        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))

        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) * 0.5
        else:
            median = -max_heap[0]

        res.append(median)

    return res


# 10.6 compute the k largest elements in a max-heap
def find_k_largest_in_max_heap(max_heap: List[int], k: int):
    candidate_max_heap = [(-max_heap[0], 0)]
    res = []
    for i in range(k):
        top = heapq.heappop(candidate_max_heap)
        res.append(-1 * top[0])

        left = get_left(top[1])
        right = get_right(top[1])

        if left < len(max_heap):
            heapq.heappush(candidate_max_heap, (-max_heap[left], left))

        if right < len(max_heap):
            heapq.heappush(candidate_max_heap, (-max_heap[right], right))

    return res


# 10.2 sort an inc-dec array
def sort_inc_dec(arr: List[int]):
    if not arr or len(arr) == 1:
        return arr

    is_increasing = True if arr[0] < arr[1] else False
    res = []
    start_idx = 0
    for idx in range(1, len(arr) + 1):
        if (idx == len(arr)
                or (is_increasing and arr[idx - 1] > arr[idx])
                or (not is_increasing and arr[idx - 1] < arr[idx])):
            curr_sub_array = arr[start_idx:idx] if is_increasing else list(reversed(arr[start_idx:idx]))
            res.append(curr_sub_array)
            is_increasing = not is_increasing
            start_idx = idx

    return merge_sorted_files([iter(x) for x in res])


def get_left(idx):
    return (2 * idx) + 1


def get_right(idx):
    return (2 * idx) + 2


if __name__ == "__main__":
    fi = iter([
        Star(2, 0),
        Star(0, 3),
        Star(0.5, 0.5),
        Star(0, -1),
        Star(-1, 0),
        Star(-3, 0),
    ])

    # print(res)
    x = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    x2 = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    res = sort_inc_dec(x)
    print(res)
    x2.sort()
    print(x2)
