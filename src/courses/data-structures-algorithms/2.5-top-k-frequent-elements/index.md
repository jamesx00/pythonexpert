---
lesson_name: Top K Frequent Elements
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

### Top K Frequent Elements

Write a function `top_k_frequent(nums, k)` that takes a list of integers and an integer `k`, and returns a list of the `k` values that occur most often in `nums`. You may assume there is always a unique answer (no ties at the cutoff), and the order of the returned values does not matter.

For example, given `nums = [5, 5, 5, 1, 1, 9]` and `k = 2`, the value `5` appears three times and `1` appears twice, more often than `9`, so `top_k_frequent(nums, k)` should return `[5, 1]` (in either order).

---

### Tests

<ul>
<li id="test-1"><code>top_k_frequent([5, 5, 5, 1, 1, 9], 2)</code> should return <code>[5, 1]</code> (order does not matter)</li>
<li id="test-2"><code>top_k_frequent([1, 2, 2, 3, 3, 3], 1)</code> should return <code>[3]</code></li>
<li id="test-3"><code>top_k_frequent([4], 1)</code> should return <code>[4]</code></li>
<li id="test-4"><code>top_k_frequent([7, 7, 8, 8, 9, 9], 3)</code> should return <code>[7, 8, 9]</code> (order does not matter)</li>
<li id="test-5"><code>top_k_frequent([1, 1, 1, 2, 2, 3], 2)</code> should return <code>[1, 2]</code> (order does not matter)</li>
<li id="test-6"><code>top_k_frequent([-1, -1, 2, 3, 3], 2)</code> should return <code>[-1, 3]</code> (order does not matter)</li>
</ul>
