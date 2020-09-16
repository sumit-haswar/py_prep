import string
from typing import List
from functools import reduce
from arrays import my_reverse


def is_palindromic(s: str) -> bool:
    """"""
    return all(s[i] == s[~i] for i in range(len(s) // 2))


#   6.1 interconvert strings and integers
def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        is_negative = True
        x = x * -1
    result = []
    while x:
        result.append(string.digits[x % 10])
        x //= 10

    if is_negative:
        result.append('-')

    return ''.join(c for c in reversed(result))


def string_to_int(s: str) -> int:
    is_negative = True if s[0] == '-' else False

    result = 0
    for curr in s[is_negative:]:
        result = result * 10 + string.digits.index(curr)

    return result * (-1 if is_negative else 1)


#   6.2 base conversion
def convert_base(n_string: str, b1: int, b2: int) -> str:
    is_negative = n_string[0] == '-'
    num_int = _convert_to_int(n_string[is_negative:], b1)
    return _convert_to_base(num_int, b2, is_negative)


def _convert_to_base(num: int, base: int, is_negative: bool) -> str:
    if not num:
        return ""
    result = []
    while num:
        mod = num % base
        result.append(string.hexdigits[mod].upper())
        num //= base

    if is_negative:
        result.append('-')

    return ''.join(x for x in reversed(result))


def _convert_to_int(num_list, base: int) -> int:
    result = 0
    for digit in num_list:
        result = result * base + string.digits.index(digit)
    return result


#   6.4 replace and remove
def replace_and_remove(s: List[str], size: int) -> int:
    # first iter the list to get count a's (a_count) and delete b's
    write_idx = 0
    a_count = 0
    for idx in range(size):
        if s[idx] != 'b':
            s[write_idx] = s[idx]
            write_idx += 1
        if s[idx] == 'a':
            a_count += 1

    curr_idx = write_idx - 1
    write_idx = write_idx + a_count - 1
    final_size = write_idx + 1

    while curr_idx >= 0:
        if s[curr_idx] == 'a':
            # write 2 dd's
            s[write_idx] = 'd'
            write_idx -= 1
            s[write_idx] = 'd'
            write_idx -= 1
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1

        curr_idx -= 1

    return final_size


#   6.5 test palindromacity
def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < len(s):
            left += 1

        while not s[right].isalnum() and right >= 0:
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


#   6.6 reverse all the words in a sentence
def reverse_words(s: List[str]):
    my_reverse(s)

    left = 0
    right = 0
    while right < len(s):
        if s[right] == ' ':
            my_reverse(s, left, right - 1)
            right += 1
            left = right
        right += 1

    # right == 1 + last idx of the sentence
    my_reverse(s, left, right - 1)

    return "".join(s)


#   6.8 convert from roman to decimal
def roman_to_int(s: str) -> int:
    pass


#   6.11 implement run length encoding
def rle_decode(input: str) -> str:
    curr_count = 0
    result = []
    curr_idx = 0
    # while curr_idx < len(input):
    #     if not input[curr_idx]
    #     curr_idx +=1

    return ''.join(result)


def rle_encode(input: str) -> str:
    count = 1
    result = []
    curr_idx = 1
    while curr_idx <= len(input):
        if curr_idx == len(input) or (input[curr_idx] != input[curr_idx - 1]):
            result.append(str(count) + input[curr_idx - 1])
            count = 1
        else:
            count += 1

        curr_idx += 1

    return ''.join(result)


#   6.12 find first occurrence of a substring
def rabin_karp(s: str, t: str) -> int:
    pass

#   6.7 look and say problem
#   6.10 write a string sinusoidally
