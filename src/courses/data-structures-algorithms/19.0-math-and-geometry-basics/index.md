---
lesson_name: Math & Geometry Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Math & Geometry
---

## Why This Pattern Matters &#x1F4A1;

This section is a mix of matrix manipulation, digit arithmetic, and number tricks. There's no single template, but a handful of small techniques come up again and again.

## Matrix Techniques &#x1F9EE;

### Rotate 90° clockwise = transpose + reverse each row

```python
def rotate(matrix):
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    for row in matrix:
        row.reverse()
```

### Spiral order with shrinking boundaries

Keep `top`, `bottom`, `left`, `right`. Walk one side, then move that boundary inward. Re-check `top <= bottom` and `left <= right` before walking the last two sides, or a single middle row/column gets visited twice.

### In-place markers

To avoid an extra `O(m × n)` array (*Set Matrix Zeroes*), use the first row and first column as flags, plus one extra variable for the first row itself.

## Number Techniques &#x1F522;

### Digits

```python
while n:
    digit = n % 10      # last digit
    n //= 10            # drop it
```

### Fast power (exponentiation by squaring)

```python
def power(x, n):
    if n < 0:
        x, n = 1 / x, -n
    result = 1
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result
```

`O(log n)` multiplications instead of `n`.

### Grade-school arithmetic on strings

Work from the **rightmost** digit, keep a `carry`, and reverse the result at the end (*Plus One*, *Add Two Numbers*, *Multiply Strings*). For multiplication, digit `i` times digit `j` lands at position `i + j + 1` of a result array of length `len(a) + len(b)`.

## Tips & Gotchas &#x1F4CC;

- **Cycle detection on numbers** (*Happy Number*): a `seen` set or fast/slow pointers, the same idea as in linked lists.
- **Python's `%` and `//` floor toward negative infinity.** `-7 // 2 == -4`. To truncate toward zero, use `int(a / b)`.
- **Python ints never overflow.** Problems that say "return 0 on 32-bit overflow" need an explicit check against `2**31 - 1` and `-2**31`.
- **Geometry with points:** store them in a `Counter` of `(x, y)` tuples for O(1) lookups (*Detect Squares*).
- **Squared distance** (`x*x + y*y`) is enough for comparisons. Skip the `sqrt`.
