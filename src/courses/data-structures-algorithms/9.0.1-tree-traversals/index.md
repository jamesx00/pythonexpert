---
lesson_name: "Warm-up: Preorder, Inorder & Postorder"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(h)
hints:
  - "All three orders visit the same nodes with the same recursion. What is the only thing that changes between them?"
  - "Use *Recursive DFS: trust the recursion* from *Trees Basics*: a helper `dfs(node)` that stops at `None`, recurses left and right, and appends `node.val` before (pre), between (in) or after (post) the two calls."
rich_test_results: true
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

**Brute force:** there isn't a slower way worth writing. Every traversal has to visit every node once, so `O(n)` is the floor.

**Key idea:** all three share one skeleton: stop at `None`, recurse left, recurse right. Moving the single `append` line changes the order. Remember it by where the **node** goes: **pre** = before the children, **in** = between them, **post** = after them.

**Why it's correct:** the recursion visits every node exactly once and always handles a node's whole left subtree before its whole right subtree. The position of `append` decides whether the node's value lands before, between or after those two blocks.

**Complexity:** `O(n)` time. `O(h)` extra space for the call stack, where `h` is the height of the tree: `O(log n)` when balanced, `O(n)` for a chain.

**Common mistakes:** creating `result = []` inside `dfs`, so each call gets its own list and the values are lost. Forgetting the `None` check, which raises `AttributeError` on the first missing child. Post-order is the one most "compute something from my children" problems use, so it's worth knowing well.

</details>
