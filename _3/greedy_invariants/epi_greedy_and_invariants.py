from typing import List, Iterable

class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left}-{self.right}"

    def __lt__(self, other: 'Interval'):
        return self.right < other.right

    def is_overlapping(self, other: 'Interval') -> bool:
        event_a = self
        event_b = other
        if event_a.left > event_b.left:
            event_a, event_b = event_b, event_a

        return (event_a.left <= event_b.left <= event_a.right) or (event_a.left <= event_b.right <= event_a.right)

#   boot-camp, make change with min. coins
def make_change(amount: int):
    res = []
    for coin in [100, 50, 25, 10, 5, 1]:
        if amount <= 0:
            break
        curr_coin_count = amount // coin
        amount = amount - curr_coin_count * coin
        res.append(f"{coin} * {curr_coin_count}")

    return res

#   17.1, compute the optimum assignment of two-tasks per 1 worker
def compute_optimum_assignment(tasks: List[int]) -> List[tuple]:
    res = []
    tasks.sort()
    left = 0
    right = len(tasks) - 1
    while left < right:
        res.append((tasks[left], tasks[right]))
        left += 1
        right -= 1

    return res

#   17.2, schedule to minimize task/service execution wait times


#   17.3, the interval covering problem
def interval_covering_problem(intervals: List[Interval]):
    intervals.sort()
    curr = intervals[0]
    res = []
    for interval in intervals:
        if not curr.is_overlapping(interval):
            res.append(curr)
            curr = interval

    res.append(curr)
    return res


#   -------- invariants --------
#   boot-camp, has-two-sum
def has_two_sum(seq: List[int], target: int) -> bool:
    seq.sort()
    left = 0
    right = len(seq) - 1

    while left < right:
        if seq[left] + seq[right] == target:
            return True
        elif seq[left] + seq[right] > target:
            right -= 1
        else:
            left += 1

    return False


#   17.4, the 3-sum problem
def has_three_sum(seq: List[int], target: int) -> bool:
    seq.sort()
    for curr in seq:
        res = has_two_sum(seq, target - curr)
        if res:
            return True

    return False

#   17.5, find the majority element of a stream or list
def find_majority(seq: Iterable[int]) -> int:
    candidate = None
    candidate_count = 0
    for num in seq:
        if candidate_count == 0:
            candidate = num
            candidate_count += 1
        elif num == candidate:
            candidate_count += 1
        else:
            candidate_count -= 1

    return candidate


#   17.7, compute max water trapped by a pair of vertical lines
def compute_trapped_water(seq: List[int]) -> (int, int, int):
    left = 0
    right = len(seq) - 1

    res_left, res_right = None, None
    max_water = float('-inf')

    while left < right:
        curr_water = (right - left) * min(seq[left], seq[right])
        if curr_water > max_water:
            max_water = curr_water
            res_left, res_right = left, right

        # if left is lower in height than right, we shift left hoping to find taller building
        if seq[left] <= seq[right]:
            left += 1
        else: # seq[left] > seq[right]
            right -= 1


    return res_left, res_right, max_water


#todo
#   17.6, the gas-up problem
#   17.8, compute the largest rectangle under the skyline
def compute_largest_rectangle() -> (int, int):
    pass

if __name__ == "__main__":
    res =interval_covering_problem(
        [Interval(1,2),
        Interval(2,3),
        Interval(3,4),
        Interval(2,3),
         Interval(3,4),
         Interval(4,5)]
    )

    print(compute_trapped_water([1,2,1,3,4,4,5,6,2,1,3,1,3,2,1,2,4,1]))
