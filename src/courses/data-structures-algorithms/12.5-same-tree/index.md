---
lesson_name: Same Tree
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(h)
hints:
  - "When are two empty trees the same? When is an empty tree the same as a non-empty one?"
  - "Use *Recursive DFS: trust the recursion* from *Trees Basics*: two trees are the same if their roots match and both pairs of subtrees are the same."
  - "Template: both `None`: `True`. One `None`: `False`. Otherwise return `p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)`."
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

**Brute force:** serialize both trees, for example with a preorder walk that writes `#` for missing children, and compare the strings. It's `O(n)` time too, but builds two strings of size `O(n)` and reads both trees to the end even when the roots already differ.

**Bottleneck:** the strings are only a detour for comparing the trees node by node.

**Optimal idea:** walk both trees at the same time and compare matching nodes, stopping at the first difference.

**Why it's correct:** two empty trees are the same, and an empty and a non-empty tree aren't. For two non-empty trees, being the same means the same root value, the same left subtree and the same right subtree, which is exactly what the recursion checks. `and` stops at the first `False`.

**Complexity:** `O(n)` time, where `n` is the size of the smaller tree. `O(h)` extra space for the call stack.

**Common mistakes:** comparing only values, for example `preorder(p) == preorder(q)`, which treats `[1, 2]` and `[1, None, 2]` as the same. Checking `p.val` before checking for `None`.

</details>
