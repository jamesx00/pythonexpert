def get_bit(x, i):
    return (x >> i) & 1


def set_bit(x, i):
    return x | (1 << i)


def clear_bit(x, i):
    return x & ~(1 << i)
