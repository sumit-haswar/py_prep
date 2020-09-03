# reverse a list in-place
def my_reverse(list):
    left = 0
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
        else:
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
    pass


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
    sieve = [False, False] + [True] * (num - 1)

    for i in range(2, len(sieve)):
        curr = sieve[i]
        if curr:
            # mark all multiples as False
            for j in range(curr + 1, len(sieve)):
                candidate = sieve[j]
                if candidate % curr == 0:
                    sieve[j] = False

    return [idx for idx, elem in enumerate(sieve) if elem]

#   5.12 sample offline data
def random_sampling(input, k):
    pass


#   5.17 the sudoku checker problem

#   5.18 compute the spiral ordering of a 2-d array


#   5.10 permute the elements of an array
#   5.15 compute a random subset
#   5.11 compute the next permutation

def _swap(list, idx_a, idx_b):
    temp = list[idx_a]
    list[idx_a] = list[idx_b]
    list[idx_b] = temp
