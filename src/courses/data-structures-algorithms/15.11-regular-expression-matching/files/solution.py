from functools import lru_cache


def is_match(s, p):
    n, m = len(s), len(p)

    @lru_cache(maxsize=None)
    def dp(i, j):
        if j == m:
            return i == n
        first = i < n and (p[j] == s[i] or p[j] == '.')
        if j + 1 < m and p[j + 1] == '*':
            return dp(i, j + 2) or (first and dp(i + 1, j))
        return first and dp(i + 1, j + 1)

    result = dp(0, 0)
    dp.cache_clear()
    return result
