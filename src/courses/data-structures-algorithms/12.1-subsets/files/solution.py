def subsets(nums):
    result = [[]]
    for n in nums:
        result += [subset + [n] for subset in result]
    return result
