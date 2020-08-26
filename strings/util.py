def find_match(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)

    # iter from text 0 to n - len(pattern)
    for curr in range(0, text_len - pattern_len + 1):
        pivot = 0
        while pivot < pattern_len and pattern[pivot] == text[curr + pivot]:
            pivot += 1
        if pivot == pattern_len:
            return curr

    return -1
