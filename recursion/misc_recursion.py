from typing import List
from util import is_char
from binary_tree import TreeNode


def all_subsets(input: str) -> List:
    def _all_subset(input, curr_idx, slate):
        if curr_idx >= len(input):
            result.append("".join(slate))
            return

        curr_char = input[curr_idx]
        for i in [curr_char, '']:
            slate.append(i)
            # for duplicate entries in input skip over the duplicates, just taking the current one
            # curr_idx + k, where k is the count of total occurrence of
            _all_subset(input, curr_idx + 1, slate)
            del slate[-1]

    result = []
    curr_idx = 0
    slate = []
    _all_subset(input, curr_idx, slate)
    return result


def all_permutations(nums: List[int]):
    def _perm(curr_idx, slate):
        if curr_idx == len(nums):
            result.append(slate.copy())
            return

        for idx in range(curr_idx, len(nums)):
            slate[idx], slate[curr_idx] = slate[curr_idx], slate[idx]
            _perm(curr_idx + 1, slate)
            slate[idx], slate[curr_idx] = slate[curr_idx], slate[idx]

    result = []
    slate = []
    _perm(0, slate)
    return result


def all_permutations_unique(nums: List[int]):
    def _perm(curr_idx):
        if curr_idx == len(nums):
            result.append(nums.copy())
            return

        lookup = set()
        for idx in range(curr_idx, len(nums)):
            if nums[idx] not in lookup:
                # swap idx and curr_idx
                nums[idx], nums[curr_idx] = nums[curr_idx], nums[idx]
                _perm(curr_idx + 1)
                nums[idx], nums[curr_idx] = nums[curr_idx], nums[idx]
                lookup.add(nums[idx])

    result = []
    _perm(0)
    return result


def remove_invalid_parentheses(expression: str) -> List[str]:

    def _bracket_violation(left, right):
        return left < 0 or right < 0 or left < right

    def _exp_valid(exp):
        stack = []
        for ch in exp:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if not stack:
                    return False
                stack.pop()

        return len(stack) == 0

    def _remove_invalid_parentheses(curr_idx, curr_expression):
        # base case, exhausted parsing all the characters
        if curr_idx >= len(expression):
            # verify if expression is valid
            exp_len = len(expression) - len(curr_expression)
            if _exp_valid(curr_expression) and exp_len <= min_exp_len[0]:
                if exp_len < min_exp_len[0]:
                    min_exp_len[0] = exp_len
                    result.clear()

                result.append(curr_expression)

            return

        curr_char = expression[curr_idx]
        if curr_char in ('(', ')'):
            _remove_invalid_parentheses(curr_idx + 1, curr_expression)
            _remove_invalid_parentheses(curr_idx + 1, curr_expression + curr_char)
        else:
            _remove_invalid_parentheses(curr_idx + 1, curr_expression + curr_char)

    result = []
    min_exp_len = [0]

    _remove_invalid_parentheses(0, '')

    return result


# a12b3 --> ["a12b3","a12B3","A12b3","A12B3"]
def letter_case_permutation(input: str) -> List:
    def _letter_case_perm(input, curr_idx, slate):
        if curr_idx >= len(input):
            result.append("".join([str(x) for x in slate]))
            return

        curr_char = input[curr_idx]
        if is_char(curr_char):
            for ch in [curr_char.lower(), curr_char.upper()]:
                slate.append(ch)
                _letter_case_perm(input, curr_idx + 1, slate)
                del slate[-1]
        else:
            slate.append(curr_char)
            _letter_case_perm(input, curr_idx + 1, slate)
            del slate[-1]

    result = []
    slate = []
    _letter_case_perm(input, 0, slate)
    return result


# 2 --> ['00', '01', '10', '11']
# 3 --> ['000', '001', '010', '011', '100', '101', '110', '111']
def binary_strings(digits: int) -> List:
    def _binary_strings(digits, curr_idx, slate):
        if curr_idx == digits:
            result.append("".join(slate))
            return

        for bit in ["0", "1"]:
            slate.append(bit)
            _binary_strings(digits, curr_idx + 1, slate)
            del slate[-1]

    result = []
    slate = []
    _binary_strings(digits, 0, slate)
    return result


def perform_op(expr_list, op):
    result = []
    idx = 0
    while idx < len(expr_list):

        elem = expr_list[idx]

        if elem == op:
            left_num = int(result[-1])
            right_num = int(expr_list[idx + 1])

            if op == '*':
                r = left_num * right_num
            elif op == '+':
                r = left_num + right_num
            else:
                raise Exception("invalid operation")

            del result[-1]

            result.append(r)

            idx += 2
        else:
            result.append(elem)
            idx += 1
    return result


def eval_expr(expr):
    expr_list = []
    buffer = []
    for ch in expr:
        if ch in ['*', '+']:
            expr_list.append("".join(buffer))
            expr_list.append(ch)
            buffer = []
        else:
            buffer.append(ch)
    if buffer:
        expr_list.append("".join(buffer))

    # pass 1 for calculating all *
    result = perform_op(expr_list, '*')
    # pass 2 for calculating all +
    result = perform_op(result, '+')

    return result[0]


def generate_all_expressions(s, target):
    def _generate_all_expressions(curr_idx, partial_exp):
        if curr_idx >= len(s):
            print(partial_exp)
            val = int(eval_expr(partial_exp))
            if val == target:
                result.append(partial_exp)
            return

        for op in ['', '*', '+']:
            if not op:
                _generate_all_expressions(curr_idx + 1, partial_exp + s[curr_idx])
            else:
                _generate_all_expressions(curr_idx + 1, partial_exp + op + s[curr_idx])

    result = []
    partial_exp = s[0]
    _generate_all_expressions(1, partial_exp)
    return result


def check_if_sum_possible(arr, k):
    def _check_sum_possible(arr, slate, curr_idx):

        if curr_idx >= len(arr):
            s = 0
            sum_seq = [x for x in slate if x != float('inf')]
            for e in sum_seq:
                s += e
            if sum_seq and s == k:
                result.append(True)
            return

        curr_num = arr[curr_idx]
        for i in [curr_num, float('inf')]:
            slate.append(i)
            _check_sum_possible(arr, slate, curr_idx + 1)
            del slate[-1]

    result = []
    slate = []
    _check_sum_possible(arr, slate, 0)
    if result:
        return True
    else:
        return False


def count_binary_trees(node_count):
    if node_count <= 1:
        return 1
    sum = 0
    for left_node_count in range(0, node_count):
        right_node_count = node_count - left_node_count - 1

        left = count_binary_trees(left_node_count)
        right = count_binary_trees(right_node_count)

        sum = sum + left * right

    return sum


if __name__ == "__main__":
    print(generate_all_expressions("123", 6))
    # generate_all_expressions("12", 12)
    # eval_expr('012+2*3*45+90')
    # print(count_binary_trees(3))
