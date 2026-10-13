from functools import lru_cache


def count_target_sums(nums, target):
    n = len(nums)

    @lru_cache(maxsize=None)
    def dp(i, total):
        if i == n:
            return 1 if total == target else 0
        return dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])

    result = dp(0, 0)
    dp.cache_clear()
    return result
