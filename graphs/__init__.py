from .epi_graphs import *
from .misc_graph import *
from .set_union import SetUnion


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.color = 'white'
        self.state = 'undiscovered'
