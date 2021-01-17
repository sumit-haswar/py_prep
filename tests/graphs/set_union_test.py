import unittest
from graphs import SetUnion
from graphs.misc_graph import Node


class SetUnionTestCase(unittest.TestCase):
    def test_same_component(self):
        graph = self._create_graph()

        set_union = SetUnion(graph)
        self.assertFalse(set_union.same_component('a', 'b'))
        self.assertTrue(set_union.same_component('a', 'a'))

        set_union.union_set('a', 'b')

        self.assertTrue(set_union.same_component('a', 'b'))

    def test_union_set(self):
        graph = self._create_graph()
        set_union = SetUnion(graph)

        set_union.union_set('c', 'e')
        set_union.union_set('e', 'd')
        set_union.union_set('g', 'e')
        set_union.union_set('c', 'g')

        self.assertTrue(set_union.same_component('c', 'e'))
        self.assertTrue(set_union.same_component('e', 'd'))
        self.assertTrue(set_union.same_component('g', 'e'))

    def _create_graph(self):
        return {
            'a': Node('a'),
            'b': Node('b'),
            'c': Node('c'),
            'd': Node('d'),
            'e': Node('e'),
            'f': Node('f'),
            'g': Node('g')
        }


if __name__ == '__main__':
    unittest.main()
