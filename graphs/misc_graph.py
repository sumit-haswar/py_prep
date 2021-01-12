import collections
from collections import defaultdict


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

class Edge:
    def __init__(self, weight):
        self.weight = weight


class Node:
    def __init__(self, val):
        self.val = val
        self.edges = {}

    def add_neighbor(self, node_val, weight):
        self.edges[node_val] = weight

    def __str__(self):
        return "Val: {}".format(self.val)


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


def create_mst_prims(graph: {}, start_node: Node):
    in_tree = set()

    curr_node = start_node

    distance = {}
    parent = {}
    for key in graph.keys():
        distance[key] = float('inf')

    distance[start_node.val] = 0

    while curr_node.val not in in_tree:
        # mark current node as visited and in tree
        in_tree.add(curr_node.val)

        # iter all the edges of current node and update distances and parent
        for adj_node_val, weight in curr_node.edges.items():

            if distance[adj_node_val] > weight and adj_node_val not in in_tree:
                distance[adj_node_val] = weight
                parent[adj_node_val] = curr_node.val

        # iter all vertices of graph and set curr_node to min of unvisited
        min_dist = float('inf')
        for node_val in graph.keys():
            node = graph[node_val]
            if node.val not in in_tree and min_dist > distance[node.val]:
                min_dist = distance[node.val]
                curr_node = node

    return parent


def create_mst_kruskal():
    pass


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
