import heapq
from typing import List, Iterable


# boot camp
def k_longest_strings(k: int, stream: Iterable[str]):
    min_heap = []
    for _ in range(k):
        elem = next(stream)
        min_heap.append((len(elem), elem))

    heapq.heapify(min_heap)

    for curr in stream:
        if len(curr) > len(min_heap[0][1]):
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, (len(curr), curr))

    return [elem[1] for elem in min_heap]


#   10.1 merge sorted files
def merge_sorted_streams(streams: List[Iterable]) -> List[int]:
    class HeapItem:
        def __init__(self, item, idx):
            self.item = item
            self.it_idx = idx

        def __lt__(self, other):
            return self.item < other.item

    heap = []
    for idx, stream in enumerate(streams):
        first_elem = next(stream)
        heap.append(HeapItem(first_elem, idx))

    heapq.heapify(heap)
    result = []

    while heap:
        min = heapq.heappop(heap)
        result.append(min.item)
        # push to heap
        new_elem = next(streams[min.it_idx], None)
        if new_elem:
            heapq.heappush(heap, HeapItem(new_elem, min.it_idx))

    return result


#   10.2 sort an inc-dec array
def sort_inc_dec_array(a: List[int]) -> List[int]:
    start_idx = 0
    is_increasing = True
    result = []
    for idx in range(1, len(a) + 1):
        prev = a[idx - 1]
        if (idx == len(a)
                or (is_increasing and a[idx] <= prev)
                or (not is_increasing and a[idx] < prev)):
            result.append(
                a[start_idx: idx] if is_increasing else a[idx - 1:start_idx - 1:-1]
            )
            start_idx = idx
            is_increasing = not is_increasing

    return merge_sorted_streams([iter(l) for l in result])


#   10.3 sort an almost-sorted array
def sort_k_sorted_array(A: Iterable[int], k: int):
    min_heap = []
    # add first k elements to heap
    for _ in range(k):
        heapq.heappush(min_heap, next(A))

    result = []
    for curr in A:
        min = heapq.heappop(min_heap)
        result.append(min)
        heapq.heappush(min_heap, curr)

    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result


class Star():
    def __init__(self, earth_distance):
        self.earth_distance = earth_distance

    def __lt__(self, other):
        return self.earth_distance < other.earth_distance


#   10.4 compute the k closest stars
def get_k_closest_stars(stars: Iterable[Star], k: int) -> List[Star]:

    max_heap = []
    for _ in range(k):
        star = next(stars)
        heapq.heappush(max_heap, (-star.earth_distance, star))

    for star in stars:
        if star.earth_distance < max_heap[0][1].earth_distance:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-star.earth_distance, star))

    # returns furthest to closest
    return [star[1].earth_distance for star in heapq.nlargest(k, max_heap)]


#   10.5 compute the median of online(streaming) data
def compute_stream_median(stream: Iterable[int]) -> List[int]:
    min_heap = []
    max_heap = []
    result = []
    for i in stream:
        # add to min_heap
        heapq.heappush(min_heap, i)
        # move from min to max_heap
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if len(min_heap) < len(max_heap):
            # move from max to min
            max_top = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -1 * max_top)

        median = ((min_heap[0] + (max_heap[0] * -1)) * 0.5) \
            if len(min_heap) == len(max_heap) \
            else min_heap[0]
        result.append(median)

    return result


#   10.6 compute the k largest elements in a max-heap
def get_k_largest_in_heap(heap: List[int], k: int) -> List[int]:
    max_heap = []
    heapq.heappush(max_heap, (-1 * heap[0], 0))
    result = []
    for _ in range(k):

        (elem, idx) = heapq.heappop(max_heap)
        result.append(-1 * elem)
        # push left and right
        left = idx * 2 + 1
        right = idx * 2 + 2
        if left < len(heap):
            heapq.heappush(max_heap, (-1 * heap[left], left))
        if right < len(heap):
            heapq.heappush(max_heap, (-1 * heap[right], right))

    return result
