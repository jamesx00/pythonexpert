---
lesson_name: Climbing Stairs
section: 1-D Dynamic Programming
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

</details>
