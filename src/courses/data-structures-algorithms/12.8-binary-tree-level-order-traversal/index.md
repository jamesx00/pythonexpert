---
lesson_name: Binary Tree Level Order Traversal
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "If you had all the nodes of one level in a list, how would you get all the nodes of the next level?"
  - "Use *BFS level by level* from *Trees Basics*: keep the current level in a queue, read its values, and collect its children as the next level."
  - "Template: if `root is None`, return `[]`. `queue = [root]`. While `queue`: append `[node.val for node in queue]` to the result, then set `queue` to the non-`None` children of those nodes, left to right."
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

**Brute force:** a DFS that passes the depth down and appends each value to `result[depth]`. That's also `O(n)` and works, since a preorder walk visits each level left to right. It's the BFS shape that most later problems build on, though.

**Key idea:** process the tree one level at a time. The children of one level, in order, are exactly the next level.

**Why it's correct:** the root is level 0 on its own. If `queue` holds level `d` left to right, then walking it left to right and collecting each node's left child and then right child gives level `d + 1` left to right. Each round adds one level to the result.

**Complexity:** `O(n)` time, each node is added and read once. `O(n)` extra space for the widest level and the result.

**Common mistakes:** using a single queue without separating levels, which gives one flat list. Pushing `None` children into the queue and then reading `node.val` on them. Returning `[[]]` instead of `[]` for an empty tree.

</details>
