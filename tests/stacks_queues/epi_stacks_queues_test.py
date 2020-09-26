import unittest
from stacks_queues import \
    MaxStack, \
    evaluate_rpn_expression, \
    is_string_well_formed, \
    get_sunset_view, \
    get_tree_nodes_by_level, \
    ArrayQueue, \
    StackQueue, \
    MaxQueue

from binary_tree.util import build_1_to_10_bst


class EpiStacksQueuesTestCase(unittest.TestCase):

    def test_max_stack(self):
        max_stack = MaxStack()
        max_stack.push(44)
        max_stack.push(4)
        max_stack.push(60)
        max_stack.push(2)
        max_stack.push(24)
        max_stack.push(500)
        self.assertEqual(500, max_stack.get_max())
        max_stack.pop()  # pop 500
        self.assertEqual(60, max_stack.get_max())
        max_stack.pop()  # pop 24
        self.assertEqual(60, max_stack.get_max())
        max_stack.pop()  # pop 2
        max_stack.pop()  # pop 60
        self.assertEqual(44, max_stack.get_max())

    def test_evaluate_rpn_expression(self):
        result = evaluate_rpn_expression('5 3 2 * +')
        self.assertEqual(11, result)

        result = evaluate_rpn_expression('9 4 / 1 2 + -')
        self.assertEqual(-1, result)

        result = evaluate_rpn_expression('10 6 9 3 + -11 * / * 17 + 5 +')
        self.assertEqual(22, result)

    def test_is_string_well_formed(self):
        self.assertTrue(is_string_well_formed(''))
        self.assertTrue(is_string_well_formed('[]{}(){[()]}'))
        self.assertFalse(is_string_well_formed('[]{}(){[(]}'))

    def test_get_sunset_view(self):
        actual = get_sunset_view(iter([6, 9, 3, 9, 5, 16, 9, 13]))
        self.assertEqual([7, 5], actual)
        actual = get_sunset_view(iter([17, 15, 3, 15, 32, 14, 21, 26, 8, 34,
                                       42, 14, 5, 4, 13, 42, 19, 36, 30, 14,
                                       45, 20, 43, 13]))
        self.assertEqual([23, 22, 20], actual)

    def test_get_tree_nodes_by_level(self):
        tree = build_1_to_10_bst()
        level_list = get_tree_nodes_by_level(tree)
        self.assertListEqual([[5], [3, 9], [2, 4, 7, 10], [1, 6, 8]], level_list)

    def test_stack_queue(self):
        sq = StackQueue()
        for e in [11, 22, 33]:
            sq.enqueue(e)
        self.assertEqual(11, sq.dequeue())
        self.assertEqual(22, sq.dequeue())
        for e in [44, 55, 66]:
            sq.enqueue(e)
        self.assertEqual(33, sq.dequeue())
        self.assertEqual(44, sq.dequeue())
        self.assertEqual(55, sq.dequeue())

    def test_array_queue(self):
        sq = ArrayQueue(8)
        for e in range(1, 6):
            sq.enqueue(e * 11)
        self.assertEqual(5, sq.size())
        for e in range(1, 6):
            self.assertEqual(e * 11, sq.dequeue())

        sq = ArrayQueue(5)
        for e in range(1,10):
            sq.enqueue(e * 11)

        for e in range(1,10):
            self.assertEqual(e * 11, sq.dequeue())

    def test_max_queue(self):
        mq = MaxQueue()
        mq.enqueue(-202)
        self.assertEqual(-202, mq.get_max())
        mq.enqueue(131)
        mq.enqueue(-105)
        self.assertEqual(131, mq.get_max())
        mq.enqueue(265)
        mq.enqueue(-284)
        mq.enqueue(117)
        self.assertEqual(-202, mq.dequeue())
        self.assertEqual(265, mq.get_max())
        mq.enqueue(574)
        self.assertEqual(574, mq.get_max())
        mq.enqueue(947)
        self.assertEqual(131, mq.dequeue())
        self.assertEqual(947, mq.get_max())
        self.assertEqual(-105, mq.dequeue())
        self.assertEqual(265, mq.dequeue())



if __name__ == '__main__':
    unittest.main()
