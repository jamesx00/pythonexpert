---
lesson_name: Balanced Binary Tree
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

### Balanced Binary Tree

Write a function `is_balanced(root)` that returns `True` if the tree is height-balanced, meaning that for every node, the heights of its left and right subtrees differ by at most `1`. An empty tree counts as balanced.

For example, the tree built from `[3, 9, 20, None, None, 15, 7]` is balanced because at every node the two subtree heights never differ by more than one. A tree like `[1, 2, 2, 3, 3, None, None, 4, 4]`, where one branch keeps growing deeper than its sibling, is not.

---

### Tests

<ul>
<li id="test-1"><code>is_balanced(build_tree([3, 9, 20, None, None, 15, 7]))</code> should return <code>True</code></li>
<li id="test-2"><code>is_balanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4]))</code> should return <code>False</code></li>
<li id="test-3"><code>is_balanced(build_tree([]))</code> should return <code>True</code></li>
<li id="test-4"><code>is_balanced(build_tree([1]))</code> should return <code>True</code></li>
<li id="test-5"><code>is_balanced(build_tree([1, 2, None, 3, None, 4]))</code> should return <code>False</code></li>
<li id="test-6"><code>is_balanced(build_tree([1, 2, 3]))</code> should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1
```

</details>
