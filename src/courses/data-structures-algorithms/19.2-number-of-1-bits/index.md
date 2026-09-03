---
lesson_name: Number of 1 Bits
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

### Number of 1 Bits

Write a function `count_set_bits(n)` that takes a non-negative integer `n` and returns how many bits in its binary representation are `1` (this is often called the Hamming weight).

You can solve this by repeatedly checking the lowest bit of `n` with `n & 1` and then shifting `n` right by one (`n >>= 1`) until nothing is left, counting every `1` you see along the way. A faster trick is `n & (n - 1)`, which clears the lowest set bit in one step, letting you count set bits in a number of iterations equal to the count itself.

For example, `n = 11` is `1011` in binary, which has three `1` bits, so the function should return `3`.

---

### Tests

<ul>
<li id="test-1"><code>count_set_bits(11)</code> should return <code>3</code></li>
<li id="test-2"><code>count_set_bits(0)</code> should return <code>0</code></li>
<li id="test-3"><code>count_set_bits(1)</code> should return <code>1</code></li>
<li id="test-4"><code>count_set_bits(128)</code> should return <code>1</code></li>
<li id="test-5"><code>count_set_bits(255)</code> should return <code>8</code></li>
<li id="test-6"><code>count_set_bits(1023)</code> should return <code>10</code></li>
<li id="test-7"><code>count_set_bits(4294967295)</code> should return <code>32</code></li>
</ul>
