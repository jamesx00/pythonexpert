---
lesson_name: "Warm-up: Tribonacci Bottom-Up"
code_editor: True
code_execution: True
adding_file_allowed: False
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

### Warm-up: Tribonacci Bottom-Up

The Tribonacci numbers are like Fibonacci, but each term is the sum of the previous **three**: `t(0) = 0`, `t(1) = 1`, `t(2) = 1`, and `t(n) = t(n - 1) + t(n - 2) + t(n - 3)`.

Write a function `tribonacci(n)` using **bottom-up** DP: no recursion. Fill in answers from the smallest `n` upward.

For example, `tribonacci(4)` returns `4` (`0, 1, 1, 2, 4`).

**Hint:** you could fill a list `dp` of size `n + 1`. But each value only depends on the last three, so three variables are enough: on each step, `a, b, c = b, c, a + b + c`.

---

### Tests

<ul>
<li id="test-1"><code>tribonacci(0)</code> should return <code>0</code></li>
<li id="test-2"><code>tribonacci(1)</code> should return <code>1</code></li>
<li id="test-3"><code>tribonacci(2)</code> should return <code>1</code></li>
<li id="test-4"><code>tribonacci(4)</code> should return <code>4</code></li>
<li id="test-5"><code>tribonacci(25)</code> should return <code>1389537</code></li>
<li id="test-6"><code>tribonacci(37)</code> should return <code>2082876103</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b, c = 0, 1, 1
    for _ in range(n - 2):
        a, b, c = b, c, a + b + c
    return c
```

Bottom-up DP solves subproblems in an order where everything you need is already computed, so there's no recursion and no memo. Keeping only the last three values reduces space from `O(n)` to `O(1)`. *Climbing Stairs*, *House Robber* and *Min Cost Climbing Stairs* all compress this way.

</details>
