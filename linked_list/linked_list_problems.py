"""
this module contains solutions to problems listed in
http://cslibrary.stanford.edu/105/
Most of the solutions are inspired from the pdf document on this page.
For details regarding problem and solutions pls refer the original document:
    http://cslibrary.stanford.edu/105/LinkedListProblems.pdf
"""


from .node import Node
from .util import print_list, \
    get_random_list, \
    push, \
    length, \
    create_list


# Solutions to linked-list problems defined in: http://cslibrary.stanford.edu/105/

# 3. build at head with push()
def build_at_head():
    head = None

    for e in [5, 4, 3, 2, 1]:
        head = push(head, e)

    return head


# 4. build with tail pointer
def build_at_tail():
    head = Node(1)
    curr = head

    for e in [2, 3, 4, 5, 6]:
        this = Node(e)
        curr.next = this
        curr = this

    return head


# questions
# 1. count
# Write a Count() function that counts the number of times a given int occurs in a list. The
# code for this has the classic list traversal structure as demonstrated in Length().
def count_occurrence(head, elem):
    if not head:
        return 0

    curr = head
    count = 0
    while curr:
        if (curr.data == elem):
            count = count + 1
        curr = curr.next

    return count


# 2. get Nth
# // Given a list and an index, return the data
# // in the nth node of the list. The nodes are numbered from 0.
# // Assert fails if the index is invalid (outside 0..length-1).
def get_nth(head, idx):
    assert head
    curr_idx = 0
    curr = head
    while curr:
        if curr_idx == idx:
            return curr.data
        curr = curr.next
        curr_idx = curr_idx + 1

    raise Exception('invalid idx')


# 3. delete list


# 4. pop
# The opposite of Push(). Takes a non-empty list
# and removes the front node, and returns the data
# which was in that node.
def pop(head):
    assert head
    new_head = head.next
    return new_head


# 5. insert Nth
# A more general version of Push().
# Given a list, an index 'n' in the range 0..length,
# and a data element, add a new node to the list so
# that it has the given index.
def insert_nth(head, idx, data):
    # insert at head case
    if idx == 0:
        new_node = Node(data, head)
        return new_node

    curr_idx = 0
    curr = head
    while curr:
        if curr_idx == idx - 1:
            # insert after curr
            new_node = Node(data, curr.next)
            curr.next = new_node
            return head

        curr = curr.next
        curr_idx = curr_idx + 1

    return head


# 6. sorted insert
def sorted_insert(head, new_node):
    """
    Write a SortedInsert() function which given a list that is sorted in increasing order, and a
    single node, inserts the node into the correct sorted position in the list. While Push()
    allocates a new node to add to the list, SortedInsert() takes an existing node, and just
    rearranges pointers to insert it into the list. There are many possible solutions to this
    problem.
    """
    # add at head
    if not head or head.data > new_node.data:
        new_node.next = head
        return new_node

    curr = head
    while curr.next:
        if curr.next.data > new_node.data:
            # add after curr
            new_node.next = curr.next
            curr.next = new_node
            return head
        curr = curr.next

    # add at tail
    curr.next = new_node
    return head


# 7. insert sort
def insert_sort(head):
    """
    Write an InsertSort() function which given a list, rearranges its nodes so they are sorted in
    increasing order. It should use SortedInsert().
    :param head:
    :return:
    """
    pass


# 8. append
# Append 'b' onto the end of 'a', and then set 'b' to NULL.
def append(a_head, b_head):
    if not b_head:
        return a_head
    elif not a_head:
        return b_head

    curr_a = a_head
    while curr_a.next:
        curr_a = curr_a.next

    curr_a.next = b_head
    return a_head


# 9. front back split
# Split the nodes of the given list into front and back halves,
# and return the two lists using the reference parameters.
# If the length is odd, the extra node should go in the front list.
def front_back_split(head):
    slow = head
    fast = head.next

    if (fast is None):
        return (slow, None)

    if (fast.next is None):
        slow.next = None
        return (slow, fast)

    while True:
        temp = fast.next
        # end found
        if temp is None:
            # slow.next is head of back
            fast = slow.next
            slow.next = None
            return (head, fast)

        # end found
        if temp.next is None:
            # slow.next.next, is head of back
            fast = slow.next.next
            slow.next.next = None
            return (head, fast)

        # keep traversing
        slow = slow.next
        fast = temp.next


# 10. remove duplicates
# Remove duplicates from a sorted list.
def remove_duplicates(head):
    curr = head

    if curr is None or curr.next is None:
        return curr

    next = curr.next

    while next is not None:
        if curr.val == next.val:
            # keep traversing next till non-equal found
            while next is not None and next.val == curr.val:
                next = next.next
            curr.next = next
        curr = next
        next = next.next if next else None

    return head


# 11. move node
# Take the node from the front of the source, and move it to
# the front of the dest.
# It is an error to call this with the source list empty.
def move_node(source_head, dest_head):
    new_source_head = source_head.next
    source_head.next = dest_head
    return new_source_head, source_head


# 12. alternating split
# Given the source list, split its nodes into two shorter lists.
# If we number the elements 0, 1, 2, ... then all the even elements
# should go in the first list, and all the odd elements in the second.
# The elements in the new lists may be in any order.
def alternating_split(source_head):
    even_head = source_head
    odd_head = source_head.next

    curr_is_even = True
    curr_even = even_head
    curr_odd = odd_head

    while curr_even is not None and curr_odd is not None:
        if curr_is_even:
            curr_even.next = curr_odd.next
            curr_even = curr_odd.next
        else:
            curr_odd.next = curr_even.next
            curr_odd = curr_even.next

        curr_is_even = not curr_is_even

    return even_head, odd_head

# 13. shuffle merge
# Merge the nodes of the two lists into a single list taking a node
# alternately from each list, and return the new list.
# shuffle_merge() with {1, 2, 3} and {7, 13, 1} should yield {1, 7, 2, 13, 3, 1}.
def shuffle_merge(a_head, b_head):
    if a_head is None or b_head is None:
        return a_head if a_head is None else b_head

    head = a_head
    curr = a_head
    next = b_head

    while next is not None:
        temp = curr.next
        curr.next = next

        curr = next
        next = temp

    return head


# 14. sorted merge
# Takes two lists sorted in increasing order, and
# splices their nodes together to make one big
# sorted list which is returned.
def sorted_merge(a_head, b_head):
    if a_head is None or b_head is None:
        return a_head if a_head is None else b_head

    if a_head.val < b_head.val:
        head = a_head
        curr = a_head
        candidate = b_head
    else:
        head = b_head
        curr = b_head
        candidate = a_head

    # compare curr.next, curr and candidate
    while curr is not None and candidate is not None:
        if curr.next is None:
            curr.next = candidate
            break

        if candidate.val < curr.next.val:
            temp = curr.next
            curr.next = candidate
            curr = candidate
            candidate = temp
        else:
            curr = curr.next

    return head


# 15. merge sort
# (This problem requires recursion) Given FrontBackSplit() and SortedMerge(), it's pretty
# easy to write a classic recursive MergeSort(): split the list into two smaller lists,
# recursively sort those lists, and finally merge the two sorted lists together into a single
# sorted list. Ironically, this problem is easier than either FrontBackSplit() or
# SortedMerge().
def merge_sort_util(head):
    pass


def merge_sort(head):
    # base-case:
    if head is None or head.next is None:
        return head

    # split list into two-halves
    front, back = front_back_split(head)

    # merge front and back recursively
    front = merge_sort(front)
    back = merge_sort(back)

    # merge the sorted result
    return sorted_merge(front, back)


def get_first_diff(node):
    while node.next is not None and node.val == node.next.val:
        node = node.next
    return node

# 16. sorted intersect
# Given two lists sorted in increasing order, create and return a new list representing the
# intersection of the two lists. The new list should be made with its own memory — the
# original lists should not be changed. Ideally, each list should only be traversed once.
def sorted_intersect(list_a, list_b):

    # assume both list_a and list_b are not null
    curr_a = list_a
    curr_b = list_b

    # use head as dummy (empty) node
    head = Node()
    curr = head

    while curr_a is not None and curr_b is not None:
        # every time exhaust both lists till consecutive non-equal element
        curr_a = get_first_diff(curr_a)
        curr_b = get_first_diff(curr_b)

        if curr_a.val < curr_b.val:
            temp = Node(curr_a.val)
            curr.next = temp
            curr = temp
            curr_a = curr_a.next
        elif curr_a.val > curr_b.val:
            temp = Node(curr_b.val)
            curr.next = temp
            curr = temp
            curr_b = curr_b.next
        else:
            temp = Node(curr_b.val)
            curr.next = temp
            curr = temp

            curr_a = curr_a.next
            curr_b = curr_b.next

    while curr_a is not None:
        curr_a = get_first_diff(curr_a)
        if curr_a is None:
            break
        temp = Node(curr_a.val)
        curr.next = temp
        curr = temp
        curr_a = curr_a.next

    while curr_b is not None:
        curr_b = get_first_diff(curr_b)
        if curr_b is None:
            break
        temp = Node(curr_b.val)
        curr.next = temp
        curr = temp
        curr_b = curr_b.next

    return head.next


# 17. reverse
# back-middle-front strategy
# start with three pointers: back, middle and front
# do:
#   middle.next --> back
#   assign back to middle
#   assign middle to front
#   assign front to front.next
#   continue till front reaches end of list
# do one last middle.next --> back assignment
def reverse(list):
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

# 18. recursive reverse !
# Recursively reverses the given linked list by changing its .next
# pointers and its head pointer in one pass of the list.
def recursive_reverse(head):
    # base-case
    if head is None or head.next is None:
        return head

    recur = recursive_reverse(head.next)

    head.next.next = head
    head.next = None

    return recur

def main():
    #todo create test lists using create_list
    #   for example: source = create_list([0,1,2,3,4,5,6,7,8,9,10,11,12])
    #   invoke required methods to be tested
    #   print result using print_list

    list = create_list([2,3,4,5,8,9,11,33])
    print_list(recursive_reverse(list))