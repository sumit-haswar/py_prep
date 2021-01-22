from typing import List
from abc import ABC, abstractmethod


class Backtrack(ABC):

    def __init__(self):
        self.finished = False
        self.result = []

    @abstractmethod
    def is_a_solution(self, a, k, input_data):
        pass

    @abstractmethod
    def construct_candidates(self, a, k, input_data, candidates):
        pass

    @abstractmethod
    def process_solution(self, a, k, input_data):
        pass

    def backtrack(self, a: List[int], k: int, input_data):
        # candidates for next position
        # a new candidates array is allocated with each recursive procedure call
        # the subsets of not yet considered extension candidates at each position will
        # not interfere with each other
        candidates = []

        if self.is_a_solution(a, k, input_data):
            self.process_solution(a, k, input_data)
        else:
            k += 1

            # next position candidate count
            # fills candidates with complete set of possible candidates for the kth position of `a`
            # given the contents of first k-1 positions.
            number_of_candidates = self.construct_candidates(a, k, input_data, candidates)

            for i in range(number_of_candidates):
                # a[k - 1] = candidates[i]
                a[k] = candidates[i]
                # make_move
                self.backtrack(a, k, input_data)
                # unmake_move
                if self.finished:  # premature termination if required
                    return


class Subsets(Backtrack):

    def is_a_solution(self, a, k, input_data):
        return k == input_data

    def construct_candidates(self, a, k, input_data, candidates):
        """This method constructs candidates CELL based on Sk
        True | False implies if an element in n IS IN or NOT in"""
        candidates.append(True)
        candidates.append(False)
        return 2

    def process_solution(self, a, k, input_data):
        solution = []
        for idx in range(1, k + 1):
            if a[idx]:
                solution.append(idx)

        self.result.append(','.join(str(x) for x in solution))


class Permutation(Backtrack):

    def is_a_solution(self, a, k, input_data):
        return k == input_data

    def process_solution(self, a, k, input_data):
        solution = []
        for idx in range(1, k + 1):
            solution.append(a[idx])

        self.result.append(','.join(str(x) for x in solution))

    def construct_candidates(self, a, k, input_data, candidates):
        in_perm = set()

        # for 1 to k get all numbers which are in permutation
        for i in range(1, k):
            in_perm.add(a[i])

        # iter all from 1 to N, adding numbers which are NOT in in_perm
        for i in range(1, input_data + 1):
            if i not in in_perm:
                candidates.append(i)

        return len(candidates)
