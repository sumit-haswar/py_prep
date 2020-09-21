from .node import Node
from .util import create_list, length
import typing


#   7.1 merge two sorted lists
def merge_sorted_list(head_a: Node, head_b: Node) -> Node:
    if not head_a or not head_b:
        return head_a if not head_b else head_b

    if head_a.data < head_b.data:
        head = head_a
        curr = head_a
        candidate = head_b
    else:
        head = head_b
        curr = head_b
        candidate = head_a

    while curr and candidate:
        if curr.next is None:
            curr.next = candidate
            break
        if curr.next.data > candidate.data:
            next = curr.next
            curr.next = candidate
            # curr = candidate
            candidate = next
        else:
            curr = curr.next

    return head


#   7.2 reverse a single sublist
def reverse_sublist(head, start, end):
    sublist_start = head
    curr = 1
    # get to one node before the sublist start
    while curr < (start - 1):
        sublist_start = sublist_start.next
        curr += 1

    sublist_head = sublist_start
    sublist_start = sublist_start.next

    back = None
    middle = sublist_start
    front = sublist_start.next

    for _ in range(end - start):
        middle.next = back
        back = middle
        middle = front
        front = front.next

    middle.next = back
    sublist_head.next = middle
    sublist_start.next = front

    # return sublist_head if head is sublist_head else head
    return head


#   7.3 test for cyclic-ity
def get_cycle_head(head: Node) -> Node:
    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            # cycle detected, find the head
            slow = head
            # move in lock-steps
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None


#   7.4 test for overlapping lists, lists are cycle-free
def get_overlap_head(head_a: Node, head_b: Node) -> Node:
    curr_a = head_a
    curr_b = head_b

    curr_a_len = length(curr_a)
    curr_b_len = length(curr_b)

    if curr_b_len > curr_a_len:
        curr_a = head_b
        curr_b = head_a

    for _ in range(abs(curr_a_len - curr_b_len)):
        curr_a = curr_a.next

    # move in lock-steps
    while curr_a and curr_b and curr_a is not curr_b:
        curr_a = curr_a.next
        curr_b = curr_b.next

    return curr_a


#   7.5 test for overlapping lists, lists may have cycles
def get_overlap_node_cyclic(head_a: Node, head_b: Node) -> Node:
    pass


#   7.6 delete a node from a singly linked list
def delete_node(node: Node) -> None:
    node.data = node.next.data
    node.next = node.next.next


#   7.7 remove the kth last element from a linked-list
def remove_last_kth_node(head: Node, k: int) -> None:
    curr = head
    fwd = head

    for _ in range(k + 1):
        fwd = fwd.next

    # move in lock-steps
    while fwd:
        curr = curr.next
        fwd = fwd.next

    # curr.next is to be removed
    curr.next = curr.next.next


#   7.8 remove dupes from a sorted linked-list
def remove_duplicates(head: Node):
    curr = head
    next = curr.next

    # find next diff node
    while curr:
        while next and curr.data == next.data:
            next = next.next

        # next is now a diff node
        curr.next = next
        curr = next
        if next:
            next = curr.next

    return head


#   7.10 implement even-odd merge
def even_odd_merge(head: Node) -> Node:
    pass


#   7.11 test whether a singly linked list is palindromic
def is_palindromic(head):
    # find middle of the list using slow-fast pointer
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # slow is in middle for odd length
    # slow is the first node of the second half

    # reverse the list in-place from slow to end
    # now compare head -> middle and middle -> end in lock-steps
    fast = _reverse(slow)
    slow = head
    while slow and fast:
        if slow.data != fast.data:
            return False
        slow = slow.next
        fast = fast.next

    return True


def _reverse(list):
    if list is None or list.next is None:
        return list

    back = None
    middle = list
    front = list.next

    while front is not None:
        middle.next = back
        back = middle
        middle = front
        front = front.next

    middle.next = back
    return middle
