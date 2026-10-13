---
lesson_name: Balanced Binary Tree
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(h)
hints:
  - "To check one node you need the heights of its two subtrees. Can the same recursion that computes heights also report \"not balanced\"?"
  - "Use *Return one thing, track another* from *Trees Basics*: return the height, or a special value like `-1` once any node below is unbalanced."
  - "Template: `height(node)`: `0` for `None`; get `left` and `right`, returning `-1` if either is `-1` or `abs(left - right) > 1`; otherwise return `1 + max(left, right)`. Answer: `height(root) != -1`."
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

### Balanced Binary Tree

Write a function `is_balanced(root)` that returns `True` if the tree is height-balanced, meaning that for every node, the heights of its left and right subtrees differ by at most `1`. An empty tree counts as balanced.

For example, the tree built from `[3, 9, 20, None, None, 15, 7]` is balanced because at every node the two subtree heights never differ by more than one. A tree like `[1, 2, 2, 3, 3, None, None, 4, 4]`, where one branch keeps growing deeper than its sibling, is not.

---

### Tests

<ul>
<li id="test-1"><code>is_balanced(build_tree([3, 9, 20, None, None, 15, 7]))</code> should return <code>True</code></li>
<li id="test-2"><code>is_balanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4]))</code> should return <code>False</code></li>
<li id="test-3"><code>is_balanced(build_tree([]))</code> should return <code>True</code></li>
<li id="test-4"><code>is_balanced(build_tree([1]))</code> should return <code>True</code></li>
<li id="test-5"><code>is_balanced(build_tree([1, 2, None, 3, None, 4]))</code> should return <code>False</code></li>
<li id="test-6"><code>is_balanced(build_tree([1, 2, 3]))</code> should return <code>True</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1
```

**Brute force:** at every node, call a separate `height` function on both children and compare. Each call walks a whole subtree, so on a deep tree that's `O(n^2)` time.

**Bottleneck:** the heights are recomputed for every ancestor.

**Optimal idea:** compute heights bottom-up once, and let `-1` mean "something below is unbalanced". Once a `-1` appears, it is passed straight up.

**Why it's correct:** a tree is balanced when every node is. The recursion checks the height difference at every node as it returns, and any failure turns into `-1`, which every ancestor passes up unchanged. If no node fails, the root gets a real height.

**Complexity:** `O(n)` time, each node is visited once (and the walk stops early on the first failure). `O(h)` extra space for the call stack.

**Common mistakes:** only comparing the root's two subtree heights. `[1, 2, 2, 3, None, None, 3, 4, None, None, 4]` has subtrees of the same height under the root but is unbalanced below it. Forgetting to pass `-1` up, so it gets mixed into `1 + max(...)` like a real height.

</details>
