---
lesson_name: Maximum Subarray
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

### Maximum Subarray

You're given a list of integers `nums` representing the daily change in a shop's revenue over a stretch of days (positive numbers mean the shop made more than the day before, negative numbers mean it made less). Write a function `max_subarray(nums)` that returns the largest possible sum of any contiguous run of days in `nums`.

`nums` always contains at least one number and can include negative values. For example, with `nums = [3, -2, 5, -1, 4]`, the best run is the whole list, giving a sum of `9`; but with `nums = [-3, 1, -8, 4, 6]`, the best run is just `[4, 6]`, giving `10`.

---

### Tests

<ul>
<li id="test-1"><code>max_subarray([3, -2, 5, -1, 4])</code> should return <code>9</code></li>
<li id="test-2"><code>max_subarray([-3, 1, -8, 4, 6])</code> should return <code>10</code></li>
<li id="test-3"><code>max_subarray([-5])</code> should return <code>-5</code></li>
<li id="test-4"><code>max_subarray([1, 2, 3, 4])</code> should return <code>10</code></li>
<li id="test-5"><code>max_subarray([-2, -1, -3, -4])</code> should return <code>-1</code></li>
<li id="test-6"><code>max_subarray([5, 4, -1, 7, 8])</code> should return <code>23</code></li>
<li id="test-7"><code>max_subarray([0, 0, 0, 3, -1])</code> should return <code>3</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_subarray(nums):
    max_sum = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        max_sum = max(max_sum, cur)
    return max_sum
```

</details>
