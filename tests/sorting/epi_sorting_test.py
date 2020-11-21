import unittest
from sorting import *
from linked_list import Node


class EpiSortingTestCase(unittest.TestCase):

    def test_sort_students_by_gpa(self):
        students = [
            Student('Jim', 3.0),
            Student('Park', 3.9),
            Student('Sara', 3.8),
            Student('Pablo', 4.0),
        ]
        students = sort_students_by_gpa(students)
        self.assertListEqual(['Pablo', 'Park', 'Sara', 'Jim'], [s.name for s in students])

    def test_sort_students_by_name(self):
        students = [
            Student('Jim', 3.0),
            Student('Park', 3.9),
            Student('Sara', 3.8),
            Student('Pablo', 4.0),
            Student('Andy', 4.0),
        ]
        sort_students_by_name(students)
        self.assertListEqual(['Andy', 'Jim', 'Pablo', 'Park', 'Sara'], [s.name for s in students])

    def test_intersect_two_sorted_lists_binary_search(self):
        result = intersect_two_sorted_lists_binary_search([2, 3, 3, 5, 5, 6, 7, 7, 8, 12],
                                                          [5, 5, 6, 8, 8, 9, 10, 10])
        self.assertListEqual([5, 6, 8], result)

        result = intersect_two_sorted_lists_binary_search([-9, -5, -1, 2, 3, 3, 5, 7, 8, 10],
                                                          [-15, -13, -8, -8, -6, -1, 0, 2, 2,
                                                           8, 11, 13, 13, 14, 15])
        self.assertListEqual([-1, 2, 8], result)

    def test_intersect_two_sorted_lists(self):
        result = intersect_two_sorted_lists([2, 3, 3, 5, 5, 6, 7, 7, 8, 12],
                                            [5, 5, 6, 8, 8, 9, 10, 10])
        self.assertListEqual([5, 6, 8], result)

        result = intersect_two_sorted_lists([-9, -5, -1, 2, 3, 3, 5, 7, 8, 10],
                                            [-15, -13, -8, -8, -6, -1, 0, 2, 2,
                                             8, 11, 13, 13, 14, 15])
        self.assertListEqual([-1, 2, 8], result)

    def test_merge_sorted_arrays(self):
        result = merge_sorted_arrays([-1, 0, 0, 0, 0],
                                     1,
                                     [-3, -1, 0, 3],
                                     4)
        self.assertListEqual([-3, -1, -1, 0, 3], result)

        result = merge_sorted_arrays([-10, -9, -8, -6, -6, 1, 2, 9, 10, 10, 0], 10, [-1], 1)
        self.assertListEqual([-10, -9, -8, -6, -6, -1, 1, 2, 9, 10, 10], result)

        result = merge_sorted_arrays([-17, -16, -13, -12, -4, -4, -1, 4, 5, 5, 7, 7, 8, 12, 14, 16, 17, 18,
                                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     18,
                                     [-17, -14, -13, -12, -8, -7, -4, -4, -4, -1, 0, 0, 4, 5, 10, 11, 11],
                                     17)
        expected = [-17, -17, -16, -14, -13, -13, -12, -12, -8, -7, -4, -4, -4, -4, -4, -1, -1, 0, 0, 4, 4, 5, 5, 5,
                    7, 7, 8, 10, 11, 11, 12, 14, 16, 17, 18]
        self.assertListEqual(expected, result)

    def test_get_h_index(self):
        citations = [1, 20, 20, 17, 16, 2, 12, 13, 17, 23, 9, 23, 9, 19]
        h_index = get_h_index(citations)
        self.assertEqual(10, h_index)

        h_index = get_h_index([3, 44, 38, 23, 37, 43, 28, 21,
                               12, 44, 0, 37, 13, 23, 28, 2,
                               41, 26, 35, 1, 42, 28, 10])

        self.assertEqual(16, h_index)

        self.assertEqual(10,
                         get_h_index([0, 21, 14, 15, 16,
                                      19, 6, 13, 20, 13,
                                      24, 15, 7]))

        self.assertEqual(18,
                         get_h_index([47, 20, 42, 8, 7, 18,
                                      36, 34, 50, 30, 50, 8,
                                      8, 3, 22, 42, 34, 42,
                                      31, 15, 33, 36, 27, 10,
                                      5, 40]))

    def test_remove_first_name_duplicates(self):
        names = [
            Name('Ian', 'Bothom'),
            Name('David', 'Bell'),
            Name('Ian', 'Carter'),
            Name('Jimmy', 'Page'),
            Name('David', 'Bowie')
        ]

        names = eliminate_duplicates(names)

        self.assertListEqual(['Bell', 'Bothom', 'Page'], [name.last for name in names])

    def test_find_max_simultaneous_events(self):
        events = [
            Event(0, 1),
            Event(0, 2),
            Event(2, 4),
            Event(3, 6),
            Event(4, 6),
            Event(6, 8),
            Event(7, 9),
            Event(11, 12),
            Event(14, 17)
        ]
        self.assertEqual(3, find_max_simultaneous_events(events))

        events.append(Event(3, 6))
        self.assertEqual(4, find_max_simultaneous_events(events))

    def test_add_interval(self):
        intervals = [
            Interval(-4, -1),
            Interval(0, 2),
            Interval(3, 6),
            Interval(7, 9),
            Interval(11, 12),
            Interval(14, 17)
        ]
        intervals = add_interval(intervals, Interval(1, 8))
        expected = [[-4, -1], [0, 9], [11, 12], [14, 17]]

        intervals = [[interval.left, interval.right]
                     for interval in intervals]

        self.assertListEqual(expected, intervals)

        intervals = [[6, 14], [18, 18], [22, 30], [32, 42], [51, 57], [59, 62], [66, 73], [78, 79], [84, 86], [92, 100],
                     [108, 118], [119, 120], [123, 126], [130, 136], [139, 144], [152, 154], [160, 169], [173, 177],
                     [182, 187], [191, 200], [205, 210], [217, 220], [230, 239], [249, 259], [260, 265], [266, 270],
                     [273, 279], [281, 291], [292, 302], [312, 319], [320, 329], [336, 341], [346, 347], [353, 357],
                     [362, 369], [371, 378], [382, 388], [392, 395], [403, 412], [420, 427], [432, 440], [445, 447],
                     [452, 458], [460, 468], [476, 486], [487, 491], [492, 501], [511, 518], [526, 526], [532, 537],
                     [538, 546]]
        intervals = [Interval(i[0], i[1]) for i in intervals]
        intervals = add_interval(intervals, Interval(263, 280))
        intervals = [[interval.left, interval.right]
                     for interval in intervals]
        expected = [[6, 14], [18, 18], [22, 30], [32, 42], [51, 57], [59, 62], [66, 73], [78, 79], [84, 86], [92, 100],
                    [108, 118], [119, 120], [123, 126], [130, 136], [139, 144], [152, 154], [160, 169], [173, 177],
                    [182, 187], [191, 200], [205, 210], [217, 220], [230, 239], [249, 259], [260, 280], [281, 291],
                    [292, 302], [312, 319], [320, 329], [336, 341], [346, 347], [353, 357], [362, 369], [371, 378],
                    [382, 388], [392, 395], [403, 412], [420, 427], [432, 440], [445, 447], [452, 458], [460, 468],
                    [476, 486], [487, 491], [492, 501], [511, 518], [526, 526], [532, 537], [538, 546]]
        self.assertListEqual(expected, intervals)

    def test_union_of_intervals(self):
        intervals = [[8, True, 9, False], [157, False, 166, False], [163, False, 168, True], [177, True, 182, True],
                     [30, True, 32, False], [169, False, 170, True], [149, True, 153, False], [121, False, 129, False],
                     [226, False, 228, False], [211, False, 217, True], [177, True, 184, False], [8, False, 17, True],
                     [225, True, 233, True], [16, True, 18, False], [243, False, 246, False], [102, True, 110, True],
                     [170, True, 173, True], [169, True, 175, True], [169, False, 170, True], [105, True, 108, False],
                     [125, False, 128, False], [61, True, 67, False], [175, False, 180, False], [205, True, 210, False],
                     [125, False, 128, False]]

        intervals = [Interval(interval[0], interval[2], interval[1], interval[3])
                     for interval in intervals]

        union = union_of_intervals(intervals)

        expected = [[8, True, 18, False], [30, True, 32, False], [61, True, 67, False], [102, True, 110, True],
                    [121, False, 129, False], [149, True, 153, False], [157, False, 168, True], [169, True, 184, False],
                    [205, True, 210, False], [211, False, 217, True], [225, True, 233, True], [243, False, 246, False]]

        for idx, interval in enumerate(union):
            # curr = [interval.left,
            #         interval.is_left_closed,
            #         interval.right,
            #         interval.is_right_closed]
            curr = [interval.left,
                    interval.right]
            self.assertListEqual([expected[idx][0], expected[idx][2]], curr)
        # -- -- -- -- -- -- -- --
        intervals = [[10, 11], [0, 3], [5, 7], [12, 14], [1, 1], [2, 4], [3, 4], [7, 8], [8, 11]]

        intervals = [Interval(interval[0], interval[1])
                     for interval in intervals]

        union = union_of_intervals(intervals)

        expected = [[0, 4], [5, 11], [12, 14]]

        for idx, interval in enumerate(union):
            # curr = [interval.left,
            #         interval.is_left_closed,
            #         interval.right,
            #         interval.is_right_closed]
            curr = [interval.left,
                    interval.right]
            self.assertListEqual([expected[idx][0], expected[idx][1]], curr)

    def test_valid_team_placement_exists(self):
        team_a = Team([180, 124, 150, 155, 130])
        team_b = Team([180, 124, 150, 155, 130])

        self.assertTrue(valid_team_placement_exists(team_a, team_b))

        team_b = Team([181, 124, 150, 155, 130])
        self.assertFalse(valid_team_placement_exists(team_a, team_b))

    def test_stable_sort_linked_list(self):
        head = Node(14)
        curr = head
        for i in [3, 67, 12, 13, 66, 8]:
            node = Node(i)
            curr.next = node
            curr = node

        ll = stable_sort_linked_list(head)

        actual = []
        while ll:
            actual.append(ll.val)
            ll = ll.next

        self.assertIsNotNone([3, 8, 12, 13, 14, 66, 67], actual)

    def test_group_by_age(self):
        names = [
            ('Greg', 14),
            ('John', 12),
            ('Andy', 11),
            ('Jim', 13),
            ('Phil', 12),
            ('Bob', 13),
            ('Chip', 13),
            ('Tim', 14)
        ]

        group_by_age(names)

        expected = [
            ('Greg', 14),
            ('Tim', 14),
            ('Phil', 12),
            ('John', 12),
            ('Andy', 11),
            ('Bob', 13),
            ('Chip', 13),
            ('Jim', 13)
        ]

        self.assertListEqual(expected, names)

if __name__ == '__main__':
    unittest.main()
