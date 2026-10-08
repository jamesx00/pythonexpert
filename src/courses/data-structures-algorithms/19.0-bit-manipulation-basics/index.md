---
lesson_name: Bit Manipulation Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Bit Manipulation
---

## Why This Pattern Matters &#x1F4A1;

Integers are stored as binary bits. Bitwise operators work on all bits at once, which allows `O(1)`-space tricks that would otherwise need a hash set or extra loops.

## The Operators &#x1F9F1;

| Operator | Meaning | Example (`a = 0b1100`, `b = 0b1010`) |
| --- | --- | --- |
| `a & b` | AND: 1 if both are 1 | `0b1000` |
| `a \| b` | OR: 1 if either is 1 | `0b1110` |
| `a ^ b` | XOR: 1 if they differ | `0b0110` |
| `~a` | NOT: flip every bit | `-13` in Python |
| `a << k` | shift left (× 2ᵏ) | `0b110000` |
| `a >> k` | shift right (÷ 2ᵏ) | `0b11` |

Use `bin(x)` to see the bits, e.g. `bin(12) == '0b1100'`.

## Must-Know Tricks &#x1F9E0;

```python
(x >> i) & 1        # read bit i
x | (1 << i)        # set bit i
x & ~(1 << i)       # clear bit i
x ^ (1 << i)        # toggle bit i
x & (x - 1)         # drop the lowest set bit
x & -x              # isolate the lowest set bit
x & (x - 1) == 0    # x is a power of two (for x > 0)
```

**XOR cancels pairs:** `a ^ a == 0` and `a ^ 0 == a`, in any order. XOR every number together and the pairs disappear, leaving the odd one out (*Single Number*, *Missing Number*).

### Counting set bits

```python
def count_bits(n):
    count = 0
    while n:
        n &= n - 1      # each step removes one 1-bit
        count += 1
    return count
```

### Counting bits for 0..n with DP

`bits[i] = bits[i >> 1] + (i & 1)`. Shifting right drops the last bit, which you already counted.

## Tips & Gotchas &#x1F4CC;

- **Python ints are unbounded**, so `~x` and negative numbers don't wrap at 32 bits. For 32-bit problems, mask with `& 0xFFFFFFFF`, and convert back with `x if x <= 0x7FFFFFFF else ~(x ^ 0xFFFFFFFF)`.
- **Reversing 32 bits:** loop exactly 32 times, `result = (result << 1) | (n & 1)` and `n >>= 1`.
- **Adding without `+`:** `a ^ b` is the sum without carries, `(a & b) << 1` is the carries. Repeat until there are no carries (with the 32-bit mask in Python).
- **Operator precedence:** `&`, `|`, `^` bind more loosely than `==`, so `x & 1 == 0` means `x & (1 == 0)`. Use parentheses: `(x & 1) == 0`.
- `bin(n).count("1")` or `n.bit_count()` (Python 3.10+) is fine in real code. Interviewers usually want the manual version.
