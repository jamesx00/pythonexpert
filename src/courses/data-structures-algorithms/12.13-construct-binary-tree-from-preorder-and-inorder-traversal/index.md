---
lesson_name: Construct Binary Tree from Preorder and Inorder Traversal
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "Which value in `preorder` is the root? Where does that value split `inorder`?"
  - "Use *Recursive DFS: trust the recursion* from *Trees Basics*: the first preorder value is the root, everything before it in `inorder` is the left subtree, everything after is the right. Build each side the same way."
  - "Template: `index = {val: i for i, val in enumerate(inorder)}`, `next_root = iter(preorder)`. `build(lo, hi)`: `None` if `lo > hi`; `root = TreeNode(next(next_root))`; `mid = index[root.val]`; build left from `(lo, mid - 1)`, then right from `(mid + 1, hi)`."
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
    index = {val: i for i, val in enumerate(inorder)}
    next_root = iter(preorder)

    def build(lo, hi):
        if lo > hi:
            return None
        root = TreeNode(next(next_root))
        mid = index[root.val]
        root.left = build(lo, mid - 1)
        root.right = build(mid + 1, hi)
        return root

    return build(0, len(inorder) - 1)
```

**Brute force:** take `preorder[0]` as the root, find it with `inorder.index(...)`, slice both lists into left and right parts, and recurse on the slices. Each call searches and copies its whole range, so a chain-shaped tree takes `O(n^2)` time.

**Bottleneck:** the linear `index` search and the list slices at every level.

**Optimal idea:** look up each value's inorder position in a dictionary built once, and pass index bounds instead of slices. Preorder lists roots in the order you create them (root, then the whole left subtree, then the right), so one iterator over it is enough, as long as you build the left subtree before the right.

**Why it's correct:** in preorder the root comes first. In inorder, the root splits the values into the left subtree (before it) and the right subtree (after it). Values are unique, so the dictionary gives the split point. Each subtree is again a preorder/inorder pair, so the same rule rebuilds it.

**Complexity:** `O(n)` time: one dictionary build and `O(1)` work per node. `O(n)` extra space for the dictionary, plus `O(h)` for the call stack.

**Common mistakes:** building the right subtree before the left, which takes the wrong values off the preorder iterator. Off-by-one bounds, such as `build(lo, mid)` for the left side. The slicing version is fine for small inputs but copies lists at every level.

</details>
