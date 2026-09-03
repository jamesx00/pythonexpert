---
lesson_name: Reverse Integer
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

### Reverse Integer

Write a function `reverse_integer(x)` that takes a signed integer `x` and returns the integer formed by reversing its decimal digits, keeping the original sign. Treat `x` as if it were stored in a **32-bit signed** register, with a valid range of `-2147483648` to `2147483647` — if reversing the digits would produce a value outside that range, the function should return `0` instead of the actual reversed value.

Work with the absolute value of `x` to reverse the digits (peeling off the last digit with `% 10` and dividing by `10` repeatedly, building the reversed number from the front), then reapply the original sign before checking it against the 32-bit bounds.

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

</details>
