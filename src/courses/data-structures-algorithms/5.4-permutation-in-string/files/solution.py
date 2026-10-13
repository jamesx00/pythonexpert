from collections import Counter

def contains_permutation(pattern, text):
    need = Counter(pattern)
    have = Counter()
    L = len(pattern)
    if L > len(text):
        return False
    for i in range(L):
        have[text[i]] += 1
    if have == need:
        return True
    for i in range(L, len(text)):
        have[text[i]] += 1
        have[text[i - L]] -= 1
        if have[text[i - L]] == 0:
            del have[text[i - L]]
        if have == need:
            return True
    return False
