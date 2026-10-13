---
lesson_name: Valid Parenthesis String
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Without stars, you'd track one count of open brackets. With stars, the count isn't fixed. What range of counts is possible after each character?"
  - "Use *Keep a range instead of one value* from *Greedy Basics*: `lo` is the fewest open brackets possible, `hi` the most. A `*` lowers `lo` and raises `hi`. If `hi < 0`, too many `)`. Never let `lo` go below `0`."
  - "Template: `lo = hi = 0`. `(`: both `+1`. `)`: both `-1`. `*`: `lo -= 1`, `hi += 1`. After each character, return `False` if `hi < 0`, then `lo = max(lo, 0)`. Return `lo == 0`."
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

### Valid Parenthesis String

You're given a string `s` made up only of the characters `(`, `)`, and `*`, where each `*` can be treated as either `(`, `)`, or an empty string. Write a function `check_valid_string(s)` that returns `True` if there's some way to interpret every `*` so the resulting string of parentheses is balanced (every opening bracket has a matching closing bracket, in the correct order), and `False` otherwise.

For example, `s = "(*))"` is valid because treating the `*` as `(` turns it into the balanced `(())`. But `s = "(((*"` is not valid: even treating the `*` as `(` still leaves three opening brackets with nothing to close them.

---

### Tests

<ul>
<li id="test-1"><code>check_valid_string("()")</code> should return <code>True</code></li>
<li id="test-2"><code>check_valid_string("(*)")</code> should return <code>True</code></li>
<li id="test-3"><code>check_valid_string("(*))")</code> should return <code>True</code></li>
<li id="test-4"><code>check_valid_string("(((*")</code> should return <code>False</code></li>
<li id="test-5"><code>check_valid_string("())")</code> should return <code>False</code></li>
<li id="test-6"><code>check_valid_string(")(")</code> should return <code>False</code></li>
<li id="test-7"><code>check_valid_string("*")</code> should return <code>True</code></li>
<li id="test-8"><code>check_valid_string("((*)")</code> should return <code>True</code></li>
<li id="test-9">Performance: a string of 18,000 characters, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def check_valid_string(s):
    lo = hi = 0
    for c in s:
        if c == '(':
            lo += 1
            hi += 1
        elif c == ')':
            lo -= 1
            hi -= 1
        else:
            lo -= 1
            hi += 1
        if hi < 0:
            return False
        lo = max(lo, 0)
    return lo == 0
```

**Brute force:** try all three choices for every `*` and check each resulting string. That's `O(3^k * n)` for `k` stars. Keeping a set of every possible open count instead is `O(n^2)`.

**Bottleneck:** the set of possible open counts is always an unbroken range, so storing every value in it is wasted work.

**Optimal idea:** keep just the range ends. `lo` is the fewest open brackets any choice of stars gives so far, `hi` the most. `(` raises both, `)` lowers both, `*` lowers `lo` and raises `hi`.

**Why it's correct:** the possible counts form a range with no gaps. It starts as `{0}`. `(` and `)` shift every count by the same amount, and `*` turns each count `x` into `x - 1`, `x` and `x + 1`, which fills any gap. A count below `0` means a `)` with nothing to close, so that choice is dead. Clamping `lo` at `0` throws those choices away. If even `hi` goes below `0`, every choice is dead, so return `False`. At the end, some choice is balanced exactly when `0` is in the range, which is when `lo == 0`.

**Complexity:** `O(n)` time, one pass. `O(1)` extra space.

**Common mistakes:** not clamping `lo`, which lets a dead choice cancel a later `(`: `"*("` would return `True`. Returning `hi >= 0` or `lo <= 0 <= hi` without the clamp. Treating `*` as only `(` or only `)`.

</details>
