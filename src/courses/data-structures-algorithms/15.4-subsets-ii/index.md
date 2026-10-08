---
lesson_name: Subsets II
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

### Subsets II

Write a function `subsets_with_dup(nums)` that takes a list of integers which may contain duplicate values, and returns every distinct subset of that list (including the empty subset and the full list). Even though the same value can appear more than once in `nums`, no two subsets in the result should contain the exact same multiset of values. The order of the subsets and the order of elements within each subset do not matter.

For example, given `[1, 2, 2]`, the subsets `[2]` picked from either copy of `2` are the same subset and must only appear once, so a valid return value is `[[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]`.

---

### Tests

<ul>
<li id="test-1"><code>subsets_with_dup([1, 2, 2])</code> should return <code>[[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]</code> (any order)</li>
<li id="test-2"><code>subsets_with_dup([0])</code> should return <code>[[], [0]]</code></li>
<li id="test-3"><code>subsets_with_dup([])</code> should return <code>[[]]</code></li>
<li id="test-4"><code>subsets_with_dup([4, 4, 4])</code> should return <code>[[], [4], [4, 4], [4, 4, 4]]</code> (any order)</li>
<li id="test-5"><code>subsets_with_dup([1, 2, 3])</code> should return all 8 subsets of <code>[1, 2, 3]</code> (any order)</li>
<li id="test-6"><code>subsets_with_dup([2, 1, 2, 1])</code> should return <code>[[], [1], [2], [1, 1], [1, 2], [2, 2], [1, 1, 2], [1, 2, 2], [1, 1, 2, 2]]</code> (any order)</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def subsets_with_dup(nums):
    nums = sorted(nums)
    result = []

    def backtrack(start, path):
        result.append(list(path))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

</details>
