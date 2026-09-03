---
lesson_name: Counting Bits
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

### Counting Bits

Write a function `count_bits(n)` that takes a non-negative integer `n` and returns a list `result` of length `n + 1`, where `result[i]` is the number of `1` bits in the binary representation of `i`, for every `i` from `0` to `n` inclusive.

Rather than counting the set bits of each number from scratch, notice that any number `i` can be split into its lowest bit and the rest: `i >> 1` drops the lowest bit, and `i & 1` tells you whether that dropped bit was a `1`. That means `result[i] = result[i >> 1] + (i & 1)`, so you can build the whole list from previously computed answers in a single linear pass.

For example, given `n = 5`, the binary forms of `0` through `5` are `0, 1, 10, 11, 100, 101`, with `0, 1, 1, 2, 1, 2` set bits respectively, so the function should return `[0, 1, 1, 2, 1, 2]`.

---

### Tests

<ul>
<li id="test-1"><code>count_bits(5)</code> should return <code>[0, 1, 1, 2, 1, 2]</code></li>
<li id="test-2"><code>count_bits(0)</code> should return <code>[0]</code></li>
<li id="test-3"><code>count_bits(1)</code> should return <code>[0, 1]</code></li>
<li id="test-4"><code>count_bits(2)</code> should return <code>[0, 1, 1]</code></li>
<li id="test-5"><code>count_bits(8)</code> should return <code>[0, 1, 1, 2, 1, 2, 2, 3, 1]</code></li>
<li id="test-6"><code>count_bits(15)</code> should return <code>[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]</code></li>
</ul>
