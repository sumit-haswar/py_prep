from typing import List
import math
import collections

# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    result = []
    buffer = []
    buffer_word_count = 0
    # for idx in range(len(words) - 1):
    idx = 0
    while idx < len(words):
        this_word_count = len(words[idx])

        if len(buffer) + len(words[idx]) <= maxWidth:  # 0 + 4
            buffer.extend((' ' if buffer else '') + words[idx])
            buffer_word_count += 1
            idx += 1
        else:   #this word will overflow!
            line = _format_line(buffer, buffer_word_count, maxWidth)
            result.append(line)
            buffer = []
            buffer_word_count = 0


    return result
    # arrange buffer as per left justification

def _left_divide_total(total, count):
    recur_total = 0
    groups = []
    ceil = math.ceil(total / count)
    while recur_total + ceil < total:
        groups.append(ceil)
        recur_total += ceil

    if recur_total < total:
        groups.append(total - recur_total)

    return groups

def _format_line(buffer, word_count, max_width):

    if len(buffer) == max_width:
        return ''.join(buffer)

    right_pad = max_width - len(buffer)
    ws_count = word_count - 1

    total_space = right_pad + ws_count

    group_idx = 0
    ws_groups = _left_divide_total(total_space, ws_count)

    write_stream = []
    read_idx = 0
    while len(write_stream) <= max_width and read_idx < len(buffer):
        if buffer[read_idx] == ' ':
            for i in range(ws_groups[group_idx]):
                write_stream.append(' ')
            read_idx += 1
        else:
            write_stream.append(buffer[read_idx])
            read_idx += 1

    return ''.join(write_stream)

def minWindow(s: str, t: str) -> str:
    # Input: s = "ADOBECODEBANC", t = "ABC"
    # Output: "BANC"
    counter = collections.Counter(t)
    count = len(t)
    curr_count = 0
    left = 0
    right = 0
    best_result = None

    while right < len(s):
        if curr_count == count:
            # left -> right contains t, so keep incrementing left
            result = s[left: right]
            while left < len(s):
                curr = s[left]
                if curr not in counter:
                    left += 1
                    result = s[left: right]
                else:
                    counter[curr] += 1
                    if counter[curr] == 1:
                        curr_count -= 1
                        break
                    else:
                        left += 1
                        result = s[left: right]
            if best_result:
                best_result = result if len(result) < len(best_result) else best_result
            else:
                best_result = result

        # keep incrementing right
        if s[right] in counter:
            if counter[s[right]] == 1:
                curr_count += 1
            counter[s[right]] -= 1

        right += 1


if __name__ == '__main__':
    # line = fullJustify(None, ["This", "is", "an", "example", "of", "text", "justification."], 16)
    result = minWindow(s = "ADOBECODEBANC", t = "ABC")

    print(result)