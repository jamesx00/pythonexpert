def partition(nums, lo, hi):
    pivot = nums[hi]
    store = lo
    for i in range(lo, hi):
        if nums[i] < pivot:
            nums[i], nums[store] = nums[store], nums[i]
            store += 1
    nums[store], nums[hi] = nums[hi], nums[store]
    return store


def quicksort(nums, lo=0, hi=None):
    # Already written for you: sorts nums in place using your partition.
    if hi is None:
        hi = len(nums) - 1
    if lo < hi:
        p = partition(nums, lo, hi)
        quicksort(nums, lo, p - 1)
        quicksort(nums, p + 1, hi)
