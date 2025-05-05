from typing import List, Dict
from collections import deque
import string


class MatchResult:
    def __init__(self, winner: str, loser: str):
        self.winner = winner
        self.loser = loser


class Point:
    def __init__(self, x, y, val=None):
        self.x = x
        self.y = y
        self.val = val

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_neighbors(self) -> List['Point']:
        return [
            Point(self.x + 1, self.y),
            Point(self.x - 1, self.y),
            Point(self.x, self.y + 1),
            Point(self.x, self.y - 1),
        ]

    def is_out_of_bound(self, row_max, col_max) -> bool:
        if self.x < 0 or self.y < 0:
            return True

        if self.x > row_max or self.y > col_max:
            return True

        return False


# graph boot camp
def can_team_a_beat_team_b(matches: List[MatchResult], team_a: str, team_b: str) -> bool:
    winner_loser_map: Dict[str, set] = {}
    visited = set()

    def _can_a_beat_b_recur(curr_team, team_b):
        if curr_team == team_b:
            return True

        visited.add(curr_team)

        if curr_team not in winner_loser_map:  # cur team has not defeated anybody
            return False

        # recur case:
        for loser in winner_loser_map[curr_team]:
            if loser not in visited:
                res = _can_a_beat_b_recur(loser, team_b)
                if res:
                    return True

        return False

    # create a dictionary from list of matches
    for match in matches:
        if match.winner not in winner_loser_map:
            winner_loser_map[match.winner] = set()
        winner_loser_map[match.winner].add(match.loser)

    return _can_a_beat_b_recur(team_a, team_b)


#   18.1    search a maze, find a path from point `start` to point `end` of a 2d maze array
def find_maze_path(maze: List[List], start: Point, end: Point) -> List[Point]:
    row_limit = len(maze) - 1
    col_limit = len(maze[0]) - 1

    visited = [[False] * (col_limit + 1) for _ in range(row_limit + 1)]
    path: List = []

    def _find_maze_path_recur(curr_point: Point) -> bool:
        if curr_point == end:  # reached end
            path.append((curr_point.x, curr_point.y))
            return True

        visited[curr_point.x][curr_point.y] = True
        path.append((curr_point.x, curr_point.y))
        neighbors = curr_point.get_neighbors()
        for neighbor in neighbors:
            if (neighbor.is_out_of_bound(row_limit, col_limit)
                    or visited[neighbor.x][neighbor.y]
                    or maze[neighbor.x][neighbor.y] == "B"):
                continue

            if _find_maze_path_recur(neighbor):
                return True

        del path[-1]
        return False

    _find_maze_path_recur(start)

    return path


#   18.1    search a maze, find a path from point `start` to point `end` of a 2d maze array
def find_maze_path_bfs(maze: List, start, end) -> str:
    dq = deque()
    total_rows = len(maze)
    total_cols = len(maze[0])

    visited = [[False] * total_cols for x in range(total_rows)]

    # add start point to deque
    dq.append((start, ""))

    while dq:
        curr, path = dq.popleft()
        if curr == end:
            # reached destination
            return path + "->" + f"({curr.x},{curr.y})"

        visited[curr.x][curr.y] = True

        path = path + "->" + f"({curr.x},{curr.y})"

        neighbors = curr.get_neighbors()
        for neighbor in neighbors:
            if (neighbor.is_out_of_bound(total_rows - 1, total_cols - 1)
                    or visited[neighbor.x][neighbor.y]
                    or maze[neighbor.x][neighbor.y] == "B"):
                continue
            dq.append((neighbor, path))

    return "destination not found"


#   18.7    transform one string to another
def transform_string(src: str, dest: str, dictionary: {}) -> (str, int):
    dq = deque()

    dq.append((src, 0, src))
    dictionary.remove(src)

    while dq:
        curr_word, dist, path = dq.popleft()
        if curr_word == dest:
            # destination word found
            return path, dist

        for idx in range(len(curr_word)):
            for c in string.ascii_lowercase:
                next_word = curr_word[:idx] + c + curr_word[idx + 1:]
                if next_word in dictionary:
                    dq.append((next_word, dist + 1, path + "->" + next_word))
                    dictionary.remove(next_word)

    return "", -1


#   18.2    paint a boolean matrix, wap that takes an n x m bool arr and a point A.
#               flips the color of the region associated with point
def flip_color(maze: List, point: Point) -> List:
    row_max = len(maze) - 1
    col_max = len(maze[0]) - 1

    point_color = maze[point.x][point.y]
    dq = deque()
    # flip current point and append
    maze[point.x][point.y] = not maze[point.x][point.y]
    dq.append(point)

    while dq:

        curr = dq.popleft()

        for neighbor in curr.get_neighbors():
            if neighbor.is_out_of_bound(row_max, col_max) or maze[neighbor.x][neighbor.y] != point_color:
                continue
            # flip and append
            maze[neighbor.x][neighbor.y] = not maze[neighbor.x][neighbor.y]
            dq.append(Point(neighbor.x, neighbor.y))

    return maze


#   18.3    compute enclosed regions, take a 2D array with W or B, replace all Ws that cannot
#               reach the boundary with a B

#   18.5    clone a graph

#   18.4    deadlock detection

if __name__ == "__main__":
    # matches = [
    #     MatchResult("a", "x"),
    #     MatchResult("a", "y"),
    #     MatchResult("a", "z"),
    #     MatchResult("z", "p"),
    #     MatchResult("z", "q"),
    #     MatchResult("y", "b"),
    #     MatchResult("b", "c"),
    # ]
    # res = can_team_a_beat_team_b(matches, "a", "y")

    maze = [
        # 0     1       2
        [False, False, False],  # 0
        [True, True, True],  # 1
        [False, False, False]  # 2
    ]

    dictionary = {"cat", "hat", "matrix", "pat", "rat", "pot", "poo"}

    res = flip_color(maze, Point(0, 0))

    print(res)
