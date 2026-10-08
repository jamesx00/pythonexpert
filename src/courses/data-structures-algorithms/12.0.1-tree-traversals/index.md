---
lesson_name: "Warm-up: Preorder, Inorder & Postorder"
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

### Warm-up: Preorder, Inorder & Postorder

Depth-first traversals of a binary tree differ only in **when** you visit the node relative to its children:

- **Preorder:** node, then left subtree, then right subtree.
- **Inorder:** left subtree, then node, then right subtree. On a binary search tree this visits values in sorted order.
- **Postorder:** left subtree, then right subtree, then node.

Write three functions, `preorder(root)`, `inorder(root)` and `postorder(root)`, that each return a list of node values in that order. An empty tree returns `[]`.

For the tree built from `[1, 2, 3, 4, 5]`:

```
    1
   / \
  2   3
 / \
4   5
```

preorder is `[1, 2, 4, 5, 3]`, inorder is `[4, 2, 5, 1, 3]`, and postorder is `[4, 5, 2, 3, 1]`.

**Hint:** write a recursive helper that appends to a shared `result` list. The three functions differ only in where the `append` line goes.

---

### Tests

<ul>
<li id="test-1"><code>preorder([1, 2, 3, 4, 5])</code> should return <code>[1, 2, 4, 5, 3]</code></li>
<li id="test-2"><code>inorder([1, 2, 3, 4, 5])</code> should return <code>[4, 2, 5, 1, 3]</code></li>
<li id="test-3"><code>postorder([1, 2, 3, 4, 5])</code> should return <code>[4, 5, 2, 3, 1]</code></li>
<li id="test-4"><code>inorder([4, 2, 6, 1, 3, 5, 7])</code> should return <code>[1, 2, 3, 4, 5, 6, 7]</code></li>
<li id="test-5"><code>preorder([])</code> should return <code>[]</code></li>
<li id="test-6"><code>postorder([1, None, 2, None, 3])</code> should return <code>[3, 2, 1]</code></li>
<li id="test-7"><code>inorder([1, None, 2, 3])</code> should return <code>[1, 3, 2]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def preorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result


def inorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result


def postorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(root)
    return result
```

All three share the same skeleton: stop at `None`, recurse left, recurse right. Moving the single `append` line changes the order. Remember the pattern by where the **node** goes: **pre** = before the children, **in** = between them, **post** = after them. Post-order is what most "compute something from my children" problems use.

</details>
