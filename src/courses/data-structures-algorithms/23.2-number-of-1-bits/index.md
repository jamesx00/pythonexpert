---
lesson_name: Number of 1 Bits
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(k)
  space: O(1)
hints:
  - "Can you remove one `1` bit at a time, without looking at the `0` bits?"
  - "Use *Counting set bits* from *Bit Manipulation Basics*: `n & (n - 1)` drops the lowest set bit. Count how many times you can do that before `n` is `0`."
  - "Template: `count = 0`. While `n`: `n &= n - 1`, `count += 1`. Return `count`."
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

### Number of 1 Bits

Write a function `count_set_bits(n)` that takes a non-negative integer `n` and returns how many bits in its binary representation are `1` (this is often called the Hamming weight).

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
<li id="test-8"><code>count_set_bits(2147483648)</code> should return <code>1</code></li>
<li id="test-9"><code>count_set_bits(2863311530)</code> should return <code>16</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
```

Here `k` is the number of `1` bits in `n`.

**Brute force:** check the lowest bit with `n & 1`, add it to the count, and shift `n` right with `n >>= 1` until `n` is `0`. That's one step per bit of `n`, `O(log n)` steps, or 32 for a 32-bit number. It's a fine answer. Every approach here is fast, so there's no performance test.

**Bottleneck:** the shift loop also spends a step on every `0` bit. `2147483648` has a single `1` bit but takes 32 steps.

**Optimal idea:** `n - 1` flips the lowest `1` bit of `n` to `0` and every `0` below it to `1`. AND-ing it with `n` keeps everything above that bit and clears the rest. So `n &= n - 1` removes exactly one `1` bit per step.

**Why it's correct:** each step removes one `1` bit and leaves the others alone, so the loop runs once per `1` bit and stops when none are left.

**Complexity:** `O(k)` time, at most 32 steps for a 32-bit number. `O(1)` extra space.

**Common mistakes:** writing `n & 1 == 1`, which Python reads as `n & (1 == 1)`. It happens to work here, but `n & 1 == 0` does not. Using `n & (n - 1)` without assigning it back to `n`, which loops forever. `bin(n).count("1")` and `n.bit_count()` are fine in real code, but interviewers usually want the loop.

</details>
