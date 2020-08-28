def power(num, pow):
    if pow <= 0:
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
    pass


def reverse_bits_cached(num):
    pass

# 4.7   compute pow(x, y)

# 4.8   reverse digits

# 4.11  rectangle intersection
