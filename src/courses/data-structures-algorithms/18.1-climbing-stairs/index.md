---
lesson_name: Climbing Stairs
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Your last move onto step `n` was either a 1-step or a 2-step. Where were you standing just before it?"
  - "So `ways(n) = ways(n - 1) + ways(n - 2)`, with `ways(0) = ways(1) = 1`. That's the Fibonacci-like shape in *Common 1-D Shapes* in *1-D Dynamic Programming Basics*: fill it bottom-up and keep only the last two values (*Space optimisation*)."
  - "Template: if `n <= 1`, return `1`. Set `a, b = 1, 1`. Repeat `n - 1` times: `a, b = b, a + b`. Return `b`."
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

### Climbing Stairs

Write a function `climb_stairs(n)` that returns the number of distinct ways to climb a staircase of `n` steps, given that on each move you may advance either 1 step or 2 steps.

For example, with `n = 3` you could climb `1+1+1`, `1+2`, or `2+1`, so there are 3 distinct ways. `n` is always a non-negative integer, and a staircase with `0` steps has exactly one way to "climb" it (do nothing).

---

### Tests

<ul>
<li id="test-1"><code>climb_stairs(2)</code> should return <code>2</code></li>
<li id="test-2"><code>climb_stairs(3)</code> should return <code>3</code></li>
<li id="test-3"><code>climb_stairs(4)</code> should return <code>5</code></li>
<li id="test-4"><code>climb_stairs(5)</code> should return <code>8</code></li>
<li id="test-5"><code>climb_stairs(1)</code> should return <code>1</code></li>
<li id="test-6"><code>climb_stairs(0)</code> should return <code>1</code></li>
<li id="test-7"><code>climb_stairs(10)</code> should return <code>89</code></li>
<li id="test-8">Performance: a staircase of 40 steps, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def climb_stairs(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
```

**Brute force:** recurse on the last move: `climb_stairs(n - 1) + climb_stairs(n - 2)`. That's correct, but each call makes two more, so it takes about `O(2^n)` calls. `climb_stairs(40)` needs hundreds of millions.

**Bottleneck:** the recursion solves the same smaller staircases many times.

**Optimal idea:** `ways(i)` depends only on `ways(i - 1)` and `ways(i - 2)`. Compute the values from the bottom up and keep only the last two.

**Why it's correct:** every way to reach step `i` ends with a 1-step from `i - 1` or a 2-step from `i - 2`, and never both, so the two counts add up without overlap. `ways(0) = 1` (do nothing) and `ways(1) = 1`. Before each loop step, `a, b` hold `ways(i - 2), ways(i - 1)`, and the step moves them forward by one.

**Complexity:** `O(n)` time. `O(1)` extra space.

**Common mistakes:** returning `0` for `n = 0`: the empty climb counts as one way. Starting the sequence at `1, 2` and then running the loop one time too many or too few. Writing the recursion without a memo, which passes small tests and times out on the large one.

</details>
