---
lesson_name: Invert Binary Tree
code_editor: True
code_execution: True
adding_file_allowed: False
section: Trees
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

### Invert Binary Tree

Write a function `invert_tree(root)` that mirrors a binary tree: at every node, swap its left and right children, and return the root of the mirrored tree.

The tree is given to you already built from a `TreeNode` (`val`, `left`, `right`) via the `build_tree` helper, which reads a level-order list where `None` marks a missing child. For example, the tree built from `[4, 2, 7, 1, 3, 6, 9]` looks like:

```
        4
      /   \
     2     7
    / \   / \
   1   3 6   9
```

After inverting it, walking the result level-order should produce `[4, 7, 2, 9, 6, 3, 1]` — every left/right pair has been swapped, all the way down.

---

### Tests

<ul>
<li id="test-1"><code>invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))</code> should mirror to <code>[4, 7, 2, 9, 6, 3, 1]</code></li>
<li id="test-2"><code>invert_tree(build_tree([1, 2]))</code> should mirror to <code>[1, None, 2]</code></li>
<li id="test-3"><code>invert_tree(build_tree([1, None, 2]))</code> should mirror to <code>[1, 2]</code></li>
<li id="test-4"><code>invert_tree(build_tree([]))</code> should mirror to <code>[]</code></li>
<li id="test-5"><code>invert_tree(build_tree([5]))</code> should mirror to <code>[5]</code></li>
<li id="test-6"><code>invert_tree(build_tree([3, 9, 20, None, None, 15, 7]))</code> should mirror to <code>[3, 20, 9, 7, 15]</code></li>
</ul>
