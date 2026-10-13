def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result
