---
lesson_name: Counting Bits
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "`i >> 1` is `i` with its last bit dropped, and it's smaller than `i`. What do you already know about it?"
  - "Use *Counting bits for 0..n with DP* from *Bit Manipulation Basics*: `i` has the same `1` bits as `i >> 1`, plus one more if its last bit `i & 1` is `1`."
  - "Template: `result = [0] * (n + 1)`. For `i` in `range(1, n + 1)`: `result[i] = result[i >> 1] + (i & 1)`. Return `result`."
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

### Counting Bits

Write a function `count_bits(n)` that takes a non-negative integer `n` and returns a list `result` of length `n + 1`, where `result[i]` is the number of `1` bits in the binary representation of `i`, for every `i` from `0` to `n` inclusive.

Try to build the list in a single pass, without counting the bits of each number from scratch.

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
<li id="test-7"><code>count_bits(17)</code> should return <code>[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def count_bits(n):
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    return result
```

**Brute force:** count the bits of every `i` from scratch, for example with the `n & (n - 1)` loop from *Number of 1 Bits*. Each number takes up to `O(log n)` steps, so that's `O(n log n)` time. The extra `log n` factor is too small to time reliably, so there's no performance test.

**Bottleneck:** counting `i` from scratch repeats work you've already done for smaller numbers that share most of its bits.

**Optimal idea:** `i >> 1` drops the last bit of `i`. It's smaller than `i`, so its count is already in `result`. Add `1` if the dropped bit `i & 1` was a `1`.

**Why it's correct:** the bits of `i` are the bits of `i >> 1` followed by the bit `i & 1`. So the number of `1` bits is `result[i >> 1] + (i & 1)`. Filling `i` in increasing order means `result[i >> 1]` is always ready, and `result[0] = 0` starts it off.

**Complexity:** `O(n)` time, one step per number. `O(n)` space for the output list, and no other extra space.

**Common mistakes:** returning a list of length `n` instead of `n + 1`, which drops the count for `n` itself. Writing `result[i >> 1] + i & 1`: `+` binds tighter than `&`, so that's `(result[i >> 1] + i) & 1`. Another correct recurrence is `result[i] = result[i & (i - 1)] + 1`.

</details>
