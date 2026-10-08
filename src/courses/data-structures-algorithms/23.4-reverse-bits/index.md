---
lesson_name: Reverse Bits
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

### Reverse Bits

Write a function `reverse_bits(n)` that takes an integer `n` representing a **32-bit unsigned** value and returns the integer you get by reversing the order of its 32 bits.

Python integers don't have a fixed width, so treat `n` as if it were stored in exactly 32 bits: the bit at position 0 (the least significant bit) swaps places with the bit at position 31 (the most significant bit), the bit at position 1 swaps with position 30, and so on. Both the input and the output are plain Python ints, but you should reason about them as 32-bit unsigned binary strings while doing the reversal — build the result by reading `n`'s bits from least significant to most significant and writing them into the result from most significant to least significant.

For example, `n = 1` is `00000000000000000000000000000001` as a 32-bit value. Reversing those bits puts the single `1` at the front instead of the back, giving `10000000000000000000000000000000`, which as an unsigned integer is `2147483648`.

---

### Tests

<ul>
<li id="test-1"><code>reverse_bits(1)</code> should return <code>2147483648</code></li>
<li id="test-2"><code>reverse_bits(0)</code> should return <code>0</code></li>
<li id="test-3"><code>reverse_bits(4294967295)</code> should return <code>4294967295</code></li>
<li id="test-4"><code>reverse_bits(43261596)</code> should return <code>964176192</code></li>
<li id="test-5"><code>reverse_bits(2147483648)</code> should return <code>1</code></li>
<li id="test-6"><code>reverse_bits(2)</code> should return <code>1073741824</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def reverse_bits(n):
    result = 0
    for i in range(32):
        bit = (n >> i) & 1
        result |= bit << (31 - i)
    return result
```

</details>
