def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def count_x_buggy(s):
    """Meant to count how many times "x" appears in s. It has a bug."""
    if s == "":
        return 0
    if s[0] == "x":
        1 + count_x_buggy(s[1:])
    return count_x_buggy(s[1:])


def fib_call_order():
    return [4, 3, 2, 1, 0, 1, 2, 1, 0]


def fib_return_order():
    return [1, 0, 1, 1, 2, 1, 0, 1, 3]


def fib_max_depth():
    return 4


def fib_total_calls():
    return 9


def buggy_result():
    return 0


def count_x(s):
    if s == "":
        return 0
    if s[0] == "x":
        return 1 + count_x(s[1:])
    return count_x(s[1:])
