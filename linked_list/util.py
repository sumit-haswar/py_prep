from .node import Node
import random


def get_ordered_linked_list():
    num_list = [2, 34, 55, 89, 90, 120, 240]
    head = Node(0)
    prev = head
    for e in num_list:
        curr = Node(e)
        prev.next = curr
        prev = curr

    return head


def create_list(arr):
    head = Node(arr[0])
    prev = head
    for elem in arr[1:]:
        curr = Node(elem)
        prev.next = curr
        prev = curr
    return head

def get_123_list():
    three = Node(3, None)
    two = Node(2,three)
    one = Node(1, two)

    return one


def get_random_list(count):
    head = Node(random.randrange(1, 150))
    prev = head
    for i in range(0,count-1):
        curr = Node(random.randrange(1, 150))
        prev.next = curr
        prev = curr

    return head


def print_list(head):
    if not head:
        print("-- empty list --")
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
