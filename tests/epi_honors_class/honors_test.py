import unittest
from epi_honors_class import *
from linked_list.util import create_list, get_list_from_linked_list


class MyTestCase(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(5, gcd(0, 5))
        self.assertEqual(12, gcd(456, 900))
        self.assertEqual(45, gcd(945, 900))
        self.assertEqual(27, gcd(945, 3456))

    def test_gcd_mod(self):
        self.assertEqual(5, gcd_mod(0, 5))
        self.assertEqual(12, gcd_mod(456, 900))
        self.assertEqual(45, gcd_mod(945, 900))

    def test_rotate_array(self):
        self.assertListEqual([22, 45, 78, 6, 89, 90],
                             rotate_array([6, 89, 90, 22, 45, 78], 3))

        self.assertListEqual([45, 78, 89, 90, 154, 99, 22],
                             rotate_array([89, 90, 154, 99, 22, 45, 78], 2))

    def test_justify_text(self):
        actual = justify_text('the quick brown fox jumped over the lazy dogs', 11)
        expected = [
            'the   quick',
            'brown   fox',
            'jumped over',
            'the    lazy',
            'dogs       '
        ]
        self.assertListEqual(expected, actual)

    def test_zipping_linked_list(self):
        ll = create_list([9, 12, 14, 22, 40, 99, 10])
        zipped_ll = zipping_linked_list(ll)
        zipped_ll_list = get_list_from_linked_list(zipped_ll)
        expected = [9, 10, 12, 99, 14, 40, 22]
        self.assertListEqual(expected, zipped_ll_list)

    def test_queue_with_max(self):
        max_q = QueueWithMax()
        max_q.enqueue(4)
        max_q.enqueue(19)
        max_q.enqueue(12)
        max_q.enqueue(13)
        max_q.enqueue(11)

        self.assertEqual(19, max_q.get_max())
        self.assertEqual(4, max_q.dequeue())
        self.assertEqual(19, max_q.dequeue())
        self.assertEqual(13, max_q.get_max())
        self.assertEqual(12, max_q.dequeue())
        max_q.enqueue(21)
        self.assertEqual(21, max_q.get_max())

    def test_calculate_traffic_volumes(self):
        traffic_volumes = [
            TrafficElement(0, 1.3),
            TrafficElement(2, 2.5),
            TrafficElement(3, 3.7),
            TrafficElement(5, 1.4),
            TrafficElement(6, 2.6),
            TrafficElement(8, 2.2),
            TrafficElement(9, 1.7),
            TrafficElement(14, 1.7)
        ]

        result = calculate_traffic_volumes(traffic_volumes, 3)
        expected = [
            (0, 1.3),
            (2, 2.5),
            (3, 3.7),
            (5, 3.7),
            (6, 3.7),
            (8, 2.6),
            (9, 2.6),
            (14, 1.7)
        ]
        idx = 0
        for traffic_elem in result:
            self.assertEqual(expected[idx][0], traffic_elem.time)
            self.assertEqual(expected[idx][1], traffic_elem.volume)
            idx += 1

    def test_calculate_trapping_water(self):
        heights = [1, 2, 1, 2, 3, 5, 4, 4, 5, 2, 3, 0, 4]
        capacity = calculate_trapping_water(heights)
        self.assertEqual(10, capacity)

        heights = [10, 2, 1, 2, 3, 5, 4, 4, 5, 2, 3, 0, 4]
        capacity = calculate_trapping_water(heights)
        self.assertEqual(21, capacity)

    def test_find_longest_increasing_subarray(self):
        pass

    def test_compute_skyline(self):
        buildings = [
            Building(0, 2, 1),
            Building(1, 4, 2),
            Building(2, 3, 3),
            Building(3, 6, 1),
        ]
        skyline = compute_skyline(buildings)
        print(skyline)

    def test_is_match(self):
        pass


if __name__ == '__main__':
    unittest.main()
