from typing import List
import string
import functools


#   1.1 is unique
def is_unique(input: str) -> bool:
    lookup = set()
    for c in input:
        if c in lookup:
            return False
        lookup.add(c)
    return True


def is_unique_bit_map(input: str) -> bool:
    bitmap = 0
    for c in input:
        code = ord(c) - ord('a')
        if bitmap & (1 << code):
            return False
        bitmap = bitmap | (1 << code)
    return True


def is_unique_sort(input: str) -> bool:
    sorted_input = ''.join(sorted(input))
    idx = 1
    while idx < len(sorted_input):
        if sorted_input[idx - 1] == sorted_input[idx]:
            return False
        idx += 1
    return True


#   1.2 check permutation
def is_permutation(a: str, b: str) -> bool:
    lookup = [0] * 256
    for c in a:
        code = ord(c) - ord('a')
        lookup[code] += 1

    for c in b:
        code = ord(c) - ord('a')
        lookup[code] -= 1
        if lookup[code] < 0:
            return False

    return True


def is_permutation_sort(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    return sorted_a == sorted_b


#   1.3 URLify
def get_url(input: str) -> str:
    # count number of spaces
    count = functools.reduce(lambda cnt, ch: cnt + (1 if ch == ' ' else 0), input, 0)
    write_stream = [' '] * (len(input) + count * 2)
    write_idx = 0
    for ch in input:
        if ch == ' ':
            write_stream[write_idx] = '%'
            write_stream[write_idx + 1] = '2'
            write_stream[write_idx + 2] = '0'
            write_idx += 3
        else:
            write_stream[write_idx] = ch
            write_idx += 1

    # arr = list(input)
    return ''.join(write_stream)


#   1.4 Palindrome permutation
def is_palindromic(input: str) -> bool:
    lookup = 0
    for ch in input:
        code = ord(ch) - ord('a')
        # flip code bit
        lookup = lookup ^ (1 << code)

    # check if lookup has all zeros OR just one 1
    diff = lookup - 1

    return lookup == 0 or (diff & lookup) == 0


#   1.5 one away
def is_one_edit_away(a: str, b: str) -> bool:
    def _one_mutation_away(x: str, y: str) -> bool:
        pass

    def _one_edit_away() -> bool:
        pass

    if len(a) == len(b):
        return _one_mutation_away(a, b)
    elif len(a) + 1 == len(b):  # a is shorter
        return _one_edit_away()
    elif len(a) - 1 == len(b):  # b is shorter
        return _one_edit_away()

    return False


#   1.6 string compression
def compress_string(text: str) -> bool:
    pass


#   1.7 rotate matrix
def rotate_matrix(matrix: List[List[int]]):
    pass

#   1.8 zero matrix
#   1.9 string rotation
