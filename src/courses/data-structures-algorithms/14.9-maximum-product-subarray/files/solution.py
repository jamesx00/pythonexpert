def max_product_subarray(nums):
    res = nums[0]
    cur_max = cur_min = nums[0]
    for n in nums[1:]:
        candidates = (n, cur_max * n, cur_min * n)
        cur_max = max(candidates)
        cur_min = min(candidates)
        res = max(res, cur_max)
    return res
