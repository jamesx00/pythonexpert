---
lesson_name: Find Minimum in Rotated Sorted Array
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(log n)
  space: O(1)
hints:
  - "Compare the middle element with the last element. What does it tell you about where the rotation point is?"
  - "If `nums[mid] > nums[hi]`, the drop to the minimum happens after `mid`. Otherwise `mid..hi` is sorted, so the minimum is at `mid` or before it. Use template 2 in *Binary Search Basics*."
  - "Template: `lo, hi = 0, len(nums) - 1`. While `lo < hi`, set `lo = mid + 1` if `nums[mid] > nums[hi]`, else `hi = mid`. Return `nums[lo]`."
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

### Find Minimum in Rotated Sorted Array

You're given a list of distinct integers that was originally sorted in ascending order, then rotated some unknown number of positions (possibly zero) — meaning a prefix of the sorted list was moved to the end. Write a function that returns the smallest value in the list. Solve it in `O(log n)` time rather than scanning every element.

For example, `[11, 15, 19, 2, 5, 8]` is `[2, 5, 8, 11, 15, 19]` rotated by three positions, so the minimum is `2`. A list that hasn't been rotated at all, like `[1, 2, 3, 4]`, should just return its first element, `1`.

---

### Tests

<ul>
<li id="test-1"><code>find_min([11, 15, 19, 2, 5, 8])</code> should return <code>2</code></li>
<li id="test-2"><code>find_min([1, 2, 3, 4])</code> should return <code>1</code></li>
<li id="test-3"><code>find_min([4, 1, 2, 3])</code> should return <code>1</code></li>
<li id="test-4"><code>find_min([3, 4, 1, 2])</code> should return <code>1</code></li>
<li id="test-5"><code>find_min([2, 3, 4, 1])</code> should return <code>1</code></li>
<li id="test-6"><code>find_min([9])</code> should return <code>9</code></li>
<li id="test-7"><code>find_min([2, 1])</code> should return <code>1</code></li>
<li id="test-8">Performance: 5,000 calls on a 200,000-element list, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def find_min(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]
```

**Brute force:** `min(nums)`, or a scan for the place where a value is smaller than the one before it. That's `O(n)`.

**Bottleneck:** the list is two sorted runs, and one comparison tells you which run `mid` is in, but a scan never uses that.

**Optimal idea:** compare `nums[mid]` with `nums[hi]`. If it's bigger, `mid` is in the left run and the minimum is to its right. Otherwise `mid` is in the right run, and the minimum is `mid` or something before it.

**Why it's correct:** the minimum is always inside `[lo, hi]`. If `nums[mid] > nums[hi]`, the values must drop somewhere after `mid`, and the minimum is where they drop, so `lo = mid + 1` keeps it. Otherwise `nums[mid..hi]` is sorted, so nothing after `mid` is smaller than `nums[mid]`, and `hi = mid` keeps it. The values are distinct, so one of the two cases always applies.

**Complexity:** `O(log n)` time. `O(1)` extra space.

**Common mistakes:** comparing with `nums[lo]` instead of `nums[hi]`, which fails on a list that isn't rotated, like `[1, 2, 3, 4]`. Setting `hi = mid - 1`, which can skip the minimum when it's at `mid`.

</details>
