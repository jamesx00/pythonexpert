def num_decodings(digits):
    n = len(digits)
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[n] = 1
    dp[n - 1] = 1 if digits[n - 1] != '0' else 0
    for i in range(n - 2, -1, -1):
        if digits[i] == '0':
            dp[i] = 0
            continue
        dp[i] = dp[i + 1]
        two = int(digits[i:i + 2])
        if 10 <= two <= 26:
            dp[i] += dp[i + 2]
    return dp[0]
