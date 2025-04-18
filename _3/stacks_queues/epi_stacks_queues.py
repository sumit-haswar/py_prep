from _3.trees.tree_node import TreeNode
from typing import List, Optional
from collections import deque

class StackEntry:
    def __init__(self, elem, max):
        self.elem = elem
        self.max = max

# 8.1 implement a stack with max api
class MaxStack:

    def __init__(self):
        self._stack : List = []

    def get_max(self):
        return self._stack[-1].max

    def push(self, elem):
        if not self._stack:
            self._stack.append(StackEntry(elem, elem))
        else:
            top = self._stack[-1]
            self._stack.append(StackEntry(elem, max(elem, top.max)))

    def pop(self):
        return self._stack.pop().elem


# 8.6 compute binary tree nodes in order of increasing depth
def get_level_order_traversal(root: TreeNode):
    if not root:
        return []

    curr = deque() # [root]
    next = deque()
    res = []
    curr_level = []

    curr.append(root)

    while curr:
        node = curr.popleft()
        curr_level.append(node.val)

        if node.left:
            next.append(node.left)

        if node.right:
            next.append(node.right)

        if not curr:
            # write curr_level to result
            res.append([x for x in curr_level])
            curr_level = []

            # swap curr and next queues
            temp = curr
            curr = next
            next = temp

    return res


# 8.2 evaluate RPN expressions
def eval_rpn_expression(exp: str):
    stack = []
    tokens = exp.split(",")
    operators = {"*", "+", "/", "-"}
    for token in tokens:
        if token in operators:
            match token:
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    stack.append(stack.pop() - stack.pop())
                case "/":
                    stack.append(stack.pop() // stack.pop())
        else:
            stack.append(_parse_int(token))

    return stack[0] if stack else None


# 8.7 implement a circular queue(using arrays)
class CircularQueue:

    def __init__(self):
        self._arr = [0] * 5     # initiate by size 5
        self._head = 0
        self._tail = 0
        self._count = 0

    def enq(self, elem):

        if self._count == len(self._arr): # time to re-size
            new_arr = [0] * 2 * len(self._arr)

            idx = 0
            # copy from head to end
            for e in self._arr[self._head:]:
                new_arr[idx] = e
                idx += 1

            # copy from front to tail
            for e in self._arr[:self._tail]:
                new_arr[idx] = e
                idx += 1

            self._arr = new_arr
            self._head = 0
            self._tail = idx

        self._arr[self._tail] = elem
        self._tail = (self._tail + 1) % len(self._arr)
        self._count += 1


    def dq(self) -> int:
        if self._count == 0:
            raise Exception("empty queue")

        elem = self._arr[self._head]
        self._arr[self._head] = 0

        self._head = (self._head + 1) % len(self._arr)

        self._count -= 1

        return elem



# 8.3 is a string well-formed
def is_string_well_formed(expr: str) -> bool:
    stack = []
    lookup = {
        "}" : "{",
        "]" : "[",
        ")": "("
    }
    for token in expr:
        if token in lookup:
            # found a closing token, check if latest is matching
            if not stack:
                return False
            top = stack.pop()
            if top != lookup[token]:
                return False
        else:
            stack.append(token)


    return len(stack) == 0


# 8.8 implement a queue using stacks
class MyQueue:

    def __init__(self):
        self._en_stack = []
        self._dq_stack = []

    def en(self, elem):
        self._en_stack.append(elem)

    def dq(self):
        if not self._en_stack and not self._dq_stack:
            raise Exception("queue empty")

        # if self._dq_stack:
        #     return self._dq_stack.pop()
        if not self._dq_stack:
            while self._en_stack:
                self._dq_stack.append(self._en_stack.pop())

        return self._dq_stack.pop()

# 8.5 compute buildings with a sunset view
def compute_sunset_view_buildings(buildings: List[int]) -> List[int]:
    stack : List = []
    for idx, building_height in enumerate(buildings):
        if not stack:
            stack.append((idx, building_height))
        else:
            while stack and stack[-1][1] <= building_height:
                stack.pop()
            stack.append((idx, building_height))

    return [x[0] for x in stack]


# 8.9 implement a queue with max api
class MaxQueue:
    def __init__(self):
        self._queue = deque()
        self._max_candidate = deque()

    def en(self, elem):
        self._queue.append(elem)
        # keep popping _max_candidate from right till you find
        while self._max_candidate and self._max_candidate[-1] < elem:
            self._max_candidate.pop()

        self._max_candidate.append(elem)

    def dq(self):
        elem = self._queue.popleft()
        if elem == self._max_candidate[0]:
            self._max_candidate.popleft()
        return elem

    def get_max(self):
        return self._max_candidate[0]

# todo
#   8.4 normalize path-names


def _parse_int(s : str) -> Optional[int]:
    try:
        return int(s)
    except:
        return None

if __name__ == "__main__":
    # max_stack = MaxStack()
    #
    # for n in [8,5,7,12,4,13]:
    #     max_stack.push(n)
    #     print(max_stack.get_max())
    #
    # max_stack.pop()
    # print(is_string_well_formed("{(){[]}()}"))
    q = MaxQueue()

    q.en(5)
    q.en(66)
    q.en(7)
    q.en(8)

    print(q.get_max())
    q.dq()
    q.dq()
    print(q.get_max())
