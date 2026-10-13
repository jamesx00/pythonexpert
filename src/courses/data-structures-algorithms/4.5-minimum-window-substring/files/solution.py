from collections import Counter

def min_window(text, chars):
    if not chars or not text:
        return ""
    need = Counter(chars)
    missing = len(chars)
    left = 0
    best = (float("inf"), 0, 0)
    for right, ch in enumerate(text):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            need[text[left]] += 1
            if need[text[left]] > 0:
                missing += 1
            left += 1
    return "" if best[0] == float("inf") else text[best[1]:best[2]]
