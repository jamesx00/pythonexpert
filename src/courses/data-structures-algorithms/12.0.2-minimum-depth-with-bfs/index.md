---
lesson_name: "Warm-up: Minimum Depth with BFS"
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

### Warm-up: Minimum Depth with BFS

Write a function `min_depth(root)` that returns the number of nodes on the **shortest** path from the root down to the nearest **leaf** (a node with no children). An empty tree has depth `0`.

For example, the tree `[3, 9, 20, None, None, 15, 7]` has minimum depth `2` (the path `3 -> 9`).

Solve it with **breadth-first search**. BFS visits the tree level by level, so the first leaf it reaches is the closest one, and you can stop right there instead of exploring the whole tree.

**Hint:** keep a `deque` of `(node, depth)` pairs, starting with `(root, 1)`. Pop from the left; if the node is a leaf, return its depth; otherwise push its children with `depth + 1`.

---

### Tests

<ul>
<li id="test-1"><code>min_depth([3, 9, 20, None, None, 15, 7])</code> should return <code>2</code></li>
<li id="test-2"><code>min_depth([])</code> should return <code>0</code></li>
<li id="test-3"><code>min_depth([1])</code> should return <code>1</code></li>
<li id="test-4"><code>min_depth([2, None, 3, None, 4, None, 5, None, 6])</code> should return <code>5</code></li>
<li id="test-5"><code>min_depth([1, 2, 3, 4, 5])</code> should return <code>2</code></li>
<li id="test-6"><code>min_depth([1, 2, 3, 4, None, None, 5, 6])</code> should return <code>3</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import deque

def min_depth(root):
    if not root:
        return 0
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
```

The queue hands out nodes in order of depth, so the first leaf popped is the shallowest. A DFS would have to explore every branch to be sure. Watch out for a common DFS bug: `1 + min(left, right)` is wrong when one child is missing, because the missing side reports depth `0` even though it isn't a leaf path. BFS avoids that entirely.

</details>
