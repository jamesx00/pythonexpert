---
lesson_name: Pow(x, n)
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(log n)
  space: O(1)
hints:
  - "If you already know `x^(n/2)`, how many more multiplications do you need to get `x^n`?"
  - "Square the base and halve the exponent at each step, and multiply the base into the result when the exponent is odd. See *Fast power (exponentiation by squaring)* in *Math & Geometry Basics*."
  - "Template: if `n < 0`, set `x = 1 / x` and `n = -n`. Start `result = 1.0`. While `n > 0`: if `n` is odd, `result *= x`. Then `x *= x` and `n //= 2`. Return `result`."
rich_test_results: true
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 1
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 2
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
    id: 1
    name: Python
---

### Pow(x, n)

Write a function that computes `x` raised to the integer power `n`, without relying on a built-in power operator or library function. `n` can be negative, in which case the result is `1 / x^|n|`, and `x` can be a float. Your solution should avoid the naive approach of multiplying `x` by itself `n` times, since `n` may be large.

For example, `my_pow(2.0, 10)` is `1024.0`, and `my_pow(2.0, -2)` is `0.25` (that's `1 / 2^2`).

Floating-point results can differ in the last few digits depending on the order of the multiplications, so answers are compared after rounding to 6 decimal places.

---

### Tests

<ul>
<li id="test-1"><code>my_pow(2.0, 10)</code> should return <code>1024.0</code></li>
<li id="test-2"><code>my_pow(2.0, -2)</code> should return <code>0.25</code></li>
<li id="test-3"><code>my_pow(2.1, 3)</code> should return approximately <code>9.261</code></li>
<li id="test-4"><code>my_pow(5.0, 0)</code> should return <code>1.0</code></li>
<li id="test-5"><code>my_pow(1.0, 1000)</code> should return <code>1.0</code></li>
<li id="test-6"><code>my_pow(-2.0, 3)</code> should return <code>-8.0</code></li>
<li id="test-7"><code>my_pow(0.5, 4)</code> should return <code>0.0625</code></li>
<li id="test-8"><code>my_pow(-3.0, -3)</code> should return approximately <code>-0.037037</code></li>
<li id="test-9">Performance: <code>my_pow(1.000000001, 1000000000)</code> should return approximately <code>2.718282</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
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
```

**Brute force:** multiply `x` into the result `n` times. That's `O(n)` multiplications. Test 9 has `n = 1,000,000,000`, a billion loop steps, which is far too slow.

**Bottleneck:** the brute force recomputes the same products. `x^8` is just `x^4` squared, but the loop builds it one factor at a time.

**Optimal idea:** read `n` in binary. Keep squaring `base`, so it goes through `x`, `x^2`, `x^4`, `x^8`, and so on. Whenever the lowest bit of `n` is `1`, multiply the current `base` into the result. Then halve `n`. A negative `n` becomes `1 / x` raised to `-n`.

**Why it's correct:** `n` is a sum of powers of two, so `x^n` is the product of `x` raised to those powers. Each loop step looks at one bit of `n`, and at that point `base` is `x` raised to that bit's value. So the result collects exactly the right factors.

**Complexity:** `O(log n)` time, one step per bit of `n`. `O(1)` extra space. A recursive version (`half = my_pow(x, n // 2)`) is also `O(log n)` time, but uses `O(log n)` stack space.

**Common mistakes:** calling `my_pow(x, n // 2)` twice in the recursive version, which brings back `O(n)` time. Forgetting negative `n`. Comparing floats with `==`: `2.1 * 2.1 * 2.1` is `9.261000000000001`, which is why the tests round.

</details>
