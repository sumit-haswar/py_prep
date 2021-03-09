from collections import deque
from string import ascii_lowercase, ascii_uppercase


# Complete the function below.

def _get_neighbors(row, col):
    top = (row - 1, col)
    right = (row, col + 1)
    bottom = (row + 1, col)
    left = (row, col - 1)

    return [top, right, bottom, left]


class XY:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.path_so_far = []
        self.path_keys = set()


def _get_start(grid, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                return i, j


def find_shortest_path(grid):
    rows = len(grid)
    cols = len(grid[0])

    start_row, start_col = _get_start(grid, rows, cols)

    queue = deque()
    start_node = XY(start_row, start_col)
    start_node.path_so_far.append([start_row, start_col])
    queue.append(start_node)

    visited = []
    for i in range(rows):
        curr_row = []
        for j in range(cols):
            curr_row.append(False)
        visited.append(curr_row)

    visited[start_row][start_col] = True

    while queue:
        curr = queue.popleft()

        neighbors = _get_neighbors(curr.row, curr.col)

        for neighbor in neighbors:
            r = neighbor[0]
            c = neighbor[1]
            if r < 0 or c < 0 or r >= rows or c >= cols:
                continue

            # if visited[r][c] is True:
            #     continue

            char = grid[r][c]

            if char == '#':
                continue
            elif (char == '.' or char == '@') and visited[r][c] is False:
                # visited[r][c] = True
                neighbor_node = XY(r, c)
                neighbor_node.path_so_far = [] + curr.path_so_far
                neighbor_node.path_so_far.append([neighbor_node.row, neighbor_node.col])
                neighbor_node.path_keys = curr.path_keys
                queue.append(neighbor_node)
            elif char == '+':
                # goal found!
                curr.path_so_far.append([r, c])
                return curr.path_so_far
            elif char in ascii_lowercase and visited[r][c] is False:
                # node is either key or door
                # visited[r][c] = True
                neighbor_node = XY(r, c)
                neighbor_node.path_so_far = [] + curr.path_so_far
                neighbor_node.path_so_far.append([neighbor_node.row, neighbor_node.col])
                neighbor_node.path_keys = curr.path_keys
                neighbor_node.path_keys.add(char)
                queue.append(neighbor_node)
            elif char in ascii_uppercase and char.lower() in curr.path_keys and visited[r][c] is False:
                # visited[r][c] = True
                neighbor_node = XY(r, c)
                neighbor_node.path_so_far = [] + curr.path_so_far
                neighbor_node.path_so_far.append([neighbor_node.row, neighbor_node.col])
                neighbor_node.path_keys = curr.path_keys
                queue.append(neighbor_node)


if __name__ == '__main__':
    # grid = ["...B",
    #         ".b#.",
    #         "@#+."]
    grid = [
        "+B...",
        "####.",
        "##b#.",
        "a...A",
        "##@##"
    ]
    print(find_shortest_path(grid))
