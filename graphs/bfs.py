from abc import ABC, abstractmethod
from graphs import GraphNode
import collections


class Bfs(ABC):

    @abstractmethod
    def pre_process_node(self, node: GraphNode):
        pass

    @abstractmethod
    def process_edge(self, source: GraphNode, sink: GraphNode):
        pass

    @abstractmethod
    def post_process_node(self, node: GraphNode):
        pass

    def bfs(self, start_node: GraphNode):
        parent_of = {}
        queue = collections.deque()
        queue.append(start_node)
        start_node.state = 'discovered'
        parent_of[start_node.val] = None

        while queue:
            curr = queue.popleft()
            self.pre_process_node(curr)
            curr.state = 'processed'

            for neighbor in curr.edges:
                if neighbor.color != 'processed':  # or graph.is_directed
                    self.process_edge(curr, neighbor)
                if neighbor.color != 'discovered':
                    queue.append(neighbor)
                    neighbor.state = 'discovered'
                    parent_of[neighbor.val] = curr.val

            self.post_process_node(curr)

        return parent_of
