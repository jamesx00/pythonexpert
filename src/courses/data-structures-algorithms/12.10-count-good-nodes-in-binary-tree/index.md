---
lesson_name: Count Good Nodes in Binary Tree
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(h)
hints:
  - "To decide if one node is good, you only need one number about the path above it. Which one?"
  - "Use *Passing info down* from *Trees Basics*: pass the largest value seen so far on the path into each recursive call."
  - "Template: `dfs(node, max_so_far)`: return for `None`; if `node.val >= max_so_far`, count it and set `max_so_far = node.val`; recurse into both children with `max_so_far`. Start with `dfs(root, float('-inf'))`."
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

### Count Good Nodes in Binary Tree

A node in a binary tree is called "good" if, looking at the path from the root down to that node, no earlier node on the path has a value greater than the node's own value (the root itself is always good, since its path has nothing before it).

Write a function `good_nodes(root)` that returns how many good nodes the tree has. For example, in the tree built from `[3, 1, 4, 3, None, 1, 5]`, the root `3` is good, the left child `1` is not good (3 > 1), the right child `4` is good, and so on — counting carefully across the whole tree gives `4` good nodes.

---

### Tests

<ul>
<li id="test-1"><code>good_nodes(build_tree([3, 1, 4, 3, None, 1, 5]))</code> should return <code>4</code></li>
<li id="test-2"><code>good_nodes(build_tree([3, 3, None, 4, 2]))</code> should return <code>3</code></li>
<li id="test-3"><code>good_nodes(build_tree([1]))</code> should return <code>1</code></li>
<li id="test-4"><code>good_nodes(build_tree([]))</code> should return <code>0</code></li>
<li id="test-5"><code>good_nodes(build_tree([5, 4, 3, 2, 1]))</code> should return <code>1</code></li>
<li id="test-6"><code>good_nodes(build_tree([1, 2, 3, 4, 5, 6, 7]))</code> should return <code>7</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def good_nodes(root):
    count = [0]

    def dfs(node, max_so_far):
        if node is None:
            return
        if node.val >= max_so_far:
            count[0] += 1
            max_so_far = node.val
        dfs(node.left, max_so_far)
        dfs(node.right, max_so_far)

    dfs(root, float('-inf'))
    return count[0]
```

**Brute force:** for every node, walk the path from the root down to it and check that nothing on it is bigger. With parent pointers or stored paths that's `O(n * h)` time: `O(n^2)` for a chain.

**Bottleneck:** paths to sibling nodes share all their earlier nodes, so their maximum is computed again and again.

**Optimal idea:** carry the maximum of the path so far down the recursion. Each node compares itself to one number and passes the updated maximum to its children.

**Why it's correct:** when `dfs` reaches a node, `max_so_far` is the largest value on the path from the root to its parent. The node is good exactly when no earlier value is bigger, that is when `node.val >= max_so_far`. Starting from minus infinity makes the root good.

**Complexity:** `O(n)` time, each node is visited once. `O(h)` extra space for the call stack.

**Common mistakes:** using `>` instead of `>=`, which says a node equal to the path maximum isn't good (the `3` under `3 -> 1` in the example is good). Storing the maximum in a shared variable, so one branch's update leaks into its sibling.

</details>
