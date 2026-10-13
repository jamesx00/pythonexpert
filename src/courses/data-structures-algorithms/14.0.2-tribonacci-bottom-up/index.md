---
lesson_name: "Warm-up: Tribonacci Bottom-Up"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "To get `t(5)`, which values do you need? Which order lets you have them ready before you need them?"
  - "Use *Bottom-up: fill a table* and *Space optimisation* from *1-D Dynamic Programming Basics*: start from `t(0), t(1), t(2)` and move forward. Each value needs only the last three, so keep three variables and shift them: `a, b, c = b, c, a + b + c`."
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

### Warm-up: Tribonacci Bottom-Up

The Tribonacci numbers are like Fibonacci, but each term is the sum of the previous **three**: `t(0) = 0`, `t(1) = 1`, `t(2) = 1`, and `t(n) = t(n - 1) + t(n - 2) + t(n - 3)`.

Write a function `tribonacci(n)` using **bottom-up** DP: no recursion. Fill in answers from the smallest `n` upward.

For example, `tribonacci(4)` returns `4` (`0, 1, 1, 2, 4`).

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

**Brute force:** the plain recursion `t(n - 1) + t(n - 2) + t(n - 3)`. Each call makes three more, so the number of calls grows exponentially. `tribonacci(37)` would take billions of calls.

**Bottleneck:** the recursion asks for the same small values over and over.

**Optimal idea:** go the other way. Start from the base cases and compute `t(3)`, `t(4)`, ... in order, so every value you need is already known. Only the last three values are ever used, so keep just those three in `a`, `b` and `c`.

**Why it's correct:** before each step, `a, b, c` hold `t(i - 3), t(i - 2), t(i - 1)`. The step computes `t(i) = a + b + c` and shifts the window by one. After `n - 2` steps, `c` holds `t(n)`.

**Complexity:** `O(n)` time, one addition per step. `O(1)` extra space.

**Common mistakes:** updating the variables one at a time (`a = b`, then `b = c`, then `c = a + b + c`), which uses the new `a` and `b` in the sum. The tuple assignment computes the right side first. Running the loop `n` times instead of `n - 2` and going past the answer. Forgetting the cases `n = 0`, `1` and `2`.

</details>
