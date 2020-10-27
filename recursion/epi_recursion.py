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


#   todo 15.1 the tower of hanoi problem

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


#   todo 15.3 generate all non-attacking placements of n-queens

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

#   15.10 implement a sudoku solver

#   15.11 compute a gray code


# todo

#   15.6 generate all subsets of size k
#   15.8 generate palindromic decompositions
#   15.9 generate binary trees
