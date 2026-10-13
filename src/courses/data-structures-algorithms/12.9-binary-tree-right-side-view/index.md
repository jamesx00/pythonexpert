---
lesson_name: Binary Tree Right Side View
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "Is the visible node on each level always a right child? What about a level where the rightmost node is a left child?"
  - "Use *BFS level by level* from *Trees Basics*: walk the tree one level at a time and keep the last node of each level."
  - "Template: same loop as level order traversal. For each level, append the value of the last node in it, then build the next level from the children."
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

### Binary Tree Right Side View

Write a function `right_side_view(root)` that returns the list of node values you would see if you stood to the right of the tree and looked at it edge-on — one value per depth level, taken from the rightmost node at that level, ordered top to bottom.

For example, the tree built from `[1, 2, 3, None, 5, None, 4]` looks like `1` on top, `2` and `3` below it, then `5` under `2` and `4` under `3`. Standing on the right you'd see `1`, then `3`, then `4`, so `right_side_view` should return `[1, 3, 4]`.

---

### Tests

<ul>
<li id="test-1"><code>right_side_view(build_tree([1, 2, 3, None, 5, None, 4]))</code> should return <code>[1, 3, 4]</code></li>
<li id="test-2"><code>right_side_view(build_tree([1, None, 3]))</code> should return <code>[1, 3]</code></li>
<li id="test-3"><code>right_side_view(build_tree([]))</code> should return <code>[]</code></li>
<li id="test-4"><code>right_side_view(build_tree([1]))</code> should return <code>[1]</code></li>
<li id="test-5"><code>right_side_view(build_tree([1, 2, 3, 4]))</code> should return <code>[1, 3, 4]</code></li>
<li id="test-6"><code>right_side_view(build_tree([1, 2, 3, 4, None, None, 5]))</code> should return <code>[1, 3, 5]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def right_side_view(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        next_queue = []
        for index, node in enumerate(queue):
            if index == len(queue) - 1:
                result.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
    return result
```

**Brute force:** follow `.right` pointers down from the root. It's `O(h)`, but wrong: in `[1, 2, 3, 4]` the bottom level's only node, `4`, hangs off the left side and is still visible.

**Key idea:** the visible node on a level is simply the rightmost node on that level, whichever side of its parent it hangs from. BFS gives you each level in order.

**Why it's correct:** each round of the loop has exactly one level in `queue`, left to right, so its last node is the rightmost one, which is what you see from the right. One value is taken per level, top to bottom.

**Complexity:** `O(n)` time, each node is visited once. `O(n)` extra space for the widest level.

**Common mistakes:** only following right children, as above. Taking the first node of each level instead of the last (that's the left side view). A DFS version also works if it visits right before left and records the first node seen at each new depth.

</details>
