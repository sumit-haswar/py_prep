
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.color = 'white'
        self.state = 'undiscovered'

class Node:
    def __init__(self, val):
        self.val = val
        self.edges = {}

    def add_neighbor(self, node_val, weight=0):
        self.edges[node_val] = weight

    def __str__(self):
        return "Val: {}".format(self.val)

class Edge:
    def __init__(self, source, sink, weight):
        self.source = source
        self.sink = sink
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight \
            if self.weight != other.weight else self.sink < other.sink

    def __str__(self):
        return "{} <--{}--> {}".format(self.source, self.weight, self.sink)
