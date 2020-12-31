import random
from math import sqrt, floor

from typing import List


# reverse a list in-place
def my_reverse(list, left=0, right=None):
    if not right:
        right = len(list) - 1
    while left < right:
        _swap(list, left, right)
        left += 1
        right -= 1


# even-odd partitioning
def even_odd_partition(list):
    even, odd = 0, len(list) - 1

    while even < odd:
        # even idx is even
        if list[even] % 2 == 0:
            even += 1
        else:
            # swap even and odd
            _swap(list, even, odd)
            odd -= 1


#   5.1 dutch national flag problem
def dutch_national_flag_n_space(list, pivot_idx):
    # create 3 lists: less_than, equal, greater_than
    less_than = []
    greater_than = []
    equal = []

    pivot = list[pivot_idx]

    idx = 0
    while idx < len(list):
        if list[idx] == pivot:
            equal.append(list[idx])
        elif list[idx] < pivot:
            less_than.append(list[idx])
        else:
            greater_than.append(list[idx])
        idx += 1

    # merge all the lists and return
    return less_than + equal + greater_than


def dutch_national_flag(list, pivot_idx):
    pivot = list[pivot_idx]

    # move pivot elem to end of list
    _swap(list, pivot_idx, len(list) - 1)
    end = len(list) - 1

    left = -1
    right = 0
    while right < end:
        if list[right] < pivot:
            left += 1
            _swap(list, right, left)
            right += 1
        elif list[right] == pivot:
            end -= 1
            _swap(list, right, end)
        else:  # list[right] > pivot
            right += 1

    # all greater than are from left + 1 to end - 1
    pivot_start = end
    idx = left + 1
    while pivot_start < len(list):
        _swap(list, idx, pivot_start)
        idx += 1
        pivot_start += 1


#   5.2 increment an arbitrary precision integer
def increment_number(list):
    # inc last element
    list[-1] += 1

    idx = len(list) - 1
    while idx > 0:
        if list[idx] != 10:
            break
        list[idx] = 0
        list[idx - 1] += 1
        idx -= 1

    # instead of recreating a list with extra 1 on left,
    # append 0 to end of list and set 0 to 1
    if list[0] == 10:
        list.append(0)
        list[0] = 1

    return list


#   5.3 multiply two arbitrary precision integer
def multiply_two_numbers(num1, num2):
    sign = -1 if ((num1[0] < 0) ^ (num2[0] < 0)) else 1

    if num1[0] < 0:
        num1[0] = num1[0] * -1

    if num2[0] < 0:
        num2[0] = num2[0] * -1

    if len(num2) > len(num1):
        temp = num2
        num2 = num1
        num1 = temp

    result = [0] * (len(num1) + len(num2))

    num2_idx = len(num2) - 1

    # iterate on steps which is the digits in multiplier
    # dec num2_idx by 1 after each multiplication
    for step in range(0, len(num2)):

        result_idx = len(result) - 1 - step

        #iterate on num1 from right to left
        for num1_idx in reversed(range(len(num1))):
            prod = num1[num1_idx] * num2[num2_idx]

            sum = result[result_idx] + prod
            carry = sum // 10

            result[result_idx] = sum % 10
            result[result_idx - 1] += carry

            result_idx -= 1

        num2_idx -= 1

    idx = 0
    while result:
        if result[idx] != 0:
            break
        del result[idx]

    result[0] = result[0] * sign

    return result


#   5.5 delete duplicates from a sorted array
def delete_duplicates_o_n(list):
    result = []
    look_up = {}
    for i in range(0, len(list)):
        curr = list[i]
        if curr not in look_up:
            result.append(list[i])
        look_up[curr] = True
    return result


#   5.5 delete duplicates from a sorted array
def delete_duplicates(list):
    write_idx = 1
    curr_idx = 1
    while curr_idx < len(list):
        if list[curr_idx - 1] != list[curr_idx]:
            list[write_idx] = list[curr_idx]
            curr_idx += 1
            write_idx += 1
        else:
            curr_idx += 1

    return write_idx


#   5.6 buy and sell a stock once
def max_profit_buy_sell(list):
    """"""
    curr_min = list[0]
    max_profit = 0
    for curr in range(1, len(list)):
        curr_profit = list[curr] - curr_min
        max_profit = max(curr_profit, max_profit)
        curr_min = min(list[curr], curr_min)

    return max_profit


#   5.9 enumerate all primes to n
def get_primes(num):
    # create a boolean array of
    primes = []
    sieve = [False, False] + [True] * (num - 1)

    for curr in range(2, len(sieve)):
        if sieve[curr]:
            primes.append(curr)
            # mark all multiples of curr as False
            for multiple in range(curr * 2, num + 1, curr):
                sieve[multiple] = False

    return primes


#   5.12 sample offline data
def random_sampling(input, k):
    n = len(input)

    for idx in range(k):
        elem_idx = random.randint(idx, n - 1)
        _swap(input, idx, elem_idx)

    return input[0:k]


#   5.15 compute a random subset
def get_random_subset(n: int, k: int):
    look_up = {}
    for idx in range(k):
        rand_idx = random.randint(idx, n)
        if rand_idx in look_up:
            val = look_up[rand_idx]
            look_up[idx] = val
            look_up[rand_idx] = idx
        else:
            look_up[rand_idx] = idx
            look_up[idx] = rand_idx

    return [look_up[i] for i in range(k)]


#   5.11 compute the next permutation
def get_next_permutation(list: List[int]):
    # find the first dip from right to left
    curr_idx = len(list) - 1

    while curr_idx > 0:
        if list[curr_idx] > list[curr_idx - 1]:
            break
        curr_idx -= 1

    if curr_idx == 0:
        return []

    curr_idx -= 1

    # find swap_idx
    swap_idx = len(list) - 1
    while swap_idx > 0:
        if list[swap_idx] > list[curr_idx]:
            break
        swap_idx -= 1

    _swap(list, curr_idx, swap_idx)

    # reverse curr_idx -1 to len(list) - 1
    my_reverse(list, curr_idx + 1)

    return list


#   5.17 the sudoku checker problem
def is_valid_sudoku(grid):
    # check all rows
    row_count = len(grid)
    for row in range(row_count):
        non_zero_items = [elem for elem in grid[row] if elem != 0]
        if len(non_zero_items) != len(set(non_zero_items)):
            return False

    # check all columns
    col_count = len(grid[0])
    for col in range(col_count):
        non_zero_items = []
        for row in range(row_count):
            if grid[row][col] != 0:
                non_zero_items.append(grid[row][col])
        if len(non_zero_items) != len(set(non_zero_items)):
            return False

    # check block
    block_size = floor(sqrt(len(grid)))
    block_range = [(idx * block_size)
                   for idx in range(block_size)]

    for block_row in block_range:
        for block_col in block_range:
            # get data for this block
            # row, col: 0,0; 0,3; 0,6 . . .
            non_zero_items = []
            for row in range(block_row, block_row + block_size):
                for col in range(block_col, block_col + block_size):
                    if grid[row][col] != 0:
                        non_zero_items.append(grid[row][col])
            if len(non_zero_items) != len(set(non_zero_items)):
                return False

    return True


#   5.10 permute the elements of an array
def apply_permutation():
    pass


# todo
#   5.18 compute the spiral ordering of a 2-d array
#   5.19 rotate a 2-d array

def _swap(list, idx_a, idx_b):
    temp = list[idx_a]
    list[idx_a] = list[idx_b]
    list[idx_b] = temp
