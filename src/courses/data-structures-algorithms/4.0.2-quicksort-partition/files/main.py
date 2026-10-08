def partition(nums, lo, hi):
    return lo


def quicksort(nums, lo=0, hi=None):
    # Already written for you: sorts nums in place using your partition.
    if hi is None:
        hi = len(nums) - 1
    if lo < hi:
        p = partition(nums, lo, hi)
        quicksort(nums, lo, p - 1)
        quicksort(nums, p + 1, hi)
