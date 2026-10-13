import heapq


def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
