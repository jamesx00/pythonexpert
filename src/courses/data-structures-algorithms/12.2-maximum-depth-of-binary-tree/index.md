---
lesson_name: Maximum Depth of Binary Tree
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(h)
hints:
  - "If you knew the depth of the left and right subtrees, how would you get the depth of the whole tree?"
  - "Use *Recursive DFS: trust the recursion* from *Trees Basics*: the depth of a tree is `1` for the root plus the deeper of its two subtrees."
  - "Template: if `root is None`, return `0`. Return `1 + max(max_depth(root.left), max_depth(root.right))`."
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

### Maximum Depth of Binary Tree

Write a function `max_depth(root)` that returns the number of nodes on the longest path from the root down to a leaf, counting the root itself as depth 1. An empty tree has depth `0`.

The tree is built for you with the `build_tree` helper from a level-order list. For example, `build_tree([3, 9, 20, None, None, 15, 7])` produces a tree whose longest root-to-leaf path is `3 -> 20 -> 15` (or `3 -> 20 -> 7`), so `max_depth` should return `3`.

---

### Tests

<ul>
<li id="test-1"><code>max_depth(build_tree([3, 9, 20, None, None, 15, 7]))</code> should return <code>3</code></li>
<li id="test-2"><code>max_depth(build_tree([]))</code> should return <code>0</code></li>
<li id="test-3"><code>max_depth(build_tree([1]))</code> should return <code>1</code></li>
<li id="test-4"><code>max_depth(build_tree([1, 2, None, 3, None, 4]))</code> should return <code>4</code></li>
<li id="test-5"><code>max_depth(build_tree([1, 2, 3, 4, 5, 6, 7]))</code> should return <code>3</code></li>
<li id="test-6"><code>max_depth(build_tree([1, None, 2, None, 3, None, 4]))</code> should return <code>4</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Brute force:** list every root-to-leaf path and take the longest. Copying the paths costs up to `O(n * h)` time and space.

**Bottleneck:** the paths share most of their nodes, so building each one from scratch repeats work.

**Optimal idea:** let each subtree report only its depth. The parent needs nothing else.

**Why it's correct:** the longest path from the root goes through the root and then down one of its subtrees, so its length is `1` plus the larger subtree depth. An empty tree has depth `0`, which makes a leaf come out as `1`.

**Complexity:** `O(n)` time, each node is visited once. `O(h)` extra space for the call stack.

**Common mistakes:** returning `1` for an empty tree, which counts a missing child as a node. Counting edges instead of nodes: this problem counts the root as depth `1`.

</details>
