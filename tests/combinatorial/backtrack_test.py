import unittest
from combinatorial import Subsets, Permutation, AllPaths
# from graphs.graph_node import Node
from graphs import GraphNode, Node


class BacktrackTestCase(unittest.TestCase):
    def test_subset(self):
        subset = Subsets()
        n = 3
        k = 0
        a = [False] * (n + 1)

        subset.backtrack(a, k, n)

        expected = ['1,2,3', '1,2', '1,3', '1', '2,3', '2', '3', '']
        self.assertListEqual(sorted(expected), sorted(subset.result))

    def test_permutation(self):
        permutation = Permutation()
        n = 3
        k = 0
        a = [0] * (n + 1)

        permutation.backtrack(a, k, n)

        expected = ['1,2,3', '1,3,2', '2,3,1', '2,1,3', '3,2,1', '3,1,2']
        self.assertListEqual(sorted(expected), sorted(permutation.result))

    def test_all_paths(self):
        graph = self._create_graph()

        a = [0] * (len(graph.keys()) + 1)

        all_paths = AllPaths(graph)

        input_data = {
            'source': 1,
            'dest': 3
        }

        all_paths.backtrack(a, 0, input_data)

        expected = ['1,2,6,3', '1,2,6,4,3','1,3',
                    '1,4,3','1,4,6,3','1,5,6,3','1,5,6,4,3']

        self.assertListEqual(sorted(expected), sorted(all_paths.result))

    def _create_graph(self):
        _1 = Node(1)
        _2 = Node(2)
        _3 = Node(3)
        _4 = Node(4)
        _5 = Node(5)
        _6 = Node(6)

        _1.add_neighbor(2)
        _1.add_neighbor(3)
        _1.add_neighbor(4)
        _1.add_neighbor(5)

        _2.add_neighbor(1)
        _2.add_neighbor(6)

        _3.add_neighbor(1)
        _3.add_neighbor(6)
        _3.add_neighbor(4)

        _4.add_neighbor(1)
        _4.add_neighbor(3)
        _4.add_neighbor(6)

        _5.add_neighbor(1)
        _5.add_neighbor(6)

        _6.add_neighbor(2)
        _6.add_neighbor(3)
        _6.add_neighbor(4)
        _6.add_neighbor(5)

        return {
            1: _1,
            2: _2,
            3: _3,
            4: _4,
            5: _5,
            6: _6
        }


if __name__ == '__main__':
    unittest.main()
