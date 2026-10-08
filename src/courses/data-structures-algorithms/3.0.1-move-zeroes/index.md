---
lesson_name: "Warm-up: Move Zeroes"
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

### Warm-up: Move Zeroes

Write a function `move_zeroes(nums)` that moves every `0` in the list to the end **in place**, keeping the relative order of the non-zero numbers. The function doesn't need to return anything; the tests inspect `nums` after your function runs.

For example, `[0, 1, 0, 3, 12]` becomes `[1, 3, 12, 0, 0]`.

**Hint:** use the read/write two-pointer shape. `read` scans every element; `write` marks where the next non-zero value should go. After the scan, fill everything from `write` onward with zeros (or swap as you go).

---

### Tests

<ul>
<li id="test-1"><code>move_zeroes([0, 1, 0, 3, 12])</code> should change <code>nums</code> to <code>[1, 3, 12, 0, 0]</code></li>
<li id="test-2"><code>move_zeroes([0])</code> should change <code>nums</code> to <code>[0]</code></li>
<li id="test-3"><code>move_zeroes([1, 2, 3])</code> should change <code>nums</code> to <code>[1, 2, 3]</code></li>
<li id="test-4"><code>move_zeroes([0, 0, 1])</code> should change <code>nums</code> to <code>[1, 0, 0]</code></li>
<li id="test-5"><code>move_zeroes([4, 0, 5, 0, 0, 6])</code> should change <code>nums</code> to <code>[4, 5, 6, 0, 0, 0]</code></li>
<li id="test-6"><code>move_zeroes([])</code> should change <code>nums</code> to <code>[]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
```

Everything before `write` is the finished, non-zero part. When `read` finds a non-zero value, it's swapped into position `write`, which pushes a zero (if any) back towards `read`. Each element is visited once: `O(n)` time, `O(1)` space.

</details>
