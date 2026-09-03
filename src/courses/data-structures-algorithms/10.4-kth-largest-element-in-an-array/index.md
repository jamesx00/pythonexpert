---
lesson_name: Kth Largest Element in an Array
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

### Kth Largest Element in an Array

Write a function `find_kth_largest(nums, k)` that takes a fixed (non-streaming) list of integers and an integer `k`, and returns the k-th largest value in the list when the values are ranked from largest to smallest. Duplicates count separately by position, so if the same value appears twice it can occupy two consecutive ranks.

For example, given `nums = [7, 2, 9, 4, 9]` and `k = 2`, sorting from largest to smallest gives `[9, 9, 7, 4, 2]`, so the 2nd largest value is `9` (the duplicate at rank 2), and `find_kth_largest(nums, k)` returns `9`.

---

### Tests

<ul>
<li id="test-1"><code>find_kth_largest([7, 2, 9, 4, 9], 2)</code> should return <code>9</code></li>
<li id="test-2"><code>find_kth_largest([3, 1, 5, 12, 8, 2], 3)</code> should return <code>5</code></li>
<li id="test-3"><code>find_kth_largest([1], 1)</code> should return <code>1</code></li>
<li id="test-4"><code>find_kth_largest([2, 2, 2, 2], 3)</code> should return <code>2</code></li>
<li id="test-5"><code>find_kth_largest([-1, -5, -3, 0], 1)</code> should return <code>0</code></li>
<li id="test-6"><code>find_kth_largest([10, 20, 30, 40, 50], 5)</code> should return <code>10</code></li>
</ul>
