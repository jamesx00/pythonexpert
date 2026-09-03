---
lesson_name: Binary Tree Right Side View
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

### Binary Tree Right Side View

Write a function `right_side_view(root)` that returns the list of node values you would see if you stood to the right of the tree and looked at it edge-on — one value per depth level, taken from the rightmost node at that level, ordered top to bottom.

For example, the tree built from `[1, 2, 3, None, 5, None, 4]` looks like `1` on top, `2` and `3` below it, then `5` under `2` and `4` under `3`. Standing on the right you'd see `1`, then `3`, then `4`, so `right_side_view` should return `[1, 3, 4]`.

---

### Tests

<ul>
<li id="test-1"><code>right_side_view(build_tree([1, 2, 3, None, 5, None, 4]))</code> should return <code>[1, 3, 4]</code></li>
<li id="test-2"><code>right_side_view(build_tree([1, None, 3]))</code> should return <code>[1, 3]</code></li>
<li id="test-3"><code>right_side_view(build_tree([]))</code> should return <code>[]</code></li>
<li id="test-4"><code>right_side_view(build_tree([1]))</code> should return <code>[1]</code></li>
<li id="test-5"><code>right_side_view(build_tree([1, 2, 3, 4]))</code> should return <code>[1, 3, 4]</code></li>
<li id="test-6"><code>right_side_view(build_tree([1, 2, 3, 4, None, None, 5]))</code> should return <code>[1, 3, 5]</code></li>
</ul>
