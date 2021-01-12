import unittest
from graphs.misc_graph import Node, create_mst_prims


class MiscGraphTestCase(unittest.TestCase):

    def test_create_mst_prims(self):
        # create a sample weighted graph (refer algo design manual pg.196)
        graph = self._create_graph()
        parent_map = create_mst_prims(graph, graph['a'])
        weight_total = self._get_edge_weight_total(graph, parent_map)
        self.assertEqual(23, weight_total)

    def _get_edge_weight_total(self, graph, parent_map):
        weight_total = 0
        for src, sink in parent_map.items():
            src_node = graph[src]
            weight_total += src_node.edges[sink]

        return weight_total

    def _create_graph(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')

        a.add_neighbor('b', 5)
        a.add_neighbor('g', 7)
        a.add_neighbor('f', 12)

        b.add_neighbor('a', 5)
        b.add_neighbor('g', 9)
        b.add_neighbor('c', 7)

        c.add_neighbor('b', 7)
        c.add_neighbor('g', 4)
        c.add_neighbor('d', 5)
        c.add_neighbor('e', 2)

        d.add_neighbor('c', 5)
        d.add_neighbor('e', 2)

        e.add_neighbor('d', 2)
        e.add_neighbor('c', 2)
        e.add_neighbor('g', 3)
        e.add_neighbor('f', 7)

        f.add_neighbor('e', 7)
        f.add_neighbor('g', 4)
        f.add_neighbor('a', 12)

        g.add_neighbor('a', 7)
        g.add_neighbor('b', 9)
        g.add_neighbor('c', 4)
        g.add_neighbor('e', 3)
        g.add_neighbor('f', 4)

        graph = {
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'e': e,
            'f': f,
            'g': g
        }

        return graph


if __name__ == '__main__':
    unittest.main()
