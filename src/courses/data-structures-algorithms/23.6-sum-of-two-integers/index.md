---
lesson_name: Sum of Two Integers
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(1)
  space: O(1)
hints:
  - "Adding two bits gives a sum bit and a carry bit. Which bitwise operators compute each of those for all positions at once?"
  - "See *Adding without `+`* in *Bit Manipulation Basics*: `a ^ b` is the sum without carries and `(a & b) << 1` is the carries. Add them again the same way until there are no carries. Python ints don't stop at 32 bits, so mask with `& 0xFFFFFFFF`."
  - "Template: `mask = 0xFFFFFFFF`. While `b`: `a, b = (a ^ b) & mask, ((a & b) << 1) & mask`. At the end, if `a > 0x7FFFFFFF`, convert back to negative with `a = ~(a ^ mask)`. Return `a`."
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

### Sum of Two Integers

Write a function `sum_of_two(a, b)` that returns the sum of two 32-bit signed integers `a` and `b`, **without using the `+` or `-` operators anywhere in your solution** (this includes `+=`, `-=`, `sum()`, and similar). You may use bitwise operators, comparisons, loops, and multiplication/division by powers of two.

Both numbers and their sum fit in a 32-bit signed integer, from `-2147483648` to `2147483647`. Python integers have no fixed width, unlike a real 32-bit register, so negative numbers need extra care.

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
<li id="test-8"><code>sum_of_two(5, -9)</code> should return <code>-4</code></li>
<li id="test-9"><code>sum_of_two(2147483647, -1)</code> should return <code>2147483646</code></li>
<li id="test-10"><code>sum_of_two(1073741824, 1073741823)</code> should return <code>2147483647</code></li>
<li id="test-11"><code>sum_of_two(-2147483648, 2147483647)</code> should return <code>-1</code></li>
<li id="test-12"><code>sum_of_two(-2147483648, 0)</code> should return <code>-2147483648</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def sum_of_two(a, b):
    mask = 0xFFFFFFFF
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    if a > 0x7FFFFFFF:
        a = ~(a ^ mask)
    return a
```

**Brute force:** without `+` or `-`, there's no obvious slow version. Counting up one at a time would need `+` too. So the question is how to add with bitwise operators alone.

**Bottleneck:** adding bit by bit means handling the carry. A carry can make the next position carry too, and so on.

**Optimal idea:** do every position at once. `a ^ b` adds each pair of bits without the carries: `1 + 1` gives `0`. `a & b` marks where both bits are `1`, which is where a carry starts, and `<< 1` moves each carry into the next position. The sum is now `(a ^ b) + ((a & b) << 1)`, another addition, so repeat until there are no carries left.

**Why it's correct:** each round keeps the total the same: `a + b == (a ^ b) + ((a & b) << 1)`. In a 32-bit register, the carry moves at least one position left every round and falls off after bit 31, so the loop ends within 32 rounds. Python ints have no bit 31 to fall off: a negative number has endless `1` bits on the left, so when one number is negative and the sum isn't, the carry moves left forever. Masking with `0xFFFFFFFF` keeps only 32 bits, like a real register. The result is then the sum as a 32-bit two's complement pattern. If bit 31 is set (`a > 0x7FFFFFFF`), it stands for a negative number. `a ^ mask` flips the low 32 bits and `~` flips every bit, which turns it back into the negative Python int.

**Complexity:** `O(1)`: at most 32 rounds for 32-bit numbers. `O(1)` extra space.

**Common mistakes:** skipping the mask, which loops forever on `sum_of_two(-1, 1)`. Masking but not converting back, which returns `4294967292` instead of `-4` for `sum_of_two(5, -9)`. Converting with `a - 2**32`, which uses `-`. Updating `a` before computing the carry from the old `a`, instead of assigning both at once.

</details>
