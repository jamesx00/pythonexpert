def max_subarray(nums):
    best = nums[0]
    cur = 0  # best sum of a run that ends on the current day
    for n in nums:
        cur = max(n, cur + n)  # extend the run, or start fresh at n
        best = max(best, cur)
    return best
