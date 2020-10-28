import unittest
from sorting import Student, \
    sort_students_by_gpa, \
    sort_students_by_name, \
    intersect_two_sorted_lists, \
    intersect_two_sorted_lists_binary_search, \
    get_h_index, \
    merge_sorted_arrays


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
        pass


if __name__ == '__main__':
    unittest.main()
