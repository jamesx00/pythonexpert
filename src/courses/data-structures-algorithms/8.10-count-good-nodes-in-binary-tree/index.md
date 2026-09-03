---
lesson_name: Count Good Nodes in Binary Tree
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

### Count Good Nodes in Binary Tree

A node in a binary tree is called "good" if, looking at the path from the root down to that node, no earlier node on the path has a value greater than the node's own value (the root itself is always good, since its path has nothing before it).

Write a function `good_nodes(root)` that returns how many good nodes the tree has. For example, in the tree built from `[3, 1, 4, 3, None, 1, 5]`, the root `3` is good, the left child `1` is not good (3 > 1), the right child `4` is good, and so on — counting carefully across the whole tree gives `4` good nodes.

---

### Tests

<ul>
<li id="test-1"><code>good_nodes(build_tree([3, 1, 4, 3, None, 1, 5]))</code> should return <code>4</code></li>
<li id="test-2"><code>good_nodes(build_tree([3, 3, None, 4, 2]))</code> should return <code>3</code></li>
<li id="test-3"><code>good_nodes(build_tree([1]))</code> should return <code>1</code></li>
<li id="test-4"><code>good_nodes(build_tree([]))</code> should return <code>0</code></li>
<li id="test-5"><code>good_nodes(build_tree([5, 4, 3, 2, 1]))</code> should return <code>1</code></li>
<li id="test-6"><code>good_nodes(build_tree([1, 2, 3, 4, 5, 6, 7]))</code> should return <code>7</code></li>
</ul>
