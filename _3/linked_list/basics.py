from node import Node
from typing import List, Optional


def length(head: Node) -> int:
    cnt = 0
    curr = head
    while curr:
        cnt += 1
        curr = head.next

    return cnt


def push(curr_head: Node, val) -> Node:
    if curr_head is None:
        return Node(val)

    new_node = Node(val)
    new_node.next = curr_head
    return new_node


# count
def get_count(head: Node, val: int) -> int:
    cnt = 0
    curr = head
    while curr:
        if curr.val == val:
            cnt += 1
        curr = head.next

    return cnt


# get nth
def get_nth(head: Node, n: int) -> Node:
    curr = head
    curr_idx = 0
    while curr is not None:
        if curr_idx == n:
            return curr
        curr = curr.next
        curr_idx += 1

    raise Exception("invalid value of n")


# pop
def pop(head: Node) -> Node:
    if head is None:
        raise Exception("null head node")
    new_head = head.next
    head.next = None
    return new_head


# insert nth
def insert_nth(head: Node, n: int, val: int) -> Node:
    if n == 0:
        new_node = Node(val)
        new_node.next = head
        return new_node

    curr_idx = 0
    curr = head
    while curr:
        if curr_idx == (n - 1):
            new_node = Node(val)
            new_node.next = curr.next
            curr.next = new_node
        curr = curr.next
        curr_idx += 1

    return head


# sorted-insert
def sorted_insert(head: Node, val: int) -> Node:
    if head.val > val:
        new_node = Node(val)
        new_node.next = head
        return new_node

    curr = head
    while curr and curr.next:
        if curr.next.val >= val:
            new_node = Node(val)
            new_node.next = curr.next
            curr.next = new_node
            return head
        curr = curr.next

    # add at tail
    new_node = Node(val)
    curr.next = new_node

    return head


# insert sort


# append list a to b
def append(head_a: Node, head_b: Node) -> Node:
    if not head_a:
        return head_b

    curr = head_a
    while curr.next:
        curr = curr.next

    curr.next = head_b
    return head_a


# front back split
# Given a list, split it into two sub-lists — one for the front half, and one for the back half. If
# the number of elements is odd, the extra element should go in the front list.
def front_back_split(head: Node) -> (Node, Node):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast_next = fast.next
        fast = fast_next.next

    head_b = slow.next
    slow.next = None

    return (head, head_b)


# remove duplicates from a sorted list
def remove_duplicates(head: Node) -> Node:
    if not head.next:
        return head

    curr = head
    next = curr.next
    while curr and next:
        while curr.val == next.val:
            next = next.next
            if not next:
                break

        curr.next = next
        curr = next
        next = next.next if next else None

    return head


# move-node
# takes two lists, removes the front node from the second list and pushes
# it onto the front of the first.
def move_node(head_to: Node, head_from: Node) -> (Node, Node):
    if not head_from:
        return head_to, None

    node = head_from.next
    head_from.next = head_to

    return head_from, node


# alternating split
# for {a, b, a, b, a}, one sublist should be {a, a, a} and the other should be {b, b}
def alt_split(head: Node) -> (Node, Node):
    head_a = head
    head_b = head.next

    curr_a = head_a
    curr_b = head_b

    while curr_a and curr_b:
        curr_a.next = curr_b.next
        curr_a = curr_a.next

        curr_b.next = curr_a.next if curr_a else None
        curr_b = curr_b.next

    return head_a, head_b


# shuffle merge
# {1, 2, 3} and {7, 13, 17} should yield {1, 7, 2, 13, 3, 1}
def shuffle_merge(head_a: Node, head_b: Node) -> Node:
    head = head_a

    curr_a = head_a
    curr_b = head_b

    while curr_a and curr_b:
        a_next = curr_a.next
        curr_a.next = curr_b

        curr_a = curr_b
        curr_b = a_next

    return head


# sorted merge
# takes two lists, each of which is sorted in increasing and merges
# the two together into one list which is in increasing order.
def sorted_merge(head_a: Node, head_b: Node) -> Node:
    if head_a.val < head_b.val:
        head = head_a
        low = head_a
        high = head_b
    else:
        head = head_b
        low = head_b
        high = head_a

    while low and high:
        while low.next and low.next.val < high.val:
            low = low.next

        # swap low and high
        next = low.next
        low.next = high
        low = high
        high = next

    return head


# merge sort, using front-back split and sorted-merge
def merge_sort(head: Node) -> Node:
    if head.next is None:
        return head

    front, back = front_back_split(head)

    front = merge_sort(front)
    back = merge_sort(back)

    return sorted_merge(front, back)


# sorted intersect,
# Given two lists sorted, create and return a new list representing the intersection of the two lists.
def sorted_intersect(head_a: Node, head_b: Node) -> Node:
    curr_a = head_a
    curr_b = head_b

    # dummy_head = Node()
    head = None
    prev = Node()

    while curr_a and curr_b:
        if curr_a.val == curr_b.val:

            if not head:
                head = prev

            prev.next = curr_a
            curr_a = curr_a.next
            curr_b = curr_b.next

            prev.next.next = None
            prev = prev.next

        elif curr_a.val < curr_b.val:
            curr_a = curr_a.next
        else:
            curr_b = curr_b.next

    return head.next


# reverse - iterative
def reverse(head: Node) -> Node:
    prev = None
    curr = head
    next = head.next

    while curr:
        curr.next = prev
        prev = curr
        curr = next

        next = next.next if next else None

    return prev


# reverse - recursive
def reverse_recur(node: Node) -> Optional[Node]:
    if node.next is None:
        return node

    recur = reverse_recur(node.next)  # return 4

    node.next.next = node  # 3 -> 4 -> 3 (
    node.next = None  # 3 -> None

    return recur


def _create_list(arr: List[int]):
    head = Node(arr[0])
    prev = head
    for n in arr[1:]:
        curr = Node(n)
        prev.next = curr
        prev = curr

    return head


def _print_list(head: Node):
    arr = []
    curr = head
    while curr is not None:
        arr.append(curr.val)
        curr = curr.next
    print("->".join([str(x) for x in arr]))


if __name__ == "__main__":
    head = _create_list([1, 2, 3, 4, 5, 6])

    head = reverse_recur(head)

    _print_list(head)
