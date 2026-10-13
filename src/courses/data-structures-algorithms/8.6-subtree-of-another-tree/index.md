---
lesson_name: Subtree of Another Tree
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(m * n)
  space: O(h)
hints:
  - "If you already had `is_same_tree`, which nodes of `root` would you call it on?"
  - "Use *Recursive DFS: trust the recursion* from *Trees Basics* twice: a `same(a, b)` check, and a walk over `root` that tries `same(node, sub_root)` at every node."
  - "Template: if `root is None`, return `False`. If `same(root, sub_root)`, return `True`. Otherwise return `is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)`."
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

### Subtree of Another Tree

Write a function `is_subtree(root, sub_root)` that returns `True` if the tree rooted at `sub_root` matches, node-for-node, some node's entire subtree inside `root` (including possibly `root` itself), and `False` otherwise.

For example, if `root` is built from `[3, 4, 5, 1, 2]` and `sub_root` is built from `[4, 1, 2]`, then the left branch of `root` starting at the node `4` is an exact match for `sub_root`, so the answer is `True`. If `sub_root` were `[4, 1]` instead, it wouldn't line up with any full subtree of `root`, so the answer would be `False`.

---

### Tests

<ul>
<li id="test-1"><code>is_subtree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2]))</code> should return <code>True</code></li>
<li id="test-2"><code>is_subtree(build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]), build_tree([4, 1, 2]))</code> should return <code>False</code></li>
<li id="test-3"><code>is_subtree(build_tree([1, 2, 3]), build_tree([1, 2, 3]))</code> should return <code>True</code></li>
<li id="test-4"><code>is_subtree(build_tree([1, 2, 3]), build_tree([2]))</code> should return <code>True</code></li>
<li id="test-5"><code>is_subtree(build_tree([1, 2, 3]), build_tree([4]))</code> should return <code>False</code></li>
<li id="test-6"><code>is_subtree(build_tree([]), build_tree([1]))</code> should return <code>False</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_subtree(root, sub_root):
    def same(a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

    if root is None:
        return False
    if same(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)
```

**Brute force:** this is it. For each of the `m` nodes of `root`, compare its subtree with `sub_root`, which costs up to `O(n)` for `n` nodes in `sub_root`. That's `O(m * n)` in the worst case, which is the target here.

**Faster option:** serialize both trees with markers for missing children and search for one string inside the other, or hash every subtree. That's `O(m + n)` with a linear-time string search, but it's harder to get right.

**Key idea:** "matches some node's entire subtree" splits into two jobs: walking `root`, and comparing two trees. Write each job as its own small recursion.

**Why it's correct:** `sub_root` is a subtree of `root` exactly when some node of `root` is the root of an identical tree. The walk tries every node, and `same` compares the whole tree below it, so a match that only covers the top of a subtree is rejected.

**Complexity:** `O(m * n)` time in the worst case, though `same` usually stops after a few nodes. `O(h)` extra space for the call stack.

**Common mistakes:** checking only that the values of `sub_root` appear in `root` in the same order, which accepts `[4, 1]` inside `[3, 4, 5, 1, 2]`: the node `4` there also has a right child `2`. Returning `False` when the first `same` fails, instead of trying the children.

</details>
