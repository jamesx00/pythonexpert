---
lesson_name: Two Sum
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

### Two Sum

Write a function `two_sum(nums, target)` that takes a list of integers and a target integer, and returns the indices of the two elements that add up to `target`, as a list `[i, j]`. Assume every input has exactly one valid pair, and you cannot use the same element twice.

For example, given `nums = [3, 5, -4, 8]` and `target = 4`, the values `-4` and `8` add up to `4`, so `two_sum(nums, target)` should return `[2, 3]`. The order of the returned indices does not matter, and there is always exactly one pair of numbers that add up to the target.

---

### Tests

<ul>
<li id="test-1"><code>two_sum([3, 5, -4, 8], 4)</code> should return <code>[2, 3]</code></li>
<li id="test-2"><code>two_sum([2, 7, 11, 15], 9)</code> should return <code>[0, 1]</code></li>
<li id="test-3"><code>two_sum([3, 2, 4], 6)</code> should return <code>[1, 2]</code></li>
<li id="test-4"><code>two_sum([1, 5, 5, 2], 10)</code> should return <code>[1, 2]</code></li>
<li id="test-5"><code>two_sum([-3, 4, 3, 90], 0)</code> should return <code>[0, 2]</code></li>
<li id="test-6"><code>two_sum([0, 4, 3, 0], 0)</code> should return <code>[0, 3]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []
```

</details>
