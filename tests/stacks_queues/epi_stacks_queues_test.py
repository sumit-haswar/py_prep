import unittest
from stacks_queues import \
    MaxStack, \
    evaluate_rpn_expression, \
    is_string_well_formed


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
        s = ''
        actual = is_string_well_formed(s)


if __name__ == '__main__':
    unittest.main()
