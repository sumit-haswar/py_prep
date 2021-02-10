from typing import List
from util import is_char


def all_subsets(input: str) -> List:
    def _all_subset(input, curr_idx, slate, result):
        if curr_idx >= len(input):
            result.append("".join(slate))
            return

        curr_char = input[curr_idx]
        for i in [curr_char, '']:
            slate.append(i)
            # for duplicate entries in input skip over the duplicates, just taking the current one
            # curr_idx + k, where k is the count of total occurrence of
            _all_subset(input, curr_idx + 1, slate, result)
            del slate[-1]

    result = []
    curr_idx = 0
    slate = []
    _all_subset(input, curr_idx, slate, result)
    return result


# a12b3 --> ["a12b3","a12B3","A12b3","A12B3"]
def letter_case_permutation(input: str) -> List:
    def _letter_case_perm(input, curr_idx, slate):
        if curr_idx >= len(input):
            result.append("".join([str(x) for x in slate]))
            return

        curr_char = input[curr_idx]
        if is_char(curr_char):
            for ch in [curr_char.lower(), curr_char.upper()]:
                slate.append(ch)
                _letter_case_perm(input, curr_idx + 1, slate)
                del slate[-1]
        else:
            slate.append(curr_char)
            _letter_case_perm(input, curr_idx + 1, slate)
            del slate[-1]

    result = []
    slate = []
    _letter_case_perm(input, 0, slate)
    return result


# 2 --> ['00', '01', '10', '11']
# 3 --> ['000', '001', '010', '011', '100', '101', '110', '111']
def binary_strings(digits: int) -> List:
    def _binary_strings(digits, curr_idx, slate):
        if curr_idx == digits:
            result.append("".join(slate))
            return

        for bit in ["0", "1"]:
            slate.append(bit)
            _binary_strings(digits, curr_idx + 1, slate)
            del slate[-1]

    result = []
    slate = []
    _binary_strings(digits, 0, slate)
    return result


if __name__ == "__main__":
    print(all_subsets("123"))
