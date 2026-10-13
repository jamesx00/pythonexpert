def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1.0
    base = x
    while n > 0:
        if n % 2 == 1:
            result *= base
        base *= base
        n //= 2
    return result
