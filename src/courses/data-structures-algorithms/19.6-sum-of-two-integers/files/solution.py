def sum_of_two(a, b):
    mask = 0xFFFFFFFF
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    if a > 0x7FFFFFFF:
        a = ~(a ^ mask)
    return a
