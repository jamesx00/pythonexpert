---
lesson_name: Subsets
section: Backtracking
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

### Subsets

Write a function `subsets(nums)` that takes a list of distinct integers and returns every possible subset of that list, including the empty subset and the list itself. The result should be a list of lists, and neither the order of the subsets nor the order of elements within a subset needs to match any particular arrangement.

For example, given `[1, 2, 3]`, a valid return value would be `[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]` — eight subsets in total, since a set of 3 distinct elements has 2³ possible subsets.

---

### Tests

<ul>
<li id="test-1"><code>subsets([1, 2, 3])</code> should return all 8 subsets of <code>[1, 2, 3]</code> (any order)</li>
<li id="test-2"><code>subsets([])</code> should return <code>[[]]</code></li>
<li id="test-3"><code>subsets([5])</code> should return <code>[[], [5]]</code> (any order)</li>
<li id="test-4"><code>subsets([4, 7])</code> should return all 4 subsets of <code>[4, 7]</code> (any order)</li>
<li id="test-5"><code>subsets([0, -1])</code> should return all 4 subsets of <code>[0, -1]</code> (any order)</li>
<li id="test-6"><code>subsets([1, 2, 3, 4])</code> should return all 16 subsets of <code>[1, 2, 3, 4]</code> (any order)</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def subsets(nums):
    result = [[]]
    for n in nums:
        result += [subset + [n] for subset in result]
    return result
```

</details>
