import collections
from collections import defaultdict
from typing import List
from graphs.set_union import SetUnion
from graphs.graph_node import GraphNode, Node, Edge


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


def get_min_score(products_nodes, products_from, products_to):
    # create graph map
    from_idx, to_idx = 0, 0
    graph_map = defaultdict(set)
    while from_idx < len(products_from):
        source = products_from[from_idx]
        sink = products_to[to_idx]

        graph_map[source].add(sink)
        graph_map[sink].add(source)

        from_idx += 1
        to_idx += 1

    tri_cycles = {}

    for node in products_nodes:
        start = [node]
        get_tri_cycle(node, node, 0, start, graph_map, tri_cycles)

    min_trio_product = None
    # iter through trios and get minimum
    for trio, trio_nodes in tri_cycles.items():
        trio_product = 0
        for curr in trio_nodes:
            # get edges of curr
            for edge in graph_map[curr]:
                if edge not in trio_nodes:
                    trio_product += 1

        min_trio_product = trio_product if min_trio_product is None else min(min_trio_product, trio_product)

    return min_trio_product if min_trio_product else -1


def get_tri_cycle(curr_node, source_node, level, seq, graph_map, tri_cycles):
    if level > 3:
        return

    if curr_node == source_node and level == 3:
        curr_seq = set(sorted(seq))
        trio_signature = '-'.join([str(e) for e in curr_seq])
        if trio_signature not in tri_cycles:
            tri_cycles[trio_signature] = curr_seq
        return

    for edge in graph_map[curr_node]:
        seq.append(edge)
        get_tri_cycle(edge, source_node, level + 1, seq, graph_map, tri_cycles)
        del seq[-1]


class Cell:
    def __init__(self, r, c, rows, cols):
        self.r = r
        self.c = c
        self.visited = []
        for _ in range(rows):
            curr_row = []
            for _ in range(cols):
                curr_row.append(False)
            self.visited.append(curr_row)


# A N D
# T D Z
# X Y Q
def _iter_bfs(matrix, origin_cell, word_lookup, result):
    pass

def _dfs(matrix, origin_cell, word_lookup, result):
    pass

def find_words_in_matrix(matrix, word_lookup):
    rows = len(matrix)
    cols = len(matrix[0])

    result = set()

    for r in range(rows):
        for c in range(cols):
            _iter_bfs(matrix, r, c, result)

    print(result)
    return result


def top_sort(graph):
    def _top_sort(node):
        node.color = 'gray'
        for neighbor in node.edges:
            if neighbor.color != 'black':
                _top_sort(neighbor)

        result.append(node.val)
        node.color = 'black'

    result = []
    for val, node in graph.items():
        if node.color == 'white':
            _top_sort(node)

    return result


def find_order(words):
    curr_idx = 0

    graph = {}

    while True:

        if curr_idx == (len(words) - 1):
            break

        curr_word = words[curr_idx]
        next_word = words[curr_idx + 1]

        end_idx = min(len(curr_word), len(next_word))

        for pivot_idx in range(end_idx):

            curr_char = curr_word[pivot_idx]
            next_char = next_word[pivot_idx]

            if curr_char != next_char:

                if curr_char in graph:
                    curr_node = graph[curr_char]
                else:
                    curr_node = GraphNode(curr_char)
                    graph[curr_char] = curr_node

                if next_char in graph:
                    next_node = graph[next_char]
                else:
                    next_node = GraphNode(next_char)
                    graph[next_char] = next_node

                # next-char is before curr-char
                next_node.edges.append(curr_node)
                break

        curr_idx += 1

    return top_sort(graph)


def count_connected_components(graph: List[GraphNode]):
    """Gets count of different connected components in graph
    If the entire graph is connected, will return 1"""
    connected_components = 0
    bfs = Bfs()

    for node in graph:
        if node.state == 'undiscovered':
            bfs.bfs(node)
            connected_components += 1

    return connected_components


# graph is bipartite
def two_color_graph(graph: List[GraphNode]):
    class TwoColorBfs(Bfs):
        def _complement_color(self, color):
            if color == 'white':
                return 'black'
            elif color == 'black':
                return 'white'
            else:
                return 'uncolored'

        def process_edge(self, source: GraphNode, sink: GraphNode):
            if color_map[source.val] == color_map[sink.val]:
                raise Exception('Graph is not bipartite')
            color_map[sink.val] = self._complement_color(source.color)

    color_map = {}
    for node in graph:
        color_map[node.val] = 'uncolored'

    bipartite = True

    two_color_bfs = TwoColorBfs()

    for node in graph:
        if node.state == 'undiscovered':
            color_map[node.val] = 'white'
            two_color_bfs.bfs(node)

    return bipartite


# dfs based algorithms

# finding cycles

# articulation vertices

# topological sorting

# strongly connected components

# -- -- -- -- -- -- weighted graph algorithms -- -- -- -- -- --

def create_mst_prims(graph, start_node: Node):
    # set to determine if a node is in the mst we are constructing
    in_tree = set()

    curr_node = start_node

    # node and distance map
    distance = {}
    for key in graph.keys():
        distance[key] = float('inf')
    distance[start_node.val] = 0

    # parent-of map
    parent = {}

    while curr_node.val not in in_tree:
        # mark current node as visited and in tree
        in_tree.add(curr_node.val)

        # iter all the edges of current node and update distances and parent
        for adj_node_val, weight in curr_node.edges.items():

            if distance[adj_node_val] > weight and adj_node_val not in in_tree:
                distance[adj_node_val] = weight
                parent[adj_node_val] = curr_node.val

        # iter over all vertices of graph and set curr_node to min of unvisited
        min_dist = float('inf')
        for node_val in graph.keys():
            node = graph[node_val]
            if node.val not in in_tree and min_dist > distance[node.val]:
                min_dist = distance[node.val]
                curr_node = node

    return parent


def create_mst_kruskal(graph) -> List[Edge]:
    # create edge list from graph
    edges = []
    edge_set = set()
    for node_val, node in graph.items():
        for sink, weight in node.edges.items():
            edge_key = ''.join(sorted((node_val, sink)))
            if edge_key not in edge_set:
                edge_set.add(edge_key)
                edges.append(Edge(node_val, sink, weight))

    edges.sort()

    set_union = SetUnion(graph)

    result_edges = []

    while edges:
        curr_edge = edges.pop(0)
        if not set_union.same_component(curr_edge.source, curr_edge.sink):
            result_edges.append(Edge(curr_edge.source, curr_edge.sink, curr_edge.weight))
            set_union.union_set(curr_edge.sink, curr_edge.source)

    return result_edges


# dijkstra
def dijkstra(graph, start_node: Node):
    visited = set()

    # create distance map for each node, init start to 0
    distance = {}
    for node_val in graph.keys():
        distance[node_val] = float('inf')
    distance[start_node.val] = 0

    # node - parent lookup
    parent_of = {}

    curr_node = start_node
    while curr_node.val not in visited:

        visited.add(curr_node.val)

        for adj_node, weight in curr_node.edges.items():
            if distance[adj_node] > (distance[curr_node.val] + weight):  ##
                distance[adj_node] = distance[curr_node.val] + weight  ##
                parent_of[adj_node] = curr_node.val  ##

        dist = float('inf')
        # get the min non-visited of all nodes in graph
        for node_val, node in graph.items():
            if node_val not in visited and distance[node_val] < dist:
                dist = distance[node_val]
                curr_node = node

    return distance, parent_of


# floyd warshall (all-pairs shortest path)
def floyd_warshall(graph):
    # convert graph to adj-matrix
    node_val_to_idx = {}
    curr_idx = 0
    for node_val in graph.keys():
        node_val_to_idx[node_val] = curr_idx
        curr_idx += 1

    adj_matrix = []
    for node_val in range(len(graph)):
        curr_row = []
        for node_val in range(len(graph)):
            curr_row.append(float('inf'))
        adj_matrix.append(curr_row)

    for node_val, node in graph.items():
        source_idx = node_val_to_idx[node_val]
        for neighbor, weight in node.edges.items():
            sink_idx = node_val_to_idx[neighbor]
            adj_matrix[source_idx][sink_idx] = weight

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                cost_through_k = adj_matrix[i][k] + adj_matrix[k][j]
                if cost_through_k < adj_matrix[i][j]:
                    adj_matrix[i][j] = cost_through_k

    return adj_matrix, node_val_to_idx


# todo netflow and bipartite matching
# todo bellman ford

# 3 3 3 3 3 1
# 3 4 4 4 3 4
# 2 4 3 3 3 4
# 2 4 4 4 4 4
input = [[3, 3, 3, 3, 3, 1],
         [3, 4, 4, 4, 3, 4],
         [2, 4, 3, 3, 3, 4],
         [2, 4, 4, 4, 4, 4]]

if __name__ == '__main__':
    matrix = [
        ['a', 'n', 'g'],
        ['t', 'd', 'a'],
        ['l', 'a', 'r'],
    ]
    lookup = set()
    lookup.add('and')
    lookup.add('a')
    lookup.add('ant')
    lookup.add('atlas')
    lookup.add('anger')
    lookup.add('at')
    lookup.add('ragna')
    find_words_in_matrix(matrix, lookup)

