---
lesson_name: Serialize and Deserialize Binary Tree
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

### Serialize and Deserialize Binary Tree

Implement two functions that are inverses of each other: `serialize(root)` should turn a binary tree into a single string, and `deserialize(data)` should take that string and rebuild the exact same tree structure (same shape, same values), returning its root.

You get to design the string format yourself — a common approach is a preorder walk that writes a placeholder (like `"#"`) for missing children, separated by commas, e.g. `"1,2,#,#,3,4,#,#,5,#,#"` for the tree built from `[1, 2, None, None, 3, 4, None, None, 5]`. As long as `deserialize(serialize(root))` always reproduces `root`'s exact structure, any format works.

---

### Tests

<ul>
<li id="test-1">for a tree built from <code>[1, 2, 3, None, None, 4, 5]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[1, 2, 3, None, None, 4, 5]</code></li>
<li id="test-2">for a tree built from <code>[]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[]</code></li>
<li id="test-3">for a tree built from <code>[1]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[1]</code></li>
<li id="test-4">for a tree built from <code>[1, 2]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[1, 2]</code></li>
<li id="test-5">for a tree built from <code>[5, 4, 7, 3, None, 2, None, -1, None, 9]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[5, 4, 7, 3, None, 2, None, -1, None, 9]</code></li>
<li id="test-6">for a tree built from <code>[1, None, 2, None, 3, None, 4]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[1, None, 2, None, 3, None, 4]</code></li>
</ul>
