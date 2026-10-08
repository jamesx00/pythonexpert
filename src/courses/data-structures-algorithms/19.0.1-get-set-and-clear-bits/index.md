---
lesson_name: "Warm-up: Get, Set & Clear Bits"
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

### Warm-up: Get, Set & Clear Bits

Bits are numbered from the right, starting at `0`. For example, `5` is `0b101`: bits `0` and `2` are `1`, and bit `1` is `0`.

Write three functions:

- `get_bit(x, i)`: return `1` if bit `i` of `x` is set, otherwise `0`.
- `set_bit(x, i)`: return `x` with bit `i` turned **on**.
- `clear_bit(x, i)`: return `x` with bit `i` turned **off**.

For example, `get_bit(5, 1)` is `0`, `set_bit(5, 1)` is `7` (`0b111`), and `clear_bit(5, 0)` is `4` (`0b100`).

**Hint:** `1 << i` builds a **mask** with only bit `i` set. Combine it with `&` (test), `|` (turn on) or `& ~` (turn off). Shifting `x` right by `i` moves bit `i` into position `0`.

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

`(x >> i) & 1` slides bit `i` to the end and masks off everything else. OR-ing with the mask forces that bit to `1`. AND-ing with the **inverted** mask (`~(1 << i)` has every bit set except bit `i`) forces it to `0` and leaves the others alone. Setting a bit that's already on, or clearing one that's already off, leaves `x` unchanged. These three one-liners are the building blocks of every problem in this section.

</details>
