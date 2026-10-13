---
lesson_name: "Warm-up: Move Zeroes"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "If you only had to keep the non-zero values in order, where would the next one you find need to go?"
  - "Use the read/write shape (shape 2 in *Two Pointers Basics*): `read` scans every element, and `write` marks where the next non-zero value belongs. Swap each non-zero value into position `write`."
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

### Warm-up: Move Zeroes

Write a function `move_zeroes(nums)` that moves every `0` in the list to the end **in place**, keeping the relative order of the non-zero numbers. The function doesn't need to return anything; the tests inspect `nums` after your function runs.

For example, `[0, 1, 0, 3, 12]` becomes `[1, 3, 12, 0, 0]`.

---

### Tests

<ul>
<li id="test-1"><code>move_zeroes([0, 1, 0, 3, 12])</code> should change <code>nums</code> to <code>[1, 3, 12, 0, 0]</code></li>
<li id="test-2"><code>move_zeroes([0])</code> should change <code>nums</code> to <code>[0]</code></li>
<li id="test-3"><code>move_zeroes([1, 2, 3])</code> should change <code>nums</code> to <code>[1, 2, 3]</code></li>
<li id="test-4"><code>move_zeroes([0, 0, 1])</code> should change <code>nums</code> to <code>[1, 0, 0]</code></li>
<li id="test-5"><code>move_zeroes([4, 0, 5, 0, 0, 6])</code> should change <code>nums</code> to <code>[4, 5, 6, 0, 0, 0]</code></li>
<li id="test-6"><code>move_zeroes([])</code> should change <code>nums</code> to <code>[]</code></li>
<li id="test-7">Performance: 200,000 elements, half of them zeros, within 1 second</li>
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

**Brute force:** for every zero, `nums.remove(0)` and then `nums.append(0)`. Each `remove` shifts the rest of the list left, so this is `O(n²)` when there are many zeros.

**Bottleneck:** each zero is moved one step at a time by shifting everything after it, and the same elements get shifted over and over.

**Optimal idea:** keep a `write` index for the next slot a non-zero value belongs in. When `read` finds a non-zero value, swap it into `write` and advance `write`.

**Why it's correct:** everything before `write` is the non-zero values seen so far, in their original order, and everything from `write` to `read` is zeros. Each swap keeps both of these true, so when `read` reaches the end, all zeros sit after `write`.

**Complexity:** `O(n)` time, one pass with a constant-time swap per element. `O(1)` extra space.

**Common mistakes:** building a new list and returning it. The tests check `nums` itself, so the change has to happen in place (`nums[:] = ...` would work, but uses `O(n)` extra space).

</details>
