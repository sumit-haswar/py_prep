import collections
import string
from typing import Tuple, List, Set

WHITE = 0
BLACK = 1


class Team():
    def __init__(self, name, victories):
        self.name = name
        self.victories = victories

    def __str__(self):
        return str(self.name)


class Coordinate():
    def __init__(self, x, y, val=0):
        self.x = x
        self.y = y
        self.val = val

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "{}:{}".format(self.x, self.y)


class GraphVertex():
    WHITE, GRAY, BLACK = range(3)

    def __init__(self, val=0):
        self.val = val
        self.color = GraphVertex.WHITE
        self.edges: List['GraphVertex'] = []

    def __str__(self):
        return "{} -> {} edges".format(str(self.val), len(self.edges))


#   can team a beat team b
def can_team_a_beat_team_b(team_a: str, team_b: str, matches: List[Tuple]):
    def _can_team_a_beat_team_b(team_a: str, team_b: str, team_graph, visited):
        if (team_a not in team_graph) or (team_a in visited):
            return False
        # set of all teams defeated by team_a
        victories = team_graph[team_a]
        if team_b in victories:
            return True
        visited.add(team_a)
        for opponent in team_graph[team_a]:
            beats = _can_team_a_beat_team_b(opponent, team_b, team_graph, visited)
            if beats:
                return True
            else:
                continue

        return False

    # construct team graph (map)
    team_graph = {}
    for result in matches:
        winner = result[0]
        loser = result[1]
        if winner not in team_graph:
            team_graph[winner] = set()
        team_graph[winner].add(loser)
    visited = set()

    return _can_team_a_beat_team_b(team_a, team_b, team_graph, visited)


#   18.1 search a maze
def search_maze(maze: List[List[int]], start: Coordinate, end: Coordinate):
    def _search_maze(curr: Coordinate) -> bool:
        if curr == end:
            path.append(curr)
            return True

        adjacent_cells = _get_adjacent_cells(curr.x, curr.y)
        # recur on adjacent cells of curr
        for cell in adjacent_cells:
            x = cell[0]
            y = cell[1]
            if x < 0 or x >= rows or y < 0 or y >= cols or maze[x][y] == 1:
                continue
            path.append(curr)
            maze[x][y] = 1
            result = _search_maze(Coordinate(x, y, maze[x][y]))
            if result:
                return True
            del path[-1]

        return False

    path = []
    rows = len(maze)
    cols = len(maze[0])
    _search_maze(start)
    return path


#   18.2 paint a boolean matrix
def flip_color(matrix: List[List[int]], cell: Tuple):
    row = len(matrix)
    col = len(matrix[0])
    # flip and enqueue cell
    matrix[cell[0]][cell[1]] = 1
    q = collections.deque()
    q.append(cell)
    while q:
        curr = q.popleft()
        adjacent_cells = _get_adjacent_cells(curr[0], curr[1])
        for cell in adjacent_cells:
            r, c = cell[0], cell[1]
            if r < 0 or r >= row or c < 0 or c >= col or matrix[r][c] == 1:
                continue

            matrix[r][c] = 1
            q.append((r, c))


#   18.3 compute enclosed region
def fill_surrounded_region(matrix: List[List[int]]):
    rows = len(matrix)
    cols = len(matrix[0])
    q = collections.deque()
    # update all surrounding cell 0s to 2s
    for row in range(rows):
        if row in (0, cols - 1):
            for col in range(cols):
                if matrix[row][col] == 0:
                    q.append((row, col))
                    matrix[row][col] = 2
        else:
            for col in [0, cols - 1]:
                if matrix[row][col] == 0:
                    q.append((row, col))
                    matrix[row][col] = 2
    # bfs over the surrounding cells and mark all reachable 0s to 2s
    while q:
        r, c = q.popleft()
        adjacent_cells = _get_adjacent_cells(r, c)
        for cell in adjacent_cells:
            x, y = cell[0], cell[1]
            if x < 0 or x >= cols or y < 0 or y >= cols:
                continue
            if matrix[x][y] == 0:
                matrix[x][y] = 2
                q.append((x, y))

    # flip all 2s to 0 and rest to 1s
    for r in range(rows):
        for c in range(cols):
            matrix[r][c] = 0 if matrix[r][c] == 2 else 1


#   18.4 deadlock detection
def is_deadlocked(graph: List[GraphVertex]) -> bool:
    def _has_cycle(curr: GraphVertex) -> bool:
        if curr.color == GraphVertex.GRAY:
            # cycle detected
            return True

        curr.color = GraphVertex.GRAY
        for node in curr.edges:
            if node.color != GraphVertex.BLACK:
                result = _has_cycle(node)
                if result:
                    return True

        curr.color = GraphVertex.BLACK
        return False

    for vertex in graph:
        if vertex.color == GraphVertex.WHITE:
            result = _has_cycle(vertex)
            if result:
                return True

    return False


#   18.5 clone a graph
def clone_graph(root: GraphVertex) -> GraphVertex:
    hash_map = {root: GraphVertex(root.val)}
    q = collections.deque()
    q.append(root)

    while q:
        curr = q.popleft()
        curr_clone = hash_map[curr]
        for edge in curr.edges:
            if edge not in hash_map:
                edge_clone = GraphVertex(edge.val)
                hash_map[edge] = edge_clone
                q.append(edge)
            else:
                edge_clone = hash_map[edge]

            curr_clone.edges.append(edge_clone)

    return hash_map[root]


def clone_graph_dfs(root: GraphVertex) -> GraphVertex:
    def _clone_graph(curr: GraphVertex):

        curr_clone = hash_map[curr]
        for edge in curr.edges:
            # all edges of curr should be appended to curr's clone
            if edge in hash_map:
                edge_clone = hash_map[edge]
            else:
                edge_clone = GraphVertex(edge.val)
                hash_map[edge] = edge_clone
                _clone_graph(edge)

            curr_clone.edges.append(edge_clone)

    hash_map = {root: GraphVertex(root.val)}
    _clone_graph(root)
    return hash_map[root]


#   18.7 transform one string to another
def transform_string(dictionary: Set[str], start: str, end: str):
    q = collections.deque()
    q.append((start, 0))
    dictionary.remove(start)

    while q:
        word, d = q.popleft()
        if word == end:
            # return depth
            return d

        for idx in range(len(word)):
            for c in string.ascii_lowercase:
                candidate = word[:idx] + c + word[idx + 1:]
                if candidate in dictionary:
                    dictionary.remove(candidate)
                    q.append((candidate, d + 1))

    return -1


# todo
#   18.6 making wired connections
#   ---- advanced graph algorithms ----
#   18.8 Team Photo Day - 2

def get_dfs_traversal(node: GraphVertex):
    def _dfs(curr: GraphVertex, curr_path: List[int]):
        if not curr.edges:
            path.append('->'.join([str(x) for x in curr_path]))
            return

        for edge in curr.edges:
            curr_path.append(edge.val)
            _dfs(edge, curr_path)
            del curr_path[-1]

    path = []
    _dfs(node, [node.val])
    return path


def _get_adjacent_cells(x, y):
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]
