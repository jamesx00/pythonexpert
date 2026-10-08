---
lesson_name: Binary Tree Maximum Path Sum
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

### Binary Tree Maximum Path Sum

A "path" through a binary tree is any sequence of nodes where consecutive nodes are connected by an edge, and no node appears more than once; the path does not have to pass through the root and does not have to end at a leaf.

Write a function `max_path_sum(root)` that returns the largest possible sum of node values along any such path. Values can be negative, so sometimes the best path is a single node. For example, in the tree built from `[-10, 9, 20, None, None, 15, 7]`, the best path is `15 -> 20 -> 7`, giving a sum of `42` — better than routing through the negative root.

---

### Tests

<ul>
<li id="test-1"><code>max_path_sum(build_tree([-10, 9, 20, None, None, 15, 7]))</code> should return <code>42</code></li>
<li id="test-2"><code>max_path_sum(build_tree([1, 2, 3]))</code> should return <code>6</code></li>
<li id="test-3"><code>max_path_sum(build_tree([-3]))</code> should return <code>-3</code></li>
<li id="test-4"><code>max_path_sum(build_tree([2, -1]))</code> should return <code>2</code></li>
<li id="test-5"><code>max_path_sum(build_tree([-1, -2, -3]))</code> should return <code>-1</code></li>
<li id="test-6"><code>max_path_sum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]))</code> should return <code>48</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def max_path_sum(root):
    best = [float('-inf')]

    def dfs(node):
        if node is None:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        best[0] = max(best[0], node.val + left + right)
        return node.val + max(left, right)

    dfs(root)
    return best[0]
```

</details>
