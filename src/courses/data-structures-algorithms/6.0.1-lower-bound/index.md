---
lesson_name: "Warm-up: Lower Bound"
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

### Warm-up: Lower Bound

Write a function `lower_bound(nums, target)` that takes a list sorted in ascending order and returns the **first index** `i` where `nums[i] >= target`. If every number is smaller than `target`, return `len(nums)`.

For example, `lower_bound([1, 3, 3, 5], 3)` returns `1`, and `lower_bound([1, 3, 3, 5], 4)` returns `3`. This is exactly where you'd insert `target` to keep the list sorted.

Don't use the `bisect` module. Write the binary search yourself, in `O(log n)`.

**Hint:** search the range `lo = 0`, `hi = len(nums)` with `while lo < hi`. If `nums[mid] >= target`, `mid` could be the answer, so keep it with `hi = mid`. Otherwise the answer is to the right: `lo = mid + 1`.

---

### Tests

<ul>
<li id="test-1"><code>lower_bound([1, 3, 3, 5], 3)</code> should return <code>1</code></li>
<li id="test-2"><code>lower_bound([1, 3, 3, 5], 4)</code> should return <code>3</code></li>
<li id="test-3"><code>lower_bound([1, 3, 3, 5], 0)</code> should return <code>0</code></li>
<li id="test-4"><code>lower_bound([1, 3, 3, 5], 9)</code> should return <code>4</code></li>
<li id="test-5"><code>lower_bound([], 5)</code> should return <code>0</code></li>
<li id="test-6"><code>lower_bound([2, 2, 2, 2], 2)</code> should return <code>0</code></li>
<li id="test-7"><code>lower_bound([1, 2, 4, 8, 16, 32, 64], 17)</code> should return <code>5</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

The loop keeps one invariant: the answer is always inside `[lo, hi]`. Starting `hi` at `len(nums)` (not `len(nums) - 1`) allows the answer "past the end". The range shrinks every step, and the loop ends when `lo == hi`, which is the answer.

</details>
