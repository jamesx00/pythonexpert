---
lesson_name: Two Sum on a Sorted Array
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

### Two Sum on a Sorted Array

You're given a list of integers that is already sorted from smallest to largest, along with a `target` value. Write a function that finds two different elements in the list that add up exactly to `target`, and returns their positions as a two-item list `[i, j]` with `i < j`. You may assume exactly one valid pair exists, and each element can only be used once.

For example, given `[1, 3, 4, 7, 11]` and a target of `10`, the values at positions `1` and `3` are `3` and `7`, which sum to `10`, so the function should return `[1, 3]`.

---

### Tests

<ul>
<li id="test-1"><code>two_sum_sorted([1, 3, 4, 7, 11], 10)</code> should return <code>[1, 3]</code></li>
<li id="test-2"><code>two_sum_sorted([-4, -1, 0, 3, 8], 4)</code> should return <code>[0, 4]</code></li>
<li id="test-3"><code>two_sum_sorted([2, 5], 7)</code> should return <code>[0, 1]</code></li>
<li id="test-4"><code>two_sum_sorted([1, 2, 3, 4, 6], 10)</code> should return <code>[3, 4]</code></li>
<li id="test-5"><code>two_sum_sorted([-6, -3, -1, 2, 9], -9)</code> should return <code>[0, 1]</code></li>
<li id="test-6"><code>two_sum_sorted([0, 0, 3, 5], 0)</code> should return <code>[0, 1]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return None
```

</details>
