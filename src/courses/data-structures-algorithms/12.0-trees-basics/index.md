---
lesson_name: Trees Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Trees
---

## Why This Pattern Matters &#x1F4A1;

A binary tree is a linked list where each node has **two** next pointers, `left` and `right`. Almost every tree problem comes down to choosing a traversal and deciding **what each node returns to its parent**.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Spotting It &#x1F50D;

- Depth, height, diameter, balance, path sums: **DFS that returns a value upward**.
- "Level by level", "right side view", "minimum depth": **BFS with a queue**.
- **BST** (left < node < right): use the ordering to skip half the tree, and remember that in-order traversal visits values in sorted order.

## Core Building Blocks &#x1F9F1;

### Recursive DFS: trust the recursion

Assume the recursive call already works for the children, then combine their answers:

```python
def max_depth(root):
    if not root:              # base case: empty tree
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

Ask yourself: *"If I knew the answer for my left and right subtrees, how would I compute mine?"*

### Return one thing, track another

Some problems need a value passed **up** that differs from the final answer. Keep the answer in an outer variable:

```python
def diameter(root):
    best = 0
    def height(node):
        nonlocal best
        if not node:
            return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)     # answer: path through this node
        return 1 + max(l, r)        # return: height for the parent
    height(root)
    return best
```

*Max Path Sum* and *Balanced Binary Tree* use the same shape.

### Passing info down

Use arguments to pass context from parent to child, like valid bounds or the max value seen so far:

```python
def is_valid_bst(node, low=float("-inf"), high=float("inf")):
    if not node:
        return True
    if not (low < node.val < high):
        return False
    return (is_valid_bst(node.left, low, node.val) and
            is_valid_bst(node.right, node.val, high))
```

### BFS level by level

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):     # exactly this level's nodes
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

## Tips & Gotchas &#x1F4CC;

- **Base case first:** `if not root: return ...`. Pick the return value carefully (`0`, `True`, `None`, `float("-inf")`).
- **Pre/in/post-order** = do the work before, between, or after the recursive calls. Post-order is the usual choice when the parent needs the children's results.
- **BST checks need bounds**, not just a parent-child comparison. A node deep in the left subtree must still be less than the root.
- **Kth smallest in a BST** = in-order traversal, stop at the k-th visit.
- **LCA in a BST:** if both values are smaller, go left; if both bigger, go right; otherwise you're at the split, which is the answer.
- **Use `nonlocal`** (or a one-element list) to update an outer variable from a nested function.
- **Recursion depth:** Python's default limit is ~1000. A very skewed tree can hit it, so use an explicit stack in that case.
- Time is almost always `O(n)` (visit each node once). Space is `O(h)` for the recursion, where `h` is the tree height.
