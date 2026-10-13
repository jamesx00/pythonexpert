---
lesson_name: "Warm-up: Dynamic Array"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(1) amortized append, O(n) insert_front
  space: O(n)
hints:
  - "When the block is full, you have to copy everything into a bigger one. If the new block were only one slot bigger, how often would you copy? What if it were twice as big?"
  - "Follow *Dynamic Array* in *Build-It-Yourself Data Structures Basics*: write a `_resize(new_capacity)` helper that copies the items into `[None] * new_capacity`, and call it with `2 * self._capacity` when `self._size == self._capacity`. For `insert_front`, resize if needed, then shift items one slot right, starting from the **end**, and write the new value into slot `0`."
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

### Warm-up: Dynamic Array

Python's `list` is a **dynamic array**: a fixed-size block of memory plus a count of how many slots are in use. Build one yourself. The starter code stores the items in `self._data`, a plain list that you must treat as a fixed-size block: it always has exactly `self._capacity` slots, and you must not call `append` or `insert` on it.

Implement:

- `get(index)`: return the item at `index`. Raise `IndexError` if `index` is negative or `>= len(self)`.
- `append(value)`: add `value` at the end. If the block is full, first replace it with a block of **twice** the capacity and copy the items across.
- `insert_front(value)`: add `value` at the start, shifting every item one slot to the right. Resize first if the block is full.

A new array starts with capacity `1`, so after 1, 2, 3, 4 and 5 appends the capacity is `1`, `2`, `4`, `4` and `8`.

---

### Tests

<ul>
<li id="test-1">append 10, 20, 30, then <code>get(0)</code>, <code>get(1)</code>, <code>get(2)</code> should return <code>10</code>, <code>20</code>, <code>30</code></li>
<li id="test-2"><code>capacity()</code> after each of 5 appends should be <code>1</code>, <code>2</code>, <code>4</code>, <code>4</code>, <code>8</code></li>
<li id="test-3">after 5 appends, <code>len()</code> should be <code>5</code> and the block <code>_data</code> should have <code>8</code> slots</li>
<li id="test-4">append 2, 3, then <code>insert_front(1)</code>: <code>get(0..2)</code> should return <code>1</code>, <code>2</code>, <code>3</code> and <code>len()</code> should be <code>3</code></li>
<li id="test-5"><code>insert_front(&#x27;a&#x27;)</code> on an empty array, append <code>&#x27;b&#x27;</code>, <code>insert_front(&#x27;z&#x27;)</code>: <code>get(0..2)</code> should return <code>&#x27;z&#x27;</code>, <code>&#x27;a&#x27;</code>, <code>&#x27;b&#x27;</code>, and <code>capacity()</code> should be <code>4</code></li>
<li id="test-6">with 2 items, <code>get(2)</code> and <code>get(-1)</code> should both raise <code>IndexError</code></li>
<li id="test-7">Performance: 200,000 appends, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._data = [None] * self._capacity

    def __len__(self):
        return self._size

    def capacity(self):
        return self._capacity

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return self._data[index]

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def insert_front(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, 0, -1):
            self._data[i] = self._data[i - 1]
        self._data[0] = value
        self._size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
```

**Brute force:** when the block is full, grow it by **one** slot. Every append after the first then copies the whole array: `1 + 2 + … + (n - 1)` copies for `n` appends, which is `O(n²)` in total and `O(n)` per append.

**Bottleneck:** resizing on almost every append. The copying itself is unavoidable, but it shouldn't happen this often.

**Optimal idea:** grow by a constant **factor**: double the capacity. Resizes then happen only when the size reaches 1, 2, 4, 8, …, so they get rarer as the array grows.

**Why it's correct (and fast):** `_resize` copies the first `_size` slots in order, so every item keeps its index. Over `n` appends, the copies add up to `1 + 2 + 4 + … + n/2 < n`, plus `n` writes, so the whole sequence costs `O(n)`: `O(1)` **amortized** per append. `insert_front` shifts from the end (`i = _size` down to `1`) so that each item is moved into an empty slot before its old slot is overwritten.

**Complexity:** `get` is `O(1)`, because the slot is found directly by its index. `append` is `O(1)` amortized and `O(n)` in the worst case (a resize). `insert_front` is always `O(n)`, because every item moves: that's why `list.insert(0, x)` and `list.pop(0)` are slow. `O(n)` space, and at most half of the block is ever unused.

**Common mistakes:** growing by `+1` or `+10`, which makes append `O(n)` amortized. Shifting left to right in `insert_front`, which copies the first item into every slot. Forgetting to resize in `insert_front`. Checking `index > self._size` instead of `>=`, which returns an unused `None` slot. Allowing negative indexes, which silently read empty slots at the end of the block.

</details>
