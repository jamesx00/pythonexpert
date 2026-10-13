from collections import Counter


def top_k_frequent(nums, k):
    counts = Counter(nums)
    most_common = counts.most_common(k)
    return [n for n, _ in most_common]
