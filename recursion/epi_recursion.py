from typing import List
from arrays.epi_arrays import get_next_permutation

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


#   15.2 compute all mnemonics for a phone number
def get_phone_mnemonic(phone_number: str):
    def _get_phone_mnemonic(curr_idx, mnemonic_list, result):
        if curr_idx == len(phone_number):
            # base-case
            number = ''.join(mnemonic_list)
            result.append(number)
            return

        for char in list(PHONE_MAP[int(phone_number[curr_idx])]):
            # A, B, C
            mnemonic_list[curr_idx] = char
            _get_phone_mnemonic(curr_idx + 1, mnemonic_list, result)

    result = []
    mnemonic_list = [0] * len(phone_number)
    _get_phone_mnemonic(0, mnemonic_list, result)
    return result


#   15.4 generate permutations
def generate_permutation(A: List[int]) -> List[List[int]]:
    def _generate_permutation(curr, result):
        if curr == len(A) - 1:
            result.append(A.copy())
            return

        for idx in range(curr, len(A)):
            A[curr], A[idx] = A[idx], A[curr]
            _generate_permutation(curr + 1, result)
            # swap back
            A[idx], A[curr] = A[curr], A[idx]

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
    pass


#   15.7 generate strings of matched parens
def _bracket_violation(left, right):
    return left > right or left < 0 or right < 0


def well_formed_brackets(bracket_count):
    def _well_formed_brackets(slate, left, right):
        if _bracket_violation(left, right):
            return
        if left == 0 and right == 0:
            result.append(slate)
            return

        _well_formed_brackets(slate + "(", left - 1, right)
        _well_formed_brackets(slate + ")", left, right - 1)

    result = []
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
    offset = 0
    partial_list = []
    _palindrome_decompositions(offset, partial_list)
    return result


#   15.10 implement a sudoku solver

#   15.11 compute a gray code

#   15.3 generate all non-attacking placements of n-queens
def _placement_violated(col, row, col_placements):
    for idx, val in enumerate(col_placements[:row]):
        # todo
        pass

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


if __name__ == "__main__":
    # print(palindrome_decompositions('adabrar'))
    s = "sumit"
    offset = 0
    for i in range(offset + 1, len(s) + 1):
        prefix = s[offset:i]
        print(prefix)

# todo
#   15.1 the tower of hanoi problem
#   15.6 generate all subsets of size k
#   15.9 generate binary trees
