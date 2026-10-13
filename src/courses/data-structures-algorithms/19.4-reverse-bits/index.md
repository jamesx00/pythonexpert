---
lesson_name: Reverse Bits
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(1)
  space: O(1)
hints:
  - "Read the bits of `n` from the right, one at a time. Where does each one go in the result?"
  - "See *Reversing 32 bits* in *Bit Manipulation Basics*: bit `i` of `n` moves to bit `31 - i` of the result. Loop exactly 32 times, so leading zeros count too."
  - "Template: `result = 0`. Repeat 32 times: `result = (result << 1) | (n & 1)`, `n >>= 1`. Return `result`."
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

### Reverse Bits

Write a function `reverse_bits(n)` that takes an integer `n` representing a **32-bit unsigned** value and returns the integer you get by reversing the order of its 32 bits.

Python integers don't have a fixed width, so treat `n` as if it were stored in exactly 32 bits: the bit at position 0 (the least significant bit) swaps places with the bit at position 31 (the most significant bit), the bit at position 1 swaps with position 30, and so on. Both the input and the output are plain Python ints, but you should reason about them as 32-bit unsigned binary strings while doing the reversal.

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
<li id="test-7"><code>reverse_bits(4294967293)</code> should return <code>3221225471</code></li>
<li id="test-8"><code>reverse_bits(6)</code> should return <code>1610612736</code></li>
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

**Brute force:** format `n` as a 32-character binary string with `format(n, "032b")`, reverse it with `[::-1]`, and convert back with `int(..., 2)`. It's also `O(1)` for 32 bits and a fine answer in real code, so there's no performance test. The bit loop is what interviewers expect.

**Bottleneck:** `bin(n)` drops the leading zeros, so reversing it without padding to 32 characters gives the wrong answer: `bin(1)[2:]` is `"1"`, which reverses to `1`, not `2147483648`.

**Optimal idea:** take bit `i` of `n` with `(n >> i) & 1` and put it at position `31 - i` of the result. Loop over all 32 positions, so the leading zeros of `n` become trailing zeros of the result.

**Why it's correct:** reversing 32 bits means exactly that bit `i` swaps with bit `31 - i`. Every position from `0` to `31` is handled once, and OR-ing into `result` never disturbs bits already placed, since each goes to a different position.

**Complexity:** `O(1)`: always 32 steps. `O(1)` extra space.

**Common mistakes:** stopping when `n` becomes `0` instead of after 32 steps, which loses the trailing zeros of the result. Reversing `bin(n)` without padding. Shifting the result one time too many, for example `result <<= 1` after the last bit, which doubles the answer.

</details>
