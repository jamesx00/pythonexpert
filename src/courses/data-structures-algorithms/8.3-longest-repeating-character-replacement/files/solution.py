from collections import Counter

def longest_replacement(s, k):
    counts = Counter()
    left = 0
    max_freq = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ch] += 1
        max_freq = max(max_freq, counts[ch])
        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
