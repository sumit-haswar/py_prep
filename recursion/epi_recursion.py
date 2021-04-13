from typing import List
from arrays.epi_arrays import get_next_permutation
from binary_tree import TreeNode

PHONE_MAP = [
    '0',
    '1',
    'ABC',
    'DEF',
    'GHI',
    'JKL',
    'MNO',
    'PQRS',
    'TUV',
    'WXYZ',
]

#   15.1 the towers of hanoi problem
def compute_tower_hanoi(num_rings):
    def _compute_tower_hanoi(curr_num_rings, from_peg, to_peg, using_peg):
        if curr_num_rings > 0:
            _compute_tower_hanoi(curr_num_rings - 1, from_peg, using_peg, to_peg)
            # since all n-1 rings have been moved, move bottommost ring from --> to
            ring = pegs[from_peg].pop()
            pegs[to_peg].append(ring)
            # write the movement step to result
            result.append((from_peg, to_peg))

            _compute_tower_hanoi(curr_num_rings - 1, using_peg, to_peg, from_peg)

    result = []
    # create first peg as [num_rings..3,2,1]
    first_peg = [x for x in reversed(range(1, num_rings + 1))]
    # create all peg as [[3,2,1], [], []]
    pegs = [first_peg, [], []]
    _compute_tower_hanoi(num_rings, 0, 1, 2)
    return result


#   15.2 compute all mnemonics for a phone number
def get_phone_mnemonic(phone_number: str):
    def _get_phone_mnemonic(curr_idx, mnemonic_list, result):

        # base-case we have reached the end of current "slate"
        if curr_idx == len(phone_number):
            number = ''.join(mnemonic_list)
            result.append(number)
            return

        curr_digit = int(phone_number[curr_idx])
        for char in list(PHONE_MAP[curr_digit]):
            # A, B, C
            mnemonic_list[curr_idx] = char
            _get_phone_mnemonic(curr_idx + 1, mnemonic_list, result)

    result = []
    mnemonic_list = [0] * len(phone_number)
    _get_phone_mnemonic(0, mnemonic_list, result)
    return result


#   15.3 generate all non-attacking placements of n-queens
def _placement_violated(place_col, row, col_placements):
    # check violation from row 0 to row-1
    for idx, col in enumerate(col_placements[:row]):
        # get diff between curr-col and place-col
        diff = abs(col - place_col)
        # if diff == 0, then there's column violation
        # if diff == row - idx, then there's diagonal violation
        if diff in (0, row - idx):
            return True

    return False


def find_all_queen_arrangements(n):
    def _find_all_arrangements(column_placement, curr_row):
        if curr_row >= n:
            print(column_placement)
            return
        for col in range(n):
            # recur only if placing a queen at [curr_row][col] does not violate condition
            if not _placement_violated(col, curr_row, column_placement):
                # place queen at curr_idx and current_col
                column_placement[curr_row] = col
                _find_all_arrangements(column_placement, curr_row + 1)

    result = []
    column_placement = [0] * n
    _find_all_arrangements(column_placement, 0)
    return result


def find_all_queen_arrangements_brute_force(n):
    def _find_all_arrangements(column_placement, curr_row):
        if curr_row >= n:
            print(column_placement)
            return
        for col in range(n):
            # recur only if placing a queen at [curr_row][col] does not violate condition
            if not _placement_violated(col, curr_row, column_placement):
                # place queen at curr_idx and current_col
                column_placement[curr_row] = col
                _find_all_arrangements(column_placement, curr_row + 1)

    result = []

    placement = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        placement.append(row)

    _find_all_arrangements(placement, 0)
    return result


#   15.4 generate permutations
def generate_permutation(A: List[int]) -> List[List[int]]:
    def _generate_permutation(curr_idx, result):
        if curr_idx >= len(A):
            result.append(A.copy())
            return

        for idx in range(curr_idx, len(A)):
            # swap
            A[curr_idx], A[idx] = A[idx], A[curr_idx]
            _generate_permutation(curr_idx + 1, result)
            # swap back
            A[idx], A[curr_idx] = A[curr_idx], A[idx]

    result = []
    _generate_permutation(0, result)

    return result


def generate_permutation_iter(A: List[int]) -> List[List[int]]:
    result = []
    A.sort()
    while True:
        result.append(A.copy())
        A = get_next_permutation(A)
        if not A:
            break

    return result


#   15.5 generate the power set
def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def _gen_power_set(partial_result, curr_idx):
        if curr_idx >= len(input_set):
            result.append(partial_result.copy())
            return

        curr_elem = input_set[curr_idx]
        for elem in [curr_elem, None]:
            if elem:
                partial_result.append(elem)
                _gen_power_set(partial_result, curr_idx + 1)
                del partial_result[-1]
            else:
                _gen_power_set(partial_result, curr_idx + 1)

    result = []
    _gen_power_set([], 0)
    return result


#   15.6 generate all subsets of size k
def combinations(n: int, k: int):
    def _combinations(partial_exp, curr_idx):
        if len(partial_exp) == k:
            result.append(partial_exp.copy())
            print(partial_exp)
            return

        if curr_idx > n:
            return

        curr_elem = curr_idx
        for i in [curr_elem, None]:
            if i:
                partial_exp.append(i)
                _combinations(partial_exp, curr_idx + 1)
                del partial_exp[-1]
            else:
                _combinations(partial_exp, curr_idx + 1)

    result = []
    _combinations([], 1)
    return result


#   15.7 generate strings of matched parens
def _bracket_violation(left, right):
    return left > right or left < 0 or right < 0


def well_formed_brackets(bracket_count):
    def _well_formed_brackets(slate, left, right):
        # short-circuit on bracket violation
        #   left OR right becomes negative
        #   result has more right[we start by decrementing left] than left brackets
        #   (basically you closed a bracket before opening it)
        if _bracket_violation(left, right):
            return
        if left == 0 and right == 0:
            result.append(slate)
            return

        # add open bracket to partial-exp and recur by dec left count
        _well_formed_brackets(slate + "(", left - 1, right)

        # add closing bracket to partial-exp and recur by dec right count
        _well_formed_brackets(slate + ")", left, right - 1)

    result = []
    # initially left and right counts are both n
    _well_formed_brackets("", bracket_count, bracket_count)
    return result


#   15.8 generate palindromic decompositions
def palindrome_decompositions(input: str):
    def _palindrome_decompositions(offset, partial_list):
        if offset == len(input):
            result.append("|".join(partial_list))
            return

        for i in range(offset + 1, len(input) + 1):
            # at each node, fan out into multiple prefix in steps of 1
            # for example "sumit" --> s, su, sum, sumi, sumit
            prefix = input[offset:i]
            if prefix == prefix[::-1]:  # recur only if prefix is a palindrome
                _palindrome_decompositions(i, partial_list + [prefix])

    result = []
    _palindrome_decompositions(0, [])
    return result


def all_decompositions(word: str):
    def _all_decompositions(partial_res, offset):
        if offset >= len(word):
            print(partial_res)
            return
        for idx in range(offset + 1, len(word) + 1):
            # at each node, fan out into multiple prefix in steps of 1
            # for example "sumit" --> s, su, sum, sumi, sumit
            prefix = word[offset:idx]
            _all_decompositions(partial_res + [prefix], idx)

    result = []
    _all_decompositions([], 0)
    return result


#   15.9 generate binary trees (todo)
def generate_all_binary_trees(node_count: int):
    # base case: node_count is 0
    if node_count == 0:
        return [None]

    result = []
    # iter from left of root being size 0 to left of root being (node_count - 1)
    for left_node_count in range(0, node_count):
        right_node_count = node_count - left_node_count - 1

        left_subtrees = generate_all_binary_trees(left_node_count)
        right_subtrees = generate_all_binary_trees(right_node_count)

        # add this root to the result and return
        curr_result = []
        for left in left_subtrees:
            for right in right_subtrees:
                curr_result.append(TreeNode(data=None, left=left, right=right))

        result = result + curr_result
    return result


# todo   15.10 implement a sudoku solver
# todo   15.11 compute a gray code

if __name__ == "__main__":
    # _placement_violated(col, row, col_placements):
    # find_all_queen_arrangements(4)
    print(well_formed_brackets(4))
    # prefix = [1,3,0,0]
    # for i in range(4):
    #     prefix[3] = i
    #     res = _placement_violated(i, 3, [1,3,0,0])
    #     print( "{}: {}".format(prefix, res))
    #     # print(_placement_violated(i, 3, [0, 3, 2, 0]))
