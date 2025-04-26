from _3.trees.tree_node import TreeNode
from _3.trees.util import *
from collections import deque
from typing import Optional, List
from sortedcontainers import SortedList, SortedDict

def get_height(node: TreeNode) -> int:
    if node is None:
        return -1

    return max(get_height(node.left), get_height(node.right)) + 1

def _get_range_status(val, left, right) -> str:
    if val < left:
        return "left"
    elif left <= val <= right:
        return "between"
    else:
        return "right"

#   14.1    test if a binary tree satisfies a bst property
def is_bst(root: TreeNode) -> bool:
    def _is_bst_internal(node: TreeNode, minimum: float, maximum: float) -> bool:
        if not node:
            return True

        # check if this node DOES NOT violate bst rule
        if node.val < minimum or node.val > maximum:
            return False

        return _is_bst_internal(node.left, minimum, node.val) and _is_bst_internal(node.right, node.val, maximum)

    return _is_bst_internal(root, float("-inf"), float("inf"))


def is_bst_bfs(root: TreeNode) -> bool:
    queue = deque()
    queue.append((root, (float("-inf"), float("inf"))))

    while queue:
        entry = queue.popleft()
        node = entry[0]
        minimum = entry[1][0]
        maximum = entry[1][1]
        # check bst rule violation
        if node.val < minimum or node.val > maximum:
            return False

        if node.left:
            queue.append((node.left, (minimum, node.val)))

        if node.right:
            queue.append((node.right, (node.val, maximum)))

    return True


def get_right_most(node: TreeNode) -> Optional[TreeNode]:
    if node.right:
        return get_right_most(node.right)
    return node


#   14.2    find the first key greater than a given value in a bst(successor)
def find_successor(root: TreeNode, val: int):
    candidate = None
    curr_node = root
    while curr_node:
        if val < curr_node.val:
            candidate = curr_node
            curr_node = curr_node.left
        elif val >= curr_node.val:
            curr_node = curr_node.right

    return candidate


#   14.3    find k largest elements in a bst
def find_k_largest(root: TreeNode, k: int):
    res = []

    def _find_k_largest(node: TreeNode, k: int):
        if not node:
            return

        # go right
        _find_k_largest(node.right, k)
        # process this node
        if len(res) < k:
            res.append(node.val)
            _find_k_largest(node.left, k)

    _find_k_largest(root, k)
    return res


#   14.4    compute the LCA in a bst
def find_lca(root: TreeNode, node_a: TreeNode, node_b: TreeNode):
    if node_a.val > node_b.val:
        node_a, node_b = node_b, node_a

    def _find_lca(curr_node: TreeNode) -> Optional[TreeNode]:
        if not curr_node:
            return None

        if node_a.val == curr_node.val or node_b.val == curr_node.val:
            return curr_node
        elif node_a.val < curr_node.val < node_b.val:
            return curr_node
        else:
            return _find_lca(curr_node.left) if (
                    node_a.val < curr_node.val and node_b.val < curr_node.val) else _find_lca(curr_node.right)

    return _find_lca(root)


#   14.5    generate a bst from traversal data: pre, order
def generate_bst(pre_order_seq: List[int]) -> TreeNode:
    def _gen_bst(curr_seq: List[int]):
        if not curr_seq:
            return None

        curr_node_val = curr_seq[0]
        right_child_idx = 1
        while right_child_idx < len(curr_seq) and curr_seq[right_child_idx] < curr_node_val:
            right_child_idx += 1

        left = _gen_bst(curr_seq[1:right_child_idx])
        right = _gen_bst(curr_seq[right_child_idx:])
        return TreeNode(curr_node_val, left, right)

    return _gen_bst(pre_order_seq)


def generate_bst_optimal(pre_order_seq: List[int]) -> TreeNode:
    def _gen_bst(curr_root_idx, min_val, max_val) -> Optional[TreeNode]:
        # base-case
        if curr_root_idx[0] >= len(pre_order_seq): #
            return None
        curr_root_val = pre_order_seq[curr_root_idx[0]]
        if curr_root_val < min_val or curr_root_val > max_val:
            return None

        curr_root_idx[0] += 1
        left = _gen_bst(curr_root_idx, min_val, curr_root_val)
        right = _gen_bst(curr_root_idx, curr_root_val, max_val)
        return TreeNode(curr_root_val, left, right)


    curr_root_idx = [0]
    return _gen_bst(curr_root_idx, float('-inf'), float('inf'))


#   14.6    find the closest entries in three sorted arrays
def find_closest_trio(lists: List[List[int]]) -> int:

    class Node:
        def __init__(self, val, iterator):
            self.val = val
            self.iterator = iterator

        def __lt__(self, other: 'Node'):
            return self.val < other.val

        def __str__(self):
            return f"{self.val}"

    bst = SortedList()

    for idx, list in enumerate(lists):
        iterator = iter(list)
        bst.add(Node(next(iterator), iterator))

    min_dist = None

    while True:
        curr_dist = abs(bst[0].val - bst[-1].val)
        if min_dist is None or curr_dist < min_dist:
            min_dist = curr_dist

        least_node = bst.pop(0)
        next_node = next(least_node.iterator, None)
        if not next_node:
            break
        bst.add(Node(next_node, least_node.iterator))

    return min_dist


#   14.8    build a min height BST from a sorted array
def build_min_height_bst(arr: List[int]):

    def _build_bst(arr, left: int, right: int):
        if left > right:
            return None
        # base case: arr of just 1 length
        if left == right:
            return TreeNode(arr[left])

        mid_idx = left + (right - left)//2
        curr_node = TreeNode(arr[mid_idx])
        curr_node.left = _build_bst(arr, left, mid_idx - 1)
        curr_node.right = _build_bst(arr, mid_idx + 1, right)

        return curr_node

    return _build_bst(arr, 0, len(arr) - 1)


#   14.9    test if three nodes are totally ordered
def are_nodes_ordered(parent_or_desc_a: TreeNode, parent_or_desc_b: TreeNode, middle: TreeNode) -> str:
    curr_a = parent_or_desc_a
    curr_b = parent_or_desc_b

    # descend curr_a and curr_b in lock-steps till middle is reached OR reached leaf-node
    while curr_a or curr_b:
        if curr_a:
            if middle is curr_a:
                break
            elif middle.val > curr_a.val: # go right
                curr_a = curr_a.right
            else: # middle.val < curr_a.val # go left
                curr_a = curr_a.left

        if curr_b:
            if middle is curr_b:
                break
            elif middle.val > curr_b.val:  # go right
                curr_b = curr_b.right
            else:  # middle.val < curr_b.val # go left
                curr_b = curr_b.left

    parent = parent_or_desc_a if curr_a else parent_or_desc_b
    if not parent:
        return "NOT ORDERED"

    # now to find middle -> descendent
    candidate_desc = parent_or_desc_b if curr_a else parent_or_desc_a
    curr_middle = middle
    while curr_middle:
        if curr_middle.val == candidate_desc.val:
            return f"{parent.val} -> {middle.val} -> {candidate_desc.val}"
        elif curr_middle.val > candidate_desc.val:
            curr_middle = curr_middle.left
        else:
            curr_middle = curr_middle.right

    return f"{parent.val} -> {middle.val} -> None"


#   14.10   the range lookup problem, get all nodes of a binary-tree within a range
def get_range_nodes_val(root: TreeNode, rng: List[int]) -> List[int]:

    def _get_range_nodes_val(curr_node: TreeNode, left, right):
        # base-case:
        if not curr_node:
            return

        range_status = _get_range_status(curr_node.val, left, right)
        if range_status == 'left':
            _get_range_nodes_val(curr_node.right, left, right)
        elif range_status == 'between':
            _get_range_nodes_val(curr_node.left, left, right)
            res.append(curr_node.val)
            _get_range_nodes_val(curr_node.right, left, right)
        else:   # 'right'
            _get_range_nodes_val(curr_node.left, left, right)

        # in-order traversal

    res = []
    _get_range_nodes_val(root, rng[0], rng[-1])
    return res


#   14.11   add credits
class ClientCredits:
    def __init__(self):
        self.credit_to_client_bst = SortedDict()
        self.client_to_credit_map = {}

    def add_client(self, client_name: str, credit_val: int):
        if client_name in self.client_to_credit_map:
            self.remove(client_name)

            self.client_to_credit_map[client_name] = credit_val
            if credit_val in self.credit_to_client_bst:
                credit_set = self.credit_to_client_bst.get(credit_val)
                credit_set.add(client_name)
            else:
                self.credit_to_client_bst.setdefault(credit_val, {client_name})

    def remove(self, client_name):
        if client_name in self.client_to_credit_map:
            credit_val = self.client_to_credit_map[client_name]
            credit_set = self.credit_to_client_bst[credit_val]
            credit_set.remove(client_name)
            if len(credit_set) == 0:
                del self.credit_to_client_bst[credit_val]

            del self.client_to_credit_map[client_name]

    def get_max(self):
        return self.credit_to_client_bst.peekitem(index=-1)


#   todo
#       14.7

if __name__ == "__main__":
    root = build_prime_bst()
    _43 = root.right
    _37 = root.right.left.right
    _7 = root.left

    res = find_closest_trio([[3,3,6],
                             [1,5,7],
                             [4,9,10]])

    client_credits = ClientCredits()

    client_credits.add_client("Sumit", 100)
    client_credits.add_client("Aashka", 120)
    client_credits.add_client("Jim", 90)

    print(client_credits.get_max())
