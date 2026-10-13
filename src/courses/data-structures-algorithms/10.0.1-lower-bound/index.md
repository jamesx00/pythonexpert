---
lesson_name: "Warm-up: Lower Bound"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(log n)
  space: O(1)
hints:
  - "Look at the middle element. If it's `>= target`, could the answer be further right than `mid`? Could it be `mid` itself?"
  - "Use template 2 in *Binary Search Basics*, *find the first position where a condition becomes true*: search `lo = 0`, `hi = len(nums)` with `while lo < hi`. If `nums[mid] >= target`, keep `mid` with `hi = mid`, otherwise `lo = mid + 1`."
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

### Warm-up: Lower Bound

Write a function `lower_bound(nums, target)` that takes a list sorted in ascending order and returns the **first index** `i` where `nums[i] >= target`. If every number is smaller than `target`, return `len(nums)`.

For example, `lower_bound([1, 3, 3, 5], 3)` returns `1`, and `lower_bound([1, 3, 3, 5], 4)` returns `3`. This is exactly where you'd insert `target` to keep the list sorted.

Don't use the `bisect` module. Write the binary search yourself, in `O(log n)`.

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
<li id="test-8">Performance: 20,000 searches in a 200,000-element list, within 1 second</li>
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

**Brute force:** scan from the left and return the first index with `nums[i] >= target`. That's `O(n)` per search.

**Bottleneck:** the scan ignores the ordering. One comparison with the middle element rules out half the list.

**Optimal idea:** binary search for the boundary between "smaller than `target`" and "`>= target`". The condition is false for a prefix of the list and true for the rest, so the boundary can be found by halving.

**Why it's correct:** the answer always stays in `[lo, hi]`. When `nums[mid] >= target`, `mid` could be the first such index, so `hi = mid` keeps it. Otherwise every index up to `mid` is too small, so `lo = mid + 1`. The range shrinks every step and stops when `lo == hi`, which is the answer. Starting `hi` at `len(nums)` covers the case where every value is smaller.

**Complexity:** `O(log n)` time, since the range halves each step. `O(1)` extra space.

**Common mistakes:** writing `hi = mid - 1` when `nums[mid] >= target`, which can skip the answer. Using `while lo <= hi` with `hi = mid`, which loops forever when `lo == hi`.

</details>
