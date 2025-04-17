from _3.trees.tree_node import TreeNode
from typing import List, Optional


class StackEntry:
    def __init__(self, elem, max):
        self.elem = elem
        self.max = max

# 8.1 implement a stack with max api
class MaxStack:

    def __init__(self):
        self._stack : List = []

    def get_max(self):
        return self._stack[-1].max

    def push(self, elem):
        if not self._stack:
            self._stack.append(StackEntry(elem, elem))
        else:
            top = self._stack[-1]
            self._stack.append(StackEntry(elem, max(elem, top.max)))

    def pop(self):
        return self._stack.pop().elem


# 8.6 compute binary tree nodes in order of increasing depth


# 8.2 evaluate RPN expressions
def eval_rpn_expression(exp: str):
    stack = []
    tokens = exp.split(",")
    operators = {"*", "+", "/", "-"}
    for token in tokens:
        if token in operators:
            match token:
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    stack.append(stack.pop() - stack.pop())
                case "/":
                    stack.append(stack.pop() // stack.pop())
        else:
            stack.append(_parse_int(token))

    return stack[0] if stack else None


# 8.7 implement a circular queue


# 8.3 is a string well-formed
def is_string_well_formed(expr: str) -> bool:
    pass

# 8.8 implement a queue using stacks

# 8.4 normalize path-names

# 8.5 compute buildings with a sunset view
def compute_sunset_view_buildings(buildings: List[int]) -> List[int]:
    stack : List = []
    for idx, building_height in enumerate(buildings):
        if not stack:
            stack.append((idx, building_height))
        else:
            while stack and stack[-1][1] <= building_height:
                stack.pop()
            stack.append((idx, building_height))

    return [x[0] for x in stack]


# 8.9 implement a queue with max api


def _parse_int(s : str) -> Optional[int]:
    try:
        return int(s)
    except:
        return None

if __name__ == "__main__":
    # max_stack = MaxStack()
    #
    # for n in [8,5,7,12,4,13]:
    #     max_stack.push(n)
    #     print(max_stack.get_max())
    #
    # max_stack.pop()
    print(compute_sunset_view_buildings([2,4,2,5,3,1,12]))