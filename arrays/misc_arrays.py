import collections


def minWindow(s: str, t: str) -> str:

    def _get_best_result(left, right, text, best):
        if best is None:
            return text[left:right + 1]
        curr = text[left:right + 1]
        best = curr if len(curr) < len(best) else best
        return best

    # Input: s = "ADOBECODEBANC", t = "ABC"
    # Output: "BANC"
    counter = collections.Counter(t)
    cover_count = 0
    left = 0
    right = 0
    best_result = None

    while right < len(s):
        curr = s[right]
        if curr in counter:
            counter[curr] -= 1
            if counter[curr] == 0:
                cover_count += 1

            if cover_count == len(t):
                # we have covered the string, now increment left
                while left < len(s):
                    curr_left = s[left]
                    if curr_left not in counter:
                        left += 1
                        continue
                    # curr_left is in counter, check if we have to exit or continue
                    counter[curr_left] += 1
                    if counter[curr_left] == 1:
                        # removing cover_left will break the cover
                        best_result = _get_best_result(left, right, s, best_result)
                        left += 1
                        cover_count -= 1
                        break
                    left += 1

        right += 1

    return best_result


def get_max_rectangle_area_origin(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    min_length = cols
    max_area = None

    for curr_row in range(0, rows):
        curr_length = 0

        if matrix[curr_row][0] == 0:
            break
        curr_col = 0
        while curr_col < min_length:
            curr_cell = matrix[curr_row][curr_col]
            if curr_cell == 1:
                curr_length += 1
            else:
                break
            curr_col += 1

        curr_area = (curr_row + 1) * curr_length
        min_length = curr_col
        if max_area is None:
            max_area = curr_area
        elif curr_area > max_area:
            max_area = curr_area

    return max_area


if __name__ == "__main__":
    min_cover = minWindow('ADOBECODEBANC', 'ABC')
    print(min_cover)
