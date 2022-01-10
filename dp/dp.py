# Input: n=7, steps=[2, 3]
# Output: 3
# Three ways to reach: [{2, 2, 3}, {2, 3, 2}, {3, 2, 2}]

def countWaysToClimbRecur(steps, n):
    def _countWaysToClimb(n):
        # base-case
        if n == 0:
            total_count[0] += 1
            return
        if n < 0:
            return

        for step in steps:
            if n - step >= 0:
                _countWaysToClimb(n - step)

    total_count = [0]

    _countWaysToClimb(n)
    return total_count[0]


def countWaysToClimbMemo(steps, n):
    def _countWaysToClimb(n, curr_count):
        if n in dp_map:
            return dp_map[n]

        if n == 0:
            return curr_count + 1
        if n < 0:
            return 0
        total_count = 0
        for step in steps:
            if n - step >= 0:
                total_count = total_count + _countWaysToClimb(n - step, curr_count)

        dp_map[n] = total_count
        return total_count

    dp_map = {}
    _countWaysToClimb(n, 0)
    print(dp_map)
    return dp_map[n]


def maxStolenValue(values):
    def _max_stolen_val(curr_houses, curr_idx, curr_val):
        # base-case
        if curr_idx >= len(values):
            return curr_val

        curr_houses.append(values[curr_idx])
        with_curr = _max_stolen_val(curr_houses, curr_idx + 2, curr_val + values[curr_idx])
        del curr_houses[-1]

        without_curr = _max_stolen_val(curr_houses, curr_idx + 1, curr_val)

        return max(with_curr, without_curr)

    return _max_stolen_val([], 0, 0)


def maxStolenValueMemo(values):
    def _max_stolen_val(curr_houses, curr_idx, curr_val):

        if curr_idx in memo:
            return memo[curr_idx]

        # base-case
        if curr_idx >= len(values):
            return curr_val

        curr_houses.append(values[curr_idx])
        with_curr = _max_stolen_val(curr_houses, curr_idx + 2, curr_val + values[curr_idx])
        del curr_houses[-1]

        without_curr = _max_stolen_val(curr_houses, curr_idx + 1, curr_val)

        max_curr = max(with_curr, without_curr)
        memo[curr_idx] = max_curr

        return max_curr

    memo = {}
    _max_stolen_val([], 0, 0)
    print(memo)


def maxStolenValueDp(values):
    table = [0] * (len(values) + 1)

    # init table
    table[0] = 0
    table[1] = values[0]

    for idx in range(2, len(table)):
        # max of prev OR curr + prev of prev
        table[idx] = max(table[idx - 1], (table[idx - 2] if idx >= 2 else 0) + values[idx - 1])

    print(table)


# Given a phone keypad as shown below:
# 1 2 3
# 4 5 6
# 7 8 9
# – 0 –

phone_keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 0, 1]
]

neighbors_map = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]

}


def get_neighbors(digit):
    return neighbors_map[digit]


def num_phone_numbers_recur(start_digit, phone_number_length):
    def _num_phone_numbers_recur(curr_digit, phone_number):
        if len(phone_number) == phone_number_length:
            total_count[0] += 1
            return

        neighbors = get_neighbors(curr_digit)
        for neighbor in neighbors:
            _num_phone_numbers_recur(neighbor, phone_number + str(neighbor))

    total_count = [0]
    _num_phone_numbers_recur(start_digit, str(start_digit))
    return total_count[0]


def num_phone_numbers_memo(start_digit, phone_number_length):
    def _num_phone_numbers_recur(curr_digit, curr_length):

        map_key = "{}-{}".format(curr_digit, curr_length)
        if map_key in dp_map:
            return dp_map[map_key]
        # base-case
        if curr_length == 0:
            return 1

        count = 0
        neighbors = get_neighbors(curr_digit)
        for neighbor in neighbors:
            count = count + _num_phone_numbers_recur(neighbor, curr_length - 1)

        dp_map[map_key] = count

        return count

    dp_map = {}
    _num_phone_numbers_recur(start_digit, phone_number_length - 1)
    return dp_map["{}-{}".format(start_digit, phone_number_length - 1)]
    # return dp_map[-1]


# todo
def num_phone_numbers_dp():
    pass


# Word Break Count
#
# Given a dictionary of words and a string, find the number of ways the string can be broken down into the dictionary
# words. Return the answer modulo 10^9 + 7.
#
#
# Example
# Input: Dictionary: [“kick", "start", "kickstart", "is", "awe", "some", "awesome”]. String: “kickstartisawesome”.
# Output: 4
# Here are all four ways to break down the string into the dictionary words:
#
# kick start is awe some
# kick start is awesome
# kickstart is awe some
# kickstart is awesome
# 4 % 1000000007 = 4 so the correct output is 4

# Example One
# Input: startdigit = 1, phonenumberlength = 2
# Output: 2
# Two possible numbers of length 2: 16, 18.
#
# Example Two
# Input: startdigit = 1, phonenumberlength = 3
# Output: 5
# The possible numbers of length 3: 160, 161, 167, 181, 183

def find_prefix_index(dictionary, txt):
    prefix_idx_list = []
    for pivot_idx in range(1, len(txt)):
        if txt[:pivot_idx] in dictionary:
            prefix_idx_list.append(pivot_idx)

    if txt in dictionary:
        prefix_idx_list.append(len(txt))

    return prefix_idx_list


def wordBreakCountRecur(dictionary, txt):
    dictionary = set(dictionary)

    def _wordBreakCountRecur(prefix, curr_txt):
        # base case
        if not curr_txt:
            result.append(prefix.strip())
            return

        for candidates in find_prefix_index(dictionary, curr_txt):
            curr_prefix = curr_txt[:candidates]
            _wordBreakCountRecur(prefix + ' ' + curr_prefix, curr_txt[candidates:])

    result = []
    _wordBreakCountRecur('', txt)
    return len(result)


def wordBreakCount(dictionary, txt):
    dictionary = set(dictionary)

    def _wordBreakCount(prefix, curr_txt):
        if curr_txt in dp_map:
            return dp_map[curr_txt]

        # base case
        if not curr_txt:
            return 1

        count = 0
        for candidate in find_prefix_index(dictionary, curr_txt):
            curr_prefix = curr_txt[:candidate]
            count = count + _wordBreakCount(prefix + ' ' + curr_prefix, curr_txt[candidate:])

        dp_map[curr_txt] = count
        return count

    dp_map = {}
    _wordBreakCount('', txt)
    return dp_map[txt]


if __name__ == '__main__':
    # print(maxStolenValue([1, 2, 4, 5, 1]))
    # print(maxStolenValue([6, 1, 2, 7]))
    #
    # print(maxStolenValueDp([1, 2, 4, 5, 1]))
    # print(maxStolenValueDp([6, 1, 2, 7]))
    steps = [1, 2, 3, 4, 5]
    n = 5
    # --> 16
    # [2, 3], 7) --> 3
    # print(countWaysToClimbMemo(steps, n))
    # print(countWaysToClimb(steps, n))
    # print(num_phone_numbers_recur(1, 7))
    # print(num_phone_numbers_memo(1, 7))
    dictionary = {"kick", "start", "kickstart", "is", "awe", "some", "awesome"}
    txt = 'kickstartisawesome'
    print(wordBreakCountRecur(dictionary, "kickstartisawesome"))
    print(wordBreakCount(dictionary, "kickstartisawesome"))
