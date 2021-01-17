class SetUnion:

    def __init__(self, graph: dict):
        self.parent = {}
        self.size = {}

        for node in graph.keys():
            self.parent[node] = node
            self.size[node] = 1

    def _get_root(self, node_val):
        if self.parent[node_val] == node_val:
            return node_val
        else:
            return self._get_root(self.parent[node_val])

    def union_set(self, node_a, node_b):
        """Perform a Union of node_a's component and node_b's component"""
        if self.same_component(node_a, node_b):
            return

        root_a = self._get_root(node_a)
        root_b = self._get_root(node_b)

        if self.size[root_a] >= self.size[root_b]:
            # since root_a is of bigger size, make root_a parent of root_b
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]
        else:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]

    def same_component(self, node_a, node_b) -> bool:
        """Check if node_a and node_b belong to a same connected component"""
        return self._get_root(node_a) == self._get_root(node_b)
