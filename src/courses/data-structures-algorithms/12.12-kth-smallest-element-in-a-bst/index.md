---
lesson_name: Kth Smallest Element in a BST
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

### Kth Smallest Element in a BST

Write a function `kth_smallest(root, k)` that returns the `k`-th smallest value stored in a binary search tree, where `k` is `1`-based (`k=1` means the smallest value in the tree).

For example, in the BST built from `[5, 3, 8, 2, 4, 7, 9]`, the values in sorted order are `2, 3, 4, 5, 7, 8, 9`, so `kth_smallest(root, 3)` should return `4`.

---

### Tests

<ul>
<li id="test-1"><code>kth_smallest(build_tree([5, 3, 8, 2, 4, 7, 9]), 3)</code> should return <code>4</code></li>
<li id="test-2"><code>kth_smallest(build_tree([5, 3, 8, 2, 4, 7, 9]), 1)</code> should return <code>2</code></li>
<li id="test-3"><code>kth_smallest(build_tree([5, 3, 8, 2, 4, 7, 9]), 7)</code> should return <code>9</code></li>
<li id="test-4"><code>kth_smallest(build_tree([3, 1, 4, None, 2]), 1)</code> should return <code>1</code></li>
<li id="test-5"><code>kth_smallest(build_tree([3, 1, 4, None, 2]), 4)</code> should return <code>4</code></li>
<li id="test-6"><code>kth_smallest(build_tree([1]), 1)</code> should return <code>1</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def kth_smallest(root, k):
    order = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        order.append(node.val)
        inorder(node.right)

    inorder(root)
    return order[k - 1]
```

</details>
