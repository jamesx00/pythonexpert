---
lesson_name: Construct Binary Tree from Preorder and Inorder Traversal
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

### Construct Binary Tree from Preorder and Inorder Traversal

Write a function `build_tree_from_traversals(preorder, inorder)` that rebuilds a binary tree given its preorder traversal (root, then left subtree, then right subtree) and its inorder traversal (left subtree, then root, then right subtree), both as lists of unique values, and returns the root `TreeNode`.

For example, `preorder = [3, 9, 20, 15, 7]` and `inorder = [9, 3, 15, 20, 7]` describe a tree whose root is `3` (the first preorder value), with `9` alone on the left (everything before `3` in the inorder list) and `20`, `15`, `7` on the right (everything after `3` in the inorder list) — which reconstructs the same tree you'd get from `build_tree([3, 9, 20, None, None, 15, 7])`.

---

### Tests

<ul>
<li id="test-1"><code>build_tree_from_traversals([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])</code> should rebuild to <code>[3, 9, 20, None, None, 15, 7]</code></li>
<li id="test-2"><code>build_tree_from_traversals([-1], [-1])</code> should rebuild to <code>[-1]</code></li>
<li id="test-3"><code>build_tree_from_traversals([], [])</code> should rebuild to <code>[]</code></li>
<li id="test-4"><code>build_tree_from_traversals([1, 2, 3], [3, 2, 1])</code> should rebuild to <code>[1, 2, None, 3]</code></li>
<li id="test-5"><code>build_tree_from_traversals([1, 2, 3], [1, 2, 3])</code> should rebuild to <code>[1, None, 2, None, 3]</code></li>
<li id="test-6"><code>build_tree_from_traversals([5, 3, 1, 4, 8, 7, 9], [1, 3, 4, 5, 7, 8, 9])</code> should rebuild to <code>[5, 3, 8, 1, 4, 7, 9]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def build_tree_from_traversals(preorder, inorder):
    if not preorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    idx = inorder.index(root_val)
    left_inorder = inorder[:idx]
    right_inorder = inorder[idx + 1:]
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]
    root.left = build_tree_from_traversals(left_preorder, left_inorder)
    root.right = build_tree_from_traversals(right_preorder, right_inorder)
    return root
```

</details>
