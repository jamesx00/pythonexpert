---
lesson_name: Reverse Integer
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(log x)
  space: O(1)
hints:
  - "How do you take the last digit off a number, and how do you add a digit to the end of another?"
  - "Work on `abs(x)` and put the sign back at the end. `digits % 10` is the last digit and `digits //= 10` drops it, and `reversed_num * 10 + digit` appends it. Python ints are unbounded (see *Tips & Gotchas* in *Bit Manipulation Basics*), so check the 32-bit range yourself at the end."
  - "Template: `sign = -1 if x < 0 else 1`, `digits = abs(x)`, `reversed_num = 0`. While `digits`: `reversed_num = reversed_num * 10 + digits % 10`, `digits //= 10`. Multiply by `sign`, and return `0` if it's outside `-2147483648..2147483647`."
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

### Reverse Integer

Write a function `reverse_integer(x)` that takes a signed integer `x` and returns the integer formed by reversing its decimal digits, keeping the original sign. Treat `x` as if it were stored in a **32-bit signed** register, with a valid range of `-2147483648` to `2147483647` — if reversing the digits would produce a value outside that range, the function should return `0` instead of the actual reversed value.

For example, `reverse_integer(513)` should return `315`, and `reverse_integer(-120)` should return `-21` (the trailing zero disappears once it becomes a leading digit). An input like `reverse_integer(1563847412)` reverses to `2147483651`, which is just past the 32-bit signed maximum of `2147483647`, so the function should return `0` for it.

---

### Tests

<ul>
<li id="test-1"><code>reverse_integer(513)</code> should return <code>315</code></li>
<li id="test-2"><code>reverse_integer(-120)</code> should return <code>-21</code></li>
<li id="test-3"><code>reverse_integer(0)</code> should return <code>0</code></li>
<li id="test-4"><code>reverse_integer(100)</code> should return <code>1</code></li>
<li id="test-5"><code>reverse_integer(1563847412)</code> should return <code>0</code></li>
<li id="test-6"><code>reverse_integer(-2147483648)</code> should return <code>0</code></li>
<li id="test-7"><code>reverse_integer(7)</code> should return <code>7</code></li>
<li id="test-8"><code>reverse_integer(-1563847412)</code> should return <code>0</code></li>
<li id="test-9"><code>reverse_integer(1463847412)</code> should return <code>2147483641</code></li>
<li id="test-10"><code>reverse_integer(-2147483412)</code> should return <code>-2143847412</code></li>
<li id="test-11"><code>reverse_integer(-8)</code> should return <code>-8</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def reverse_integer(x):
    sign = -1 if x < 0 else 1
    digits = abs(x)
    reversed_num = 0
    while digits:
        reversed_num = reversed_num * 10 + digits % 10
        digits //= 10
    reversed_num *= sign
    if reversed_num < -2147483648 or reversed_num > 2147483647:
        return 0
    return reversed_num
```

**Brute force:** `int(str(abs(x))[::-1])`, then put the sign back and check the range. It's also `O(log x)`, one step per digit, and a fine answer in Python, so there's no performance test. The digit loop is what interviewers expect, because it doesn't rely on strings.

**Bottleneck:** the 32-bit rule. Python ints never overflow, so a reversed number like `2147483651` is stored without complaint. You have to check the range yourself.

**Optimal idea:** peel digits off the end of `abs(x)` with `% 10` and `// 10`, and append each one to `reversed_num` with `* 10 +`. Put the sign back, then return `0` if the result is outside `-2147483648..2147483647`.

**Why it's correct:** the loop reads the digits of `abs(x)` from last to first and writes them from first to last, so `reversed_num` holds them in reverse order. Trailing zeros of `x` become leading zeros, which add nothing: `120` gives `21`. The range check covers both ends, since the sign is applied first: `-1563847412` reverses to `-2147483651`, just below the minimum. In a language with 32-bit ints, you'd check before each `* 10` instead, since the overflow would happen inside the loop.

**Complexity:** `O(log x)` time, one step per decimal digit, at most 10 for a 32-bit number. `O(1)` extra space.

**Common mistakes:** using `x % 10` on a negative `x`: in Python, `-123 % 10` is `7`, not `-3`. Reversing `str(x)` with the minus sign, which gives `"321-"` and a `ValueError`. Checking only the upper bound, which misses `-2147483651`.

</details>
