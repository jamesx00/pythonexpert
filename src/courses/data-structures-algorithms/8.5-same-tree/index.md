---
lesson_name: Same Tree
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

### Same Tree

Write a function `is_same_tree(p, q)` that returns `True` if two binary trees are structurally identical and every corresponding pair of nodes holds the same value, and `False` otherwise.

For example, `build_tree([1, 2, 3])` and `build_tree([1, 2, 3])` describe the same shape and the same values everywhere, so they're the same tree. But `build_tree([1, 2])` and `build_tree([1, None, 2])` are not — the `2` sits on the left in one and on the right in the other.

---

### Tests

<ul>
<li id="test-1"><code>is_same_tree(build_tree([1, 2, 3]), build_tree([1, 2, 3]))</code> should return <code>True</code></li>
<li id="test-2"><code>is_same_tree(build_tree([1, 2]), build_tree([1, None, 2]))</code> should return <code>False</code></li>
<li id="test-3"><code>is_same_tree(build_tree([1, 2, 1]), build_tree([1, 1, 2]))</code> should return <code>False</code></li>
<li id="test-4"><code>is_same_tree(build_tree([]), build_tree([]))</code> should return <code>True</code></li>
<li id="test-5"><code>is_same_tree(build_tree([1]), build_tree([]))</code> should return <code>False</code></li>
<li id="test-6"><code>is_same_tree(build_tree([5, 3, 8, 1, 4]), build_tree([5, 3, 8, 1, 4]))</code> should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
```

</details>
