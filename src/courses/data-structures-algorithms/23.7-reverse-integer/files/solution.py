def reverse_integer(x):
    sign = -1 if x < 0 else 1
    digits = abs(x)
    reversed_num = 0
    while digits:
        reversed_num = reversed_num * 10 + digits % 10
        digits //= 10
    reversed_num *= sign
    if reversed_num < -2147483648 or reversed_num > 2147483647:
        return 0
    return reversed_num
