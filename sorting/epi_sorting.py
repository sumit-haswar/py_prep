from typing import List
import bisect

# boot-camp
class Student():

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        return self.name < other.name


def sort_students_by_gpa(students):
    return sorted(students, key=lambda student: student.gpa, reverse=True)


def sort_students_by_name(students: List[Student]):
    students.sort()


#   13.1 compute intersection of two sorted arrays
def intersect_two_sorted_lists_binary_search(arr1: List[int], arr2: List[int]) -> List[int]:

    def _find(elem: int, arr: List[int]):

        idx = bisect.bisect_left(arr, elem, 0, len(arr))
        if idx != len(arr) and arr[idx] == elem:
            return True
        return False

    if len(arr2) > len(arr1):
        arr1, arr2 = arr2, arr1
    result = []
    # iter through shorter array and b-search in longer
    for idx, val in enumerate(arr2):
        if (idx == 0 or arr2[idx - 1] != arr2[idx]) and _find(val, arr1):
            result.append(val)

    return result


def intersect_two_sorted_lists(arr_a: List[int], arr_b: List[int]) -> List[int]:
    idx_a, idx_b = 0, 0
    result = []
    while idx_a < len(arr_a) and idx_b < len(arr_b):
        if arr_a[idx_a] == arr_b[idx_b]:
            val = arr_a[idx_a]
            result.append(val)

            # move a and b till its value is not val
            while idx_a < len(arr_a) and arr_a[idx_a] == val:
                idx_a += 1

            while idx_b < len(arr_b) and arr_b[idx_b] == val:
                idx_b += 1

        elif arr_a[idx_a] < arr_b[idx_b]:
            idx_a += 1
        else:   # a > b
            idx_b += 1

    return result


#   13.2 merge two sorted arrays
def merge_sorted_arrays(a: List[int], a_count , b: List[int], b_count) -> List[int]:
    write_idx = a_count + b_count - 1
    read_idx_b = b_count - 1
    read_idx_a = a_count - 1

    while read_idx_b >= 0 and read_idx_a >= 0:
        if a[read_idx_a] == b[read_idx_b]:
            a[write_idx] = b[read_idx_b]
            read_idx_b -= 1
        elif a[read_idx_a] < b[read_idx_b]:
            a[write_idx] = b[read_idx_b]
            read_idx_b -= 1
        else: #a[read_idx_a] > b[read_idx_b]:
            a[write_idx] = a[read_idx_a]
            read_idx_a -= 1

        write_idx -= 1

    while read_idx_b >= 0:
        a[write_idx] = b[read_idx_b]
        write_idx -= 1
        read_idx_b -= 1

    return a


#   13.3 computing the h-index
def get_h_index(citations: List[int]) -> int:
    pass

#   13.4 remove first name duplicates

#   13.6 render a calendar

#   13.8 compute the union of intervals

#   13.9 partitioning and sorting an array with many repeated entries

#   13.11 implement a fast sorting algorithm for lists

# todo
#   13.5 smallest non-constructible value
#   13.7 merging intervals
#   13.10 Team Photo Day - 1
