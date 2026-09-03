---
lesson_name: Lowest Common Ancestor of a BST
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

### Lowest Common Ancestor of a BST

Write a function `lowest_common_ancestor(root, p, q)` that takes the root of a binary **search** tree along with two nodes `p` and `q` that are guaranteed to exist somewhere in it, and returns the value of their lowest common ancestor — the deepest node that has both `p` and `q` in its subtree (a node counts as its own ancestor).

For example, in the BST built from `[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]`, the lowest common ancestor of the nodes with values `2` and `8` is `6`, since neither is a descendant of the other. The lowest common ancestor of `2` and `4` is `2` itself, since `4` sits inside `2`'s subtree.

---

### Tests

<ul>
<li id="test-1"><code>lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), node(2), node(8))</code> should return <code>6</code></li>
<li id="test-2"><code>lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), node(2), node(4))</code> should return <code>2</code></li>
<li id="test-3"><code>lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), node(3), node(5))</code> should return <code>4</code></li>
<li id="test-4"><code>lowest_common_ancestor(build_tree([2, 1]), node(2), node(1))</code> should return <code>2</code></li>
<li id="test-5"><code>lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), node(7), node(9))</code> should return <code>8</code></li>
<li id="test-6"><code>lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), node(0), node(5))</code> should return <code>2</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def lowest_common_ancestor(root, p, q):
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
```

</details>
