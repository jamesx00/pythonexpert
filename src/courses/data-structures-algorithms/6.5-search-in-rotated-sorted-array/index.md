---
lesson_name: Search in Rotated Sorted Array
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(log n)
  space: O(1)
hints:
  - "Split the range at `mid`. Can both halves be unsorted, or is at least one of them always sorted?"
  - "One half is always sorted: the left half if `nums[lo] <= nums[mid]`, otherwise the right half. For the sorted half you can check whether `target` is inside it with two comparisons. Then adapt template 1 in *Binary Search Basics*."
  - "Template: if the left half is sorted and `nums[lo] <= target < nums[mid]`, search left (`hi = mid - 1`), otherwise search right. If the right half is sorted and `nums[mid] < target <= nums[hi]`, search right, otherwise search left."
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

### Search in Rotated Sorted Array

You're given a list of distinct integers that was sorted in ascending order and then rotated at some unknown pivot, along with a target value. Write a function that returns the index of the target in the list, or `-1` if it isn't present. As with a plain sorted list, your solution should run in `O(log n)` time.

For example, in `[30, 40, 50, 5, 10, 20]` (the sorted list `[5, 10, 20, 30, 40, 50]` rotated by three), searching for `10` should return `4`, and searching for `100` should return `-1`.

---

### Tests

<ul>
<li id="test-1"><code>search_rotated([30, 40, 50, 5, 10, 20], 10)</code> should return <code>4</code></li>
<li id="test-2"><code>search_rotated([30, 40, 50, 5, 10, 20], 100)</code> should return <code>-1</code></li>
<li id="test-3"><code>search_rotated([4, 5, 6, 7, 0, 1, 2], 0)</code> should return <code>4</code></li>
<li id="test-4"><code>search_rotated([4, 5, 6, 7, 0, 1, 2], 3)</code> should return <code>-1</code></li>
<li id="test-5"><code>search_rotated([1], 1)</code> should return <code>0</code></li>
<li id="test-6"><code>search_rotated([1], 0)</code> should return <code>-1</code></li>
<li id="test-7"><code>search_rotated([5, 1, 3], 5)</code> should return <code>0</code></li>
<li id="test-8"><code>search_rotated([1, 2, 3, 4, 5], 5)</code> should return <code>4</code></li>
<li id="test-9">Performance: 20,000 searches in a 200,000-element list, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

**Brute force:** `nums.index(target)`, or a scan. That's `O(n)`.

**Bottleneck:** the list is almost sorted, but a scan can't skip anything.

**Optimal idea:** at each step, one of the two halves around `mid` is sorted. Check whether `target` falls inside the sorted half's range. If it does, search there, and if not, search the other half.

**Why it's correct:** a rotated sorted list has at most one drop, so the drop is in at most one of the two halves, and the other half is sorted. A sorted half holds `target` exactly when `target` is between its first and last values, so that check decides correctly which half to keep. The target, if present, is never discarded.

**Complexity:** `O(log n)` time. `O(1)` extra space.

**Common mistakes:** using `<` instead of `<=` in `nums[lo] <= nums[mid]`. When `lo == mid` the left half is the single element `nums[lo]`, which is sorted. Getting the range checks' strict and non-strict ends wrong, which misses targets at the edges of a half, as in `search_rotated([5, 1, 3], 5)`.

</details>
