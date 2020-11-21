def bit_count(num):
    count = 0
    while num:
        result = num & 1
        num = num >> 1
        if result:
            count += 1

    return count


# clear the lowest set bit
def clear_lowest(num):
    return num & (num - 1)


# set the lower-most/right-most 0
def set_lowest(num):
    return num | (num + 1)


# get bit index
def get_lowest_set_idx(num):
    pass


def get_lowest_unset_idx(num):
    pass


# 4.1   compute parity of a 64-bit word
def get_parity_use_lowest_set(num):
    """time-complexity: O(k), where k is the number of bits in num set to 1"""
    parity = 0
    while num:
        # alternately flip parity between 1 and 0
        parity ^= 1
        # clear the lowest non-zero bit of the number
        num = num & (num - 1)
    return parity


def get_parity_caching(num):
    # num is 64 bit in size
    # create parity cache of 0 - (2^16 - 1)
    parity_cache = {}
    for i in range(0, 2 ** 16):
        parity_cache[i] = get_parity_use_lowest_set(i)

    # divide num into 4 sub words of 16 bits each
    shift_size = 16
    mask = (2 ** 16) - 1

    result = parity_cache[num >> (3 * shift_size)] \
             ^ parity_cache[(num >> (2 * shift_size)) & mask] \
             ^ parity_cache[(num >> shift_size) & mask] \
             ^ parity_cache[num & mask]

    return result


def get_parity_xor(num):
    powers = [5, 4, 3, 2, 1, 0]
    for power in powers:
        shift_bits = 1 << power
        num ^= (num >> shift_bits)

    return num & 1


# 4.2   swap bits
def swap_bits(num, i, j):
    # swap only if bits are different
    if (num >> i) & 1 != (num >> j) & 1:
        # create to masks: 1 << i and 1 << j
        # create an OR of these masks
        i_mask = 1 << i
        j_mask = 1 << j
        mask = i_mask | j_mask
        # now we just xor this with num
        num ^= mask

    return num


# 4.3   reverse bits
def reverse_bits(num):
    """Iterate through the 32 least significant bits and
    swap with corresponding 32 most significant bits"""
    diff = 63
    for idx in range(0, 32):
        swap_idx = diff + idx
        num = swap_bits(num, idx, swap_idx)
        diff -= 2

    return num


def reverse_bits_cached(num):
    # create cache of reverse from 0 to 65,535
    reverse_cache = {}
    for entry in range(0, (2 ** 16)):
        reverse_cache[entry] = reverse_bits(entry)

    # now for 4 sub-words in num 3(16),2(16),1(16) and 0(16)
    shift_size = 16
    mask = (2 ** 16) - 1

    msb = reverse_cache[num & mask] << (3 * shift_size)
    # >> by shift_size --> & with mask to clear --> look-up in cache --> left shift by twice
    mid_left = reverse_cache[(num >> shift_size) & mask] << (2 * shift_size)
    # >> by 2 * shift_size --> & with mask to clear --> look-up in cache --> left shift once
    mid_right = reverse_cache[(num >> (2 * shift_size)) & mask] << shift_size
    lsb = reverse_cache[(num >> (3 * shift_size)) & mask]

    return msb | mid_left | mid_right | lsb


# 4.7   compute pow(x, y)
def power(num, pow):
    """Use divide and conquer to get power of a number"""
    # base-cases
    if pow == 0:
        return 1
    elif pow == 1:
        return num
    else:
        result = power(num, pow // 2)
        # if power is even:
        if pow % 2 == 0:
            return result * result
        else:
            return num * result * result


# 4.8   reverse digits
def reverse_digits(num):
    """"""
    result = 0
    num_process = abs(num)
    while num_process:
        remainder = num_process % 10
        result = (result * 10) + remainder
        num_process = num_process // 10

    return result if num > 0 else -result


# 4.11  rectangle intersection
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def _is_intersecting(rectangle_1: Rectangle, rectangle_2: Rectangle):
    """two rects are intersecting if r1.x falls within r2.x + width and vice versa and
     r1.y falls within r2.y + height"""
    return rectangle_1.x <= (rectangle_2.x + rectangle_2.width) \
           and rectangle_2.x <= (rectangle_1.x + rectangle_1.width) \
           and rectangle_1.y <= (rectangle_2.y + rectangle_2.height) \
           and rectangle_2.y <= (rectangle_1.y + rectangle_1.height)


def intersecting_rectangle(rectangle_1: Rectangle, rectangle_2: Rectangle):
    if not _is_intersecting(rectangle_1, rectangle_2):
        return Rectangle(-1, -1, 0, 0)

    x, y = max(rectangle_1.x, rectangle_2.x), max(rectangle_1.y, rectangle_2.y)

    width = min(rectangle_1.x + rectangle_1.width, rectangle_2.x + rectangle_2.width) \
            - max(rectangle_1.x, rectangle_2.x)

    height = min(rectangle_1.y + rectangle_1.height, rectangle_2.y + rectangle_2.height) \
             - max(rectangle_1.y, rectangle_2.y)

    return Rectangle(x, y, width, height)
