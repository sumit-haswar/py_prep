from node import Node
from typing import List, Optional


def length(head: Node) -> int:
    pass


def push(curr_head: Node, val) -> Node:
    pass


# count
def get_count(head: Node, val: int) -> int:
    pass


# get nth
def get_nth(head: Node, n: int) -> Node:
    pass


# pop
def pop(head: Node) -> Node:
    pass


# insert nth
def insert_nth(head: Node, n: int, val: int) -> Node:
    pass


# sorted-insert
def sorted_insert(head: Node, val: int) -> Node:
    pass


# insert sort


# append list a to b
def append(head_a: Node, head_b: Node) -> Node:
    pass


# front back split
# Given a list, split it into two sub-lists — one for the front half, and one for the back half. If
# the number of elements is odd, the extra element should go in the front list.
def front_back_split(head: Node) -> (Node, Node):
    pass


# remove duplicates from a sorted list
def remove_duplicates(head: Node) -> Node:
    pass


# move-node
# takes two lists, removes the front node from the second list and pushes
# it onto the front of the first.
def move_node(head_to: Node, head_from: Node) -> (Node, Node):
    pass


# alternating split
# for {a, b, a, b, a}, one sublist should be {a, a, a} and the other should be {b, b}
def alt_split(head: Node) -> (Node, Node):
    pass


# shuffle merge
# {1, 2, 3} and {7, 13, 17} should yield {1, 7, 2, 13, 3, 1}
def shuffle_merge(head_a: Node, head_b: Node) -> Node:
    pass


# sorted merge
# takes two lists, each of which is sorted in increasing and merges
# the two together into one list which is in increasing order.
def sorted_merge(head_a: Node, head_b: Node) -> Node:
    pass


# merge sort, using front-back split and sorted-merge
def merge_sort(head: Node) -> Node:
    pass


# sorted intersect,
# Given two lists sorted, create and return a new list representing the intersection of the two lists.
def sorted_intersect(head_a: Node, head_b: Node) -> Node:
    pass


# reverse - iterative
def reverse(head: Node) -> Node:
    pass


# reverse - recursive
def reverse_recur(node: Node) -> Optional[Node]:
    pass

def create_linked_list(expr: str) -> Node:
    pass

def _create_list(arr: List[int]):
    pass


def _print_list(head: Node):
    pass


if __name__ == "__main__":
    pass
