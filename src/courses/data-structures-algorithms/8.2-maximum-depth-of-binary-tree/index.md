---
lesson_name: Maximum Depth of Binary Tree
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

### Maximum Depth of Binary Tree

Write a function `max_depth(root)` that returns the number of nodes on the longest path from the root down to a leaf, counting the root itself as depth 1. An empty tree has depth `0`.

The tree is built for you with the `build_tree` helper from a level-order list. For example, `build_tree([3, 9, 20, None, None, 15, 7])` produces a tree whose longest root-to-leaf path is `3 -> 20 -> 15` (or `3 -> 20 -> 7`), so `max_depth` should return `3`.

---

### Tests

<ul>
<li id="test-1"><code>max_depth(build_tree([3, 9, 20, None, None, 15, 7]))</code> should return <code>3</code></li>
<li id="test-2"><code>max_depth(build_tree([]))</code> should return <code>0</code></li>
<li id="test-3"><code>max_depth(build_tree([1]))</code> should return <code>1</code></li>
<li id="test-4"><code>max_depth(build_tree([1, 2, None, 3, None, 4]))</code> should return <code>4</code></li>
<li id="test-5"><code>max_depth(build_tree([1, 2, 3, 4, 5, 6, 7]))</code> should return <code>3</code></li>
<li id="test-6"><code>max_depth(build_tree([1, None, 2, None, 3, None, 4]))</code> should return <code>4</code></li>
</ul>
