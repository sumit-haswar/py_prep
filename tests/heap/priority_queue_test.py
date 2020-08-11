from heap import PriorityQueue

import unittest


class PriorityQueueTest(unittest.TestCase):

    def test_get_max(self):
        pq = PriorityQueue([12, 3, 4, 5, 67, 99])
        self.assertEqual(99, pq.get_max())

    def test_extract_max(self):
        pq = PriorityQueue([12, 3, 4, 5, 67, 99])
        self.assertEqual(99, pq.extract_max())
        self.assertEqual(67, pq.get_max())

    def test_insert(self):
        pq = PriorityQueue([12, 3, 4, 5, 67, 99])
        self.assertEqual(99, pq.get_max())
        pq.insert(101)
        self.assertEqual(101, pq.get_max())

        pq.insert(97)
        self.assertEqual(101, pq.get_max())


if __name__ == '__main__':
    unittest.main()
