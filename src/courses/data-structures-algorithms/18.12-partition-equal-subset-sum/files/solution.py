def can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = {0}
    for n in nums:
        dp |= {n + x for x in dp if n + x <= target}
    return target in dp
