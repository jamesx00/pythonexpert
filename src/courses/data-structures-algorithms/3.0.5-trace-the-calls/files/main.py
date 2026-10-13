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


# Step 1
def fib_call_order():
    return []


# Step 2
def fib_return_order():
    return []


# Step 3
def fib_max_depth():
    return 0


# Step 4
def fib_total_calls():
    return 0


# Step 5
def buggy_result():
    return None


# Step 6
def count_x(s):
    return 0
