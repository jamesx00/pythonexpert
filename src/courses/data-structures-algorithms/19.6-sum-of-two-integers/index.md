---
lesson_name: Sum of Two Integers
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

### Sum of Two Integers

Write a function `sum_of_two(a, b)` that returns the sum of two 32-bit signed integers `a` and `b`, **without using the `+` or `-` operators anywhere in your solution** (this includes `+=`, `-=`, `sum()`, and similar). You may use bitwise operators, comparisons, loops, and multiplication/division by powers of two.

The trick is to add numbers the way binary adders work in hardware: `a ^ b` gives you the sum of each bit position ignoring carries, while `(a & b) << 1` gives you the carry that needs to be added back in. Repeating this — replacing `a` with the XOR result and `b` with the shifted carry — until there is no carry left produces the final sum. Because Python integers have unlimited width (unlike a real 32-bit register), you'll need to mask intermediate results to 32 bits and convert back to a signed value at the end so negative numbers behave correctly.

For example, `sum_of_two(3, 5)` should behave exactly like `3 + 5` and return `8`; `sum_of_two(-2, 3)` should return `1`.

---

### Tests

<ul>
<li id="test-1"><code>sum_of_two(3, 5)</code> should return <code>8</code></li>
<li id="test-2"><code>sum_of_two(-2, 3)</code> should return <code>1</code></li>
<li id="test-3"><code>sum_of_two(0, 0)</code> should return <code>0</code></li>
<li id="test-4"><code>sum_of_two(-5, -7)</code> should return <code>-12</code></li>
<li id="test-5"><code>sum_of_two(12, -12)</code> should return <code>0</code></li>
<li id="test-6"><code>sum_of_two(100, 250)</code> should return <code>350</code></li>
<li id="test-7"><code>sum_of_two(-1, 1)</code> should return <code>0</code></li>
</ul>
