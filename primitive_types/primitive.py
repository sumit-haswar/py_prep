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

# 4.1   compute parity of a word
def get_parity(num):
    pass

def get_parity_use_lowest_set(num):
    """time-complexity: O(k), where k is the number of bits set to 1"""
    parity = 0
    while num:
        # alternately flip parity between 1 and 0
        parity ^= 1
        # clear the lowest non-zero bit of the number
        num = num & (num - 1)
    return parity

def get_parity_caching(num):
    pass

def get_parity_xor(num):
    pass


# 4.2   swap bits

# 4.3   reverse bits

# 4.7   compute pow(x, y)

# 4.8   reverse digits

# 4.11  rectangle intersection
