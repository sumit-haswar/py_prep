from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = {} if children is None else children


def traverse_bfs(root : TreeNode) -> List:
    res = []

    if root is None:
        return []

    curr_q = deque()
    next_q = deque()
    curr_res = []

    curr_q.append(root)

    while curr_q:
        curr_node = curr_q.popleft()
        curr_res.append(curr_node.val)

        # add all children of current into next_q
        for key, val in curr_node.children.items():
            next_q.append(val)

        if not curr_q:
            res.append(curr_res.copy())
            curr_res = []
            # todo swap curr_q and next_q


    print(res)
    return res