from abc import ABC, abstractmethod
from .graph_node import GraphNode


class Dfs(ABC):

    def __init__(self):
        self.time = 0
        self.entry_time = {}
        self.exit_time = {}
        self.terminate = False
        self.parent_of = {}

    # @abstractmethod
    def pre_process_node(self, node: GraphNode):
        print('pre process node: {}'.format(node.val))

    # @abstractmethod
    def post_process_node(self, node: GraphNode):
        print('post process node: {}'.format(node.val))

    @abstractmethod
    def process_edge(self, parent: GraphNode, child: GraphNode):
        print('process edge: {} --> {}'.format(parent.val, child.val))

    def dfs(self, node: GraphNode):
        if self.terminate:
            raise Exception("traversal terminated")

        node.discovered = True
        self.time += 1
        self.entry_time[node.val] = self.time

        self.pre_process_node(node)

        for neighbor in node.edges:
            if neighbor.discovered is False:
                self.parent_of[neighbor.val] = node.val
                self.process_edge(node, neighbor)
                self.dfs(neighbor)
            elif neighbor.processed is False and self.parent_of[node.val] != neighbor.val:
                self.process_edge(node, neighbor)

        self.post_process_node(node)

        node.processed = True
        self.exit_time[node.val] = self.time
        self.time += 1


class FindingCycles(Dfs):

    def __init__(self, node_list):
        super().__init__()
        for node in node_list:
            self.parent_of[node] = -1


    def process_edge(self, parent: GraphNode, child: GraphNode):
        print('process edge: {} --> {}'.format(parent.val, child.val))
        if child.discovered and self.parent_of[parent.val] != child.val:
            print("!!!! cycle detected !!!!")


if __name__ == "__main__":
    # create a cyclic graph
    one = GraphNode(1)
    two = GraphNode(2)
    three = GraphNode(3)
    six = GraphNode(6)

    one.edges.append(two)
    one.edges.append(six)
    one.edges.append(three)

    two.edges.append(one)
    two.edges.append(three)

    three.edges.append(one)
    three.edges.append(two)

    six.edges.append(one)

    finding_cycles = FindingCycles([1,2,3,6])
    finding_cycles.dfs(one)
    print('dfs complete')
