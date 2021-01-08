import typing
from typing import List, Optional
from binary_tree import TreeNode
import collections
from sortedcontainers import SortedList, SortedDict


#   14.1 test if bt satisfies the bst property
def is_bst(root: TreeNode):
    def _is_bst(node: TreeNode, lower_bound, upper_bound):
        if node is None:
            return True

        if node.data < lower_bound or node.data > upper_bound:
            return False

        return _is_bst(node.left, lower_bound, node.data) \
               and _is_bst(node.right, node.data, upper_bound)

    return _is_bst(root, float('-inf'), float('inf'))


def is_bst_bfs(root: TreeNode) -> bool:
    queue = collections.deque()

    # add root to queue
    queue.append({'node': root,
                  'lower': float('-inf'),
                  'upper': float('inf')})

    while queue:
        curr = queue.popleft()
        # check if curr violates bst:
        if curr['node'].data < curr.get('lower') \
                or curr['node'].data > curr.get('upper'):
            return False

        if curr['node'].left:
            queue.append({'node': curr['node'].left,
                          'lower': float('-inf'),
                          'upper': curr['node'].data})
        if curr['node'].right:
            queue.append({'node': curr['node'].right,
                          'lower': curr['node'].data,
                          'upper': float('inf')})

    return True


#   14.2 find the first greater than a given value in a bst
def find_greater_than_k(root: TreeNode, k: int) -> TreeNode:
    curr = root
    candidate = None
    while curr:
        if curr.data > k:  # go left
            candidate = curr
            curr = curr.left
        else:  # go right
            curr = curr.right

    return candidate


#   14.3 find kth largest elements in a bst
def find_k_largest(root: TreeNode, k: int):
    def _find_k_largest(node: TreeNode, seq: List[int]):
        # reverse in-order traversal
        if node is None or len(seq) >= k:
            return
        _find_k_largest(node.right, seq)
        if len(seq) < k:
            seq.append(node.data)
            _find_k_largest(node.left, seq)

    seq = []
    _find_k_largest(root, seq)
    return seq


#   14.4 compute the lca in a bst
def get_lca(root: TreeNode, a: int, b: int):
    def _get_lca(node: TreeNode, a: int, b: int):
        if a <= node.data <= b:
            return node
        elif a < node.data and b < node.data:
            # go left
            return _get_lca(node.left, a, b)
        else:
            # go right
            return _get_lca(node.right, a, b)

    if b < a:
        a, b = b, a

    return _get_lca(root, a, b)


def get_lca_iter(root: TreeNode, node_a: int, node_b: int):
    # wlog assume node_a < node_b
    if node_a > node_b:
        node_a, node_b = node_b, node_a

    curr = root
    while curr:
        if node_a < curr.data < node_b:
            return curr
        elif node_a < curr.data and node_b < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    return None


#   14.5 reconstruct a bst from traversal data
def build_bst_from_preorder(seq: List[int]):
    def _build_bst_from_preorder(left: int, right: int) -> Optional[TreeNode]:
        if left > right or left > len(seq) or right > len(seq):
            return None

        idx = left + 1
        while idx < len(seq) and seq[idx] < seq[left]:
            idx += 1
        # idx now points to root element of right tree
        return TreeNode(seq[left],
                        _build_bst_from_preorder(left + 1, idx - 1),
                        _build_bst_from_preorder(idx, right))

    return _build_bst_from_preorder(0, len(seq) - 1)


def build_bst_from_preorder_optimal(seq: List[int]):
    """post-order building using the lower bound and upper-bound paradigm"""

    def _build_bst_from_preorder_optimal(lower_bound, upper_bound):
        # end of list
        if curr_root_idx[0] >= len(seq):
            return None

        root_val = seq[curr_root_idx[0]]
        if not (lower_bound < root_val < upper_bound):
            return None

        # recur left
        curr_root_idx[0] += 1
        left = _build_bst_from_preorder_optimal(lower_bound, root_val)
        # recur right
        right = _build_bst_from_preorder_optimal(root_val, upper_bound)

        # build this node
        return TreeNode(root_val, left, right)

    curr_root_idx = [0]
    return _build_bst_from_preorder_optimal(float('-inf'), float('inf'))


#   14.6 find the closest entries in 3 sorted arrays
#   solving for the general case of k sorted-arrays
def find_closest_elements_in_sorted_array(list_of_list: List[List[int]]):
    class Node(object):
        def __init__(self, val, iterator):
            self.val = val
            self.iterator = iterator

        def __lt__(self, other):
            return self.val < other.val

    bst = SortedList()

    for idx, list in enumerate(list_of_list):
        # add following data to bst: iter of the list, its first val and
        iterator = iter(list)
        min_val = next(iterator, None)
        if min_val:
            bst.add(Node(min_val, iterator))

    min_distance_so_far = float('inf')
    while True:
        curr_distance = abs(bst[0].val - bst[-1].val)
        min_distance_so_far = min(curr_distance, min_distance_so_far)

        min_node = bst.pop(0)
        next_node = next(min_node.iterator, None)
        if next_node is None:
            # one of the list has exhausted,
            # min_distance_so_far can only increase from here
            return min_distance_so_far
        else:
            bst.add(Node(next_node, min_node.iterator))


#   14.8 build a min height bst from a sorted array
def create_bst(seq: List[int]):
    def _create_bst(left: int, right: int):
        if left > right:
            return None

        mid_idx = left + (right - left) // 2

        return TreeNode(seq[mid_idx],
                        _create_bst(left, mid_idx - 1),
                        _create_bst(mid_idx + 1, right))

    return _create_bst(0, len(seq) - 1)


#   (14.9) test if three bst nodes are totally ordered
def pair_includes_ancestor_and_descendant_of_m(candidate_0, candidate_1, node):
    # ascend in lock steps from candidate_0 and candidate_1 till you find node
    curr_0 = candidate_0
    curr_1 = candidate_1
    ancestor = None
    while curr_0 or curr_1:
        if (curr_0 and curr_0.data == node.data) or (curr_1 and curr_1.data == node.data):
            # todo assign ancestor
            ancestor = candidate_0 if curr_0 and curr_0.data == node.data else candidate_1
            break
        else:
            if curr_0:
                curr_0 = curr_0.left if node.data < curr_0.data else curr_0.right

            if curr_1:
                curr_1 = curr_1.left if node.data < curr_1.data else curr_1.right

    # none of the candidates are node's ancestor
    if ancestor is None:
        return False

    possible_descendant = candidate_0 if candidate_1 is ancestor else candidate_1

    curr_node = node
    while curr_node:
        if curr_node.data == possible_descendant.data:
            return True
        else:
            curr_node = curr_node.left \
                if possible_descendant.data < curr_node.data else curr_node.right

    return False


#   (14.10) the range lookup problem
def get_range_in_bst(root: TreeNode, lower: int, upper: int) -> List[int]:
    def _get_range_in_bst(node, seq):
        if not node:
            return
        # if this node is between upper and lower
        if lower <= node.data <= upper:
            # perform inorder traversal
            _get_range_in_bst(node.left, seq)
            seq.append(node.data)
            _get_range_in_bst(node.right, seq)
        elif node.data > upper:
            _get_range_in_bst(node.left, seq)
        else:
            _get_range_in_bst(node.right, seq)

    seq = []
    _get_range_in_bst(root, seq)
    return seq


#   ____________________  augmented BSTs ____________________
#   (14.11) add credits
class ClientsCreditsInfo:

    def __init__(self):
        # key is client-id
        self.hash_map = {}
        # key is credit, value is set
        self.bst = SortedDict()
        self.CREDIT = 0

    def insert(self, client_id, credit):
        self.remove(client_id)

        # add to hash-table
        self.hash_map[client_id] = credit

        # add to bst
        if credit not in self.bst:
            # add new node
            self.bst[credit] = set()
            self.bst[credit].add(client_id)
        else:
            self.bst[credit].add(client_id)

    def remove(self, client_id: str):
        if client_id in self.hash_map:
            credit = self.hash_map[client_id]

            # remove from bst
            self.bst[credit].remove(client_id)
            if not self.bst[credit]:
                del self.bst[credit]

            # remove from hash_map
            del self.hash_map[client_id]

    def lookup(self, client_id: str):
        credit = self.hash_map.get(client_id, None)
        if credit:
            return {'client_id': client_id,
                    'credit': credit + self.CREDIT}
        else:
            return None

    def get_max(self):
        return self.bst.peekitem()[1]

#   todo (14.7) enumerate extended integers
