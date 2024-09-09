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


# pop, takes a non-empty list and deletes the head node and returns it
def pop(head: Node) -> (Node, Node):
    if head is None:
        raise Exception("head node is None")

    if head.next is None:
        return head, None

    new_head = head.next
    head.next = None

    return head, new_head


# insert nth, inserts a new node at the n-th index of the linked list
def insert_nth(head: Node, n: int, val: int) -> Node:
    if head is None:
        raise Exception("head node is None")

    if n == 0:
        new_node = Node(val)
        new_node.next = head
        return new_node

    # iter till we get to n-1
    curr_idx = 0
    curr_node = head

    while curr_node is not None:
        if curr_idx == (n - 1):
            new_node = Node(val)

            new_node.next = curr_node.next
            curr_node.next = new_node
            return head
        curr_idx += 1
        curr_node = curr_node.next

    # check if its to be added to the tail
    if curr_idx == (n - 1) and curr_node is not None:
        new_node = Node(val)
        curr_node.next = new_node

    return head


# sorted-insert, given a sorted linked-list add a new node to its correct sorted position
def sorted_insert(head: Node, val: int) -> Node:
    new_node = Node(val)

    if head is None:
        return new_node

    # check if node is to be added to head
    if head.val >= val:
        new_node.next = head
        return new_node

    curr_node = head
    while curr_node.next:
        if curr_node.next.val >= val:
            new_node.next = curr_node.next
            curr_node.next = new_node
            return head
        curr_node = curr_node.next

    # reached end of the linked-list
    curr_node.next = new_node

    return head


# insert sort, given an unsorted list, re-arrange node so they are sorted in increasing order
def insert_sort(head: Node) -> Node:
    res_list_head = None

    curr_head = head
    while curr_head:
        res_list_head = sorted_insert(res_list_head, curr_head.val)
        curr_head = curr_head.next

    return res_list_head


# insert sort, given an unsorted list, re-arrange node so they are sorted in increasing order
def insert_sort_in_place(head: Node) -> Node:
    pass


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
    if head is None or head.next is None:
        return head, None

    slow = head
    fast = head.next

    while fast:
        if fast.next is None:
            break
        fast = fast.next.next
        slow = slow.next

    back = slow.next
    slow.next = None
    return head, back


# remove duplicates from a sorted list
def remove_duplicates(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    curr_node = head
    next_node = head.next
    while curr_node:

        # keep iterating will we find a diff node
        while next_node and curr_node.val == next_node.val:
            next_node = next_node.next

        curr_node.next = next_node

        curr_node = next_node
        next_node = next_node.next if next_node else None

    return head


# move-node
# takes two lists, removes the front node from the second list and pushes
# it onto the front of the first.
def move_node(head_to: Node, head_from: Node) -> (Node, Node):
    new_head_from = head_from.next
    head_from.next = head_to

    return head_from, new_head_from


# alternating split
# for [a, b, a, b, a], one sublist should be {a, a, a} and the other should be {b, b}
def alt_split(head: Node) -> (Node, Node):
    if head is None or head.next is None:
        return head, None

    a_head = head
    b_head = head.next
    curr_a = a_head
    curr_b = b_head

    while curr_a and curr_b:
        curr_a.next = curr_b.next
        curr_b.next = curr_b.next.next if curr_b.next else None

        curr_a = curr_a.next
        curr_b = curr_b.next

    return a_head, b_head


# shuffle merge
# [1, 2, 3] and [7, 13, 17] should yield [1, 7, 2, 13, 3, 1]
def shuffle_merge(head_a: Node, head_b: Node) -> Node:
    if head_a is None or head_b is None:
        return head_a if head_a else head_b

    curr_a = head_a
    curr_b = head_b

    while curr_a and curr_b:
        next_a = curr_a.next
        next_b = curr_b.next

        curr_a.next = curr_b
        curr_b.next = next_a if next_a else next_b

        curr_a = next_a
        curr_b = next_b

    return head_a


# sorted merge
# takes two lists, each of which is sorted in increasing order and merges
# the two together into one list which is also in increasing order.
def sorted_merge(head_a: Node, head_b: Node) -> Node:
    if head_a is None or head_b is None:
        return head_a if head_a else head_b

    # create two nodes: curr which is lesser val and candidate which is the other linked-lest head
    if head_a.val <= head_b.val:
        head = head_a
        curr = head_a
        candidate = head_b
    else:
        head = head_b
        curr = head_b
        candidate = head_a

    while curr and candidate:
        # one list has exhausted, we can break now
        if curr.next is None:
            curr.next = candidate
            break

        # if candidate is lesser than current's next, then we need to swap!
        if candidate.val < curr.next.val:
            next = curr.next
            curr.next = candidate
            curr = candidate
            candidate = next
        else:
            curr = curr.next

    return head


# merge sort, using front-back split and sorted-merge
def merge_sort(head: Node) -> Optional[Node]:
    # base case a single node ll is already sorted
    if head is None or head.next is None:
        return head

    # divide ll into two
    front, back = front_back_split(head)

    # sort left and right individually
    left = merge_sort(front)
    right = merge_sort(back)

    # final step in recursion: combine the result
    return sorted_merge(left, right)


# sorted intersect,
# Given two lists sorted, create and return a new list representing the intersection of the two lists.
def sorted_intersect(head_a: Node, head_b: Node) -> Node:
    head = Node(None)
    curr = head

    curr_a = head_a
    curr_b = head_b

    while curr_a and curr_b:
        if curr_a.val == curr_b.val:
            new_node = Node(curr_a.val)
            curr.next = new_node
            curr = curr.next

            curr_a = curr_a.next
            curr_b = curr_b.next
        elif curr_a.val < curr_b.val:
            curr_a = curr_a.next
        else:
            curr_b = curr_b.next

    return head.next


# reverse - iterative
def reverse(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    back = None
    curr = head
    front = head.next

    while front:
        curr.next = back
        back = curr

        curr = front
        front = front.next

    curr.next = back

    return curr


# reverse - recursive
def reverse_recur(curr_node: Node) -> Optional[Node]:
    # base-case
    if curr_node.next is None:
        return curr_node

    # recur is the next of curr_node
    recur = reverse_recur(curr_node.next)

    # flip the linkage from curr_node --> recur to recur --> curr_node
    curr_node.next.next = curr_node

    # break the circular linkage
    curr_node.next = None

    # `recur` is the og tail and now new head of the ll and needs to be propagated all the
    # way to the top
    return recur


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

    list_elem: List[str] = []
    curr = head
    while curr:
        list_elem.append(str(curr.val))
        curr = curr.next
    print("->".join(list_elem))


if __name__ == "__main__":
    curr_list_1 = _create_list([5, 6, 9, 2, 1])

    a = reverse_recur(curr_list_1)
    _print_list(a)
