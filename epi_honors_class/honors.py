from typing import List
from linked_list import Node
from binary_tree import TreeNode
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

class HeadAndTail:
    def __init__(self,head, tail):
        self.head = head
        self.tail = tail

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


#
def find_first_missing_positive(arr: List[int]) -> int:
    # one approach: sort arr, look for 0
    # and move right till missing entry found

    # another approach is to use hashtable A --> S and
    # iter from 1 to len(arr)

    # set A[k-1] to k

    for idx, elem in enumerate(arr):
        if elem > 0:
            pass


#   24.05
def find_longest_increasing_subarray(arr: List[int]):
    pass


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


#   24.07 rook attach
def rook_attack(matrix: List[List[int]]):
    pass


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
    # pad spaces to the right of the last line
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


#   24.13 compute fair bonuses
def calculate_bonus(productivity: List[int]):
    pass


#   24.14
def binary_search_unknown_length(seq: List[int], k: int):
    pass


#   24.18 find line through most points

#   24.19 convert a sorted doubly linked list into a BST

#   24.20 convert a bst to sorted doubly linked list
def bst_to_doubly_linked_list(root: TreeNode) -> TreeNode:
    def _bst_to_doubly_linked_list(treenode: TreeNode):
        if treenode is None:
            return HeadAndTail(head=None, tail=None)

        left = _bst_to_doubly_linked_list(treenode.left)
        right = _bst_to_doubly_linked_list(treenode.right)

        # check if left has tail, then point left.tail --> curr-node
        if left.tail:
            left.tail.right = treenode
        treenode.left = left.tail

        # merge right to current node
        if right.head:
            right.head.left = treenode
        treenode.right = right.head

        # now, curr head and tail is: left (if present) and right (if present)
        return HeadAndTail(left.head or treenode, right.tail or treenode)


    return _bst_to_doubly_linked_list(root).head


#   24.22 implement regular expression matching
def is_match(regex: str, s: str) -> bool:
    def _is_match(regex: str, s: str) -> bool:
        # blank regex matches anything
        if not regex:
            return True

        if regex == '$':
            # string should now be empty
            return not s

        # if regex is <<something>>*
        if len(regex) >= 2 and regex[1] == "*":
            # check for <<something>>*
            # start with second-char of string and compare previous
            string_pivot = 1
            while string_pivot <= len(s) and regex[0] in ('.', s[string_pivot - 1]):
                if _is_match(regex[2:], s[string_pivot:]):
                    return True
                string_pivot += 1

            return _is_match(regex[2:], s)

        # lock-step comparison for direct match and .,
        # recur for rest
        return (s and regex[0] in ('.', s[0])) \
               and _is_match(regex[1:], s[1:])

    if regex[0] == "^":
        return _is_match(regex[1:], s)

    return any([_is_match(regex, s[pivot:]) for pivot in range(len(s) + 1)])


#   24.29 find the maximum 2D subarray

#   24.23 synthesize an expression

# ---------------------------------------------------------------------------


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


#   24.35 test if arbitrage is possible
def is_arbitrage_exist():
    pass


def _reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
