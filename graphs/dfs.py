from abc import ABC, abstractmethod
from graphs import GraphNode


class Dfs(ABC):

    def __init__(self):
        self.time = 0
        self.entry_time = {}
        self.exit_time = {}

    @abstractmethod
    def pre_process_node(self, node: GraphNode):
        pass

    @abstractmethod
    def post_process_node(self, node: GraphNode):
        pass

    # todo
    def dfs(self, node: GraphNode):
        node.state = 'discovered'
        self.time += 1
        self.entry_time[node.val] = self.time

        self.pre_process_node(node)

        # for neighbor in node.edges:
        #     # if neighbor hasn't been discovered yet
        #     if node.state != 'discovered'

        self.post_process_node(node)
        self.time += 1
        self.exit_time[node.val] = self.time

        node.state = 'processed'
