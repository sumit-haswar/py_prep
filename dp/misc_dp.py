from typing import List


def count_unique_paths(total_rows: int, total_cols: int) -> int:
    def _unique_paths(row, col) -> int:
        # base-cases
        if row < 0 or col < 0:
            return 0

        if row == 0 and col == 1:
            return 1
        if row == 1 and col == 0:
            return 1

        return _unique_paths(row - 1, col) + _unique_paths(row, col - 1)

    return _unique_paths(total_rows - 1, total_cols - 1)


def count_unique_paths_dp(m: int, n: int) -> int:
    dp_lookup = []

    # init dp_lookup first row
    first_row = []
    for col in range(n):
        first_row.append(1)

    dp_lookup.append(first_row)

    for r in range(1, m):
        curr_row = [1]
        for c in range(1, n):
            curr_row.append(0)
        dp_lookup.append(curr_row)

    # iter dp_lookup 1,1 --> m - 1, n - 1
    for r in range(1, m):
        for c in range(1, n):
            dp_lookup[r][c] = dp_lookup[r - 1][c] + dp_lookup[r][c - 1]

    return dp_lookup[-1][-1]


def max_path_sum(matrix: List) -> int:
    def _max_path_sum(row: int, col: int) -> int:
        # base cases
        if row < 0 or col < 0:
            return 0
        if row == 0 and col == 0:
            return matrix[row][col]

        top_cell = _max_path_sum(row - 1, col)
        left_cell = _max_path_sum(row, col - 1)

        return max(top_cell + matrix[row][col], left_cell + matrix[row][col])

    return _max_path_sum(len(matrix) - 1, len(matrix[0]) - 1)


def max_path_sum_dp(matrix: List) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    dp_lookup = []

    # init first row of dp_lookup
    first_row = [matrix[0][0]]
    for col in range(1, cols):
        first_row.append(first_row[col - 1] + matrix[0][col])

    dp_lookup.append(first_row)

    # init first col of dp_lookup
    for r in range(1, rows):
        curr_row = []
        for c in range(0, cols):
            if c == 0:
                curr_row.append(dp_lookup[r - 1][0] + matrix[r][0])
            else:
                curr_row.append(0)
        dp_lookup.append(curr_row)

    for row in range(1, rows):
        for col in range(1, cols):
            top_cell = dp_lookup[row - 1][col] + matrix[row][col]
            left_cell = dp_lookup[row][col - 1] + matrix[row][col]

            dp_lookup[row][col] = max(top_cell, left_cell)

    return dp_lookup[-1][-1]


def min_cost_stair_climb(steps: List) -> int:
    def _min_cost_stair_climb(position) -> int:
        if position == 0 or position == 1:
            return steps[position]

        prev_step_cost = _min_cost_stair_climb(position - 1) + steps[position]

        prev_prev_step_cost = _min_cost_stair_climb(position - 2) + steps[position]

        return min(prev_step_cost, prev_prev_step_cost)

    steps = [0] + steps + [0]
    return _min_cost_stair_climb(len(steps) - 1)


def min_cost_stair_climb_dp(steps: List) -> int:
    steps = [0] + steps + [0]
    dp_lookup = [0] * len(steps)

    # initiate base-cases
    dp_lookup[1] = steps[1]
    dp_lookup[2] = steps[2]

    for idx in range(3, len(dp_lookup)):
        prev_step_cost = dp_lookup[idx - 1] + steps[idx]
        prev_prev_cost = dp_lookup[idx - 2] + steps[idx]

        dp_lookup[idx] = min(prev_step_cost, prev_prev_cost)

    return dp_lookup[-1]


def coin_change_recur(total: int, coins: List[int]) -> int:
    def _coin_change_recur(sub_total, coin_count):
        # base case
        if sub_total == 0:
            if coin_count < min_so_far[0]:
                min_so_far[0] = coin_count

        if sub_total < 0:
            return

        for curr_coin in coins:
            _coin_change_recur(sub_total - curr_coin, coin_count + 1)

    min_so_far = [float('inf')]
    _coin_change_recur(total, 0)
    return min_so_far[0] if min_so_far[0] != float('inf') else -1


def coin_change_greedy():
    pass


def coin_change_memoized(total: int, coins: List[int]):
    def _coin_change_memo(curr_total, curr_count):
        if curr_total in dp_memo:
            return dp_memo[curr_total] + curr_count
        # base case
        if curr_total == 0:
            return curr_count

        min_val = float('inf')
        for coin in coins:
            if curr_total - coin >= 0:
                min_val = min(min_val, _coin_change_memo(curr_total - coin, curr_count + 1))

        dp_memo[curr_total] = min_val

        return min_val

    dp_memo = {}
    for coin in coins:
        dp_memo[coin] = 1
    _coin_change_memo(total, 0)
    return dp_memo[total]


def coin_change_dp(total, coins):
    dp_lookup = [None] * (total + 1)
    dp_lookup[0] = 0
    for coin in coins:
        dp_lookup[coin] = 1

    for idx in range(1, total + 1):
        min_val = float('inf')
        for coin in coins:
            if idx - coin >= 0:
                min_val = min(min_val, dp_lookup[idx - coin])

        dp_lookup[idx] = min_val + 1

    return dp_lookup[total]


def rod_cutting_recur(l: int, prices):
    def _rod_cutting_recur(curr_len, curr_profit):
        if curr_len == 0:
            max_so_far[0] = max(max_so_far[0], curr_profit)
            return

        for dimension, price in prices.items():
            # you can't cut rod(left) more than dimension,
            if curr_len - dimension >= 0:
                _rod_cutting_recur(curr_len - dimension, curr_profit + price)

    max_so_far = [0]
    _rod_cutting_recur(l, 0)
    return max_so_far[0]


def rod_cutting_recur2(l: int, prices: List[int]):
    def _rod_cutting_recur2(curr_length):
        if curr_length == 0:
            return 0

        max_profit = 0
        for cut in range(curr_length):
            profit = _rod_cutting_recur2(cut) + prices[curr_length - cut]
            max_profit = max(max_profit, profit)
        return max_profit

    return _rod_cutting_recur2(l)


# todo
# given a DAG find the max sum path(edge have weights)
# from source-vertex to dest-vertex
if __name__ == '__main__':
    # step_costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # print(min_cost_stair_climb(step_costs))
    # print(min_cost_stair_climb_dp(step_costs))

    matrix = [
        [2, 3, 4, 1, 0],
        [1, 3, 4, 1, 0],
        [4, 3, 4, 1, 0],
    ]
    # print(max_path_sum(matrix))
    # print(max_path_sum_dp(matrix))

    # # exp o/p = 6
    # step_costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    # print(coin_change_recur(100, [5,7, 10]))
    # print(coin_change_dp(200, [5, 7, 10]))
    # print(coin_change_memoized(13, [1, 3, 5]))

    print(rod_cutting_recur2(5, [0, 4, 10, 13, 200, 200]))
    print(rod_cutting_recur(5, {1: 4, 2: 10, 3: 13, 4: 200}))
