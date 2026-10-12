---
lesson_name: Diameter of Binary Tree
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(h)
hints:
  - "Every path has one highest node. If the path bends at that node, how long is it, in terms of the heights of its two subtrees?"
  - "Use *Return one thing, track another* from *Trees Basics*: the recursion returns a node's height to its parent, and on the way updates the best `left + right` seen so far."
  - "Template: `best = [0]`. `height(node)`: return `0` for `None`; `left, right = height(node.left), height(node.right)`; `best[0] = max(best[0], left + right)`; return `1 + max(left, right)`. Call `height(root)` and return `best[0]`."
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

### Diameter of Binary Tree

Write a function `diameter_of_binary_tree(root)` that returns the length (in edges, not nodes) of the longest path between any two nodes in the tree. That path may or may not pass through the root.

For example, in the tree built from `[1, 2, 3, 4, 5]`, the longest path runs `4 -> 2 -> 1 -> 3` or `5 -> 2 -> 1 -> 3`, which crosses 3 edges, so `diameter_of_binary_tree` should return `3`.

---

### Tests

<ul>
<li id="test-1"><code>diameter_of_binary_tree(build_tree([1, 2, 3, 4, 5]))</code> should return <code>3</code></li>
<li id="test-2"><code>diameter_of_binary_tree(build_tree([1, 2]))</code> should return <code>1</code></li>
<li id="test-3"><code>diameter_of_binary_tree(build_tree([]))</code> should return <code>0</code></li>
<li id="test-4"><code>diameter_of_binary_tree(build_tree([1]))</code> should return <code>0</code></li>
<li id="test-5"><code>diameter_of_binary_tree(build_tree([1, 2, None, 3, None, 4, None, 5]))</code> should return <code>4</code></li>
<li id="test-6"><code>diameter_of_binary_tree(build_tree([1, None, 2, None, 3]))</code> should return <code>2</code></li>
<li id="test-7">Performance: a 66,335-node tree (an 800-node chain above a 65,535-node perfect tree), within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def diameter_of_binary_tree(root):
    best = [0]

    def height(node):
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        best[0] = max(best[0], left + right)
        return 1 + max(left, right)

    height(root)
    return best[0]
```

**Brute force:** for every node, compute the heights of its two subtrees with a separate `height` function and take the largest `left + right`. Each `height` call walks a whole subtree, so on a deep tree that's `O(n^2)` time.

**Bottleneck:** the same subtree heights are computed again for every ancestor.

**Optimal idea:** compute every height once, bottom-up. The recursion has to return the height to the parent, so record the best diameter on the side as it goes.

**Why it's correct:** the longest path has a highest node. Below it, the path goes down into the left subtree and down into the right subtree as far as possible, so its length is `height(left) + height(right)`. The recursion checks this sum at every node, so it sees the highest node of the best path.

**Complexity:** `O(n)` time, each node is visited once. `O(h)` extra space for the call stack.

**Common mistakes:** returning the diameter from the recursion instead of the height: the parent needs the height. Only checking the path through the root, which misses paths that sit inside one subtree. Counting nodes instead of edges.

</details>
