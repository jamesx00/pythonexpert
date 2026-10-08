---
lesson_name: "Warm-up: Power"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(log n)
  space: O(log n)
hints:
  - "If you already knew `x` to the power `n // 2`, how could you get `x` to the power `n` with one or two more multiplications? What changes when `n` is odd?"
  - "Use the *Split in half* shape in *Recursion Basics*: compute `half = power(x, n // 2)` **once**, then return `half * half` if `n` is even, or `half * half * x` if it's odd. Calling `power(x, n // 2)` twice makes it `O(n)` again."
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

### Warm-up: Power

Write a **recursive** function `power(x, n)` that returns `x` raised to the power `n`, where `x` is an integer and `n` is a non-negative integer.

Don't use `**` or `pow()`: `power` must call itself. Multiplying by `x` once per call works for small `n`, but it needs `n` calls. Aim for `O(log n)` calls, so that `power(1, 1_000_000_000)` returns straight away.

---

### Tests

<ul>
<li id="test-1"><code>power(2, 10)</code> should return <code>1024</code></li>
<li id="test-2"><code>power(3, 0)</code> should return <code>1</code></li>
<li id="test-3"><code>power(5, 1)</code> should return <code>5</code></li>
<li id="test-4"><code>power(-2, 3)</code> should return <code>-8</code></li>
<li id="test-5"><code>power(2, 31)</code> should return <code>2147483648</code></li>
<li id="test-6"><code>power(7, 13)</code> should return <code>96889010407</code></li>
<li id="test-7"><code>power(2, 10)</code> calls itself</li>
<li id="test-8">Performance: <code>power(1, 1_000_000_000)</code> should return <code>1</code> within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x
```

**Brute force:** `return x * power(x, n - 1)`, with base case `n == 0`. It makes `n + 1` calls, so it's `O(n)` time and `O(n)` stack depth. For `n = 1,000,000,000` it hits Python's recursion limit long before finishing.

**Bottleneck:** shrinking `n` by one per call. Each call does a tiny amount of work and leaves almost the whole problem for the next call.

**Optimal idea:** halve `n` instead. `xⁿ = (x^(n/2))²` when `n` is even, and `x · (x^(n//2))²` when it's odd. Compute `power(x, n // 2)` once, store it, and square it.

**Why it's correct:** for even `n`, `n // 2 + n // 2 = n`. For odd `n`, `n // 2 + n // 2 + 1 = n`, so the extra factor of `x` makes up the difference. `n` strictly decreases until it reaches the base case `0`, where `x⁰ = 1`.

**Complexity:** `n` halves on every call, so there are about `log₂ n + 2` calls, each doing `O(1)` multiplications: `O(log n)` time. The stack is `O(log n)` frames deep. (With very large results, multiplying big integers costs more than `O(1)`, but the number of calls stays `O(log n)`.)

**Common mistakes:** writing `power(x, n // 2) * power(x, n // 2)`. That makes two calls per level, so the call tree doubles at every level and the total is back to `O(n)` calls. Forgetting the extra `* x` for odd `n`. Using `n / 2`, which gives a float that never reaches exactly `0`.

</details>
