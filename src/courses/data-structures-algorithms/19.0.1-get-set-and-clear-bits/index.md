---
lesson_name: "Warm-up: Get, Set & Clear Bits"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(1)
  space: O(1)
hints:
  - "How do you build a number that has only bit `i` set? What do `&`, `|` and `~` do with it?"
  - "Use the *Must-Know Tricks* from *Bit Manipulation Basics*: `(x >> i) & 1` reads bit `i`, `x | (1 << i)` sets it and `x & ~(1 << i)` clears it."
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

### Warm-up: Get, Set & Clear Bits

Bits are numbered from the right, starting at `0`. For example, `5` is `0b101`: bits `0` and `2` are `1`, and bit `1` is `0`.

Write three functions:

- `get_bit(x, i)`: return `1` if bit `i` of `x` is set, otherwise `0`.
- `set_bit(x, i)`: return `x` with bit `i` turned **on**.
- `clear_bit(x, i)`: return `x` with bit `i` turned **off**.

For example, `get_bit(5, 1)` is `0`, `set_bit(5, 1)` is `7` (`0b111`), and `clear_bit(5, 0)` is `4` (`0b100`).

---

### Tests

<ul>
<li id="test-1"><code>get_bit(5, 0)</code> should return <code>1</code></li>
<li id="test-2"><code>get_bit(5, 1)</code> should return <code>0</code></li>
<li id="test-3"><code>get_bit(8, 3)</code> should return <code>1</code></li>
<li id="test-4"><code>set_bit(5, 1)</code> should return <code>7</code></li>
<li id="test-5"><code>set_bit(5, 2)</code> should return <code>5</code></li>
<li id="test-6"><code>set_bit(0, 4)</code> should return <code>16</code></li>
<li id="test-7"><code>clear_bit(5, 0)</code> should return <code>4</code></li>
<li id="test-8"><code>clear_bit(5, 1)</code> should return <code>5</code></li>
<li id="test-9"><code>clear_bit(255, 7)</code> should return <code>127</code></li>
<li id="test-10"><code>get_bit(8, 10)</code> should return <code>0</code></li>
<li id="test-11"><code>set_bit(0, 40)</code> should return <code>1099511627776</code></li>
<li id="test-12"><code>clear_bit(1099511627777, 40)</code> should return <code>1</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def get_bit(x, i):
    return (x >> i) & 1


def set_bit(x, i):
    return x | (1 << i)


def clear_bit(x, i):
    return x & ~(1 << i)
```

**Brute force:** convert `x` to a string with `bin(x)`, read or change the character for bit `i`, and convert back with `int(..., 2)`. It works, but it builds strings, and you have to count positions from the right end and pad with zeros when `i` is past the last digit.

**Bottleneck:** the string is a detour. The bits are already in the integer.

**Optimal idea:** `1 << i` is a **mask** with only bit `i` set. `(x >> i) & 1` slides bit `i` to position `0` and masks off everything else. OR-ing with the mask forces that bit to `1`. AND-ing with the inverted mask `~(1 << i)`, which has every bit set except bit `i`, forces it to `0`.

**Why it's correct:** `|` and `&` work on each bit position on its own. At every position except `i`, the mask has a `0` for `|` (or a `1` for `& ~`), which leaves the bit of `x` unchanged. At position `i`, `| 1` gives `1` and `& 0` gives `0`, whatever the bit was before. So setting a bit that's already on, or clearing one that's already off, leaves `x` as it is.

**Complexity:** `O(1)` time and space for the sizes used here. Python ints have no fixed width, so very large numbers cost time proportional to their length.

**Common mistakes:** writing `x & 1 << i` and expecting `0` or `1`: it returns `0` or `2**i`. Clearing with `x ^ (1 << i)`, which *toggles* the bit and turns it on when it was off. Writing `x & 1 == 0` without parentheses, which means `x & (1 == 0)`.

</details>
