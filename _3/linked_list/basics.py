from typing import List, Optional

from _3.linked_list.node import Node


def append_node(head: Node, value: int) -> Node:
    """adds new node to the tail of the list"""
    if head is None:
        return Node(value)

    curr = head
    while curr.next is not None:
        curr = curr.next

    new_node = Node(value)
    curr.next = new_node

    return head


def copy_list(head: Node) -> Optional[Node]:
    """takes a list and returns a complete copy of the list"""
    if not head:
        return None

    new_head = Node(head.val)
    new_curr = new_head

    curr = head.next
    while curr:
        new_node = Node(curr.val)

        new_curr.next = new_node

        new_curr = new_node
        curr = curr.next

    return new_head

def length(head: Node) -> int:
    list_len = 0
    curr = head

    while curr:
        list_len = list_len + 1
        curr = curr.next

    return list_len


def push(curr_head: Node, val) -> Node:
    """adds a single node to the head of the list"""
    new_node = Node(val, curr_head)
    # new_node.next = curr_head
    return new_node


# count number of times a given int occurs in a list
def get_count(head: Node, val: int) -> int:
    curr = head
    count = 0
    while curr:
        if curr.val == val:
            count += 1
        curr = curr.next

    return count


# get nth
def get_nth(head: Node, n: int) -> Optional[Node]:
    curr_idx = 0
    curr = head
    while curr:
        if curr_idx == n:
            return curr
        curr_idx += 1
        curr = curr.next

    return None

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


# append list b to a
def append(head_a: Node, head_b: Node) -> Node:
    if not head_a:
        return head_b
    elif not head_b:
        return head_a

    curr_a = head_a
    while curr_a.next is not None:
        curr_a = curr_a.next

    # curr_a is now tail of list a
    curr_a.next = head_b

    return head_a

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


def _create_list(arr: List[int]) -> Node:

    head = Node(arr[0])
    curr = head

    for elem in arr[1:]:
        new_node = Node(elem)
        curr.next = new_node
        curr = new_node

    return head

def _print_list(head: Node):
    if not head:
        print("empty list!")
        return

    list_elem : List[str] = []
    curr = head
    while curr:
        list_elem.append(str(curr.val))
        curr = curr.next
    print("->".join(list_elem))


if __name__ == "__main__":
    print("main!")

    curr_list = _create_list([1,2,3,4,5])

    _print_list(get_nth(curr_list, 5))
