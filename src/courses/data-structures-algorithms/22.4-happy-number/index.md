---
lesson_name: Happy Number
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(log n)
  space: O(log n)
hints:
  - "The chain either reaches `1` or repeats forever. How can you notice that it's repeating?"
  - "Keep a `seen` set of numbers you've visited, the same cycle check as in linked lists. See *Cycle detection on numbers* in *Math & Geometry Basics*, and *Digits* for summing the squared digits."
  - "Template: `seen = set()`. While `n != 1 and n not in seen`: add `n` to `seen`, then `n = sum(int(d) ** 2 for d in str(n))`. Return `n == 1`."
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

### Happy Number

Take a positive integer `n` and repeatedly replace it with the sum of the squares of its digits. Keep repeating this process. Write a function that returns `True` if this chain of replacements eventually reaches `1`, and `False` if it instead falls into a repeating cycle that never includes `1`.

For example, starting from `19`: `1^2 + 9^2 = 82`, then `8^2 + 2^2 = 68`, then `6^2 + 8^2 = 100`, then `1^2 + 0^2 + 0^2 = 1`. Since the chain reached `1`, `19` is happy. Starting from `2`, the chain cycles through `4, 16, 37, 58, 89, 145, 42, 20, 4, ...` forever without ever hitting `1`, so `2` is not happy.

---

### Tests

<ul>
<li id="test-1"><code>is_happy(19)</code> should return <code>True</code></li>
<li id="test-2"><code>is_happy(2)</code> should return <code>False</code></li>
<li id="test-3"><code>is_happy(1)</code> should return <code>True</code></li>
<li id="test-4"><code>is_happy(7)</code> should return <code>True</code></li>
<li id="test-5"><code>is_happy(4)</code> should return <code>False</code></li>
<li id="test-6"><code>is_happy(100)</code> should return <code>True</code></li>
<li id="test-7"><code>is_happy(89)</code> should return <code>False</code></li>
<li id="test-8"><code>is_happy(1111111)</code> should return <code>True</code></li>
<li id="test-9"><code>is_happy(999999999)</code> should return <code>False</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
```

**Brute force:** run the chain for a fixed number of steps, say 1,000, and answer `False` if it hasn't reached `1`. It works in practice, but the cutoff is a guess, not a proof. There's no slower approach to beat here: every method follows the same short chain.

**Bottleneck:** you need a sure way to know the chain will never reach `1`.

**Optimal idea:** record every number in a `seen` set. If a number comes back, the chain is in a loop, and since it hasn't hit `1` yet, it never will.

**Why it's correct:** each number fully decides the next one. So once a number repeats, the chain repeats the same loop forever. The chain also can't grow forever: a number with `d` digits has a digit-square sum of at most `81 * d`, which is smaller than the number once it has 4 or more digits. So the chain drops below 1,000 fast, stays there, and must either reach `1` or repeat.

**Complexity:** the first step takes `O(log n)` time for the digits of `n`. After that the numbers are below 1,000, and only a few steps are left. `O(log n)` time and space overall. Fast and slow pointers (one step vs. two steps) give the same answer with `O(1)` space.

**Common mistakes:** looping `while n != 1` with no cycle check, which never ends for `2`. Checking `n in seen` after adding `n`, which stops at once and answers `False` for every number.

</details>
