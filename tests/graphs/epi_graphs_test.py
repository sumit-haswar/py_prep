import unittest
from graphs import *


class EpiGraphsTestCase(unittest.TestCase):
    def test_can_team_a_beat_team_b(self):
        matches = [
            ('ger', 'eng'),
            ('ger', 'bra'),
            ('bra', 'arg'),
            ('arg', 'bel'),
            ('fra', 'bra'),
            ('mex', 'ger'),
            ('ita', 'ger'),
            ('ita', 'fra'),
            ('esp', 'ita'),
        ]

        result = can_team_a_beat_team_b('ger', 'bel', matches)
        self.assertTrue(result)

        result = can_team_a_beat_team_b('fra', 'ita', matches)
        self.assertFalse(result)

        result = can_team_a_beat_team_b('mex', 'bel', matches)
        self.assertTrue(result)

    def test_search_maze(self):
        start = Coordinate(4, 0)
        end = Coordinate(0, 4)
        maze = [
            [0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0]
        ]
        path = search_maze(maze, start, end)
        self.assertTrue(len(path) > 0)

        maze2 = [
            [0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0]
        ]

        path2 = search_maze(maze2, start, end)
        self.assertTrue(len(path2) == 0)

    def test_flip_color(self):
        matrix = [
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0]
        ]

        flip_color(matrix, (3, 2))

        expected = [
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]

        for idx, row in enumerate(matrix):
            self.assertListEqual(expected[idx], row)

        flip_color(matrix, (0, 1))

        expected = [
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]

        for idx, row in enumerate(matrix):
            self.assertListEqual(expected[idx], row)

    def test_fill_surrounded_region(self):
        matrix = [
            [1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0]
        ]

        fill_surrounded_region(matrix)

        expected = [
            [1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0]
        ]

        for idx, row in enumerate(matrix):
            self.assertListEqual(expected[idx], row)

    def test_is_deadlocked(self):
        # create graph
        a = GraphVertex()
        b = GraphVertex()
        c = GraphVertex()
        d = GraphVertex()
        e = GraphVertex()
        f = GraphVertex()
        g = GraphVertex()
        x = GraphVertex()
        y = GraphVertex()

        a.edges.append(b)
        b.edges.extend([x, c])
        c.edges.append(d)
        d.edges.extend([e, f, g])
        x.edges.append(y)

        graph = [
            a, b, c, d, e, f, g, x, y
        ]

        self.assertFalse(is_deadlocked(graph))

    def test_is_deadlocked_has_cycle(self):
        # create graph
        a = GraphVertex()
        b = GraphVertex()
        c = GraphVertex()
        d = GraphVertex()
        e = GraphVertex()
        f = GraphVertex()
        g = GraphVertex()
        x = GraphVertex()
        y = GraphVertex()

        a.edges.append(b)
        b.edges.extend([x, c])
        c.edges.append(d)
        d.edges.extend([e, f, g])
        x.edges.append(y)
        e.edges.append(b)

        graph = [
            a, b, c, d, e, f, g, x, y
        ]

        self.assertTrue(is_deadlocked(graph))

    def test_clone_graph(self):
        a = self._create_simple_graph()

        clone = clone_graph(a)

        paths = get_dfs_traversal(a)

        clone_paths = get_dfs_traversal(clone)

        for idx, clone_path in enumerate(clone_paths):
            self.assertEqual(paths[idx], clone_path)

    def test_clone_graph_dfs(self):
        a = self._create_simple_graph()

        clone = clone_graph_dfs(a)

        paths = get_dfs_traversal(a)

        clone_paths = get_dfs_traversal(clone)

        for idx, clone_path in enumerate(clone_paths):
            self.assertEqual(paths[idx], clone_path)

    def test_transform_string(self):
        dictionary = self._get_dictionary()
        path_len = transform_string(dictionary, 'bat', 'dag')
        self.assertEqual(2, path_len)

        dictionary = self._get_dictionary()
        path_len = transform_string(dictionary, 'dot', 'bag')
        self.assertEqual(3, path_len)

    def _create_simple_graph(self):
        a = GraphVertex(1)
        b = GraphVertex(2)
        c = GraphVertex(3)
        d = GraphVertex(4)
        e = GraphVertex(5)
        f = GraphVertex(6)
        g = GraphVertex(7)
        x = GraphVertex(8)
        y = GraphVertex(9)
        l = GraphVertex(10)
        a.edges.append(b)
        a.edges.append(l)
        b.edges.extend([c, x])
        c.edges.append(d)
        d.edges.extend([e, f, g])
        x.edges.append(y)
        # avoid cycles for now
        # e.edges.append(b)
        return a

    def _get_dictionary(self):
        dictionary = set()
        dictionary.add('cat')
        dictionary.add('dog')
        dictionary.add('dat')
        dictionary.add('bat')
        dictionary.add('cot')
        dictionary.add('dot')
        dictionary.add('dag')
        dictionary.add('bag')
        return dictionary


if __name__ == '__main__':
    unittest.main()
