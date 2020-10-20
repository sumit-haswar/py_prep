import collections


# Given an 2-d array of integers, find the size of the largest contiguous block
# (horizontally/vertically connected only) of numbers with the same value.

# Examples
# 1 2 3
# 4 1 6
# 4 5 1
# Answer: 2 (of 4s)

# 1 1 1 2 4
# 5 1 5 3 1
# 3 4 2 1 1
# Answer: 4 (of 1s)

# 3 3 3 3 3 1
# 3 4 4 4 3 4
# 2 4 3 3 3 4
# 2 4 4 4 4 4
# Answer: 11 (of 4s)

# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 0 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# Answer: 24 (of 1s)

def find_max_contiguous_block(input) -> int:
    rows = len(input)  # 4
    cols = len(input[0])  # 5
    max_till_now = 0

    is_visited = [[False] * cols for _ in range(rows)]

    for curr_row in range(0, rows):
        for curr_col in range(0, cols):

            if is_visited[curr_row][curr_col]:
                continue

            curr_queue = collections.deque()

            curr_queue.append((curr_row, curr_col))

            curr_count = 0
            curr_val = input[curr_row][curr_col]  # 1

            while curr_queue:
                curr = curr_queue.popleft()  # 0,0

                is_visited[curr[0]][curr[1]] = True
                curr_count += 1  # 2

                # get all adjacent cells
                adjacent_cells = _get_adjacent_cells(curr[0], curr[1])

                for adj_cell in adjacent_cells:
                    if adj_cell[0] < 0 or adj_cell[1] < 0 or adj_cell[0] >= rows or adj_cell[1] >= cols:
                        continue

                    if is_visited[adj_cell[0]][adj_cell[1]] is True:
                        continue

                    adj_val = input[adj_cell[0]][adj_cell[1]]

                    if adj_val == curr_val:
                        curr_queue.append([adj_cell[0], adj_cell[1]])

            max_till_now = max(max_till_now, curr_count)

    return max_till_now


def _get_adjacent_cells(row, col):
    top = (row - 1, col)
    right = (row, col + 1)
    bottom = (row + 1, col)
    left = (row, col - 1)

    return [top, right, bottom, left]


# 3 3 3 3 3 1
# 3 4 4 4 3 4
# 2 4 3 3 3 4
# 2 4 4 4 4 4
input = [[3, 3, 3, 3, 3, 1],
         [3, 4, 4, 4, 3, 4],
         [2, 4, 3, 3, 3, 4],
         [2, 4, 4, 4, 4, 4]]

if __name__ == '__main__':
    print("The max is", find_max_contiguous_block(input))
