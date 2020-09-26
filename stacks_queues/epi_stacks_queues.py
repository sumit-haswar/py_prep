from typing import List, Iterator
from binary_tree import TreeNode
from collections import deque


# -- stacks --
#   8.1 stack with max api
class MaxStack():

    def __init__(self):
        self._stack = []

    def push(self, val):
        if self._stack:
            top = self._stack[-1]
            self._stack.append((val, max(val, top[1])))
        else:
            self._stack.append((val, val))

    def pop(self):
        return self._stack.pop()[0]

    def get_max(self):
        return self._stack[-1][1]


#   8.2 evaluate RPN (reverse polish notation)
def evaluate_rpn_expression(exp: str) -> int:
    calc = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: (int)(x / y)
    }
    stack = []
    for curr in exp.split(' '):
        if curr not in calc:
            stack.append(int(curr))
        else:
            y = stack.pop()
            x = stack.pop()
            result = calc[curr](x, y)
            stack.append(result)

    return stack.pop()


#   8.3 is a string well-formed
def is_string_well_formed(s: str):
    look_up = {'}': '{', ']': '[', ')': '('}
    stack = []
    for ch in s:
        if ch not in look_up:
            stack.append(ch)
        else:
            top = stack.pop()
            if top != look_up[ch]:
                return False

    return not stack


# todo  8.4 normalize path-names

#   (8.5) compute buildings with sunset-view
def get_sunset_view(itr: Iterator[int]) -> List[int]:
    """
    Input stream is in east to west direction
    :param itr:
    :return:
    """
    stack = []
    for idx, building in enumerate(itr):
        if stack:
            top = stack[-1]
            while building > top['height']:
                stack.pop()
                if not stack:
                    break
                top = stack[-1]

        stack.append({'idx': idx, 'height': building})

    return [elem['idx'] for elem in reversed(stack)]


# -- -- -- -- queues -- -- -- --

#   8.6 compute binary tree nodes in order of inc. depth
def get_tree_nodes_by_level(root: TreeNode) -> List[List[int]]:
    curr = deque()
    next = deque()
    curr.append(root)
    result = []
    curr_level = []
    while curr:
        node = curr.popleft()
        curr_level.append(node.data)
        if node.left:
            next.append(node.left)
        if node.right:
            next.append(node.right)

        # current level is done
        if not curr:
            result.append(curr_level)
            curr_level = []
            # swap curr and next queues
            temp = next
            next = curr
            curr = temp

    return result


#   8.7 implement a circular queue
class ArrayQueue():

    def __init__(self, capacity=10):
        self._q = [0] * capacity
        self.head = self.tail = self.count = 0

    def size(self):
        return self.count

    def enqueue(self, elem):
        if len(self._q) == self.count:  # resize
            self._q = (self._q[self.head:] + self._q[:self.head])
            self.head, self.tail = 0, self.count
            self._q = self._q + [0] * (len(self._q) * 2 - len(self._q))

        self._q[self.tail] = elem
        self.tail = (self.tail + 1) % len(self._q)
        self.count += 1

    def dequeue(self) -> int:
        # always dequeue from head and decrement
        result = self._q[self.head]
        self.head = (self.head + 1) % len(self._q)
        self.count -= 1
        return result


#   8.8 implement a queue using stack
class StackQueue():

    def __init__(self):
        self._en = []
        self._de = []

    def enqueue(self, elem):
        self._en.append(elem)

    def dequeue(self):
        if not self._de:
            while self._en:
                self._de.append(self._en.pop())
        return self._de.pop()


#   (8.9) implement a queue with max api
class MaxQueue():

    def __init__(self):
        self._q = deque()
        self._dq = deque()

    def enqueue(self, val: int) -> None:
        self._q.append(val)
        while self._dq and (val > self._dq[-1]):
            self._dq.pop()
        self._dq.append(val)

    def dequeue(self) -> int:
        result = self._q.popleft()
        if self._dq[0] == result:
            self._dq.popleft()
        return result

    def get_max(self) -> int:
        return self._dq[0]
