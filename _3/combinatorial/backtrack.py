from abc import ABC, abstractmethod
from typing import List


class Backtrack(ABC):
    @abstractmethod
    def is_solution(self, a: List, k: int) -> bool:
        pass

    @abstractmethod
    def process_solution(self, a: List, res: List):
        pass

    @abstractmethod
    def construct_candidates(self, a: List, k: int, seq: List) -> List:
        pass

    def backtrack(self, a: List, k: int, res: List, seq: List):
        if self.is_solution(a, k):
            self.process_solution(a, res)
            return

        k = k + 1
        candidates = self.construct_candidates(a, k, seq)
        for candidate in candidates:
            a[k] = candidate
            self.backtrack(a, k, res, seq)


class Subset(Backtrack):
    pass


class Permutation(Backtrack):

    def is_solution(self, a: List, k: int) -> bool:
        return k == (len(a) - 1)

    def process_solution(self, a: List, res: List):
        res.append(a.copy())

    def construct_candidates(self, a: List, k: int, seq: List) -> List:
        candidates = []
        exclude_set = set()
        for idx in range(k):
            exclude_set.add(a[idx])

        for elem in seq:
            if elem not in exclude_set:
                candidates.append(elem)

        return candidates


def backtrack(a: List, k: int, res: List, seq: List):
    if k == (len(a) - 1):
        # end of dfs, print solution
        curr_res = []
        for idx, val in enumerate(a):
            if val:
                curr_res.append(seq[idx])

        if not curr_res:
            res.append(None)
        else:
            res.append("{" + ",".join([str(x) for x in curr_res]) + "}")

        return

    k = k + 1
    candidates = [True, False]
    for candidate in candidates:
        a[k] = candidate
        backtrack(a, k, res, seq)

def phone_number_mnemonics(phone_number: List[int]):
    look_up = {
        2: ["A", "B", "C"],
        3: ["D", "E", "F"],
        4: ["G", "H", "I"]
    }

    res = []

    def backtrack(a: List, k: int):
        if k == (len(phone_number) - 1):
            res.append(a.copy())
            return

        k = k + 1
        candidates = look_up[phone_number[k]]
        for candidate in candidates:
            a[k] = candidate
            backtrack(a, k)

    a = [None for _ in phone_number]
    backtrack(a, -1)
    return res

def compute_subsets(seq: List[int]):
    a = [False for _ in seq]    # backtrack vector

    res = []
    backtrack(a, -1, res, seq)
    print(len(res))
    print(res)


if __name__ == "__main__":
    # phone_number = PhoneNumberMnemonics()
    # res = []
    # phone_number.backtrack([None, None], -1, res, [23])

    res = phone_number_mnemonics([2,3, 4])
    # res = generate_all_subsets_of_size_k([1,2,3,4,5], 2)

    print(len(res))
    print(res)