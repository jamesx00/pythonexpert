def is_interleave(s1, s2, s3):
    n, m = len(s1), len(s2)
    if n + m != len(s3):
        return False
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            ok = False
            if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                ok = True
            if not ok and j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                ok = True
            dp[i][j] = ok
    return dp[n][m]
