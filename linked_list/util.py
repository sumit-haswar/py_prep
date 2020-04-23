from .node import Node


def get_ordered_linked_list():

    num_list = [2, 34, 55, 89, 90, 120, 240]
    head = Node(0)
    prev = head
    for e in num_list:
        curr = Node(e)
        prev.next = curr
        prev = curr

    return head


def get_123_list():
    three = Node(3, None)
    two = Node(2,three)
    one = Node(1, two)

    return one


def print_list(head):
    if not head:
        print("empty list")
    curr = head
    list = []
    while curr:
        list.append(str(curr.data))
        curr = curr.next

    print("->".join(list))


def length(head):

    count = 0
    if not head:
        return count

    curr = head
    while curr:
        count = count + 1
        curr = curr.next

    return count


def push(head_ref, new_data):
    new_head = Node(new_data)
    new_head.next = head_ref

    return new_head
