def fib(n):
    memo = {}

    def f(i):
        if i < 2:
            return i
        if i in memo:
            return memo[i]
        memo[i] = f(i - 1) + f(i - 2)
        return memo[i]

    return f(n)
