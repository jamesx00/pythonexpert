---
lesson_name: "Warm-up: Minimum Depth with BFS"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "If you explore the tree one level at a time, which leaf do you reach first?"
  - "Use *BFS level by level* from *Trees Basics*: a `deque` of `(node, depth)` pairs starting with `(root, 1)`. Pop from the left; return the depth of the first leaf; otherwise push the children with `depth + 1`."
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

### Warm-up: Minimum Depth with BFS

Write a function `min_depth(root)` that returns the number of nodes on the **shortest** path from the root down to the nearest **leaf** (a node with no children). An empty tree has depth `0`.

For example, the tree `[3, 9, 20, None, None, 15, 7]` has minimum depth `2` (the path `3 -> 9`).

Solve it with **breadth-first search**. BFS visits the tree level by level, so the first leaf it reaches is the closest one, and you can stop right there instead of exploring the whole tree.

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

**Brute force:** a DFS that finds the depth of every leaf and takes the smallest. It's `O(n)` too, but it always explores the whole tree, even when a leaf sits right below the root.

**Bottleneck:** DFS can't know a leaf is the closest until it has seen all the others.

**Optimal idea:** BFS hands out nodes in order of depth, so the first leaf it pops is the shallowest one, and you can stop there.

**Why it's correct:** every node at depth `d` is popped before any node at depth `d + 1`. So when the first leaf is popped, no leaf at a smaller depth is left, and its depth is the minimum.

**Complexity:** `O(n)` time in the worst case, but it stops at the first leaf. `O(n)` extra space for the queue, which can hold a whole level.

**Common mistakes:** treating a node with one missing child as a leaf. The DFS version `1 + min(left, right)` has the same bug: the missing side reports depth `0` even though no path ends there. Using `list.pop(0)` instead of `deque.popleft()`, which costs `O(n)` per pop.

</details>
