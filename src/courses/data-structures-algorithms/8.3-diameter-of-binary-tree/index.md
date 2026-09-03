---
lesson_name: Diameter of Binary Tree
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

### Diameter of Binary Tree

Write a function `diameter_of_binary_tree(root)` that returns the length (in edges, not nodes) of the longest path between any two nodes in the tree. That path may or may not pass through the root.

For example, in the tree built from `[1, 2, 3, 4, 5]`, the longest path runs `4 -> 2 -> 1 -> 3` or `5 -> 2 -> 1 -> 3`, which crosses 3 edges, so `diameter_of_binary_tree` should return `3`.

---

### Tests

<ul>
<li id="test-1"><code>diameter_of_binary_tree(build_tree([1, 2, 3, 4, 5]))</code> should return <code>3</code></li>
<li id="test-2"><code>diameter_of_binary_tree(build_tree([1, 2]))</code> should return <code>1</code></li>
<li id="test-3"><code>diameter_of_binary_tree(build_tree([]))</code> should return <code>0</code></li>
<li id="test-4"><code>diameter_of_binary_tree(build_tree([1]))</code> should return <code>0</code></li>
<li id="test-5"><code>diameter_of_binary_tree(build_tree([1, 2, None, 3, None, 4, None, 5]))</code> should return <code>4</code></li>
<li id="test-6"><code>diameter_of_binary_tree(build_tree([1, None, 2, None, 3]))</code> should return <code>2</code></li>
</ul>
