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
    look_up = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    sum = look_up[s[-1]]
    for curr_idx in reversed(range(len(s) - 1)):

        # if curr >= elem to the right, if not then subtract current
        if look_up[s[curr_idx]] >= look_up[s[curr_idx + 1]]:
            val = look_up[s[curr_idx]]
        else:
            val = -look_up[s[curr_idx]]

        sum += val

    return sum


#   6.9 compute all valid IP addresses
def get_valid_ip_address(ip: str):
    pass


#   6.11 implement run length encoding
def rle_decode(input: str) -> str:
    curr_count = 0
    result = []
    curr_idx = 0
    while curr_idx < len(input):
        if input[curr_idx].isnumeric():
            curr_count = curr_count * 10 + string.digits.index(input[curr_idx])
        else:
            result.append(input[curr_idx] * curr_count)
            curr_count = 0

        curr_idx += 1

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
def rabin_karp(pattern: str, text: str) -> int:
    if len(pattern) > len(text):
        return -1

    base = 26
    pattern_hash = reduce(lambda val, char: val * base + ord(char), pattern, 0)

    # create hash of the first len(pattern) characters of the text
    text_hash = reduce(lambda val, char: val * base + ord(char),
                       text[:len(pattern)],
                       0)

    # power is used to REMOVE the leftmost char hash when rolling
    power_s = pow(base, len(pattern) - 1)

    for pivot in range(len(pattern), len(text)):
        if pattern_hash == text_hash \
                and pattern == text[pivot - len(pattern): pivot]:
            return pivot - len(pattern)

        # remove the left char
        text_hash = text_hash - (ord(text[pivot - len(pattern)]) * power_s)
        # add a curr char to text_hash
        text_hash = text_hash * base + ord(text[pivot])

    # check the last len(pattern) chars from the text
    if pattern_hash == text_hash and pattern == text[-len(pattern):]:
        return len(text) - len(pattern)

    return -1

# Former Coding Interview Question: Compression and Decompression
# 3[abc]4[ab]c  --> abcabcabcababababc
# 2[3[a]b]      --> aaabaaab
# 2[a3[b]c]      --> abbbcabbbc
def decompress(text: str) -> str:
    num_stack = []
    str_stack = []
    idx = 1
    curr_seq = [text[0]]
    while idx < len(text):
        curr = text[idx]

        if curr == '[':
            # curr_seq must be a number push to stack and clear
            count = int(''.join(curr_seq))
            num_stack.append(count)
        elif curr == ']':
            # termination of bracket, so process
            pass
        else:
            curr_seq.append(curr)

        idx += 1

#   6.7 look and say problem
#   6.10 write a string sinusoidally
