from typing import List


#   15.3 generate all non-attacking placements of n-queens
def generate_n_queen_placements(n: int) -> List:
    res = []

    def _non_attacking_placement(column_vector: List, column: int, curr_row: int) -> bool:
        # check if setting value: `column` for curr_row cause an attacking placement
        for idx, val in enumerate(column_vector[:curr_row]):
            # new queen will be placed on the same column as an existing one
            if val == column:
                return False
            # new queen will be placed on the same diagonal OR anti-diagonal
            if (idx - val == curr_row - column) or (idx + val == column + curr_row):
                return False

        return True

    def _gen_n_queen(column_vector: List, curr_row: int):
        if curr_row >= n:
            res.append(column_vector.copy())
            return

        for column in range(n):
            if _non_attacking_placement(column_vector, column, curr_row):
                column_vector[curr_row] = column
                _gen_n_queen(column_vector, curr_row + 1)

    column_vector = [0] * n
    _gen_n_queen(column_vector, 0)

    return res


#   15.4 generate permutations
def generate_permutations(seq: List[int]):
    # refer: _3/combinatorial/backtrack.py
    pass


#   15.5 generate the power-set/ all subsets of a list of elements
def generate_power_set(seq: List[int]):
    # refer: _3/combinatorial/backtrack.py
    pass


#   15.2 compute all mnemonics of a phone number
def compute_phone_number_mnemonics(phone_number: List[int]):
    # refer: _3/combinatorial/backtrack.py
    pass


#   15.6 generate all subsets of size k
def generate_all_subsets_of_size_k(seq: List[int], k: int) -> List:
    # refer: _3/combinatorial/backtrack.py
    pass


#   15.9 generate binary trees
def generate_binary_trees(node_count: int):
    pass


#   todo
#       15.1 the tower of hanoi problem
#       15.10 implement a sudoku solver
#       15.11 compute a gray code
#       15.7 generate strings of matched parens
#       15.8 generate palindromic decompositions


if __name__ == "__main__":
    res = generate_n_queen_placements(5)
    print(len(res))
    print(res)
