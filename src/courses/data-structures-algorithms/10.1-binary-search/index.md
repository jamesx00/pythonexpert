---
lesson_name: Binary Search
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(log n)
  space: O(1)
hints:
  - "Compare `target` with the middle element. Which half of the list can you throw away?"
  - "Use template 1 in *Binary Search Basics*, *find an exact value*: keep a range `lo..hi`, look at `mid`, and move `lo` or `hi` past `mid` depending on which side `target` must be on."
  - "Template: `lo, hi = 0, len(nums) - 1`. While `lo <= hi`, return `mid` on a match, set `lo = mid + 1` if `nums[mid] < target`, otherwise `hi = mid - 1`. Return `-1` after the loop."
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

### Binary Search

Write a function that takes a list of integers sorted in ascending order and a target value, and returns the index of the target if it appears in the list. If the target isn't present, return `-1`. Your function must run in `O(log n)` time, so scanning the whole list one element at a time won't cut it — you need to repeatedly cut the search range in half.

For example, searching for `9` in `[-4, 0, 3, 9, 14, 22]` should return `3`, since `9` sits at index `3`. Searching for `10` in the same list should return `-1`, since `10` never appears.

---

### Tests

<ul>
<li id="test-1"><code>binary_search([-4, 0, 3, 9, 14, 22], 9)</code> should return <code>3</code></li>
<li id="test-2"><code>binary_search([-4, 0, 3, 9, 14, 22], 10)</code> should return <code>-1</code></li>
<li id="test-3"><code>binary_search([1, 2, 3, 4, 5], 1)</code> should return <code>0</code></li>
<li id="test-4"><code>binary_search([1, 2, 3, 4, 5], 5)</code> should return <code>4</code></li>
<li id="test-5"><code>binary_search([], 5)</code> should return <code>-1</code></li>
<li id="test-6"><code>binary_search([7], 7)</code> should return <code>0</code></li>
<li id="test-7"><code>binary_search([7], 3)</code> should return <code>-1</code></li>
<li id="test-8"><code>binary_search([2, 4, 6, 8, 10, 12, 14], 12)</code> should return <code>5</code></li>
<li id="test-9">Performance: 20,000 searches in a 200,000-element list, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Brute force:** check every element, or use `nums.index(target)`. That's `O(n)` per search, and it doesn't use the fact that the list is sorted.

**Bottleneck:** each comparison in a linear scan rules out a single element, but in a sorted list one comparison with the middle can rule out half.

**Optimal idea:** compare `target` with the middle of the remaining range. If it's bigger, it can only be to the right, and if it's smaller, only to the left.

**Why it's correct:** if `target` is in the list, it's always inside `[lo, hi]`, because each step only drops elements that are too small or too big. The range shrinks every step, so the loop ends either at the target or with an empty range, meaning `target` isn't there.

**Complexity:** `O(log n)` time, since the range halves each step. `O(1)` extra space.

**Common mistakes:** `while lo < hi`, which misses a target in a one-element range, as in `binary_search([7], 7)`. Setting `lo = mid` or `hi = mid` in this template, which can loop forever.

</details>
