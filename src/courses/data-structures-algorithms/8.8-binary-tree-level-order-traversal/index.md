---
lesson_name: Binary Tree Level Order Traversal
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

### Binary Tree Level Order Traversal

Write a function `level_order(root)` that returns a list of lists: one inner list per depth level of the tree, each holding that level's node values left to right, ordered from the root's level down to the deepest level. An empty tree should produce an empty list.

For example, the tree built from `[3, 9, 20, None, None, 15, 7]` has root level `[3]`, then `[9, 20]`, then `[15, 7]`, so `level_order` should return `[[3], [9, 20], [15, 7]]`.

---

### Tests

<ul>
<li id="test-1"><code>level_order(build_tree([3, 9, 20, None, None, 15, 7]))</code> should return <code>[[3], [9, 20], [15, 7]]</code></li>
<li id="test-2"><code>level_order(build_tree([]))</code> should return <code>[]</code></li>
<li id="test-3"><code>level_order(build_tree([1]))</code> should return <code>[[1]]</code></li>
<li id="test-4"><code>level_order(build_tree([1, 2, 3, 4, 5, 6, 7]))</code> should return <code>[[1], [2, 3], [4, 5, 6, 7]]</code></li>
<li id="test-5"><code>level_order(build_tree([1, None, 2, None, 3]))</code> should return <code>[[1], [2], [3]]</code></li>
<li id="test-6"><code>level_order(build_tree([1, 2, None, 3]))</code> should return <code>[[1], [2], [3]]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def level_order(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        level = []
        next_queue = []
        for node in queue:
            level.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        result.append(level)
        queue = next_queue
    return result
```

</details>
