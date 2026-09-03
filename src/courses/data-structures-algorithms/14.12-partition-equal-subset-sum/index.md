---
lesson_name: Partition Equal Subset Sum
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

### Partition Equal Subset Sum

Write a function `can_partition(nums)` that takes a list of positive integers and returns `True` if the list can be split into two subsets whose elements sum to the same total, or `False` if no such split exists. Every element must belong to exactly one of the two subsets.

For example, given `nums = [1, 5, 11, 5]`, splitting into `[1, 5, 5]` and `[11]` gives two subsets that both sum to `11`, so the function should return `True`.

---

### Tests

<ul>
<li id="test-1"><code>can_partition([1, 5, 11, 5])</code> should return <code>True</code></li>
<li id="test-2"><code>can_partition([1, 2, 3, 5])</code> should return <code>False</code></li>
<li id="test-3"><code>can_partition([1, 1])</code> should return <code>True</code></li>
<li id="test-4"><code>can_partition([1])</code> should return <code>False</code></li>
<li id="test-5"><code>can_partition([2, 2, 3, 5])</code> should return <code>False</code></li>
<li id="test-6"><code>can_partition([3, 3, 3, 4, 5])</code> should return <code>True</code></li>
<li id="test-7"><code>can_partition([2, 2, 2, 2, 3, 4, 5])</code> should return <code>True</code></li>
</ul>
