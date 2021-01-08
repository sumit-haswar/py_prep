from typing import List
from linked_list import Node
import collections


class TrafficElement:
    def __init__(self, time, volume):
        self.time = time
        self.volume = volume

    def __lt__(self, other):
        return self.volume < other.volume

    def __eq__(self, other):
        return self.time == other.time and self.volume == other.volume


class QueueWithMax:
    def __init__(self):
        self.queue = collections.deque()
        self.max_dq = collections.deque()

    def get_head(self):
        return self.queue[0]

    def enqueue(self, elem):
        self.queue.append(elem)
        # pop all less than curr from tail
        while self.max_dq and self.max_dq[-1] < elem:
            self.max_dq.pop()
        self.max_dq.append(elem)

    def dequeue(self):
        # deque and pop from max, if max is curr
        elem = self.queue.popleft()
        if self.max_dq[0] == elem:
            self.max_dq.popleft()
        return elem

    def get_max(self):
        return self.max_dq[0]


class Building:
    def __init__(self, left, right, height):
        self.left = left
        self.right = right
        self.height = height

    def __lt__(self, other):
        if self.left != other.left:
            return self.left < other.left
        else:
            return self.right < other.right

    def __str__(self):
        return "{}-{}, {}".format(self.left, self.right, self.height)


#   24.01 gcd
def gcd_mod(x: int, y: int) -> int:
    if x > y:
        x, y = y, x

    if x == y:
        return x
    if x == 0 or y == 0:
        return x if y == 0 else y
    return gcd_mod(x, y % x)


#   24.01 gcd
def gcd(x: int, y: int) -> int:
    if x > y:
        x, y = y, x
    if x == y:
        return x
    if x == 0:
        return y

    # both x and y are odd
    if x & 1 and y & 1:
        return gcd(x, y - x)
    # both x and y are even
    elif x & 1 == 0 and y & 1 == 0:
        return 2 * gcd(x >> 1, y >> 1)
    # x/y are even/odd
    elif x & 1 == 0 and y & 1 == 1:
        return gcd(x >> 1, y)
    # x/y are odd/even
    else:
        return gcd(x, y >> 1)


#   24.06 rotate an array
def rotate_array(arr: List[int], offset: int):
    offset = offset % len(arr)

    # first reverse the complete array
    _reverse(arr, 0, len(arr) - 1)

    # then reverse 0 to offset
    _reverse(arr, 0, offset - 1)

    # then reverse offset to end
    _reverse(arr, offset, len(arr) - 1)

    return arr


def _reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


#   24.08 justify text
def justify_text(text: str, limit: int) -> List[str]:
    text_list = text.split(' ')

    result = []
    curr_line = []
    curr_line_len = 0

    for word in text_list:
        if curr_line_len + len(word) + len(curr_line) > limit:
            for i in range(limit - curr_line_len):
                curr_line[i % max(len(curr_line) - 1, 1)] += ' '
            result.append(''.join(curr_line))
            curr_line = []
            curr_line_len = 0
        curr_line.append(word)
        curr_line_len += len(word)

    last_line = ' '.join(curr_line)
    last_line = last_line + ' ' * (limit - len(last_line))
    return result + [last_line]


#   24.09 implement list zipping
def zipping_linked_list(head: Node):
    # split first and second half
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second_head = slow.next
    slow.next = None

    # reverse second half
    second_head = _reverse_ll(second_head)

    # zip head and second_half
    curr = head
    candidate = second_head

    while curr:
        curr_next = curr.next
        curr.next = candidate

        curr = candidate
        candidate = curr_next

    return head


def _reverse_ll(head: Node):
    if head is None or head.next is None:
        return head
    prev = None
    curr = head
    next = curr.next

    while curr:
        curr.next = prev
        prev = curr

        curr = next
        next = next.next if next else None

    return prev


#   24.12 compute max of a sliding window
def calculate_traffic_volumes(arr: List[TrafficElement], width: int):
    result = []

    max_q = QueueWithMax()
    for traffic_elem in arr:
        # append to max_q
        max_q.enqueue(traffic_elem)
        # pop all which are out of range
        while traffic_elem.time - max_q.get_head().time > width:
            max_q.dequeue()

        result.append(TrafficElement(traffic_elem.time,
                                     max_q.get_max().volume))

    return result


#   24.18 find line through most points

#   24.19 convert a sorted doubly linked list to a bst

#   24.22 implement regular expression matching
def is_match(regex: str, s: str) -> bool:
    pass


#   24.29 find the maximum 2D subarray

# ---------------------------------------------------------------------------

#   24.05 longest contiguous increasing subarray
def find_longest_increasing_subarray(arr: List[int]):
    pass


#   24.25 draw the skyline
def compute_skyline(buildings: List[Building]):
    # buildings = sorted(buildings)
    skyline_seq = [0] * (buildings[-1].right - buildings[0].left + 1)

    for building in buildings:
        for point in range(building.left, building.right + 1):
            skyline_seq[point] = max(skyline_seq[point], building.height)

    return skyline_seq


#   24.31 trapping water
def calculate_trapping_water(heights: List[int]) -> int:
    # find idx of max in heights
    max_idx = 0
    max_height = heights[0]
    for idx, height in enumerate(heights):
        if height > max_height:
            max_idx = idx
            max_height = height

    def _get_capacity(seq):
        capacity = 0
        max_height = float('-inf')
        for height in seq:
            if height >= max_height:
                max_height = height
            else:
                capacity += (max_height - height)

        return capacity

    capacity_left = _get_capacity(heights[:max_idx])
    capacity_right = _get_capacity(reversed(heights[max_idx + 1:]))

    return capacity_left + capacity_right

#   24.34 road network
