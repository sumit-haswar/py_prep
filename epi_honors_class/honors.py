from typing import List
from linked_list import Node


#   24.01 gcd
def gcd_mod(x: int, y: int) -> int:
    if x > y:
        x, y = y, x

    if x == y:
        return x
    if x == 0 or y == 0:
        return x if y == 0 else y
    return gcd_mod(x, y % x)


#   24.01 gcd
def gcd(x: int, y: int) -> int:
    pass


#   24.06 rotate an array
def rotate_array():
    pass


#   24.08 justify text
def justify_text(text: str) -> List[str]:
    pass


#   24.09 implement list zipping
def zipping_linked_list(head: Node):
    pass

#   24.12 compute max of a sliding window

#   24.18 find line through most points

#   24.19 convert a sorted doubly linked list to a bst

#   24.22 implement regular expression matching

#   24.29 find the maximum 2D subarray

# --------------------------------------------------------------------------------------------------------------------

#   24.05 longest contiguous increasing subarray

#   24.25 draw the skyline

#   24.31 trapping water

#   24.34 road network
