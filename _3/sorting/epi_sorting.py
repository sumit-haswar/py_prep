from typing import List
import collections

class Event:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __lt__(self, other: 'Event'):
        return self.start < other.start if self.start != other.start else self.end < self.end

    def __str__(self):
        return f"[{self.start}, {self.end}]"


class Endpoint:
    def __init__(self, time: int = None, is_start: bool = None):
        self.time = time
        self.is_start = is_start

    def __str__(self):
        return f"{self.time}, {'start' if self.is_start else 'end'}"

    def __lt__(self, other: 'Endpoint'):
        return self.is_start if self.time == other.time else self.time < other.time


class Student:
    def __init__(self, first_name: str, last_name: str, age: int=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other: 'Student'):
        return self.first_name == other.first_name

    def __lt__(self, other: 'Student'):
        return self.first_name < other.first_name if self.first_name != other.first_name \
            else self.last_name < other.last_name


# 13.1 compute the intersection of two sorted arrays
def intersect_sorted_list(list_a: List[int], list_b: List[int]):
    res = []

    curr_a = 0
    curr_b = 0
    while curr_a < len(list_a) and curr_b < len(list_b):
        a = list_a[curr_a]
        b = list_b[curr_b]
        if a == b:
            if not res or a != res[-1]:
                res.append(a)
            curr_a += 1
            curr_b += 1
        elif a < b:
            curr_a += 1
        else:  # b > a
            curr_b += 1

    return res


# 13.2 merge two sorted arrays, "in-place" in A since len(A) > len(B)
def merge_sorted_list_in_place(list_a: List[int], count_a: int, list_b: List[int], count_b: int) -> List[int]:
    write_idx = count_a + count_b - 1
    idx_a = count_a - 1
    idx_b = count_b - 1
    while idx_a >= 0 and idx_b >= 0:
        curr_a = list_a[idx_a]
        curr_b = list_b[idx_b]

        if curr_a < curr_b:
            list_a[write_idx] = curr_b
            write_idx -= 1
            idx_b -= 1
        elif curr_b == curr_a:
            list_a[write_idx] = curr_b
            write_idx -= 1
            idx_b -= 1
            list_a[write_idx] = curr_a
            write_idx -= 1
            idx_a -= 1
        else:  # curr_a > curr_b
            list_a[write_idx] = curr_a
            write_idx -= 1
            idx_a -= 1

    while idx_b >= 0:
        list_a[write_idx] = list_b[idx_b]
        write_idx -= 1
        idx_b -= 1

    return list_a


# 13.6 render a calendar, wap that takes a set of events and determines the max no. of events
#   that take place concurrently
def max_concurrent_event(events: List[Event]):
    endpoints: List[Endpoint] = []
    for event in events:
        endpoints.append(Endpoint(event.start, True))
        endpoints.append(Endpoint(event.end, False))

    # sort endpoints
    endpoints.sort()
    max_concurrent_events = 0
    curr_concurrent_events = 0
    for endpoint in endpoints:
        if endpoint.is_start:
            curr_concurrent_events += 1
            max_concurrent_events = max(max_concurrent_events, curr_concurrent_events)
        else:
            curr_concurrent_events -= 1

    return max_concurrent_events


# 13.8 compute the union of intervals, takes a set of intervals, returns their union as disjoint intervals
def combine_intervals(events: List[Event]):
    if not events or len(events) == 1:
        return events

    events.sort()

    res = [events[0]]
    idx = 1
    while idx < len(events):
        curr_event = events[idx]
        if _is_intersecting(res[-1], curr_event):
            res[-1].end = max(res[-1].end, curr_event.end)
        else:
            res.append(curr_event)

        idx += 1

    return res



# 13.9 partition and sort an array with many repeated entries, preferably "in-place"
def partition_in_place(arr: List[Student]):
    age_counter = collections.Counter([s.age for s in arr])
    print(age_counter)

    age_offset = {}
    offset = 0
    for age, count in age_counter.items():
        age_offset[age] = offset
        offset += count

    while age_offset:

        from_age = next(iter(age_offset))
        from_idx = age_offset[from_age]

        to_age = arr[from_idx].age
        to_idx = age_offset[arr[from_idx].age]
        #swap
        arr[from_idx], arr[to_idx] = arr[to_idx], arr[from_idx]

        age_counter[to_age] -= 1
        if age_counter[to_age]:
            age_offset[to_age] = to_idx + 1
        else:
            del age_offset[to_age]

    return arr




# 13.3 computing the h-index, find the largest h such that at least h entries >=h
def get_h_index(arr: List[int]):
    arr.sort()

    for idx, elem in enumerate(arr):
        elem_to_right = len(arr) - idx - 1
        if elem > elem_to_right:
            return elem

    return None


# 13.4 remove first name duplicates from list of Students, "in-place"
# this algorithm basically deletes duplicates in-place
def remove_first_name_duplicates(students: List[Student]) -> List[Student]:
    if not students or len(students) == 1:
        return students

    students.sort() # students with same first-name are grouped together

    write_idx = 1
    for candidate in students[1:]:
        if candidate != students[write_idx - 1]:
            students[write_idx] = candidate
            write_idx += 1


    return students[:write_idx]


# 13.7 merging intervals, take a disjoint set of interval pairs and add an input interval to it.
def add_interval(events: List[Event], new_event: Event) -> List[Event]:
    events.sort()
    res = []
    idx = 0
    while idx < len(events):
        event = events[idx]
        if _is_intersecting(event, new_event):  # start merging
            break
        res.append(event)
        idx += 1

    # keep combining will event intersects
    while idx < len(events):
        if _is_intersecting(events[idx], new_event):
            new_event = Event(min(new_event.start, events[idx].start), max(new_event.end, events[idx].end))
            idx += 1
        else:
            break

    res.append(new_event)

    return res + events[idx:]



# todo
#   13.11 implement a fast sorting algo for LINKED lists
def merge_sort_linked_list():
    pass
#   13.10
#   13.5

def _is_intersecting(event_a: Event, event_b: Event):
    if event_a.start > event_b.start:
        event_a, event_b = event_b, event_a

    return (event_a.start <= event_b.start <= event_a.end) or (event_a.start <= event_b.end <= event_a.end)


if __name__ == "__main__":
    # print(merge_sorted_list_in_place([2,3,3,3,7,11, 95, None, None, None, None, None, None, None],7,
    #                                  [0,3,3,7, 90], 5))

    # print(_is_intersecting(Event(0, 2), Event(3, 7)))
    #
    # x = add_interval([Event(-2, -1),
    #                      Event(0, 2),
    #                   Event(3, 4),
    #                   Event(5, 6),
    #                   Event(7,9),
    #                   Event(10,15)],
    #                  Event(3,7))
    x = partition_in_place([Student("greg", "", 14),
                        Student("john", "", 12),
                        Student("andy", "", 11),
                        Student("jim", "", 13),
                        Student("phil", "", 12),
                        Student("bob", "", 13),
                        Student("chip", "", 13),
                        Student("tim", "", 14),
                        ])

    print([str(x) for x in x])
