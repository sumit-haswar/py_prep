import typing


# -- stacks --
#   8.1 stack with max api
class MaxStack():

    def __init__(self):
        self._stack = []

    def push(self, val):
        if self._stack:
            top = self._stack[-1]
            self._stack.append((val, max(val, top[1])))
        else:
            self._stack.append((val, val))

    def pop(self):
        return self._stack.pop()[0]

    def get_max(self):
        return self._stack[-1][1]


#   8.2 evaluate RPN (reverse polish notation)
def evaluate_rpn_expression(exp: str) -> int:
    calc = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: (int)(x / y)
    }
    stack = []
    for curr in exp.split(' '):
        if curr not in calc:
            stack.append(int(curr))
        else:
            y = stack.pop()
            x = stack.pop()
            result = calc[curr](x, y)
            stack.append(result)

    return stack.pop()


#   8.3 is a string well-formed
def is_string_well_formed(s: str):
    pass


#   8.4 normalize path-names

#   (8.5) compute buildings with sunset-view

# -- -- -- -- queues -- -- -- --

#   8.6 compute binary tree nodes in order of inc. depth

#   8.7 implement a circular queue

#   8.8 implement a queue using stack

#   (8.9) implement a queue with max api
class MaxQueue():

    def __init__(self):
        pass

    def enqueue(self, val: int) -> None:
        pass

    def dequeue(self, val: int) -> int:
        pass

    def get_max(self) -> int:
        pass
