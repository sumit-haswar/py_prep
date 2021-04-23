from typing import List, Tuple
import bisect
from linked_list.epi_linked_lists import merge_sorted_list
from linked_list import Node


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

    #wlog arr1 is longer than arr2
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
        else:  # a > b
            idx_b += 1

    return result


#   13.2 merge two sorted arrays
def merge_sorted_arrays(a: List[int], a_count,
                        b: List[int], b_count) -> List[int]:
    # write from the right
    write_idx = a_count + b_count - 1

    # read from the right
    read_idx_b = b_count - 1
    read_idx_a = a_count - 1

    while read_idx_b >= 0 and read_idx_a >= 0:
        if a[read_idx_a] == b[read_idx_b]:
            a[write_idx] = b[read_idx_b]
            read_idx_b -= 1
        elif a[read_idx_a] < b[read_idx_b]:
            a[write_idx] = b[read_idx_b]
            read_idx_b -= 1
        else:  # a[read_idx_a] > b[read_idx_b]:
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
    citations.sort()
    for idx, citation in enumerate(citations):
        right = len(citations) - idx
        if citation >= right:
            return len(citations[idx:])

    return 0


#   13.4 remove first name duplicates
class Name():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __eq__(self, other):
        return self.first == other.first

    def __lt__(self, other):
        return (self.last < other.last) \
            if self.first == other.first else self.first < other.first

    def __str__(self):
        return "{} {}".format(self.first, self.last)


def eliminate_duplicates(names: List[Name]):
    names.sort()
    write_idx = 1
    for curr_idx in range(1, len(names)):
        if names[curr_idx] != names[curr_idx - 1]:
            names[write_idx] = names[curr_idx]
            write_idx += 1

    del names[write_idx:]
    return names


class Event():
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish


class EndPoint():
    def __init__(self, val, is_start=True):
        self.val = val
        self.is_start = is_start

    def __lt__(self, other):
        if self.val == other.val:
            return self.is_start
        else:
            return self.val < other.val


#   13.6 render a calendar
def find_max_simultaneous_events(events: List[Event]) -> int:
    # sort all the 2n endpoints
    endpoints = []
    for event in events:
        start = EndPoint(event.start)
        end = EndPoint(event.finish, False)
        endpoints.append(start)
        endpoints.append(end)

    # sort endpoints by val
    endpoints.sort()

    max_events = 0
    curr = 0
    for endpoint in endpoints:
        # increment if EP is start
        if endpoint.is_start:
            curr += 1
            max_events = max(max_events, curr)
        else:   # decrement if EP is end
            curr -= 1

    return max_events


class Interval():
    def __init__(self, left, right, is_left_closed=True, is_right_closed=True):
        self.left = left
        self.right = right
        self.is_left_closed = is_left_closed
        self.is_right_closed = is_right_closed

    def __lt__(self, other):
        return self.left < other.left

    def __str__(self):
        return "{}:{}".format(self.left, self.right)


#   13.7 merging intervals
def add_interval(intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:
    if not intervals:
        return [new_interval]

    result = []
    # find all to the left of interval
    idx = 0
    while idx < len(intervals):
        curr = intervals[idx]
        if (curr.left <= new_interval.left <= curr.right) \
                or (curr.left <= new_interval.right <= curr.right):
            break
        result.append(curr)
        idx += 1

    # combine curr and new_interval
    new_interval = Interval(min(curr.left, new_interval.left),
                            max(curr.right, new_interval.right))
    # keep combining till current is to right of new_interval
    idx += 1
    while idx < len(intervals) and new_interval.right > intervals[idx].left:
        new_interval.right = max(intervals[idx].right, new_interval.right)
        idx += 1

    result.append(new_interval)

    return result + intervals[idx:]


#   13.8 compute the union of intervals
def union_of_intervals(intervals: List[Interval]):
    def _is_intersecting(interval_1, interval_2):
        # wlog assume interval_1 is longer than interval_2
        if abs(interval_1.left - interval_1.right) < abs(interval_2.left - interval_2.right):
            interval_1, interval_2 = interval_2, interval_1

        if (interval_1.left <= interval_2.left <= interval_1.right) \
                or (interval_1.left <= interval_2.right <= interval_1.right):
            return True
        else:
            return False

    if not intervals or len(intervals) == 1:
        return intervals

    # sort the intervals
    intervals.sort()
    result = [intervals[0]]
    for idx in range(1, len(intervals)):
        curr = intervals[idx]
        top = result[-1]

        if _is_intersecting(curr, top):
            # perform union of curr and top
            top.left = min(top.left, curr.left)
            top.right = max(top.right, curr.right)
        else:
            result.append(curr)

    return result


#   13.9 partitioning and sorting an array with many repeated entries
def group_by_age(names: List[Tuple]):
    # create hash-map of age to indices
    age_to_indices = {}
    for idx, name in enumerate(names):
        age = name[1]
        if age in age_to_indices:
            indices = age_to_indices[age]
            indices.add(idx)
        else:
            s = set()
            s.add(idx)
            age_to_indices[age] = s

    for i in range(0, len(names)):
        curr = next(iter(age_to_indices))
        indices = age_to_indices[curr]

        curr_idx = next(iter(indices))
        if i == curr_idx:
            indices.remove(curr_idx)
            if not indices:
                del age_to_indices[curr]
            continue

        indices.remove(curr_idx)

        # we have to move curr_idx to i
        elem_at_i = names[i]
        swap_indices = age_to_indices[elem_at_i[1]]

        # swap the elements at i and curr_idx
        names[i], names[curr_idx] = names[curr_idx], names[i]

        # change i in swap_indices to curr_idx
        swap_indices.remove(i)
        swap_indices.add(curr_idx)

        if not indices:
            del age_to_indices[curr]


class Team():

    def __init__(self, players: List[int]):
        self.players = players


#   13.10 Team Photo Day - 1
def valid_team_placement_exists(team_a: Team, team_b: Team) -> bool:
    team_a.players.sort()
    team_b.players.sort()

    # check in lock-steps
    for idx in range(len(team_a.players)):
        player_a = team_a.players[idx]
        player_b = team_b.players[idx]
        if player_a < player_b:
            return False

    return True


#   13.11 implement a fast sorting algorithm for lists
def stable_sort_linked_list(head: Node):
    if not head or not head.next:
        return head

    slow, fast = head, head
    pre_slow = None
    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next

    if pre_slow:
        pre_slow.next = None

    return merge_sorted_list(stable_sort_linked_list(head),
                             stable_sort_linked_list(slow))

# todo
#   13.5 smallest non-constructible value
