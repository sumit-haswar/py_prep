from typing import List, Optional
import random


#   even-odd partition
def even_odd_partition(arr: List[int]):
    even_idx = 0
    odd_idx = len(arr) - 1
    while even_idx < odd_idx:
        if arr[even_idx] % 2 == 1:
            # swap with odd-idx
            arr[even_idx], arr[odd_idx] = arr[odd_idx], arr[even_idx]
            odd_idx -= 1
        else:
            even_idx += 1

    return arr


#   5.1 the dutch national flag problem
def dutch_national_flag(arr: List[int], pivot_idx: int):

    pivot_val = arr[pivot_idx]
    smaller, curr, larger = 0, 0, len(arr)

    while curr < larger:
        curr_val = arr[curr]
        if curr_val < pivot_val:
            arr[smaller], arr[curr] = arr[curr], arr[smaller]
            smaller += 1
            curr += 1
        elif curr_val > pivot_val:
            larger -= 1
            arr[larger], arr[curr] = arr[curr], arr[larger]
        else:   # curr_val == pivot_val
            curr += 1


#   5.6 buy and sell a stock once
#       [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
def buy_sell_stock(seq: List[int]) -> int:
    min_so_far = seq[0]
    max_profit = 0

    for idx in range(1, len(seq)):
        curr_profit = seq[idx] - min_so_far
        max_profit = max(max_profit, curr_profit)
        min_so_far = min(min_so_far, seq[idx])

    return max_profit


#   5.12 sample offline data
def sample_offline_data(arr: List[int], k: int) -> List[int]:
    res = []
    for idx in range(k):
        rand_idx = random.randint(idx, len(arr) - 1)
        res.append(arr[rand_idx])
        arr[idx], arr[rand_idx] = arr[rand_idx], arr[idx]

    return res


#   5.18    compute the spiral ordering of a 2d-array
def get_spiral_ordering(arr_2d: List[int]):
    pass


#   5.2 increment an arbitrary precision integer by 1
def inc_int_by_one(num_seq: List[int]) -> List[int]:
    num_seq[-1] += 1

    if num_seq[-1] < 10:
        return num_seq

    curr_idx = len(num_seq) - 1
    while curr_idx >= 1:
        if num_seq[curr_idx] > 9:
            num_seq[curr_idx] = 0
            num_seq[curr_idx - 1] += 1
            curr_idx -= 1
        else:
            break

    if num_seq[0] > 9:
        num_seq[0] = 0
        return [1] + num_seq

    return num_seq


#   5.5 delete duplicates from a sorted array
# 3,6,7,8,8,9,9,10,14,14,14,17
def delete_duplicates(arr: List[int]) -> int:
    if not arr or len(arr) == 1:
        return 0

    write_idx = 1
    read_idx = 1
    while read_idx < len(arr):
        if arr[read_idx - 1] != arr[read_idx]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
            read_idx += 1
        else:
            read_idx += 1

    return write_idx


#   5.3 multiply two arbitrary precision numbers
def multiply_two_numbers(a: List[int], b: List[int]) -> List[int]:
    res = [0] * (len(a) + len(b))


#   5.11    compute the next permutation
#   [4, 2, 4, 3]
def get_next_permutation(seq: List[int]) -> Optional[List[int]]:
    right_idx = len(seq) - 1
    while right_idx > 0:
        if seq[right_idx - 1] < seq[right_idx]:
            break
        right_idx -= 1

    if right_idx == 0:
        return None

    pivot_idx = right_idx - 1

    swap_idx = len(seq) - 1
    while swap_idx > 0:
        if seq[swap_idx] > seq[pivot_idx]:
            break
        swap_idx -= 1

    seq[pivot_idx], seq[swap_idx] = seq[swap_idx], seq[pivot_idx]

    # reverse, pivot_idx + 1: end

    # look for element to right of
    return seq[:pivot_idx + 1] + list(reversed(seq[pivot_idx + 1:]))


#   5.19    rotate a 2d-array
def rotate_2d_array(arr: List[List[int]]):
    pass


# todo
#   5.10    permute the elements of an array <--!
#   5.9     enumerate all primes to n
#   5.15    compute a random subset
#   5.17    the sudoku checker problem


if __name__ == "__main__":
    # print(get_next_permutation([4, 3, 1, 7, 0]))
    arr = [2,3,4,5,6]

    k = delete_duplicates(arr)
    print(arr[:k])
