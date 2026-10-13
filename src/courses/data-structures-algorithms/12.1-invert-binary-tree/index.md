---
lesson_name: Invert Binary Tree
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(h)
hints:
  - "If the left and right subtrees were already inverted, what would be left to do at the root?"
  - "Use *Recursive DFS: trust the recursion* from *Trees Basics*: invert both subtrees, then swap them."
  - "Template: if `root is None`, return `None`. `root.left, root.right = invert_tree(root.right), invert_tree(root.left)`. Return `root`."
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

### Invert Binary Tree

Write a function `invert_tree(root)` that mirrors a binary tree: at every node, swap its left and right children, and return the root of the mirrored tree.

The tree is given to you already built from a `TreeNode` (`val`, `left`, `right`) via the `build_tree` helper, which reads a level-order list where `None` marks a missing child. For example, the tree built from `[4, 2, 7, 1, 3, 6, 9]` looks like:

```
        4
      /   \
     2     7
    / \   / \
   1   3 6   9
```

After inverting it, walking the result level-order should produce `[4, 7, 2, 9, 6, 3, 1]` — every left/right pair has been swapped, all the way down.

---

### Tests

<ul>
<li id="test-1"><code>invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))</code> should mirror to <code>[4, 7, 2, 9, 6, 3, 1]</code></li>
<li id="test-2"><code>invert_tree(build_tree([1, 2]))</code> should mirror to <code>[1, None, 2]</code></li>
<li id="test-3"><code>invert_tree(build_tree([1, None, 2]))</code> should mirror to <code>[1, 2]</code></li>
<li id="test-4"><code>invert_tree(build_tree([]))</code> should mirror to <code>[]</code></li>
<li id="test-5"><code>invert_tree(build_tree([5]))</code> should mirror to <code>[5]</code></li>
<li id="test-6"><code>invert_tree(build_tree([3, 9, 20, None, None, 15, 7]))</code> should mirror to <code>[3, 20, 9, 7, 15]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

**Brute force:** read the tree into a level-order list, reverse each level, and build a new tree. That's `O(n)` time but `O(n)` extra space, and it builds new nodes instead of mirroring the given tree.

**Bottleneck:** the copy only exists because swapping "all the way down" sounds like it needs a view of the whole tree.

**Optimal idea:** mirroring is local. At every node, swap its two children, and do the same inside each child.

**Why it's correct:** by induction on the height. An empty tree is its own mirror. For any other node, the recursive calls return the mirrored subtrees, and putting the mirrored right subtree on the left (and the other way round) mirrors the whole tree.

**Complexity:** `O(n)` time, each node is swapped once. `O(h)` extra space for the call stack.

**Common mistakes:** writing `root.left = invert_tree(root.right)` and then `root.right = invert_tree(root.left)` on two lines: the second line reads the *new* left child, so both sides end up the same. The one-line tuple assignment evaluates both calls first. Forgetting to `return root`.

</details>
