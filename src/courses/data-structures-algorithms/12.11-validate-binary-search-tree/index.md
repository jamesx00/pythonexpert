---
lesson_name: Validate Binary Search Tree
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

### Validate Binary Search Tree

Write a function `is_valid_bst(root)` that returns `True` if the tree obeys the binary search tree property everywhere — every node's value must be strictly greater than all values in its left subtree and strictly less than all values in its right subtree — and `False` otherwise.

For example, `build_tree([5, 3, 8, 1, 4, 7, 9])` is a valid BST. But `build_tree([5, 1, 4, None, None, 3, 6])` is not, even though `5 > 1` and `5 < ` the right side look fine at a glance, because the node `3` sits under `5`'s right subtree yet is smaller than `5`, breaking the rule for the whole right side, not just the direct parent `4`.

---

### Tests

<ul>
<li id="test-1"><code>is_valid_bst(build_tree([5, 3, 8, 1, 4, 7, 9]))</code> should return <code>True</code></li>
<li id="test-2"><code>is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6]))</code> should return <code>False</code></li>
<li id="test-3"><code>is_valid_bst(build_tree([2, 1, 3]))</code> should return <code>True</code></li>
<li id="test-4"><code>is_valid_bst(build_tree([1, 1]))</code> should return <code>False</code></li>
<li id="test-5"><code>is_valid_bst(build_tree([]))</code> should return <code>True</code></li>
<li id="test-6"><code>is_valid_bst(build_tree([10, 5, 15, None, None, 6, 20]))</code> should return <code>False</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_valid_bst(root):
    def valid(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root, float('-inf'), float('inf'))
```

</details>
